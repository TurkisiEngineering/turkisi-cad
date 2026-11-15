# Parametreler (birim: inç, açı: derece) — `spanner.py` başındaki değişkenler

| Ad | Değer | Özellik |
|---|---|---|
| T | 0.12 | Plaka kalınlığı, Y = -0.06..+0.06 (F1 ekstrüzyon) |
| Y0 | -T/2 = -0.06 | Ekstrüzyon başlangıç düzlemi |
| X_HEAD_TOP | -1.354007 | Sap üst kenarının (Z=0) baş tarafı ucu (F1 seg. 1/11) |
| X_END_C | 1.970605 | Sap ucu yarım dairesinin merkez X'i (F1 seg. 2, F3) |
| R_END | 0.194895 | Sap ucu yarıçapı (F1 seg. 2) |
| W_HANDLE | 2·R_END = 0.389790 | Sap genişliği (alt kenar Z) |
| Z_MID | -R_END = -0.194895 | Sap orta yüksekliği (kanal ekseni, ayna düzlemi) |
| X_NECK | -0.703984 | Sap alt kenarının bittiği X (F1 seg. 3/4) |
| R_NECK | 0.468750 (15/32) | İçbükey boyun yayı (F1 seg. 4) |
| P_NECK_END | (-1.024250, -0.516259) | Boyun yayı sonu |
| R_BACK, C_BACK | 0.707013, (-1.507307, 0) | Başın dış sırt yayı (F1 seg. 5) |
| P_BACK_END | (-2.159435, -0.273121) | Sırt yayı sonu |
| R_TIP, C_TIP | 0.078125 (5/64), (-2.087375, -0.242941) | Kanca ucu yuvarlağı (F1 seg. 6) |
| P_TIP_END | (-2.104284, -0.166668) | Uç yayı sonu |
| P_HOOK_TOP | (-1.931443, -0.128350) | Kanca üst yüzü sonu (F1 seg. 7) |
| P_PIN_TIP | (-1.864243, -0.193720) | Pim ucu (F1 seg. 8) |
| P_PIN_UNDER | (-1.922674, -0.215905) | Pim alt yüzü sonu, uzunluk 0.0625 (F1 seg. 9) |
| R_JAW, C_JAW | 0.3125 (5/16), (-1.696750, 0) | Ağız yayı, Ø0.625 somun (F1 seg. 10) |
| P_JAW_END | (-1.411824, -0.128350) | Ağız yayı sonu (F1 seg. 10/11) |
| SLOT_C1, SLOT_C2 | 1.918717, 1.944702 | Askı kanalı yarım daire merkezleri X (F2) |
| SLOT_R | 0.064965 | Kanal yarıçapı, genişlik 0.129930 (F2) |
| R_ROUND | 0.015625 (1/64) | Sap kenar yuvarlatma yarıçapı (F3) |
| YC | T/2 - R_ROUND = 0.044375 | Yuvarlatma merkez çizgisi \|Y\| (F3/F4) |
| X_ROUND_START | -0.441484 | Tam yuvarlatmanın başladığı X (F3/F4) |
| RUNOUT_ANGLE | 10 | Konik bitiş yarı açısı (F4) |
| X_RUNOUT | -0.478189 | Konik bitişin keskin köşeye ulaştığı X (F4); hesaplanan r = 0.022097 = √2·R_ROUND |
| BIG | 0.1 | Kesici kutuların dışa taşma payı (yardımcı; geometriye etkisi yok) |
