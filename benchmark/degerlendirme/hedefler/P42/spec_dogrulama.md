# P42 spec verification (beam trolley, 80 bodies, inch)

Source: `kaynak.json` (STEP, inch). `olc_cekirdek.load_step`: 80 solids, 0 empty shells dropped.
Work scripts: `_gizli\is\` (s01 structure, s02 face dumps, kenarlar/yarim exact sections, yon.py instance orientations,
s03 interference, s05 targets + names, s05b placements, s06 hidden lists, s07 recipe check, s08 back-check).

## Target table back-check (s08: spec §6 vs original)

80 / 80 bodies parsed. Max |ΔV| 0.0004 %, max |ΔA| 0.0003 %, max ΔCoM 0.0018 mm, max Δbbox 0.0003 mm. paket_denetle: body
count 80 = STEP, assembly bbox Δ 0.

## GProp vs mesh volume

All bodies within 0.057 % (threaded bolts / axles largest). GProp volumes are the targets.

## Interference (capped boolean worker, bbox pre-filter)

172 touching pairs tested, all common volumes 0. `girisimler` = [].

## Spec checks

- Every profile in the spec (long angle, bumper angle, wheel, shield, end stops) is taken from exact B-rep section edges; arc
  centres re-checked against three points per arc (two end-stop centres corrected during the check).
- Long-angle and bumper-angle profile area 1.6741 in² = the reference end-face area.
- Thread pitch measured on H1, H5, H6 sections: 0.0769 in (13 TPI), root radius 0.200, crest 0.250.
- Instance orientations measured per body (yon.py): all nut / bolt-head / axle hex flats have one pair normal to X; all lock
  washer gaps as listed in spec §5 (from the gap faces and the CoM offset of each washer).

## Hidden lists

- `ozellikler.json`: 53 items; s07 on the original **BAD 0**.
- `resim_olculeri.json`: 9 rows. 7 measurable rows reproduce exactly (36.00, 3.00, 4.00 wheel, 4.00 angle, 47.75, 7.00,
  12.00). "9.48 in Max" and "3.36 in Max" are adjustable-width limits; the model is built at a wider setting (long angles
  6.000 apart), so they are `modelde_var: false`, not measured.
- `parametreler.json`: wheel Ø4.0, axle spacing 36.0, angle thickness 0.25, angle length 47.0, 13 TPI.

## Undetermined items

- Thread start angles (phase) on H1, H5, H6.

## Tier

Matrix tier `cok_zor`. Body count is high (80) but there are only 11 distinct parts, all prismatic or turned, plus modelled
1/2-13 threads on 16 bodies. The model looks closer to `zor` than to `cok_zor`; the lead may want to re-tier it.

## olc self-check result

`olc.py` original vs itself (2026-11-12, 5407 s incl. low-memory waits): **85.00 / 85** (geometry 40, completeness 10,
assembly 10, features 20, drawing 5); all 80 bodies IoU 1.000000, interference 0 / 0.
