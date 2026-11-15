# P39 spec verification (side-connection threaded-stem dial thermometer, 3 bodies)

Source: original STEP (path in `kaynak.json`), read with `olc_cekirdek.load_step`: 3 solids, **22 empty shells dropped**,
0 free shells. Spec unit **mm** (the source is built in round millimetres: 28.5, 41.3, 13.5, 36.5 ...; inch-born sizes
6.35, 22.23, 25.4/14 are quoted in mm). Global frame = STEP frame (dial axis Z, stem axis X toward -X).
Work scripts: `_gizli\is\` (s01 structure, s02/s02b face dumps, s03 interference, s05 targets, s06 hidden lists,
s07 recipe self-check, s08 back-check, s10 dial marks, s11 sections, s12 thread sections, s13/s14 vertices, r_govde
rebuild from the spec text).

## Body roles

| STEP index | Spec | Role | Faces |
|---|---|---|---|
| 0 | P03 | calibration screw head (disc Ø4.5 x 1, cross recess) on the case back | 17 |
| 1 | P01 | case + boss + neck + hex + threaded spigot + stem + dial face + 100 marks + texts + pointer and hub (one solid) | 687 |
| 2 | P02 | lens, plain disc Ø70.21 x 3 (raw file: 136 faces, 132 of them zero-area degenerate planes; 4 after loading) | 4 |

## s08 table: spec section 6 vs original

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.0000 | 0.0000 |
| P02 | +0.0000 | +0.0000 | 0.0000 | 0.0000 |
| P03 | -0.0216 | +0.0068 | 0.0000 | 0.0000 |

(P03: rounding of the printed 13.81 mm3 / 52.68 mm2; the exact values are in `hedef.json`.)

## Rebuild from the spec text (`r_govde.py`, build123d)

| body | what was rebuilt | dV % | dA % | dCoM mm | max sampled face distance to original |
|---|---|---|---|---|---|
| P01 | 4.1 to 4.6 incl. the helical thread groove (half-turn sweeps), R1.5 neck blend, pointer, 100 marks; texts omitted | +0.0001 | -0.0036 | 0.0001 | 0.0007 mm (126 faces sampled) |
| P01 | same without the thread groove | +0.4251 | -2.54 | 0.19 | 0.66 mm on the thread |
| P02 | plain disc | 0.0000 | 0.0000 | 0 | 0.0000 |
| P03 | disc minus two crossed slots | 0.0000 | 0.0000 | 0 | 0.0000 |

The remaining P01 area residual (-0.86 mm2) is the omitted texts (side walls 0.01 high plus glyph details). The thread
phase, hand, pitch, taper and the stop at root-centre x = -43.0 reproduce the original to < 0.001 mm.
Note for builders: one long helical sweep failed silently in the boolean (no material removed); half-turn segments
worked. The spec does not prescribe a method.

## Volume check (GProp vs mesh)

| body | GProp mm3 | mesh mm3 | diff % |
|---|---|---|---|
| P03 | 13.8130 | 13.8089 | +0.030 |
| P01 | 99749.86 | 99744.11 | +0.006 |
| P02 | 11614.73 | 11614.29 | +0.004 |

All below 0.5 %: GProp values are the targets.

## Interference (capped BoolWorker after bbox pre-filter)

Pairs tested: P03-P01 common 0.0, P01-P02 common 0.0 (P03-P02 bboxes disjoint). **No pair above 8 mm3**:
`girisimler` is empty. Contacts: lens rim on the bezel bore (same radius 35.105), screw head top on the case back z 13.5.

## Hidden lists summary

- `ozellikler.json`: 54 items (P01 43, P02 3, P03 6, assembly 2); 34 measured items, 20 region-only items
  (`bolgesel_sapma` for profile rounds, chamfers, thread middle / free end / run-out, neck blend, pointer, scale ends,
  the three texts). Counts: 5 R2.5 tori, 3 R1.5 tori of the back, 6 hex flats, 4 slot-end cylinders, 84 separate mark
  top faces with centre above y -15 (`ayri_yuzler`, `yon` +Z; the box edge y -15 is ≥ 0.37 mm from any mark centre; a
  box at y -19 sits 0.1 mm from two mark centres and gave 90 instead of the expected 91, so it was not used).
  Thread is region-checked only (B-spline flanks are kernel dependent).
- `resim_olculeri.json`: 7 rows = every printed dimension (1.87, 0.875, 3.25, 7.25, 0.25, 4 in, 1/2 NPT). 6 measured;
  "1/2 NPT" `modelde_var: false` (callout, checked by the thread region items), like P20.
- `parametreler.json`: thread pitch 1.814286, stem diameter 6.35, stem length 101.6, case diameter 82.6, hex 22.23.
- s07 self-check: **BAD 0** (all measured items reproduce `nom` on the original; region points lie inside faces).

## Source conflicts

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall length | 7.25 in drawing; 7 1/2 in product data | 7.2520 in | 3D (= drawing) |
| Dial diameter | 3 in product data; 3.25 in drawing | case 3.252 in, bore 2.764 in | 3D |
| Taper | NPT 1:16 (1.7899 deg) | 1.783333 deg half-angle | 3D |
| Graduations | 2 °F, -40..160 (101 marks) | 100 equal marks over 280 deg | 3D |

## Undetermined

Digit and degree-ring glyph outlines (boxes given; volume about 0.08 mm3 in all); P03 material; the start of the thread
groove beyond the free end (any start clearing the material gives the same solid).

## Tier

Given "zor". Confirmed: 3 bodies but a modelled tapered helical pipe thread with exact phase, a two-axis main body
(revolves about Z and X, hex with double chamfer, blended neck), a 100-mark pattern and raised texts.

## olc self-check result

pending (lead runs olc.py)
