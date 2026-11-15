# Build log: döner tablalı tekerlek (swivel plate caster), 4 in

Araç: build123d 0.11.1 (OCP/OCCT), Python 3.13. Tek betik: `caster.py`. Ölçüm betiği: `olcum.py`.
Birim inç, çerçeve spec bölüm 1'deki gibi. Her gövde kendi yerinde ayrı bir solid olarak kuruldu, sonradan taşıma
yapılmadı. STEP AP214 (AUTOMOTIVE_DESIGN), uzunluk birimi INCH, 12 solid; her birinin PRODUCT adı spec'teki ID ile
başlıyor (`P01_Fork` … `H1_Axle_pin`).

## Ne yapıldı

Yardımcılar: spec'teki "arc R c=(a,b) to (p,q), cw/ccw" tarifleri `profile_face()` ile doğrudan kenara çevrildi.
Yayın orta noktası, merkezden ve verilen yönden (cw / ccw / kısa yol) hesaplanıp `make_three_point_arc` ile kuruldu.
Profiller (x,y), (x,z), (r,y) ve (rho,z) düzlemlerinden 3B'ye eşlendi.

- **P01 çatal**: OUTER = P_out profilinin ±1.029 simetrik ekstrüzyonu, ({x≥0} ∪ R1.029 silindiri) ile kesişimi.
  RIDGE = R_xy profilinin ±1.133 ekstrüzyonu, ({x≥0} ∪ R1.133 silindiri) ile kesişimi. GAP, ±0.83 bölgesinde tavan
  profili ve R8.342 yayıyla çıkarıldı, x>2.4615 tamamen açık. x<0 tarafında R0.83 silindiri y=2.184'e kadar çıkarıldı.
  Ardından Ø1.0 pim deliği ve Ø0.6 aks deliği açıldı. Yuvarlatmalar tek bir `BRepFilletAPI_MakeFillet` çağrısında
  kenar başına ayrı yarıçapla yapıldı: 24 kenarda R0.06 (iki dış yüzün bütün çevre kenarları, üst yüz/taç
  yuvarlağı ve R2.5/taç kesişim eğrisi) ve 2 kenarda R0.125 (bacak ucu düşey kenarları). İkinci çağrıda 16 kenara
  R0.04 uygulandı (sırt üst kenarları, taç halka bandının iki kenarı, R1.5/halka geçiş eğrileri). Kenar seçimi
  yüz komşuluğuna göre yapıldı. Aks deliği, sırt dibi (sırt duvarı ile dış yüzün birleşimi) ve x=0'daki teğet
  dikiş çizgisi hariç tutuldu.
- **P02 plaka**: köşeleri R0.25 yuvarlatılmış plaka, 4 oval delik. r<0.75 bölgesi çıkarılıp T3 yarım kesitinin
  döndürülmüş hali eklendi.
- **P03 kral pimi**: K1 yarım kesiti döndürüldü. K2 çıkıntısının (x,z) planı (R0.063 göbek ve iki R0.0394 içbükey
  geçiş, gövde silindiri üzerinden kapatılarak) y 2.502 ile 2.6 arasında ekstrüde edilip eklendi.
- **P04 rondela, P05 altıgen halka**: döndürülmüş kesitler. Altıgen 1.51 anahtar ağzında, köşeleri X ekseni üzerinde.
  Delik döndürülmüş kesit olarak çıkarıldı.
- **P06 pedal**: sap (B1) ±0.825 ekstrüzyon. Ayak plakası (B2) yan profilin ±1.05 ekstrüzyonu ile plan profilinin Y
  yönündeki ekstrüzyonunun kesişimi. R0.04 kenarlar, plan yan yüzü ile profil üst/alt yüzü arasındaki her kenara
  uygulandı. Sonuna 6 nervür silindiri (R0.025) birleştirildi.
- **P07–P10, H1**: tekerlek ekseni etrafında döndürülmüş kesitler. P10 çanak yüzü torus yayıdır (R3.75269, merkez
  rho 0.305, z ±2.9277). R0.02 yuvarlatmaların teğet noktaları kodda hesaplandı (jant tarafında z≈-0.6296).
  P10-b, P10-a'nın z→-z aynalı kesitidir. P09 dolu disk, H1 düz silindir; spec'teki P09–H1 girişimi aynen
  korundu.

## Takıldığım yerler ve çözümler

