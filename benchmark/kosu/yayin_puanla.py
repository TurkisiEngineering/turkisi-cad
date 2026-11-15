"""Faz Yayın puanlayıcısı (lead, 2026-11-11; v2 havuz).

Yollar (bu repodaki referans sürüm): TCAD_IS_KOKU iş kökü (kos.py ile aynı), TCAD_OLC ölçüm betiği (varsayılan
../degerlendirme/olc/olc.py), TCAD_KALIBRASYON kalibrasyon ölçümleri. Paket başına gizli klasör
<IS_KOKU>/paketler/<P#>/_gizli/: hedef.json (gizli ölçüm listesi) ve kaynak.json ({"orijinal_step": "<cevap anahtarı
STEP yolu>"}). İkisi de yapımcıya hiç gösterilmez ve bu repoda yoktur.

kayit\\kosu_listesi.csv'de faz=Y ve durumu tamam / tavan / cokme olan, sonuc\\yayin_puan.csv'de henüz olmayan her koşuyu
olc.py ile ölçer. Ölçüm klasörü puan\\<run_id>\\. §6 (CAD kalitesi, 15) puanlayıcı elinde; burada §1-§5 / 85.

v2 (canlı yayında hızlı puan): yalnız yayın puanlaması için tek-olc kuralı gevşetildi.
- En çok ISCI (3) olc.py aynı anda; başka (yabancı) olc.py süreçleri de yuva sayılır.
- Yeni ölçüm yalnız boş bellek >= 4 GB iken başlar (psutil, o an). Boş bellek bir kez < 2 GB görülürse havuz 2'ye iner.
- Ucuz koşu önce: paketin bilinen öz-kontrol süresi, yoksa gövde / yüz sayısından tahmin.
- Tek kopya: kayit\\yayin_puanla.pid kilidi; canlı başka kopya varsa çıkar.
- yayin_puan.csv'ye yalnız ana döngü yazar (işçiler alt süreç), eşzamanlı yazma yok.
- olc.py değişmedi (boolean bellek koruması aynı).

Kullanım: python -I yayin_puanla.py [--bir-kez]   (varsayılan: 20 sn'de bir yoklayan sürekli döngü)
"""
import csv, json, os, subprocess, sys, time
from pathlib import Path
import psutil

ISCI = 3
BOS_GB_BASLA = 4.0
BOS_GB_DUSUR = 2.0
ARAC = Path(__file__).resolve().parent                       # benchmark/kosu/
KOK = Path(os.environ.get("TCAD_IS_KOKU", ARAC / "_is")).resolve()
PID = KOK / "kayit" / "yayin_puanla.pid"
LISTE = KOK / "kayit" / "kosu_listesi.csv"
CIKTI = KOK / "sonuc" / "yayin_puan.csv"
OLC = Path(os.environ.get("TCAD_OLC", ARAC.parent / "degerlendirme" / "olc" / "olc.py"))
KALIBRASYON = Path(os.environ.get("TCAD_KALIBRASYON", KOK / "kalibrasyon"))
ALAN = ["run_id", "config", "paket", "durum_kosu", "puan_85", "geometri", "tamlik", "montaj", "ozellik", "resim",
        "azami_1_5", "olcum_sure_s", "zaman", "not", "iptal", "montajli"]
# Panelin "Sıfırla" düğmesi yayından önceki deneme koşularını buraya yazar (sekmeyle: run_id, config, paket, durum, neden).
# Bu koşular puanlanmaz; daha önce puanlandıysa satırı silinmez, "iptal" sütunu işaretlenir.
IPTAL = KOK / "kayit" / "yayin_iptal.txt"
BEKLEYEN = KOK / "kayit" / "yayin_bekleyen.txt"   # puanlanmayı bekleyen yayın koşuları (öncelik kapısı)


def iptaller():
    if not IPTAL.exists():
        return set()
    return {s.split("\t")[0].strip() for s in IPTAL.read_text(encoding="utf-8", errors="replace").splitlines()
            if s.strip()}


def iptal_isle():
    """Puanlanmış ama sonradan iptal edilen satırları işaretler (satır silinmez; dosya aynı satırlarla yeniden yazılır)."""
    ip = iptaller()
    if not ip or not CIKTI.exists():
        return
    with CIKTI.open(encoding="utf-8") as f:
        satirlar = list(csv.DictReader(f))
    degisti = False
    for r in satirlar:
        if r["run_id"] in ip and r.get("iptal") != "1":
            r["iptal"] = "1"; degisti = True
    if degisti:
        gecici = CIKTI.with_suffix(".csv.yeni")
        with gecici.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=ALAN, extrasaction="ignore")
            w.writeheader()
            for r in satirlar:
                w.writerow({k: r.get(k, "") for k in ALAN})
        gecici.replace(CIKTI)


