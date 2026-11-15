# P20 spec verification (diaphragm air pulse valve, 1/4 pipe ports)

Original: `kaynak.json` (6 solids, one flat part, identity frame, inch STEP; STEP order P01, P02, H1-a, H1-b, H1-c,
P03). **16 empty (zero-area) shells inside the diaphragm solid** are dropped by `olc_cekirdek.load_step` (as for P2 / P3);
the diaphragm has 12 real faces (108 in the file). Scripts: `_gizli/is/` (s01 structure, s02 face dumps in `b/`,
kenar.py, kesit.py, s03 interference, s04 / s04b / s04c thread analysis, r_govde / r_kucuk text rebuilds, fkontrol.py,
s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table, s09 thread point-classification check).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | -0.0000 | 0.0012 | 0.0010 |
| P02 | -0.0000 | +0.0000 | 0.0011 | 0.0013 |
| P03 | +0.0004 | -0.0001 | 0.0006 | 0.0013 |
| H1-a | +0.0016 | -0.0011 | 0.0010 | 0.0013 |
| H1-b | +0.0016 | -0.0011 | 0.0011 | 0.0013 |
| H1-c | +0.0016 | -0.0011 | 0.0011 | 0.0013 |

Largest: |dV| 0.0016 % (5-decimal in3 rounding of the screws), dCoM 0.0012 mm, dbbox 0.0013 mm (4-decimal inch
rounding; the exact extremes are printed separately in the spec). Bodies 6 / 6. GProp vs fine-mesh volume: largest
0.039 % (screws): GProp values used.

## Interference set of the original (capped boolean worker, all 11 touching pairs)
All 0: the screw shanks have exactly the hole diameter (0.138); flange, diaphragm and cover touch face to face.
`girisimler` is empty.

## Independent checks from the spec text
| body | check | result |
|---|---|---|
| P01 body | rebuild without threads and rounds, ports as crest cones (`r_govde.py`) | every non-thread, non-round face of the original lies on the rebuild (max 0.000 in); residuals only on the omitted R0.03125 / R0.0625 rounds (max 0.013 in) and on the thread surfaces (= thread depth) |
| P02 cover | rebuild with pilot port as crest cone (`r_kucuk.py`) | all non-thread faces exact; dV +0.83 % = the omitted thread groove |
| P03 diaphragm | full rebuild | dV -0.000 %, area -0.0002 %; point distances 0.000 in except a 0.011 in reading on part of the rebuilt edge torus, where a test point on the exact original torus (rho 0.80999, y 0.1521) also reads 0.011 to the rebuild while the same point rotated to z = 0 reads 0.000: a point-to-face extrema artefact on the revolved face, not geometry |
| H1-a screw | rebuild with vertical recess walls, no corner flats | dV +0.093 %; residuals only on the recess walls (5 deg draft and 45 deg corner flats omitted in the check, max 0.008 in) |
| threads T1 / T2 / T3 | point classification against the original (`s09_dis_dogrula.py`, random theta, depth and radius between crest and root cones) | T1 1 / 380, T2 18 / 385, T3 5 / 373 mismatches, all within 0.0005 in of a surface (T2 is only 0.0038 deep; its crest flats are axial lines, up to 0.0008 off the cone) |

Thread data were read from exact half-plane sections (`s04c_flat.py`): constant crest / root flat widths, radii on
cones of half-angle 1.783 deg, phase advance exactly p / 4 per 90 deg (right-hand) for all three ports.

## olc self-check (original vs itself)
85.00 / 85, details at the end of this file.

## Hidden lists
- ozellikler.json: 50 items (body 24, cover 9, diaphragm 4, screws 4 x 3, assembly 1); all numbered items reproduce
  nom on the original (s07_kontrol.py); 16 are region-only (threads as boxes, chamfers, rounds, recesses).
- resim_olculeri.json: 5 rows. 1.99 (assembly Y 1.9921) and 2.00 (body X 2.0039) at tol 0.005. **1.62 (bottom view,
  diameter): the model is 1.6299; the drawing truncates (1.6299 -> 1.62, 2.0039 -> 2.00, 1.9921 -> 1.99), so tol = 0.01
  (one unit of the last printed digit); with 0.005 the original itself would fail this row. Lead to confirm.** The two
  "1/4 NPT" notes are `modelde_var: false` (no recipe measures a cone diameter; the threads are region items in
  ozellikler.json; the root cone diameter at both mouths is 0.540 = 1/4 NPT OD).
- parametreler.json: flange / cover diameter 1.62992, screw circle radius 0.68, hub diameter 0.625, inlet end face
  1.189 from the axis, thread pitch 1/18.

## Undetermined (written as such in the spec)
Internal passages, seat, solenoid / pilot mechanism (none modelled); screw thread size (shank plain 0.138); exact thread
run-out at the mouth chamfers.

## Source conflicts (K)
- Drawing 1.62 vs model 1.6299 (see above); product data "overall length 1 5/8" likewise.
- Inlet called 1/4 NPT: the model's root cone matches 1/4 NPT (0.540 at the mouth, 18 per inch) but the groove is only
  0.0038 deep and undercut (dovetail), unlike the outlet (0.0369 deep, normal 60 deg V). Spec follows the 3D.
- Top (pilot) port not named in the product data: 27 per inch tapered = 1/8 pipe size.

## Tier
Index: "hard" (fluid, solenoid valve). Found: 6 bodies (3 identical screws), three modelled tapered helical threads,
one of them undercut, an inclined cut with blended rounds. "hard" confirmed.

## olc self-check result
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00;
727 s). The 1.62 drawing row passes only with its tol 0.01 (see Hidden lists).
