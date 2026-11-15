# build_log — P10 tırtıllı kavrama topuzu (build123d 0.11.1, inç)

## Ne yaptım
- `params.py` (isimli ölçüler) + `knob.py` (kurulum + STEP). Bütün gövdeler spec çerçevesinde yerinde kuruldu,
  hiçbir taşıma yok. (r, z) profilleri XZ düzleminde (x = r) çizilip Z ekseni etrafında 360° döndürüldü; plan
  konturları (L0, Lci, Lo, Li) daire − 8 disk, gerektiğinde `Face.fillet_2d(0.1)` ile köşe yuvarlatma.
- **P01 çekirdek:** C1 döndürme → C2 8 silindir oyuk → C3 boşluk K = (K1 ∪ K2) − göbek konisi − 4 levha kaburga →
  C4 yuva + konik delik + R0.015 → C5 halka çıkıntı (birleştirme).
- **P02 kaplama:** S1 Lo prizması − Li prizması → S2 z=-0.18 ve z=0.5'teki bütün yatay kenarlara R0.06 (üç halka) →
  S3 kubbe başlığı → S4 Lci prizması (0.26..0.35), üst açıklık döndürmesi, bitmiş çekirdek çıkarıldı.
- **P03 insert:** manşon (R0.265625 − major R0.1875 silindiri) + diş sırtı (malzeme) + iki 90° havşa.
  Diş sırtı, 4 adet tam helis kenarı (`Edge.make_helix`, sağ el, adım 0.0625) arasında **ruled yüzeylerle**
  (`Face.make_surface_from_curves`) ve iki düz uç kapakla kapalı kabuk → Solid; insert boyundan uzun kurulup
  dış silindirle kesişimle kırpıldı.
- STEP: AP214 (AUTOMOTIVE_DESIGN), `xstep.cascade.unit = write.step.unit = INCH` → dosyada `CONVERSION_BASED_UNIT('INCH')`,
  koordinatlar inç değerleriyle aynen. 3 ayrı MANIFOLD_SOLID_BREP.

## Takıldığım yerler
1. Göbek ucu R0.02'nin merkezini ilk denemede r = 0.625 − 0.02 = 0.605 aldım; spec 0.606021 diyor (yuvarlatma 3°
   koniye teğet). Merkezi koniye dik ofsetle hesaplayınca çekirdek hacmi/alanı birebir tuttu.
2. Diş: profili helis boyunca `sweep(is_frenet=True)` ile süpürmek geçerli bir katı verdi ama manşondan çıkarma /
   birleştirme boolean'ları sessizce başarısız oldu (oluk kesilmedi, ya da Null shape). Çözüm: helis kenarları
   arasında ruled yüzeylerle kurulan sırt + "boşluk yerine malzeme" yaklaşımı (spec'in master tarifiyle de uyumlu:
   tepe ve yanaklar helisel serbest yüzey, dip silindir).
3. Havşalar: önce koniyi yalnız 0.03125 derinliğe kadar (r 0.1875'te düz tabanla) kestim → hacim 0.00062 fazla çıktı.
   "Koniler dişi keser" ifadesini, 45° koninin dişin içinden minör çapa kadar devam etmesi olarak yorumladım
   (kesici = uç yüzden tepesine kadar tam koni). Hacim 0.06402 → 0.06336, alan 1.9391 → 1.8865 oldu (hedef
   0.06340 / 1.8851).
4. Oturum içindeki ölçüm çekirdeğin CoM z'sini 0.07558 verdi (kubbe yüzeyi BSpline "REVOLUTION" yüzeyi; OCC
   integrasyonu bunu tam yakalamıyor). Aynı geometri STEP'ten okunduğunda 0.07567, yani hedefle aynı. Aşağıdaki tablo
   teslim edilen `final.step`'in yeniden okunmasıyla ölçüldü.

## Bilerek yaptığım yorumlar / basitleştirmeler
- Diş sırtının tabanı manşon duvarına 0.005 gömülü kuruldu ve birleştirildi; sonuç geometrisine etkisi yok.
- Diş tepe/yanak yüzeyleri tam helisel ruled yüzeyler (spec: "any exact helical representation is fine").
- Yüz sayıları master'dan az (çekirdek 110/123, kaplama 255/292, insert 16/27). build123d boolean sonrası aynı
  alandaki yüzleri birleştiriyor (ör. göbek dış konisi ile boşluk içindeki göbek konisi tek yüz; master'da kaburga
  aralarında ayrı parçalar); helisel yüzeyler master'da birden çok parçaya bölünmüş. Geometri değişmiyor.
- Insert CoM'unun eksenden küçük sapması (hedef −0.00012, −0.00032; ölçülen +0.00055, −0.00016) tutmadı. Diş fazı
  ölçümle doğrulandı (θ=0'da dip düzlüğü merkezi z = −0.37915, θ=90°'de −0.36355; spec −0.379218 / −0.363593, sağ el).
  Fark büyük ihtimalle dişin havşa konileriyle kesildiği uçlardaki küçük hacim farkından (≈0.00004 in³) geliyor.

## Ölçüm ↔ hedef (final.step yeniden okunarak, inç)

| Gövde | Hacim in³ (hedef) | Alan in² (hedef) | CoM z (hedef) | Bbox | Yüz (hedef) |
|---|---|---|---|---|---|
| P01 çekirdek | 2.07190 (2.07189) | 24.9601 (24.9600) | 0.07567 (0.07567) | ±1.2, −0.695..0.62 ✓ | 110 (123) |
| P02 kaplama | 0.72941 (0.72941) | 25.8622 (25.8622) | 0.22687 (0.22687) | ±1.26, −0.18..0.68 ✓ | 255 (292) |
| P03 insert | 0.06336 (0.06340) | 1.8865 (1.8851) | −0.43000 (−0.43003) | ±0.265625, −0.68..−0.18 ✓ | 16 (27) |
| Montaj | 2.86467 (2.86470) | 52.7088 (52.7074) | 0.10298 (0.10298) | ±1.26, −0.695..0.68 ✓ | 3 gövde |

- Bütün gövdeler `is_valid = True`; ikili kesişim hacimleri 0 (yalnız temas).
- Montaj bbox mm: ±32.004, −17.653..17.272 (hedefle aynı).
- Çekirdek ve kaplama 5 anlamlı basamakta tuttu; insert hacmi %0.06, alanı %0.07 farklı.
