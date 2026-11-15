# Build log — P01 Spanner (build123d 0.11.1, inç)

## Yapılanlar
1. **F1** Dış hat, spec'teki 11 segment sırasıyla Y=0 düzleminde 3B kenarlar olarak (x,0,z) kuruldu
   (doğrular `make_line`, yaylar `make_three_point_arc`). Yay ara noktaları: sap ucu için (2.1655, -0.194895),
   sırt yayı için en alt nokta (-1.507307, -0.707013), uç yayı için en sol nokta (-2.1655, -0.242941);
   boyun ve ağız yayları için verilen merkez/yarıçaptan kısa yol açıortay noktası hesaplandı
   (ağız yayı alttan geçer, malzeme çemberin dışında). Yüz Y=-0.06'ya kaydırılıp +Y yönünde 0.12 ekstrüde edildi.
2. **F2** Obround kanal aynı şekilde yüz olarak kuruldu, ekstrüde edilip çıkarıldı.
3. **F3/F4** Kenar yuvarlatmaları BRep fillet yerine "kesici gövde" ile yapıldı (kısmi uzunlukta, konik bitişli
   fillet OCC'de doğrudan yok):
   - Düz kenar kesicisi (üst, +Y köşe): X_RUNOUT..X_END_C arası köşe kutusu − (R1/64 silindir
     [X_ROUND_START..X_END_C] ∪ 10° koni [X_RUNOUT..X_ROUND_START], r: 0.022097→0.015625).
     Z_MID'e göre ve Y=0'a göre aynalanarak 4 köşe elde edildi.
   - Uç kesicisi: uç merkezi ekseni etrafında halka − torus (R 0.179270 / r 0.015625), x ≥ X_END_C yarısı; ±Y.
   - Tüm kesiciler birleştirilip plakadan tek seferde çıkarıldı.
4. STEP AP214, **inç** birimiyle yazıldı (`write.step.unit = INCH`). build123d'nin `unit=Unit.IN`
   parametresi tek başına dosyayı mm'ye ölçekleyip mm etiketiyle yazıyordu; bu yakalandı ve düzeltildi.
   Dosya geri okunarak doğrulandı (1 katı, 27 yüz, 0.208501 in³).

## Takıldığım yerler
- Yalnızca STEP birimi (yukarıda). Geometri ilk denemede hedefleri tuttu.

## Bilerek basitleştirilen / yorumlanan
- Kaynak dosyadaki 19 boş mikro kutu (114 sıfır alanlı yüz) spec gereği üretilmedi.
- Konik bitiş için spec'teki formül aynen kullanıldı; koninin X_RUNOUT'taki yarıçapı köşe mesafesine tam eşit
  (0.022097) olduğundan kesik orada sıfıra iner.
- Gövde etiketi "P01 Spanner".

## Ölçüm ve hedef karşılaştırması (betik çıktısı, inç)
| Büyüklük | Hedef | Model | Fark |
|---|---|---|---|
| Hacim in³ | 0.208501 | 0.208501 | <1e-6 (mm³: 3416.716 / 3416.715) |
| Alan in² | 4.612036 | 4.612037 | ~1e-6 (mm²: 2975.5015 / 2975.501) |
| CoM X | -0.088238 | -0.088237 | 1e-6 |
| CoM Y | 0 | 0.000000 | 0 |
| CoM Z | -0.251719 | -0.251719 | 0 |
| X min/max | -2.165500 / 2.165500 | -2.165500 / 2.165500 | 0 |
| Y min/max | -0.06 / 0.06 | -0.060000 / 0.060000 | 0 |
| Z min/max | -0.707013 / 0 | -0.707013 / 0.000000 | 0 |
| Yüz sayısı | 27 (+114 boş) | 27 | tam (11 silindir, 10 düzlem, 4 koni, 2 torus) |
| Katı sayısı | 1 | 1, `is_valid = True` | — |
