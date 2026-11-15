# Parametreler: P01 Miter gear

Birim mm, açılar derece. Bu adlar `betikler/build_gear.py` içindeki `P` sözlüğünde tanımlı. Betik aynı adları
SolidWorks parçasına **global değişken** olarak da yazıyor (Araçlar > Denklemler).

| Ad | Değer | Kullanıldığı özellik |
|---|---|---|
| BoreDia | 8.0 | `Sk_BlankProfile` / `Blank_Revolve`: delik çapı (r = 4.0) |
| BoreChamfer | 0.4 | `Sk_BlankProfile`: iki uçta 45° delik pahı |
| HubDia | 25.0 | `Sk_BlankProfile`: göbek çapı (r = 12.5) |
| HubLength | 7.75 | `Sk_BlankProfile`: göbek silindir boyu (y 0 → 7.75) |
| BackConeR | 16.385 | `Sk_BlankProfile`: arka koni ile diş üstü konisinin köşe yarıçapı |
| BackConeY | 9.36 | `Sk_BlankProfile`: aynı köşenin yüksekliği (topuk dış çapı 32.77) |
| ToeTipR | 11.73752 | `Sk_BlankProfile`: diş üstü konisi ile uç konisinin köşe yarıçapı |
| FaceWidthY | 19.33 | `Sk_BlankProfile`: toplam genişlik (uç diş kenarı y = 19.33) |
| ToeR | 8.5 | `Sk_BlankProfile`: uç konisinin ön yüzdeki iç yarıçapı |
| FrontFaceY | 18.0 | `Sk_BlankProfile`: ön yüz yüksekliği |
| NTeeth | 20 | `ToothSpace_Pattern`: dairesel çoğaltma adedi (denklemle bağlı: `"D1@ToothSpace_Pattern" = "NTeeth"`) |
| SpaceAngle0 | 90 | Modellenen diş boşluğunun konumu (+Z); kutup noktaları zaten bu konumda verildiği için yalnızca bilgi amaçlı |

Diş boşluğu kesicisinin kutupları (`SA_FLANK`, `SA_FILLET`, `SA_ROOT`, `SB_FLANK`, `SB_FILLET`, `SB_ROOT`) ve düğüm
vektörleri (`KNOTS6` = (0,0,0,0,0.5,0.5,1,1,1,1), `KNOTS4` = Bezier) betikte isimli sabitler olarak duruyor.
Bunlar `Sk3D_SectionA_heel` ve `Sk3D_SectionB_toe` 3B eskizlerini, onlar da `ToothSpace_Cut` loft kesimini
besliyor. Sol yarı, `mirror()` ile x → −x yansıtılarak üretiliyor.

Not: Gövde eskizinin noktaları bu parametrelerden betikte hesaplanıyor. Global değişkenler SolidWorks'te var, fakat
eskiz ölçülerine denklemle **bağlı değil**. Bağlı olan tek değişken NTeeth (desen adedi). Boyut değiştirmek için
betikteki `P` değerini değiştirip betiği yeniden çalıştırın (ayrıntı `build_log.md`'de).
