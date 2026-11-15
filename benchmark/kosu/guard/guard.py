"""F23 Agentic CAD Ligi: yapımcı oturumu guard kancası (Claude Code PreToolUse).

Çağrı (koşunun settings.json'undaki kanca komutu; kos.py yazar):
    python -I guard.py --run r123456 --config B3D-H0 --kok <koşu klasörü> --log <guard.log>

Her araç çağrısında stdin'den kanca JSON'unu okur, kural kümesini (kurallar.json) uygular (KOR_KOSU.md §1-§2),
kararı guard.log'a yazar: zaman, oturum, run_id, araç, karar.
Red gerekçesi yapımcıya genel bir cümleyle gider; benchmark / config bilgisi sızdırılmaz.

Bu repodaki sürüm referanstır: kurallar.json'daki yasak kelime / parça numarası / yasak sürücü listeleri yer tutucudur,
kendi kurulumunuzun gizli yollarıyla doldurun. Yayındaki NX-H2'ye özgü istisnalar (özel harness) çıkarıldı;
H2 için yalnız genel "uzman skill öneki" kuralı kaldı.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

KURALLAR = json.loads((Path(__file__).with_name("kurallar.json")).read_text(encoding="utf-8"))
VARSAYILAN_LOG = Path(__file__).resolve().parent / "guard.log"


def norm(s: str) -> str:
    s = s.lower().replace("/", "\\")
    s = re.sub(r"\\+", r"\\", s)
    return s


def kok_metni(kok: str) -> str:
    """Koşu kökünü sürücü harfi olmadan normalleştirir (C:\\x, /c/x ve x\\y biçimleri aynı eşleşsin)."""
    k = norm(kok)
    k = re.sub(r"^[a-z]:\\", "", k)
    k = re.sub(r"^\\[a-z]\\", "", k)
    return k.strip("\\")


def surucu_regex(harfler):
    """Yapımcıya tamamen kapalı sürücüler (ör. cevap anahtarının durduğu sürücü) için regex üretir."""
    out = []
    for h in harfler:
        h = h.lower()
        out.append(rf"(?<![a-z0-9_]){h}:(\\|/|\s|$|\"|')")
        out.append(rf"(^|[\s\"'=(:,])\\(mnt\\)?{h}(\\|$|\s)")
    return out


def karar_ver(tool: str, tinp: dict, run: str, config: str, kok: str) -> str:
    seviye = config.split("-")[-1]                   # H0 / H1 / H2
    ortak = KURALLAR["ortak"]
    blob = norm(json.dumps(tinp, ensure_ascii=False))
    blob = blob.replace('\\"', '"')

    # 1. Araç adı yasakları
    for pat in ortak["arac_yasak"]:
        if re.fullmatch(pat, tool):
            return f"deny:tool:{tool}"
    if tool.startswith("mcp__"):
        izinli = KURALLAR["mcp_izin"].get(config, [])
        if not any(tool.startswith(p) for p in izinli):
            return f"deny:mcp:{tool}"
    if seviye in ("H0", "H1"):
        for pat in KURALLAR["h0h1_arac_yasak"]:
            if re.fullmatch(pat, tool):
                return f"deny:tool:{tool}"
    h2_onek = KURALLAR.get("h2_skill_onek", "")
    if seviye == "H2" and tool == "Skill":
        ad = str(tinp.get("skill", "")).lower()
        if not (h2_onek and ad.startswith(h2_onek)):
            return f"deny:skill:{ad}"

    # 2. Kendi koşu kökünü metinden çıkar; kalan metinde yasak yer / kelime ara
    k = kok_metni(kok)
    temiz = re.sub(r"([a-z]:\\|\\[a-z]\\)?" + re.escape(k), "<KOK>", blob)

    for kelime in ortak["metin_yasak"]:
        if kelime.lower() in temiz:
            return f"deny:text:{kelime}"
    for pn in ortak["parca_no"]:
        if pn.lower() in temiz:
            return "deny:text:pn"
    for pat in ortak["regex_yasak"] + surucu_regex(ortak.get("yasak_surucu", [])):
        if re.search(pat, temiz):
            return f"deny:re:{pat[:30]}"
    # başka koşu klasörü
    for m in re.finditer(r"kosular\\(r\d{6})", blob):
        if m.group(1) != run:
            return "deny:text:baska_kosu"

    # .claude: H2'de yalnız uzman skill klasörleri
    for m in re.finditer(r"\.claude(\\[^\s\"']*)?", temiz):
        yol = m.group(0)
        if seviye == "H2" and h2_onek and yol.startswith(f".claude\\skills\\{h2_onek}"):
            continue
        return "deny:text:.claude"

    # 3. Yazma yeri: Write / Edit yalnız kendi koşu klasörüne
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        fp = norm(str(tinp.get("file_path") or tinp.get("notebook_path") or ""))
        if k not in fp:
            return "deny:write:disari"
    return "allow"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--kok", required=True, help="bu koşunun klasörü (yapımcının tek yazma yeri)")
    ap.add_argument("--log", default=str(VARSAYILAN_LOG))
    a = ap.parse_args()
    try:
        veri = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}")
    except Exception:
        veri = {}
    tool = veri.get("tool_name", "?")
    tinp = veri.get("tool_input", {}) or {}
    oturum = veri.get("session_id", "?")
    try:
        karar = karar_ver(tool, tinp, a.run, a.config, a.kok)
    except Exception as e:                            # kanca hatası: güvenli tarafta kal
        karar = f"deny:guard_hata:{type(e).__name__}"
    zaman = dt.datetime.now().isoformat(timespec="seconds")
    log = Path(a.log)
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as f:
        f.write(f"{zaman}\t{oturum}\t{a.run}\t{tool}\t{karar}\n")
    if karar != "allow":
        sys.stdout.buffer.write(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Bu işlem bu görevde kapalı (izinli alan dışı). "
                                        "Yalnız girdi klasöründeki bilgiyle ve kendi çalışma klasörünle devam et."}},
            ensure_ascii=False).encode("utf-8"))
        sys.stdout.flush()
    sys.exit(0)


if __name__ == "__main__":
    main()
