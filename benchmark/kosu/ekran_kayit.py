"""Yapımcıdan bağımsız ekran kaydı (GUI'si görünen araçta her koşu kaydedilir; yalnız Windows).

Lead başlatır / durdurur; yapımcı oturumu bunu görmez. Yalnız aracın kendi ana penceresi kaydedilir (masaüstü,
terminal, diyalog dışı pencereler girmez). Pencere koşu ortasında açılırsa (SolidWorks COM) beklenir; kapanıp yeniden
açılırsa yeni parça dosyasına geçilir (<run>.mp4, <run>_2.mp4 ...).

Kullanım: python -I ekran_kayit.py --run r123456 --arac SW|SC [--cikti <klasör>]   (durdurmak: <klasör>\\<run>.dur)
ffmpeg PATH'te olmalı ya da FFMPEG ortam değişkeniyle verilmeli.
Hafif: 10 fps, 720p yükseklik, x264 ultrafast crf 30.
"""
import argparse, ctypes, ctypes.wintypes as W, os, shutil, subprocess, time
from pathlib import Path

EKRAN_VARSAYILAN = Path(__file__).resolve().parent / "_is" / "film" / "ekran"
FFMPEG = os.environ.get("FFMPEG") or shutil.which("ffmpeg") or "ffmpeg"
SURECLER = {"SW": ["sldworks.exe"], "SC": ["solidcraft.exe", "solidcraft-gui.exe"]}

u32 = ctypes.windll.user32
k32 = ctypes.windll.kernel32
u32.SetProcessDPIAware()


def surec_adi(pid):
    h = k32.OpenProcess(0x1000, False, pid)
    if not h:
        return ""
    buf = ctypes.create_unicode_buffer(260); n = W.DWORD(260)
    ok = k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n)); k32.CloseHandle(h)
    return Path(buf.value).name.lower() if ok else ""


def pencere_bul(adlar):
    en = [None, 0]
    def cb(hwnd, _):
        if not u32.IsWindowVisible(hwnd) or u32.GetWindow(hwnd, 4):  # GW_OWNER: diyaloglar atlanır
            return True
        pid = W.DWORD(); u32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if surec_adi(pid.value) in adlar:
            r = W.RECT(); u32.GetWindowRect(hwnd, ctypes.byref(r))
            a = (r.right - r.left) * (r.bottom - r.top)
            if a > en[1]:
                en[0], en[1] = hwnd, a
        return True
    u32.EnumWindows(ctypes.WINFUNCTYPE(W.BOOL, W.HWND, W.LPARAM)(cb), 0)
    return en[0]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--arac", required=True)
    ap.add_argument("--cikti", default=str(EKRAN_VARSAYILAN))
    a = ap.parse_args()
    EKRAN = Path(a.cikti)
    EKRAN.mkdir(parents=True, exist_ok=True)
    dur = EKRAN / f"{a.run}.dur"; log = open(EKRAN / f"{a.run}.log", "a", encoding="utf-8")
    parca = 0
    while not dur.exists():
        hwnd = pencere_bul(SURECLER[a.arac])
        if not hwnd:
            time.sleep(1); continue
        parca += 1
        out = EKRAN / (f"{a.run}.mp4" if parca == 1 else f"{a.run}_{parca}.mp4")
        cmd = [FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "gdigrab", "-framerate", "10",
               "-draw_mouse", "1", "-i", f"hwnd={hwnd}", "-vf", "scale=-2:720:flags=bicubic,format=yuv420p",
               "-c:v", "libx264", "-preset", "ultrafast", "-crf", "30", str(out)]
        log.write(f"{time.strftime('%H:%M:%S')} basla {out.name} hwnd={hwnd}\n"); log.flush()
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=log)
        while p.poll() is None and not dur.exists():
            time.sleep(1)
        if p.poll() is None:
            try:
                p.stdin.write(b"q"); p.stdin.flush()
            except OSError:
                pass
            try:
                p.wait(20)
            except subprocess.TimeoutExpired:
                p.kill()
        log.write(f"{time.strftime('%H:%M:%S')} bitti {out.name} kod={p.returncode}\n"); log.flush()
    log.write(f"{time.strftime('%H:%M:%S')} durduruldu\n")


if __name__ == "__main__":
    main()
