# P32 spec verification (axial cooling fan, 80 mm square)

Source: original STEP (kaynak.json), read with `olc_cekirdek.load_step`: 3 solids, **18 empty (zero-area) shells dropped**,
0 empty solids, 0 free shells. Units: all 4 LENGTH_UNIT entries in the whole file are `SI_UNIT(.MILLI.,.METRE.)`; no inch
unit anywhere. Values are round in mm (80, 38, 71.5, 4.4, 44.4, 82, R5, R3.4, R0.5) -> spec in mm.
STEP solid order (= kaynak.json `step_govde_sirasi`): P02-a, P02-b, P01.

## s08: spec target table vs original

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | +0.0000 | 0.0001 | 0.0000 |
| P02-a | -0.0006 | -0.0003 | 0.0000 | 0.0000 |
| P02-b | -0.0006 | -0.0003 | 0.0001 | 0.0000 |

(rounding of the printed table only). `paket_denetle.py P32`: govde_hedef 3 = govde_step 3, hacim_fark 0.0 %, montaj bbox Δ 0.0.

## Rebuild from the spec text (is/r_kanat.py, is/r_govde.py)

Built only from the numbers printed in spec.md, compared with the original (olc_cekirdek.deviation, two-way):

| body | dV % | dA % | dCoM mm | dbbox max mm | dev mean / p95 / max mm |
|---|---|---|---|---|---|
| P02-a (plate + lofted root) | +0.73 | +2.81 * | 0.062 | 0.013 | 0.007 / 0.029 / 0.375 (root inner end) |
| P02-b | +0.73 | +2.81 * | 0.062 | 0.029 | 0.007 / 0.031 / 0.371 |
| P01 (no R0.5 front rounds) | +0.067 | +0.61 | 0.012 | 0.027 | 0.0018 / 0.0009 / 0.54 (lead W1 bend) |

\* the check solid is a compound of plate + root touching at the junction, so the 2 x 17.5 mm² junction wall is counted
twice (+2.9 %); the true area difference is about -0.1 %.

- P01 volume excess +59.6 mm³ = the R0.5 front-edge rounds that the check rebuild could not apply (one-batch fillet
  failed in the check kernel): 1102 mm of front edges x (1 - π/4)·0.5² = 59.1 mm³. With the rounds the residual is
  ≈ 0.0 %.
- P01 max deviation 0.54 mm is in the tight lead bend at (34.1, -15.3, 16.6); leads otherwise within ~0.1 mm. Missing
  rounds give up to 0.21 mm locally (front face edges).
- Blade plate surfaces: fitted cylinders R 96.805 / 97.577 (concentric form R 97.555 used) fit the free-form faces
  within 0.0012 mm; thickness 0.750 measured on all through-thickness edges.
- Blade root: loft through 10 measured sections + 2 end sections; +2.9 mm³ (0.73 %), max 0.37 mm at the inner-end step.

## Interference (capped BoolWorker, bbox pre-filter; is/girisim.json)

| pair | common mm³ |
|---|---|
| P02-a / P01 | 113.412 |
| P02-b / P01 | 113.398 |
| P02-a / P02-b | 0.002 (below 8, not listed) |

`hedef.json` girisimler = the two pairs above (blade roots inside the rotor: a modelling artefact of the source, kept).
Worker peak memory 0.22 GB.

## GProp vs mesh volume

P02-a 402.832 / 402.781 (+0.013 %), P02-b same, P01 89134.50 / 89132.56 (+0.002 %). All < 0.5 % -> GProp values are the
targets.

## Hidden lists

- ozellikler.json: 46 items (P01 37, P02-a 4, P02-b 4, assembly 1). Kernel-dependent free-form content (blades, root,
  lead bends, R0.5 rounds) is checked with `bolgesel_sapma` boxes / whole-body deviation, not with face counts. Counts
  used only for analytic surfaces that every kernel keeps (cylinders r 2.2 / 3.4 / 39.269 / 36.903, tori r 5 / 7.5,
  cones). s07_kontrol: **BAD 0** (every recipe reproduces its nom on the original; all points lie inside a face, distance
  ≤ 0.007 mm).
- resim_olculeri.json: 6 rows = every printed dimension of the catalogue drawing (80 mm width, 80 mm height, 71.5 mm x2,
  4.4 mm, 38 mm); all `modelde_var: true`, all reproduce exactly (tol = printed precision: 0.5 for integers, 0.05 for
  one decimal).
- parametreler.json: frame size 80, depth 38, hole spacing 71.5, hole diameter 4.4, blade count 9.

## Source conflicts

None. Drawing (80, 80, 71.5, 4.4, 38 mm) and product data (3.150" = 80 mm, depth 1.496" = 38 mm, hole 0.173" = 4.4 mm)
agree with the model. The drawing's front view shows the spoke side (z = +19). Note the model itself: only 7 of the 9
blades are fused into the fan body; 2 are separate solids that overlap the rotor (kept as the source has them).

## Undetermined / approximated (as in spec section 8)

- Blade root given as sections (≈ 0.1 mm), not an exact surface; 0.12 mm step at the root inner end simplified.
- Lead centre-line nodes measured; tight bends approximate (≤ 0.5 mm). Lead start caps buried, undetermined.
- Lead outer caps: plane normal (0.9073, -0.3959, -0.1418), 8° off the rod axis, as measured.

## Tier

"zor / hard" **confirmed**: 3 bodies but P01 has 363 faces, 9 free-form (B-spline) blades with a twisted root, curved
spokes, a clamp-jaw connector region and swept leads; the blade shape had to be reverse-engineered into an analytic
plate + section table.

## olc self-check result

`is/olc_kendi/olcum.md`: **84.96 / 85** (geometry 39.96, completeness 10, assembly 10, features 20.00 (46/46), drawing 5.00 (6/6); 228 s, 2026-11-12).

**Shortfall 0.04 = geometry, max-deviation term of P01 (fan body).** Caused by the original file and the measuring path, not by the lists: the exact boolean on the 363-face body with its free-form blades timed out (120 s cap), olc used its thin-shell IoU estimate (IoU 1.000000, P95 0.00000) and its mesh-bound samples on 6 spline faces read a 0.0144 mm maximum where the true self-deviation is 0. The lists have no influence on this term.
