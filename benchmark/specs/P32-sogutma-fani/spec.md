# Design spec: axial cooling fan, 80 mm square frame, 38 mm deep

Rebuild the three solids below exactly as described, in the global frame given here. Every number was measured on the
reference model. Lengths in **mm**, angles in degrees.

## 1. Units, frame, bodies

- Unit: **mm** (the reference model is metric; its round values are mm values).
- Global frame (keep it exactly; the result is compared without any alignment):
  - **z** = fan axis. The **front face** of the frame (the face carrying the 11 spokes and the motor housing) is the plane
    **z = +19**; the **rear face** is **z = -19**.
  - Origin = centre of the frame square on the fan axis, mid-depth. The square frame spans x = -40 … +40, y = -40 … +40.
  - The two lead wires leave the frame on the **+x side**, below the x axis (y ≈ -16), and run out to x = 61.76.
- Output: **3 solids** (no others): P01 (fan body), P02-a and P02-b (two loose impeller blades). Keep them as separate
  solids; do not unite the loose blades with P01 even though they overlap it (section 7).

## 2. Product and the reference model's own simplifications

An AC axial "muffin" cooling fan for electronics: 80 x 80 mm square plastic frame, 38 mm deep, four Ø4.4 mm mounting
holes on a 71.5 mm square pattern, a 9-blade plastic impeller on a ball-bearing motor hub, and two wire leads. Product
data (for information only): single-phase AC motor, plastic frame and blades.

The reference model is a simplified catalogue model. Copy its simplifications, do not "fix" them:

- The frame, the motor housing, the rotor, **seven** of the nine blades, the connector block and the two lead stubs are all
  **one solid** (P01). The rotor is joined to the motor housing by a solid neck; there is no bearing, no shaft, no
  air gap other than the 1.15 mm slot described in 5.5.
- The remaining **two blades** are separate solids (P02-a, P02-b). They are identical to the seven fused blades and sit in
  the two blade positions that P01 lacks; their roots lie inside the rotor (overlap 113.4 mm³ each, section 7).
- The lead wires are plain round rods Ø1.25 mm, cut off flat at x ≈ 61.5; no insulation layers, no conductors, no
  labels, no lettering anywhere.
- The reference file also contains 18 empty (zero-area) shells; they are ignored and are not part of the model.

## 3. Part list

| ID | Qty | Name | Type | Notes |
|---|---|---|---|---|
| P01 | 1 | Fan body: frame + spokes + motor housing + rotor with 7 blades + connector block + 2 lead stubs, one solid | custom | plastic |
| P02 | 2 | Impeller blade, loose (P02-a, P02-b; identical, rotated copies) | custom | plastic |

Equivalence groups: P01 (1 instance), P02 (2 instances). There is no bought-in hardware in the model.

## 4. Blade (P02-a, P02-b, and the seven blades inside P01)

All nine blades are the same shape, placed by rotation about the z axis in steps of 40°. A blade is a thin (0.75 mm)
cylindrically curved plate with a straight-sided trapezoid outline and a circular tip, plus a twisted root that dives into
the rotor.

### 4.1 Blade frame

Each blade has its own right-handed frame (u, v, w), defined by an angle ψ and the fixed tilt β = 42.000°:

- u axis e1 = (-sin ψ, cos ψ, 0) — horizontal, pointing radially outward through the blade (towards azimuth ψ + 90°).
- v axis e2 = (-cos β cos ψ, -cos β sin ψ, sin β)
- w axis n = (sin β cos ψ, sin β sin ψ, cos β) — the blade's plate normal, tilted 42° from z.
- origin C' (a point on the blade's tip axis, 0.064 mm off the z axis; see placements).
- A blade point with local coordinates (u, v, w) is at global C' + u·e1 + v·e2 + w·n.

Placements (C' of blade k is C' of P02-a rotated about the z axis by -40°·k):

