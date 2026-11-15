# P38 spec verification (synchronous motor with gearbox, small assembly)

Source: original STEP (not published) (AP203, inch).
`olc_cekirdek.load_step`: 14 solids, 0 empty shells dropped, 0 free shells. Frame unchanged. Scripts: `_gizli\is\`.

## Target table back-check (s08_dogrulama.py: spec.md section 6 vs original)

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0003 | -0.0001 | 0.0013 | 0.0000 |
| P02 | -0.0000 | +0.0000 | 0.0012 | 0.0000 |
| P03 | +0.0002 | +0.0001 | 0.0011 | 0.0000 |
| P04 | -0.0003 | -0.0001 | 0.0000 | 0.0000 |
| P05 | +0.0002 | -0.0006 | 0.0007 | 0.0000 |
| P06 | -0.0022 | -0.0013 | 0.0004 | 0.0000 |
| P07 | +0.0008 | +0.0033 | 0.0009 | 0.0000 |
| P08 | +0.0360 | -0.0054 | 0.0000 | 0.0000 |
| P09 | -0.0119 | +0.0008 | 0.0001 | 0.0013 |
| P10 | +0.0124 | +0.0016 | 0.0011 | 0.0013 |
| W1-a / W1-b | -0.0004 | -0.0003 | 0.0008 | 0.0013 |
| W2-a / W2-b | +0.0419 | +0.0137 | 0.0008 | 0.0013 |

All residuals are rounding of the printed table (in³ to 5 decimals, CoM / bbox to 4 decimals). hedef.json holds full mm values.

## Rebuild from the spec text (r_govde.py, r_iletken.py; built in inch, scaled)

| body | dV % | dA % | dCoM mm | dbbox mm | faces rb/orig |
|---|---|---|---|---|---|
| P01 housing (cup, rounds, 9 tabs + notches, 2 ears with bends + reliefs) | +0.0001 | +0.0007 | 0.0000 | 0.0000 | 157/162 |
| P02 cover (plate, rounds, pad, 7 bosses, holes) | +0.0001 | +0.0002 | 0.0000 | 0.0000 | 47/64 |
| P03 motor can (revolved section, bead, slots, holes, notch) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 33/48 |
| P04, P05, P06, P07, P08, P09, P10, W1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | — |
| W2 twisted conductor (loft through the 11 sections of spec 4.13) | +0.137 | -0.766 | 0.0093 | 0.0070 | 17/32 |

Face counts differ only by kernel face splitting (the source splits revolved / cylindrical faces into halves). The pad edge
of P02 was rebuilt with a 0.00999 fillet (a fillet equal to the pad height leaves no side face); the spec states a full
quarter round. W2 is freeform in the source; the spec gives sampled sections, so a ~0.1 % residual is expected.

## Interference set (s03_girisim.py, capped BoolWorker after bbox pre-filter)

All pairs with touching bboxes evaluated (24 pairs). Overlaps: P04 stator disc / P09 lead guide 1.91 mm³; P03 can / P09
0.073 mm³; all others 0. **No pair above 8 mm³ → `girisimler` = []**. The two W1 / W2 pairs took ~40 s each (B-spline).

## GProp vs mesh volume
Max difference 0.056 % (W2 conductors); all others < 0.04 %. Below 0.5 % → GProp volumes are the targets.

## Hidden lists
- `ozellikler.json`: 59 items (P01 20, P02 8, P03 10, P04–P10 and leads 18, assembly 3); 54 numeric recipes, 5 region-only
  (ear, pad, bead, two conductors). Counts: 9 tab top lands (`ayri_yuzler`), 7 torus tab bends (`ayri_yuzler`), 2 + 2
  cylinder bends, 7 cones, 7 boss tops, 2 can holes. Freeform W2 bodies use `bolgesel_sapma` boxes only, no `sayi`.
- `resim_olculeri.json`: 6 rows = every printed dimension of the catalogue drawing (2.165, 2.56, 1.99, 1.34, 0.264, 0.25),
  all `modelde_var: true`, all reproduced exactly. 1.99 is measured as housing Ymin to shaft Ymin + 0.125 (shaft radius).
- `parametreler.json`: M–S axis distance 1.0496, sheet thickness 0.02, shaft Ø0.25, ear hole spacing 1.885, can Ø1.75.
- `s07_kontrol.py P38`: **BAD 0** (all 54 numeric items and 6 drawing rows reproduce `nom` on the original; all
  measurement points within 0.0003 mm of the intended face, none on an edge or axis).
- `paket_denetle.py P38`: govde_hedef 14 = govde_step 14, hacim_fark 0.0 %, montaj_bbox_fark 0.0 mm.

## Source conflicts
- Product data lists overall 1 1/2 × 2 1/4 × 2 1/2 and shaft length 0.26: rounded catalogue values; the model gives
  1.34 (Z, matches the drawing), 2.165 and 2.56 (match the drawing); shaft D-length 0.264 matches the drawing.
  No conflict between the drawing and the model.

## Undetermined
- Exact twist law of the stranded conductor ends (freeform B-spline): given as an 11-station sample table.
- Internal gear train, rotor, winding, bearings: not in the source.

## Tier
Benchmark index: very-hard. Confirmed: 14 bodies, two drawn sheet-metal cups with crimp tabs, bent ears with relief slots,
revolved bead, D-shaft, twisted freeform conductors. olc.py run time should be short (only two small B-spline bodies, ~40 s
per boolean pair).

## olc self-check result
`olc.py` original vs itself (2026-11-12, `_gizli\is\olc_kendi\`): **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00, drawing 5.00). 14 / 14 bodies matched, IoU 1.000000 each, interference 0 / 0; run time 157 s.
