# Build log

## Ne yapıldı
- build123d 0.11.1, tek betik `model.py`. Model doğrudan inç ve spec'in global çerçevesinde kuruldu; her parça
  yerinde (P01–P08 global koordinatlarda, H1 bir kez yerel çerçevede kurulup spec §5 poz tablosuyla
  `Location(Plane(O, U, W))` ile yerleştirildi, her örnek bağımsız kopya).
- Kesitler (x, y) profilden Z boyunca ekstrüzyon; dönel parçalar (z, r) profilden döndürme; delikler silindir /
  döndürülmüş profil kesimleri.
- P06 vida dişi gerçek helisel oluk: yamuk oluk profili (kök 0.09252, iki yanak 30°, takım r = 0.13'e kadar uzatıldı;
  r = 0.13'te oluk genişliği 0.0495 < hatve, böylece süpürme kendini kesmiyor) `Helix` boyunca Frenet süpürme ile.
  Faz: θ = 0'da kök merkezi z = 0.515625 + 0.05k; başlangıç k = −2 (z = 0.5 ucunun tamamen dışında),
  bitiş k = 69, θ = 270° (−Y tarafı, kök merkezi z = 4.003125). Sağ el (z θ ile artıyor) ve bitiş yüzü yoklama
  noktalarıyla doğrulandı (θ = 269°'da oluk var, 271°'de yok).
- STEP: AP214 (AUTOMOTIVE_DESIGN şeması), `write.step.unit = INCH` → dosya inç birimli; 12 isimli katı gövde.

## Takıldığım yerler ve çözümler
1. **Tek parça 71.75 turluk helisel süpürme ile kesim sessizce başarısız oldu** (sonuç neredeyse kesilmemiş
   blank). Ayrıca blank'in z = 0.5 / z = 4.0 uç yüzlerini kesen süpürme parçaları da hiç kesmedi.
   Çözüm: süpürme 8 turluk parçalara bölündü; kesim önce eksenel olarak uzatılmış düz bir silindirde
   (z 0.2–4.3) yapıldı, sonra gerçek pahlı blank ile (z 0.5–4.0) kesişim alındı, en son Ø0.218 mil eklendi.
   z = 4.0'da oluğun kırpılması bu kesişimle sağlanıyor.
2. **P08 kol ucu yayı** merkezi eksenden 0.00051 dışarıda; tam döndürme "iğ tipi torus" yüzeyi veriyor. Bellekte geçerli
   olsa da STEP geri okumada bozuk geldi (hacim −29 %). Çözüm: yalnız bu yay, tam yaydan alınmış 48 noktalı B-spline
   olarak çizilip döndürüldü (sapma ihmal edilebilir; hacim/alan hedefle aynı). Diğer tüm yaylar tam daire yayı.
3. H1 için aynı şeklin taşınmış kopyaları STEP'e tek ürün + 4 örnek olarak yazılıyordu; isimlerin gövde başına
   korunması için her örnek bağımsız kopya yapıldı (dosyada 12 ayrı isimli katı).

## Bilinçli tercihler / yorumlar
- P02 F5 (spec'te "isteğe bağlı" 0.00025 inçlik kaynak artefaktı) **modellendi**: şeritler birleştirildikten sonra
  kesildi. Bunsuz taşıyıcı alanı 10.644 in² çıkıyordu (−0.56 %); fark, +X şeritlerinin üstünde kalan ince kama
  boşluğunun iki yüzüne (≈ 0.0302 × 0.5 × 2 yüz × 2 şerit = 0.060 in²) tam uyuyor, yani orijinalde artefakt
  şeritlerden sonra kesilmiş. Modelleyince alan 10.704 in² (hedefle aynı). Bu yüzden taşıyıcı X'te çok hafif asimetrik
  (spec'te belirtildiği gibi).
- Kesim takımları (delikler, havşa) yüzeylerin biraz dışına uzatıldı; bu yalnız temiz Boolean içindir, geometri aynı.
- Spec'te tarif edilen basitleştirmeler aynen korundu: somun ve el çarkı göbeği dolu (vida ile hacimsel çakışma),
  vida dişi dışında diş yok, yatak bloğu deliği boş, tırtıl / yuva yok, şeritler taşıyıcı gövdesinin parçası.
- Yüz sayıları orijinalden farklı (ör. vida 105 / 293, taban 26 / 34, taşıyıcı 56 / 63): OCCT tek helisel süpürmeyi
  tur başına bölmüyor, silindirleri tek yüz yapıyor vb. Spec bu sütunu yalnız bilgi amaçlı veriyor.

## Ölçüm – spec §6 hedefleri (final.step geri okunarak, `python measure.py`)

| Gövde | Hacim in³ (hedef) | ΔV % | Alan in² (hedef) | ΔA % | maks ΔCoM in | maks ΔBBox in | Sonuç |
|---|---|---|---|---|---|---|---|
| P01 Base | 4.5937 (4.5937) | −0.000 | 35.896 (35.896) | −0.000 | 0.00002 | 0.00004 | OK |
| P02 Carriage | 0.8300 (0.8300) | −0.003 | 10.704 (10.704) | +0.004 | 0.00001 | 0.00004 | OK |
| P03 Drive nut | 0.4059 (0.4059) | −0.002 | 3.187 (3.187) | −0.005 | 0.00004 | 0.00004 | OK |
| P04 End block | 1.1376 (1.1376) | +0.001 | 9.266 (9.266) | +0.005 | 0.00003 | 0.00004 | OK |
| P05 End plate | 0.1114 (0.1114) | −0.030 | 4.066 (4.066) | +0.008 | 0.00001 | 0.00004 | OK |
| P06 Lead screw | 0.1685 (0.1685) | +0.004 | 4.927 (4.926) | +0.015 | 0.00004 | 0.00004 | OK |
| P07 Handwheel | 1.0320 (1.0320) | +0.001 | 7.532 (7.532) | −0.004 | 0.00004 | 0.00004 | OK |
| P08 Crank handle | 0.0447 (0.0447) | +0.077 | 0.861 (0.861) | −0.001 | 0.00005 | 0.00005 | OK |
| H1-a…d (her biri) | 0.0225 (0.0225) | +0.073 | 0.628 (0.628) | −0.061 | 0.00004 | 0.00004 | OK |

(ΔV/ΔA yüzdeleri, 4 haneye yuvarlanmış hedef değerlere göre; ΔBBox ≈ 0.00004 hedef tablonun 4 hane yuvarlamasıdır.)

- Toplam hacim 8.4138 in³ (hedef 8.4138), toplam alan 78.950 in² (hedef 78.949).
- Montaj ağırlık merkezi (0.0000, −0.0224, 2.8277) — hedefle aynı.
- Montaj sınır kutusu X [−1.25, 1.25], Y [−0.83256, 0.91744], Z [−0.162, 6.5622] — hedefle aynı.
- Çakışmalar (spec §5): P01∩P02 = 4.966 mm³ (hedef 4.97), P03∩P06 = 608.66 mm³ (608.7), P06∩P07 = 191.45 mm³ (191.4).
- Tüm gövdeler `is_valid` = True (STEP geri okumasından sonra da).
