"""Agentic CAD Ligi kontrol paneli: yerel sunucu + kuyruk orkestratörü (kendisi token harcamaz).

  python panel_sunucu.py --kuru              -> kuru (demo) mod: ornek/ altındaki akışları hızlı oynatır,
                                                hiçbir CAD aracı ya da yapay zekâ çağrılmaz. Repo'dan hemen çalışır.
  python panel_sunucu.py                     -> gerçek mod: ayar.json'daki koşucuyu ('hazirla' + 'baslat') çağırır.
  python panel_sunucu.py --port 8799 --ayar baska_ayar.json

Sayfalar: http://127.0.0.1:<port>/ (panel), /skor (skor tablosu), /yayin (izleyici sayfası).

Sunucu yalnız kuyruğu yürütür: koşuyu ayar.json'daki komutla başlatır, yapımcının akış dosyasını (JSONL) SALT OKUR,
kilometre taşlarını oradan ve teslim klasöründen çıkarır. Yapımcının teslim\\*.png dışındaki dosyalarını sunmaz.
Bağımlılık: yalnız Python 3.9+ standart kütüphanesi. psutil kuruluysa CPU / RAM göstergeleri ve süreç bulma çalışır.
"""
import argparse, csv, json, os, platform, random, re, shutil, signal, subprocess, sys, threading, time
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path

try:
    import psutil                                   # isteğe bağlı: CPU / RAM göstergesi, yeniden başlatmada süreç bulma
except ImportError:
    psutil = None

PANEL = Path(__file__).resolve().parent
BITTI = {"tamam", "tavan", "cokme", "yardimli", "bilinmiyor"}
CREATE = getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
WINDOWS = os.name == "nt"

# ---------------------------------------------------------------- ayar
AYAR, AYAR_KOK = {}, PANEL
CONFIGLER, ISTASYON, PARCALAR = [], {}, {}
RUN_RE = re.compile(r"^[a-z]\d{6}$")


def is_koku():
    """Koşucunun iş kökü: ayar.json 'is_koku' -> önce ortam değişkeni (kos.py ile aynı: TCAD_IS_KOKU), yoksa varsayılan."""
    ik = AYAR.get("is_koku") or {}
    v = os.environ.get(ik.get("ortam", "")) if ik.get("ortam") else None
    p = Path(os.path.expanduser(v or ik.get("varsayilan", ".")))
    return p if p.is_absolute() else (AYAR_KOK / p).resolve()


def yol(p):
    """ayar.json'daki bir yolu çözer: göreli yollar ayar dosyasının klasörüne göredir; '{IS}' koşucunun iş köküdür."""
    if p in (None, ""):
        return None
    s = str(p)
    if "{IS}" in s:
        s = s.replace("{IS}", str(is_koku()))
    p = Path(os.path.expandvars(os.path.expanduser(s)))
    return p if p.is_absolute() else (AYAR_KOK / p).resolve()


KOSU_LISTESI_SUTUN = ["run_id", "faz", "config", "parca", "gorev", "tekrar", "basla", "bitis", "sure_dk", "token_in", "token_out",
                      "token_cache", "usd", "tool_cagri", "cokme", "durum", "not"]


def liste_oku(yol_):
    """kosu_listesi.csv satırları. Başlık satırı yoksa (kos.py yalnız veri satırı ekler) sütunlar KOSU_LISTESI_SUTUN sırasıdır."""
    with yol_.open(encoding="utf-8", newline="") as f:
        ilk = f.readline()
        f.seek(0)
        basliksiz = not ilk.startswith("run_id,")
        return list(csv.DictReader(f, fieldnames=KOSU_LISTESI_SUTUN if basliksiz else None))


def ayar_yukle(ayar_yolu):
    global AYAR, AYAR_KOK, CONFIGLER, ISTASYON, PARCALAR, RUN_RE
    ayar_yolu = Path(ayar_yolu).resolve()
    AYAR, AYAR_KOK = json.loads(ayar_yolu.read_text(encoding="utf-8")), ayar_yolu.parent
    ISTASYON = {i["kod"]: i for i in AYAR["istasyonlar"]}
    CONFIGLER = [i["kod"] for i in AYAR["istasyonlar"]]
    RUN_RE = re.compile("^" + AYAR.get("run_id_deseni", r"[a-z]\d{6}") + "$")
    with yol(AYAR["parcalar"]).open(encoding="utf-8", newline="") as f:
        PARCALAR = {r["paket"]: r for r in csv.DictReader(f)}


# ---------------------------------------------------------------- ekranda görünmemesi gerekenler
# Yayında ekrana gelen her metin buradan geçer: yapımcının çalışma klasörü './' olur, başka mutlak yollar '~' olur.
GIZLE = [
    (re.compile(r"[A-Za-z]:[\\/]+(?:[^\\/\s\"'`]+[\\/]+)*?kosular[\\/]+[a-z]\d{6}[\\/]*", re.I), "./"),
    (re.compile(r"/(?:[^/\s\"'`]+/)*?kosular/[a-z]\d{6}/?", re.I), "./"),
    (re.compile(r"[A-Za-z]:[\\/]+[^\s\"'`]*"), "~"),
    (re.compile(r"/(?:home|Users|c/Users|mnt/[a-z]/Users)/[^\s\"'`]*", re.I), "~"),
    (re.compile(r"\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b", re.I), "▒▒▒"),
]
# Kendi gizlemen gerekenleri (müşteri adı, satıcı adı, parça numarası biçimi ...) ayar.json'da "gizle": ["regex", ...]


def gizle_kur():
    for d in AYAR.get("gizle", []):
        GIZLE.append((re.compile(d, re.I), "▒▒▒"))


def temiz(s, n=150):
    s = str(s)
    for r, y in GIZLE:
        s = r.sub(y, s)
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def girdi_ozet(g):
    if not isinstance(g, dict):
        return temiz(g)
    for k in ("command", "file_path", "path", "pattern", "description", "code", "script"):
        if k in g:
            return temiz(g[k])
    return temiz(json.dumps(g, ensure_ascii=False))


# ---------------------------------------------------------------- kilometre taşları
KT = [("basladi", "Yapımcı başladı"), ("spec", "Spec okundu"), ("betik", "İlk betik / journal yazıldı"),
      ("kosu", "İlk model koşusu"), ("step", "İlk STEP yazıldı"), ("gorsel", "Görsel üretildi"),
      ("olcum", "Kendi ölçümü"), ("teslim", "Teslim dosyaları tamam"), ("hazir", "TESLIM HAZIR"), ("bitti", "Koşu bitti")]
KOD_UZ = re.compile(r"\.(py|vb|vbs|js|ts|java|cs|bas|swp)\b", re.I)
KOSU_RE = re.compile(r"python[^\n|;&]*\.py\b|run_journal|solidcraft-cli(?:\.exe)?\s+(?!--help|commands)\S|node\s+\S+\.js", re.I)
OLCUM_RE = re.compile(r"import_step|\.volume|bounding_box|GetMassProperties|mass_prop|olcum|ölçüm|measure|hedef tablo", re.I)
TESLIM_DOSYA = ["final.step", "yeniden_kur.md", "parametreler.md", "build_log.md"]


