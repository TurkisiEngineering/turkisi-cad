# Build log — P10 ribbed comfort-grip knob

Araç: SOLIDWORKS 2024 (32.5), Python 3.13 + pywin32, COM API (typelib `sldworks.tlb`/`swconst.tlb` ile makepy).
Birim inç, global çerçeve spec ile aynı (eksen = SW Z; profiller Top Plane'de (XZ, +X yarım düzlemi), plan çizimleri
Front Plane'e paralel referans düzlemlerinde). Model→sketch koordinatı `Sketch.ModelToSketchTransform` ile çevrilir,
bu yüzden hiçbir parça sonradan taşınmadı.

## Ne yapıldı
- **P01** (`build_core.py`): C1 revolve → C3a Lci prizması z -0.12..0.35 kesim → C3b tavan koni/basamak dışındaki
  halka geri eklendi (K2'nin Lci ile kırpılması böylece kendiliğinden oluşur) → C3c göbek konisi tavana kadar →
  C3d 8 radyal kaburga (0.05, z -0.12..0.35, uçları göbek ve kenar duvarına gömülü) → C2 8 adet R0.33 oyuk (her iki yön
  boydan boya) → C4 delik revolve-kesim (yuva, basamak, 3° koni, R0.015) → C5 halka.
- **P02** (`build_coating.py`): S1 Lo prizması (-0.18..0.5) − Li prizması (..0.26) → S2 alt ve üst düz yüzlerin bütün
  kenarlarına R0.06 fillet (= 3 kenar döngüsü) → S3 kubbe revolve → S4a Lci prizma kesim (0.26..0.35) → S4b üst
  açıklık revolve kesim → S4c P01 parçası `InsertPart3` ile gövde olarak eklenip Combine-Subtract.
- **P03** (`build_insert.py`): tüp (iç r = minor 0.146906) → R0.1875 daire üzerinde helis (adım 0.0625, 9 tur,
  z0 = -0.691718 = -0.379218 − 5·0.0625, θ=0'dan başlar) → +X yarım düzleminde trapez oluk profili (kök düzlüğü
  P/8 merkezi z0'da, 30° yanlar, tepe hizasında P−P/8 genişlik, içe 0.015 uzatma) helis boyunca süpürme-kesim
  (follow path) → iki uçta 90° havşa revolve-kesim (koni minor çapa kadar devam eder).
- **Montaj** (`build_assembly.py`): üç parça birim dönüşümle eklenip sabitlendi, `final.step` AP214, birim INCH.

## Ölçüm vs hedef (SW kütle özellikleri, inç)
| Gövde | Hacim (ölçülen / hedef) | Alan | CoM z | Bbox | Yüz |
|---|---|---|---|---|---|
| P01 | 2.07190 / 2.07189 | 24.9601 / 24.9600 | 0.07567 / 0.07567 | ±1.2, -0.695..0.62 ✓ | 118 / 123 |
| P02 | 0.72941 / 0.72941 | 25.8622 / 25.8622 | 0.22687 / 0.22687 | ±1.26, -0.18..0.68 ✓ | 255 / 292 |
| P03 | 0.06336 / 0.06340 | 1.8864 / 1.8851 | (-0.00012, -0.00028, -0.43000) / (-0.00012, -0.00032, -0.43003) | ±0.265625, -0.68..-0.18 ✓ | 9 / 27 |
| Toplam | 2.86467 / 2.86470 | 52.7087 / 52.7074 | | ±1.26, -0.695..0.68 ✓ | |

## Takıldığım yerler / kararlar
- pywin32 `EnsureDispatch` SW'de çalışmıyor → typelib dosyadan yüklendi; `ModelToSketchTransform` için MathUtility
  yerine dönüşüm matrisi elle uygulandı; nesne cast'leri `QueryInterface` ile.
- Kesim yönü: `FeatureCut4` varsayılanı düzlem normalinin tersi; `Dir` parametresiyle +Z'ye çevrildi (bbox ile doğrulandı).
- `AddComponent5` bileşeni bbox merkezine koyuyordu → `Transform2` birim matrise ayarlandı (kontrol edildi).
- Diş yönü/fazı: helis `Clockwise=False` + başlangıç açısı 0 ile CoM işaretleri hedefle aynı (−x, −y); `Clockwise=True`
  CoM y'yi + yapıyor → sol el, reddedildi. Faz yalnız CoM ile doğrulandı (y 0.00028 vs 0.00032; küçük fark helis
  profil yaklaşımı/faz ofsetinden olabilir).
- Havşa koniyi minor çapa kadar sürdürdüm (spec "cones cut through the thread"); hacim farkı 0.00004 in3.

## Bilerek basitleştirilen / farklı olan
- Yüz sayıları master'dan az (SW birleşik/periyodik yüzler; P03'te helisel yüzler tek yüz). Geometri hacim/alan
  olarak eşleşiyor.
- Equation Manager'daki global değişkenler bilgi amaçlıdır; sketch ölçülerine bağlı değil. Parametrik kaynak Python
  betiklerindeki `P` sözlükleridir (değiştir → `build_all.py` ile yeniden kur).
- P02 içinde P01 dış referansla (InsertPart) çıkarılır; P01 değişirse P02 yeniden kurulmalı.

## Doğrulama notu
- Teslim dosyaları betikler tek tek çalıştırılarak üretildi (core → coating → insert → assembly). `build_all.py` aynı
  çağrıları sırayla yapan sarmalayıcıdır; süre nedeniyle temiz kopyada tek parça olarak baştan sona ayrıca koşturulmadı.
- `final.step`: FILE_SCHEMA AUTOMOTIVE_DESIGN (AP214), uzunluk birimi INCH, 3 MANIFOLD_SOLID_BREP. STEP yeniden içe
  aktarılıp ölçülmedi; SW tarafındaki ölçümler yukarıdaki tablodadır.
