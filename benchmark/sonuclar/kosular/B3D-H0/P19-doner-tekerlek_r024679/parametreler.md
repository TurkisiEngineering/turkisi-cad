# Parametreler (`caster.py` başı, birim: inç)

| Ad | Değer | Özellik |
|---|---|---|
| PLATE_TOP_Y | 2.75 | Üst plaka montaj yüzü (global y) |
| WHEEL_AX_X | 1.515 | Tekerlek ekseni x (dönme ofseti / trail) |
| WHEEL_AX_Y | -0.75 | Tekerlek ekseni y |
| FORK_HALF_W | 1.029 | P01 dış yüzler z = ±; F1 simetrik ekstrüzyon |
| FORK_CROWN_R | 1.029 | P01 x<0 tarafında taç yuvarlağı (Y ekseni silindiri) |
| RIDGE_HALF_W | 1.133 | P01 F2 sırt bandı üst yüzleri z = ± |
| RIDGE_CROWN_R | 1.133 | P01 F2 taç halka bandı yarıçapı |
| GAP_HALF_W | 0.83 | P01 F3 bacak iç yüzleri z = ± |
| GAP_CROWN_R | 0.83 | P01 F3 arkadaki yarım silindir boşluk |
| FORK_TOP_Y | 2.464 | P01 düz üst yüz |
| CEILING_Y | 2.184 | P01 U içindeki tavan |
| DECK_R_OUT | 8.622 | P01 tabla üstü / P06 sap üstü yayı |
| DECK_R_IN | 8.342 | P01 tavan yayı (eş merkezli) |
| DECK_C | (0.13847, -6.14324) | R8.622 / R8.342 merkezi |
| GAP_END_X | 2.4615 | P01 boşluk uç duvarı = P06 arka yüzü |
| LEG_END_X | 3.6885 | P01 bacak ucu = P06 sap ön yüzü = ayak plakası arkası |
| FRONT_R, FRONT_C | 2.5, (-1.46454, -1.09977) | P01 bacakların tekerleğe bakan içbükey ön kenarı |
| KINGPIN_HOLE_R | 0.5 | P01 F4 pim deliği (Ø1.0) |
| AXLE_BORE_R | 0.3 | P01 F5 aks deliği (Ø0.6) |
| FORK_ROUND_R | 0.06 | P01 F10 dış yüz, üst yüz ve taç kenar yuvarlatmaları |
| LEG_END_ROUND_R | 0.125 | P01 F10 bacak ucu düşey kenarları |
| RIDGE_ROUND_R | 0.04 | P01 F10 sırt üst kenarları |
| PLATE_L × PLATE_W × PLATE_T | 3.625 × 2.5 × 0.1 | P02 T1 düz plaka |
| PLATE_CORNER_R | 0.25 | P02 köşe yuvarlatmaları |
| SLOT_W | 0.3125 | P02 T2 oval delik genişliği |
| SLOT_ARC_X | (1.40625, 1.53125) | P02 oval delik uç yayı merkezlerinin x değeri (±) |
| SLOT_Z | 0.875 | P02 oval delik merkezlerinin z değeri (±) |
| PRESS_R | 0.75 | P02 T3 preslenmiş merkezin yarıçapı (bu yarıçap içi döndürülmüş kesitle değiştirilir) |
| LUG_BOT_Y / LUG_TOP_Y | 2.502 / 2.6 | P03 K2 dönme önleyici çıkıntının alt / üst seviyesi |
| LUG_BOSS_R | 0.063 | P03 çıkıntı göbeği, merkez (-0.2965, 0) |
| LUG_FILLET_R | 0.0394 | P03 çıkıntı içbükey geçişleri |
| WASHER_R | 0.872 | P04 dış yarıçap |
| WASHER_Y | (2.464, 2.539) | P04 alt / üst |
| HEX_AF | 1.51 | P05 altıgenin anahtar ağzı (karşılıklı yüzler arası) |
| HEX_Y | (2.539, 2.614) | P05 alt / üst |
| STEM_HALF_W | 0.825 | P06 B1 sap genişliği ± |
| FOOT_HALF_W | 1.05 | P06 B2 ayak plakası genişliği ± |
| FOOT_X | (3.6885, 4.2985) | P06 ayak plakasının x aralığı |
| PEDAL_ROUND_R | 0.04 | P06 B2 kenar yuvarlatmaları |
| RIB_R | 0.025 | P06 B3 kaymaz nervürler |
| STEM_RIBS / STEM_RIB_HALF_L | 3 eksen, 0.675 | P06 sap üstündeki nervürler |
| FOOT_RIBS / FOOT_RIB_HALF_L | 3 eksen, 0.875 | P06 ayak plakası üstündeki nervürler |
| TREAD_RO / TREAD_RI | 2.0 / 1.56375 | P07 dış / iç yarıçap |
| TREAD_HALF_W | 0.625 | P07 ve P08 genişliği ± |
| TREAD_ROUND_R | 0.2 | P07 dış kenar yuvarlatmaları |
| INSERT_RI | 1.51375 | P08 iç yarıçap |
| CORE_R / CORE_HALF_W | 1.51375 / 0.3125 | P09 dolu disk; P10 jant yarıçapı ve iç yüzü |
| FLANGE_HUB_R | 0.305 | P10 göbek deliği (Ø0.61) |
| FLANGE_RIM_Z | 0.6106 | P10 jant silindirinin bittiği |z| |
| FLANGE_DISH_R / FLANGE_DISH_CZ | 3.75269 / 2.9277 | P10 çanak torus kesit yayı (merkez rho 0.305) |
| FLANGE_ROUND_R | 0.02 | P10 jant ve göbek yuvarlatmaları |
| FLANGE_HUB_ROUND_Z | 0.8049 | P10 göbek yuvarlatma merkezinin |z| değeri |
| AXLE_R / AXLE_HALF_L | 0.3 / 1.034 | H1 aks pimi |

Spec'teki profil köşe koordinatları (çatal P_out ve R_xy kesitleri, pedal profilleri, plaka ve pim yarım kesitleri)
`make_*` fonksiyonlarında spec'teki sırasıyla, doğrudan sayı olarak yer alır. Her biri spec'in ilgili satırına
karşılık gelir.
