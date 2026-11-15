# Build log — P01 Spanner (hook spanner wrench)

Araç: SolidCraft `solidcraft-cli.exe` (komut dizisi `spanner_build.json`, üretici `gen_script.py`, belge `P01_Spanner.sc`).
Belge birimi inç; çerçeve spec §1'deki gibi: plaka Y = −0.06…+0.06, profil XZ düzleminde, sap +X yönünde, üst kenar Z = 0, parça Z ≤ 0.
Gövdeler yerinde kuruldu; sonradan taşıma/döndürme yok. Tek gövde, adı `P01 Spanner`.

## 1. Kurulum sırası (zaman çizelgesi)

| Özellik | Ne yapar |
|---|---|
| F1_Outline + F1_Extrude | Spec §3 F1'deki 11 parçalı kapalı profil (XZ çizimi), simetrik T = 0.12 ekstrüzyon → plaka |
| F3a_HandleZone + F3a_TrimHandle | x > X_round0 (−0.441484) kısmı plakadan kesilir (sap ayrı gövde olarak kurulacak) |
| F4_*_Profile + F4_*_Revolve (×4) | Konik geçiş kesicileri: yuvarlama merkez çizgisinden geçen düzlemde, X'e 10° eğik kenarlı profil, merkez çizgisi etrafında köşe çeyreğine 90° döndürülür → koni r(x) = R_round + tan10°·(X_round0 − x) |
| combine cut | 4 koni kesici baş gövdesinden çıkarılır (x = −0.478189…−0.441484) |
| F3b_Handle + F3b_HandleExtrude | Sap: X_round0'dan uca dikdörtgen + R_end yarım daire, simetrik T |
| F3c_EdgeRounds | `solid.fillet` R_round: üst kenar, yarım daire uç (toroidal), alt kenar — iki yüzde (6 kenar, teğet zincir) |
| F3d join | Sap başa birleştirilir; X_round0'daki ara yüz birebir eşleşir (koni orada R_round'a iner) |
| F2_Slot + F2_SlotCut | Obround yuva (iki yarım daire + Z = −0.129930 / −0.259860 teğet çizgileri), boydan boya kesim |

Spec'teki F1→F2→F3→F4 sırası yerine F1→F3a→F4→F3b/c/d→F2 uygulandı (sonuç geometrisi aynı; nedeni §3).

## 2. Yorumlar / bilerek yapılan küçük düzeltmeler

- **Yay uç noktaları çembere izdüşürüldü.** Spec koordinatları 1e-6'ya yuvarlanmış. SolidCraft'ta merkez-nokta yayının
  yarıçapı başlangıç noktasından alınır ve bitişi çembere oturtulur; yuvarlanmış noktalarda profil ~2e-5 mm açık kalıp
  ekstrüzyon reddedildi. Çözüm: boyun/sırt teğet noktası (p5) ve sırt/uç teğet noktası (p6) iki çemberin teğet
  noktası olarak hesaplandı; p7, p10, p11 ilgili çembere izdüşürüldü (kayma < 1e-6 in). Spec'in "teğet" ifadeleri
  böylece kesin sağlanıyor (kontrol: |C_back − C_tip| = R_back − R_tip = 0.628888, |C_neck − C_back| = R_neck + R_back).
