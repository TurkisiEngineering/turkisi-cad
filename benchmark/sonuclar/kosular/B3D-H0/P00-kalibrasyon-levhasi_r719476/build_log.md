# Build log – P01 Plate

## Yapılanlar
1. spec.md okundu; tek gövde, belirsiz madde yok.
2. `p01_plate.py` (build123d 0.11.1, BuildPart) spec sırasıyla:
   - F1: 100×60×10 kutu, XY'de merkezli, alt yüz Z=0.
   - F2: Z'ye paralel 4 düşey kenara R3 fillet (üst/alt kenarlar keskin).
   - F3: GridLocations(84, 44) ile Ø6 boydan boya 4 delik (±42, ±22).
   - F4: Z=6'dan Z=10'a Ø20 silindirik kör cep (düz taban, keskin kenarlar).
   - Gövde etiketi "P01 Plate"; `export_step` ile AP214 (AUTOMOTIVE_DESIGN şeması) `final.step`.
3. STEP yeniden içe aktarılarak doğrulandı: 1 katı, hacim 57535.133, 16 yüz.

## Takıldığım yerler
Geometride yok. Dokümanları yazarken bir shell komutu ortam kancası tarafından engellendi; dosyalar doğrudan dosya yazma aracıyla oluşturuldu.

## Bilerek basitleştirme / yorum
Yok; spec birebir uygulandı. Parçalar yerinde kuruldu, sonradan taşıma yok.

## Hedef tablosu karşılaştırması

| Ölçüt | Spec | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.133 | 0 % |
| Alan mm² | 15912.159 | 15912.159 | 0 |
| CoM X / Y / Z | 0 / 0 / 4.9345 | 0.0000 / 0.0000 / 4.9345 | 0 |
| X min/max | -50 / 50 | -50.000 / 50.000 | 0 |
| Y min/max | -30 / 30 | -30.000 / 30.000 | 0 |
| Z min/max | 0 / 10 | 0.000 / 10.000 | 0 |
| Yüz sayısı | 16 | 16 | 0 |

Tüm kabul hedefleri (hacim ±0.5 %, CoM ±0.05 mm, sınır kutusu ±0.01 mm) sağlandı.
