# Parametreler (birim inç; `_deg` derece, `N_` adet)

Kaynak: betiklerdeki `P` sözlükleri; her parçada Equation Manager'a global değişken olarak da yazılır (bilgi amaçlı; geometriyi Python betiği sürer).

## P01 (`betikler/build_core.py`)

| Ad | Değer | Özellik |
|---|---|---|
| Z_hub_end | -0.68 | C1 göbek alt yüzü / C4, C5 |
| R_hub_end | 0.625 | C1 göbek konisi (z=-0.68) |
| hub_draft_deg | 3 | C1 göbek konisi, C3c göbek uzatma |
| R_hub_end_round | 0.02 | C1 göbek alt köşe R |
| Z_underside | -0.12 | C1 kafa alt seviyesi, C3a/C3d başlangıç düzlemi |
| R_head | 1.2 | C1 kafa kenarı (dia 2.4) |
| Z_rim_top | 0.44 | C1 düz üst halka |
| R_top_flat_in | 1.06 | C1 kubbe başlangıcı |
| R_dome | 2.17576 | C1 kubbe yayı |
| Dome_cx | 0.124593 | C1/S3 kubbe merkezi r |
| Dome_cz | -1.52442 | C1/S3 kubbe merkezi z |
| R_top_face_out | 0.492553 | C1 üst düz halka dış r |
| Z_top | 0.62 | C1 çekirdek üstü |
| R_scallop_pcd | 1.39 | C2/C3/S1/S4 oyuk merkez dairesi |
| R_scallop | 0.33 | C2 oyuk R (L0) |
| N_lobes | 8 | lob/oyuk/kaburga sayısı |
| R_rim_in | 1.11 | C3a/S4a Lci daire |
| R_scallop_in | 0.39 | C3a/S4a Lci oyuk R |
| Z_step | 0.26 | C3b basamak z |
| Z_ceiling | 0.35 | C3 tavan z / S4a |
| R_step | 1.01 | C3b koni alt r |
| R_ceiling | 0.92 | C3b koni üst r |
| T_rib | 0.05 | C3d kaburga kalınlığı |
| R_seat | 0.265625 | C4 insert yuvası r |
| Z_seat_top | -0.18 | C4 yuva üstü |
| R_bore_bot | 0.36 | C4 konik delik alt r |
| bore_taper_deg | 3 | C4 delik koniği |
| R_bore_round | 0.015 | C4 üst kenar R |
| R_ridge_in | 0.385417 | C5 halka iç r |
| R_ridge_out | 0.505208 | C5 halka dış r |
| H_ridge | 0.015 | C5 halka yüksekliği |

## P02 (`betikler/build_coating.py`)

| Ad | Değer | Özellik |
|---|---|---|
| T_coat | 0.06 | kaplama kalınlığı (bilgi) |
| Z_coat_bot | -0.18 | S1 alt düzlem |
| Z_coat_flat_top | 0.5 | S1 üst düz / S3 taban |
| Z_liner_top | 0.26 | S1 iç cep üstü, S4a başlangıç |
| Z_ceiling | 0.35 | C3 tavan z / S4a |
| R_outer | 1.26 | S1 Lo daire |
| R_scallop_out | 0.27 | S1 Lo oyuk R |
| R_liner | 1.05 | S1 Li daire |
| R_scallop_liner | 0.45 | S1 Li oyuk R |
| R_plan_round | 0.1 | S1 Lo/Li köşe R0.1 |
| R_rim_in | 1.11 | C3a/S4a Lci daire |
| R_scallop_in | 0.39 | C3a/S4a Lci oyuk R |
| R_scallop_pcd | 1.39 | C2/C3/S1/S4 oyuk merkez dairesi |
| R_edge_round | 0.06 | S2 kenar yuvarlatma R0.06 |
| R_dome_out | 2.23008 | S3 kubbe yayı |
| Dome_cx | 0.124593 | C1/S3 kubbe merkezi r |
| Dome_cz | -1.52442 | C1/S3 kubbe merkezi z |
| R_cap_start | 1.06 | S3 kubbe başlangıç r |
| Z_coat_top | 0.68 | S3 kaplama tepe |
| R_open_low | 0.421954 | S4b açıklık r (z<=0.62) |
| Z_open_low | 0.62 | S4b koni alt z |
| R_open_top | 0.461925 | S4b üst silindir r |
| Z_open_cone_top | 0.67467 | S4b koni üst z |

## P03 (`betikler/build_insert.py`)

| Ad | Değer | Özellik |
|---|---|---|
| R_insert_out | 0.265625 | T1 insert dış r |
| Z_insert_bot | -0.68 | T1 insert alt |
| Z_insert_top | -0.18 | T1 insert üst |
| Pitch | 0.0625 | T2 helis adımı |
| R_major | 0.1875 | T2 helis r / T3 diş dibi |
| R_minor | 0.146906 | T1 iç delik / T3 diş tepesi |
| Flat | 0.0078125 | T3 düzlükler P/8 |
| Flank_run | 0.0234375 | T3 yan eksenel uzunluk |
| Z_root_phase | -0.379218 | T2 faz (θ=0 kök merkezi) |
| N_turns | 9 | T2 helis tur sayısı |
| R_csk | 0.21875 | T4 havşa ağız r |
| Csk_depth | 0.03125 | T4 havşa derinliği (bilgi) |
| csk_angle_deg | 90 | T4 havşa açısı (bilgi) |
