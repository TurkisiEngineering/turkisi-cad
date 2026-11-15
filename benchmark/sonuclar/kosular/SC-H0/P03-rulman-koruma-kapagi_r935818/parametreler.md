# Parametreler: P01 Guard

Belge birimi: **inç** (`document.units in`). Tüm parametreler SolidCraft belgesinde (`P01_Guard.sc`) `parameters.add`
ile tanımlı isimli kullanıcı parametreleridir. Profil noktaları, uzunluklar ve yarıçaplar bu parametrelerden türetilen
ifadelerdir (ör. uç duvar alt köşesi `(d_end - sin(draft)*y_bot)/cos(draft)`). İç boşluk aynı ifadelerle,
`wall` kadar içe kaydırılmış olarak kurulur (`d_end-wall`, `R_crown-wall`, `R_side-wall` …).

| Ad | Değer | Kullanıldığı özellik(ler) |
|---|---|---|
| wall | 0.125 in | iç gövde: tüm düzlem sabitleri ve yarıçaplar `-wall`, iç yuvarlatmalar `R_side-wall`, `R_hump-wall`, `R_conc+wall`; boss girintileri |
| draft | 4 deg | uç duvar, yan duvar, tümsek bacağı ve tümsek uç yüzü profilleri (`sin(draft)`, `cos(draft)`) |
| y_bot | -1.53125 in | flanş altı / montaj yüzü: dış profillerin alt kenarı, `flange_outline` taslak düzlemi ofseti |
| fl_t | 0.125 in | `flange_extrude` kalınlığı |
| cy | -0.09375 in | tepe yayı ve tümsek kemer ekseni y (x=0); `d_slope`, `d_leg` |
| R_crown | 1.9375 in | `o_tent_profile` tepe yayı (iç: `R_crown-wall` = 1.8125); üst boss konumu |
| R_arch | 1.3125 in | `o_hump_profile` kemer yayı (iç: 1.1875) |
| n_sx | 0.721392 | eğim düzlemi normali x; eğim bossu ekseni |
| n_sy | 0.692527 | eğim düzlemi normali y; eğim bossu ekseni |
| d_end | 2.902310 in | uç duvar düzlemi `0.997564|x|+0.069756y=d_end` (iç: `d_end-wall`) |
| d_side | 0.860129 in | yan duvar düzlemi, `*_tent_sidewalls` kırpma taslağı (iç: `d_side-wall`) |
| d_hend | 1.608303 in | tümsek uç yüzü düzlemi, `*_hump_endfaces` kırpma taslağı (iç: `d_hend-wall`) |
| d_slope | `n_sy*cy + R_crown` = 1.872576 in | eğim düzlemi (tepe yayına teğet olacak şekilde türetilmiş) |
| d_leg | `sin(draft)*cy + R_arch` = 1.305960 in | tümsek bacak düzlemi (kemere teğet olacak şekilde türetilmiş) |
| R_side | 0.375 in | `o_tent_side_round_z±1` (iç `i_tent_side_round_*`: R_side-wall = 0.25) |
| R_hump | 0.375 in | `o_hump_end_round_z±1` (iç: 0.25) |
| R_conc | 0.125 in | `o_hump_tent_concave_z±1` (iç `i_hump_tent_concave_*`: R_conc+wall = 0.25) |
| y_cav | `y_bot - 0.12` | iç boşluk gövdesinin flanşın altına uzatılan alt kenarı (açık taban için) |
| boss_d | 0.8125 in | `boss_top`, `boss_slope_px/nx` silindir çapı |
| boss_h | 0.0875 in | boss üst yüzü: `boss_*_trim` kesim tabanı; girinti dibi (`recess_*` yüksekliği) |
| boss_r | 0.1 in | `boss_top_base_round`, `boss_slope_base_round_x±1` — yalnız `BOSS_ROUND=1 bash gen.sh 4` ile üretilir; çekirdek bu yuvarlatmayı kuramadığı için teslim modelinde YOK (bkz. build_log.md) |
| rec_d | 0.5625 in | `recess_top`, `recess_slope_px/nx` çapı |
| R_open | 0.1 in | `opening_round` (alt ağız kenarı) |
| Px | 1.369085 in | eğim bossu ekseninin dış eğim düzlemini deldiği nokta x |
| Py | `(d_slope - n_sx*Px)/n_sy` = 1.277826 in | aynı noktanın y'si (eğim düzlemi üzerinde) |

Flanş dış hattı (spec 3.6'daki 16 parça) sayısal köşe/merkez koordinatlarıyla `gen.sh` içindedir (parametre değil;
spec'teki değerlerin aynısı). Yay ara noktaları merkez + R·açıortay ile hesaplanır.

Yuvarlatma kenarlarının seçim noktaları (mm), aynı spec değerlerinden `gen.sh` içinde hesaplanan sayılardır;
parametre değiştirilirse seçimler SolidCraft'ın kendi kenar takibine kalır.
