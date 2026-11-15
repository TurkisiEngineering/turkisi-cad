# Parametreler — P01 Spanner

SolidCraft belgesinde (`P01_Spanner.sc`) kullanıcı parametresi olarak tanımlıdır (`parameters.add`).
Belge birimi inç; değerler inç / derece.

| Ad | İfade | Değer | Kullanıldığı özellik |
|---|---|---|---|
| T | `0.12 in` | 0.120000 | F1_Extrude, F3b_HandleExtrude (simetrik kalınlık, Y = ±T/2); F4 kesici eksenleri (Y = ±(T/2 − R_round)) |
| H_handle | `0.389790 in` | 0.389790 | F1_Outline alt kenar (Z = −H_handle), F3b_Handle, F4 alt kesiciler |
| R_end | `H_handle / 2` | 0.194895 | F1_Outline ve F3b_Handle yarım daire uç; F2_Slot merkez yüksekliği (Z = −R_end) |
| X_end | `1.970605 in` | 1.970605 | Uç yayı merkezi x (F1, F3b) |
| X_top0 | `-1.354007 in` | −1.354007 | F1_Outline üst kenar başlangıcı |
| X_neck | `-0.703984 in` | −0.703984 | F1_Outline alt kenar sonu / boyun yayı merkez x |
| R_neck | `15/32 * 1 in` | 0.468750 | F1_Outline içbükey boyun yayı |
| Xc_back | `-1.507307 in` | −1.507307 | F1_Outline baş sırt yayı merkezi (Z = 0) |
| R_back | `0.707013 in` | 0.707013 | F1_Outline baş sırt yayı (baş yüksekliği) |
| R_tip | `5/64 * 1 in` | 0.078125 | Kanca ucu yayı (bilgi parametresi; yay yarıçapı teğet noktalardan gelir, bkz. build_log) |
| Xc_jaw | `-1.696750 in` | −1.696750 | F1_Outline çene yayı merkezi (Z = 0) |
| R_jaw | `5/16 * 1 in` | 0.312500 | Çene yayı (Ø0.625 somun); uç noktalar bu çembere izdüşürülür |
| Slot_X1 | `1.918717 in` | 1.918717 | F2_Slot birinci yarım daire merkezi |
| Slot_C | `0.025985 in` | 0.025985 | F2_Slot merkezler arası |
| Slot_W | `0.129930 in` | 0.129930 | F2_Slot genişliği |
| R_round | `1/64 * 1 in` | 0.015625 | F3c_EdgeRounds (fillet), F4 koni başlangıç yarıçapı |
| X_round0 | `-0.441484 in` | −0.441484 | F3a_TrimHandle / F3b_Handle sınırı; tam yuvarlamanın bittiği x |
| A_runout | `10 deg` | 10° | F4 koni yarı açısı |
| L_runout | `(sqrt(2) - 1) * R_round / tan(A_runout)` | 0.036705 | F4 geçiş boyu (keskin köşeye x = −0.478189'da ulaşır) |
| Cut_big | `0.05 in` | 0.050000 | Yardımcı: F4 kesici profilinin parça dışında kalan radyal uzantısı |
| Cut_ext | `0.002 in` | 0.002000 | Yardımcı: F4 kesicinin keskin uçtan öteye uzantısı (malzeme kaldırmaz) |

Sabit (parametresiz) koordinatlar: kanca/pim köşeleri (−1.024250, −0.516259), (−2.159435, −0.273121),
(−2.087375, −0.242941) [uç yayı merkezi], (−2.104284, −0.166668), (−1.931443, −0.128350), (−1.864243, −0.193720),
(−1.922674, −0.215905), (−1.411824, −0.128350) — `gen_script.py` içinde spec'ten aynen; yay üzerindeki olanlar
o yayın çemberine izdüşürülür (build_log §2).
