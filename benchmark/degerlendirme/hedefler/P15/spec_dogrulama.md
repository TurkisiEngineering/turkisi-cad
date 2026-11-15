# P15 spec verification

Master: 3 solids (101 / 70 / 196 faces), no empty shells. Targets measured on the master (`is/s03_meas.py`, `meas.json`).

| Body | spec V mm3 | master V (B-rep / mesh 0.01) | dV % | dCoM mm | dBbox mm |
|---|---|---|---|---|---|
| P01 Air motor body | 557607.4 | 557607.42 / 557529.39 | 0.000 (mesh -0.014) | < 0.001 | 0.000 |
| P02 Muffler (donanim) | 42565.8 | 42565.79 / 42552.66 | 0.000 (mesh -0.031) | < 0.001 | 0.000 |
| P03 Housing + base + shaft | 1939275.4 | 1939275.36 / 1939103.29 | 0.000 (mesh -0.009) | < 0.002 | 0.000 |

- Profiles: every revolve point was read from face census + edges (`is/q.py`, `dump.txt`); barrel arcs are the masters'
  spindle tori (P01 R280.67 / centre-circle 236.982; P03 R330.733 / 253.263), end radii checked (42.418, 76.2).
- Threads (`is/thr.py`, half-plane sections): P01 ports 18 TPI, root cone r 6.858 at the top, taper 1.7833 deg, root
  flats centred at depth 0.4298 + k P toward +X, +P/4 per quarter turn toward +Z (right hand); both ports identical
  (translated). P02 crest flats at y = 36.0509 + k P toward +X, -P/4 toward +Z (right hand). P03 1/4-20 holes: root flats
  at depth 0.0794 + 1.27k toward the radially outward side; the 4 holes are 90 deg rotated copies (checked on two holes).
- All 53 feature points and 17 drawing-row points lie on the master surfaces (max 5.4e-4 mm, `is/s05_gizli.py`).
- Audit `paket_denetle.py P15`: 3 bodies = 3, volume diff 0.000 %, assembly bbox diff 0.000 mm.
- Interference: P01-P03 common volume 0 (contact only). **P01-P02 (threaded port vs threaded nipple) could not be
  measured: the capped boolean worker timed out at 120 s.** `girisimler` is left empty; the olc gate will show whether
  olc's own interference step gets a value.
- **Gate: olc.py original vs itself = 85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20 / 20,
  drawing 5 / 5; `is/olc_kendi/`). olc's interference step: 0 measured pairs, 1 unknown pair (P01-P02, boolean
  timeout) on both sides, so no penalty.

## Drawing
- 17 rows. 11 1/2 (model 11.620), 6 (model 6.100 flange / 6.080 feet) and 7 1/4 (model 7.290) disagree with the master:
  `olcum: null`, conflict stated in the spec. 1/4-20 call-out and the 1/8 keyway depth have no clean recipe (null).
  The PDF thread note prints "ERROR!:Thread Note"; the catalogue image gives 1/4 NPT, 18 TPI, 0.40 engagement, which
  matches the port depth 10.2057 mm (feature F9).

## Undetermined
- None for geometry. The P01/P02 thread pair does not mate exactly (stated as source fact). Internals not modelled.

## Tier
- "hard" confirmed: 3 bodies, three different modelled threads (tapered NPT male/female, 1/4-20 internal), spindle-torus
  barrels, cast base with blended fillets.
