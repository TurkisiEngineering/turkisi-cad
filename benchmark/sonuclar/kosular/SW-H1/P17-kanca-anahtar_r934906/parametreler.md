# Parametreler (birim: inch, açı: derece)

Tamamı `build_spanner.py` içindeki `P` sözlüğündedir. `*` işaretliler ayrıca SolidWorks Equation Manager'da
global değişkendir; `T` doğrudan `D1@F1_Outline` ölçüsünü sürer (`"D1@F1_Outline" = "T"`), diğer global
değişkenler bilgi amaçlıdır (çizim geometrisi betikten koordinatla üretiliyor, ölçü ile değil).

| Ad | Değer | Özellik |
|---|---|---|
| T * | 0.12 | F1_Outline: simetrik (mid-plane) ekstrüzyon kalınlığı, Y=±0.06 |
| Y_FACE | 0.06 (=T/2) | F3/F4 köşe profillerinin yüz konumu |
| X_HEAD_TOP | -1.354007 | F1 seg 1/11: sap üst kenarının sol ucu |
| X_END_C | 1.970605 | F1 seg 2 yay merkezi x; F3a kesim bitişi; F3b dönüş ekseni |
| R_END * | 0.194895 | F1 seg 2: sap ucu yarım daire yarıçapı |
| W_HANDLE * | 0.389790 | F1 seg 3: sap genişliği (alt kenar Z=-W) |
| Z_MID | -0.194895 (=-W/2) | F2 yuva ekseni, F3b dönüş ekseni, PL_EndAxis düzlemi |
| X_NECK | -0.703984 | F1 seg 3/4 geçişi |
| R_NECK * | 0.468750 | F1 seg 4: içbükey boyun yayı (15/32) |
| NECK_END | (-1.024250, -0.516259) | F1 seg 4/5 noktası |
| HEAD_C, R_HEAD * | (-1.507307, 0), 0.707013 | F1 seg 5: kafa sırtı yayı (kafa yüksekliği) |
| HOOK_P1 | (-2.159435, -0.273121) | F1 seg 5/6 noktası |
| HOOK_C, R_HOOK * | (-2.087375, -0.242941), 0.078125 | F1 seg 6: kanca ucu (5/64) |
| HOOK_P2 | (-2.104284, -0.166668) | F1 seg 6/7 noktası |
| PIN_TOP | (-1.931443, -0.128350) | F1 seg 7/8: pim üst köşesi |
| PIN_TIP | (-1.864243, -0.193720) | F1 seg 8/9: pim ucu |
| PIN_LOW | (-1.922674, -0.215905) | F1 seg 9/10: pim alt kenarı (0.0625) |
| JAW_C, R_JAW * | (-1.696750, 0), 0.3125 | F1 seg 10: çene yayı (Ø0.625 somun) |
| JAW_END | (-1.411824, -0.128350) | F1 seg 10/11 noktası |
| SLOT_X1, SLOT_X2 | 1.918717, 1.944702 | F2_Slot: obround yuva merkezleri |
| SLOT_R * | 0.064965 | F2_Slot: yuva yarıçapı (genişlik 0.129930) |
| R_EDGE * | 0.015625 | F3a_HandleRounds, F3b_EndRound: kenar yuvarlatma (1/64); F4 koni başlangıç yarıçapı |
| X_ROUND_START * | -0.441484 | F3a başlangıcı, F4 koni başlangıcı |
| X_RUNOUT_END * | -0.478189 | F4 koni bitişi (kenar yeniden keskin) |
| RUNOUT_ANG * | 10 | F4 koni yarım açısı → r2 = 0.022097 |