| Blade | ψ (deg) | u axis points to azimuth (deg) | origin C' (x, y, z) |
|---|---|---|---|
| Blade a (P02-a, separate solid) | 79.4126 | 169.41 | (-0.0627, 0.0117, -5.3472) |
| Blade b (P02-b, separate solid) | 39.4126 | 129.41 | (-0.0405, 0.0493, -5.3472) |
| P01 blade 1 | -0.5874 | 89.41 | (0.0006, 0.0638, -5.3472) |
| P01 blade 2 | -40.5874 | 49.41 | (0.0415, 0.0484, -5.3472) |
| P01 blade 3 | -80.5874 | 9.41 | (0.0629, 0.0105, -5.3472) |
| P01 blade 4 | -120.5874 | -30.59 | (0.0549, -0.0324, -5.3472) |
| P01 blade 5 | -160.5874 | -70.59 | (0.0212, -0.0601, -5.3472) |
| P01 blade 6 | 159.4126 | -110.59 | (-0.0224, -0.0597, -5.3472) |
| P01 blade 7 | 119.4126 | -150.59 | (-0.0556, -0.0313, -5.3472) |

For blade a: e1 = (-0.982976, 0.183736, 0), e2 = (-0.136543, -0.730499, 0.669124), n = (0.122942, 0.657732, 0.743151).
Seen from the front (+z), consecutive blades follow each other clockwise (ψ decreasing).

### 4.2 Plate (outer part, u from about 19.7 to the tip)

- **Upper surface** (the +w side): a circular cylinder whose axis is parallel to v and passes through (u, w) =
  (30.925, 93.407), radius **96.805**. So in any section v = const the upper surface is the arc
  w = 93.407 - sqrt(96.805² - (u - 30.925)²) (w = -3.398 at u = 30.925; the plate is concave towards +w).
- **Lower surface**: concentric cylinder, radius 97.555 (plate thickness **0.75**, constant).
- **Outline** (corners on the upper surface, local (u, v); side walls run through the thickness, normal to the plate):

  | Corner | u | v | note |
  |---|---|---|---|
  | G | 19.965 | -11.364 | root junction, south end |
  | A | 22.156 | -11.328 | G–A: short edge, v ≈ const |
  | B | 34.306 | -13.589 | A–B: straight trailing side |
  | D | 33.906 | 14.559 | B–D: tip, arc of the circle u² + v² = 36.903² (centre = local origin) |
  | E | 21.826 | 11.966 | D–E: straight side |
  | F | 19.719 | 11.932 | E–F: short edge, v ≈ const; F–G: straight junction line to the root |

  The tip wall is a true cylinder of radius **36.903** about the w axis (Ø73.806). The lower-surface corners lie 0.75
  below the upper ones along the plate normal (lower G, A, B, D, E, F: (19.945, -11.362), (22.088, -11.328),
  (34.315, -13.583), (33.914, 14.554), (21.755, 11.966), (19.699, 11.935)).

### 4.3 Root (u from 14.4 to the junction line F–G)

The root continues the plate inward but twists: its sections u = const are thin curved strips whose slope in the (v, w)
plane grows from 0 at the junction to about -31° at the inner end. Build it as a smooth (or finely ruled) loft through the
sections below, closed at both ends. In every section the upper and lower curves are given at seven evenly spaced v
values from v_south to v_north (v_i = v_south + i·(v_north - v_south)/6, i = 0…6); the section is closed by straight
lines at both ends.

