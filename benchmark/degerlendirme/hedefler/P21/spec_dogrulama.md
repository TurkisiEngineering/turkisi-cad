# P21 spec verification

Master: 2 solids, 171 faces each (61 cylinder, 55 plane, 32 torus, 12 cone, 11 B-spline), no empty shells. STEP order:
solid 1 = Y2 (tilted, shaft +X), solid 2 = Y1 (axis-aligned, shaft -X). Targets from `is/s05_hedef.py`.
GProp vs mesh volume: +0.0096 % both bodies (< 0.5 %, GProp kept).

| Body | spec V mm3 | master V | dV % | dA % | dCoM mm | dBbox mm |
|---|---|---|---|---|---|---|
| Y1 | 55029.18 | 55029.1807 | -0.0000 | +0.0000 | 0.0013 | 0.0009 |
| Y2 | 55030.59 | 55030.5935 | -0.0000 | +0.0000 | 0.0010 | 0.0012 |

(`is/s08_dogrulama.py P21`; the residuals are the 4-decimal inch rounding of the table.)

## How the construction was proven
- **Y2 = Y1 moved** (Rz 180 deg, then +3 deg about the pivot line x = 0, z = -14.2875 mm, dir +Y): `is/s02_transform.py`
  matches 159 of 171 faces within 0.001 mm (bbox per face); the 12 others are the pin-end ring groove / hex socket,
  which differ (depths 1.524 / 2.286 vs 1.5875 / 2.375 mm, hex not swung). Volume difference 1.41 mm3 = these details.
- **Ruled shell (B-spline faces 128/140/142/143):** both boundary curves extracted (`is/s06_rule.py`, `s10_top.py`,
  `s11_top2.py`): base = circle R11.2395 at x = -29.845, far curve at x = 2.54 = line + arc R21.5265 (centred on the axis,
  tangent) + line + three lines. The spec's correspondence rule (per segment, angle vs arc length) reproduces the
  master faces within 0.019 mm (`is/s15_loftdev.py`, discretisation included).
- **Rounds:** face 144 = constant R2.286 (cross arcs fitted, residual 0); faces 145-148 = constant R3.048 along the four
  loft corner rulings, fading to a point on the base circle (`is/s08_arcs.py`, `s09_corner.py`).
- **Whole-solid check:** `is/s14_model.py` evaluates the spec construction as an inside/outside predicate (hub, loft,
  front plane, Y slab, cavity, slot cuts, knuckles, core, groove, teeth, pin-end details; rounds NOT modelled) and
  compares it with the master's classifier at random points: gear/core box 30000 points, 0 mismatches with r < 17.3 mm;
  hub box 1 mismatch in 8000; whole yoke box 63 / 30000 mismatches, all within the R2.286 / R3.048 round zones or
  < 0.01 mm from a loft surface (`is/s16_badfaces.py`).
- Interference (`is/s12_girisim.py`, capped worker): Y1-Y2 common 70.668 mm3; one 69.94 mm3 lens where the two tilted
  front faces cross (x 0.02..1.05, z -5.7..18.8 mm), plus six tooth contacts of 0..0.03 mm3 (`is/s13_ortak_bbox.py`).
  Written into `hedef.json` `girisimler`.

## Hidden lists
- `ozellikler.json`: 87 items (36 per yoke, 6 + 1 pin-end items for Y1 / Y2 incl. the 3 deg swing and the unswung hex,
  1 assembly). All recipes re-measured on the master (`is/s07_kontrol.py P21`): BAD 0. Tooth counts use `ayri_yuzler`
  (crown torus R2.52173 and back torus R5.14166: 16 faces each, tooth 0 split in two; count 15). Tooth phase is tied by
  `aci` flank vs knuckle face (85.5 deg). Free-form regions (ruled shell, rounds, tooth crowns) have `bolge` spheres only.
- `resim_olculeri.json`: the PDF is a catalogue drawing with 5 dimensions (10 1/4, 2 3/4, 3/4, 1/2, 1 1/8) and a note
  (max operating angle 136 deg, `modelde_var: false`). 10 1/4 is the straight-joint length; the master is 3 deg off
  straight (assembly X extent 10.2905 in), so the row measures 2 x 5.125 via `koordinat` (|Y1 xmin - 0| + 130.175 mm).
  All 5 rows reproduce the drawing on the master.
- `parametreler.json`: tooth count 15, bore 0.5, bore depth 1.125, pivot offset 0.5625, knuckle diameter 0.625.

## Undetermined
- None for the analytic geometry. The ruled shell is free-form in the master; the spec's correspondence rule is an
  equivalent description within 0.02 mm, not the master's own parameterisation.
- The tiny 0.0012 mm radial step where the tooth crown meets x = -3.175 mm is stated as found.

## Tier
- "zor" confirmed: two interleaved bodies, 15-tooth round-crown gear rings with radial flanks and exact phase, a
  free-form ruled yoke shell with constant-radius rounds fading to zero, clearance slots, and a rigid 180 deg + 3 deg
  placement of the second yoke with deliberate pin-end differences.

## Gate
- `olc.py` original vs itself (`is/olc_kendi/`): **85.00 / 85** (geometry 40, completeness 10, assembly 10, features
  87 / 87 = 20, drawing 5 / 5 = 5). Interference: 1 original pair, 1 rebuilt pair, 0 unknown.
- First run scored 84.00 (completeness 9): olc clusters Y1 and Y2 as one kind (they are the same design), while
  `hedef.json` had them as two `esdeger_grubu`. Both now carry `esdeger_grubu: "Y"` (2 pcs); first report kept as
  `is/olc_kendi_ilk_84.md`.
- `paket_denetle.py P21`: 2 bodies = 2, volume diff 0.000 %, assembly bbox diff 0.000 mm.
