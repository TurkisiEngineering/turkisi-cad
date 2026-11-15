# Parametreler — P01 Crank handle

Birim: mm. Kaynak: `build_crank.py` içindeki `PARAM` sözlüğü (betik bu değerlerle modeli kurar). Aynı değerler `P01 Crank handle.SLDPRT` içinde Equation Manager'a global değişken olarak da yazılır.

| Ad | Değer | Özellik / spec adımı |
|---|---|---|
| `hub_d` | 28.0 | A1 step 1-2, hub cylinder diameter |
| `hub_len` | 28.0 | A1 step 11, hub top face X |
| `hub_cyl_end_x` | 18.153 | A1 step 2, end of hub cylinder |
| `bore_d` | 10.0 | C, through bore diameter |
| `csk_d` | 13.4641 | C, countersink diameter at X=0 (120 deg incl.) |
| `csk_depth` | 1.0 | C, countersink depth |
| `neck_fillet_r` | 2.5 | A1 step 3 |
| `neck_in_r` ⓘ | 18.0 | A1 step 4 |
| `neck_rev_r` | 30.0 | A1 step 5 |
| `arm_in_x` | 48.0 | A1 step 6, arm inner face X |
| `arm_out_x` | 52.68507 | A1 step 7-8, arm outer face X |
| `arm_radial_constr` | 112.0 | A1 step 6-7, construction radius (trimmed by A2) |
| `neck_out_r` ⓘ | 37.5 | A1 step 9 |
| `neck_out_r2` ⓘ | 10.5 | A1 step 10 |
| `collar_r` | 15.5 | A2 hub collar radius |
| `crank_r` | 100.0 | hub axis -> grip axis |
| `boss_plan_r` | 8.0 | A2 grip boss circle radius |
| `arm_half_w0` ⓘ | 8.25150 | A2 strip half width at y=0 |
| `arm_taper` ⓘ | 0.0150150 | A2 strip half width slope dz/dy |
| `blend_hub_r` ⓘ | 22.5 | A2 blend arc at hub |
| `blend_grip_r` ⓘ | 13.5 | A2 blend arc at grip boss |
| `grip_boss_d` | 16.0 | B step 1-2 |
| `grip_boss_end_x` | 60.5 | B step 2 |
| `grip_boss_edge_r` | 0.5 | B step 3 |
| `grip_neck_d` | 13.0 | B step 5 |
| `grip_neck_x0` | 61.0 | B step 4 |
| `grip_neck_x1` | 67.0 | B step 6 |
| `grip_collar_d` | 18.0 | B step 7 |
| `grip_concave_r` ⓘ | 17.1 | B step 8 |
| `grip_barrel_r` ⓘ | 40.502 | B step 9 (barrel max dia 20 at x=103.95) |
| `grip_end_r` | 4.1 | B step 10 spherical end radius |
| `grip_end_x` | 128.0 | B step 10 overall X length |

ⓘ = bilgi amaçlı (yay merkezleri/teğet noktaları spec koordinatlarından alındığı için bu yarıçap betikte geometriyi doğrudan sürmüyor; değiştirilirse ilgili merkez/teğet noktaları da yeniden hesaplanmalı). Diğer tüm parametreler geometriyi doğrudan sürer.

Özellik adları (FeatureManager): `SK_A1` → `A1_HubArmRevolve`, `SK_A2` → `A2_PlanTrim`, `SK_B` → `B_GripRevolve`, `SK_C` → `C_Bore`.

Not: spec'te yalnız koordinat olarak verilen teğet/geçiş noktaları (ör. A1 (20.63435, 16.19512), (30.8125, 30.27582), (32.53906, 22.64391); A2 teğet noktaları ve blend merkezleri; B (72.96886, 9), (89.40919, 7.29981), (125.58325, 3.73854), merkezler (82.729, 23.041), (103.95, -30.502)) betikte sabit olarak, spec'teki değerleriyle aynen kullanıldı; bunlar türetilmiş noktalar olduğundan ayrı parametre yapılmadı.
