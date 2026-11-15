# P41 spec verification (electric clutch-brake, 27 bodies, inch)

Source: `kaynak.json` (STEP AP214, inch). `olc_cekirdek.load_step`: 27 solids, **22 empty shells dropped**.
Work scripts: `_gizli\is\` (s01 structure, s02 face dumps, kenarlar/dilim/yarim = exact section outlines, s03 interference,
s05 targets, s06 hidden lists, s07 recipe check, s08 back-check, r_kesit outline-area check).

## Target table back-check (s08: spec §6 vs original)

All 27 bodies parsed. Largest deltas: ΔV −0.0126 % (P15 tips, rounding of the 5-decimal in³ column; the mm³ column is
exact), ΔA ≤ 0.0052 %, ΔCoM ≤ 0.0018 mm, Δbbox ≤ 0.0013 mm. Assembly V 2 203 953.58 mm³, bbox Δ 0 (paket_denetle).

## GProp vs mesh volume

All bodies within 0.05 % (largest: wires P13/P14 0.050 %, set screws 0.041 %, housing 0.0002 %). GProp volumes are the targets.

## Interference (capped boolean worker, bbox pre-filter)

No pair above 8 mm³. Largest: H1-d with P01 0.32 mm³; all other touching pairs 0. `girisimler` = [].

## Spec checks

- Housing master outline B (§4.1.1) mirrored in X and closed: area minus the four Ø0.250 holes = 29.29606 in², reference
  slab area at z = 0.5 = 29.29621 in² (Δ −0.0005 %).
- Rear outline R (§4.1.2) at z = 2.3: Δ 0.2915 in², fully explained by the wire-entry hole and boss of §4.1.4 that cross
  this section (0.609 × 0.500 hole − 0.013 boss lip = 0.2915 in²).
- Every outline in the spec is generated from the reference B-rep section edges (exact line / arc data, 4 decimals in inch).
- Mirror symmetry in X of the housing sections checked by sampling at 13 z levels (max deviation ≤ 0.02 in from the sampling of
  straight edges only; no real asymmetry beyond the small R0.03 root rounds listed in spec §7).
- Not rebuilt solid-by-solid: the housing's many R0.01–R0.10 rounds and the H2 helical thread are described by rule only.

## Hidden lists

- `ozellikler.json`: 60 items (27 bodies). s07 on the original: **BAD 0** (every numbered item reproduces its nom; region
  points lie inside faces, distances to the face ≤ 0.0013 mm).
- `resim_olculeri.json`: 7 rows from the catalogue drawing (6.750, 6.741, 2.061, 5/8, keyway 0.188 × 0.188 read on the key,
  36 in lead wire `modelde_var: false`). All 6 measurable rows reproduce exactly.
- `parametreler.json`: housing OD 6.75, shaft Ø0.625, key width 0.188, fin thickness 0.150, coil turns 4.

## Undetermined items

- H2 internal thread exact profile and the hole bottom (~z −0.59 … −0.61): only 20 TPI, major Ø0.250 and length given.
- Small R0.03 fin-root rounds that the reference has on one side only; the single R0.08-floored rear recess.
- Drawing "36 in lead wire length" has no counterpart (the model's wires are a short run plus a 4-turn coil).

## Tier

`cok_zor` confirmed: 27 bodies, 1591-face finned housing with ~45 z-zones, helical coils, a modelled helical thread.

## olc self-check result

`olc.py` original vs itself (2026-11-12, 675 s): **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20,
drawing 5); all 27 bodies IoU 1.000000, interference 0 / 0.
