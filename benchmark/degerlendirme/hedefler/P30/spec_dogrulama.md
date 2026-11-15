# P30 spec verification (threaded-sleeve gas filling valve with hex body and fluted cap)

Original: `kaynak.json` (3 solids, **mm** STEP, identity frame; STEP order P03 cap, P02 sleeve, P01 body). No empty
shells. Not in `_benchmark40_index.csv`; tier given by the lead as "zor". Scripts: `_gizli/is/` (ortak.py with IN = 1
so all script output is mm; s01 structure, s02 face dumps in `b/`, kesit.py exact sections, s03 interference, s04c
thread flats (mm thresholds), s11 exact surface parameters, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this
table, r_noktalar.py spec-formula point check).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | -0.0002 | 0.0000 | 0.0000 |
| P02 | -0.0034 | -0.0008 | 0.0001 | 0.0000 |
| P03 | -0.0001 | +0.0005 | 0.0000 | 0.0000 |

Largest |dV| 0.0034 % (sleeve, 3-decimal mm3 rounding). Bodies 3 / 3. GProp vs fine-mesh volume: largest 0.449 %
(sleeve, under the 0.5 % rule): GProp values used.

## Interference set of the original
Two touching pairs (cap / sleeve bounding boxes, sleeve / body on y = -2.025): common volume 0. `girisimler` empty.

## Independent check from the spec text
`r_noktalar.py`: 75 points from the spec formulas (cap bottom cone, cylinder, barrel R8.8, round R1.0, top face, button
arc and top, bore and bore end, flute bottoms and flanks of three flutes; body hexagon chamfer, fillet R1.5, inlet
chamfer, collar, T1 flats at theta 0 and 90 deg, **the closed thread tunnel's inner flats at y -7.94 ... -4.94 and its
flat end face**; sleeve T2 flats at theta 0 and 90 deg and the top chamfer): **all 75 on the original surfaces
(max < 0.002 mm)**.

Thread data from exact half-plane sections (`s04c_flat.py`): M10 x 1 (outer 5.0, inner 4.35048, flats 0.125) and
0.305 in - 32 (outer 3.8735, inner 3.35794, flats 0.09922), both phase advance p/4 per 90 deg (right-hand).

## olc self-check (original vs itself)
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00 = 34 / 34, drawing
5.00 = 5 / 5; 135 s).

## Hidden lists
- ozellikler.json: 34 items (body 16, sleeve 5, cap 12, assembly 1); every numbered item reproduces nom on the
  original (s07_kontrol.py, BAD 0); 8 are region-only (threads, the thread tunnel, chamfers, barrel, bottom cone).
- resim_olculeri.json: 5 rows, all modelled. **20 mm** and **3/8 in**: both end on the drawing's upper reference line,
  which is the cap's hidden bore end (y 6.0): inlet face y -14 to 6.0 = 20.000, hexagon top y -3.525 to 6.0 = 9.525 =
  0.375 in (body-to-cap plane distances, `govde2`). 12 mm hex (12.000), M10 x 1 (outer flat diameter 10.000),
  0.305 in - 32 (outer flat diameter 0.30500 in). Tolerances: 0.5 for whole mm, 0.005 in for 3/8, 0.0005 in for 0.305.
  The two upper-line readings are my interpretation of the drawing (lead to confirm).
- parametreler.json: hexagon AF 12, inlet thread diameter 10, inlet pitch 1.0, cap flute count 16, bore diameter 6.5.

## Undetermined (written as such in the spec)
Valve core, seal, internal thread (none modelled); exact thread run-out shapes (the inlet groove ends as a closed
tunnel with a flat end, which is described exactly).

## Source conflicts (K)
- The inlet thread groove continues 4.5 mm past the collar as a closed internal helical tunnel inside the collar and
  hexagon (a modelling artefact of the source). Spec follows the 3D and describes it (B5).
- The sleeve wall under its thread root is 0.108 mm and its top is a knife edge: spec follows the 3D.
- All drawing dimensions agree with the model.

## Tier
Given "zor" (not in the index). Found: 3 bodies, two modelled helical threads (one with an internal tunnel run-out),
a fluted cap with a barrel profile (16 rounded V flutes), a hexagon with chamfer and fillet. "zor" confirmed; the
mm frame and the few bodies keep it below P26.
