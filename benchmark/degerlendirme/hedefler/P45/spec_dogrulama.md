# P45 spec verification (water-to-air fin heat exchanger with fan, guard and cord; 103 bodies)

Original: `kaynak.json` (103 solids in one multibody inch STEP; `olc_cekirdek.load_step` drops nothing: 0 empty bodies,
0 empty shells, 0 free shells). Spec unit inch (values round in inch). Scripts in `_gizli/is/`: s01 structure
(`metrics.json`), s02 face dumps (`b/dump_NN.txt`), `prof.py` (planar face wire profiles), `kes.py` / `kes2.py`
(sections, incl. the plug local frame), `lokal.py` (plug faces in the local frame), `kord.py` (cord helix fit),
`vida.py` (screw thread hand / pitch / flank), s03 interference + mesh volume (`girisim.json`), s05 hedef + kaynak +
target rows, s06 / s06b hidden lists, s07 recipe self-check (`s07_sonuc.txt`), s08 target table back-check
(`s08_sonuc.txt`), `r_govde.py` spec-text rebuilds (`rebuild_sonuc.json`, `rb_*.step`). spec.md is assembled from
`spec_1.md`, `spec_2.md`, `spec_3.md` + `tablo.md`.

## Target table (spec section 6) measured back against the original (s08, 103 / 103 bodies; max per group)
| group | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | 0.0000 | 0.0000 | 0.0015 | 0.0005 |
| P02 | 0.0002 | 0.0000 | 0.0005 | 0.0000 |
| P03 | 0.0003 | 0.0002 | 0.0004 | 0.0007 |
| P04 | 0.0037 | 0.0005 | 0.0000 | 0.0000 |
| P05 | 0.0005 | 0.0003 | 0.0005 | 0.0007 |
| P06 | 0.0001 | 0.0001 | 0.0004 | 0.0011 |
| P07 | 0.0000 | 0.0000 | 0.0006 | 0.0000 |
| P08 | 0.0013 | 0.0004 | 0.0007 | 0.0011 |
| P09 | 0.0013 | 0.0002 | 0.0007 | 0.0011 |
| P10 | 0.0000 | 0.0000 | 0.0009 | 0.0000 |
| P11 | 0.0000 | 0.0000 | 0.0011 | 0.0000 |
| P12 | 0.0044 | 0.0004 | 0.0010 | 0.0000 |
| P13 | 0.0187 | 0.0026 | 0.0000 | 0.0000 |
| P14 | 0.0000 | 0.0000 | 0.0018 | 0.0011 |
| P15 | 0.0000 | 0.0000 | 0.0005 | 0.0000 |
| P16 | 0.0002 | 0.0001 | 0.0012 | 0.0010 |
| P17 | 0.0000 | 0.0000 | 0.0003 | 0.0000 |
| P18 | 0.0000 | 0.0000 | 0.0009 | 0.0012 |
| P19 | 0.0000 | 0.0002 | 0.0010 | 0.0013 |
| P20 | 0.0002 | 0.0008 | 0.0015 | 0.0013 |
| H1 | 0.0006 | 0.0000 | 0.0014 | 0.0000 |
| H2 | 0.0192 | 0.0008 | 0.0000 | 0.0000 |

Largest: |dV| 0.019 % (washers; 5-decimal in3 rounding of a 20.5 mm3 body), dCoM 0.0018 mm, dbbox 0.0013 mm (4-decimal
inch rounding). GProp vs fine-mesh volume (s03, all 103 bodies): largest difference 0.21 % (< 0.5 %), so the GProp
values are the targets.

## Interference set of the original (capped boolean worker after bbox pre-filter; 246 pairs, 0 errors / timeouts)
Pairs > 8 mm3 (`hedef.json` girisimler, 11 pairs): P02-a/P01-b, P02-c/P01-d, P02-e/P01-f 108.594 each; P02-b/P01-c,
P02-d/P01-e 99.560 each (return bend leg ending at z -2.5 inside the hairpin leg end, which ends at -2.56; row B offset
0.02452 in x); P02-b/P07-a, P02-d/P07-a 9.034 each (row B bend legs at x -0.453 cut the tube sheet beside its holes at
x -0.47752); H1-a..d / P17 86.088 each (screws through the guard, which has no holes). Below 8 mm3: H1-a/H2-a 2.629,
H1-b/H2-b 1.859, P14/P18 0.842, H1-c/H2-c 0.832. All are stated in spec section 5. The fins do not touch the tubes
(no bbox overlap).

