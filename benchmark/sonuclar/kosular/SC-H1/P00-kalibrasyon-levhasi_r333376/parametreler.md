# Parametreler (SolidCraft kullanıcı parametreleri, mm)

| Ad | Değer | Kullanıldığı özellik |
|---|---|---|
| `L` | 100 mm | `PlateSketch` dikdörtgen genişliği (X) → `F1_PlateBlock`; `F3_CornerHole` X konumu `-(L/2 - hole_inset)`; `F3_CornerHoles` X aralığı `L - 2*hole_inset` |
| `W` | 60 mm | `PlateSketch` dikdörtgen yüksekliği (Y) → `F1_PlateBlock`; `F3_CornerHole` Y konumu `-(W/2 - hole_inset)`; `F3_CornerHoles` Y aralığı `W - 2*hole_inset` |
| `T` | 10 mm | `F1_PlateBlock` ekstrüzyon mesafesi (Z=0…T); `F3_CornerHole` kesici boyu `T + 2`; `F4_CentralPocket` taban Z'si `T - pocket_depth` |
| `corner_r` | 3 mm | `F2_CornerRounds` köşe yuvarlatma yarıçapı |
| `hole_d` | 6 mm | `F3_CornerHole` (ve desenle `F3_CornerHoles`) delik çapı |
| `hole_inset` | 8 mm | Delik merkezinin komşu dış kenarlara uzaklığı → `F3_CornerHole` konumu, `F3_CornerHoles` aralıkları (84 × 44) |
| `pocket_d` | 20 mm | `F4_CentralPocket` cep çapı |
| `pocket_depth` | 4 mm | `F4_CentralPocket` cep derinliği (taban Z = T - pocket_depth = 6) |

Türetilmiş değerler: delik aralığı X = `L - 2*hole_inset` = 84, Y = `W - 2*hole_inset` = 44; köşe yuvarlak merkezleri
(±(L/2 - corner_r), ±(W/2 - corner_r)) = (±47, ±27).

Parametrik deneme (`check_parameters`, sonra geri alındı): L=120, hole_inset=10, pocket_depth=5 → hata yok, hacim
69221.19 mm³ (analitik 69220.97), delikler (±50, ±20), köşe merkezleri (±57, ±27), cep tabanı Z=5: model parametreleri izliyor.