class Akis:
    """Bir koşunun akış dosyasını (Claude Code --output-format stream-json) artımlı okur; salt okuma."""

    def __init__(self, yol_):
        self.yol, self.konum, self.satir = yol_, 0, 0
        self.arac, self.mesaj_id, self.son = 0, set(), []
        self.tok = {"girdi": 0, "cikti": 0, "onbellek": 0}
        self.usd, self.sonuc, self.kt = None, None, {}

    def oku(self, simdi):
        if not self.yol.exists():
            return
        with self.yol.open("rb") as h:
            h.seek(self.konum)
            veri = h.read()
        son_nl = veri.rfind(b"\n")
        if son_nl < 0:
            return
        self.konum += son_nl + 1
        for s in veri[: son_nl + 1].decode("utf-8", "replace").splitlines():
            try:
                d = json.loads(s)
            except Exception:
                continue
            self.satir += 1
            self._isle(d, simdi)

    def _isle(self, d, t):
        tip = d.get("type")
        if tip == "system" and d.get("subtype") == "init":
            self.kt.setdefault("basladi", t)
        elif tip == "assistant":
            m = d.get("message", {})
            mid = m.get("id")
            if mid and mid not in self.mesaj_id:
                self.mesaj_id.add(mid)
                u = m.get("usage", {})
                self.tok["girdi"] += u.get("input_tokens", 0)
                self.tok["cikti"] += u.get("output_tokens", 0)
                self.tok["onbellek"] += u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            for c in m.get("content", []):
                if c.get("type") == "text" and "TESLIM HAZIR" in c.get("text", ""):
                    self.kt.setdefault("hazir", t)
                if c.get("type") != "tool_use":
                    continue
                self.arac += 1
                ad = c.get("name", "?").replace("mcp__", "")
                g = c.get("input") or {}
                ham = json.dumps(g, ensure_ascii=False)
                self.son.append({"t": t, "ad": ad, "ozet": girdi_ozet(g)})
                self.son = self.son[-8:]
                if "spec.md" in ham:
                    self.kt.setdefault("spec", t)
                yaz = (c.get("name") in ("Write", "Edit", "MultiEdit") and KOD_UZ.search(str(g.get("file_path", "")))) or \
                      (c.get("name") == "Bash" and re.search(r"cat\s*>+\s*\S+\.(py|vb|vbs|js|bas)\b|tee\s+\S+\.py", ham))
                if yaz:
                    self.kt.setdefault("betik", t)
                if (c.get("name") == "Bash" and KOSU_RE.search(str(g.get("command", "")))) or \
                   (c.get("name", "").startswith("mcp__") and not re.search(r"status|list|help|get_", c["name"])):
                    if "betik" in self.kt or c.get("name", "").startswith("mcp__"):
                        self.kt.setdefault("kosu", t)
                if "step" in self.kt and OLCUM_RE.search(ham):
                    self.kt.setdefault("olcum", t)
        elif tip == "result":
            self.usd = d.get("total_cost_usd")
            self.sonuc = (d.get("result") or "")[-300:]
            if "TESLIM HAZIR" in self.sonuc:
                self.kt.setdefault("hazir", t)
            self.kt.setdefault("bitti", t)


def teslim_tara(kok, kt):
    """Teslim klasöründen kilometre taşları (dosya zamanı) + PNG listesi."""
    teslim = kok / "teslim"
    pngler = []
    if not kok.exists():
        return pngler
    stepler = [p for p in kok.rglob("*") if p.suffix.lower() in (".step", ".stp") and "girdi" not in p.parts]
    if stepler:
        kt.setdefault("step", datetime.fromtimestamp(min(p.stat().st_mtime for p in stepler)).isoformat(timespec="seconds"))
    if teslim.exists():
        pngler = sorted((p for p in teslim.glob("*.png")), key=lambda p: p.stat().st_mtime)
        if pngler:
            kt.setdefault("gorsel", datetime.fromtimestamp(pngler[0].stat().st_mtime).isoformat(timespec="seconds"))
        if all((teslim / f).exists() for f in TESLIM_DOSYA):
            kt.setdefault("teslim", datetime.fromtimestamp(max((teslim / f).stat().st_mtime for f in TESLIM_DOSYA))
                          .isoformat(timespec="seconds"))
    return [p.name for p in pngler][-6:]


# ---------------------------------------------------------------- skor yardımcıları
GECME_ESIGI = 68.0          # 85'in %80'i: ölçülen kısımda geçme eşiği (skor sayfasında yazılı)
KAT_AZAMI = {"geometri": 50, "tamlik": 10, "montaj": 10, "ozellik": 20, "resim": 5}


def sayi(v):
    try:
        return round(float(str(v).replace(",", ".")), 4) if str(v).strip() not in ("", "None") else None
    except (TypeError, ValueError):
        return None


def montajli_mi(p):
    """'montajli' sütunu (1 montaj, 0 tek gövde); boşsa yedek tahmin: geometri > 40 ise tek gövde."""
    v = str(p.get("montajli", "")).strip()
    if v in ("1", "0"):
        return v == "1"
    g = sayi(p.get("geometri"))
    return not (g is not None and g > 40)


def ort(x):
    return round(sum(x) / len(x), 2) if x else None


