# Parametreler — P01 Plate

Hepsi SolidCraft belgesinde (`plate.sc`) kullanıcı parametresi olarak tanımlı (`parameters.add`, `plate_build.json` adım 2–9).
Birim: mm.

| Ad | Değer | Kullanıldığı özellik |
|---|---|---|
| `L` | 100 mm | F1 `SK_F1_Plate` dikdörtgen köşeleri X = ±L/2; F3 delik merkezleri X = ±(L/2 − E_hole) |
| `W` | 60 mm | F1 `SK_F1_Plate` dikdörtgen köşeleri Y = ±W/2; F3 delik merkezleri Y = ±(W/2 − E_hole) |
| `T` | 10 mm | F1 `F1_Plate_Block` ekstrüzyon mesafesi; F3 `F3_Corner_Holes` kesme mesafesi (tam kalınlık); F4 `SK_F4_Pocket` eskiz düzlemi ofseti (Z = T) |
| `R_corner` | 3 mm | F2 dikey köşe yuvarlatması (`solid.fillet`, 4 kenar) |
| `D_hole` | 6 mm | F3 `SK_F3_Holes` 4 dairenin çapı |
| `E_hole` | 8 mm | F3 delik merkezinin bitişik dış kenara uzaklığı (merkezler ±42, ±22) |
| `D_pocket` | 20 mm | F4 `SK_F4_Pocket` daire çapı |
| `H_pocket` | 4 mm | F4 `F4_Central_Pocket` kesme derinliği (taban Z = T − H_pocket = 6) |

SolidCraft eskiz/özellik boyutlarını otomatik `d1…d10` adlarıyla da listeler; bunların hepsi yukarıdaki
adlara bağlı ifadelerdir (ör. `d3 = D_hole`, `d10 = H_pocket`), bağımsız değer taşımazlar.

Türetilen kontrol ölçüleri: delik merkez aralığı X = L − 2·E_hole = 84, Y = W − 2·E_hole = 44;
yuvarlatma merkezleri (±(L/2 − R_corner), ±(W/2 − R_corner)) = (±47, ±27).