1. **Çatal kenar seçimi**: ilk denemede "sırt duvarı" testi yanlıştı (yüz bbox'ının min |z| değerine bakıyordu).
   Bu yüzden tabla üstü, eğim, R8.622 ve R2.5 kenarları seçilmedi, sırt dibi ise yanlışlıkla seçildi. Sonuç
   +%0.29 hacimdi. Test "yüz |z|>1.03'e taşıyor mu" şeklinde düzeltilince seçim spec F10 listesiyle birebir örtüştü.
2. **Pedal ayak plakası yuvarlatması**: OCC fillet işlemi "BRep_Tool:: no parameter on edge" hatası verdi.
   Kenarları tek tek denediğimde -z tarafındaki bütün zincirler çalışıyordu, +z tarafındakiler ise hata veriyordu.
   Nedeni, +z tarafında arka teğet köşede (R0.04 plan köşesi ile R0.05 profil köşesinin buluştuğu yer) boolean
   işleminin ürettiği 0.0005 uzunluğunda sayısal bir kıymık kenardı. Çözüm: yalnız -z yarısındaki 14 kenar
   yuvarlatıldı, gövde z=0'da kesildi, aynalanıp birleştirildi ve `clean()` uygulandı. Gövde zaten z=0'a göre
   simetrik olduğu için sonuç geometrik olarak aynı. Alternatif olarak denenen offset açma (-0.04 / +0.04) OCC'de
   başarısız oldu.
3. **STEP birimi**: `export_step(unit=Unit.IN)` geometriyi doğru ölçekliyor ama dosyayı mm olarak yazıyordu
   (değerler ×25.4). Spec biriminde teslim için `write.step.unit = INCH` ayarlandı. Dosyada artık
   `CONVERSION_BASED_UNIT('INCH')` var ve koordinatlar 1:1 (ör. 1.8125).

## Bilerek yapılan basitleştirmeler ve yorumlar

- Spec F10 ve B2'de iki yuvarlatmanın buluştuğu küçük geçiş yüzleri tanımlanmamış ("any smooth blend of that radius
  is acceptable"). Bu geçişleri OCC'nin fillet köşe çözümü üretti.
- P03'te K1'in R0.015 içbükey yuvarlatması (yaka üstü / üst gövde) çıkıntının altında kalıyor. Çıkıntı bir union
  olarak eklendiği için yuvarlatma "çıkıntıda durur".
- Yüz sayıları spec'tekinden farklı (ör. P01 91 / 111, P02 36 / 45, P03 20 / 33, P06 76 / 72). Bunun nedeni OCC'nin
  döndürülmüş ve silindirik yüzleri tek parça tutması, kaynak modelin ise ikiye bölmesi. Spec bu sütunu "information
  only" olarak veriyor.
- Spec'teki koordinatlar 4–5 ondalık hassasiyetle verildiği için P02 ile P04/P05 arasında yaklaşık 1e-5 in³
  (≈0.00015 mm³) sayısal temas örtüşmesi ölçülüyor. Bu ihmal edilebilir; diğer bütün çiftler sıfır.
  P09–H1 = 0.17671 in³ (hedef 0.17671).

## Ölçüm ve hedef tablosu (`python olcum.py final.step`, STEP geri okunarak, inç)

| ID | Vol | Vol hedef | dVol | Alan | Alan hedef | CoM | dCoM max | dBBox max | faces | durum |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 5.06925 | 5.06749 | +0.035% | 50.2168 | 50.1952 | (0.9997, 1.5153, 0.0000) | 0.0010 | 0.0000 | 91 | OK |
| P02 | 0.83201 | 0.83205 | -0.005% | 18.5312 | 18.5321 | (0.0000, 2.6875, 0.0000) | 0.0001 | 0.0000 | 36 | OK |
| P03 | 0.23071 | 0.23072 | -0.004% | 3.1488 | 3.1492 | (-0.0009, 2.3584, 0.0000) | 0.0000 | 0.0000 | 20 | OK |
| P04 | 0.12991 | 0.12992 | -0.005% | 4.2447 | 4.2445 | (0.0000, 2.5004, 0.0000) | 0.0000 | 0.0000 | 5 | OK |
| P05 | 0.07254 | 0.07254 | -0.005% | 2.7849 | 2.7849 | (0.0000, 2.5740, 0.0000) | 0.0000 | 0.0000 | 10 | OK |
| P06 | 1.90478 | 1.90479 | -0.000% | 11.7310 | 11.7309 | (3.2588, 1.5941, 0.0000) | 0.0000 | 0.0000 | 76 | OK |
| P07 | 5.89432 | 5.89220 | +0.036% | 35.5650 | 35.5529 | (1.5150, -0.7500, 0.0000) | 0.0000 | 0.0000 | 6 | OK |
| P08 | 0.60427 | 0.60427 | -0.001% | 25.1375 | 25.1375 | (1.5150, -0.7500, 0.0000) | 0.0000 | 0.0001 | 4 | OK |
| P09 | 4.49923 | 4.49923 | +0.000% | 20.3420 | 20.3420 | (1.5150, -0.7500, 0.0000) | 0.0000 | 0.0001 | 3 | OK |
| P10a | 2.93143 | 2.93150 | -0.002% | 17.8823 | 17.8824 | (1.5150, -0.7500, -0.5290) | 0.0000 | 0.0001 | 6 | OK |
| P10b | 2.93143 | 2.93150 | -0.002% | 17.8823 | 17.8824 | (1.5150, -0.7500, 0.5290) | 0.0000 | 0.0001 | 6 | OK |
| H1 | 0.58471 | 0.58471 | +0.001% | 4.4636 | 4.4636 | (1.5150, -0.7500, 0.0000) | 0.0000 | 0.0000 | 3 | OK |

- Toplam hacim 25.68457 in³ (hedef 25.68092, +%0.014). Toplam alan 211.930 in² (hedef 211.898).
- Montajın ağırlık merkezi (bellekteki model): (1.4680, 0.0360, 0.0000), hedef (1.4678, 0.0360, 0.0000).
- Montaj bbox: X [-1.8125, 4.2985], Y [-2.75, 2.75], Z [-1.25, 1.25]; hedefle birebir aynı.
- 12 gövdenin hepsi spec toleransı içinde: hacim ≤%0.5 (H1 için %2), CoM ≤0.02, bbox ≤0.005. En büyük sapmalar P01
  (+%0.035) ve P07 (+%0.036).
- P01'in hacmi bellekte 5.06673 (-%0.015), STEP geri okunduğunda 5.06925 (+%0.035) ölçülüyor. Fark, fillet
  B-spline yüzlerinde OCC'nin hacim integrasyonu ve STEP aktarım toleransından geliyor; her iki değer de
  toleransta.
- P07'deki +%0.036'nın kaynağını bulamadım; ölçüler spec'tekiyle birebir. Kaynak modeldeki tessellation ya da
  yuvarlatma farkı olabilir.
- Temiz kopya testi: `caster.py` boş bir klasöre kopyalanıp çalıştırıldı ve aynı sonuçlar alındı.
