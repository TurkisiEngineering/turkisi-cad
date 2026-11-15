# P5 spec verification (rod end)

Original: STEP solids in order P01 housing+shank, P02 ball; identity frame.

## Target table measured back
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.0015 | 0.0000 |
| P02 | -0.0000 | +0.0001 | 0.0000 | 0.0000 |

Largest: |dV| 0.0000 %, dCoM 0.0015 mm (printed CoM rounding), dbbox 0.000 mm. Bodies 2 / 2.

## Interference set of the original
P01 x P02: 0.0000 mm3 (ball sphere = socket sphere R0.5625). Empty set.

## Independent rebuild / checks from the spec text
- P02 ball (build123d): dV +0.000 %, IoU 1.00000.
- P01 head region y >= 0 (eye, neck torus, flats, 14.5 deg slopes, socket): dV -0.001 %, CoM identical (boolean with the original failed, coincident faces).
- P01 shank y < 0: volume integrated numerically from the spec thread definition (phase, P/8 flats, chamfer, run-out cone): 4575.78 vs 4583.75 mm3 (-0.17 % of the shank, -0.07 % of P01). Residual comes from the master's flats being ~0.006 in vs P/8 = 0.00625 in.
- Thread analysis (thread_probe.py on the helical faces): right hand confirmed (phase concentration 0.97-0.99 vs 0.02-0.6 for left hand), root flat centred at y = 0.00312 + 0.05k on +X.

## Hidden lists
- ozellikler.json 18 items, resim_olculeri.json 10 rows (9 modelled), all reproduce on the original.
- Recipe extension used: `koordinat` (|referans - bbox min/max|) for the 1.625 and 2.625 drawing dimensions. Lead to confirm or replace.

## Undetermined
Liner and real ball clearance (not modelled), max swivel 65 deg (kinematic), plating.

## Notes
- P02 has ~126 zero-area degenerate faces in the master (export artefact); face count 140 is not meaningful.