def medyan(x):
    if not x:
        return None
    x = sorted(x); n = len(x)
    return round(x[n // 2] if n % 2 else (x[n // 2 - 1] + x[n // 2]) / 2, 4)


def surec_agacini_kapat(pid):
    """Bir süreci ve çocuklarını kapatır (Windows: taskkill /T; öteki sistemler: psutil ya da süreç grubu)."""
    if WINDOWS:
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True, creationflags=CREATE)
        return
    if psutil:
        try:
            ana = psutil.Process(pid)
            for c in ana.children(recursive=True):
                c.kill()
            ana.kill()
            return
        except psutil.Error:
            pass
    try:
        os.killpg(os.getpgid(pid), signal.SIGKILL)
    except Exception:
        try:
            os.kill(pid, signal.SIGKILL)
        except Exception:
            pass


def klasoru_ac(p):
    if WINDOWS:
        os.startfile(str(p))                      # noqa: Windows'a özgü
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", str(p)])
    else:
        subprocess.Popen(["xdg-open", str(p)])


def pid_canli(pid):
    if psutil:
        return psutil.pid_exists(pid)
    try:
        os.kill(pid, 0)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------- panel
class Panel:
    def __init__(self, kuru, hiz, skor_dosyasi=None, liste_dosyasi=None):
        self.kuru, self.hiz = kuru, hiz
        self.kilit = threading.RLock()
        calisma = PANEL / "_calisma" / ("kuru" if kuru else "gercek")     # çalışma durumu: git'e girmez
        calisma.mkdir(parents=True, exist_ok=True)
        self.calisma = calisma
        if kuru:
            k = AYAR["kuru"]
            self.kuyruk_kok = calisma / "kuyruk"
            sablon = yol(k["kuyruk_sablonu"])
            self.akis_dir, self.kosular = calisma / "akis", calisma / "kosular"
            self.liste, self.puan = calisma / "kosu_listesi.csv", calisma / "yayin_puan.csv"
            self.iptal_yol, self.hazir_yol, self.faz = calisma / "yayin_iptal.txt", None, ""
            self.akis_dir.mkdir(exist_ok=True); self.kosular.mkdir(exist_ok=True)
        else:
            g = AYAR["gercek"]
            self.kuyruk_kok = yol(g["kuyruk_klasoru"])
            sablon = yol(g.get("kuyruk_sablonu"))
            self.akis_dir, self.kosular = yol(g["akis_klasoru"]), yol(g["kosular_klasoru"])
            self.liste, self.puan = yol(g["kosu_listesi"]), yol(g["puan_dosyasi"])
            self.iptal_yol, self.hazir_yol = yol(g["iptal_dosyasi"]), yol(g.get("hazir_dosyasi"))
            self.faz = g.get("faz", "")
            self.kosucu = yol(g["kosucu_klasoru"])
        for c in CONFIGLER:                                        # kuyruk yoksa şablondan kopyalanır
            (self.kuyruk_kok / c).mkdir(parents=True, exist_ok=True)
            if not self.kuyruk_yol(c).exists():
                if sablon and (sablon / c / "kuyruk.csv").exists():
                    shutil.copy2(sablon / c / "kuyruk.csv", self.kuyruk_yol(c))
                else:
                    self.kuyruk_yaz(c, [])
        self.skor_yol = Path(skor_dosyasi) if skor_dosyasi else self.puan      # yalnız skor sayfası için (test)
        self.liste_yol = Path(liste_dosyasi) if liste_dosyasi else self.liste
        self.log = calisma / "_log"; self.log.mkdir(exist_ok=True)
        self.durum_yol = calisma / "_durum.json"
        self.d = {"istasyon": {c: {"otomatik": False} for c in CONFIGLER}, "kosu": {}}
        if self.durum_yol.exists():
            try:
                eski = json.loads(self.durum_yol.read_text(encoding="utf-8"))
                self.d["kosu"] = eski.get("kosu", {})
                for c in CONFIGLER:
                    self.d["istasyon"][c].update(eski.get("istasyon", {}).get(c, {}))
            except Exception as e:
                print("durum dosyası okunamadı:", e)
        self.surec, self.akis = {}, {}
        self.olaylar = []
        self.toparla()

    # -- istasyon
    def ozel_mi(self, c):
        """Özel istasyon: arayüzde görünür ama bu kurulumda koşturulamaz (ör. özel harness gerektiren istasyon).
        Kuru modda örnek akışı olmayan istasyon da özeldir."""
        if ISTASYON[c].get("ozel"):
            return True
        return self.kuru and c not in AYAR["kuru"].get("kaynak", {})

    def ozel_not(self, c):
        return ISTASYON[c].get("ozel_not") or "özel harness"

    # -- dosyalar
    def kuyruk_yol(self, c):
        return self.kuyruk_kok / c / "kuyruk.csv"

    def kuyruk(self, c):
        with self.kuyruk_yol(c).open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))

    def kuyruk_yaz(self, c, satirlar):
        yol_ = self.kuyruk_yol(c)
        alanlar = ["sira", "paket", "ad", "seviye", "sure_dk", "run_id", "durum"]
        tmp = yol_.with_suffix(".csv.tmp")
        with tmp.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=alanlar, lineterminator="\n")
            w.writeheader()
            for s in satirlar:
                w.writerow({k: s.get(k, "") for k in alanlar})
        os.replace(tmp, yol_)

    def satir_guncelle(self, c, sira, **alan):
        with self.kilit:
            sat = self.kuyruk(c)
            for s in sat:
                if s["sira"] == str(sira):
                    s.update({k: str(v) for k, v in alan.items()})
            self.kuyruk_yaz(c, sat)

    def kaydet(self):
        tmp = self.durum_yol.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.d, ensure_ascii=False, indent=1), encoding="utf-8")
        os.replace(tmp, self.durum_yol)

    def olay(self, metin):
        self.olaylar.append({"t": datetime.now().isoformat(timespec="seconds"), "m": metin})
        self.olaylar = self.olaylar[-30:]
        print(datetime.now().strftime("%H:%M:%S"), metin, flush=True)

    def hazir_paketler(self):
        """Spec'i hazır paketler. hazir_dosyasi yoksa bütün paketler hazırdır; varsa her satırda bir paket kodu."""
        if not self.hazir_yol:
            return set(PARCALAR)
        h = set(AYAR["gercek"].get("her_zaman_hazir", []))
        if self.hazir_yol.exists():
            h |= {s.strip() for s in self.hazir_yol.read_text(encoding="utf-8").splitlines() if s.strip()}
        return h

    def puanlar(self):
        p = {}
        if self.puan and self.puan.exists():
            with self.puan.open(encoding="utf-8-sig", newline="") as f:
                for s in csv.DictReader(f):
                    run = s.get("run_id") or s.get("run")
                    v = s.get("puan_85") or s.get("puan") or s.get("toplam")
                    try:
                        p[run] = round(float(str(v).replace(",", ".")), 1)
                    except (TypeError, ValueError):
                        pass
        return p

    def liste_durum(self, run):
        if not self.liste or not self.liste.exists():
            return None
        for s in liste_oku(self.liste):
            if s.get("run_id") == run and s.get("durum"):
                return s["durum"]
        return None

    # -- süreç bulma (yeniden başlatmada)
    def canli_surec(self, run):
        if not psutil:
            return None
        betikler = {"panel_sunucu.py"}
        if not self.kuru:
            betikler |= {Path(x).name.lower() for x in AYAR["gercek"]["baslat"] if str(x).endswith(".py")}
        for p in psutil.process_iter(["pid", "name", "cmdline"]):
            try:
                av = p.info["cmdline"] or []
                if run in av and any(Path(x).name.lower() in betikler for x in av):
                    return p.info["pid"]
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return None

    def toparla(self):
        """Sunucu açılınca: 'kosuyor' satırların sürecini bul; yoksa kayıttan durumunu oku ya da 'bilinmiyor' yap."""
        for c in CONFIGLER:
            for s in self.kuyruk(c):
                if s["durum"] != "kosuyor":
                    continue
                run = s["run_id"]
                pid = self.canli_surec(run)
                if pid:
                    self.olay(f"{c} · {run} hâlâ çalışıyor (pid {pid}); izlemeye alındı")
                    self.d["kosu"].setdefault(run, {"config": c, "sira": s["sira"], "basla": datetime.now().isoformat(timespec="seconds"), "kt": {}})
                    self.d["kosu"][run]["pid"] = pid
                    threading.Thread(target=self.bekle_pid, args=(c, s["sira"], run, pid), daemon=True).start()
                else:
                    dur = self.son_json(run) or self.liste_durum(run) or "bilinmiyor"
                    self.satir_guncelle(c, s["sira"], durum=dur)
                    self.olay(f"{c} · {run} süreç yok; durum '{dur}' yazıldı")
        self.kaydet()

    def son_json(self, run):
        """Koşucunun stdout'undaki son JSON satırından 'durum' alanı (sözleşme: README)."""
        f = self.log / f"{run}.out"
        if not f.exists():
            return None
        for s in reversed(f.read_text(encoding="utf-8", errors="replace").splitlines()):
            try:
                d = json.loads(s)
                if isinstance(d, dict) and d.get("durum"):
                    return d["durum"]
            except Exception:
                continue
        return None

    # -- komutlar
    def aktif(self, c):
        for s in self.kuyruk(c):
            if s["durum"] == "kosuyor":
                return s
        return None

    def komut(self, sablon, **alan):
        alan.setdefault("python", sys.executable)
        return [str(x).format(**alan) for x in sablon]

    def baslat(self, c, onay=False):
        with self.kilit:
            if c not in CONFIGLER:
                return 404, {"hata": "böyle bir istasyon yok"}
            if self.ozel_mi(c):
                return 409, {"hata": f"{c}: {self.ozel_not(c)}"}
            if self.aktif(c):
                return 409, {"hata": "bu istasyonda zaten bir koşu var"}
            if ISTASYON[c].get("onay") and not onay:
                return 428, {"hata": "önce onay kutusunu işaretleyin", "onay": ISTASYON[c]["onay"]}
            sira = next((s for s in self.kuyruk(c) if not s["durum"].strip() and not s["run_id"].strip()), None)
            if not sira:
                return 409, {"hata": "kuyruk bitti"}
            if sira["paket"] not in self.hazir_paketler():
                return 409, {"hata": f"{sira['paket']} için spec henüz hazır değil"}
            if self.kuru:
                run = "k%06d" % random.randrange(10 ** 6)
                while (self.kosular / run).exists():
                    run = "k%06d" % random.randrange(10 ** 6)
                (self.kosular / run / "teslim").mkdir(parents=True, exist_ok=True)
                cmd = [sys.executable, str(Path(__file__).resolve()), "--tekrar-oynat", AYAR["kuru"]["kaynak"][c], run,
                       "--hiz", str(self.hiz), "--kok", str(self.calisma), "--ayar", str(AYAR_KOK / AYAR_ADI[0]),
                       "--config", c, "--paket", sira["paket"]]
                cwd = PANEL
            else:
                g = AYAR["gercek"]
                r = subprocess.run(self.komut(g["hazirla"], config=c, paket=sira["paket"], sure_dk=sira["sure_dk"]),
                                   cwd=self.kosucu, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                   timeout=600, creationflags=CREATE)
                desen = AYAR.get("run_id_deseni", r"[a-z]\d{6}")
                m = re.findall(r"\b" + desen + r"\b", r.stdout)
                if r.returncode or not m:
                    self.olay(f"{c} · hazirla başarısız: {temiz(r.stdout + r.stderr, 200)}")
                    return 500, {"hata": "koşucu 'hazirla' başarısız", "ayrinti": temiz(r.stdout + r.stderr, 300)}
                run = m[-1]
                cmd, cwd = self.komut(g["baslat"], run_id=run, config=c, paket=sira["paket"], sure_dk=sira["sure_dk"]), self.kosucu
            self.satir_guncelle(c, sira["sira"], run_id=run, durum="kosuyor")
            out = (self.log / f"{run}.out").open("w", encoding="utf-8")
            ek = {} if WINDOWS else {"start_new_session": True}
            p = subprocess.Popen(cmd, cwd=cwd, stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                 creationflags=CREATE, **ek)
            self.surec[run] = p
            self.d["kosu"][run] = {"config": c, "sira": sira["sira"], "paket": sira["paket"], "pid": p.pid,
                                   "basla": datetime.now().isoformat(timespec="seconds"), "tavan_dk": int(sira["sure_dk"]), "kt": {}}
            self.kaydet()
            self.olay(f"▶ {c} · {sira['paket']} {sira['ad']} · {run} · tavan {sira['sure_dk']} dk")
            threading.Thread(target=self.bekle, args=(c, sira["sira"], run, p, out), daemon=True).start()
            return 200, {"run_id": run, "paket": sira["paket"]}

    def bitir(self, c, sira, run, dur):
        with self.kilit:
            sat = {s["sira"]: s for s in self.kuyruk(c)}
            if sat.get(str(sira), {}).get("durum") == "kosuyor":
                self.satir_guncelle(c, sira, durum=dur)
            k = self.d["kosu"].setdefault(run, {})
            k["bitis"] = datetime.now().isoformat(timespec="seconds"); k.pop("pid", None)
            self.kaydet()
            self.olay(f"■ {c} · {run} · {dur}")
            oto = self.d["istasyon"][c].get("otomatik") and dur != "yardimli"
        if oto:
            time.sleep(2)
            kod, sonuc = self.baslat(c, onay=True)
            if kod != 200:
                self.olay(f"{c} · otomatik devam durdu: {sonuc.get('hata')}")

    def bekle(self, c, sira, run, p, out):
        p.wait()
        out.close()
        self.surec.pop(run, None)
        if self.d["kosu"].get(run, {}).get("durduruldu"):
            return
        self.bitir(c, sira, run, self.son_json(run) or self.liste_durum(run) or "cokme")

    def bekle_pid(self, c, sira, run, pid):
        while pid_canli(pid):
            time.sleep(3)
        if self.d["kosu"].get(run, {}).get("durduruldu"):
            return
        self.bitir(c, sira, run, self.son_json(run) or self.liste_durum(run) or "bilinmiyor")

    def durdur(self, c):
        with self.kilit:
            s = self.aktif(c)
            if not s:
                return 409, {"hata": "bu istasyonda çalışan koşu yok"}
            run = s["run_id"]
            k = self.d["kosu"].setdefault(run, {})
            pid = k.get("pid") or self.canli_surec(run)
            k["durduruldu"] = True
            if pid:
                surec_agacini_kapat(pid)
            self.satir_guncelle(c, s["sira"], durum="yardimli")
            k["bitis"] = datetime.now().isoformat(timespec="seconds"); k.pop("pid", None)
            self.kaydet()
            self.olay(f"✕ {c} · {run} durduruldu (yardımlı)")
            return 200, {"run_id": run, "durum": "yardimli"}

    def sifirla(self):
        """Deneme sonrası temiz başlangıç; hiçbir şey silinmez. Kuyruklar ve panel durumu _calisma/<mod>/_sifirlama/<zaman>/
        altına kopyalanır, o ana kadarki koşular iptal dosyasına yazılır (puanlanmaz), kuyruklar boşaltılır."""
        with self.kilit:
            acik = [c for c in CONFIGLER if self.aktif(c)]
            if acik:
                return 409, {"hata": "önce çalışan koşuları durdurun: " + ", ".join(acik)}
            zaman = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            taban = self.calisma / "_sifirlama"
            arsiv, i = taban / zaman, 2
            while arsiv.exists():
                arsiv, i = taban / f"{zaman}_{i}", i + 1
            arsiv.mkdir(parents=True)
            iptal = []
            for c in CONFIGLER:
                (arsiv / c).mkdir()
                shutil.copy2(self.kuyruk_yol(c), arsiv / c / "kuyruk.csv")
                sat = self.kuyruk(c)
                iptal += [(s["run_id"], c, s["paket"], s["durum"]) for s in sat if s.get("run_id")]
                for s in sat:
                    s["run_id"] = ""; s["durum"] = ""
                self.kuyruk_yaz(c, sat)
            if self.durum_yol.exists():
                shutil.copy2(self.durum_yol, arsiv / self.durum_yol.name)
            if iptal and self.iptal_yol:
                self.iptal_yol.parent.mkdir(parents=True, exist_ok=True)
                with self.iptal_yol.open("a", encoding="utf-8") as f:
                    for r in iptal:
                        f.write("\t".join([r[0], r[1], r[2], r[3] or "-", f"panel sıfırlandı {zaman}"]) + "\n")
            self.d = {"istasyon": {c: {"otomatik": False} for c in CONFIGLER}, "kosu": {}}
            self.surec, self.akis = {}, {}
            self.olaylar = []
            self.kaydet()
            self.olay(f"↺ panel sıfırlandı · {len(iptal)} koşu iptal listesine yazıldı")
            return 200, {"iptal": len(iptal), "arsiv": zaman}

    def klasor_ac(self, run):
        """Teslim edilmiş bir koşunun teslim klasörünü dosya yöneticisinde açar (yalnız kuyruklarda kayıtlı run_id)."""
        if not RUN_RE.match(run):
            return 404, {"hata": "yok"}
        kayitli = any(s.get("run_id") == run for c in CONFIGLER for s in self.kuyruk(c))
        yol_ = self.kosular / run / "teslim"
        if not kayitli or not yol_.is_dir():
            return 404, {"hata": "teslim klasörü bulunamadı"}
        try:
            klasoru_ac(yol_)
        except Exception as e:
            return 500, {"hata": f"klasör açılamadı: {e}"}
        return 200, {"acildi": run}

    # -- skor tablosu (/skor): puanlar + koşu kaydı + kuyruklar; hepsi SALT OKUNUR
    def iptaller(self):
        if not self.iptal_yol or not self.iptal_yol.exists():
            return set()
        return {s.split("\t")[0].strip() for s in self.iptal_yol.read_text(encoding="utf-8", errors="replace").splitlines() if s.strip()}

    def skor(self):
        iptal = self.iptaller()
        puan_satir, kalite_kol = {}, None
        if self.skor_yol and self.skor_yol.exists():
            with self.skor_yol.open(encoding="utf-8-sig", newline="") as f:
                okuyucu = csv.DictReader(f)
                kalite_kol = next((k for k in (okuyucu.fieldnames or []) if k and "kalite" in k.lower()), None)
                for s in okuyucu:
                    run = (s.get("run_id") or "").strip()
                    if not run:
                        continue
                    if str(s.get("iptal", "")).strip() in ("1", "true", "evet"):
                        iptal.add(run)
                    puan_satir[run] = s                            # aynı run iki kez yazıldıysa sonuncusu
        liste = {}
        if self.liste_yol and self.liste_yol.exists():
            for s in liste_oku(self.liste_yol):
                if (not self.faz or s.get("faz") == self.faz) and s.get("run_id"):
                    liste[s["run_id"]] = s
        kuyruk, sirada = {}, {}
        for c in CONFIGLER:
            sat = self.kuyruk(c)
            sirada[c] = sum(1 for s in sat if not s["run_id"].strip() and not s["durum"].strip())
            for s in sat:
                if s["run_id"].strip():
                    kuyruk[s["run_id"]] = (c, s)
        kosular = []
        for run in set(puan_satir) | set(liste) | set(kuyruk):
            if run in iptal:
                continue
            p, l, (kc, ks) = puan_satir.get(run, {}), liste.get(run, {}), kuyruk.get(run, (None, {}))
            config = kc or (p.get("config") if p.get("config") in CONFIGLER else None) or l.get("config")
            if config not in CONFIGLER:
                continue
            paket = ks.get("paket") or p.get("paket") or l.get("parca")
            kd = ks.get("durum", "")
            durum = "kosuyor" if kd == "kosuyor" else (p.get("durum_kosu") or l.get("durum") or kd or "bilinmiyor")
            k = self.d["kosu"].get(run, {})
            basla = l.get("basla") or k.get("basla")
            dk, usd, arac = sayi(l.get("sure_dk")), sayi(l.get("usd")), sayi(l.get("tool_cagri"))
            if durum == "kosuyor":
                if basla:
                    dk = round((datetime.now() - datetime.fromisoformat(basla)).total_seconds() / 60, 1)
                a = self.akis.get(run)
                if a:
                    arac, usd = a.arac, a.usd
            bilgi = PARCALAR.get(paket, {})
            kosular.append({
                "run_id": run, "config": config, "paket": paket, "ad": bilgi.get("ad", paket), "seviye": bilgi.get("seviye", ""),
                "resim": bilgi.get("resim", ""), "durum": durum, "basla": basla, "dk": dk, "usd": usd,
                "arac": int(arac) if arac is not None else None,
                "puan": sayi(p.get("puan_85")), "kalite": sayi(p.get(kalite_kol)) if kalite_kol else None,
                "kat": {k2: sayi(p.get(k2)) for k2 in ("geometri", "tamlik", "montaj", "ozellik", "resim")},
                "montajli": montajli_mi(p),
                "acilir": run in kuyruk and durum != "kosuyor"})
        kosular.sort(key=lambda r: r["basla"] or "", reverse=True)
        tablo = []
        for c in CONFIGLER:
            ks = [r for r in kosular if r["config"] == c]
            pu = [r for r in ks if r["puan"] is not None]
            bitmis = [r for r in ks if r["durum"] != "kosuyor"]
            seviye = {}
            for sv in ("sekil", "zor", "cok_zor"):
                x = [r["puan"] for r in pu if r["seviye"] == sv]
                seviye[sv] = {"ort": ort(x), "n": len(x)}
            kat = {}
            for k2 in ("geometri", "tamlik", "montaj", "ozellik", "resim"):
                sat = [r for r in pu if r["kat"][k2] is not None and not (k2 == "montaj" and not r["montajli"])]
                x = [r["kat"][k2] for r in sat]                    # montaj yalnız montajlı parçada sayılır
                az = [KAT_AZAMI[k2] if k2 != "geometri" else (40 if r["montajli"] else 50) for r in sat]
                kat[k2] = {"ort": ort(x), "n": len(x), "azami": ort(az),
                           "oran": round(sum(x) / sum(az), 4) if az and sum(az) else None}
            dkl = [r["dk"] for r in bitmis if r["dk"] is not None]
            usdl = [r["usd"] for r in bitmis if r["usd"] is not None]
            kal = [r["kalite"] for r in pu if r["kalite"] is not None]
            aktif = next((r for r in ks if r["durum"] == "kosuyor"), None)
            tablo.append({
                "config": c, "ozel": self.ozel_mi(c), "n": len(pu), "ort": ort([r["puan"] for r in pu]), "seviye": seviye, "kat": kat,
                "gecen": sum(1 for r in pu if r["puan"] >= GECME_ESIGI),
                "medyan_dk": medyan(dkl), "n_dk": len(dkl), "medyan_usd": medyan(usdl), "n_usd": len(usdl),
                "cokme": sum(1 for r in bitmis if r["durum"] == "cokme"), "tavan": sum(1 for r in bitmis if r["durum"] == "tavan"),
                "yardimli": sum(1 for r in bitmis if r["durum"] == "yardimli"),
                "bitti": len(bitmis), "puan_bekliyor": sum(1 for r in bitmis if r["puan"] is None),
                "kalite": {"ort": ort(kal), "n": len(kal)} if kalite_kol else None,
                "aktif": aktif and {"paket": aktif["paket"], "ad": aktif["ad"], "dk": aktif["dk"]}, "sirada": sirada[c]})
        tablo.sort(key=lambda t: (t["ort"] is None, -(t["ort"] or 0), -t["n"]))
        for i, t in enumerate(tablo):
            t["sira"] = i + 1 if t["ort"] is not None else None
        # kafa kafaya: 2+ istasyonun puanladığı ya da yarıştığı parça (bir istasyonun son koşusu)
        parca = {}
        for r in sorted(kosular, key=lambda r: r["basla"] or ""):
            parca.setdefault(r["paket"], {})[r["config"]] = r
        kk = []
        for paket, hucre in parca.items():
            puanli = [c for c, r in hucre.items() if r["puan"] is not None]
            if len(puanli) < 2 and len(hucre) < 2:
                continue
            en = max((hucre[c]["puan"] for c in puanli), default=None)
            b = PARCALAR.get(paket, {})
            kk.append({"paket": paket, "ad": b.get("ad", paket), "seviye": b.get("seviye", ""), "resim": b.get("resim", ""),
                       "puanli": len(puanli), "en": en if len(puanli) >= 2 else None,
                       "hucre": {c: {"puan": r["puan"], "durum": r["durum"], "run_id": r["run_id"], "dk": r["dk"],
                                     "acilir": r["acilir"]} for c, r in hucre.items()}})
        kk.sort(key=lambda x: (-x["puanli"], int(re.sub(r"\D", "", x["paket"] or "") or 0)))
        return {"saat": datetime.now().isoformat(timespec="seconds"), "kuru": self.kuru, "esik": GECME_ESIGI, "azami": 85,
                "kalite_var": bool(kalite_kol), "tablo": tablo, "kafa": kk, "kosular": kosular[:40], "toplam_kosu": len(kosular),
                "iptal_sayisi": len(iptal), "istasyonlar": istasyon_listesi()}

    def sec(self, c, paket):
        """İstasyonun SIRADAKİ parçasını listeden seç: kuyrukta bekleyen bir satırsa öne alınır, değilse yeni satır
        olarak ilk boş satırın önüne eklenir. Hiçbir satır silinmez; özgün kuyruk sırası arkada kalır."""
        with self.kilit:
            if paket not in PARCALAR:
                return 404, {"hata": "böyle bir parça yok"}
            if self.ozel_mi(c):
                return 409, {"hata": f"{c}: {self.ozel_not(c)}"}
            if paket not in self.hazir_paketler():
                return 409, {"hata": f"{paket} için spec henüz hazır değil"}
            sat = self.kuyruk(c)
            if any(s["paket"] == paket and (s["run_id"].strip() or s["durum"].strip()) for s in sat):
                return 409, {"hata": f"{c} bu parçayı zaten çizdi ya da çiziyor"}
            ilk = next((i for i, s in enumerate(sat) if not s["durum"].strip() and not s["run_id"].strip()), len(sat))
            var = next((i for i, s in enumerate(sat) if s["paket"] == paket), None)
            if var is not None:
                satir = sat.pop(var)
                if var < ilk:
                    ilk -= 1
            else:
                r = PARCALAR[paket]
                satir = {"sira": str(max([int(s["sira"]) for s in sat] or [0]) + 1), "paket": paket, "ad": r["ad"],
                         "seviye": r["seviye"], "sure_dk": r["sure_dk"], "run_id": "", "durum": ""}
            sat.insert(ilk, satir)
            self.kuyruk_yaz(c, sat)
            self.olay(f"⇢ {c} · sıradaki: {paket} {PARCALAR[paket]['ad']}")
            return 200, {"config": c, "paket": paket}

    def cikar(self, c, sira):
        """Henüz başlamamış bir satırı kuyruktan çıkarır. Satır kaybolmaz: _calisma/<mod>/_cikarilan.csv'ye yazılır,
        parça seçiciden yeniden eklenebilir."""
        with self.kilit:
            sat = self.kuyruk(c)
            i = next((i for i, x in enumerate(sat) if x["sira"] == str(sira)), None)
            if i is None:
                return 404, {"hata": "böyle bir satır yok"}
            x = sat[i]
            if x["run_id"].strip() or x["durum"].strip():
                return 409, {"hata": "başlamış ya da bitmiş koşu kuyruktan çıkarılamaz"}
            kayit = self.calisma / "_cikarilan.csv"
            yeni = not kayit.exists()
            with kayit.open("a", encoding="utf-8", newline="") as f:
                w = csv.writer(f, lineterminator="\n")
                if yeni:
                    w.writerow(["zaman", "config", "sira", "paket", "ad", "seviye", "sure_dk"])
                w.writerow([datetime.now().isoformat(timespec="seconds"), c, x["sira"], x["paket"], x["ad"], x["seviye"], x["sure_dk"]])
            sat.pop(i)
            self.kuyruk_yaz(c, sat)
            self.olay(f"✕ {c} · kuyruktan çıkarıldı: {x['paket']} {x['ad']}")
            return 200, {"config": c, "paket": x["paket"]}

    def sec_hepsi(self, paket):
        sonuc = {c: self.sec(c, paket) for c in CONFIGLER if not self.ozel_mi(c)}
        tamam = [c for c, (k, _) in sonuc.items() if k == 200]
        red = {c: d["hata"] for c, (k, d) in sonuc.items() if k != 200}
        return (200 if tamam else 409), {"tamam": tamam, "red": red, "hata": "; ".join(f"{c}: {h}" for c, h in red.items())}

    def otomatik(self, c, acik):
        if self.ozel_mi(c):
            return 409, {"hata": f"{c}: {self.ozel_not(c)}"}
        with self.kilit:
            self.d["istasyon"][c]["otomatik"] = bool(acik)
            self.kaydet()
        return 200, {"otomatik": bool(acik)}

    # -- durum
    def durum(self):
        simdi = datetime.now()
        hazir, puan = self.hazir_paketler(), self.puanlar()
        out = {"kuru": self.kuru, "baslik": AYAR.get("baslik", ""), "saat": simdi.isoformat(timespec="seconds"),
               "istasyon": [], "olay": self.olaylar[-8:], "sistem": sistem_olc(self.calisma)}
        out["parcalar"] = [{"paket": r["paket"], "ad": r["ad"], "seviye": r["seviye"], "resim": r.get("resim", ""),
                            "hazir": r["paket"] in hazir} for r in PARCALAR.values()]
        for c in CONFIGLER:
            sat = self.kuyruk(c)
            for s in sat:
                s["puan"] = puan.get(s["run_id"]) if s["run_id"] else None
                s["hazir"] = s["paket"] in hazir
            ak = next((s for s in sat if s["durum"] == "kosuyor"), None)
            sonraki = next((s for s in sat if not s["durum"].strip() and not s["run_id"].strip()), None)
            ozel = self.ozel_mi(c)
            ist = {"config": c, "kuyruk": sat, "otomatik": self.d["istasyon"][c].get("otomatik", False),
                   "onay": ISTASYON[c].get("onay"), "ozel": ozel, "ozel_not": self.ozel_not(c) if ozel else None,
                   "sonraki": sonraki and {"sira": sonraki["sira"], "paket": sonraki["paket"],
                                           "ad": sonraki["ad"], "hazir": sonraki["paket"] in hazir},
                   "aktif": None, "son": None}
            goster = ak or next((s for s in reversed(sat) if s["run_id"].strip()), None)
            if goster:
                ist["aktif" if ak else "son"] = self.kosu_ozet(goster, simdi)
            out["istasyon"].append(ist)
        out["istasyonlar"] = istasyon_listesi()
        return out

    def kosu_ozet(self, s, simdi):
        run = s["run_id"]
        k = self.d["kosu"].setdefault(run, {"basla": None, "kt": {}})
        a = self.akis.get(run)
        if a is None:
            a = self.akis[run] = Akis(self.akis_dir / f"{run}.jsonl")
            a.kt.update(k.get("kt", {}))
        a.oku(simdi.isoformat(timespec="seconds"))
        pngler = teslim_tara(self.kosular / run, a.kt)
        if k.get("kt") != a.kt:
            k["kt"] = dict(a.kt); self.kaydet()
        basla = k.get("basla")
        if not basla and (self.akis_dir / f"{run}.jsonl").exists():
            basla = datetime.fromtimestamp((self.akis_dir / f"{run}.jsonl").stat().st_ctime).isoformat(timespec="seconds")
        bitis = k.get("bitis")
        son = datetime.fromisoformat(bitis) if bitis and s["durum"] != "kosuyor" else simdi
        gecen = int((son - datetime.fromisoformat(basla)).total_seconds()) if basla else 0
        return {"run_id": run, "sira": s["sira"], "paket": s["paket"], "ad": s["ad"], "seviye": s["seviye"],
                "durum": s["durum"], "puan": s.get("puan"), "basla": basla, "gecen_sn": gecen,
                "tavan_sn": int(s["sure_dk"]) * 60, "arac": a.arac, "token": a.tok, "usd": a.usd,
                "kt": [{"ad": ad, "etiket": et, "t": a.kt.get(ad)} for ad, et in KT],
                "akis": a.son, "gorsel": pngler}


