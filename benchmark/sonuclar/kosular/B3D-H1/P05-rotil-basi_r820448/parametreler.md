# Parametreler (`rod_end.py`, birim: inç)

| Ad | Değer | Özellik |
|---|---|---|
| EYE_R | 0.75 | P01 F1 göz küresi yarıçapı (Ø1.5) |
| BALL_CY | 1.0 | göz / bilye / yuva merkezi y |
| NECK_ARC_R | 0.5 | F2 boyun içbükey yayı yarıçapı |
| NECK_ARC_CR | 0.75 | F2 yay merkezi r (merkez (r,y)=(0.75,0)) |
| NECK_TOP_Y | 0.4 | F2 boyun üst ucu (küreye teğet, r=0.45) |
| FLAT_Z | 0.22656 | F3 yan düzlükler z=±0.22656 (kalınlık 0.45312) |
| SLOPE_Y | 0.09062 | F3 boyun eğiminin bittiği y |
| SLOPE_Z0 | 0.25 | F3 eğimin y=0'daki yarı genişliği |
| SOCKET_R | 0.5625 | F4 bilye yuvası küre yarıçapı |
| SHANK_LEN | 1.625 | F5 şaft uzunluğu, uç yüz y=-1.625 |
| MAJOR_R | 0.25 | F5 diş tepe yarıçapı (Ø0.5) |
| MINOR_R | 0.21752 | F5 diş dibi yarıçapı (Ø0.43504) |
| THREAD_DEPTH | 0.03248 (= MAJOR_R - MINOR_R) | diş derinliği |
| PITCH | 0.05 | adım (20 TPI), sağ el, tek ağız |
| FLAT_W | 0.00625 (= P/8) | dip ve tepe düzlük genişliği |
| FLANK_HALF | 30° | yanak açısı (60° dahili) |
| ROOT_PHASE_Y | 0.003125 (= P/16) | +X tarafında dip düzlüğü merkezi y = 0.003125 - 0.05k (spec 0.0031) |
| END_FLAT_R | 0.205 | uç yüz düz disk yarıçapı; 45° pah r 0.205→0.25 |
| RUNOUT_TOP_R | 0.25 | diş çıkış konisi r = 0.25 + y (45°) |
| SHANK_EXTRA | 0.3 | yalnız kurulum: kesim için şaft kütüğünün uç yüzün altına geçici uzatması |
| GROOVE_OVERRUN | 0.003 | yalnız kurulum: kesici profil yanağı tepe yarıçapının 0.003 ötesine uzatılır |
| GROOVE_CLEAR | 0.02 | yalnız kurulum: kesici dış yarıçapı = MAJOR_R + 0.02 |
| K_START | 37 | helis başlangıcı: dip merkezi y = 0.003125 - 37·0.05 = -1.8469 |
| TURNS_PER_SEG | 19 | helis sweep'i segment başına tur sayısı |
| N_SEGS | 2 | segment sayısı (2×19 tur, y -1.847 … +0.053) |
| BALL_R | 0.5625 | P02 bilye küresi (Ø1.125) |
| COLLAR_R | 0.35 | P02 mesafe bileziği yarıçapı (Ø0.70) |
| COLLAR_HALF | 0.625 | bilezik yarı boyu (toplam 1.25) |
| BORE_R | 0.25 | bilye deliği (Ø0.5) |
| BORE_CHAMFER | 0.025 | delik ağız pahı 45° × 0.025 |
