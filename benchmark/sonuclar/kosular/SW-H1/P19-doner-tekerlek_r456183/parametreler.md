# parametreler.md

Birim: inç. Tüm parametreler `scripts/parts.py` içindeki `PARAMS` sözlüğündedir; betikler bunları kullanarak geometriyi üretir.
Ayrıca aynı adlarla `Caster_Assembly.SLDASM` içine global değişken (Equations) olarak yazılmıştır (belgeleme amaçlı; parça özellik boyutlarına bağlı değil, değişiklik betikten yapılır).

| Ad | Değer (in) | Değer (mm) | Hangi özellik |
|---|---|---|---|
| `mount_height` | 5.50000 | 139.7000 | kontrol (plaka üstü 2.75 − tekerlek altı −2.75) |
| `plate_top_y` | 2.75000 | 69.8500 | P02 üst yüz, P03 üst |
| `swivel_offset` | 1.51500 | 38.4810 | tekerlek ekseni x (P07–P10, H1, P01 aks deliği) |
| `axle_y` | -0.75000 | -19.0500 | tekerlek ekseni y, ref. düzlem Plane_axle_y |
| `wheel_od` | 4.00000 | 101.6000 | P07 Rev_tread (dış çap) |
| `wheel_width` | 1.25000 | 31.7500 | P07/P08 genişlik |
| `tread_bore_r` | 1.56375 | 39.7192 | P07 iç yarıçap |
| `tread_edge_round` | 0.20000 | 5.0800 | P07 kenar R0.2 (kesitte) |
| `insert_ri` | 1.51375 | 38.4492 | P08 iç yarıçap |
| `insert_ro` | 1.56375 | 39.7192 | P08 dış yarıçap |
| `core_r` | 1.51375 | 38.4492 | P09 Ext_core, P10 jant yarıçapı |
| `core_half_width` | 0.31250 | 7.9375 | P09 yarı genişlik, P10 iç yüz z |
| `flange_hub_r` | 0.30500 | 7.7470 | P10 göbek deliği |
| `flange_dish_R` | 3.75269 | 95.3183 | P10 çanak torus yarıçapı |
| `flange_dish_cz` | 2.92770 | 74.3636 | P10 çanak merkezi z |
| `flange_round` | 0.02000 | 0.5080 | P10 R0.02 yuvarlatmalar |
| `axle_d` | 0.60000 | 15.2400 | H1 Ext_axle çap |
| `axle_half_len` | 1.03400 | 26.2636 | H1 yarı boy (Ext_axle mid-plane) |
| `fork_half_width` | 1.02900 | 26.1366 | P01 Ext_OUTER (|z|<=1.029) |
| `fork_inner_half_gap` | 0.83000 | 21.0820 | P01 Cut_GAP_front (|z|<0.83) |
| `ridge_half_width` | 1.13300 | 28.7782 | P01 Ext_RIDGE (|z|<=1.133) |
| `crown_R` | 1.02900 | 26.1366 | P01 Cut_trim_crown |
| `ridge_R` | 1.13300 | 28.7782 | P01 Cut_trim_ridge |
| `gap_R` | 0.83000 | 21.0820 | P01 Cut_GAP_back (revolve) |
| `deck_top_y` | 2.46400 | 62.5856 | P01 üst yüz / sınıflandırma |
| `ceiling_y` | 2.18400 | 55.4736 | P01 tavan (gap) |
| `kingpin_hole_d` | 1.00000 | 25.4000 | P01 Cut_kingpin_hole |
| `axle_bore_d` | 0.60000 | 15.2400 | P01 Cut_axle_bore |
| `top_arc_R` | 8.62200 | 218.9988 | P01/P06 R8.622 üst yay (bilgi; profilde nokta olarak) |
| `ceiling_arc_R` | 8.34200 | 211.8868 | P01 R8.342 tavan yayı (bilgi) |
| `gap_end_x` | 2.46150 | 62.5221 | P01 gap sonu, P06 arka yüz |
| `leg_end_x` | 3.68850 | 93.6879 | P01 bacak ucu, P06 ön yüz/ayak arka yüz |
| `fork_round` | 0.06000 | 1.5240 | P01 Fillet_outer_R0_06* |
| `leg_end_round` | 0.12500 | 3.1750 | P01 Fillet_leg_end_R0_125 |
| `ridge_round` | 0.04000 | 1.0160 | P01 Fillet_ridge_R0_04 |
| `plate_len` | 3.62500 | 92.0750 | P02 Ext_plate X |
| `plate_wid` | 2.50000 | 63.5000 | P02 Ext_plate Z |
| `plate_t` | 0.10000 | 2.5400 | P02 kalınlık (Ext_plate) |
| `plate_corner_R` | 0.25000 | 6.3500 | P02 köşe R0.25 |
| `slot_w` | 0.31250 | 7.9375 | P02 slot genişliği |
| `slot_pitch_x` | 2.93750 | 74.6125 | P02 slot aralığı X |
| `slot_pitch_z` | 1.75000 | 44.4500 | P02 slot aralığı Z |
| `slot_arc_dx` | 0.12500 | 3.1750 | P02 slot yay merkezleri arası |
| `kp_shank_d` | 0.58570 | 14.8768 | P03 alt gövde çapı (kesit) |
| `kp_collar_d` | 0.75100 | 19.0754 | P03 yaka çapı (kesit) |
| `kp_upper_d` | 0.59300 | 15.0622 | P03 üst gövde çapı (kesit) |
| `kp_bottom_y` | 1.75700 | 44.6278 | P03 alt (kesit) |
| `lug_top_y` | 2.60000 | 66.0400 | P03 Ext_lug üst |
| `lug_R` | 0.06300 | 1.6002 | P03 Sk_lug boss R |
| `washer_od` | 1.74400 | 44.2976 | P04 Rev_washer dış çap |
| `washer_t` | 0.07500 | 1.9050 | P04 kalınlık (kesit) |
| `hex_af` | 1.51000 | 38.3540 | P05 Sk_hex anahtar ağzı |
| `hex_t` | 0.07500 | 1.9050 | P05 Ext_hex |
| `pedal_stem_half_w` | 0.82500 | 20.9550 | P06 Ext_pedal_stem |
| `pedal_foot_half_w` | 1.05000 | 26.6700 | P06 Ext_foot_side |
| `pedal_front_x` | 4.29850 | 109.1819 | P06 ön yüz |
| `pedal_round` | 0.04000 | 1.0160 | P06 Fillet_foot_R0_04 |
| `rib_R` | 0.02500 | 0.6350 | P06 Ext_ribs_* |

Profil köşe noktaları (spec §4'teki koordinatlar) betiklerde `Path(...)` zincirleri olarak, spec'teki sırayla ve aynı sayılarla yazılıdır (`parts.py`, `parts_b.py`, `parts_fork.py`).
