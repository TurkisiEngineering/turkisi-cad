# P33 spec verification (cable-operated rotary latch kit with T-handle, 20 bodies)

Original: original STEP (not published) (one
product, 20 solids). Loaded with `olc_cekirdek.load_step`: **20 solids, 0 empty shells dropped**, 0 free shells.
Work scripts: `_gizli\is\` (s01 structure, s02 face dumps, s04 wire dumps, g_* sections / rays / renders, s03
interference, s05 targets, s06 hidden lists, s07 recipe self-check, s08 back-check, r_* spec-text rebuilds, yap.py).

## Units decision

The STEP declares **INCH** (`CONVERSION_BASED_UNIT('INCH')`, the lead's 3 MB header scan missed it: the unit entity is
at line 45148). The geometry, however, is round in **millimetres** (pull axis y 12, z -60.4; plate 45 x 56; pivots
(0.243, 39.8) / (-22.257, 43.3); bolt axis (-37.857, 75.7); latch plates y 1.01 / 2.6 / 4.4 / 8.4 / 12.9 / 14.9 ...),
with some inch-derived features (cable 6.35, bend R38.1, ferrules 7.112 / 5.588, wires 2.032 / 3.81). **Spec unit:
mm.** JSON in mm.

## s08 back-check: spec target table vs original (per body)

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | +0.0000 | 0.0000 | 0.0000 |
| P02 | +0.0000 | -0.0000 | 0.0001 | 0.0000 |
| P03 | +0.0000 | +0.0001 | 0.0000 | 0.0000 |
| P04 | +0.0001 | -0.0000 | 0.0001 | 0.0000 |
| P05 | -0.0003 | +0.0004 | 0.0000 | 0.0000 |
| P06-a | +0.0023 | +0.0000 | 0.0000 | 0.0000 |
| P06-b | +0.0023 | +0.0000 | 0.0000 | 0.0000 |
| P07 | +0.0001 | +0.0004 | 0.0000 | 0.0000 |
| P08 | -0.0000 | +0.0000 | 0.0000 | 0.0000 |
| P09 | +0.0000 | +0.0001 | 0.0000 | 0.0000 |
| P10 | -0.0000 | +0.0001 | 0.0001 | 0.0000 |
| P11 | -0.0001 | +0.0003 | 0.0001 | 0.0000 |
| P12 | +0.0003 | -0.0001 | 0.0000 | 0.0000 |
| P13-a | +0.0004 | -0.0004 | 0.0000 | 0.0000 |
| P13-b | +0.0004 | -0.0004 | 0.0000 | 0.0000 |
| P14 | +0.0005 | -0.0009 | 0.0000 | 0.0000 |
| P15 | +0.0005 | +0.0005 | 0.0001 | 0.0000 |
| P16 | -0.0004 | -0.0008 | 0.0000 | 0.0000 |
| H1 | -0.0001 | +0.0002 | 0.0001 | 0.0000 |
| H2 | +0.0153 | +0.0040 | 0.0001 | 0.0000 |

20 / 20 bodies in the table (largest residual = rounding of the printed values). `paket_denetle.py P33`: body count
20 = STEP 20, assembly bbox delta 0.0, 60 features, 22 drawing rows, 5 parameters.

## GProp vs mesh volume

All 20 bodies within 0.06 % (largest H2 0.053 %, P16 0.038 %, P03 0.037 %). **GProp volumes are the targets.**

## Spec-text rebuilds (r_*.py, build123d, from the spec numbers) vs original

| body | rebuild | dV % | dA % | dCoM | dbbox | sampled surface deviation |
|---|---|---|---|---|---|---|
| P08 cable | r_basit | +0.0000 | +0.0000 | 0.0000 | 0.0000 | - |
| P06-a / P06-b | r_basit | 0.0000 | 0.0000 | 0.0000 | 0.0000 | - |
| P05 / P07 | r_basit | 0.0000 | -0.0002 / 0.0000 | 0 | 0 | - |
| P13-a / P13-b, P14, H2 | r_basit | 0.0000 | 0.0000 | 0 | 0 | - |
| P01 housing | r_p01 | -0.0003 | -0.0001 | 0.0000 | 0.0000 | - |
| P03 pull rod (drafts not modelled) | r_p03 | +0.128 | +0.182 | 0.027 | 0.017 | max 0.074 (the 1 deg / 0.5 deg drafts) |
| P04 anchor block (0.5 deg drafts, end lift not modelled) | r_p04 | +0.153 | +0.099 | 0.030 | 0.021 | - |
| P11 rotor, P12 lever, P15, P16 | r_mandal | 0.0000 | 0.0000 | 0 | 0 | - |
| P10 cover plate | r_mandal | -0.0000 | -0.0000 | 0 | 0 | max 0.025 |
| P09 base plate | r_mandal | -0.058 | +0.018 | 0.009 | 0 | max 0.038 |
| H1 bolt WITHOUT the thread groove | r_civata | +3.59 | -6.35 | 0.52 | 0 | groove volume 102 mm3 = 9.2 mm3/mm x 11 mm, consistent with the stated profile |
| P02 T-handle, APPROXIMATE (no rounds, straight recess prisms of the x = 69 outline, floors = +X face - 3.54) | r_tutamak | +2.32 | +6.29 | 0.11 | 0 | rounds R1.9 to R3 and the panels explain about -3 % |

All analytic bodies are reproduced from the spec text to within 0.2 % volume and 0.03 mm CoM; H1 to the thread groove;
P02 only approximately (free-form blends).

## Interference set (original, capped BoolWorker 3 GB / 120 s, bbox pre-filter; 39 candidate pairs, peak 0.26 GB)

| pair | common mm3 | note |
|---|---|---|
| **P03 / P02** | **228.604** | pull rod inside the T-handle shank (no hole modelled) -> `girisimler` |
| H1 / H2 | 7.137 | ring eccentric under the flange, cuts the thread crest (< 8, not listed) |
| P07 / P10 | 4.684 | fitting shoulder into the cover joggle (< 8) |
| P13-a / P09, P13-b / P09 | 2.827 each | spacer bottom collar 0.1 into the recess floor (< 8) |
| P09 / P12 | 0.784 | (< 8) |
| P04 / P05, P05 / P03, P12 / P16, P15 / P16 | 0.053, 0.022, 0.023, 0.003 | (< 8) |

## Hidden lists

- `ozellikler.json`: 60 items on 18 of the 20 bodies + MONTAJ (P01 11, P02 9, P03 6, P04 5, P05 2, P06-a 1, P06-b 1,
  P08 3, P09 5, P10 3, P11 2, P12 1, P13-a 1, P13-b 1, P15 1, P16 2, H1 4, H2 1, MONTAJ 1; P07 and P14 are covered by
  the per-body targets only); 50 numeric, 10 region-only (T-handle recesses, crown, voids, top surface; housing
  V-notch; rod grooves; anchor tab and windows; L-pin bend; bolt thread).
  `sayi` used only for analytic cylinders (4 mounting holes, 4 R6 plate corners).
- `resim_olculeri.json`: all 22 printed items of the catalogue drawing (20 measured, 2 `modelde_var: false`: 3 ft cable
  length (no path-length recipe; model 914.40 = 36.000 in) and the max cumulative bend 720 deg note). Spec
  writer's readings to confirm: **0.28 in** read as the lever-pivot spacer bore (7.2 = 0.2835 in, the two extension
  lines straddle that hole); **0.89 in** and **0.61 in** read as X-distances (pivot to pivot 22.5; strike bolt axis to
  rotor pivot 15.6); **1.00 in** read as flange dome (at the shank) to head top (25.40); **0.76 in** = latch depth
  19.30 (L-pin bottom to cover tab top); 0.86 in = T-handle thickness 22.0 (0.866, truncated -> tol 0.01).
- `parametreler.json`: pull axis height 12, cable diameter 6.35, bend radius 38.1, pivot spacing 22.5, T-handle length
  60.
- s07 recipe self-check on the original: **BAD 0** (60 items, 22 rows).

## Undetermined items

T-handle free-form blends (R0.3 to R3, median radii given), exact recess floor / wall surfaces and the two flattened
panels on its +X face; free-form upper -Z quarter of the pull rod clevis end; thread run-out under the bolt flange;
springs and cable internals (not in the source).

## Source conflicts

Catalogue / product data inch values agree with the 3D within the drawing's rounding (2 decimals, some truncated); the
product data "mounting hole 9/32 in at 7/8 in" of the latch has no matching feature (the latch has no separate
mounting holes; the pivot holes are 9.1 at 22.77). Follow the 3D everywhere.

## Tier

"cok_zor / very-hard" **confirmed**: 20 bodies, a 591-face free-form molded T-handle with internal voids, a modelled
M8 helical thread, drafted molded parts, a 914 mm swept cable and two sheet metal parts with bends.

## olc self-check result

`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00; 269 s, 2026-11-12). Interference set reproduced (original 1 pair, P02 / P03).
