# P14 spec verification

## Spec vs master

A solid rebuild with the test kernel failed: the boolean cut of a 96-turn helical groove tube from the shaft returns
invalid results (in one piece, in fused 8-turn pieces, in 4-lead segments, and with an exact-helix pipe shell;
`is/s08_rebuild.py`, `is/s08b_occ.py`). The spec was therefore verified analytically against the master:

| Check | Result |
|---|---|
| Master surface samples (3.6 M points, UV grids on all 394 faces) -> distance to the spec's exact surfaces (OD cylinder, groove circle swept with lead 9.5504 mm / 2 starts / phase z = 1.1684 mm at theta 0, end planes, 45 deg chamfers) (`is/s08d_dev.py`) | P95 0.0029 mm, max 0.0031 mm (groove points: same) |
| Groove form: circle fit in the helical axial section, 2 x 9 stations along the length (`is/s06_prof.py`, `is/s07_drift.py`) | R 1.18110 mm (0.0465 in), centre on r = 8.31850 (OD), residual < 1e-12 mm; centre wobbles +/-0.003 mm with angle (spline approximation of the sweep in the master) |
| Lead from 382 land-edge vertices at theta = +/-90 (`is/s05_lands.py`) | 4.775200 mm per half turn (2 starts) -> lead 9.550400 mm = 0.376 in, residual 2e-13 |
| Volume: spec solid integrated exactly (R_max(theta, z)^2 / 2, `is/s08c_analytic.py`, two resolutions agree to 0.001 mm3) | 178089.88 mm3 vs master GProp 178065.83 mm3: +0.0135 % |
| CoM | spec solid (0, 0, 0) exactly (it has a two-fold axis); master GProp (0, 0, 0.043) mm: dCoM 0.043 mm |
| Bbox | identical: X / Y +/-8.3185, Z +/-457.2 mm (dBbox 0) |

## olc.py self-check: NOT completed

- Started 17:54 (`is/olc_kendi.log`); fine mesh done at 306 s; then step `govde:P01` (two-way exact deviation) ran
  > 1 h 45 min CPU-bound without finishing and was stopped on the lead's instruction (it blocked the shared olc gate).
- Reason (timed in `is/s11_olc_zaman.py`, < 2 min CPU): the master's two groove faces are single B-spline faces
  (6 x 1927 poles) that run the whole 914 mm length and wrap 96 turns, so their bounding boxes contain every sample
  point. In `exact_dist_bb` every sample (about 24 000 per direction: 2 x 2500 on the grooves, 40 on each of 384 land
  faces, + 8 hot points per face) therefore has lower bound 0 to both groove faces and projects onto them:
  0.024 s per `GeomAPI_ProjectPointOnSurf` on a groove face (0.03-0.04 s for the Extrema fallback / Tree), versus
  < 0.001 s on a land cylinder. With 2-5 groove calls per point, plus `project_own` for the groove samples, the
  deviation needs about 2-5 ks per direction.
- Estimate of the full olc runtime on this part: **about 2.5-4 h** (mesh 5 min + deviation 1.5-3 h + feature
  recipes with box regions over 60-120 mm of grooved shaft, each again projecting on the groove faces). A producer's
  rebuild will cost the same on the original side; on the rebuild side it depends on how the producer's kernel writes
  the groove (per-turn faces are fast, one long spline face is slow).
- The lists are not the cause: the slow step is §1 geometry (deviation), before any list is read.

## Lists

- Features: 21 items (no analytic counts on the free-form groove; regional deviation at groove bottoms / flanks at
  both ends and the middle, second start at theta 180, right hand at theta 90, three grooved boxes, end chamfers).
  Recipe points were placed on the faces by construction from the verified formula; not yet confirmed by olc.
- Drawing: 7 rows; only 3 ft has a recipe. Root diameter 0.562 matches the model (2 x (0.3275 - 0.0465)) but the
  groove bottom is free-form (hand check). Source conflict (K): the drawing prints "0.188 in travel distance per turn"
  but with 2 starts the model's lead is 0.376 in (0.188 is the groove-to-groove pitch). The designation 0.625 in x
  0.188 in is nominal; the model's outside diameter is 0.655 in. Pins (2 x 0.125 in) are not in the model.
- Undetermined: nut, pins and balls are not modelled; material only from product data.
