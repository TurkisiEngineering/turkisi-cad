# Parametreler (SolidWorks Equation Manager global değişkenleri, mm)

| Ad | Değer | Bağlı olduğu özellik / boyut |
|---|---|---|
| `L` | 100 | `D1@SK_PlateOutline` — F1 dikdörtgen uzunluğu (X) |
| `W` | 60 | `D2@SK_PlateOutline` — F1 dikdörtgen genişliği (Y) |
| `T` | 10 | `D1@F1_PlateBlock` — F1 ekstrüzyon kalınlığı; `D1@PL_TopZ10` — F4 çizim düzlemi ofseti (Z=T) |
| `R_corner` | 3 | `D1@F2_CornerRounds` — F2 dikey köşe radyüsü |
| `D_hole` | 6 | `D1@SK_CornerHoles` — F3 delik çapı (sürücü boyut 1 delikte; diğer 3 delik betikte aynı çapla çiziliyor) |
| `E_hole` | 8 | F3 delik merkezlerinin dış kenarlara uzaklığı — betikte merkezler `(±(L/2−E_hole), ±(W/2−E_hole))` = (±42, ±22) olarak hesaplanır; modelde canlı denklem bağı yok |
| `D_pocket` | 20 | `D1@SK_Pocket` — F4 cep çapı |
| `H_pocket` | 4 | `D1@F4_CentralPocket` — F4 cep derinliği (taban Z = T − H_pocket = 6) |

Betik tarafında aynı değerler `build_p01.py` içindeki `P` sözlüğündedir; değiştirip betiği yeniden çalıştırmak tüm modeli yeniden üretir.
