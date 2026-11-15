# Parametreler — P01 Plate

Hepsi SolidWorks **Global Variables** (Equations yöneticisi), birim mm. Ölçüler denklemlerle bu değişkenlere bağlı;
bir değişkeni değiştirip yeniden oluşturmak modeli günceller (test edildi: `Plate_L = 120` → X = -60…60, merkezli kalıyor).

| Ad | Değer | Hangi özellik / ölçü |
|---|---|---|
| `Plate_L` | 100 | F1_PlateBlock — Sketch1 ölçüsü `L@Sketch1` (X boyu, merkez dikdörtgen) |
| `Plate_W` | 60 | F1_PlateBlock — Sketch1 ölçüsü `W@Sketch1` (Y eni) |
| `Plate_T` | 10 | F1_PlateBlock — ekstrüzyon derinliği `D1@F1_PlateBlock` (Z = 0 → 10) |
| `Corner_R` | 3 | F2_CornerRounds — fillet yarıçapı `D1@F2_CornerRounds` (4 dikey köşe kenarı) |
| `Hole_D` | 6 | F3_CornerHoles — Sketch2 çap ölçüleri `HoleD1..4@Sketch2` |
| `Hole_PX` | 84 | F3_CornerHoles — delik X aralığı; `HoleX1..4@Sketch2 = Hole_PX / 2` (orijinden yatay) |
| `Hole_PY` | 44 | F3_CornerHoles — delik Y aralığı; `HoleY1..4@Sketch2 = Hole_PY / 2` (orijinden dikey) |
| `Pocket_D` | 20 | F4_CentralPocket — Sketch3 çap ölçüsü `PocketD@Sketch3` |
| `Pocket_Depth` | 4 | F4_CentralPocket — kör kesim derinliği `D1@F4_CentralPocket` (taban Z = 6) |

Aynı değerler `build_plate.py` başındaki `P = dict(...)` sözlüğünde de tanımlı (betik global değişkenleri buradan yaratır).
