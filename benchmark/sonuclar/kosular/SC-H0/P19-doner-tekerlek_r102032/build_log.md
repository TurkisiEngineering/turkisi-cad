# Build log: swivel plate caster (r102032)

## Ne yapıldı

- Araç: SolidCraft CLI. Model, `gen.js` dosyasının ürettiği tek bir komut dizisiyle (`caster_script.json`, 260 adım)
  kuruluyor. `solidcraft-cli run caster_script.json --save caster.sc` modeli sıfırdan kuruyor;
  `file.export_step` AP242 `final.step` dosyasını yazıyor.
- Birim ve çerçeve: Belge birimi inç; spec'in global çerçevesi aynen kullanıldı (+Y yukarı, salınım ekseni Y, tekerlek
  ekseni x=1.515, y=-0.75). Bütün gövdeler yerinde kuruldu; sonradan taşıma yok. Taslak noktaları SolidCraft'a mm
  olarak veriliyor (inç × 25.4), boyutlar ise inç parametreli ifadelerle.
- STEP birimi: SolidCraft'ın STEP yazıcısı birimi her zaman mm olarak yazıyor (`SI_UNIT(.MILLI.,.METRE.)`), belge inç
  olsa bile. Geometri 1 in = 25.4 mm ile spec'in çerçevesinde. Başlık elle değiştirilmedi. STEP geri okununca
  12 gövde, gövde adları ve hacimler doğru çıkıyor.
- 12 gövde: `P01_Fork`, `P02_TopPlate`, `P03_Kingpin`, `P04_BearingWasher`, `P05_HexRing`, `P06_BrakePedal`,
  `P07_WheelTread`, `P08_WheelInsertRing`, `P09_WheelCoreDisc`, `P10a_CoreFlange_negZ`, `P10b_CoreFlange_posZ`,
  `H1_AxlePin`.

