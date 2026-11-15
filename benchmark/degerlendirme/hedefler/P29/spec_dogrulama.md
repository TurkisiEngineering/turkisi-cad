# P29 spec verification (swivel hoist ring, hand-tightened, 3/4-10)

Original: `kaynak.json` (5 solids, identity frame, inch STEP; STEP order P01, P02, P03, P04, H1). **22 empty
(zero-area) shells inside the bolt solid** are dropped by `olc_cekirdek.load_step` (132 degenerate point faces at
(-0.22, -0.332, -0.031) in); the bolt has 46 real faces. Scripts in `_gizli/is/`: s01 structure, s02 / s02b face dumps
(`b/`), kesit6 sections, kenar edge loops, s03 interference + mesh volumes, s04_egrilik B-spline curvature, s04c_flat
thread flats, r_bail / r_diger text rebuilds, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table, s09
thread point classification.

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | -0.0000 | 0.0005 | 0.0013 |
| P02 | -0.0000 | +0.0000 | 0.0013 | 0.0011 |
| P03 | +0.0000 | +0.0000 | 0.0014 | 0.0000 |
| P04 | -0.0000 | -0.0000 | 0.0001 | 0.0000 |
| H1 | -0.0000 | +0.0000 | 0.0017 | 0.0000 |

GProp vs fine-mesh volume: largest 0.019 % (bushing): GProp values used.

## Interference set of the original (capped boolean worker, 8 touching pairs)
All common volumes 0. `girisimler` is empty.

## Independent checks from the spec text
| body | check | result |
|---|---|---|
| P01 base | full rebuild (`r_diger.py base`) | dV 0.000 %, every face max 0.0002 in or less |
| P04 sleeve | full rebuild | dV 0.000 %, every face exact |
| H1 bolt | rebuild without thread | all faces exact except the thread faces and the R0.1 fillet drawn as a line in the check |
| H1 thread | point classification, 493 random points (`s09_dis_dogrula.py`) | 0 mismatches (RH, P 0.1, flats P/8, phase as written) |
| P03 bushing | rebuild without the slot-mouth flares | all analytic faces exact; dV +0.88 % = the two flares (free-form, undetermined) |
| P02 bail | bar sweep + web with R0.2 rounds (intersection construction) + R0.125 and R0.375 fillets (`r_bail.py`) | all 36 analytic faces exact (0.00000 in); R0.125 fillets 0.00013; R0.375 web-leg fillet 0.0007 on the band, 0.0055 on the round zone; top-of-hole blends not rebuilt (0.007); dV -0.015 % |

B-spline curvature census (`s04_egrilik.py`): bail faces 20/21 constant R0.125 (rolling ball); 33/36 R0.375; 32-37
and 44-53 carry R0.375 in one direction but vary (0.23 to 0.375) where they cross the R0.2 rounds; bushing flares
19/24 vary 0.41 to 1.84 (no constant radius) and 18/21/22/25 are nearly flat (R 25 to 31).

## Hidden lists
- ozellikler.json: 62 items (base 14, bail 17, bushing 8, sleeve 11, bolt 10, assembly 2); all numbered items
  reproduce nom on the original (`s07_kontrol.py`, BAD 0); 18 are region-only (rounds, fillets, chamfers, flares,
  thread, dome).
- resim_olculeri.json: 7 rows, all printed values. 6.995 overall height (tol 0.0005), 3.5 base tip to tip (0.05),
  0.75 bail thickness (0.005), 2.4 inside width (0.05; model 2.3975), 1 thread length (0.5; base bottom to bolt end
  1.000). Not measured (`modelde_var: false`): the 3/4-10 note (thread checked in ozellikler) and the movement note.
- parametreler.json: overall height 6.995, star diameter 3.5, bar diameter 0.75, inside width 2.3975, pitch 0.1.

## Undetermined (written as such in the spec)
The free-form surfaces of the two bushing slot-mouth flares (asymmetric, +X smaller than -X; boundary curves and two
sections given); the blends where the bail hole sides meet the top bar (about R0.375, 0.007 in effect). A rebuild that
leaves the flares out loses 0.88 % of the bushing volume (above the 0.5 % tolerance); the boundary data given should
bring a lofted surface within it.

## Source conflicts (K)
- Drawing 2.4 inside width vs model 2.3975 (product data 2 3/8 = 2.375): within the drawing's 1-decimal precision.
- The bushing slot mouths are flared differently on the two sides (CoM x = +0.0045 in): kept as in the source.

## Tier
Index: "hard". Found: 5 bodies, one modelled helical thread, a swept bail with web, full rounds and blend fillets,
free-form flares, a six-point star. "hard" confirmed.

## olc self-check result
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00, drawing 5.00; 239 s).
