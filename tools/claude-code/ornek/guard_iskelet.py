"""PreToolUse guard kancasının en kısa hali (öğretim amaçlı iskelet).

Claude Code her araç çağrısından önce bu betiği çalıştırır ve çağrıyı JSON olarak stdin'e verir:
    {"session_id": "...", "tool_name": "Bash", "tool_input": {"command": "..."}}
Betik hiçbir şey yazmazsa çağrı geçer. Aşağıdaki "deny" JSON'unu yazarsa çağrı reddedilir ve gerekçe ajana gider.

Bağlama: settings.json -> hooks.PreToolUse -> {"matcher": "*", "hooks": [{"type": "command",
         "command": "python -I <GUARD_KLASÖRÜ>/guard_iskelet.py --run <run_id> --config SW-H1
                     --kok <KÖK>/kosular/<run_id> --log <KÖK>/kayit/guard.log"}]}
Argümanlar yayındaki tam guard'la (benchmark/kosu/guard/guard.py) aynıdır. Betik ve log koşu klasörünün DIŞINDA durmalı.

Yayında kullanılan tam guard (config'e göre MCP izni, H0/H1 skill yasağı, log) benchmark/kosu/ klasöründe.
"""
import argparse
import datetime as dt
import json
import re
import sys

YASAK_ARACLAR = {"WebSearch", "WebFetch", "Skill", "Agent", "Task"}
# config -> izinli MCP sunucusu (H0'da yok)
MCP_IZIN = {"SW-H1": "solidworks", "B3D-H1": "build123d", "SC-H1": "solidcraft"}
YASAK_DESENLER = [r"\bcurl\b", r"\bwget\b", r"invoke-webrequest", r"\bpip3?\s+install", r"\bnpm\s+(i|install)\b",
                  r"\bgit\s+clone\b", r"\.\.[\/]\.\."]


def karar(arac: str, girdi: dict, kok: str, izinli_mcp: str) -> str:
    if arac in YASAK_ARACLAR:
        return "araç kapalı"
    if arac.startswith("mcp__") and not (izinli_mcp and arac.startswith(f"mcp__{izinli_mcp}__")):
        return "bu MCP kapalı"
    metin = json.dumps(girdi, ensure_ascii=False).lower()
    for desen in YASAK_DESENLER:
        if re.search(desen, metin):
            return "yasak komut"
    if arac in ("Write", "Edit"):
        yol = str(girdi.get("file_path", "")).lower().replace("\\", "/")
        if not yol.startswith(kok.lower().replace("\\", "/")):
            return "koşu klasörü dışına yazma"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="koşu kimliği")
    ap.add_argument("--config", required=True, help="ör. SW-H1, B3D-H0")
    ap.add_argument("--kok", required=True, help="yapımcının yazabileceği tek klasör")
    ap.add_argument("--log", default="", help="kararların yazılacağı log dosyası (koşu klasörü dışında)")
    a = ap.parse_args()
    veri = {}
    try:
        veri = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}")
        neden = karar(veri.get("tool_name", ""), veri.get("tool_input") or {}, a.kok, MCP_IZIN.get(a.config, ""))
    except Exception:
        neden = "kanca hatası"            # hata olursa güvenli tarafta kal: reddet
    if a.log:
        with open(a.log, "a", encoding="utf-8") as f:
            satir = [dt.datetime.now().isoformat(timespec="seconds"), veri.get("session_id", "?"), a.run,
                     veri.get("tool_name", "?"), "deny:" + neden if neden else "allow"]
            f.write("\t".join(satir) + "\n")
    if neden:
        cikti = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                        "permissionDecisionReason": f"Bu işlem bu görevde kapalı ({neden})."}}
        sys.stdout.buffer.write(json.dumps(cikti, ensure_ascii=False).encode("utf-8"))


if __name__ == "__main__":
    main()
