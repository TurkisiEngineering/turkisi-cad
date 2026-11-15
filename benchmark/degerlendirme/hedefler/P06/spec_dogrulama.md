# P6 spec verification (flange bearing)

Original: STEP solids in order P02 outer ring, H1-b, P03 inner ring, H1-a, P01 housing, H2 grease fitting; identity frame.

## Target table measured back
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | +0.0000 | 0.0013 | 0.0000 |
| P02 | -0.0000 | +0.0000 | 0.0010 | 0.0007 |
| P03 | +0.0000 | -0.0001 | 0.0013 | 0.0000 |
| H1-a | -0.0025 | -0.0021 | 0.0005 | 0.0010 |
| H1-b | -0.0025 | -0.0021 | 0.0009 | 0.0012 |
| H2 | +0.0007 | -0.0012 | 0.0016 | 0.0013 |

Largest: |dV| 0.0025 %, dCoM 0.0016 mm, dbbox 0.0013 mm (4-decimal inch rounding). Bodies 6 / 6.

## Interference set of the original
All 15 pairs 0.0000 mm3 (threads of screws and holes coincide in phase; ring/ring and ring/seat are face contacts). Empty set.

## Independent rebuild from the spec text
| body | dV % | note |
|---|---|---|
| P02 outer ring | -0.037 | bbox and CoM identical |
| H2 grease fitting | -0.000 | bbox and CoM identical (hex orientation confirmed) |
| P03 ring without holes | +2.90 | expected: the two threaded holes are ~240 mm3 |
| P01 housing without the small rounds and fillets | +0.164 | CoM within 0.0005 in; residual = the omitted R0.0437 / R0.01311 / R0.11811 blends |

The boolean comparison of the rebuilt housing with the original needed > 14 GB RAM and was stopped; only V and CoM were compared.

## Thread checks (thread_probe.py)
Hole and screw threads: right hand, pitch 1/28, minor flat centred w = 0.0260 + kP at theta = 0 (U = +X), identical in hole A, hole B, H1-a, H1-b.

## Hidden lists
- ozellikler.json 37 items, resim_olculeri.json 9 rows (8 modelled), all reproduce on the original. `aci` evaluated on cylinder axes for the hole pair (axes 60 deg as lines = holes 120 deg apart). MONTAJ bbox used for the 1.475 width.

## Undetermined
Rolling elements, seals, ring fit, grease passage, casting draft (none modelled).

## Notes
- The grease fitting shank and its housing hole are stored as cones with 0.001 deg half angle: a `silindir_cap` recipe will not find them, so none is used.

## Hidden-list fix (2026-11-11)
Backup: `is/lead_yedek_2026-11-11/`. I4 region point moved from (14.2392, -12.2673, -3.287), which is on the hole A axis and 2.59 mm from any face, to (17.4142, -11.5904, -3.1056), inside the thread crest face (cylinder r 3.175, face 8 of P03, 0.057 mm from its edges). The r 1.5 sphere now holds about 3100 samples per side. olc.py original vs itself (`araclar/kalibrasyon/k2c_P6`): 85.00 / 85, I4 tam, region 0.
