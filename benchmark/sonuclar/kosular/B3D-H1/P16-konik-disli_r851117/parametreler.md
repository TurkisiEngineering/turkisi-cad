# Parametreler (miter_gear.py)

| Ad | Değer | Özellik |
|---|---|---|
| N_TEETH | 20 | Diş sayısı / kesici dairesel dizisinin adedi |
| PITCH_ANGLE | 360/20 = 18° | Kesici kopyaları arası açı (Y ekseni etrafında) |
| BORE_R | 4.0 mm | Delik yarıçapı (Ø8, boydan boya) |
| BORE_CHAMFER | 0.4 mm | Delik pahı 0.4×45°, iki uçta |
| HUB_R | 12.5 mm | Göbek yarıçapı (Ø25) |
| HUB_LEN | 7.75 mm | Göbek boyu (y=0 → 7.75) |
| HEEL_TIP | (16.385, 9.36) | Topuk dış köşesi (r, y); dış çap 32.77; arka koni ucu |
| TOE_TIP | (11.73752, 19.33) | Burun diş ucu kenarı; toplam genişlik 19.33 |
| FRONT_Y | 18.0 mm | Ön yüz düzlemi |
| FRONT_R | 8.5 mm | Ön yüz dış yarıçapı (burun konisi başlangıcı) |
| BLANK_PROFILE | 9 noktalı (r,y) çokgen | Döndürülmüş kütük (spec 3.A) |
| SA_FLANK / SA_FILLET / SA_ROOT | spec tablosu | Topuk tarafı kesit S_A: sağ yanak, sağ taban radyusu, taban Bezier kutupları |
| SB_FLANK / SB_FILLET / SB_ROOT | spec tablosu | Burun ötesi kesit S_B kutupları |
| KNOTS_6 | (0,0,0,0,0.5,0.5,1,1,1,1) | 6 kutuplu kübik B-spline düğüm vektörü (yanak, radyus) |
| KNOTS_BEZ | (0,0,0,0,1,1,1,1) | Taban kübik Bezier |
