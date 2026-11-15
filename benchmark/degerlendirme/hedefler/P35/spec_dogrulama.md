# P35 spec verification (external gear pump with flange mount, keyed shaft and threaded ports)

Original: `kaynak.json` (13 solids, inch STEP, identity frame; STEP order P04, P05, P01, P02, H1-a, H1-b, H1-c, H1-d,
H2-c, H2-b, H2-a, H2-d, P03). `olc_cekirdek.load_step`: **0 empty solids, 0 empty shells, 0 free shells dropped**.
Scripts in `_gizli/is/`: s01 structure (`metrics.json`), s02 face dumps (`b/dump_NN.txt`), rnd.py renders, kesit.py /
kesit2.py sections, dis_kesit.py thread half-plane sections, s03 interference + mesh check (`girisim.json`), r_lib.py +
r_plaka / r_kucuk / r_arka / r_on text rebuilds (`rb_*.step`), fk.py face-distance check, s05 hedef, s06 hidden lists,
s07 recipe self-check, s08 this table.

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| H1-a | -0.0031 | +0.0012 | 0.0000 | 0.0009 |
| H1-b | -0.0031 | +0.0012 | 0.0000 | 0.0009 |
| H1-c | -0.0031 | +0.0012 | 0.0000 | 0.0009 |
| H1-d | -0.0031 | +0.0012 | 0.0000 | 0.0009 |
| H2-a | -0.0003 | +0.0006 | 0.0009 | 0.0008 |
| H2-b | -0.0004 | +0.0005 | 0.0009 | 0.0008 |
| H2-c | -0.0004 | +0.0005 | 0.0009 | 0.0008 |
| H2-d | -0.0004 | +0.0005 | 0.0009 | 0.0008 |
| P01 | -0.0000 | -0.0000 | 0.0012 | 0.0005 |
| P02 | -0.0000 | -0.0000 | 0.0017 | 0.0000 |
| P03 | +0.0000 | -0.0000 | 0.0014 | 0.0000 |
| P04 | -0.0001 | -0.0001 | 0.0008 | 0.0000 |
| P05 | +0.0005 | +0.0000 | 0.0012 | 0.0008 |

Bodies 13 / 13. Largest |dV| 0.0031 % (washers, 5-decimal in3 rounding), dCoM 0.0017 mm, dbbox 0.0009 mm (4-decimal
inch rounding). GProp vs fine-mesh volume (s03): largest 0.020 % (shaft) → GProp values are the targets.

## Interference set of the original (capped BoolWorker, bbox pre-filter, all 16 touching pairs)
All 0.000 mm3 (shaft/key, shaft/front cover, cover/plate, plate/rear housing, washers/heads, washers and heads/rear
housing). `girisimler` is empty.

## Independent checks from the spec text (`fk.py`: per-face max distance, both directions)
| body | check | result |
|---|---|---|
| P02 middle plate | full rebuild (`r_plaka.py`, O1 grown 0.0205 as written) | dV +0.001 %, no face over 0.002 in either way |
| P04 shaft / P05 key | full rebuild (`r_kucuk.py`) | dV 0.000 % / +0.015 %, no face over 0.0005 in |
| H1 washer / H2 hex head | full rebuild (`r_kucuk.py`) | dV -0.003 % / +0.022 %, no face over 0.0005 in |
| P03 rear housing | rebuild of B1-B9 without the R0.04 / R0.1 / R0.01 rounds and without the thread grooves (ports bored at the minor diameter) (`r_arka.py`) | dV +0.98 %; the thread grooves alone are 0.0714 in3 = 1170 mm3 = 1.00 % (T1 0.0431 + T2 0.0283 in3, from the stated profiles), leaving -0.01 % for the omitted rounds. All non-round, non-thread faces lie on the rebuild; residuals only next to the rounds (max 0.0185 in at the R0.04 port-face rounds, expected <= 0.04 (sqrt2-1) = 0.0166 plus blends) and on the thread surfaces (<= thread depth) |
| P01 front cover | rebuild of A1-A7 without the R0.3 domes, the R0.1 slot bottoms and the R0.04 / R0.02 / R0.01 rounds (`r_on.py`) | dV +0.52 % (omitted R0.3 domes about +0.48 %, slot-bottom rounds about +0.14 %, minus the omitted concave fillets); every other face lies on the rebuild; residuals only on the round regions (max 0.109 in where the domes are missing, 0.025 in on the slot walls where the R0.1 bottoms are missing) |
| port threads | half-plane sections at theta = 0, 90, 180 deg (`dis_kesit.py`) | constant crest / root flats p/8, 30 deg flanks, phase advance exactly p/4 per 90 deg in the stated sense (right-hand) for both ports; thread end planes at exactly 10 pitches |

## olc self-check (recipes on the original, `s07_kontrol.py P35`)
BAD 0: every numbered item of ozellikler.json (95 items, 79 with a measurement, 16 region-only) and all 15 drawing rows
reproduce nom on the original.

## Hidden lists
- ozellikler.json: 95 items: P01 30, P02 6, P03 29, P04 4, P05 4, washers 2 x 4, hex heads 3 x 4, assembly 2. Region-only
  items: the two port threads (boxes), both mouth chamfers, slot-bottom rounds, pilot chamfer, the two R0.3 domes, the
  50 deg and 58 deg cones, the hex-head chamfers. Count items: 2 mounting holes, 8 slot ends R0.1095, 4 R0.25 flat-to-boss
  fillets (z-limited box excludes the +Y boss R0.25).
- resim_olculeri.json: 15 rows, all `modelde_var: true`, every one within its printed precision. "2.5in" (flange
  height) uses `bbox_boyut` with a box z 0.47..0.4875 in (mesh nodes on the flange walls just below the top R0.01 round,
  above the 0.404 skirt), tol 0.05 (1 decimal printed). "0.188in" = shaft top (P04 ymax) to key bottom (P05 ymin).
  "1.25in" = pilot face (P01 zmax) to shaft end (P04 zmax). The two thread notes are measured as the root (major)
  diameter on a root land (0.875 / 0.75). "Dash Size 10, 08" and "SAE Trade Size AA" are notes, not dimensions (not
  listed).
- parametreler.json: pilot diameter 2.0, mounting hole spacing 3.25, shaft diameter 0.5, flange thickness 0.406, large
  port thread pitch 1/14.

## Undetermined (written as such in the spec)
Gears, gear chambers, bearings, seals, internal passages (none modelled); bolt shanks / tapped holes (none); blind-hole
thread (plain in the model); which port is the inlet (not marked; the larger -X port is presumably suction, my reading).

## Source conflicts (K)
None: the drawing's 15 printed dimensions all agree with the model within their printed precision; the product data
(flange 3 15/16 x 2 1/2 x 3/8, holes 0.39 on 3 1/4, shaft 1/2 x 1 1/4, key 0.125 x 5/8 x 0.188, overall 4 x 3 5/8)
agrees within its fractional rounding (3/8 vs modelled 0.406 flange thickness: the drawing's 0.406 governs; 3 5/8 vs
3.604 overall height). Product data names no material for shaft, key and plate.

## Tier
Index: "very-hard" (cok_zor). Found: 13 bodies (5 distinct custom / hardware + 2 x 4 identical hardware), two modelled
helical port threads, two cast housings with about 500 faces including ~110 B-spline blend faces, R0.3 domes, two
chamfer cones and many R0.04 rounds. No gears are modelled (the "gear pump" interior is absent). "very-hard" confirmed
by the casting and thread content.

## olc self-check result
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00 (95/95), drawing 5.00 (15/15); 180 s, 2026-11-12).
