# P26 spec verification (panel-mount needle valve, elbow body, five-lobe knob)

Original: `kaynak.json` (7 solids, inch STEP, identity frame; STEP order P04 stem, H2 set screw, P01 body, H1 panel nut,
P05 knob, P03 gland nut, P02 sleeve). No empty shells (olc_cekirdek.load_step drops 0). Scripts: `_gizli/is/`
(s01 structure, s02 face dumps in `b/`, kesit.py exact sections, s03 interference, s04c thread flats, s10 knurl
planes, s11 exact surface parameters, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table,
r_noktalar.py spec-formula point check).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.0004 | 0.0009 |
| P02 | +0.0000 | -0.0002 | 0.0009 | 0.0013 |
| P03 | -0.0003 | +0.0004 | 0.0004 | 0.0013 |
| P04 | +0.0001 | -0.0001 | 0.0000 | 0.0000 |
| P05 | +0.0000 | -0.0001 | 0.0013 | 0.0012 |
| H1 | +0.0002 | +0.0002 | 0.0016 | 0.0007 |
| H2 | +0.0000 | -0.0058 | 0.0013 | 0.0011 |

Largest: |dV| 0.0003 %, |dA| 0.0058 % (set screw, 4-decimal in2 rounding), dCoM 0.0016 mm, dbbox 0.0013 mm (4-decimal
inch rounding; exact extremes are printed in the spec). Bodies 7 / 7. GProp vs fine-mesh volume: largest 0.074 %
(sleeve): GProp values used.

## Interference set of the original (capped boolean worker, 12 touching pairs)
One pair overlaps: **stem P04 / body P01 = 107.727 mm3** (the stem runs from y -0.21 up through solid body material
between y -0.1775 and -0.0425; the body has a closed void exactly at the stem's lowest 0.0325). This is a source
condition, written into the spec (sections 2, 4 B10, 5) and into `hedef.json` `girisimler`. All other pairs 0 (the
mating threads T3 and T4 share their surfaces exactly; the stem fits its bores with zero clearance).

## Independent check of the spec text
`r_noktalar.py`: 143 points built from the spec formulas (knob top cone, ceiling, lobe and scallop walls, all
chamfers and lips, every knurl ridge and groove bottom and a flank midpoint in two scallops, knurl end face, 7 core
holes, body sphere / hexagon chamfers / port cones / void, thread flats T1 to T4 at theta 0 and 90 deg, panel nut
countersink and rounds, set screw countersink). **All 143 lie on the original surfaces (max 0.000000 in).**

Thread data were read from exact half-plane sections (`s04c_flat.py`): constant flat widths, phase advance exactly p/4
per 90 deg (right-hand) for all four threads; T1 / T2 cones half-angle 1.7833 deg. The knurl flank planes were
intersected exactly (`s10_tirtil.py`): ridge pitch 16.5330 deg, ridge r' 0.3125, groove bottom r' 0.3425.

## olc self-check (original vs itself)
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00 = 72 / 72,
drawing 5.00 = 4 / 4; 682 s, peak 0.76 GB). The body P01 IoU used the thin-shell estimate (OCC self-boolean not valid
on that body); this does not change the score.

## Hidden lists
- ozellikler.json: 72 items (body 28, sleeve 6, gland nut 7, stem 2, knob 20, panel nut 4, set screw 4, assembly 1);
  every numbered item reproduces nom on the original (s07_kontrol.py, BAD 0); 16 are region-only (threads as boxes,
  chamfers, void, cavity ceiling).
- resim_olculeri.json: 5 rows. 3.04 (assembly Y 3.0400), 1.31 (body X 1.3105), 0.94 (side port face to bottom port
  axis 0.9390) at tol 0.005; "Panel cutout 0.562" mapped to the sleeve thread outer diameter 0.5625 at tol 0.0005
  (the original passes at exactly 0.0005: a rebuild must hit the 0.5625 crest radius; lead may widen to 0.001 if
  wanted). "2X 1/4 NPT" is `modelde_var: false` (no cone-diameter recipe; threads are region items; root cone 0.540 at
  both mouths).
- parametreler.json: knob lobe diameter 1.75, side port face 0.939 from the axis, pipe thread pitch 1/18, panel thread
  diameter 0.5625, stem diameter 0.249.

## Undetermined (written as such in the spec)
Internal flow path, seat, needle point and packing (none modelled); the set screw thread (modelled plain); the exact
run-out of each thread groove at chamfers / cones.

## Source conflicts (K)
- Product data call it a needle valve; the model's stem is a plain rod that overlaps the body (107.73 mm3). Spec
  follows the 3D and states the overlap.
- In the sleeve's lower part (y 0.0525 to 0.1475) the outer radius equals the internal thread's outer radius
  (0.21875): zero wall along the helical root flat. Spec follows the 3D.
- Drawing / product dimensions (3.04 / 3 1/16, 1.31 / 1 5/16, 0.94 / 15/16, 0.562) all agree with the model.

## Tier
Index: "hard". Found: 7 bodies, four modelled helical threads (two tapered pipe threads, two straight threads whose
mating parts share surfaces), a shelled five-lobe knob with 40 knurl grooves and 10 corner rounds, a sphere-trimmed
block. "zor" confirmed; it is at the upper end of the tier (the knob alone has 255 faces).
