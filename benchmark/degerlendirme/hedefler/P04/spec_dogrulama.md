# P4 spec verification (enclosure)

Original: `kaynak.json` (STEP solids in order P02 lid, P01 base, H1 screw; one flat part, no assembly tree, identity frame).
Scripts: `_gizli/is/` (s01 structure, s02 face dump, sect.py sections, s03 targets + pairwise booleans, s09 table back-check, s07/s08 rebuilds, olc_mini.py recipes).

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | -0.0000 | 0.0010 | 0.0000 |
| P02 | -0.0000 | -0.0000 | 0.0005 | 0.0000 |
| H1 | -0.0034 | +0.0026 | 0.0008 | 0.0000 |

Largest: |dV| 0.0034 % (rounding of the printed mm3), dCoM 0.001 mm, dbbox 0.000 mm. Bodies 3 / 3. Assembly V, A, CoM, bbox printed from the same measurement.

## Interference set of the original (BRepAlgoAPI_Common, all pairs)
- P01 x P02: 4.998 mm3 (tongue outer flank 0.00157 in into the groove wall) -> below the 8 mm3 RUBRIK threshold, listed in hedef.json as information only.
- P02 x H1: 0.055 mm3 (shank R0.036 in hole R0.035). P01 x H1: 0.

## Independent rebuild from spec.md text only (build123d, s07/s08)
| body | dV % | dA % | IoU | note |
|---|---|---|---|---|
| P02 lid | +0.007 | +0.003 | 0.99986 | after the corner wording fix (constant R0.1 corner, sphere corner patches) |
| H1 screw | +0.006 | -0.007 | 1.0000 | |
| P01 base | +0.008 | +0.098 | (boolean with the original failed: coplanar faces) | CoM z within 0.001 mm; residuals only at the corner pockets (simplified in the check) and the R0.005 rib fillets (omitted in the check) |

Lessons put into the spec: (1) a uniform taper/offset of the rounded outline is wrong; the master keeps R0.1 and moves the corner centres (2.8 mm3 per corner otherwise); (2) the R0.1 top/bottom edge round on an R0.1 plan corner is a sphere octant (verified: corner patch = sphere within 0.00000 in); many kernels refuse the rolling-ball round, so the spec gives the explicit sphere centres.

## Hidden lists
- ozellikler.json: 40 items, all reproduce nom on the original (olc_mini.py). Several "region check" items use a dummy number (bbox) and rely on `bolge` for the verdict.
- resim_olculeri.json: 6 rows, 5 modelled and reproduced; 0.75 inside depth has no counterpart.
- Recipe extension used: `bbox_boyut` with govde `MONTAJ` (assembly bbox) for the 0.93 overall depth.

## Undetermined (written as such in the spec)
Screw thread size and pitch; real gate / ejector features.

## Source conflicts (K)
Drawing "Inside Height 2.11 / Inside Width 1.55" equal the label-recess outline in the 3D, not the cavity (2.24 x 1.69 at the rim); "Inside Depth 0.75" matches nothing (cavities 0.39 + 0.39). Product data 1 5/8 x 2 1/8 x 3/4 also differs. Spec follows the 3D.
