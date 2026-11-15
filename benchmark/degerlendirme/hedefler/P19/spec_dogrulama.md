# P19 spec verification (swivel plate caster, 4 in wheel, total lock)

Original: `kaynak.json` (12 solids, one flat part, no assembly tree, identity frame, inch STEP; STEP order P09, P03, P02,
P04, P05, P01, P06, H1, P10-a, P10-b, P07, P08). No empty shells, no free shells. Scripts: `_gizli/is/` (s01 structure,
s02 face dumps in `b/`, kenar.py face edge loops, kesit.py sections with circle fits, s03 interference, r_fork /
r_pedal / r_kucuk text rebuilds, fkontrol.py per-face check, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this
table).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | -0.0000 | 0.0013 | 0.0000 |
| P02 | +0.0000 | -0.0000 | 0.0012 | 0.0001 |
| P03 | +0.0000 | -0.0000 | 0.0007 | 0.0000 |
| P04 | +0.0001 | -0.0001 | 0.0008 | 0.0000 |
| P05 | +0.0003 | +0.0003 | 0.0003 | 0.0000 |
| P06 | +0.0000 | +0.0001 | 0.0004 | 0.0008 |
| P07 | +0.0000 | -0.0000 | 0.0011 | 0.0000 |
| P08 | -0.0000 | +0.0000 | 0.0000 | 0.0013 |
| P09 | -0.0000 | +0.0000 | 0.0000 | 0.0013 |
| P10-a | -0.0000 | -0.0000 | 0.0007 | 0.0013 |
| P10-b | -0.0000 | -0.0000 | 0.0007 | 0.0013 |
| H1 | -0.0000 | +0.0000 | 0.0000 | 0.0000 |

Largest: |dV| 0.0003 % (4-decimal inch rounding of P05), dCoM 0.0013 mm, dbbox 0.0013 mm (4-decimal rounding of
x = 0.00125). Bodies 12 / 12. GProp volume vs fine-mesh integral: largest difference 0.033 % (P07), so all targets are
GProp values.

## Interference set of the original (capped boolean worker, bbox pre-filter, all 29 touching pairs)
- P09 x H1: 2895.83 mm3 (the solid core disc has no axle hole; pin volume inside |z| <= 0.3125). Listed in hedef.json.
- Every other pair: 0 (face contacts: plate / kingpin / washer / hex ring stack, wheel rings, axle in the fork bores).

## Independent rebuild checks from the spec text (build123d, rounds omitted where noted)
| body | check | result |
|---|---|---|
| P01 fork | profile + trims + ridge + gap + holes, no rounds (`r_fork.py`) | every non-round face of the original lies on the rebuild (per-face max 0.000 in); residuals only on the R0.06 / R0.04 / R0.125 rounds and their blends (max 0.028 in at the R0.125 leg-end round); volume +0.58 % = the omitted rounds |
| P06 pedal | stem + pad + ribs, no R0.04 rounds (`r_pedal.py`) | all non-round faces exact; residual only on the R0.04 rounds and blends (max 0.012 in); volume +0.06 % |
| P02 plate | full (`r_kucuk.py`) | dV +0.000 %, both directions per-face max 0.000 in |
| P03 kingpin | full incl. lug and R0.015 rounds | dV -0.004 %, per-face max 0.000 in |
| P04 / P05 | full | dV -0.006 % / -0.019 % |
| wheel parts, H1 | direct from exact sections (cylinders, tori, R0.2) | not rebuilt |

Lessons put into the spec: the pedal "grooves" are raised half-round ribs (arc through the top of the R0.025 circle);
the fork back is a Z-extrusion trimmed by a cylinder about the swivel axis, not a revolve.

## olc self-check (original vs itself)
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00).
First run 84.72: item F20 (bevel angle) had a 1.0 mm region that caught no samples on the narrow bevel face; region
radius raised to 2.5 mm (`is/olc_kendi_1/` kept).

## Hidden lists
- ozellikler.json: 71 items over all 12 bodies + assembly; all reproduce nom on the original (s07_kontrol.py). Seven
  items are region-only (`olcum: null`): leg-end R0.125 round, kingpin lug, tread R0.2 edge round (B-spline in the
  original), both dished flange faces.
- resim_olculeri.json: 9 rows, all modelled and reproduced: 4 wheel dia, 5.5 mounting height (assembly bbox), 3.625,
  2.5, 1.25, 1.75, 2.938 (model 2.9375, measured between end-arc axes of two slots), 0.438 (slot length = end-arc axis
  distance 0.125 + `ekle_mm` slot width 0.3125), 5/16 screw (slot width 0.3125). Tolerance 0.005 in (catalogue reference
  drawing, as in P7 / P8 / P9).
- parametreler.json: wheel diameter 4.0, wheel width 1.25, plate length 3.625, plate width 2.5, swivel offset 1.515.

## Undetermined (written as such in the spec)
Ball bearings, brake / swivel-lock mechanism, kingpin rivet head, fasteners (none modelled); exact shape of the small
blend patches where two rounds meet on P01 / P06 (radii given).

## Source conflicts (K)
Product data "mounting plate length 3 11/16" vs drawing and 3D 3.625: spec follows the 3D. Product data says ball
bearings and a total-lock mechanism; the 3D has neither.

## Tier
Index: "hard" (molded and freeform). Found: 12 bodies, mostly analytic 2.5D profiles; free-form only in small blends and
the tread edge rounds; no threads or gears. "hard" confirmed.