| u | v_south | v_north | w upper (i = 0…6) | w lower (i = 0…6) |
|---|---|---|---|---|
| 15.25 | -11.802 | 8.361 | 5.091, 2.959, 0.922, -1.025, -2.887, -4.670, -6.377 | 4.165, 2.052, 0.033, -1.898, -3.744, -5.513, -7.206 |
| 15.50 | -11.894 | 8.602 | 4.675, 2.646, 0.708, -1.144, -2.915, -4.609, -6.231 | 3.766, 1.754, -0.167, -2.004, -3.760, -5.440, -7.048 |
| 16.00 | -12.040 | 9.074 | 3.839, 2.018, 0.280, -1.378, -2.961, -4.472, -5.914 | 2.958, 1.153, -0.570, -2.214, -3.783, -5.281, -6.710 |
| 16.50 | -12.135 | 9.531 | 2.994, 1.386, -0.145, -1.602, -2.989, -4.309, -5.565 | 2.137, 0.543, -0.974, -2.418, -3.792, -5.100, -6.345 |
| 17.00 | -12.176 | 9.965 | 2.141, 0.753, -0.565, -1.816, -3.003, -4.129, -5.197 | 1.304, -0.071, -1.376, -2.615, -3.791, -4.907, -5.965 |
| 17.50 | -12.167 | 10.384 | 1.295, 0.129, -0.975, -2.018, -3.002, -3.929, -4.800 | 0.476, -0.679, -1.772, -2.804, -3.777, -4.693, -5.554 |
| 18.00 | -12.105 | 10.786 | 0.449, -0.495, -1.380, -2.207, -2.978, -3.697, -4.364 | -0.360, -1.293, -2.166, -2.982, -3.742, -4.451, -5.109 |
| 18.50 | -11.986 | 11.153 | -0.405, -1.116, -1.773, -2.380, -2.940, -3.455, -3.929 | -1.202, -1.902, -2.549, -3.147, -3.698, -4.206, -4.672 |
| 19.00 | -11.830 | 11.484 | -1.215, -1.698, -2.138, -2.534, -2.888, -3.197, -3.461 | -2.003, -2.477, -2.908, -3.296, -3.640, -3.939, -4.192 |
| 19.50 | -11.603 | 11.847 | -2.060, -2.315, -2.521, -2.681, -2.798, -2.878, -2.928 | -2.852, -3.095, -3.290, -3.439, -3.547, -3.620, -3.663 |

End sections (non-planar, given by their corner points (u, v, w)):

- **Junction** (shared with the plate edge F–G): upper line from (19.965, -11.364, -2.762) to (19.719, 11.932, -2.761);
  lower line from (19.945, -11.362, -3.514) to (19.699, 11.935, -3.515). Both straight.
- **Inner end** (a flat-ish end wall, roughly normal to u): upper polyline (15.099, -11.729, 5.332) → (14.578, 4.751,
  -4.965) → (14.531, 8.021, -6.984); lower polyline (14.985, -12.093, 4.859) → (14.459, 4.243, -5.612) → (14.411,
  7.510, -7.683). The short north part of the inner end (v 4.2 … 8.0) is a small 0.12 mm step; a straight closing is
  acceptable.

The root's north and south side walls connect the section ends (north: F to the inner end at v ≈ 8.0; south: G to the
inner end at v ≈ -11.7 … -12.1). They are slightly curved; lofting through the table reproduces them within about
0.1 mm.

### 4.4 Blade checks (blade a, global frame)

- Volume 402.83 mm³, area 1200.87 mm², 16 faces in the reference (15 free-form + the tip cylinder).
- Global extent: x -37.1762 … -12.5444, y -8.0797 … 14.8614, z -17.4743 … 1.9035.
- The root reaches radius 14.7 from the z axis (inside the rotor); the tip reaches radius 37.18 (the bore is 38.333).

## 5. Fan body P01 (one solid)

Build P01 as the union of the items below; then cut the wire channel (5.7); then add the connector block and the leads
(5.7, 5.8). All edges are sharp unless a round is listed in 5.9.

### 5.1 Frame block

1. Square prism x -40 … 40, y -40 … 40, z -19 … 19; its four vertical corner edges rounded **R3.4** (centres at
   (±36.6, ±36.6)).
