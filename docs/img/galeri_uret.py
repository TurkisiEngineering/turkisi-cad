"""README görselleri: panel/varlik.js'teki 45 parça render'ından
docs/img/banner.png ve docs/img/parcalar/P##.webp kartlarını üretir.

    python docs/img/galeri_uret.py
"""
import base64, csv, io, json, re, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KOK = Path(__file__).resolve().parents[2]
CIKTI = KOK / "docs" / "img"
FONT = "C:/Windows/Fonts/bahnschrift.ttf"   # değişken font: ağırlık/genişlik ismiyle seçilir

BG, BG2, IZGARA = (18, 26, 38), (24, 34, 50), (30, 41, 58)
LIME, CYAN, BEYAZ, GRI = (230, 255, 46), (34, 211, 238), (240, 244, 248), (150, 163, 180)
KIRMIZI, MAVI = (220, 38, 70), (52, 97, 160)


def font(boy, stil="Bold"):
    f = ImageFont.truetype(FONT, boy)
    try:
        f.set_variation_by_name(stil)
    except Exception:
        pass
    return f


def renderlar():
    s = (KOK / "panel" / "varlik.js").read_text(encoding="utf8")
    r = json.loads(re.search(r"var RESIM = (\{.*?\});", s, re.S).group(1))
    return {k: Image.open(io.BytesIO(base64.b64decode(v.split(",", 1)[1]))).convert("RGBA")
            for k, v in r.items()}


def kirp(im):
    return im.crop(im.getbbox())


def golge(im, r=10, op=110):
    a = im.split()[-1].point(lambda v: op if v > 0 else 0)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.putalpha(a)
    return sh.filter(ImageFilter.GaussianBlur(r))


def izgara(im, adim=40):
    d = ImageDraw.Draw(im)
    for x in range(0, im.width, adim):
        d.line([(x, 0), (x, im.height)], fill=IZGARA)
    for y in range(0, im.height, adim):
        d.line([(0, y), (im.width, y)], fill=IZGARA)


def etiket(d, xy, metin, f, bg, fg):
    x, y = xy
    w = d.textlength(metin, font=f)
    asc, desc = f.getmetrics()
    h = asc + 4
    nokta = metin.startswith("● ")
    if nokta:
        metin = metin[2:]
        w = d.textlength(metin, font=f) + 22
    d.rounded_rectangle([x, y, x + w + 28, y + h + 18], 6, fill=bg)
    if nokta:
        cy = y + (h + 18) / 2
        d.ellipse([x + 14, cy - 6, x + 26, cy + 6], fill=fg)
        d.text((x + 36, y + 11), metin, font=f, fill=fg)
    else:
        d.text((x + 14, y + 11), metin, font=f, fill=fg)
    return x + w + 28


def kart(im, kod, boyut=(360, 300)):
    W, H = boyut
    k = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, W - 1, H - 1], 18, fill=255)
    zemin = Image.new("RGBA", (W, H), BG)
    izgara(zemin, 24)
    # ortadan hafif aydınlık
    isik = Image.new("L", (W, H), 0)
    ImageDraw.Draw(isik).ellipse([W * .1, H * .1, W * .9, H * .95], fill=70)
    zemin = Image.composite(Image.new("RGBA", (W, H), (44, 60, 84)), zemin, isik.filter(ImageFilter.GaussianBlur(50)))
    k.paste(zemin, (0, 0), m)
    p = kirp(im)
    if max(p.width, p.height) > 5 * min(p.width, p.height):  # çok ince parçayı çapraz yatır
        p = kirp(p.rotate(-40 if p.height > p.width else 25, Image.BICUBIC, expand=True))
    p.thumbnail((W - 56, H - 70), Image.LANCZOS)
    x, y = (W - p.width) // 2, (H - p.height) // 2 + 14
    k.alpha_composite(golge(p, 8, 120), (x + 6, y + 10))
    k.alpha_composite(p, (x, y))
    d = ImageDraw.Draw(k)
    etiket(d, (14, 14), kod, font(22, "Bold"), LIME, BG)
    return k


def banner(R, plan):
    W, H = 1760, 720
    im = Image.new("RGBA", (W, H), BG)
    izgara(im)
    # sağda render mozaiği
    random.seed(23)
    sira = [plan[p] for p in sorted(plan)]
    sec = ["fren", "pres", "kriko", "disli_pompa", "isi_emici", "ic_disli", "doner_mandal", "kabin_rafi",
           "konik_disli", "merdiven", "fan", "tork_sinir", "araba", "teker", "yatak", "rot_basi",
           "silindir", "halka", "capraz_disli", "motor", "abs_kutu", "topuz", "kardan", "igne_valf"]
    sec = [s for s in sec if s in R] + [s for s in sira if s not in sec]
    kat = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    hucre, x0, y0, kol = 175, 860, -20, 6
    for i, key in enumerate(sec[:30]):
        r_, c_ = divmod(i, kol)
        p = kirp(R[key])
        p.thumbnail((hucre * 1.25, hucre * 1.25), Image.LANCZOS)
        cx = x0 + c_ * hucre + (hucre // 2 if r_ % 2 else 0) + random.randint(-10, 10)
        cy = y0 + r_ * (hucre * .86) + random.randint(-8, 8)
        kat.alpha_composite(golge(p, 9, 140), (int(cx - p.width / 2 + 8), int(cy + 12)))
        kat.alpha_composite(p, (int(cx - p.width / 2), int(cy)))
    # sola doğru söndür
    maske = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(maske)
    for xx in range(W):  # x<760 görünmez, 1060'tan sonra tam
        md.line([(xx, 0), (xx, H)], fill=int(255 * min(1, max(0, (xx - 760) / 300)) ** 1.4))
    a = kat.split()[-1]
    kat.putalpha(Image.composite(a, Image.new("L", (W, H), 0), maske))
    im.alpha_composite(kat)
    d = ImageDraw.Draw(im)
    f_t = font(24, "Bold")
    x = etiket(d, (64, 78), "● CANLI · 11.11.2026", f_t, KIRMIZI, BEYAZ)
    x = etiket(d, (x + 12, 78), "F23 · AGENTIC CAD LİGİ", f_t, MAVI, BEYAZ)
    # başlık: sayılar lime
    y = 150
    for satir in [[("4", LIME), (" CAD,", BEYAZ)], [("5", LIME), (" yarışmacı,", BEYAZ)], [("45", LIME), (" parça.", BEYAZ)]]:
        xx = 60
        for t, c in satir:
            f = font(118, "Bold SemiCondensed")
            d.text((xx, y), t, font=f, fill=c)
            xx += d.textlength(t, font=f)
        y += 122
    f_a = font(32, "SemiLight")
    d.text((66, y + 34), "Aynı yapay zekâ modeli, farklı CAD araçları.", font=f_a, fill=BEYAZ)
    d.text((66, y + 78), "Her parça yalnız yazılı bir spec'ten, kör çizilir.", font=f_a, fill=GRI)
    d.text((66, H - 58), "TÜRKİŞİ ENGINEERING", font=font(22, "Bold"), fill=CYAN)
    return im.convert("RGB")


def main():
    R = renderlar()
    plan = json.loads((CIKTI / "parcalar.json").read_text(encoding="utf8"))
    (CIKTI / "parcalar").mkdir(exist_ok=True)
    for p, key in plan.items():
        kart(R[key], p).save(CIKTI / "parcalar" / f"{p}.webp", quality=88, method=6)
    banner(R, plan).save(CIKTI / "banner.png", optimize=True)
    print("tamam:", len(plan), "kart + banner")


if __name__ == "__main__":
    main()
