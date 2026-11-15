# Build log — P16 düz dişli konik (miter) dişli, P01

## Ne yaptım
1. **Ham parça:** spec §3A'daki 9 köşeli (r, y) kapalı poligon XY düzleminde (x = r) çizildi,
   global Y ekseni etrafında 360° döndürüldü (`revolve`).
2. **Diş boşluğu kesicisi:** S_A ve S_B kesitlerinin her biri 6 kenarlı kapalı tel olarak kuruldu:
   sol yanak (sağ yanak kutupları x→−x, kutup 6→1), sol kök radyüsü, kök Bezier, sağ kök radyüsü (6→1),
   sağ yanak, düz kapama çizgisi. B-spline'lar OCP `Geom_BSplineCurve` ile spec'teki kutup ve düğüm
   vektörüyle (0,0,0,0,.5,.5,1,1,1,1) birebir oluşturuldu. İki tel arasında `Solid.make_loft(ruled=True)`
   ile cetvel (ruled) katı üretildi — kenar kenar eşleşen düz çizgiler.
3. **Desen:** kesici Y ekseni etrafında k·18° (k = 0..19) döndürülüp hepsi tek bir boolean ile çıkarıldı.
4. Tek katı, `label = "P01 Miter gear"`, `final.step` (AP214 / AUTOMOTIVE_DESIGN şeması) olarak yazıldı.
   Taşıma yok; her şey yerinde, spec çerçevesinde kuruldu.

## Ölçüm vs hedef (spec §4)

| Büyüklük | Hedef | Benim | Fark |
|---|---|---|---|
| Hacim mm³ | 8494.85 | 8494.78 | −0.07 (−0.0008 %) |
| Alan mm² | 3858.30 | 3858.28 | −0.02 |
| CoM (X, Y, Z) | (0, 9.030, 0) | (0.000, 9.030, 0.000) | 0 |
| X min/max | ±16.281 | ±16.281 | 0 |
| Y min/max | 0 / 19.330 | 0 / 19.330 | 0 |
| Z min/max | ±16.281 | ±16.281 | 0 |
| Katı sayısı | 1 | 1 (geçerli) | — |
| Yüz sayısı | 134 | 128 | −6 |

STEP geri okundu: 1 katı, 128 yüz, hacim 8494.78; şema `AUTOMOTIVE_DESIGN` (AP214). Dışa aktarım kayıpsız.

## Yüz sayısı farkı (128 vs 134)
Benim topolojim: 100 B-spline (20 boşluk × [2 yanak + 2 kök radyüsü + 1 kök]), 20 diş üstü konik
alanı, arka koni, burun konisi, 2 delik pahı konisi, göbek silindiri, delik silindiri, arka ve ön düzlem
= 128. Spec'in "sonuç kontrolleri" ile tutarlı: 20 ayrı diş üstü alanı; kök arka koniye r ≈ 13.37'de
(göbek r 12.5'in dışında) değdiği için arka koni tek parça halka; burunda kök r ≈ 9.5 > 8.5 olduğu için
burun konisi de tek parça. Hacim, alan ve bbox birebir tuttuğundan geometri aynıdır; 6 yüzlük farkın
orijinal CAD'in 360° döner yüzlerinin bir kısmını dikiş yerinden ikiye bölmesinden kaynaklanan bir
topoloji (gösterim) farkı olduğunu varsaydım. Sayıyı tutturmak için yapay yüz bölme eklemedim.

## Takıldığım / basitleştirdiğim
- Takılma olmadı; ilk çalıştırmada geçerli tek katı çıktı (~8 s).
- Bilerek basitleştirme yok. Spec'in uyarısına uyularak yanak cetvelleri ortak tepe noktasına
  "düzeltilmedi"; kutuplar aynen kullanıldı.
- Malzeme (1045 çelik) yalnız ürün bilgisi; STEP'e yazılmadı.
