# P31 spec verification (rear-stem dial gauge for pressure, 12 bodies)

Source: `kaynak.json` → original STEP (inch-based; JSON in mm). `olc_cekirdek.load_step`: **12 solids, 20 empty shells
dropped** (`bos_kabuk_atilan: 20`). Spec unit: inch. Frame = STEP frame unchanged (origin at the case back boss face,
Z = gauge axis, dial toward +Z).

STEP order → spec names (`step_govde_sirasi`): 0 P01 case, 1 P02 bezel, 2 P06 stem rod, 3 P07 main pointer, 4 P08 sub
pointer, 5 H1-b hub cap (0, -0.375), 6 H1-a hub cap (0, 0), 7 P05 socket, 8 H2-b stop pin, 9 P04 dial, 10 P03 lens,
11 H2-a stop pin.

## s08: spec section 6 table against the original

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| H1-a | -0.0306 | -0.0011 | 0.0008 | 0.0000 |
| H1-b | -0.0306 | -0.0011 | 0.0008 | 0.0000 |
| H2-a | +0.0748 | +0.0183 | 0.0000 | 0.0000 |
| H2-b | -0.0380 | -0.0304 | 0.0015 | 0.0007 |
| P01 | +0.0000 | -0.0000 | 0.0000 | 0.0000 |
| P02 | +0.0005 | +0.0001 | 0.0011 | 0.0000 |
| P03 | -0.0000 | -0.0000 | 0.0014 | 0.0000 |
| P04 | +0.0001 | -0.0000 | 0.0013 | 0.0000 |
| P05 | +0.0000 | -0.0001 | 0.0008 | 0.0000 |
| P06 | +0.0001 | +0.0005 | 0.0008 | 0.0000 |
| P07 | -0.0023 | -0.0048 | 0.0013 | 0.0006 |
| P08 | -0.0520 | -0.0001 | 0.0008 | 0.0001 |

All deltas are rounding of the printed table (largest: P08 dV -0.05 % from 5-decimal in³ on a 9.4 mm³ body).

## Spec rebuild (is/r_govde.py, every body built from the spec text alone)

| body | dV % | dA % | dCoM in | dbbox max in | note |
|---|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.00000 | 0.00000 | |
| P02 | -0.0021 | -0.0015 | 0.00001 | 0.00000 | 16-element half-section |
| P03 | +0.0001 | +0.0001 | 0.00000 | 0.00000 | incl. marker recess |
| P04 | +0.2491 | -0.5154 | 0.00017 | 0.00000 | rebuilt **plain** (no engraving), as the spec announces |
| P05 | -0.2295 (GProp) / -0.007 (mesh) | -0.1822 | 0.00144 | 0.00038 | helical tapered thread; see below |
| P06 | +0.0002 | +0.0002 | 0.00000 | 0.00000 | |
| P07 | -0.0071 | -0.0059 | 0.00002 | 0.00001 | |
| P08 | +0.0028 | +0.0023 | 0.00002 | 0.00001 | |
| H1-a/b | 0.0000 | 0.0000 | 0 | 0 | |
| H2-a | 0.0000 | 0.0000 | 0 | 0 | |
| H2-b | +0.1984 | -4.1345 | 0.00006 | 0 | sliver cut left out (spec says it may be) |

P05: the rebuild's exact (GProp) volume is 0.23 % low, but its mesh volume is 7080.12 mm³ against the original mesh
7080.62 mm³ (-0.007 %); z-slab comparisons and half-sections at 0 / 90 / 180 / 270 deg agree with the original to
< 0.0005 in. The GProp shortfall is an integration artefact of the swept thread surfaces in the rebuild, not a shape
difference. Sections of the rebuild thread at angle 0 reproduce every crest / root / flank endpoint of the original
within 0.0005 in.

Region checks (is/s09_bolge_rb.py, dense two-way deviation original vs spec rebuild, every `bolge` of ozellikler.json):
all ≤ 0.0126 mm except the two dial engraving boxes (0.0254 mm = the 0.001 in engraving depth, plain rebuild). Thread
lower half 0.0069 mm, upper half with run-out 0.0126 mm, end chamfer 0.0012 mm. So a builder who omits the engraving
still passes the dial region items (tolerance 0.05 mm).

## Interference (is/s03_girisim.py, capped BoolWorker, bbox pre-filter)

One pair over 8 mm³: **P04 dial × P03 lens = 119.82 mm³** (lens skirt r 1.2–1.25 from z 0.821 overlaps the dial rim up
to z 0.84; ring 0.05 × 0.019 in → 119.8 mm³ analytically). In `hedef.json girisimler` and stated in the spec (§2, §5).
All other touching pairs: 0.

## GProp vs mesh volume (original)

All 12 bodies within 0.033 % (largest: hub caps 0.033 %). No body above 0.5 %: GProp volumes are the targets.

## Hidden lists

- `ozellikler.json`: 68 items (51 with a numeric recipe, 17 region-only; 18 carry a region check). s07 self-check on the original: **BAD 0**. Hole counts on
  the dial use `bolge` boxes because glyph free-form faces of matching curvature would otherwise be counted (26 / 20
  instead of 2 / 2). Dial graphics are checked only by two `bolgesel_sapma` boxes (`tur: yazi`); the thread by two
  boxes plus the end chamfer (`vida_disi` / `pah`).
- `resim_olculeri.json`: 6 rows, every printed dimension of the catalogue drawing (2.64, 1.02, 2.00, 0.96, 0.31,
  1/4 NPT); all reproduce on the original within the printed precision (0.005 in). 1/4 NPT is measured as the 0.54
  shank that continues the crest cone (thread outside diameter at its top); noted in the row.
- `parametreler.json`: dial diameter 2.5, bezel OD 2.64, pitch 1/18, stem rod diameter 0.31, socket length 2.0.

## Source conflicts

- Drawing shows a **hexagon** wrench section; the model has a **square** (four flats 0.56 across, corners on R0.324).
  Spec follows the model and says so.
- Product data "1 in stem length" has no single model counterpart (rod projects 0.96 beyond the socket end; thread zone
  0.4018). Not a drawing dimension; noted in spec §7.
- Lens and dial overlap (119.82 mm³) in the source; reproduced, not trimmed.

## Undetermined items

Exact glyph outlines / positions of the engraved numerals and text, exact lengths and widths of individual graduation
marks (given approximately: counts, radii, label positions); case interior, movement, pressure passage; graphic
colours; the scale the main pointer reads.

## Tier

Index tier "hard" confirmed: 12 bodies, a modelled helical tapered pipe thread with run-out, a 30-element rolled bezel
profile, and a 1690-face engraved dial.

## olc self-check result

`is/olc_kendi/olcum.md`: **84.50 / 85** (geometry 40, completeness 9.50, assembly 10, features 20.00 (68/68), drawing 5.00 (6/6); 390 s, 2026-11-12).

**Shortfall 0.50 = completeness, distinct-part check for group H2 (stop pins).** Caused by the original file, not by the lists: in the original, one dial numeral's engraving cuts a 0.001 in sliver into H2-b, so H2-b has 11 faces and its area is 13.214 mm2 vs 12.668 mm2 for H2-a (+4.3 %), beyond olc.py's congruence tolerance; olc therefore puts the two pins in different clusters even when the original is compared with itself. The lists keep H2-a / H2-b as one group (H2) on purpose: the spec tells the builder the sliver may be ignored, and a builder who models two identical pins gets the group right (full 2.00). Splitting the group would give the original 85.00 but would punish every builder who follows the spec. Lead to decide.
