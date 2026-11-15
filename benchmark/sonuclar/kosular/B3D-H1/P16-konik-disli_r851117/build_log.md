# Build log — P16 miter dişli (P01)

## Yapılanlar
1. **Kütük:** spec 3.A'daki 9 noktalı (r, y) çokgen XY düzleminde (x=r) çizilip Y ekseni etrafında 360° döndürüldü.
2. **Kesici:** S_A ve S_B kesitlerinin her biri 6 kenarlı kapalı tel olarak kuruldu: kutuplar doğrudan
   `Geom_BSplineCurve` (OCP) ile, verilen düğüm vektörleriyle (6 kutup: 0,0.5(×2),1; Bezier 0,1) oluşturuldu.
   Sol yarı x→−x aynası; kenar yönleri spec'teki sıraya göre (sol yanak 6→1, sol radyus 1→6, taban, sağ radyus 6→1,
   sağ yanak 1→6, kapatma çizgisi). İki tel `Solid.make_loft(ruled=True)` ile çizgisel (ruled) katıya çevrildi;
   karşılıklı kenarlar aynı parametrede düz çizgilerle birleşir. Rulinglere ortak apeks "düzeltmesi" yapılmadı.
3. **Dizi:** kesici Y ekseni etrafında k·18° (k=0..19) döndürülüp tek seferde kütükten çıkarıldı. Boşluk +Z'de
   ortalanmış (kutuplar zaten +Z tarafında), dolayısıyla ±X, ±Z'de de boşluk var.
4. `final.step` AP214 olarak dışa aktarıldı ve tekrar içe alınarak kontrol edildi (1 katı, aynı hacim).

## Ölçüm vs hedef

| Büyüklük | Hedef | Model | Fark |
|---|---|---|---|
| Hacim mm³ | 8494.85 | 8494.78 | −0.001 % |
| Alan mm² | 3858.30 | 3858.28 | −0.0005 % |
| CoM (X,Y,Z) | (0, 9.030, 0) | (0.000, 9.030, 0.000) | 0 |
| X min/max | ±16.281 | ±16.281 | 0 |
| Y min/max | 0 / 19.330 | 0 / 19.330 | 0 |
| Z min/max | ±16.281 | ±16.281 | 0 |
| Yüz sayısı | 134 | 128 | −6 (aşağıya bkz.) |
| Topukta taban, x=0 düzleminde y=8.11 | r ≈ 13.37 | r = 13.373 | ✓ |

Geçerlilik: `is_valid=True`, tek katı.

## Takıldığım / bilerek bıraktığım noktalar
- **Yüz sayısı 128 vs 134:** 100 B-spline yüz (20 boşluk × 2 yanak + 2 radyus + taban), 20 ayrı diş ucu konik
  arazisi, ve 8 dönel yüz (arka/ön düzlem, göbek ve delik silindiri, arka koni, burun konisi, 2 pah). Geometri
  hedefle örtüşüyor (hacim/alan/CoM eşleşiyor); fark büyük olasılıkla master modelde 6 periyodik dönel yüzün dikiş
  çizgisinde ikiye bölünmüş olmasından kaynaklanıyor (pahlar, delik, göbek, arka koni, burun konisi = 6).
  Topolojiyi yapay olarak bölmedim.
- Ara kesici katısı tek başına `is_valid=False` raporluyor (ruled loft'un kapalı tel kenarlarında küçük tolerans
  meselesi olmalı) ama hacmi pozitif (99.69 mm³) ve boolean sonucu geçerli, hedeflerle uyumlu; bu yüzden bırakıldı.
- Basitleştirme yok; diş ucu pahı/kenar yuvarlatması spec gereği yok.
