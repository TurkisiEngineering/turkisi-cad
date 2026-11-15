# Parametreler (birim: inch, açı: derece) — `spanner.py`

| Ad | Değer | Özellik |
|---|---|---|
| T | 0.12 | F1 plaka kalınlığı (Y = ±0.06) |
| H_W | 0.389790 | F1 sap genişliği |
| X_HEAD | -1.354007 | F1 sap üst kenarının başlangıcı (adım 1/11) |
| X_END | 1.970605 | F1 sap ucu yarım dairesinin merkez x'i |
| R_END | 0.194895 (=H_W/2) | F1 sap ucu yarıçapı (adım 2) |
| Z_MID | -0.194895 | Sap orta yüksekliği |
| X_NECK | -0.703984 | F1 sap alt kenarı sonu (adım 3) |
| R_NECK, C_NECK | 0.468750, (-0.703984, -0.858540) | F1 iç bükey boyun yayı (adım 4) |
| P_NECK_END | (-1.024250, -0.516259) | adım 4 bitişi |
| R_BACK, C_BACK | 0.707013, (-1.507307, 0) | F1 kafa sırtı yayı (adım 5) |
| P_BACK_END | (-2.159435, -0.273121) | adım 5 bitişi |
| R_TIP, C_TIP | 0.078125, (-2.087375, -0.242941) | F1 kanca ucu yuvarlatması (adım 6) |
| P_TIP_END | (-2.104284, -0.166668) | adım 6 bitişi |
| X_LEFT | -2.165500 | en sol nokta (adım 6 ara noktası) |
| P_HOOK_TOP | (-1.931443, -0.128350) | kanca üst yüzü sonu (adım 7) |
| P_PIN_TIP | (-1.864243, -0.193720) | pim ön yüzü sonu / pim ucu (adım 8) |
| P_PIN_UNDER | (-1.922674, -0.215905) | pim alt yüzü sonu (adım 9) |
| R_JAW, C_JAW | 0.312500, (-1.696750, 0) | F1 çene yayı, Ø0.625 somun (adım 10) |
| P_JAW_END | (-1.411824, -0.128350) | adım 10 bitişi |
| SLOT_C1, SLOT_C2 | 1.918717, 1.944702 | F2 oval delik yarım daire merkezleri x |
| SLOT_R | 0.064965 | F2 oval delik yarıçapı (genişlik 0.129930) |
| SLOT_ZC | -0.194895 | F2 oval delik merkez z |
| R_RND | 0.015625 | F3 sap kenar yuvarlatma yarıçapı |
| X_RND_START | -0.441484 | F3 düz yuvarlatmaların başlangıcı |
| RUNOUT_HALF_ANGLE | 10 | F4 konik bitiş yarı açısı |
| X_RUNOUT_END | -0.478189 | F4 konik bitişin keskin kenara döndüğü x |
