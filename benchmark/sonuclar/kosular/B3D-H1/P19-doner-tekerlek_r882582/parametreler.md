# Parametreler (caster.py başı; birim inç)

| Ad | Değer | Özellik |
|---|---|---|
| PLATE_TOP_Y | 2.75 | Plaka üst (montaj) yüzü |
| WHEEL_X, WHEEL_Y | 1.515, -0.75 | Tekerlek ekseni (Z'ye paralel), döner eksenden kaçıklık 1.515 |
| WHEEL_R / TREAD_RO | 2.0 | Tekerlek yarıçapı (Ø4.0), taban y = -2.75 |
| FORK_HALF_W | 1.029 | P01 dış yan yüzler z=±1.029, arka taç yarıçapı |
| RIDGE_HALF_W | 1.133 | P01 nervür üst yüzü z=±1.133, taç halka yarıçapı |
| GAP_HALF_W | 0.83 | P01 bacak iç yüzleri / arka iç yarım silindir R0.83 |
| DECK_TOP_Y | 2.464 | P01 düz üst yüz (P04 oturma yüzü) |
| DECK_CEIL_Y | 2.184 | P01 U tavanı (tabla kalınlığı 0.28) |
| GAP_END_X | 2.4615 | P01 boşluk uç duvarı = P06 arka yüzü |
| LEG_END_X | 3.6885 | P01 bacak ucu = P06 ayak plakası arka yüzü |
| TOP_ARC_C, TOP_ARC_R | (0.13847,-6.14324), 8.622 | P01 eğimli tabla üstü / P06 sap üstü (aynı daire) |
| CEIL_ARC_R | 8.342 | P01 tavan yayı (eş merkezli) |
| FRONT_ARC_C, FRONT_ARC_R | (-1.46454,-1.09977), 2.5 | P01 bacak ön içbükey kenarı |
| KINGPIN_HOLE_R | 0.5 | P01 pim deliği Ø1.0 |
| AXLE_BORE_R | 0.3 | P01 aks deliği Ø0.6 |
| FORK_ROUND_R | 0.06 | P01 F10 dış yüz / üst yüz yuvarlatmaları |
| FORK_LEGEND_ROUND_R | 0.125 | P01 bacak ucu düşey kenarları (uygulanamadı, R0.06 kaldı – build_log) |
| RIDGE_ROUND_R | 0.04 | P01 nervür üst kenar yuvarlatmaları |
| PLATE_HALF_L, PLATE_HALF_W | 1.8125, 1.25 | P02 plaka 3.625 × 2.5 |
| PLATE_T | 0.1 | P02 kalınlık (y 2.65–2.75) |
| PLATE_CORNER_R | 0.25 | P02 köşe yuvarlatma |
| SLOT_W | 0.3125 | P02 kızak genişliği |
| SLOT_X_IN, SLOT_X_OUT, SLOT_Z | 1.40625, 1.53125, 0.875 | P02 kızak uç-yay merkezleri (merkezler 2.9375 × 1.75) |
| PRESS_R | 0.75 | P02 preslenmiş merkez dönel bölge yarıçapı |
| LUG_TOP_Y | 2.6 | P03 dönme önleyici tırnak üstü |
| LUG_BOSS_R, LUG_FILLET_R | 0.063, 0.0394 | P03 tırnak plan yayları |
| WASHER_R_OUT, WASHER_Y0, WASHER_Y1 | 0.872, 2.464, 2.539 | P04 rondela |
| HEX_AF, HEX_Y0, HEX_Y1 | 1.51, 2.539, 2.614 | P05 altıgen halka (köşeler X üzerinde) |
| STEM_HALF_W | 0.825 | P06 sap genişliği (bacaklara 0.005 boşluk) |
| FOOT_HALF_W | 1.05 | P06 ayak plakası genişliği |
| FOOT_X0, FOOT_X1 | 3.6885, 4.2985 | P06 ayak plakası X aralığı |
| FOOT_ROUND_R | 0.04 | P06 ayak plakası kenar yuvarlatmaları |
| FOOT_MID_Y | 1.5195 | P06 ayak plakası yan profil simetri yüksekliği |
| RIB_R | 0.025 | P06 kaydırmaz nervürleri |
| STEM_RIB_HALF_L, FOOT_RIB_HALF_L | 0.675, 0.875 | P06 nervür yarı boyları |
| STEM_RIBS, FOOT_RIBS | 3+3 eksen konumu | P06 nervür eksenleri |
| TREAD_RI, TREAD_RO, TREAD_HALF_W, TREAD_ROUND_R | 1.56375, 2.0, 0.625, 0.2 | P07 lastik |
| INSERT_RI | 1.51375 | P08 ara halka iç yarıçapı (dış = TREAD_RI) |
| CORE_R, CORE_HALF_W | 1.51375, 0.3125 | P09 göbek diski |
| FL_HUB_R | 0.305 | P10 göbek deliği Ø0.61 |
| FL_RIM_Z | 0.6106 | P10 jant silindiri ucu |
| FL_DISH_R, FL_DISH_CZ | 3.75269, 2.9277 | P10 çanak yüzey (torus) |
| FL_ROUND_R, FL_HUB_ROUND_Z | 0.02, 0.8049 | P10 R0.02 yuvarlatmalar |
| PIN_R, PIN_HALF_L | 0.3, 1.034 | H1 aks pimi Ø0.6 × 2.068 |