Gövde bazında kurulum:
- **P01 Fork:** P_out yan profili ±1.029 simetrik ekstrüde edildi. "Kutu − silindir" aleti ile x<0 bölgesi kırpıldı
  (R1.029 içi kaldı). RIDGE profili ±1.133 ekstrüde edilip aynı yolla (R1.133) kırpıldı ve birleştirildi. Boşluk
  (GAP), yan tavan profilinin (x=-1'den başlıyor) ±0.83 ekstrüzyonu ile üstten "R0.83 yarım daire + |z|<0.83 bant"
  profilinin kesişimi olarak tek gövde halinde kuruldu ve tek seferde çıkarıldı. Ardından F4 kingpin deliği (Ø1.0),
  F5 aks deliği (Ø0.6) ve kısmi F10 yuvarlamaları yapıldı (aşağıya bakın).
- **P02:** R0.25 köşeli 3.625 × 2.5 plaka, 4 delik ve r=0.75 merkez deliği tek taslaktan 0.1 ekstrüde edildi. Basılı
  merkez (T3 yarım kesiti) Y etrafında döndürülüp birleştirildi.
- **P03:** K1 yarım kesiti döndürüldü; K2 tırnağı ekstrüzyonla eklendi (sadeleştirme notuna bakın).
- **P04, P05:** P04 döndürmeyle kuruldu. P05 altıgen prizma (köşeler X ekseninde) olarak kuruldu, koni + R0.25 deliği
  döndürülmüş aletle çıkarıldı.
- **P06:** Gövde profili ±0.825; ayak plakası (yan profil ∩ plan profili); 6 nervür (R0.025 silindirler) birleştirildi.
- **P07, P08, P10a/b:** Tekerlek ekseni düzleminde (rho, z) yarım kesitlerden döndürüldü. P10'un R0.02 yuvarlamalarının
  çanak torusuna teğet noktaları `gen.js` içinde hesaplandı. P10b ayna profilden kuruldu.
- **P09, H1:** Silindir olarak kuruldu. P09 ile H1'in bilerek bırakılan örtüşmesi korundu.

## Nerede takıldım ve nasıl çözdüm

1. Boolean çekirdeği tam teğet ve çakışık yüzlerde "no result" hatası veriyor:
   - **GAP:** R0.83 silindir ile z=±0.83 düzlemleri x=0'da teğetti. Çözüm: tek, teğet-sürekli bir plan profiliyle
     kesişim (yukarıda anlatıldı). Geometri birebir.
   - **P02 basılı merkez:** Halkanın r=0.75 silindiri plaka deliğiyle çakışıyordu. Çözüm: döner kesit r=0.8'e kadar
     uzatıldı, plakaya 0.05 gömülü. Dış geometri birebir.
   - **P03 tırnağı:** Tabanı yaka üstüyle (y 2.502) çakışıktı ve R0.0394 içbükey geçişleri şafta teğetti. Çözüm:
     tırnak y=2.45'ten başlıyor (yakanın içinde, görünmez). Geçişler için aşağıdaki sadeleştirmeye bakın.
   - **P06 ayak plakası:** Kesişimdeki ön/arka/yan düzlemler çakışıktı ve plan köşe yayları yan profilin ön/arka
     düzlemlerine teğetti. Çözüm: plan profili x=3.6 / 4.4'e uzatıldı, yan profil ±1.15 ekstrüde edildi, köşe yay
     merkezleri kaydırıldı (aşağıda).
   - **Çatal taç kırpma:** Düz dış yüzler x=0'da R1.029 / R1.133 kırpma silindirine teğetti. Çekirdek bu durumda gövdeye
     sıfır alanlı, ±4 in uzanan bir yüz parçası bırakıyordu (sınır kutusu bozuktu). Çözüm: kırpma silindirleri
     `trim_eps` = 0.0005 in daha büyük.
2. **Yay uçlarının izdüşümü:** Spec'teki yay uçları 5 haneye yuvarlanmış. Profillerin kapanması için `gen.js` her yay
   ucunu, başlangıcından geçen çemberin üzerine izdüşürüyor (sapma ≤ ~1e-5 in). P05 delik aletinde bu yüzden aletin
   üst yüzü 0.00014 mm aşağıda kalıp ince bir film bırakmıştı. Alet üst yüzün ötesine uzatılarak düzeltildi.
3. **Fillet çekirdeği:** "not supported yet: an end face almost along the edge / only straight edges can be blended /
   the ball doesn't fit". F10 kenarları tek tek ve gruplar halinde denendi (`calisma/ft`). Kurulabilenler yalnızca
   şunlar: R0.06 ile R8.622 üst kenarlar (iki yüz) ve düz üst yüz (y 2.464) kenarları. İkisi sıralı iki ayrı özellik
   olarak modelde var. Bitişik kenarlar (örneğin eğim kenarı) bunlardan sonra eklenince başarısız oluyor.
4. Ortam: Python ve oturum scratchpad'i bu görevde kapalıydı. Üretici betik Node.js ile yazıldı; ara dosyalar
   `r102032/calisma/` altında.

## Bilerek sadeleştirdiklerim

- **P01 F10 yuvarlamaları büyük ölçüde yok.** Kurulan: R0.06 R8.622 üst kenarlar ve y=2.464 üst kenarları. Kurulamayan
  ve keskin bırakılan: R0.06 yan duvar kenarları (R2.5, R0.5, R0.5508, dikey çizgi, R0.683, alt çizgi, R0.15
  köşeler), ön eğim kenarı, taç (R1.029) kenarları, R0.125 bacak ucu kenarı, R0.04 sırt kenarlarının hepsi. Sonuç:
  çatal hacmi +0.50 %, alanı +1.7 %, yüz sayısı 53 (orijinal 111).
- **P06 B2 R0.04 yuvarlamaları yok.** Çekirdek kuramadı. Kenar listesi `gen.js` içinde duruyor
  (`tryPedalRounds = false`).
- **P06 plan köşe merkezleri:** Arka R0.04 köşe merkezleri 0.001 in -X yönüne, ön R0.25 köşe merkezleri 0.004 in +X
  yönüne kaydırıldı. Bu yüzden ön köşe yayının yarıçapı 0.2467'ye düşüyor ve R1.0 yayına geçişte ~0.9°'lik görünmez
  bir kırık oluşuyor. Şekil değişimi ≤ 0.001 in; hacim etkisi ihmal edilebilir.
- **P03 K2 tırnağı:** Yalnız R0.063 göbek dairesi olarak kuruldu. Şafta teğet R0.0394 içbükey geçişler yok (hacim
  etkisi ~1e-4 in³). Tırnak dairesinin şaftın içinde kalan kısmı birleşimde kayboluyor.
- **P01 taç kırpma** 0.0005 in büyük silindirle yapıldı: x min = -1.1335 (hedef -1.1330). Düz yüz ile taç yuvarlağı
  x≈-0.03'te 1.8°'lik bir kırıkla buluşuyor.
- **Malzemeler atanmadı.** Hepsi SolidCraft varsayılanında; hacim/alan/ağırlık merkezi bundan etkilenmiyor.

## Ölçümüm ve spec hedef tablosu (inç, SolidCraft `eval`)

| ID | Hacim (benim) | Hacim (hedef) | Fark | Alan (benim / hedef) | Ağırlık merkezi (benim) | Ağırlık merkezi (hedef) | Sınır kutusu |
|---|---|---|---|---|---|---|---|
| P01 | 5.09298 | 5.06749 | **+0.50 %** | 51.051 / 50.195 | (0.9988, 1.5128, 0) | (0.9987, 1.5153, 0) | X min -1.1335 (Δ0.0005), diğerleri tam |
| P02 | 0.83202 | 0.83205 | -0.004 % | 18.531 / 18.532 | (0, 2.6876, 0) | (0, 2.6876, 0) | tam |
| P03 | 0.23069 | 0.23072 | -0.01 % | 3.150 / 3.149 | (-0.0009, 2.3584, 0) | (-0.0009, 2.3584, 0) | tam |
| P04 | 0.12991 | 0.12992 | -0.01 % | 4.244 / 4.2445 | (0, 2.5004, 0) | (0, 2.5004, 0) | tam |
| P05 | 0.07254 | 0.07254 | 0.00 % | 2.785 / 2.785 | (0, 2.5740, 0) | (0, 2.5740, 0) | tam (köşeler X'te ±0.8718) |
| P06 | 1.90597 | 1.90479 | +0.06 % | 11.798 / 11.731 | (3.2593, 1.5940, 0) | (3.2588, 1.5941, 0) | tam |
| P07 | 5.89449 | 5.89220 | +0.04 % | 35.565 / 35.553 | (1.515, -0.75, 0) | (1.515, -0.75, 0) | tam |
| P08 | 0.60424 | 0.60427 | -0.005 % | 25.137 / 25.138 | (1.515, -0.75, 0) | aynı | tam (±0.0001) |
| P09 | 4.49895 | 4.49923 | -0.006 % | 20.341 / 20.342 | (1.515, -0.75, 0) | aynı | tam (±0.0001) |
| P10a | 2.93110 | 2.93150 | -0.014 % | 17.882 / 17.882 | (1.515, -0.75, -0.529) | (1.515, -0.75, -0.529) | tam |
| P10b | 2.93110 | 2.93150 | -0.014 % | 17.882 / 17.882 | (1.515, -0.75, 0.529) | aynı | tam |
| H1 | 0.58462 | 0.58471 | -0.015 % | 4.463 / 4.464 | (1.515, -0.75, 0) | aynı | tam |

- **Montaj:** 12 gövde. Toplam hacim 421288.6 mm³ (hedef 420834.8, +0.11 %); toplam alan 137309 mm² (hedef 136708,
  +0.44 %). Sınır kutusu X [-1.8125, 4.2985], Y [-2.75, 2.75], Z [-1.25, 1.25] in, hedefle aynı.
- **Girişim** (`inspect.interference`): Tek çift P09–H1 = 2895.51 mm³ (hedef 2895.83). Başka örtüşme yok.
- **Fonksiyonel kontroller:** Montaj yüksekliği 5.5, tekerlek Ø4.0 × 1.25, salınım kaçıklığı 1.515, plaka 3.625 × 2.5
  × 0.1, delik merkezleri 2.9375 × 1.75 ve 0.3125 genişlik, bacaklar 0.199 kalınlığında ve aradaki boşluk 1.66, çatal
  dış genişliği 2.058 (sırtlarla 2.266). Hepsi spec'teki değerlerle kuruldu.
- **Toleranslar:** P01 dışındaki 11 gövde hacimde < 0.07 %, ağırlık merkezinde < 0.001 in, sınır kutusunda
  < 0.0005 in. P01 hacimde +0.503 % (önerilen 0.5 % sınırının hemen üstü; sebep eksik F10 yuvarlamaları), ağırlık
  merkezinde 0.0025 in, sınır kutusunda 0.0005 in.
