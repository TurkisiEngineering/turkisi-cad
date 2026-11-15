# Build log – döner tablalı tekerlek (4 in), build123d 0.11.1

## Ne yapıldı
- Tek betik `caster.py`; tüm ölçüler spec'ten, inç biriminde, spec'in global çerçevesinde (+Y yukarı, döner eksen Y,
  tekerlek ekseni x=1.515, y=-0.75). 12 ayrı solid, kimlik yerleşimiyle yerinde kuruldu.
- Profil yardımcısı `profile()`: spec'teki "çizgi / merkez+yön (cw/ccw/kısa yol) yay" tariflerini doğrudan kenara çevirir
  (yay = başlangıç + merkezden hesaplanan orta nokta + bitiş, üç nokta yayı).
- P01 çatal: F = (OUTER + RIDGE) − GAP − delikler, spec'teki sırayla:
  - OUTER = P_out ±1.029 ekstrüzyonu ∩ (x≥0 yarı uzayı ∪ R1.029 silindir); sonra R0.06 yuvarlatma
    (teğet dikiş kenarları ve tabla üstü/pah kesişim kenarı hariç tüm kenarlar – 26 kenar tek seferde başarılı).
  - RIDGE = R_xy ±1.133 ekstrüzyonu ∩ (x≥0 ∪ R1.133 silindir); üst kenarlarına R0.04 (18 kenar). Nervür tabanı keskin.
  - GAP: x≥0'da tavan konturunun altı (|z|<0.83) + R0.83 silindir; pim deliği R0.5, aks deliği R0.3.
  - Yuvarlatmalar GAP'ten önce yapıldı; hepsi |z|≥0.904'te olduğundan GAP bunlara dokunmaz.
- P02 plaka: R0.25 köşeli kutu − 4 obround kızak − r<0.75 silindir + preslenmiş merkezin dönel kesiti (r ≤ 0.75).
- P03 pim: dönel kesit + plan konturundan y 2.502→2.6 ekstrüde tırnak (birleşim).
- P04, P05, P07–P10: dönel kesitler / silindirler; P10-b = P10-a'nın z=0 düzlemine göre aynası.
  P10 çanak yüzeyindeki R0.02 yuvarlatmaların teğet noktaları iç teğetlik koşulundan hesaplandı.
- P06 pedal: sap (±0.825) + ayak plakası (yan profil ±1.05 ∩ plan konturu Y yönünde) + 6 nervür silindiri.
- STEP: `export_step(..., unit=Unit.IN)` + `write.step.unit = INCH`, AP214 (AUTOMOTIVE_DESIGN), her solid adlı ürün.

## Nerede takıldım
1. **P06 ayak plakası R0.04**: tüm kenarlar birlikte → OCC fillet hatası. Tek tek denendiğinde üst kenarların hepsi
   başarılı, alt kenarların hepsi başarısız (nedeni bulunamadı; profil y=1.5195'e göre simetrik olmasına rağmen).
   Çözüm: yan profil spec'e göre y = 1.5195'e göre tam simetrik olduğundan, üst kenarlar yuvarlatıldı, üst yarı kesildi
   ve y=1.5195 düzlemine göre aynalanıp birleştirildi. Sonuç hacim/alan hedefle −0.002 % / 0.00 %.
2. **STEP birimi**: build123d `unit=Unit.IN` ile bile OCCT çıkışı varsayılan mm'ye çeviriyordu (dosyada
   SI_UNIT MILLI METRE, koordinatlar ×25.4). `Interface_Static write.step.unit = INCH` ile dosya inç birimli yazıldı;
   koordinatlar spec değerleriyle birebir (geri okuma kontrolü yapıldı).

## Bilerek basitleştirilen / farklı olanlar
- **P01 R0.125 bacak ucu düşey kenarları**: P_out konturu bacak ucunda baştan sona G1 (teğet) olduğundan OCC fillet
  zinciri tek kenarda durmuyor; R0.125 verilirse tüm dış kontura yayılıyor. Bu iki kısa kenar (0.19 boy) diğerleriyle
  birlikte **R0.06** kaldı. Hacim etkisi ≈ 2·(0.125²−0.06²)(1−π/4)·0.19 ≈ 0.001 in³ (%0.02). Köşe "küçük blend"
  yamaları da bu yüzden yok.