2. **Waist** between the two flanges: remove everything outside the following surface of revolution about the z axis, for
   -15 < z < 15: a cylinder **r = 41** from z = -15 to z = 10, then a concave round **R5** (centre circle r = 46,
   z = 10) rising from (r 41, z 10) to (r 46, z 15). At z = -15 the waist meets the rear flange with a sharp edge. Result:
   front flange z 15 … 19 and rear flange z -19 … -15 are full 80 x 80 squares; between them the outer wall is the
   flat side faces where |x| or |y| = 40 lies inside r = 41 (|y| < 9 on the x sides and vice versa), and the r = 41
   cylinder in the corners.
3. Exception, quadrant x > 0, y < -16.964 (south of the wire exit slot): there the R5 round is absent; the r = 41 waist
   runs straight up to the flange underside z = 15 with a sharp inner corner.
4. **Bore**: through cylinder **r = 38.3333 (Ø76.667)** from z = -19 to z = 14, and **r = 38.374 (Ø76.748)** from z = 14
   to z = 19 (a 0.04 mm step at z = 14).
5. **Mounting holes**: 4 x **Ø4.4** at (±35.75, ±35.75), through the front flange (z 15 … 19) and the rear flange
   (z -19 … -15) (they open into air between the flanges). Hole spacing **71.5** both ways. Front entry of each hole: a
   45° cone from Ø4.4 at z = 18.5 to Ø5.107 at z = 18.8536, blending tangentially into an R0.5 round that meets the front
   face at Ø5.814 (round centre circle r = 2.9071, z = 18.5). Rear hole edges sharp.

### 5.2 Spokes (front, 11 off)

Eleven curved spokes join the motor housing to the bore wall, occupying **z 14 … 19** (front face flush with the frame
front, flat underside at z = 14). Spoke k (k = 1 … 11) is the region

- inside the circle of radius **39.269** centred c1,k and outside the circle of radius **39.269** centred c2,k,
- between the motor housing (r = 22.2) and the bore wall (r = 38.374).

The centres lie on the circle r = 38.60994: c1,k at azimuth φk = -111.7944° + (k - 1)·32.72727°, c2,k at φk + 2.8087°.

| Spoke | φk (deg) | c1 (x, y) | c2 (x, y) |
|---|---|---|---|
| S1 | -111.7944 | (-14.3350, -35.8502) | (-12.5611, -36.5096) |
| S2 | -79.0671 | (7.3227, -37.9092) | (9.1715, -37.5048) |
| S3 | -46.3399 | (26.6555, -27.9323) | (27.9922, -26.5926) |
| S4 | -13.6126 | (37.5254, -9.0871) | (37.9256, -7.2374) |
| S5 | 19.1147 | (36.4812, 12.6432) | (35.8178, 14.4157) |
| S6 | 51.8420 | (23.8545, 30.3594) | (22.3382, 31.4918) |
| S7 | 84.5692 | (3.6542, 38.4366) | (1.7663, 38.5695) |
| S8 | 117.2965 | (-17.7063, 34.3105) | (-19.3663, 33.4017) |
| S9 | 150.0238 | (-33.4452, 19.2911) | (-34.3503, 17.6291) |
| S10 | 182.7511 | (-38.5654, -1.8531) | (-38.4283, -3.7407) |
| S11 | 215.4783 | (-31.4414, -22.4090) | (-30.3056, -23.9228) |

Each spoke is about 1.35 mm wide and 17.8 mm long; spoke S6 (the one at the wire exit) carries the north clamp jaw of 5.7.

### 5.3 Motor housing (stator side, front)

Cylinder **r = 22.2 (Ø44.4)** from z = 5.7 to z = 19 (front disc flush with the frame front face). Underside z = 5.7 is
flat.

### 5.4 Neck

Cylinder **r = 13.32 (Ø26.64)** from z = 4.55 to z = 5.7. It joins the housing to the rotor and leaves a
**1.15 mm** wide annular slot (z 4.55 … 5.7, r 13.32 … 22.2) between them.

### 5.5 Rotor (hub)

