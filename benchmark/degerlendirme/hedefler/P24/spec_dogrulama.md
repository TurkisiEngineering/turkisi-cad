# P24 spec verification

Master: 3 solids (P02 lever 14 faces, H1 set screw 21, P01 hub 45), no empty shells. STEP order -> spec names:
`["P02", "H1", "P01"]` (kaynak.json). Targets measured on the master (`is/s01_yapi.py`, `is/s05_hedef.py`).

| Body | dV % | dA % | dCoM mm | dBbox mm | GProp V / mesh V (mm3) |
|---|---|---|---|---|---|
| P01 Hub | +0.0000 | +0.0000 | 0.0011 | 0.0000 | 29611.04 / 29608.95 (0.007 %) |
| P02 Lever (bar, bends, arms, balls) | -0.0000 | -0.0000 | 0.0003 | 0.0000 | 27888.39 / 27881.73 (0.024 %) |
| H1 Set screw (donanim) | +0.0003 | -0.0007 | 0.0008 | 0.0000 | 449.49 / 449.33 (0.035 %) |

(spec table rounding vs master, `is/s08_dogrulama.py P24`). GProp vs mesh < 0.5 %, so targets are GProp values.

- Profiles and edges read from the face dump (`is/b/dump_*.txt`) and edge loops (`is/kenar.py`).
- Lever: bend tori R0.375 / r0.1875 centred (0, +-0.625, 0.75); arm axis (0, +-0.83340, 0.55266) through the ball centre
  (0, +-3, 1.875). The arm angle 33.5500 deg is the tangency solution 2.375 sin t - 1.125 cos t = 0.375 (tangent point
  (0.83225, 0.43747), equal to the master's arm-axis point to 1e-5 in).
- Thread (`is/s03_profil.py`, half-plane sections at 0/90/180/270 deg and 179/181 deg): 13 TPI, right hand, root
  r 0.25 (cylinder slivers), crest r 0.20004 (B-spline), root and crest flats P/8, flanks 3P/8 axially at 30 deg.
  Crest centres at +X: z = -0.8125 + kP; +P/4 per quarter turn toward +Y. Ridge ends at the half plane -X (plane face
  y = 0, z -0.1923..-0.125); 45 deg entry countersink r 0.26923 at z = -0.875 trims the ridge.
- Interference (`is/s03_girisim.py`, capped boolean worker): all three pairs common volume 0 (bar 0.01 radial clearance in
  the cross hole; set screw = bore, coincident; flat point tangent to the bar). `girisimler` empty.
- Recipe self-check `is/s07_kontrol.py P24`: 25 measured items + 5 drawing rows (14 region-only items), BAD 0.
- **Gate: olc.py original vs itself = 85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20, drawing 5;
  interference 0 / 0 / 0 unknown; `is/olc_kendi/`). No pose loss: the set screw's hex socket and the hub's thread give
  every body a defined orientation, and the lever is not rotationally symmetric.
- `esdeger_grubu`: P01, P02, H1, one per body (three distinct parts, no copies).

## Drawing
- 6 rows: 7 (lever y extent), 3.25 (assembly z), 1.75 (hub z), 1.25 (hub diameter), 1/2"-13 (major diameter 0.5 on the
  plain bore end), all exact on the master. `.75` (thread depth) has no recipe (`olcum: null`): the thread end is
  the edge circle z = -0.125 at the foot of a cone, no plane; it is covered by the thread region items F13-F15.

## Undetermined
- None for geometry. Product data not in the master: knobs are nylon in the product but fused into the steel lever
  solid in the master; set-screw and bore threads not modelled (stated in the spec).

## Tier
- "hard" confirmed: 3 bodies, a modelled 1/2-13 internal thread with phase and an abrupt ridge end, a swept bent lever
  whose angle comes from a tangency condition, and a hex-socket set screw with a countersunk socket mouth.
