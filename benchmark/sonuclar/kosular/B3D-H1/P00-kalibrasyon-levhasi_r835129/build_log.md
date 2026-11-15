# Build log — P01 Plate

## Yapılanlar
- `plate.py` (build123d 0.11.1, BuildPart) yazıldı; spec'in global çerçevesinde, yerinde kuruldu (taşıma yok).
  - F1+F2: `RectangleRounded(100, 60, 3)` XY düzleminde, Z=0..10 ekstrüzyon. Bu, blok + 4 dikey kenara R3 fillet ile
    geometrik olarak özdeştir (köşe merkezleri ±47, ±27); üst/alt kontur kenarları keskin.
  - F3: `GridLocations(84, 44, 2, 2)` ile 4 adet Ø6 delik, Z=0..10 çıkarıldı.
  - F4: Z=10 düzleminden Ø20 daire, −4 mm ekstrüzyonla çıkarıldı (düz taban Z=6, keskin kenarlar).
- `final.step` AP214 (AUTOMOTIVE_DESIGN şeması) olarak yazıldı, etiket "P01 Plate"; yeniden içe aktarılıp hacim
  doğrulandı (57535.133 mm³, 1 solid).

## Takılmalar
- Betikte `is_valid` özelliğini metot gibi çağırmıştım (0.11.1'de property); düzeltildi.
- Dokümanları tek bir kabuk komutuyla (heredoc) yazma denemesini ortam kancası engelledi; dosyalar doğrudan
  dosya yazma aracıyla oluşturuldu. Modele etkisi yok.

## Basitleştirmeler / yorumlar
- Yok. Spec'te belirsiz madde yok.

## Hedef tablo karşılaştırması

| Ölçü | Spec | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.133 | 0 |
| Alan mm² | 15912.159 | 15912.159 | 0 |
| CoM X/Y/Z | 0 / 0 / 4.9345 | 0.0000 / -0.0000 / 4.9345 | 0 |
| BBox | (-50,-30,0)-(50,30,10) | (-50,-30,0)-(50,30,10) | 0 |
| Yüz sayısı | 16 | 16 | 0 |
| Geçerlilik | — | valid, 1 solid | — |

Tüm kabul kriterleri (hacim ±%0.5, CoM ±0.05 mm, bbox ±0.01 mm) sağlandı.