Solid of revolution: cylinder **r = 22.2** from z = 4.55 (flat top annulus) down to z = -9.5, then a rear round **R7.5**
(centre circle r = 14.7, z = -9.5) down to the flat rear disc **z = -17** (r ≤ 14.7). No recess, no shaft.

### 5.6 Blades on the rotor

The seven "P01 blade" positions of 4.1 carry blades of exactly the shape of section 4, united with the rotor (their root
parts inside the rotor disappear in the union; small slivers of root just outside r = 22.2 remain visible). The two
positions ψ = 79.4126° and 39.4126° are empty in P01 (filled by the separate solids P02-a, P02-b).

### 5.7 Wire exit: channel, clamp jaws, connector block

Use the rotated in-plane directions **a = (0.868926, -0.494942)** (azimuth -29.666°) and **b = (0.494942, 0.868926)**;
"a = 34.3075" means the plane {p : a·(px, py) = 34.3075}, etc.

1. **Wire channel** (cut through the full depth z -19 … 19): region b 1.1405 … 6.4919 (width **5.3514**), from the bore
   out to a = 39.3075 (outer end wall). In the xy plane its side walls run from the bore to the corner points
   (34.720, -18.464) and (37.368, -13.814).
2. **Exit slot** (full depth): region **y -16.9639 … -15.3139** (width **1.65**), from the channel end wall a = 39.3075
   out through the side face x = 40 (corner points (35.574, -16.964) and (36.514, -15.314) on the end wall). It splits
   the frame wall locally.
