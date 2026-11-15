# Parametreler

Birim: inch (açılar derece). Kaynak: `betikler/params.py` (tek yer); betikler bu adları kullanarak SolidWorks özelliklerini kurar.
SolidWorks özellik ağacındaki adlar aşağıdaki 'Özellik' sütunundakilerle aynıdır.

| Parça | Ad | Değer | Özellik (SolidWorks ağacı) | Açıklama |
|---|---|---|---|---|
| P01 | `R_EDGE` | 0.1 | `P01_PerimeterRound_R0.1` | perimeter round radius |
| P01 | `W_HALF` | 0.925 | `P01_SK_outlineS` | outline S half width X |
| P01 | `L_HALF` | 1.2 | `P01_SK_outlineS` | outline S half length Y |
| P01 | `R_CORNER` | 0.1 | `P01_SK_outlineS / _drafted` | vertical corner radius (constant) |
| P01 | `DRAFT_OUT` | 3.0 | `P01_SK_outlineS_drafted` | outer wall draft deg (offset 0.35*tan3) |
| P01 | `CAV_HX` | 0.845 | `P01_SK_cavityC` | cavity half width at open side |
| P01 | `CAV_HY` | 1.12 | `P01_SK_cavityC` | cavity half length at open side |
| P01 | `CAV_CHAMF` | 1.87062 | `P01_SK_cavityC` | corner chamfer line abs(x)+abs(y) |
| P01 | `CAV_DEPTH` | 0.39 | `P01_Cavity_1deg` | cavity depth |
| P01 | `DRAFT_IN` | 1.0 | `P01_Cavity_1deg` | cavity draft deg |
| P01 | `R_CAV_FILLET` | 0.03 | `P01_FloorFillet_R0.03` | floor/ceiling fillet |
| P01 | `RECESS_DEPTH` | 0.035 | `P01_CornerRecess_x4` | corner recess depth |
| P01 | `RECESS_R` | 0.02 | `P01_SK_cornerRecess` | corner recess arc radius |
| P01 | `LIP_H` | 0.03 | `P01_Lip_3deg` | lip height |
| P01 | `LIP_IN` | 0.865 x 1.140 half | `P01_SK_lip` | lip inner boundary (sharp) |
| P01 | `LIP_OUT` | 0.915 x 1.190 half, R0.09 | `P01_SK_lip` | lip outer boundary |
| P01 | `TONGUE_R` | 0.005 | `P01_TongueRound_R0.005` | tongue top-edge round |
| P01 | `TONGUE_H` | 0.03 | `P01_SK_tongue / P01_Tongue_10deg` | tongue height |
| P01 | `TONGUE_HALF_W` | 0.01925 | `P01_SK_tongue / P01_Tongue_10deg` | tongue half width at base |
| P01 | `TONGUE_DRAFT` | 10.0 | `P01_SK_tongue / P01_Tongue_10deg` | flank draft deg |
| P01 | `TONGUE_X_C` | 0.88582 | `P01_SK_tongue / P01_Tongue_10deg` | X-side centreline |
| P01 | `TONGUE_Y_C` | 1.16082 | `P01_SK_tongue / P01_Tongue_10deg` | Y-side centreline |
| P01 | `TONGUE_X_END` | 1.07085 | `P01_SK_tongue / P01_Tongue_10deg` | X-side round end centre |y| |
| P01 | `TONGUE_Y_END` | 0.79585 | `P01_SK_tongue / P01_Tongue_10deg` | Y-side round end centre |x| |
| P01 | `TONGUE_GAP` | 0.156 | `P01_SK_tongueGap` | flat ends of X-side segments |y| |
| P01 | `BOSS_R` | 0.0925 | `P01_SK_boss` | boss radius at top |
| P01 | `BOSS_TOP_BASE` | 0.03 | `P01_Boss_1deg` | boss top z |
| P01 | `RIB_HALF_T` | 0.015 | `P01_SK_ribUpper` | rib half thickness at z=0 |
| P01 | `RIB_STEP_X` | 0.123 | `P01_SK_ribUpper` | rib step face |
| P01 | `RIB_END_X` | 0.15221 | `P01_SK_ribLower` | rib end face at z=-0.035 |
| P01 | `RIB_LOW_Z` | -0.035 | `P01_SK_ribLower` | rib lower top z |
| P01 | `HOLE_CB_R` | 0.085 | `P01_SK_screwHole` | counterbore radius |
| P01 | `HOLE_CB_Z` | -0.429 | `P01_SK_screwHole` | counterbore top z |
| P01 | `HOLE_CS_Z` | -0.38586 | `P01_SK_screwHole` | countersink end z (82 deg) |
| P01 | `HOLE_R` | 0.0475 | `P01_SK_screwHole` | through hole radius |
| P01 | `LABEL_OUT` | 0.775 x 1.055 half | `P01_SK_label` | label groove outer |
| P01 | `LABEL_IN` | 0.755 x 1.035 half | `P01_SK_label` | label groove inner |
| P01 | `LABEL_DEPTH` | 0.01 | `P01_LabelRecess` | label groove depth |
| P02 | `R_EDGE` | 0.1 | `P02_PerimeterRound_R0.1` | perimeter round radius |
| P02 | `W_HALF` | 0.925 | `P02_SK_outlineS` | outline S half width X |
| P02 | `L_HALF` | 1.2 | `P02_SK_outlineS` | outline S half length Y |
| P02 | `R_CORNER` | 0.1 | `P02_SK_outlineS / _drafted` | vertical corner radius (constant) |
| P02 | `DRAFT_OUT` | 3.0 | `P02_SK_outlineS_drafted` | outer wall draft deg (offset 0.35*tan3) |
| P02 | `CAV_HX` | 0.845 | `P02_SK_cavityC` | cavity half width at open side |
| P02 | `CAV_HY` | 1.12 | `P02_SK_cavityC` | cavity half length at open side |
| P02 | `CAV_CHAMF` | 1.87062 | `P02_SK_cavityC` | corner chamfer line abs(x)+abs(y) |
| P02 | `CAV_DEPTH` | 0.39 | `P02_Cavity_1deg` | cavity depth |
| P02 | `DRAFT_IN` | 1.0 | `P02_Cavity_1deg` | cavity draft deg |
| P02 | `R_CAV_FILLET` | 0.03 | `P02_FloorFillet_R0.03` | floor/ceiling fillet |
| P02 | `GROOVE_IN` | 0.8650 x 1.1400 half, R0.0500 | `P02_SK_groove` | groove inner boundary at mouth |
| P02 | `GROOVE_OUT` | 0.9035 x 1.1785 half, R0.0885 | `P02_SK_groove` | groove outer boundary at mouth |
| P02 | `GROOVE_DEPTH` | 0.035 | `P02_Groove_10deg` | groove depth |
| P02 | `GROOVE_DRAFT` | 10.0 | `P02_Groove_10deg` | groove wall draft deg |
| P02 | `KEY_HALF` | 0.146 | `P02_SK_key` | key half length |y| at the mouth |
| P02 | `KEY_DRAFT` | 3.0 | `P02_Key_3deg` | key end-face draft deg |
| P02 | `BOSS_R` | 0.0925 | `P02_SK_boss` | boss radius at z=0.035 |
| P02 | `LID_BOSS_Z` | 0.035 | `P02_SK_boss` | boss / rib bottom z |
| P02 | `LID_RIB_END` | 0.153 | `P02_SK_ribs` | rib end |x| at z=0.035 |
| P02 | `RIB_HALF_T` | 0.015 | `P02_SK_ribs` | rib half thickness at z=0.035 |
| P02 | `LID_HOLE_R` | 0.035 | `P02_SK_hole` | lid hole radius (plain) |
| P02 | `LABEL_OUT` | 0.775 x 1.055 half | `P02_SK_label` | label groove outer |
| P02 | `LABEL_IN` | 0.755 x 1.035 half | `P02_SK_label` | label groove inner |
| P02 | `LABEL_DEPTH` | 0.01 | `P02_LabelRecess` | label groove depth |
| H1 | `SCR_HEAD_R` | 0.081 | `H1_SK_profile` | head radius |
| H1 | `SCR_Z_HEAD` | -0.45 | `H1_SK_profile` | head face z |
| H1 | `SCR_Z_CONE` | -0.4 | `H1_SK_profile` | end of 84 deg head cone |
| H1 | `SCR_R` | 0.036 | `H1_SK_profile` | shank radius |
| H1 | `SCR_Z_END` | 0.05 | `H1_SK_profile` | shank end z |
| H1 | `SCR_RECESS_D` | 0.03 | `H1_CrossRecess_4deg` | cross recess depth |
| H1 | `SCR_RECESS_DRAFT` | 4.0 | `H1_CrossRecess_4deg` | recess wall draft deg |
| H1 | `SCR_ARM_REACH` | 0.053 | `H1_SK_crossRecess` | arm reach at mouth |
| H1 | `SCR_ARM_HALF` | 0.0085 | `H1_SK_crossRecess` | arm half width at mouth |
| H1 | `SCR_FILL` | 0.0235 | `H1_SK_crossRecess` | 45 deg fill-flat vertex |

Türetilmiş değerler (betikte hesaplanır):

- `T3 = tan(3°)`, `T1 = tan(1°)`, `T10 = tan(10°)`
- Dış duvar loft alt profili: yarı genişlik `W_HALF - 0.35*T3`, yarı boy `L_HALF - 0.35*T3`, köşe `R_CORNER` (sabit)
- Kenar yuvarlatma merkezleri `EDGE_C_HX = 0.80652`, `EDGE_C_HY = 1.08152` (slab yarı ölçüleri = merkez + `R_EDGE`)
- Alt nervür yarı kalınlığı (z=-0.035): `RIB_HALF_T + 0.035*T1`
- Dil üst kenar noktası: `TONGUE_HALF_W - TONGUE_H*T10`
