# P40 spec verification (hysteresis clutch for torque limiting on a through shaft)

Source: original STEP (not published) (read only).
Loaded with `olc_cekirdek.load_step`: 20 solids, 0 empty / 0 empty-shell / 0 free-shell dropped. Spec unit inch
(Ø3.23, Ø3.31, 2.52, Ø0.375, Ø2.375 bolt circle are round in inch; threads metric M5 × 0.8). Frame = STEP frame, Z = axis.
Scripts: `_gizli\is\` (s01 structure, s02 face dumps → `b\`, s03 interference, s04 sections, s05 hedef, s06 hidden lists,
s07 recipe self-check, s08 table back-check, r_govde rebuild from spec text).

## 1. Target table back-check (s08: spec.md section 6 vs original)

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | +0.0000 | 0.0012 | 0.0000 |
| P02 | +0.0000 | -0.0000 | 0.0011 | 0.0000 |
| P03 | -0.0000 | -0.0000 | 0.0010 | 0.0000 |
| P04 | -0.0000 | +0.0000 | 0.0013 | 0.0000 |
| P05 | -0.0000 | -0.0000 | 0.0013 | 0.0000 |
| P06 | -0.0000 | +0.0000 | 0.0013 | 0.0000 |
| P07 | -0.0000 | -0.0000 | 0.0014 | 0.0000 |
| P08 | -0.0000 | -0.0000 | 0.0005 | 0.0000 |
| P09 | -0.0000 | -0.0000 | 0.0015 | 0.0000 |
| H1-a / H1-b | -0.0003 | +0.0002 | 0.0009 | 0.0013 |
| H2 | +0.0004 | +0.0005 | 0.0002 | 0.0007 |
| H3-a…d | -0.0052 | +0.0061 | 0.0012 | 0.0013 |
| H4-a / H4-b | -0.0006 | +0.0010 | 0.0004 | 0.0013 |
| H5-a / H5-b | -0.0045 | +0.0010 | 0.0012 | 0.0006 |

All 20 bodies parsed. Maximum: dV 0.0052 % (rounding of a 29 mm³ head), dCoM 0.0015 mm, dbbox 0.0013 mm (4-decimal
inch rounding).

## 2. Rebuild from the spec text (r_govde.py, build123d, original frame)

| body | dV % | dA % | dCoM mm | dbbox max mm | note |
|---|---|---|---|---|---|
| P01 | +0.0000 | -0.0001 | 0.0000 | 0.0000 | |
| P04 | -0.0000 | +0.0001 | 0.0000 | 0.0000 | counterbores + 18 slits |
| P05 | +0.0000 | +0.0000 | 0.0000 | 0.0000 | |
| P06 | +0.0000 | +0.0000 | 0.0000 | 0.0000 | |
| P07 | +0.0160 | +0.1085 | 0.0028 | 0.0000 | hole-mouth flare (freeform) not rebuilt |
| P08 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | |
| P09 | -0.0077 | +0.0074 | 0.0002 | 0.0000 | 150-groove knurl, flat, V mark, spot faces: confirms the groove form |
| H1-a | +0.0133 | +0.0091 | 0.0020 | 0.0013 | outline from 4-decimal arc data |
| H2 | +0.0237 | +0.0116 | 0.0009 | 0.0007 | |
| H3-a | +0.0313 | -0.0088 | 0.0002 | 0.0000 | |
| P02 | +0.4876 | -3.2483 | 0.0085 | 0.0000 | threads NOT rebuilt (plain Ø0.156 holes): this is the thread's share |
| P03 | +0.3374 | -3.1511 | 0.0117 | 0.0000 | same |

H4, H5 not rebuilt (small heads / threaded set screws; shapes taken directly from sections, s04). Thread form and phase
were read from sections through the hole axes (s04): pitch 0.031496, major Ø0.19685, minor Ø0.1560, 0.0039 flats, 60°,
right hand (checked on P02 hole 0, P03 hole 0, H5-a); the P02 hole at 120° was checked to be a rotated copy of hole 0
(same outer-side root positions).

## 3. Interference (s03, capped BoolWorker after bbox pre-filter)

All tested pairs: common volume 0.0. Pairs P07 / H5-a and P07 / H5-b timed out (120 s, helical thread against the plain
hole); analytically the set-screw crests (Ø0.19685) equal the hole wall (Ø0.19685), so they only touch: overlap 0.
`girisimler` = [] (no pair > 8 mm³).

## 4. GProp vs mesh volume

Largest difference 0.059 % (H4 button heads); all bodies < 0.5 %, so the GProp values are the targets.

## 5. Hidden lists

- `ozellikler.json`: 60 items (counts, diameters, depths, slit count 9+9 with `ayri_yuzler`, knurl / flat / threads as
  `bolgesel_sapma` boxes because the threads are B-spline and the knurl face count depends on the kernel).
- `resim_olculeri.json`: 8 rows = every printed dimension: 0.375, 2.375 (twice, both ends), 3.31, 3.23, 2.52, M5 × 0.8
  (twice; thread callouts, `modelde_var` true, `olcum` null, covered by the thread region items).
- `parametreler.json`: bore 0.375, body OD 3.23, overall length 2.52, bolt circle 2.375, knurl groove count 150.
- s07 self-check (`tarifler.olc` on the original): **BAD 0** (54 measured items + 6 rows within tol; 6 region-only items).
- `paket_denetle.py P40`: govde_hedef 20 = govde_step 20, hacim fark 0.0 %, montaj bbox fark 0.0 mm.

## 6. Source conflicts with the drawing

None. 3.31 = knurl crest Ø (2 × 1.655), 3.23 = P01/P02 OD, 2.52 = Z extent, 0.375 = bore, 2.375 = hole bolt circle on
both ends. Note: the left drawing view is the knurled (top) end, the right view the bottom cap with the 4 screw heads.

## 7. Undetermined

- Which rings are magnets, pole count, magnetisation (not modelled).
- Screw shanks under H3 / H4 (heads only in the source).
- Thread run-out shape at the helix ends (helix simply cut at the hole bottom / screw ends; phase given).
- Exact shape of the small freeform flare at the P07 radial hole mouths.
- Materials and finishes.

## 8. Tier

Index: couplings / torque limiters, very-hard, ~20 bodies. Confirmed: 20 solids, 8 thread helices (6 tapped holes + 2 set
screws), a 150-groove knurl (661-face body), slotted drum (171 faces). Very-hard is justified by the knurl and modelled
threads more than by the (mostly revolved) bodies.

## olc self-check result

`olc.py` original vs itself (2026-11-12, `_gizli\is\olc_kendi\`): **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00, drawing 5.00). 20 / 20 bodies matched, IoU 1.000000 each; interference original 0 / rebuild 0, 2 pairs undetermined (hub vs set screw, boolean timed out on both sides; thread OD = hole diameter, contact only); run time 1730 s.
