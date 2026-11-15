# P18 spec verification

Master: 11 solids, 13 empty zero-area shells (78 faces) inside the shield solid, dropped by olc and stated in the spec. Targets measured on the
master (`is/s03_meas.py`, `meas.json`); body-to-STEP-index map in `hedef.json` notes.

| Body | spec V mm3 | master V (B-rep / mesh) | dV % (B-rep) | dCoM | dBbox |
|---|---|---|---|---|---|
| P01 shield | 129230.92 | 129230.92 / 129230.10 | 0 | 0 | 0 |
| P02 clamp | 15685.41 | 15685.41 / 15679.67 | 0 | 0 | 0 |
| P03 plug | 625.24 | 625.24 / 624.32 | 0 | 0 | 0 |
| P04 arm | 70311.57 | 70311.57 / 70260.93 | 0 | 0 | 0 |
| P05 base | 6040.45 | 6040.45 / 6043.02 | 0 | 0 | 0 |
| H1-a/b screws | 230.99 | 230.99 / 230.70 | 0 | 0 | 0 |
| H2-a/b bolts | 689.60 | 689.60 / 688.57 | 0 | 0 | 0 |
| H3-a/b nuts | 166.45 | 166.45 / 166.54 | 0 | 0 | 0 |

(Spec table is in inches; the values above are the mm targets written to `hedef.json`; all GProp/mesh gaps < 0.1 %.)

- Local frame u = (x - y)/sqrt 2, v = (x + y)/sqrt 2, w = z (`is/ql.py`, `is/lsec.py`); every recipe point is written in
  global mm via that transform and lies on the master surface (max 5.7e-4 mm, `is/s05_gizli.py`).
- Threads (`is/thr.py`): H1 48 TPI, crest flats z = 0.00585 + kP toward +u, +P/4 toward +v (right hand), H1-a and H1-b
  same phase. H2 1/4-20: crest flats u = 431.101 + 1.27k toward +w, -P/4 toward +v (right hand); H2-b same phase as
  H2-a. H3 nut root flats coincide with the bolt crest flats (u = 432.371 + 1.27k).
- Interference (capped worker, `is/s04_int.py`): all pairs 0 except clamp-shield 1.36 mm3 (< 8 mm3, not listed).
- Audit `paket_denetle.py P18`: 11 bodies = 11, volume diff 0.000 %, assembly bbox diff 0.000 mm.
- **Gate: olc.py original vs itself = 85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20 / 20,
  drawing 5 / 5; `is/olc_kendi/`). Interference: 0 pairs, 0 unknown. After the run the 12 in row was set
  `modelde_var: false` (no recipe, not counted; score unchanged).

## Drawing
- 6 rows: 8, 8, 0.125, 1.375 (base hole spacing 34.925 mm), mounting hole 0.25 (model 0.255, passes at tol 0.005).
  "12 in" has no exact model counterpart (arm 11.615, clamp socket face to base back face 12.115, cut corner to base back
  12.5): `olcum: null`.

## Undetermined
- None measured as missing. The base slot-mouth transition (notch through the lip, <= 0.4 mm features) is described by
  its defining cylinder and one check section; its R0.01 blend patches are given by intent only.

## Tier
- "hard" confirmed (11 bodies, 3 kinds of modelled threads, diagonal local frame, moulded clamp/base blends).