- Uç yayı yarıçapı bu yüzden teğet noktalarından gelir (0.078125'ten sapma < 1e-6); `R_tip` parametresi bilgi amaçlı.
- Koni kesicisi keskin uçtan 0.002 in (Cut_ext) öteye uzatıldı; orada koni yarıçapı köşe mesafesini aştığı için
  malzeme kaldırmaz, yalnızca kesicinin uç yüzünün tam köşe noktasına dokunmasını (dejenere temas) önler.
- STEP'te ürün adı dosya adından (`final`) geliyor; katı gövdenin adı `P01 Spanner` (`MANIFOLD_SOLID_BREP('P01 Spanner')`).

## 3. Takıldığım yerler

1. **SolidCraft çizim koordinatları mm** (belge birimi inç olsa da çıplak sayılar mm). Tüm koordinatlar parametre ya da
   `"<değer> in"` ifadesi olarak yazıldı. XZ çiziminde çizim-y = −Z (deneme ile doğrulandı).
2. `sketch.slot.center_to_center` ifade kabul etmedi → yuva çizgi + iki yay ile çizildi.
3. `solid.revolve` için `{origin, dir}` ekseni ifade kabul etmedi → eksen olarak çizim içinde yardımcı çizgi kullanıldı.
   Döndürme açısının yönü profil tarafından ölçülüyor: +90° → +Z, −90° → −Z (kesici bbox'larıyla doğrulandı).
4. **İlk yaklaşım başarısız:** tam plaka + köşe kesicileri (düz çeyrek tüp + uçta 180° toroidal kesici). Düz kesiciler
   çalıştı, ama toroidal kesici (torus ile R_end silindiri teğet) boolean'da "no result" verdi; kesicileri önce birleştirmek
   de işe yaramadı. Çözüm: sapı ayrı gövde olarak kurup kernel'in kendi `solid.fillet`'iyle yuvarlamak, başı keskin bırakmak.
5. Koni kesimi birleştirmeden **sonra** yapılınca kesicinin X_round0'daki uç yüzü basamak yüzleriyle çakışıp kesim
   bozuldu (2 koni kayboldu). Koni kesimini birleştirmeden **önce** baş gövdesine yapınca temiz sonuç verdi.

## 4. Bilinen sınırlamalar

- **STEP birimi mm.** `file.export_step` / `--out` her zaman `SI_UNIT(.MILLI.,.METRE.)` yazıyor; birim seçeneği yok
  ve başlığı elle değiştirmek yasak. Geometri aynı çerçevede ve fiziksel olarak doğru ölçekte (1 in = 25.4 mm);
  STEP okuyan her araç doğru boyutta açar. Belge (`.sc`) inç biriminde.
- **Yüz sayısı:** STEP'te 27 `ADVANCED_FACE` (hedef 27, STEP yeniden okununca da 27). Native gövdede kernel 31 yüz
  raporluyor: her konik geçiş yüzü, köşe noktasından 45° doğrultusunda bir dikiş kenarıyla ikiye bölünmüş (farklı
  kesici kurgusu — açıortay düzlemde simetrik döndürme — denendi, değişmedi). Geometri etkilenmiyor; STEP yazıcısı birleştiriyor.
- Fillet kenar seçimleri sayısal noktalar (mm, dünya koordinatı). Parametre büyük değişirse (ör. H_handle) seçim
  noktaları da `gen_script.py`'de güncellenmeli; betik yeniden üretilince bu otomatik değil, sabit 0.5 in / 0.06 / uç noktası.
- SolidCraft'ın raporladığı hacim/alan tessellation tabanlı (ör. R1/64 çeyrek silindirin alanı ~%2.7 düşük çıkıyor:
  çeyrek yay 2 kirişle örnekleniyor). Bu yüzden ölçülen hacim/alan analitik değerden çok az düşük.

## 5. Hedef tablosu ile karşılaştırma

Ölçüm: `solidcraft-cli eval spanner_build.json` (native) ve `solidcraft-cli eval final.step` (STEP geri okuma).
Analitik: `calisma/check_analytic.py` (spec geometrisinden bağımsız sayısal integral).

| Büyüklük | Hedef | Native model | STEP geri okuma | Fark (native) |
|---|---|---|---|---|
| Hacim in³ | 0.208501 | 0.208498 (3416.661 mm³) | 0.208497 (3416.650 mm³) | −0.0016 % |
| Hacim (analitik) | 0.208501 | 0.2085009 (3416.717 mm³) | — | +0.0001 % |
| Alan in² | 4.612036 | 4.611935 (2975.436 mm²) | 4.611921 (2975.427 mm²) | −0.0022 % (tessellation) |
| CoM X | −0.088238 | −0.088247 | −0.088242 | 9e-6 in |
| CoM Y | 0 | 0.000000 | 0.000000 | 0 |
| CoM Z | −0.251719 | −0.251718 | −0.251717 | 1e-6 in |
| Xmin / Xmax | −2.165500 / 2.165500 | −2.165498 / 2.165500 | −2.165498 / 2.165500 | ≤ 2e-6 (Xmin tessellation) |
| Ymin / Ymax | ∓0.060000 | −0.060000 / 0.060000 | ∓0.060123 | STEP okumada koni/torus mesh taşması 1.2e-4 in |
| Zmin / Zmax | −0.707013 / 0 | −0.707013 / 0.000010 | −0.707013 / 0.000095 | mesh taşması (B-rep düzlemi Z = 0) |
| Yüz sayısı | 27 (+114 boş) | 31 kernel (konik yüzler 2'şer parça) | **27** | §4 |

Kontrol ölçüleri: toplam boy 4.331000 (−2.1655…2.1655) ✓; kalınlık 0.12 ✓; sap genişliği 0.38979 ✓; çene R0.3125 ✓;
pim alt yüzü 0.0625 (p9–p10 arası 0.062500) ✓; uç yarıçapı 0.194895 ✓; baş yüksekliği 0.707013 ✓.
Kaynak modeldeki 19 boş mikro-kutu (114 sıfır alanlı yüz) bilerek üretilmedi (spec: "do not reproduce").

Görsel kontrol: ön/izometrik ve geçiş bölgesi yakın çekimleri `calisma/shot_*.png` — kanca, pim, çene, yuva,
yuvarlatılmış sap ve x ≈ −0.46'daki konik geçiş beklendiği gibi.
