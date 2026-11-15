# Parametreler (birim: inç, açı: derece) — kaynak `params.py`

| Ad | Değer | Özellik |
|---|---|---|
| N_LOBES | 8 | lob / oyuk / kaburga sayısı |
| SCALLOP_PCR | 1.39 | oyuk merkezlerinin dairesi (C2, L0/Lci/Lo/Li) |
| SCALLOP_THETA0 | 22.5 | ilk oyuk merkezinin açısı (adım 45°) |
| HUB_END_Z | -0.68 | göbek uç yüzü (C1), insert alt ucu |
| HUB_R_END | 0.625 | göbek yarıçapı z=-0.68'de (Ø1.25), 3° koni (C1 adım 3, C3 "hub") |
| TAN3 | tan 3° | göbek konisi ve konik delik eğimi |
| HUB_END_ROUND | 0.02 | göbek ucu R0.02 yuvarlatma (C1 adım 2; merkez koniye teğet hesaplanır → r 0.606021) |
| HEAD_UNDER_Z | -0.12 | baş alt düzlemi / jant alt yüzü (C1, C3 K1) |
| CORE_RIM_R | 1.20 | çekirdek jant yarıçapı (Ø2.4) |
| RIM_TOP_Z | 0.44 | jant üstü / üst düz halka |
| TOP_FLAT_R_IN | 1.06 | kubbenin başladığı yarıçap (C1, S3) |
| DOME_R | 2.175763 | çekirdek kubbe yarıçapı (C1 adım 7) |
| DOME_C | (0.124593, -1.524424) | kubbe merkezleri (çekirdek ve kaplama ortak) |
| CORE_TOP_Z | 0.62 | çekirdek üst düz halkası |
| DOME_END_R | 0.492553 | çekirdek kubbesinin bittiği yarıçap |
| SCALLOP_R_CORE | 0.33 | C2 oyuk silindirleri (L0) |
| LCI_R / LCI_SCALLOP_R | 1.11 / 0.39 | Lci (jant iç konturu, C3 K1/K2, S4) |
| CAV_STEP_Z / CAV_CEIL_Z | 0.26 / 0.35 | boşluk basamağı / tavanı (C3 K1-K2), astar üstü (S4) |
| CAV_CONE_R_LO / _HI | 1.01 / 0.92 | 45° tavan pahı (C3 K2) |
| RIB_T | 0.05 | 8 radyal kaburga kalınlığı (C3) |
| BORE_SEAT_R | 0.265625 | insert yuvası (Ø0.53125) (C4) |
| BORE_STEP_Z | -0.18 | yuva üst basamağı (C4), kaplama altı (S1) |
| BORE_R0 | 0.36 | konik deliğin z=-0.18'deki yarıçapı (3° koni) |
| BORE_TAN_PT | (0.401182, 0.605785) | konik delik → R0.015 teğet noktası |
| BORE_ROUND_C / BORE_TOP_ROUND | (0.416161, 0.605) / 0.015 | delik ağzı yuvarlatması |
| RIDGE_RI / RIDGE_RO / RIDGE_H | 0.385417 / 0.505208 / 0.015 | göbek ucu halka çıkıntısı (C5) |
| COAT_T | 0.06 | kaplama kalınlığı |
| LO_R / LO_SCALLOP_R | 1.26 / 0.27 | Lo kaplama dış konturu (S1) |
| LI_R / LI_SCALLOP_R | 1.05 / 0.45 | Li astar iç konturu (S1) |
| PLAN_CORNER_R | 0.10 | Lo ve Li'nin 16 köşe yuvarlatması |
| COAT_BOT_Z / COAT_FLAT_TOP_Z | -0.18 / 0.50 | kaplama B prizmasının alt / üst düzlemi (S1) |
| COAT_EDGE_R | 0.06 | S2 kenar yuvarlatmaları (3 halka) |
| COAT_DOME_R | 2.230085 | kaplama kubbesi (S3) |
| COAT_TOP_Z | 0.68 | kaplamanın tepesi |
| COAT_DOME_END_R | 0.461925 | üst açıklık silindiri / kubbe ucu (S4) |
| TOP_OPEN_R / TOP_OPEN_CONE_Z | 0.421954 / 0.674670 | üst açıklık (S4) |
| INS_R / INS_Z0 / INS_Z1 | 0.265625 / -0.68 / -0.18 | insert dış silindiri ve boyu (P03) |
| PITCH | 0.0625 | 3/8"-16 adım, sağ el |
| TH_MAJOR_R / TH_MINOR_R | 0.1875 / 0.146906 | diş dibi (major) / tepe (minor) yarıçapı |
| TH_FLAT | 0.0078125 (P/8) | dip ve tepe eksenel düzlükleri |
| TH_PHASE_Z | -0.379218 | θ=0'da dip düzlüğü merkezi (faz) |
| CSK_R / CSK_DEPTH | 0.21875 / 0.03125 | 90° havşalar, iki uç |

Betik içi yardımcı değerler (knob.py): `dr_out = 0.005` (diş sırtının manşon duvarına gömülen kısmı, sonuca etkisi
yok), `n_below = 7`, `height = 13·P` (helis insert boyundan uzun başlatılıp gövde ile kırpılır).