- Yuvarlatmaların buluştuğu küçük blend yamaları OCC'nin kendi köşe çözümleriyle oluştu (spec "herhangi düzgün blend
  kabul" diyor).
- Yüz sayıları orijinalden azdır (ör. P01 95/111, P02 36/45, dönel gövdeler tam 360° tek yüz): OCC tam dönüşte yüzleri
  bölmez, eş yüzleri birleştirir; spec'e göre yüz sayısı yalnız bilgi amaçlı.
- P09–H1 girişimi spec'teki gibi bırakıldı (P09 deliksiz).

## Ölçüm – spec §6 hedef tablosu (final.step geri okunarak, inç)

| ID | Hacim | Hedef | ΔV % | Alan | ΔA % | ΔCoM max | ΔBBox max | Yüz |
|---|---|---|---|---|---|---|---|---|
| P01 | 5.06928 | 5.06749 | +0.035 | 50.2174 | +0.04 | 0.0010 | 0.0000 | 95 |
| P02 | 0.83201 | 0.83205 | −0.004 | 18.5312 | 0.00 | 0.0001 | 0.0000 | 36 |
| P03 | 0.23071 | 0.23072 | −0.004 | 3.1488 | −0.01 | 0.0000 | 0.0000 | 20 |
| P04 | 0.12991 | 0.12992 | −0.006 | 4.2447 | +0.01 | 0.0000 | 0.0000 | 5 |
| P05 | 0.07254 | 0.07254 | −0.005 | 2.7849 | 0.00 | 0.0000 | 0.0000 | 10 |
| P06 | 1.90476 | 1.90479 | −0.002 | 11.7310 | 0.00 | 0.0000 | 0.0000 | 78 |
| P07 | 5.89432 | 5.89220 | +0.036 | 35.5650 | +0.03 | 0.0000 | 0.0000 | 6 |
| P08 | 0.60427 | 0.60427 | −0.001 | 25.1375 | 0.00 | 0.0000 | 0.0001 | 4 |
| P09 | 4.49923 | 4.49923 | 0.000 | 20.3420 | 0.00 | 0.0000 | 0.0001 | 3 |
| P10-a | 2.93142 | 2.93150 | −0.003 | 17.8822 | 0.00 | 0.0000 | 0.0001 | 6 |
| P10-b | 2.93142 | 2.93150 | −0.003 | 17.8822 | 0.00 | 0.0000 | 0.0001 | 6 |
| H1 | 0.58471 | 0.58471 | +0.001 | 4.4636 | 0.00 | 0.0000 | 0.0000 | 3 |

- Toplam hacim 25.6846 in³ (hedef 25.68092, +0.014 %), toplam alan 211.93 in² (hedef 211.8978, +0.015 %).
- Bellekteki (STEP öncesi) P01 hacmi 5.06700 (−0.010 %); fark STEP'e yazılan B-spline yuvarlatma yüzeylerinin
  hacim hesabı hassasiyetinden.
- Tüm gövdeler hacimde %0.5, CoM'da 0.02 in, bbox'ta 0.005 in toleransının içinde; hepsi geçerli (is_valid) solid.
- Montaj bbox X[−1.8125, 4.2985] Y[−2.75, 2.75] Z[−1.25, 1.25] – hedefle aynı.
- Girişim: P09∩H1 = 0.176715 in³ (hedef 0.17671). Diğer çiftler sıfır; yalnız P02–P04 ve P02–P05 arasında
  ~9e-6 in³ (≈0.15 mm³) sayısal temas artığı (aynı daire yüzeylerinin üç-nokta yay yaklaşımı).
- Fonksiyonel kontroller: montaj yüksekliği 5.5, tekerlek Ø4.0 × 1.25, kaçıklık 1.515, plaka 3.625×2.5×0.1,
  kızaklar 2.9375×1.75 / 0.3125, bacak 0.199, boşluk 1.66, çatal dış genişlik 2.058 (nervürle 2.266) – modelde aynen.
