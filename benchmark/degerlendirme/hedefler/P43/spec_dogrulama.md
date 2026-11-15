# P43 spec verification (two-sided platform step ladder, 248 bodies)

Source: original STEP read with `olc_cekirdek.load_step` (248 solids, 0 empty shells dropped). Unit in the file: inch.
Spec unit: inch. JSON: mm. Work scripts: `is/` (s01 metrics, s02 shape grouping + frame registration, s03 interference +
volume check, s04/s05 sections and face data, s06 names + hedef + kaynak, s07 hidden lists, s07_kontrol recipe check,
s08 placement check, s09 spec assembly).

## Target table against the original

The spec target values (section 3 per-part V / A, section 8 per-body CoM and bounding box, assembly totals) are written
directly from the original's GProp / exact bounding boxes, so for every body ΔV = 0 %, ΔA = 0 %, ΔCoM = 0, Δbbox = 0 at
the printed precision (4 decimals in inch). Largest rounding: 0.00005 in (0.0013 mm).

## Placement check (`is/s08_yerlesim_kontrol.py`)

The spec describes 45 shape groups (35 custom parts, 10 hardware items; 11 type-B mirror twins) and places every body with
the printed (rounded) orientation and origin. Rebuilding each of the 248 bodies from its shape's reference geometry with
the printed placement reproduces the original instance: largest nearest-vertex distance **0.0036 mm**, largest CoM
error **0.002 mm** (all 248). Mirror twins: local u → (e − u) then the printed proper rotation (verified in the same run).
Shape grouping (`s02`): every instance registered to its group reference with max vertex error 0.0028 mm.

## Volume (GProp vs mesh)

`is/girisim.json`: no body differs by more than 0.5 % between GProp and the mesh integral; GProp values are the targets.

## Interference (capped boolean worker, bbox pre-filter, `is/s03_girisim.py`)

607 bbox-overlapping pairs checked, 0 invalid booleans. **137 pairs overlap by more than 8 mm³**: rivets and discs pass
through unholed rails, steps and straps (no holes are modelled in the source), step ends sit inside the rail channels,
the spacer drums cut into the top cap plates, two label strips overlap a cap plate / each other, one disc overlaps a lock
casting. All 137 are in `hedef.json` `girisimler` and listed in spec section 7.

## Hidden lists

- `ozellikler.json`: 49 items (rails, all four step lengths, rib groove counts and radii, platform grooves / V-notch
  angle / thickness, bar diameter, lattice brace wall and height, shoe groove count, foot pad grooves, sleeve wall, cap
  plate hole, rail cap cross hole, strap / angle / plate thicknesses, corner radii, hinge plate and drum, strip
  thickness, rivet / disc diameters; 5 region-only items for the free-form or lattice parts).
  `is/s07_kontrol.py`: every numbered item reproduces its nom on the original (BAD 0), all points inside faces
  (point-to-face distances ≤ 0.015 mm).
- `resim_olculeri.json`: the drawing prints 6 dimensions (6 ft, 46 in, 12.75 in platform width, 22 in platform depth,
  25.25 in, 50 in). Measured: 72.0098, 46.0000, 12.7500, —, 25.1876, 49.5923 in.
  - 6 ft, 46 in, 50 in, 22 in are whole feet / inches: tol 0.5 in.
  - **25.25 in: the model is 25.1876** (outer foot-pad faces); the catalogue rounds to a quarter inch, so tol = 0.125.
    With tol 0.005 the original itself would fail. Lead to confirm.
  - **22 in Platform Depth: `modelde_var: false`, no recipe.** The extension lines touch the outer flange faces of the
    front and back rails at platform height; the model's spread at y = 0 is 22.410 in (section of the four rails). No
    recipe type measures a spread at a given height.
- `parametreler.json`: platform height 46, overall height 72.0098, steps per side 4, step spacing 11.4854, rail section
  3.0304 (x 1.1814, wall 0.0625).

## Undetermined items

- Exact shape of the free-form blend faces: lattice brace (2 per body), top cap side plates (12 / 3), lock casting rounds,
  corner bracket (1). The spec gives their extents and neighbours only. These affect §1 deviation locally (< ~0.05 in).
- Materials (not geometry).

## Source conflicts

- Drawing 25.25 vs model 25.1876 (see above); drawing 22 vs model 22.41 at y = 0.
- One foot plate has sharp corners, the other three have R0.1 corners (kept as in the source: P24 vs P25).
- Not exactly symmetric: label strips (23 + 11 + 11 of three slightly different sizes) and one lock casting per side.

## Tier

`cok_zor` confirmed: 248 bodies in 45 shape groups, 11 mirror pairs, a 149-face lattice part and free-form cap plates;
no threads, gears or helices.

## olc self-check result

`is/olc_kendi/olcum.json`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00;
755 s, 2026-11-12 18:35). First run scored 83.00 (completeness 8): olc clusters part types mirror-invariantly, so the
10 type-B mirror twins (P02, P10, P12, P15, P17, P19, P21, P27, P29, P32) now share their type-A part's
`esdeger_grubu` in `hedef.json` (s06_hedef.py `TW`); spec.md still lists them as separate mirror parts.
