"""guard.py birim testi. Çalıştırma: python test_guard.py  (bu klasörde)

kurallar.json'daki yer tutucuların yerine test değerleri koyar (yasak sürücü "q", katalog numarası "ORNEK123",
satıcı adı "katalogsitesi", cevap anahtarı klasörü "gizli-cevaplar") ve her kararı beklenenle karşılaştırır.
"""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402

K = copy.deepcopy(guard.KURALLAR)
K["ortak"]["yasak_surucu"] = ["q"]
K["ortak"]["parca_no"] = ["ORNEK123"]
K["ortak"]["metin_yasak"] = [k for k in K["ortak"]["metin_yasak"] if not k.startswith("<")] + [
    "katalogsitesi", "gizli-cevaplar", "is-koku"]
K["h2_skill_onek"] = "uzman-"
K["mcp_izin"]["UZ-H2"] = []
guard.KURALLAR = K

RUN = "r000001"
KOK = r"C:\is-koku\kosular\r000001"


def t(cfg, tool, inp, beklenen):
    karar = guard.karar_ver(tool, inp, RUN, cfg, KOK)
    ok = (karar != "allow") == (beklenen == "deny")
    print(("OK  " if ok else "FAIL"), cfg, tool, beklenen, karar, str(inp)[:70])
    return ok


c = [
    ("B3D-H0", "Read", {"file_path": KOK + r"\girdi\spec.md"}, "allow"),
    ("B3D-H0", "Write", {"file_path": KOK + r"\teslim\final.py", "content": "from build123d import *"}, "allow"),
    ("B3D-H0", "Bash", {"command": "cd /c/is-koku/kosular/r000001 && python teslim/final.py"}, "allow"),
    ("SW-H1", "mcp__solidworks__create_part", {}, "allow"),
    ("UZ-H2", "Skill", {"skill": "uzman-modelleme"}, "allow"),
    ("B3D-H0", "Bash", {"command": "python -c \"d = {1: 2}; print(d)\""}, "allow"),
    ("B3D-H0", "Read", {"file_path": r"Q:\gizli-cevaplar\index.csv"}, "deny"),
    ("B3D-H0", "Glob", {"pattern": "**/*.STEP", "path": "C:/ev/kullanici/Desktop"}, "deny"),
    ("B3D-H0", "Glob", {"pattern": "**/*.STEP", "path": "Q:/"}, "deny"),
    ("B3D-H0", "Bash", {"command": "dir Q:\\"}, "deny"),
    ("B3D-H0", "Bash", {"command": "ls /q/gizli*"}, "deny"),
    ("B3D-H0", "Read", {"file_path": r"C:\is-koku\paketler\P1\_gizli\hedef.json"}, "deny"),
    ("B3D-H0", "Read", {"file_path": r"C:\baska\kosular\r123456\teslim\final.py"}, "deny"),
    ("B3D-H0", "Bash", {"command": "ls ../../paketler"}, "deny"),
    ("B3D-H0", "Bash", {"command": "cd .. && ls"}, "deny"),
    ("B3D-H0", "WebSearch", {"query": "internal gear step"}, "deny"),
    ("B3D-H0", "WebFetch", {"url": "https://example.com"}, "deny"),
    ("B3D-H0", "Bash", {"command": "curl https://www.example.com/x.step -o x.step"}, "deny"),
    ("B3D-H0", "PowerShell", {"command": "Invoke-WebRequest -Uri https://x.com"}, "deny"),
    ("B3D-H0", "Bash", {"command": "pip install cadquery"}, "deny"),
    ("B3D-H0", "Write", {"file_path": KOK + r"\a.py", "content": "import urllib.request"}, "deny"),
    ("B3D-H0", "Grep", {"pattern": "ORNEK123", "path": "C:/"}, "deny"),
    ("B3D-H0", "Bash", {"command": "echo katalogsitesi"}, "deny"),
    ("B3D-H0", "Skill", {"skill": "herhangi-bir-skill"}, "deny"),
    ("B3D-H1", "Agent", {"prompt": "x", "subagent_type": "cad-designer"}, "deny"),
    ("B3D-H0", "Read", {"file_path": r"C:\ev\kullanici\.claude\skills\x\SKILL.md"}, "deny"),
    ("UZ-H2", "Skill", {"skill": "baska-skill"}, "deny"),
    ("SW-H0", "mcp__solidworks__create_part", {}, "deny"),
    ("B3D-H1", "mcp__freecad__execute_code", {}, "deny"),
    ("B3D-H1", "mcp__claude-in-chrome__navigate", {"url": "x"}, "deny"),
    ("B3D-H0", "Write", {"file_path": r"C:\temp\x.py", "content": "x"}, "deny"),
]
n = sum(t(*x) for x in c)
print(n, "/", len(c))
sys.exit(0 if n == len(c) else 1)
