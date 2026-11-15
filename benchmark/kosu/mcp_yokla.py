"""Bir stdio MCP sunucusunu başlatır, initialize + tools/list yapar, araç adlarını yazar.
Kullanım: python mcp_yokla.py <ad> -- <komut> [arg...]"""
import json, subprocess, sys, threading, time, os

ad = sys.argv[1]
cmd = sys.argv[sys.argv.index("--") + 1:]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     env={**os.environ, **json.loads(os.environ.get("YOKLA_ENV", "{}"))})
cevap = {}

def oku():
    for satir in p.stdout:
        try:
            d = json.loads(satir)
        except Exception:
            continue
        if "id" in d:
            cevap[d["id"]] = d

threading.Thread(target=oku, daemon=True).start()
def gonder(m):
    p.stdin.write((json.dumps(m) + "\n").encode()); p.stdin.flush()
gonder({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "yokla", "version": "0"}}})
t0 = time.time()
while 1 not in cevap and time.time() - t0 < 90:
    time.sleep(0.2)
gonder({"jsonrpc": "2.0", "method": "notifications/initialized"})
gonder({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
while 2 not in cevap and time.time() - t0 < 120:
    time.sleep(0.2)
p.kill()
if 2 not in cevap:
    print(ad, "CEVAP YOK", (p.stderr.read() or b"")[-800:].decode("utf-8", "replace")); sys.exit(1)
info = cevap[1].get("result", {}).get("serverInfo", {})
araclar = [t["name"] for t in cevap[2]["result"]["tools"]]
print(json.dumps({"ad": ad, "server": info, "arac_sayisi": len(araclar), "araclar": araclar}, ensure_ascii=False))