## Independent checks from the spec text (`r_govde.py`, build123d rebuild vs original)
| body | dV % | dA % | dCoM mm | dbbox mm |
|---|---|---|---|---|
| P01-a hairpin | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P02-a, P02-b return bends | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P07-a tube sheet | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P08-01 fin (wavy outline) | -0.0008 | -0.0004 | 0.0000 | 0.0000 |
| P09 end fin | -0.0008 | -0.0005 | 0.0000 | 0.0000 |
| P10 side channel (profile, chamfers, slots, cut-out, holes) | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P11 side channel | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P12-a fork clip | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P05-a flare fitting | -0.0086 | -0.0049 | 0.0003 | 0.0007 |
| P15 hub | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| P18 cord (straight + 3.25-turn helix + straight) | +0.163 | +0.131 | 0.038 | 0.505 |

P18: the check sweep (spline through 400 helix points, default sweep frame) lets the section roll slightly inside the
helix (rebuilt x min 1.2306 vs 1.2505); the spec states the 0.10 side stays parallel to X, which the original shows
exactly (cord x extent 1.2505 to 1.708 = helix 0.3575 + 0.10). Volume agrees to 0.16 %, so the path data are right.
Not rebuilt (described from faces and sections): P14 frame, P17 guard (grill pattern G), P16 blade, P19 plug body,
P20 blade, P06 nut, H1, H2; their face data were read from exact sections (`kes.py`, `kes2.py`, `lokal.py`) and dumps.

## Hidden lists
- `ozellikler.json`: 60 items covering all 22 distinct parts, all points snapped to face interiors on the original (`s06_gizli.py`). **s07: BAD 0** (every
  numbered item reproduces nom; 1 region-only item: the screw thread box).
- `resim_olculeri.json`: 9 rows = every dimension / note printed on the drawing. 6.53, 5.75, 5.78, 3.60 (model 3.596),
  0.375, 0.310, 0.220 all reproduce on the original within the printed precision; "Cord Length: 2 ft" is
  `modelde_var: false` (the model cord is a coil about 46.8 in long); "37 deg Flared" is `modelde_var: true` with no
  recipe (no recipe measures a cone half angle; the cones are counted in ozellikler F13).
- `parametreler.json`: tube OD 0.375, tube pitch 0.75, fin pitch 0.12, fin count 41, fan frame size 4.9.

## Undetermined (written as such in the spec)
Free-form blend between the cord exit boss and the frame corner; exact screw thread flank / root shape (pitch 0.05,
crest 0.170, RH given); exact section orientation of the cord inside the helix (free-form sweep); materials other than
copper (tube, fins); motor, wiring, water passages (not modelled).

## Source conflicts (K)
- Row B lies at x -0.47752 for the straight legs, sheet holes and fins but at x -0.453 for the -Z end parts (return
  bends, rings, stubs, fittings, nuts): creates the 99.56 / 9.03 mm3 overlaps. Spec reproduces both.
- Screw, washer, frame hole and channel hole centres differ by up to 0.015 in; the guard has no screw holes. Reproduced.
- Drawing 3.60 vs model 3.596 (rounds correctly); product data 3 5/8, 6 1/2, 5 3/4 differ from the drawing / model
  (6.53, 5.78): spec follows the 3D.
- Cord length 2 ft (note) vs a 3.25-turn coil in the model.

## Tier
Index (`_benchmark40_index.csv`): "very-hard" (103 solids). Found: 103 bodies in 22 distinct parts (42 fin strips, 12
rings, coil with 11 tube bodies), a fan with cambered blades bounded by six analytic surfaces, two grills with 5 curved spokes,
a modelled helical screw thread, a 3.25-turn helical cord and a ribbed plug. **"very-hard" (cok_zor) confirmed.**

## olc self-check result
pending (lead runs olc.py).
