"""Kurulum denemesi: ortasında delik olan bir plaka kurar, final.step yazar.

Çalıştırma (bu klasörde):  python plaka.py
Beklenen: final.step oluşur; hacim yaklaşık 31095,2 mm³ yazılır.
"""
from build123d import Box, BuildPart, Cylinder, Mode, Align, export_step

# İsimli parametreler (mm)
BOY = 80.0        # X
EN = 50.0         # Y
KALINLIK = 8.0    # Z
DELIK_CAP = 12.0  # orta delik

with BuildPart() as plaka:
    Box(BOY, EN, KALINLIK, align=(Align.CENTER, Align.CENTER, Align.MIN))
    Cylinder(DELIK_CAP / 2, KALINLIK, align=(Align.CENTER, Align.CENTER, Align.MIN), mode=Mode.SUBTRACT)

govde = plaka.part
print(f"hacim = {govde.volume:.1f} mm3, govde sayisi = {len(govde.solids())}")
export_step(govde, "final.step")
print("final.step yazildi")