def istasyon_listesi():
    """Arayüzün istasyon kartları için: kod, araç adı, ek etiket, harness basamağı (logo yok; metin çipleri)."""
    return [{"kod": i["kod"], "arac": i.get("arac", i["kod"]), "ek": i.get("ek", ""), "basamak": i.get("basamak", "")}
            for i in AYAR["istasyonlar"]]


# ---------------------------------------------------------------- sistem göstergeleri
CPU = [None]


def cpu_olc():  # CPU yüzdesi arka planda ölçülür (istek iş parçacıklarında anlık okuma 0 döndürüyordu)
    while psutil:
        try:
            CPU[0] = round(psutil.cpu_percent(interval=1.5))
        except Exception:
            time.sleep(2)


def sistem_olc(kok):
    out = {"cpu": CPU[0], "ram": None, "ram_bos_gb": None, "disk": None, "disk_bos_gb": None}
    try:
        dk = shutil.disk_usage(kok)                       # çalışma klasörünün diski
        out["disk"], out["disk_bos_gb"] = round(dk.used / dk.total * 100), round(dk.free / 2**30)
    except Exception:
        pass
    if psutil:
        try:
            vm = psutil.virtual_memory()
            out["ram"], out["ram_bos_gb"] = round(vm.percent), round(vm.available / 2**30, 1)
        except Exception:
            pass
    return out


