# Build log: P01 Miter gear (P16)

Araç: SolidWorks 2024 (API rev 32.5) + Python 3.13 / pywin32 (COM). Betik: `betikler/build_gear.py`.
Tek gövde, mm, spec'in global çerçevesi (eksen = Y, arka yüz y = 0, dişler +Y yönünde).

## Ne yapıldı

1. **Gövde:** Spec 3.A'daki 9 kenarlı (r, y) poligonu Ön düzleme (global XY) çizdim ve Y ekseni etrafında 360°
   döndürdüm.
2. **Diş boşluğu kesicisi:** S_A ve S_B kesitleri iki 3B eskiz olarak kuruldu. Spline'lar
   `SketchManager.CreateSplinesByEqnParams2` ile spec'teki **kutup ve düğüm değerlerinden birebir** oluşturuldu;
   noktadan geçen interpolasyon değil. Yanaklar ve dib yuvarlatmaları 6 kutuplu kübik spline, düğüm vektörü
   (0,0,0,0,.5,.5,1,1,1,1). Kök 4 kutuplu Bezier. Sol yarı x → −x yansıması. Zincirin sırası ve yönü spec'teki gibi
   (1 → 6). Bu iki kesit arasında Loft-Kesim yapıldı. İki kesit tutarlı parametrelendiği için loft, karşılıklı
   noktaları doğrusal olarak birleştiriyor.
3. **Çoğaltma:** Y ekseni etrafında 20 adet, 18° aralıkla dairesel çoğaltma. Adet, `NTeeth` global değişkenine
   denklemle bağlı.

## Takıldığım yerler ve çözümler

- **Late-binding COM sorunları:** pywin32'nin dinamik dispatch'i bazı parametresiz metotları özellik sanıyor
  (`GetEquationMgr`, `CreateMassProperty`, `SetKnotPoints`). Çözüm: `G()` yardımcısı ve early-binding sarmalayıcı
  `typed()`. `typed()`, `gencache.EnsureModule` ile SolidWorks tip kütüphanesini kullanıyor; pywin32 bu sarmalayıcıyı
  kendi gen_py önbelleğine yazar. Bu dosyayı ben yazmadım, pywin32 otomatik üretir.
- **Loft-Kesim malzemeyi atmadı, gövdeyi böldü:** `InsertCutBlend` sonucunda iki gövde kaldı: dişli (9710.54 mm³)
  ve tam olarak diş boşluğu şeklindeki parça (63.98 mm³). Bu parça beklenen boşluk hacmine eşit:
  (9774.52 − 8494.85)/20 = 63.98. Yani geometri doğru, yalnız SolidWorks kesimi "ayırma" gibi uyguladı. Profil
  sırasını ters seçmek ve teğet birleştirmeyi değiştirmek sonucu değiştirmedi. Katı loft (`InsertProtrusionBlend2`,
  Merge = False) API'den hiç oluşmadı. **Çözüm:** kesimden sonra küçük parçayı bir **Gövde Sil/Tut** özelliğiyle
  (`Remove_SpaceSlug`) sildim. Dairesel çoğaltmanın 19 kopyası ise malzemeyi doğrudan attı; son durumda tek gövde
  kaldı. Betik çoğaltmadan sonra da gövde sayısını kontrol ediyor; fazla gövde kalırsa onları da siliyor.
- **Dairesel çoğaltma API'den `None` döndü:** `DName = "NULL"` ve `GeometryPattern = False` ile başarısız oldu.
  `DName = ""` ve `GeometryPattern = True` ile çalıştı. Betik önce geometri desenini, olmazsa normal deseni deniyor.
  Son koşuda geometri deseni kullanıldı.

## Bilerek basitleştirdiklerim / yorumlarım

- Gövde eskizi SolidWorks içinde ölçülendirilmedi. Noktalar betikteki isimli parametrelerden (`P`) hesaplanıp
  sabit çiziliyor. Global değişkenler parçada var, fakat yalnızca `NTeeth` bir özelliğe (desen adedi) denklemle
  bağlı. Ölçüleri değiştirmek için betikteki `P` değerleri değiştirilip betik yeniden çalıştırılmalı.
- Kesicinin uç kapakları (S_A / S_B yüzeyleri) gövdenin dışında kalıyor, spec'e göre sonucu etkilemiyor.
  Rulingleri ortak bir tepe noktasına "düzeltmedim"; kutuplar verildiği gibi kullanıldı.
- Malzeme (1045 çelik) atanmadı; spec'e göre yalnızca ürün verisi.

## Ölçüm ve hedef karşılaştırması

SolidWorks kütle özellikleri (B-rep) ile ölçüldü. Yüz sayısı STEP'teki `ADVANCED_FACE` sayısıdır.

| Büyüklük | Hedef | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 8494.85 | 8494.79 | −0.06 (−0.0007 %) |
| Alan mm² | 3858.30 | 3858.28 | −0.02 (−0.0005 %) |
| CoM X | 0.000 | 0.000 | 0 |
| CoM Y | 9.030 | 9.030 (9.02999) | 0 |
| CoM Z | 0.000 | 0.000 | 0 |
| Xmin / Xmax | ∓16.281 | ∓16.2811 | 0 |
| Ymin / Ymax | 0.000 / 19.330 | 0.000 / 19.330 | 0 |
| Zmin / Zmax | ∓16.281 | ∓16.2811 | 0 |
| Yüz sayısı | 134 | STEP'te 134 (SolidWorks içinde 128) | 0 |
| Gövde sayısı | 1 | 1 | — |

Yüz sayısı notu: SolidWorks içindeki 128 yüz şöyle dağılıyor: gövdenin 9 dönel/düzlem yüzü + 20 × 5 boşluk yüzü
(2 yanak, 2 dib yuvarlatması, 1 kök) + diş üstü konisinin 20 ayrı şeride bölünmesiyle gelen +19. STEP'e yazılırken
SolidWorks kapalı (360°) dönel yüzlerin bir kısmını ikiye bölüyor ve sayı 134'e çıkıyor; bu, hedefle birebir aynı.

Kontrol değerleri: toplam genişlik 19.33, göbek Ø25 × 7.75, delik Ø8 boydan boya, iki uçta 0.4 × 45° pah, ön yüz
y = 18 (r 4.4 → 8.5), topuk dış çapı 32.77 (köşe r = 16.385, y = 9.36), 20 diş. Sınır kutusu X/Z yönünde ±16.281;
spec'te belirtildiği gibi ±X ve ±Z eksenlerinde diş boşluğu bulunduğu için 32.77'den küçük.

STEP: `final.step`, şema AUTOMOTIVE_DESIGN (AP214), uzunluk birimi mm, 1 MANIFOLD_SOLID_BREP.
