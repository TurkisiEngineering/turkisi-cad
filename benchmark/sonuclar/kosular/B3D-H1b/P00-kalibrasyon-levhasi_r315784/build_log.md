# Build log — P01 Plate

## Yapılanlar
Tek betik `plate.py` (build123d 0.11.1, algebra API), spec'teki sırayla:
1. F1: `Box(100, 60, 10)`, XY'de merkezli, alt yüz Z = 0.
2. F2: Z'ye paralel 4 dikey kenara R3 fillet (üst/alt kontur kenarları keskin).
3. F3: (±42, ±22) merkezli 4 adet Ø6 silindir, Z = 0..10 çıkarıldı (boydan boya).
4. F4: Ø20 silindir, Z = 6..10, eksen Z ekseni; düz taban, keskin kenarlar.
Gövde etiketi "P01 Plate"; tek solid; `export_step` ile AP214 (AUTOMOTIVE_DESIGN şeması) yazıldı.
Parçalar yerinde kuruldu, sonradan taşıma yok.

## Takılmalar / basitleştirmeler / varsayımlar
Yok. Spec eksiksizdi (Bölüm 5: belirsiz madde yok). Hiçbir özellik basitleştirilmedi.

## Ölçüm vs. hedef (plate.py çıktısı; STEP yeniden okununca hacim aynı: 57535.133, 1 solid)

| Büyüklük | Hedef | Ölçülen | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.133 | 0.000 % |
| Alan mm² | 15912.159 | 15912.159 | 0 |
| CoM X/Y/Z | 0.0000 / 0.0000 / 4.9345 | 0.0000 / 0.0000 / 4.9345 | 0 |
| X min/max | -50 / 50 | -50.000 / 50.000 | 0 |
| Y min/max | -30 / 30 | -30.000 / 30.000 | 0 |
| Z min/max | 0 / 10 | 0.000 / 10.000 | 0 |
| Yüz sayısı | 16 | 16 | 0 |
| Solid sayısı | 1 | 1 | — |

Tüm kabul kriterleri (hacim ±0.5 %, CoM ±0.05 mm, kutu ±0.01 mm) sağlandı.
