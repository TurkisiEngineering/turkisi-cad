# P44 spec verification (ball screw-spline shaft with two flanged nuts, 11 bodies)

Source: original STEP read with `olc_cekirdek.load_step`: 11 solids, **18 empty shells dropped**. Unit in the file: mm.
Spec unit: mm. Work scripts in `is/` (s01 metrics, s02 face dump, s03 sections, s04 interference, s05 hedef + kaynak,
s06 groove-end probe (stopped, too slow on the long B-spline face), s07 section / face data, s08 hidden lists,
s07_kontrol recipe check, s09 spec assembly, s11 olc timing probe).

## Target table against the original

Spec section 6 (per body V, A, CoM, bbox, face count) and the assembly totals are written from the original's GProp
and exact bounding boxes: ΔV = 0 %, ΔA = 0 %, ΔCoM = 0, Δbbox = 0 for all 11 bodies at the printed precision.
GProp vs mesh volume: largest difference 0.022 % (P10), so GProp values are the targets.

## Interference (capped boolean worker, bbox pre-filter)

22 candidate pairs, all booleans valid. One overlap > 8 mm³: **P02 / P05 40.389 mm³** (the four cap screw shanks that
are part of P05 sit in the plain holes of P02). In `hedef.json` and spec section 5.

## Geometry checks behind the spec text

- Shaft: R5 / R2, chamfers 0.25 x 45 deg, four spline grooves R1.24 with axes at radius 5.8 (60/120/240/300 deg).
- Ball groove: axial half-plane sections at 30 deg and 210 deg show circular arcs R0.7075 with centres at r 5.0075,
  15.000 apart and offset 7.5 between the two half-planes (lead 15); the cross-section at x = 0 has the groove bottom on
  +Y (θ = 0) and the 30 deg section has its centre at x = 1.25: x = 15·θ/360 + 15k, right-hand (matches product data).
  The groove face is one B-spline (6 x 653 poles) from x = -150 to 121.647.
- Nut / flange / ring half-sections at 45 deg (clear of holes), hole patterns from the face lists.

## Hidden lists

- `ozellikler.json`: 34 items (shaft diameters, length, spline groove count / radius / spacing, two ball-groove region
  items, nut diameters / bores, hole counts and circles, flange diameters / thicknesses, lubrication hole, ring sizes,
  seal thickness / diameter / lobes, region items for the end cap, the wiper seal and the tapped holes).
  `is/s07_kontrol.py`: BAD 0 (every numbered item reproduces its nom; all points inside faces, ≤ 0.009 mm).
- `resim_olculeri.json`: 17 rows = every printed dimension / note. Measured 300, 3, 3, 48, 48, 42, 3.4, 23, 34.5, 21,
  33, 4, 10, 3 (M3 major) — all equal the drawing. Not measurable by a recipe (`modelde_var: false`, explained in each
  row): **270 Thread Length** (groove full depth to about x = 120, run-out to 121.65), **Root Diameter 9.27** (model groove
  bottom 8.6: source conflict), **Travel per turn 15** (lead verified by sections, no lead recipe).
- `parametreler.json`: lead 15, shaft diameter 10, bore 4, length 300, flange diameter 48.

## Undetermined items

- Free-form faces: groove run-out near x = 121, helical lip of P06, blends of P03's lubrication hole, M3 thread flanks of
  P05 and P07 (hand and phase of the M3 threads undetermined).
- Materials only from the product data.

## Source conflicts

- Drawing "Root Diameter 9.27" vs model groove bottom diameter 8.6.
- The drawing places the ball-screw nut on the left; the model agrees (ball-screw nut set at x < 0).

## Tier

`cok_zor` confirmed: long helical ball groove (single free-form face), modelled M3 threads, merged screws, helical wiper lip.

## olc self-check result

`is/olc_kendi/olcum.json`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00;
851 s, 2026-11-12 18:49). The long helical groove face cost 323 s on P01 (timing probe `is/s11_olc_zaman.py`:
0.015 s per projection), well under the 1 h limit.
