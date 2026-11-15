# Build log: rod end, 1/2-20 male shank (r820448)

Araç: build123d 0.11.1 (Python, OCCT). Kaynak: `rod_end.py` (model + STEP), `check.py` (ölçüm).
Birim inç; global çerçeve spec'teki gibi; her şey yerinde kuruldu (identity placement).

## Ne yaptım
**P01 gövde**
1. F1 küre R0.75 @ (0,1,0) ∪ F2 boyun (r=0.75-√(0.25-y²) yayı, y 0…0.4, Y etrafında döndürme).
2. F3: YZ düzleminde "tutulacak bölge" poligonu (|z| ≤ min(0.22656, 0.25-0.25866y)), X boyunca extrude, kesişim.
3. F4: R0.5625 yuva küresi çıkarıldı (her iki düzlükte açılır).
4. F5: şaft r=0.25 silindiri; helisel oluk (dip düzlüğü P/8, 30° yanaklar) Frenet sweep ile kuruldu,
   sağ el, faz: +X tarafında dip merkezi y = 0.003125 - 0.05k. Çıkış: oluk kesicisinden r ≤ 0.25+y konisi
   çıkarıldı (koni içi kesilmez). Alt uç: Ø0.41 düz disk + 45° pah (dişi tam derinlikte keser).
**P02 bilye**: küre R0.5625 ∪ silindir R0.35 (z ±0.625) − Ø0.5 delik, iki ucunda 45°×0.025 pah.
**STEP**: AP214 (`AUTOMOTIVE_DESIGN`), uzunluk birimi INCH (`write.step.unit=INCH`), 2 katı, isimli.

## Takıldığım yerler
- `intersect()` bir ShapeList döndürdü → tek katıya çeviren `one()` yardımcı fonksiyonu.
- STEP ilk denemede mm olarak yazıldı (geometri doğru ölçeklenmişti). Spec birimine uymak için
  `write.step.unit = INCH` ayarlandı; dosyada `CONVERSION_BASED_UNIT('INCH')` doğrulandı.
- Helisel kesim, sessizce hiçbir şey kesmeyen booleanlar verdi. Sebepleri ve çözümleri:
  a) profil sırasının sweep'te ters yönlü (negatif hacimli) katı vermesi → nokta sırası ters çevrildi, hacim > 0 kontrolü;
  b) profil köşesi tam tepe yarıçapında olunca helis kenarı silindir yüzeyinin üstünde kalıyordu → yanak 0.003 öteye uzatıldı;
  c) tek parça 38 turluk sweep'in B-spline yaklaşımı boolean'ı bozuyordu → 2 × 19 tur segment;
  d) helisel kesicinin şaft uç yüzünü/pahını kestiği boolean başarısızdı → kütük 0.3 uzun yapıldı, diş açıldı,
     sonra uç yüz + pah bir dönel kesimle kırpıldı. Her segment için kesilen hacim > 0 assert'i var.

## Bilinçli basitleştirme / yorumlar
- Faz 0.0031 → 0.003125 (=P/16) alındı; spec'teki -0.0219 (= -0.021875) ve 0.0156 (= 0.015625) ile tutarlı.
- Helis yüzeyleri OCCT sweep'inden gelen B-spline yaklaşımlarıdır (kesin helikoid değil); hacim hatası ihmal edilebilir.
- Oluğun üst ucu helis sweep'in kendi uç yüzüyle değil, 45° çıkış konisiyle bitiyor (spec'teki gibi).
- Bilyedeki ~120 dejenere yüz (master export artefaktı) üretilmedi. Yüz sayıları farklı (P01 51 vs 85, P02 8 vs 14 gerçek yüz):
  OCCT sweep yüzleri tur başına bölmüyor, küre/silindir yüzleri dikiş ile bölünmüyor; yüz sayısı spec'te yalnız bilgi amaçlı.
- Liner, maks. salınım açısı vb. modellenmedi (spec'e uygun).

## Hedef tablosuyla karşılaştırma (kendi ölçümüm, `check.py`)
| Gövde | Hacim in³ (hedef) | Δ | Alan in² (hedef) | Δ | CoM (hedef) | ΔCoM | BBox maks. sapma |
|---|---|---|---|---|---|---|---|
| P01 | 0.69392 (0.69442) | −0.072 % | 9.8312 (9.8350) | −0.04 % | (0, 0.1935, 0) ((0, 0.1926, 0)) | 0.0009 in | 0.0000 in |
| P02 | 0.59227 (0.59227) | 0.000 % | 6.2209 (6.2209) | 0.00 % | (0, 1.0000, 0) | 0.0000 in | 0.0000 in |
| Toplam | 1.28619 (1.28669) | −0.04 % | 16.0521 (16.0559) | −0.02 % | y 0.5649 (0.5642) | 0.0007 in | X ±0.75, Y −1.625…1.75, Z ±0.625 |

Tümü tolerans içinde (hacim < %0.5, CoM < 0.02 in, bbox < 0.005 in). Her iki katı `is_valid=True`.
Bilye–yuva girişim hacmi 0.0. STEP geri okundu: 2 katı, hacimler 11371.32 mm³ ve 9705.56 mm³ (hedef 11379.47 / 9705.56).
Diş kontrolü (nokta sorgusu, r=0.23): +X dip y=-0.2469 boş, tepe y=-0.2719 dolu; −Z dip y=-0.2344 boş, +Z dip y=-0.2594 boş
→ sağ el ve faz doğru. Çıkış: y=-0.005, r=0.24 dolu (koni içinde kesilmemiş).