# ---------------------------------------------------------------- HTTP
PANEL_OBJ = None
AYAR_ADI = ["ayar.json"]
PNG_RE = re.compile(r"^[\w.\-]+\.png$", re.I)
SAYFA = {"/": "panel.html", "/panel.html": "panel.html", "/skor": "skor.html", "/skor.html": "skor.html",
         "/yayin": "yayin_sayfasi.html", "/yayin_sayfasi.html": "yayin_sayfasi.html"}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def gonder(self, kod, govde, tip="application/json; charset=utf-8"):
        if isinstance(govde, (dict, list)):
            govde = json.dumps(govde, ensure_ascii=False).encode("utf-8")
        elif isinstance(govde, str):
            govde = govde.encode("utf-8")
        self.send_response(kod)
        self.send_header("Content-Type", tip)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(govde)))
        self.end_headers()
        try:
            self.wfile.write(govde)
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass                                   # tarayıcı sekmesi kapandı / yenilendi

    def do_GET(self):
        y = self.path.split("?")[0]
        if y in SAYFA:
            return self.gonder(200, (PANEL / SAYFA[y]).read_bytes(), "text/html; charset=utf-8")
        if y == "/varlik.js":
            return self.gonder(200, (PANEL / "varlik.js").read_bytes(), "text/javascript; charset=utf-8")
        if y == "/api/skor":
            return self.gonder(200, PANEL_OBJ.skor())
        if y == "/api/durum":
            return self.gonder(200, PANEL_OBJ.durum())
        m = re.match(r"^/api/gorsel/([^/]+)/([^/]+)$", y)
        if m and RUN_RE.match(m[1]) and PNG_RE.match(m[2]):
            teslim = (PANEL_OBJ.kosular / m[1] / "teslim").resolve()
            f = (teslim / m[2]).resolve()
            if f.parent == teslim and f.is_file():
                return self.gonder(200, f.read_bytes(), "image/png")
        return self.gonder(404, {"hata": "yok"})

    def do_POST(self):
        if self.headers.get("X-Panel") != "1":       # başka sitelerin tarayıcıdan POST'unu engeller (ön uçuş)
            return self.gonder(403, {"hata": "izin yok"})
        n = int(self.headers.get("Content-Length") or 0)
        try:
            g = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            g = {}
        m1 = re.match(r"^/api/cikar/([A-Za-z0-9\-_]+)$", self.path)
        if m1:
            if m1[1] not in CONFIGLER:
                return self.gonder(404, {"hata": "yok"})
            return self.gonder(*PANEL_OBJ.cikar(m1[1], str(g.get("sira", ""))))
        m0 = re.match(r"^/api/sec/([A-Za-z0-9\-_]+)$", self.path)
        if m0:
            if m0[1] == "HEPSI":
                return self.gonder(*PANEL_OBJ.sec_hepsi(str(g.get("paket", ""))))
            if m0[1] not in CONFIGLER:
                return self.gonder(404, {"hata": "yok"})
            return self.gonder(*PANEL_OBJ.sec(m0[1], str(g.get("paket", ""))))
        if self.path == "/api/klasor":
            return self.gonder(*PANEL_OBJ.klasor_ac(str(g.get("run_id", ""))))
        if self.path == "/api/sifirla":
            return self.gonder(*(PANEL_OBJ.sifirla() if g.get("onay") else (428, {"hata": "sıfırlamak için onay gerekli"})))
        m = re.match(r"^/api/(baslat|sonraki|durdur|otomatik)/([A-Za-z0-9\-_]+)$", self.path)
        if not m or m[2] not in CONFIGLER:
            return self.gonder(404, {"hata": "yok"})
        k, c = m[1], m[2]
        if k in ("baslat", "sonraki"):
            kod, d = PANEL_OBJ.baslat(c, onay=bool(g.get("onay")))
        elif k == "durdur":
            kod, d = (PANEL_OBJ.durdur(c) if g.get("onay") else (428, {"hata": "durdurmak için onay gerekli"}))
        else:
            kod, d = PANEL_OBJ.otomatik(c, g.get("acik"))
        return self.gonder(kod, d)


