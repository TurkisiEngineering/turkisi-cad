# P28 spec verification (plastic in-line filter housing: head and bowl)

Original: `kaynak.json` (2 solids, inch STEP, identity frame; STEP order P01 head, P02 bowl). No empty shells.
**There is no drawing of this part in the source folder** (the only PDF there is an unrelated document), so
`resim_olculeri.json` is `{"rows": []}` and `kaynak.json` "pdf" is null; RUBRIK §5 has no rows for P28.
Scripts: `_gizli/is/` (s01 structure, s02 face dumps in `b/`, kesit.py exact sections, s03 interference, s04c thread
flats, s11 exact surface parameters, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table, r_kase.py
bowl rebuild, r_kafa.py rough head rebuild, r_noktalar.py spec-formula point check).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.0009 | 0.0000 |
| P02 | -0.0000 | +0.0000 | 0.0001 | 0.0000 |

Bodies 2 / 2. GProp vs fine-mesh volume: 0.0004 % (head), 0.0022 % (bowl): GProp values used.

## Interference set of the original
One touching pair (head / bowl on y = 4.3): common volume 0. `girisimler` is empty.

## Independent checks from the spec text
| check | result |
|---|---|
| bowl rebuilt from W1 / W2 (`r_kase.py`, build123d) | dV -0.0000 %, dA -0.0000 %, bbox exact |
| head rebuilt from H1 to H10 without end-block rounds, lettering and thread grooves (`r_kafa.py`) | dV +0.167 %; the only rebuild points farther than 0.001 in from the original are in the ports (omitted thread groove, up to 0.021) and on the omitted R0.0625 end-block rounds (up to 0.020) |
| 60 points from the spec formulas on both bodies (ears, rim, dish, slopes, end blocks and their rounds and corner spheres, bridges, hole bottoms on the slope plane, boss, pocket, pin, recess, bore, port bottoms and chamfers, thread flats of both ports at theta 0 and 90 deg, letters I / N / T, bowl core / ribs / rounds) (`r_noktalar.py`) | all 60 on the original surfaces (max 0.0000 in) |

Thread data from exact half-plane sections (`s04c_flat.py`): 18 per inch, cones of half-angle 1.7833 deg, root 0.540 at
both mouths, flats 0.00605 / 0.00694, phase advance p/4 per 90 deg (right-hand) in both ports.

## olc self-check (original vs itself)
`is/olc_kendi/olcum.md`: **80.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00 = 45 / 45,
drawing `-`; 291 s). **The 5-point shortfall is §5 only: there is no drawing of this part, so `resim_olculeri.json` has no
rows and olc.py scores §5 as not applicable (`-`).** It is caused by the source folder, not by the lists; every other
category is full. Lead to decide whether §5 is rescaled for P28 (as RUBRIK does for §3 on single-body parts) or left at 0.

## Hidden lists
- ozellikler.json: 45 items (head 33, bowl 11, assembly 1); every numbered item reproduces nom on the original
  (s07_kontrol.py, BAD 0); 8 are region-only (threads, chamfers, button pin, slope hole bottoms, lettering).
  Count items that free-form faces could disturb (R0.0625 torus / cylinders: the letter O / U faces have about that
  curvature) carry a `bolge` box that keeps the lettering out.
- resim_olculeri.json: `{"rows": []}` (no drawing).
- parametreler.json: housing diameter 4.75, overall height 12.0, bridge hole spacing 1.75, pipe thread pitch 1/18,
  bowl rib count 8.

## Undetermined (written as such in the spec)
Exact free-form outlines of the letters O and U (given as point lists and near-ellipses); thread run-outs at the mouth
chamfers and port bottoms; any cartridge / seal / bowl cavity (the source bowl is solid).

## Source conflicts (K)
- No drawing. Product data "1/4 NPT" agrees with the modelled thread (18 per inch, root 0.540 at the mouth).
- The source bowl is a solid (no cavity, no thread to the head): spec follows the 3D.

## Tier
Given "zor". Found: 2 bodies only, but the head is a dense moulded part (195 faces: two tapered helical port threads,
sloped bar with rounded raised end blocks and spherical corners, bridges whose holes end on an inclined plane, a
free-standing relief pin in a pocket, raised lettering with free-form letters); the bowl is simple (8 ribs in two
crosses). "zor" is acceptable; by body count and bowl it is at the lower edge of the tier (the threads and lettering
carry most of the difficulty).