def yabanci_olc(kendi_pidler):
    """Bu puanlayıcının başlatmadığı, üst düzey olc.py süreçleri (--_ic iç süreçleri sayılmaz)."""
    n = 0
    for p in psutil.process_iter(["pid", "cmdline", "name"]):
        try:
            if not (p.info["name"] or "").lower().startswith("python"):
                continue
            c = " ".join(p.info["cmdline"] or [])
        except Exception:
            continue
        if "olc.py" in c and "--_ic" not in c and "yayin_puanla" not in c and p.info["pid"] not in kendi_pidler:
            n += 1
    return n


def bos_gb():
    return psutil.virtual_memory().available / 2 ** 30


def maliyet(paket):
    """Beklenen ölçüm süresi (s): paketin öz-kontrol / kalibrasyon süresi, yoksa gövde ve yüz sayısından kaba tahmin."""
    g = KOK / "paketler" / paket / "_gizli"
    adaylar = [g / "is" / "olc_kendi" / "olcum.json"] + sorted(KALIBRASYON.glob(f"k2*_{paket}/olcum.json"))
    if paket == "P7":
        adaylar.append(KALIBRASYON / "k2c_pres_P7" / "olcum.json")
    for a in adaylar:
        try:
            return float(json.loads(a.read_text(encoding="utf-8"))["sure_s"])
        except Exception:
            pass
    try:
        h = json.loads((g / "hedef.json").read_text(encoding="utf-8"))
        return 30 + 20 * len(h["govdeler"]) + 0.5 * sum(b.get("yuz_sayisi", 0) for b in h["govdeler"])
    except Exception:
        return 600.0


def puanlananlar():
    if not CIKTI.exists():
        return set()
    with CIKTI.open(encoding="utf-8") as f:
        return {r["run_id"] for r in csv.DictReader(f)}


def yaz(satir):
    yeni = not CIKTI.exists()
    CIKTI.parent.mkdir(parents=True, exist_ok=True)
    with CIKTI.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ALAN)
        if yeni:
            w.writeheader()
        w.writerow(satir)


def bekleyenler():
    if not LISTE.exists():
        return []
    bitti = puanlananlar() | iptaller()
    with LISTE.open(encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("faz") == "Y" and r.get("durum") in ("tamam", "tavan", "cokme")
                and r["run_id"] not in bitti]


def temel_satir(r):
    return dict(run_id=r["run_id"], config=r["config"], paket=r["parca"], durum_kosu=r["durum"],
                montajli=montajli(r["parca"]), zaman=time.strftime("%Y-%m-%dT%H:%M:%S"))


def baslat(r):
    """final.step yoksa satırı hemen yazar ve None döner; yoksa olc.py alt sürecini başlatır (Popen, log dosyası)."""
    run, paket = r["run_id"], r["parca"]
    final = KOK / "kosular" / run / "teslim" / "final.step"
    gizli = KOK / "paketler" / paket / "_gizli"
    if not final.exists():
        yaz(dict(temel_satir(r), puan_85=0, geometri=0, tamlik=0, montaj=0, ozellik=0, resim=0,
                 **{"not": "final.step yok (RUBRIK §9: §1-§5 = 0; §6 kaynaktan)"}))
        return None
    orij = json.loads((gizli / "kaynak.json").read_text(encoding="utf-8"))["orijinal_step"]
    out = KOK / "puan" / run
    out.mkdir(parents=True, exist_ok=True)
    log = (out / "olc.log").open("w", encoding="utf-8")
    p = subprocess.Popen([sys.executable, "-u", str(OLC), orij, str(final), "--gizli", str(gizli), "--out", str(out),
                          "--teslim", str(final.parent)], stdout=log, stderr=subprocess.STDOUT)
    return p, log


def bitir(r, p):
    out = KOK / "puan" / r["run_id"]
    temel = temel_satir(r)
    try:
        d = json.loads((out / "olcum.json").read_text(encoding="utf-8"))
        a = d["alt_puanlar"]

        def s(k):  # alt puan ya sayı ya {"toplam": ...}
            v = a[k]
            return round(float(v["toplam"] if isinstance(v, dict) else v), 2)
        yaz(dict(temel, puan_85=s("toplam_1_5"), geometri=s("geometri"), tamlik=s("tamlik"), montaj=s("montaj"),
                 ozellik=s("ozellik"), resim=s("resim"), azami_1_5=a.get("azami_1_5"),
                 olcum_sure_s=round(d.get("sure_s", 0)),
                 **{"not": f"olc çıkış {p.returncode}" if p.returncode else ""}))
    except Exception as e:
        yaz(dict(temel, **{"not": f"olcum.json okunamadı (çıkış {p.returncode}): {e}"[:200]}))


def montajli(paket):
    """1 = orijinal birden fazla gövdeli (montaj, §3 puanlanır); 0 = tek gövde (§3 → §1). Kaynak: gizli hedef.json."""
    try:
        h = json.loads((KOK / "paketler" / paket / "_gizli" / "hedef.json").read_text(encoding="utf-8"))
        return 1 if len(h["govdeler"]) > 1 else 0
    except Exception:
        return ""


