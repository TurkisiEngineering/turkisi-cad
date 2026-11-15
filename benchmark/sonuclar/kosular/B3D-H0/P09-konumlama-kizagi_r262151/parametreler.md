# Parametreler (`model.py` başı, birim: inç)

| Ad | Değer | Özellik |
|---|---|---|
| Y0 | 0.0424438 | Vida ekseni yüksekliği (x = 0); çoğu y değeri buna göre |
| BASE_L / BASE_W | 4.0 / 2.5 | P01 taban boyu (Z) / genişliği (X) |
| BASE_YBOT / BASE_YTOP | Y0−0.437 = −0.39456 / Y0+0.313 = 0.35544 | P01 alt (montaj) yüzü / üst yüzü |
| WAY_TOP_HALF | 0.66249 | P01 kırlangıç kanal üst açıklık yarı genişliği |
| WAY_FLOOR_Y / WAY_FLOOR_HALF | −0.01956 / 0.87900 | P01 kırlangıç taban yüksekliği / yarı genişliği (60° yanaklar) |
| GROOVE_HALF / GROOVE_FLOOR_Y | 0.562 / −0.13456 | P01 orta oluk yarı genişliği / tabanı |
| MOUNT_HOLES_XZ | (−0.343, 0.5), (0.343, 3.5) | P01 F2 havşalı delik eksenleri |
| CSK_DIA / CSK_BOT_Y / MOUNT_HOLE_DIA | 0.385 / −0.24212 / 0.198 | P01 F2 havşa (82°) çapı, havşa alt y, delik çapı |
| END_HOLE_X / END_HOLE_Y | 1.031 / −0.01956 | P01 F3, P04, P05 delikleri ve H1 eksenleri |
| END_HOLE_DIA / END_HOLE_DEPTH | 0.164 / 0.625 | P01 F3 uç delikleri çapı / derinliği |
| CAR_Z0 / CAR_Z1 | 1.5 / 4.0 | P02 taşıyıcı Z aralığı (+Z limit pozu) |
| CAR_TOP_Y / CAR_TOP_HALF | 0.41044 / 0.62308 | P02 üst yüz yüksekliği / yarı genişliği |
| CAR_UNDER_Y / CAR_FLANK_BOT_HALF | −0.00656 / 0.86383 | P02 alt yüz / yanak alt yarı genişliği |
| CHAN_BOT_HALF / CHAN_TOP_HALF / CHAN_CEIL_Y | 0.56452 / 0.43750 / 0.21344 | P02 alt kanal |
| CROWN_R / CROWN_C / CROWN_X | 0.312 / (0, −0.05356) / 0.16142 | P02 kanal tepe yayı |
| STRIP_Z / STRIP_ROUND_R | (1.6–2.1), (3.4–3.9) / 0.01 | P02 F2 aşınma şeritleri Z aralıkları / köşe yuvarlatma |
| NUT_Z / NUT_DIA | 2.75 / 0.995 | P02 F3 somun deliği ve P03 somun ekseni / çapı |
| TOP_HOLES_Z / TOP_HOLE_DIA | 1.718, 2.156, 3.344, 3.78 / 0.164 | P02 F4 üst delikler |
| F5_P1 / F5_P2 / F5_Z | (0.59562, −0.00656) / (0.56437, −0.00631) / (1.5–2.3125), (3.1875–4.0) | P02 F5 kaynak artefaktı (+X) |
| NUT_YBOT | −0.11156 | P03 somun alt yüzü (üst = CAR_TOP_Y) |
| EB_Z0 / EB_Z1 / EB_YBOT / EB_YTOP | 4.0 / 4.625 / −0.38456 / 0.40544 | P04 yatak bloğu |
| EB_CLEAR_DIA | 0.201 | P04 vida geçiş delikleri |
| EB_BORE | (4.0–4.155 Ø0.28125), (4.155–4.375 Ø0.339), (4.375–4.625 Ø0.375) | P04 kademeli delik |
| EP_Z0 / EP_Z1 / EP_YBOT / EP_YTOP / EP_HOLE_DIA | −0.062 / 0 / −0.38456 / 0.35544 / 0.185 | P05 uç plakası |
| LS_Z0 / LS_ZT / LS_Z1 | 0.5 / 4.0 / 5.0 | P06 vida başı / dişli bölüm sonu / mil ucu |
| LS_MAJOR_R / LS_SHAFT_R | 0.125 / 0.109 | P06 diş dış yarıçapı / düz mil yarıçapı |
| LS_CHAMFER_R0 / LS_CHAMFER_Z | 0.08711 / 0.56563 | P06 30° uç pahı |
| PITCH | 0.05 | P06 hatve (tek ağız, sağ) |
| ROOT_R / ROOT_HALF_LAND / FLANK_ANGLE | 0.09252 / 0.003125 / 30° | P06 oluk profili (kök Ø0.18504, 60° dahili) |
| GROOVE_OUT_R | 0.13 | P06 oluk takımının dış yarıçapı (0.125'in ötesine uzatma) |
| ROOT_Z_PHASE | 0.515625 | P06 θ = 0'da kök merkezi z |
| GROOVE_START_K | −2 | P06 süpürme başlangıç turu (z = 0.5'in dışında) |
| GROOVE_END_K / GROOVE_END_THETA | 69 / 270° | P06 oluk bitişi (kök merkezi z = 4.003125) |
| GROOVE_CHUNK_TURNS | 8 | P06 süpürmenin parça boyu (Boolean sağlamlığı) |
| HW_PROFILE | (z, r) listesi | P07 el çarkı döndürme profili |
| CRANK_Y | Y0−0.631 = −0.58856 | P08 kol ekseni |
| H1_SHANK_L / H1_SHANK_R / H1_HEAD_R / H1_HEAD_H | 0.6871 / 0.082 / 0.187 / 0.1 | H1 vida |
| H1_POSES | spec §5 tablosu | H1-a…d konumları (O, U, W) |