# ---------------------------------------------------------------- kuru mod: akış oynatıcı
class DosyaKilidi:
    """Aynı anda biten iki oynatıcı aynı CSV'ye yazarken satır kaybolmasın diye basit kilit dosyası (O_EXCL)."""

    def __init__(self, hedef):
        self.yol = Path(str(hedef) + ".kilit")

    def __enter__(self):
        for _ in range(200):
            try:
                os.close(os.open(self.yol, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
                return self
            except FileExistsError:
                time.sleep(0.05)
        return self                                     # 10 sn sonra kilitsiz devam (eski kilit kalmışsa)

    def __exit__(self, *a):
        try:
            os.remove(self.yol)
        except OSError:
            pass


def tekrar_oynat(kaynak, hedef, hiz, kok, config, paket):
    """Örnek akışı (salt okur) sahte bir run_id'ye hızlandırılmış oynatır; teslim dosyalarını yol boyunca kopyalar.
    Bitince koşucu sözleşmesindeki gibi kosu_listesi.csv'ye bir satır ekler ve stdout'a son JSON satırını yazar."""
    kok = Path(kok)
    k = AYAR["kuru"]
    src_akis = yol(k["akis_kaynak"]) / f"{kaynak}.jsonl"
    src_teslim = yol(k["teslim_kaynak"])
    out_akis = kok / "akis" / f"{hedef}.jsonl"
    out_teslim = kok / "kosular" / hedef / "teslim"
    out_teslim.mkdir(parents=True, exist_ok=True)
    basla = datetime.now().isoformat(timespec="seconds")
    satirlar = src_akis.read_text(encoding="utf-8", errors="replace").splitlines()
    sonuc = next((json.loads(s) for s in satirlar if '"type": "result"' in s or '"type":"result"' in s), {})
    toplam_sn = max(20.0, (sonuc.get("duration_ms") or 60000) / 1000 / hiz)
    adim = toplam_sn / max(1, len(satirlar))
    dosyalar = sorted(p for p in src_teslim.glob("*") if p.is_file())
    with out_akis.open("w", encoding="utf-8") as f:
        for i, s in enumerate(satirlar):
            f.write(s.replace(kaynak, hedef) + "\n"); f.flush()
            pay = (i + 1) / len(satirlar)
            for d in dosyalar[: int(len(dosyalar) * pay)]:
                if not (out_teslim / d.name).exists():
                    shutil.copy(d, out_teslim / d.name)   # copy: dosya saati şimdi, gerçek koşudaki gibi
            time.sleep(adim)
    durum = "tamam" if (out_teslim / "final.step").exists() else "cokme"
    tok = {"in": 0, "out": 0, "cache": 0}
    arac = 0
    for s in satirlar:
        try:
            d = json.loads(s)
        except Exception:
            continue
        if d.get("type") == "assistant":
            u = d["message"].get("usage", {})
            tok["in"] += u.get("input_tokens", 0); tok["out"] += u.get("output_tokens", 0)
            tok["cache"] += u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            arac += sum(1 for c in d["message"].get("content", []) if c.get("type") == "tool_use")
    usd = round(sonuc.get("total_cost_usd") or 0, 4)
    dk = round(toplam_sn / 60, 1)
    liste = kok / "kosu_listesi.csv"
    with DosyaKilidi(liste), liste.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        if f.tell() == 0:
            w.writerow(KOSU_LISTESI_SUTUN)
        w.writerow([hedef, "Y", config, paket, "A", "1", basla, datetime.now().isoformat(timespec="seconds"), dk,
                    tok["in"], tok["out"], tok["cache"], usd, arac, "", durum, f"kuru mod ({kaynak})"])
    # kuru modda skor tablosu dolsun diye örnek puan satırı (gerçek ölçüm değil; ornek/ornek_puan.csv)
    ornek = yol(k.get("puan_ornek"))
    if durum == "tamam" and ornek and ornek.exists():
        with ornek.open(encoding="utf-8", newline="") as f:
            satir = next((r for r in csv.DictReader(f) if r.get("kaynak") == kaynak), None)
        if satir:
            puan = kok / "yayin_puan.csv"
            alan = ["run_id", "config", "paket", "durum_kosu", "puan_85", "geometri", "tamlik", "montaj", "ozellik", "resim",
                    "kalite_15", "montajli", "iptal", "not"]
            with DosyaKilidi(puan), puan.open("a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=alan, lineterminator="\n")
                if f.tell() == 0:
                    w.writeheader()
                kat = {a: satir.get(a, "") for a in ("geometri", "tamlik", "montaj", "ozellik", "resim", "kalite_15", "montajli")}
                top = sum(float(kat[a] or 0) for a in ("geometri", "tamlik", "montaj", "ozellik", "resim"))
                w.writerow({"run_id": hedef, "config": config, "paket": paket, "durum_kosu": durum, "puan_85": round(top, 1),
                            **kat, "iptal": "", "not": "örnek veri, gerçek ölçüm değil"})
    print(json.dumps({"run": hedef, "durum": durum, "dk": dk, "usd": usd, "arac": arac, "red": 0}, ensure_ascii=False))


def main():
    global PANEL_OBJ
    ap = argparse.ArgumentParser(description="Agentic CAD Ligi kontrol paneli")
    ap.add_argument("--kuru", action="store_true", help="demo mod: ornek/ akışlarını oynatır, gerçek koşu başlatmaz")
    ap.add_argument("--ayar", default=str(PANEL / "ayar.json"), help="ayar dosyası (varsayılan: panel/ayar.json)")
    ap.add_argument("--hiz", type=float, help="kuru modda oynatma hızı (varsayılan ayar.json'dan)")
    ap.add_argument("--port", type=int, help="varsayılan ayar.json'dan (8765)")
    ap.add_argument("--host", default="127.0.0.1", help="yalnız bu makine; ağa açmak güvenli değildir")
    ap.add_argument("--tekrar-oynat", nargs=2, metavar=("KAYNAK", "HEDEF"), help=argparse.SUPPRESS)
    ap.add_argument("--kok", help=argparse.SUPPRESS)
    ap.add_argument("--config", help=argparse.SUPPRESS)
    ap.add_argument("--paket", help=argparse.SUPPRESS)
    ap.add_argument("--skor-dosyasi", help="skor sayfası için başka bir yayin_puan.csv (test)")
    ap.add_argument("--liste-dosyasi", help="skor sayfası için başka bir kosu_listesi.csv (test)")
    a = ap.parse_args()
    ayar_yukle(a.ayar)
    AYAR_ADI[0] = Path(a.ayar).name
    gizle_kur()
    hiz = a.hiz or AYAR.get("kuru", {}).get("hiz", 6.0)
    if a.tekrar_oynat:
        return tekrar_oynat(*a.tekrar_oynat, hiz, a.kok, a.config, a.paket)
    threading.Thread(target=cpu_olc, daemon=True).start()
    PANEL_OBJ = Panel(a.kuru, hiz, a.skor_dosyasi, a.liste_dosyasi)
    port = a.port or AYAR.get("port", 8765)
    srv = ThreadingHTTPServer((a.host, port), H)
    print(f"panel {'KURU MOD ' if a.kuru else ''}http://{a.host}:{port}  ·  skor: /skor  ·  yayın sayfası: /yayin", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