3. **North clamp jaw** (added, z **15 … 19**, inside the bore): the polygon (29.646, -8.480) → (28.079, -11.231) →
   (29.345, -11.231) → (30.793, -8.689) → (33.617, -10.297) → (33.024, -11.339) → (36.077, -13.078), closed along the
   bore wall r = 38.374 to (37.848, -6.332) and back along the south side arc of spoke S6 (circle centre (23.8545,
   30.3594), r 39.269). In a/b terms its walls are a = 29.9575, y = -11.2307, a = 31.0575, b = 7.6912, a = 34.3075,
   b = 6.4919 (the last continues as the channel's north wall).
4. **South clamp jaw** (added, z **15 … 19**): polygon (32.545, -20.332) → (25.259, -16.182) → (27.140, -12.881) →
   (28.406, -12.881) → (26.958, -15.423) → (29.782, -17.031) → (30.375, -15.989) → (33.894, -17.994), closed along the
   bore wall r = 38.374. Walls: b = -1.5588, a = 29.9575, y = -12.8807, a = 31.0575, b = -0.0588, a = 34.3075,
   b = 1.1405 (the last continues as the channel's south wall).
5. Between the jaws a pocket a 31.0575 … 34.3075, b -0.0588 … 7.6912 holds the **connector block**: a box
   a **31.2575 … 34.1075** (2.85), b **0.1912 … 7.4412** (7.25), z **15 … 19**, all edges sharp. It touches nothing
   but the two leads that pass through it (gaps 0.2 / 0.25 mm to the jaws), so it belongs to P01 only through the leads.

### 5.8 Lead wires (2 off, part of P01)

Two round rods **Ø1.25** (r = 0.625), each following a smooth centre line through the nodes below (fit a smooth
interpolating curve through all nodes except the last; the last segment is straight). Both start inside spoke S6 at the
motor housing (the start cap is buried and does not matter), run along direction a past the block (through it), turn down
in the channel and leave through the exit slot, then run straight out of the frame. The outer ends are flat caps whose
plane normal is (0.9073, -0.3959, -0.1418) through the last node.

W1 (lower lead, z 15.75 at the block): (20.678, -7.878, 15.75); (27.482, -11.753, 15.75); (28.899, -12.505, 15.932);
(33.952, -15.137, 16.732); (34.45, -15.40, 16.62); (34.736, -15.542, 16.112); (34.733, -15.542, 14.348);
(34.745, -15.547, 13.212); (35.106, -15.694, 11.767); (35.773, -15.965, 10.672); (36.677, -16.333, 9.842);
(37.978, -16.863, 9.266); (39.347, -17.419, 9.168); end (61.309, -26.366, 9.168).

W2 (upper lead, z 17.75 at the block): (20.678, -7.878, 17.75); (27.482, -11.753, 17.75); (28.899, -12.505, 17.932);
(33.952, -15.137, 18.732); (34.356, -15.346, 18.755); (35.141, -15.754, 18.562); (35.714, -16.052, 18.166);
(36.161, -16.282, 17.593); (36.454, -16.435, 16.771); (36.494, -16.457, 15.848); (36.491, -16.457, 14.052);
(36.521, -16.469, 13.204); (36.781, -16.575, 12.415); (37.226, -16.755, 11.821); (37.72, -16.958, 11.431);
(38.432, -17.247, 11.175); (39.535, -17.695, 11.140); end (61.497, -26.642, 11.140).

The straight outer runs are horizontal (z = 9.168 and 11.140), direction (0.9262, -0.3773, 0); the highest point of P01
is the top of W2 at z = 19.3847, the farthest point x = 61.7595.

### 5.9 Edge rounds

- **R0.5** on every edge of the front face z = 19: the outer square perimeter (with the R3.4 corners), the bore edge
  (r 38.374), both front edges of every spoke, the motor-housing front edge (r 22.2), all front edges of the clamp
  jaws, the channel and the exit slot. Not on the connector block.
- R0.5 hole-entry rounds as in 5.1-5.
- R5 waist round (5.1-2), R3.4 corners (5.1-1), R7.5 rotor rear round (5.5).
- Everything else sharp: the rear face z = -19 edges, the flange undersides, the spoke undersides at z = 14, the rotor
  top, the blades.

## 6. Target table (per body, mm)

| ID | Name | Vol cm3 | Vol mm3 | Area cm2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Fan body | 89.13450 | 89134.50 | 431.7341 | 43173.41 | 0.0934 | -0.0034 | 1.0403 | -40.0000 | 61.7595 | -40.0000 | 40.0000 | -19.0000 | 19.3847 | 363 |
| P02-a | Loose blade a | 0.40283 | 402.83 | 12.0087 | 1200.87 | -25.7967 | 2.5045 | -7.7537 | -37.1762 | -12.5444 | -8.0797 | 14.8614 | -17.4743 | 1.9035 | 16 |
| P02-b | Loose blade b | 0.40283 | 402.83 | 12.0087 | 1200.87 | -18.1515 | 18.5003 | -7.7537 | -32.0494 | -0.0997 | 4.3467 | 31.5473 | -17.4743 | 1.9035 | 16 |

Face counts are those of the reference and depend on how the free-form faces are split; they are for information.

## 7. Assembly totals and overlaps

- All 3 bodies: volume 89940.17 mm³, area 45575.16 mm², centre of mass (-0.1043, 0.0907, 0.9616), extent x -40 … 61.7595,
  y -40 … 40, z -19 … 19.3847.
- Intended overlaps (keep them): P02-a with P01 113.41 mm³, P02-b with P01 113.40 mm³ (blade roots inside the rotor).
  P02-a and P02-b do not overlap each other.

## 8. Undetermined and approximated

- Blade root (4.3): given as sections, not as an exact surface; a loft through them matches the reference within about
  0.1 mm (0.37 mm worst point at the inner-end step). Plate (4.2): the reference surfaces are free-form; the stated
  cylinders fit them within 0.0012 mm.
- Lead centre lines (5.8): measured nodes; the tight bends near the channel are approximate (about 0.5 mm worst).
- Wire start caps (buried) and the exact shape of the 0.12 mm step at the root inner end: undetermined, not needed.
- Mass, material grades, bearing, electrical details: not modelled.
