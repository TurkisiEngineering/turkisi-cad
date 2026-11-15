# Build log — P01 Spanner (spec P17)

## Yöntem
1. **F1:** 11 segmentli dış hat, global XZ düzleminde (y = 0) doğrudan 3B noktalarla kuruldu
   (`Edge.make_line`, `Edge.make_three_point_arc`). Adım 4 ve 10'daki yayların ara noktası spec'teki
   merkez ve yarıçaptan hesaplandı; adım 2, 5 ve 6 için spec'in verdiği uç noktalar (en sağ, en alt, en sol)
   kullanıldı. `extrude(..., amount=0.06, both=True)` ile Y = ±0.06.
2. **F2:** `SlotCenterToCenter(0.025985, 0.129930)` XZ düzleminde (1.9317095, -0.194895) merkezde, Y boyunca delindi.
3. **F3/F4:** Konik bitiş `fillet` ile yapılamadığı için yuvarlatmalar malzeme çıkarma gövdeleriyle kuruldu.
   +Y/üst köşe için çıkarma gövdesi: köşe kutusu (x = -0.484 … 1.970605), eksi R0.015625 silindir
   (x ≥ -0.441484; eksen y = 0.044375, z = -0.015625), eksi koni (10° yarı açı, x = -0.441484'te r = 0.015625).
   Koni, keskin kenara döndüğü noktanın 0.012 ötesine uzatıldı; böylece x < -0.478189'da hiç malzeme kalkmıyor.
   Uçtaki yuvarlatma için (kare − daire) profili sap ucu merkezi etrafında döndürüldü ve x ≥ 1.970605
   yarısı alındı (toroidal yuvarlatma). Bu çıkarma gövdesi alt kenar için z = Z_MID düzlemine, -Y yüzü için
   XZ düzlemine göre aynalandı; 4 kopya çıkarıldı.
4. Kaynak artefakt (19 boş mikro-kutu) bilerek üretilmedi.

## Takılma / basitleştirme
- Takılma olmadı, basitleştirme yapılmadı.
- Yorum gerektiren tek nokta: konik bitiş x = -0.478189'da köşeye teğet değiyor. Dejenere bir boolean
  oluşmasın diye koni bu noktanın biraz ötesine uzatıldı; çıkan geometri spec'le aynı.
- Not: teslim belgelerini heredoc ile yazan bir kabuk komutu ortam hook'u tarafından engellendi.
  Belgeler bunun yerine dosya yazma aracıyla oluşturuldu; modele bir etkisi yok.

## Ölçüm vs hedef (inch)
| Büyüklük | Hedef | Ölçülen |
|---|---|---|
| Hacim | 0.208501 | 0.208501 |
| Alan | 4.612036 | 4.612037 |
| CoM X / Y / Z | -0.088238 / 0 / -0.251719 | -0.088237 / 0.000000 / -0.251719 |
| X min/max | ±2.165500 | ±2.1655 |
| Y min/max | ±0.06 | ±0.06 |
| Z min/max | -0.707013 / 0 | -0.707013 / 0 |
| Yüz sayısı | 27 | 27 |
| Katı sayısı | 1 | 1 (geçerli) |

`final.step` AP214 (AUTOMOTIVE_DESIGN) şemasıyla yazıldı. Tekrar içe aktarıldığında 1 katı / 27 yüz / 0.208501 in³.
