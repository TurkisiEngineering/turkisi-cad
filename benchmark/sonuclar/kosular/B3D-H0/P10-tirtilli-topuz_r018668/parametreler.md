# Parametreler (knob.py başı; tüm uzunluklar inç, açılar derece)

| Ad | Değer | Özellik |
|---|---|---|
| N_LOBES | 8 | lob / oyuk / kaburga sayısı |
| SCALLOP_PCD_R | 1.39 | oyuk merkezlerinin çember yarıçapı |
| SCALLOP_ANG0 | 22.5 | ilk oyuk merkezi açısı (lob/kaburga θ=k·45°) |
| HUB_END_Z | -0.68 | göbek alt alın yüzü (insert alt ucu da burada) |
| HUB_END_R | 0.625 | göbek yarıçapı alt alında (Ø1.25) |
| HUB_END_ROUND | 0.02 | göbek alt kenar yuvarlatması (C1 adım 2) |
| HUB_DRAFT_DEG | 3 | göbek dış konisi ve konik delik eğimi (TAN3) |
| HEAD_UNDER_Z | -0.12 | kafa alt seviyesi / kaburga alt kenarı |
| CORE_RIM_R | 1.2 | çekirdek kafa çapı Ø2.4 (L0 çemberi) |
| CORE_RIM_TOP_Z | 0.44 | kafa üst düz halkası |
| DOME_START_R | 1.06 | kubbe başlangıç yarıçapı |
| CORE_DOME_R | 2.175763 | çekirdek kubbe yayı yarıçapı |
| DOME_CENTRE | (0.124593, -1.524424) | kubbe yay merkezi (r,z), çekirdek ve kaplama ortak |
| CORE_TOP_Z | 0.62 | çekirdek üst halka yüzü |
| CORE_DOME_END_R | 0.492553 | kubbenin üst halkaya indiği yarıçap |
| SCALLOP_R_CORE | 0.33 | çekirdek dış oyuk yarıçapı (C2, L0) |
| CI_R / SCALLOP_R_CI | 1.11 / 0.39 | Lci: kafa iç cidar çemberi / iç oyuk yarıçapı (C3, S4) |
| CAV_STEP_Z | 0.26 | alt boşluk basamak düzlemi; kaplama astar üstü |
| CAV_CEIL_Z | 0.35 | alt boşluk tavanı |
| CAV_STEP_R / CAV_CEIL_R | 1.01 / 0.92 | 45° tavan pahı alt/üst yarıçapı |
| RIB_T | 0.05 | radyal kaburga kalınlığı |
| SEAT_R | 0.265625 | insert yuvası Ø0.53125 (C4) |
| SEAT_TOP_Z | -0.18 | yuva tabanı / insert üst ucu |
| BORE_R0 | 0.36 | konik delik yarıçapı z=-0.18'de |
| BORE_ROUND | 0.015 | konik delik üst yuvarlatması |
| RIDGE_RI / RIDGE_RO / RIDGE_H | 0.385417 / 0.505208 / 0.015 | göbek alt alın bileziği (C5) |
| SKIN_T | 0.06 | kaplama kalınlığı (bilgi amaçlı; konturlarda gömülü) |
| LO_R / LO_SC_R | 1.26 / 0.27 | Lo: kaplama dış konturu |
| LI_R / LI_SC_R | 1.05 / 0.45 | Li: kaplama astar iç konturu |
| PLAN_ROUND | 0.1 | Lo ve Li plan köşe yuvarlatmaları |
| COAT_BOT_Z / COAT_FLAT_Z | -0.18 / 0.5 | kaplama B prizması alt/üst (S1) |
| COAT_EDGE_ROUND | 0.06 | S2 kenar yuvarlatmaları (3 halka) |
| COAT_DOME_R | 2.230085 | kaplama kubbe yarıçapı (S3) |
| COAT_TOP_Z | 0.68 | kaplama tepesi |
| COAT_DOME_END_R | 0.461925 | üst açıklık silindiri (Ø0.92385) |
| OPEN_R | 0.421954 | üst açıklık yarıçapı z≤0.62 |
| OPEN_CONE_TOP_Z | 0.674670 | üst açıklık konisinin üst ucu |
| INS_R | 0.265625 | insert dış yarıçapı |
| INS_Z0 / INS_Z1 | -0.68 / -0.18 | insert uçları (boy 0.5) |
| PITCH | 0.0625 | diş adımı (3/8"-16, sağ el) |
| MAJOR_R / MINOR_R | 0.1875 / 0.146906 | diş dip (major) / tepe (minor) yarıçapı |
| FLAT | 0.0078125 (P/8) | dip ve tepe eksenel düzlükleri |
| ROOT_FLAT_Z0 | -0.379218 | θ=0'da dip düzlüğü merkezi (faz) |
| CSK_R | 0.21875 | havşa yarıçapı alın yüzünde (90°) |
| THREAD_EMBED | 0.005 | modelleme bindirmesi: diş profili tüp duvarına bu kadar gömülür (geometriye etkisi yok) |
