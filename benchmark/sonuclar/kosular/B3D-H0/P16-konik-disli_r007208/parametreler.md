# Parametreler (miter_gear.py)

Birim mm / derece. Çerçeve: dişli ekseni = Y, arka yüz y = 0, dişler +Y'ye, diş boşluğu +Z'de.

| Ad | Değer | Özellik |
|---|---|---|
| N_TEETH | 20 | Diş sayısı; kesici desen adedi |
| PITCH_ANGLE_STEP | 360/20 = 18° | Kesici dairesel desen adımı (Y ekseni etrafında) |
| BORE_R | 4.0 | Delik yarıçapı (Ø8, boydan boya) |
| BORE_CHAMFER | 0.4 | Delik pahı 45° × 0.4, iki uçta |
| HUB_R | 12.5 | Göbek yarıçapı (Ø25) |
| HUB_LEN | 7.75 | Göbek boyu (göbek / arka koni köşesi y) |
| HEEL_TIP_R | 16.385 | Topuk diş üstü kenarı yarıçapı (dış çap 32.77) |
| HEEL_TIP_Y | 9.36 | Topuk diş üstü kenarı yüksekliği |
| TOE_TIP_R | 11.73752 | Burun diş üstü kenarı yarıçapı |
| TOE_TIP_Y | 19.33 | Toplam genişlik (burun diş üstü kenarı y) |
| FRONT_FACE_OUT_R | 8.5 | Ön yüz halkasının dış yarıçapı |
| FRONT_FACE_Y | 18.0 | Ön yüz düzlemi y |
| BLANK_PROFILE | 9 köşe (r, y) | Döndürülen ham parça profili (spec §3A) |
| SA_FLANK / SA_FILLET / SA_ROOT | spec tablosu | Kesici kesit S_A (topuk tarafı) kutupları: sağ yanak, sağ kök radyüsü, kök Bezier |
| SB_FLANK / SB_FILLET / SB_ROOT | spec tablosu | Kesici kesit S_B (burun ötesi) kutupları |
| BSPL_KNOTS / BSPL_MULTS | (0, 0.5, 1) / (4, 2, 4) | 6 kutuplu kübik B-spline düğüm vektörü (0,0,0,0,.5,.5,1,1,1,1) |
| BEZ_KNOTS / BEZ_MULTS | (0, 1) / (4, 4) | Kök eğrisi kübik Bezier |
| DEGREE | 3 | Eğri derecesi |
