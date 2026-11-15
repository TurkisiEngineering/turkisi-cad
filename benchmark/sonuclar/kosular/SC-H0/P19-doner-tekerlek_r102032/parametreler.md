# Parametreler

Bu parametreler SolidCraft belgesinde (`caster.sc`) kullanıcı parametresi olarak tanımlı (`parameters.add`). Belge
birimi inç. Kaynakları `gen.js` içindeki `params` tablosu.

**Durum** sütunu:
- **sürücü:** Parametre, özelliğin ifadesinde doğrudan kullanılıyor (ekstrüzyon mesafesi, silindir yarıçapı/boyu, fillet
  yarıçapı, köşe yarıçapı). Değeri değiştirip yeniden hesaplatınca model güncelleniyor.
- **bilgi:** Değer belgede kayıtlı, ama geometri taslak noktalarında sayı olarak yer alıyor. SolidCraft taslak
  noktalarını mm sayısı olarak alıyor; bu noktalar `gen.js` içinde inç değerlerinden hesaplanıyor. Böyle bir ölçüyü
  değiştirmek için `gen.js` dosyasını düzenleyip betiği yeniden üretmek gerekiyor.

| Ad | Değer (in) | mm | Durum | Hangi özellik |
|---|---|---|---|---|
| `plate_top_y` | 2.75 | 69.85 | bilgi | P02 bağlantı yüzü y (taslak düzlemleri 2.7 merkezli) |
| `plate_t` | 0.1 | 2.54 | sürücü | `P02_TopPlate_extrude` (simetrik kalınlık) |
| `plate_L` | 3.625 | 92.075 | bilgi | `S_P02_plate` yuvarlatılmış dikdörtgen X uzunluğu |
| `plate_W` | 2.5 | 63.5 | bilgi | `S_P02_plate` yuvarlatılmış dikdörtgen Z genişliği |
| `plate_corner_R` | 0.25 | 6.35 | sürücü | `S_P02_plate` köşe yarıçapı |
| `slot_w` | 0.3125 | 7.9375 | bilgi | `S_P02_plate` 4 delik genişliği (slot komutu ifade kabul etmedi) |
| `fork_top_y` | 2.464 | 62.5856 | bilgi | P01 üst yüz y (`S_P01_outer`) |
| `fork_W` | 2.058 | 52.2732 | sürücü | `P01_Fork_extrude` (OUTER, \|z\| ≤ 1.029) |
| `crown_R` | 1.029 | 26.1366 | sürücü | `T_cyl1` taç kırpma silindiri (yarıçap `crown_R + trim_eps`) |
| `ridge_W` | 2.266 | 57.5564 | sürücü | `P01_Ridge_extrude` (RIDGE, \|z\| ≤ 1.133) |
| `ridge_R` | 1.133 | 28.7782 | sürücü | `T_cyl2` sırt halkası kırpma silindiri (`ridge_R + trim_eps`) |
| `trim_eps` | 0.0005 | 0.0127 | sürücü | `T_cyl1`, `T_cyl2`: teğetliği bozan küçük pay (bkz. build_log) |
| `gap_W` | 1.66 | 42.164 | sürücü | `T_gap_extrude` (bacaklar arası boşluk, \|z\| < 0.83) |
| `gap_R` | 0.83 | 21.082 | bilgi | `S_P01_gap_plan` arka yarım daire yarıçapı |
| `kp_hole_D` | 1.0 | 25.4 | sürücü | `T_kphole` (F4 kingpin deliği) |
| `axle_x` | 1.515 | 38.481 | bilgi | tekerlek ekseni x (salınım kaçıklığı): tekerlek taslak düzlemi, H1/P09 tabanı |
| `axle_y` | -0.75 | -19.05 | bilgi | tekerlek ekseni y |
| `axle_D` | 0.6 | 15.24 | sürücü | `T_axlebore` (F5 aks deliği) ve `H1_AxlePin` çapı |
| `axle_L` | 2.068 | 52.5272 | sürücü | `H1_AxlePin` boyu |
| `fork_R06` | 0.06 | 1.524 | sürücü | `P01_round_R006_topR8622`, `P01_round_R006_topflat` |
| `fork_R125` | 0.125 | 3.175 | bilgi | F10 bacak ucu yuvarlaması: çekirdek kuramadı, kullanılmıyor |
| `ridge_R04` | 0.04 | 1.016 | bilgi | F10 sırt yuvarlamaları: çekirdek kuramadı, kullanılmıyor |
| `hex_AF` | 1.51 | 38.354 | bilgi | `S_P05_hex` altıgen (karşılıklı yüzler arası 2 × 0.755) |
| `hex_t` | 0.075 | 1.905 | sürücü | `P05_HexRing_extrude` |
| `lug_h` | 0.098 | 2.4892 | sürücü | `T_lug_extrude` (mesafe `lug_h + 0.052 in`: tırnak yakaya gömülü başlıyor) |
| `pedal_W` | 1.65 | 41.91 | sürücü | `P06_BrakePedal_extrude` (gövde, \|z\| ≤ 0.825) |
| `foot_W` | 2.1 | 53.34 | sürücü | `T_foot_extrude` (mesafe `foot_W + 0.2 in`; ±1.05 genişliği plan profili veriyor) |
| `pedal_R04` | 0.04 | 1.016 | bilgi | B2 ayak plakası yuvarlamaları: çekirdek kuramadı, kapalı |
| `rib_R` | 0.025 | 0.635 | sürücü | `P06_rib1..6` kaydırmaz nervürleri |
| `rib_stem_L` | 1.35 | 34.29 | sürücü | `P06_rib1..3` boyu |
| `rib_foot_L` | 1.75 | 44.45 | sürücü | `P06_rib4..6` boyu |
| `wheel_D` | 4.0 | 101.6 | bilgi | `S_P07_tread` dış yarıçap 2.0 |
| `wheel_W` | 1.25 | 31.75 | bilgi | `S_P07_tread`, `S_P08_insert` genişliği |
| `tread_round_R` | 0.2 | 5.08 | bilgi | `S_P07_tread` kenar yayları |
| `tread_bore_R` | 1.56375 | 39.7192 | bilgi | `S_P07_tread` iç yarıçap |
| `core_R` | 1.51375 | 38.4492 | sürücü | `P09_WheelCoreDisc` yarıçapı (P08 / P10 taslaklarında sayı) |
| `core_W` | 0.625 | 15.875 | sürücü | `P09_WheelCoreDisc` genişliği |