def onar():
    """Puanı boş kalmış ama olcum.json'u olan satırları (yayın günü yaşanan okuma hatası) yeniden ölçmeden doldurur."""
    if not CIKTI.exists():
        return
    with CIKTI.open(encoding="utf-8") as f:
        satirlar = list(csv.DictReader(f))
    degisti = False
    for r in satirlar:
        oj = KOK / "puan" / r["run_id"] / "olcum.json"
        if r.get("montajli") in ("", None):
            r["montajli"] = montajli(r["paket"]); degisti = True
        if r.get("puan_85") in ("", None) and oj.exists():
            a = json.loads(oj.read_text(encoding="utf-8"))["alt_puanlar"]
            for k, ad in (("toplam_1_5", "puan_85"), ("geometri", "geometri"), ("tamlik", "tamlik"),
                          ("montaj", "montaj"), ("ozellik", "ozellik"), ("resim", "resim")):
                v = a[k]
                r[ad] = round(float(v["toplam"] if isinstance(v, dict) else v), 2)
            r["azami_1_5"] = a.get("azami_1_5"); r["not"] = "okuma hatası sonrası olcum.json'dan dolduruldu"
            degisti = True
    if degisti:
        gecici = CIKTI.with_suffix(".csv.yeni")
        with gecici.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=ALAN, extrasaction="ignore")
            w.writeheader()
            for r in satirlar:
                w.writerow({k: r.get(k, "") for k in ALAN})
        gecici.replace(CIKTI)


def kilit_al():
    if PID.exists():
        try:
            eski = int(PID.read_text().strip())
            p = psutil.Process(eski)
            if p.is_running() and "yayin_puanla" in " ".join(p.cmdline()):
                print(time.strftime("%H:%M:%S"), f"başka kopya çalışıyor (pid {eski}), çıkıyorum", flush=True)
                sys.exit(0)
        except (ValueError, psutil.Error):
            pass
    PID.parent.mkdir(parents=True, exist_ok=True)
    PID.write_text(str(os.getpid()))


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    bir_kez = "--bir-kez" in sys.argv
    kilit_al()
    isci = ISCI
    calisan = {}          # run_id -> (r, Popen, logdosyası, başlama)
    en_dusuk = 99.0
    while True:
        onar()
        iptal_isle()
        # biten işçiler: sonucu yaz (tek yazıcı = bu döngü)
        for run in list(calisan):
            r, p, lf, t0 = calisan[run]
            if p.poll() is not None:
                lf.close(); del calisan[run]
                bitir(r, p)
                log("bitti", run, r["parca"], f"{time.time() - t0:.0f} s", f"çıkış {p.returncode}")
        bos = bos_gb(); en_dusuk = min(en_dusuk, bos)
        if bos < BOS_GB_DUSUR and isci > 2:
            isci = 2; log(f"boş bellek {bos:.1f} GB < {BOS_GB_DUSUR} GB: havuz 2 işçiye indi")
        bek = [r for r in bekleyenler() if r["run_id"] not in calisan]
        bek.sort(key=lambda r: maliyet(r["parca"]))
        # Öncelik: yayın puanlaması bekliyorsa spec öz-kontrolü (olc_kendi) başlamaz. Yazarlar bu dosya boş değilse bekler.
        BEKLEYEN.write_text("".join(r["run_id"] + "\n" for r in bek + [c[0] for c in calisan.values()]), encoding="utf-8")
        ip = iptaller()
        for r in bek:
            if r["run_id"] in ip:
                continue
            kendi = {c[1].pid for c in calisan.values()}
            if len(calisan) + yabanci_olc(kendi) >= isci:
                break
            bos = bos_gb()
            if bos < BOS_GB_BASLA:
                log(f"boş bellek {bos:.1f} GB < {BOS_GB_BASLA} GB, yeni ölçüm bekliyor"); break
            sonuc = baslat(r)
            if sonuc is None:
                log("final.step yok, 0 yazıldı", r["run_id"]); continue
            calisan[r["run_id"]] = (r, sonuc[0], sonuc[1], time.time())
            log("puanla", r["run_id"], r["config"], r["parca"], f"tahmin {maliyet(r['parca']):.0f} s",
                f"işçi {len(calisan)}/{isci}", f"boş {bos:.1f} GB")
            time.sleep(15)   # yeni sürecin belleği görünsün
        if bir_kez and not calisan and not [r for r in bekleyenler() if r["run_id"] not in ip]:
            log(f"bir-kez bitti; en düşük boş bellek {en_dusuk:.1f} GB, işçi {isci}")
            BEKLEYEN.write_text("", encoding="utf-8")
            break
        time.sleep(20)


if __name__ == "__main__":
    main()
