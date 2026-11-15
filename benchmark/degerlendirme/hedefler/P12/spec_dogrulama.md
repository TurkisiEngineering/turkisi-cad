# P12 spec verification

Master: one solid, 68 faces. The target table was measured on the master STEP (`is/s08_meas.py`, `is/s09_gizli.py`).

| Body | spec V mm3 | master V (B-rep / mesh 0.003) | dV % | dCoM mm | dBbox mm |
|---|---|---|---|---|---|
| P01 Gear | 3771.33 | 3771.325 / 3770.068 | 0.000 (mesh -0.033) | < 0.0001 | 0.0001 (Ymax 10.18992 vs 10.19) |

- Helix: flank crossings of r = 9.19239 tracked over 13 sections X = -9.9 .. -0.1 (`is/s04_helix.py`): rate
  -6.25007 deg/mm, max residual 0.0024 deg, so lead 57.600 mm, left hand about +X. Space centres phi = 90 - 6.25 (x + 10)
  + k 360/13 (exactly 6.923 = 90/13 at X = -10, i.e. one space on +Z).
- Profile: the 13 spaces are identical and symmetric (centre spread < 1e-5 deg). Table T1 (32 points, 0.1 mm
  spacing, `is/s07_table.py`): a cubic interpolation through the 63 mirrored points reproduces the master section within
  0.0005 mm (polyline 0.002 mm).
- Involute check (`is/s03_inv.py`): best-fit base radius 8.53-8.71 depending on the radius band, error 0.02-0.04 mm; the
  flank is not an involute. Nominal 20 deg / module 1 base radius would be 8.175. Stated in the spec; T1 governs.
- Every recipe point of `ozellikler.json` / `resim_olculeri.json` lies on the master surface (max 4.6e-4 mm, checked in
  `s09_gizli.py`), including the helix check points at X = -9 and -1, which confirms the twist sense.
- Gate: `olc.py` original vs itself (`is/olc_kendi/`): **85.00 / 85** (geometry 50, completeness 10, features 20 / 20,
  drawing 5 / 5). Audit `paket_denetle.py P12`: 1 body = 1 body in the STEP, volume diff 0.0001 %, bbox diff 0.0001 mm.
- Drawing: 10 rows; pitch diameter 18.38, helix angle 45 and pressure angle 20 have no face (`modelde_var: false`).

## Undetermined
- Nominal pressure angle / module are not reflected exactly in the master's tooth form; the measured profile table is
  given instead. Nothing else is undetermined.

## Tier
- Lead's tier "shape" (1 solid) confirmed: one body, but the helical non-involute tooth needs a tabulated profile and a
  helical sweep; it sits at the upper end of "shape".
