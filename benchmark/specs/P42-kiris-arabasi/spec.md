# Design specification: two-wheel-pair beam trolley (two 4 × 3 angles with four flanged wheels, two end bumper angles, bolted clamp hardware)

Rebuild the assembly below as **80 separate solids** in one STEP file, in the global frame given in §1. Every number is
measured on the reference model. Anything that could not be measured is listed in §7 as *undetermined*; do not invent it.

## 1. Units and global frame

- **Unit: inch.** All coordinates and sizes in this document are inches (1 in = 25.4 mm).
- **X** = length of the trolley (the long angles run from x = −23.5 to +23.5). **Y** = vertical, **+Y up** (wheels on top,
  bumper angles hang below). **Z** = across the trolley (the two long angles sit at z ≈ +3 … +6 and z ≈ −3 … −6).
- **Origin** at the centre of the assembly: the plane x = 0 is the middle of the long angles, the plane z = 0 the middle
  between them; y = 0 is 0.5 above the underside of the long angles' horizontal legs.
- Assembly bounding box: x −23.875 … +23.875, y −3.500 … +4.000, z −6.000 … +6.000.
- Do not move, re-centre or rotate anything: the result is compared with the reference **without alignment**.
- "Rotated 180° about Y" means the map (x, y, z) → (−x, y, −z).

## 2. Product description and source simplifications

A trolley that rides on a beam: two long steel angles (vertical leg up) carry two flanged wheels each on axles through
their vertical legs; the wheels stand between the angles. Two short angles bolted under the ends of the long angles form
the end bumpers. Four tapered square washers with longer bolts sit at the middle of the long angles (beam-flange clamp
points). All fasteners are 1/2 in.

Simplifications that are in the reference and must be kept:
- The axles and the bolts carry a **modelled helical thread** (1/2-13: 13 threads per inch, major Ø0.500, minor Ø0.400).
  The nuts have a **plain Ø0.500 hole** (no internal thread).
- No welds; the long angles' end stops are part of the angle solid.
- The trolley is modelled at one setting of its adjustable width (see §7: some catalogue "max" dimensions do not match).

## 3. Part list (80 solids, 11 distinct parts)

| Group | Count | Kind | Description |
|---|---|---|---|
| P01 | 2 | custom | long angle 4 × 3 × 1/4, 47.000 long, with end stops and holes |
| P02 | 2 | custom | end bumper angle 4 × 3 × 1/4, 12.000 long, with slots and holes |
| P03 | 4 | custom | flanged wheel, OD 4.000, tapered tread |
| P04 | 4 | custom | wheel bearing cover ring |
| H1 | 4 | hardware | wheel axle: Ø1.575 collar, 1.000 hex, Ø0.500 threaded stud |
| H2 | 16 | hardware | flat washer OD 1.203 / ID 0.500 / 0.121 thick |
| H3 | 16 | hardware | split lock washer OD 0.869 / ID 0.500 / 0.125 thick |
| H4 | 16 | hardware | hex nut 0.750 AF × 0.4375, plain Ø0.500 hole |
| H5 | 8 | hardware | hex bolt 1/2-13 × 2.0625 overall (0.750 AF head) |
| H6 | 4 | hardware | hex bolt 1/2-13 × 2.5625 overall |
| H7 | 4 | hardware | tapered square washer 1.250 × 1.250 |

Instance names (a, b, c …) and placements are in §5.

## 4. Part geometry (one instance each; §5 places them)

### 4.1 P01 Long angle (described for P01-a, the +Z one)

Cross-section in the YZ plane (constant along x from −23.5 to +23.5), closed loop:
(y 3.5000, z 3.0000) → (−0.5000, 3.0000) → (−0.5000, 6.0000) → arc R0.25 centre (−0.5000, 5.7500) through (−0.3232, 5.9268)
→ (−0.2500, 5.7500) → (−0.2500, 3.5000) → arc R0.25 centre (0.0000, 3.5000) through (−0.1768, 3.3232) → (0.0000, 3.2500) →
(3.2500, 3.2500) → arc R0.25 centre (3.2500, 3.0000) through (3.4268, 3.1768) → back to (3.5000, 3.0000).
So: vertical leg 4.000 tall (y −0.5 … 3.5) and 0.250 thick (z 3.00 … 3.25); horizontal leg 3.000 wide (z 3.0 … 6.0) and
0.250 thick (y −0.50 … −0.25); sharp outer heel at (y −0.5, z 3.0); inner root R0.25; both leg tips rounded R0.25 on the
inner side.

Holes:
- Vertical leg (along Z through the leg): Ø0.530 at (x, y) = (−18.00, 2.00), (+18.00, 2.00) (axle holes), (−12.50, 2.50),
  (+18.75, 2.50).
- Horizontal leg (along Y through the leg): Ø0.560 at z = 4.74 and x = −22.75, −20.50, −1.125, +1.125, +20.50, +22.75.

**End stops** (both ends, identical shape, P01-a): in the band y = 1.000 … 3.500 the vertical leg is replaced, near each end,
by a bent stop whose XZ cross-section (extruded along Y from y = 1.0 to y = 3.5) is:
- left end: (x −23.5000, z 3.0000) → (−23.5000, 3.2500) → (−21.9300, 3.2500) [this edge lies on the leg's outer face; the
  stop is united with the leg] … back along the inner side: (−21.9300, 3.0000) → (−21.9300, 1.6800) → arc R0.25 centre
  (−21.9300, 1.9300) through (−22.1068, 1.7532) → (−22.1800, 1.9300) → (−22.1800, 2.5000) → arc R0.25 centre (−22.4300,
  2.5000) through (−22.2532, 2.6768) → (−22.4300, 2.7500) → (−23.0000, 2.7500) → arc R0.25 centre (−23.0000, 3.0000)
  through (−23.1768, 2.8232) → (−23.2500, 3.0000) → (−23.5000, 3.0000).
- right end: the same shape translated by Δx = +45.18: (21.9300, 3.0000) … finger x 23.0000 … 23.2500 down to z = 1.6800,
  step at z 2.7500 between x 22.1800 and 22.7500, ending at (23.5000, 3.0000).
  Exact right-end loop: (23.5000, 3.0000) → (23.2500, 3.0000) → (23.2500, 1.6800) → arc R0.25 centre (23.2500, 1.9300)
  through (23.0732, 1.7532) → (23.0000, 1.9300) → (23.0000, 2.5000) → arc R0.25 centre (22.7500, 2.5000) through
  (22.9268, 2.6768) → (22.7500, 2.7500) → (22.1800, 2.7500) → arc R0.25 centre (22.1800, 3.0000) through (22.0032, 2.8232) →
  (21.9300, 3.0000).
So each stop is a 0.25-thick finger that drops 1.32 toward the wheels (to z = 1.68; its tip is a quarter round R0.25 centred on the finger's other edge) plus a 0.25-thick
block under the leg (z 2.75 … 3.0); the faces y = 1.0 and y = 3.5 bound it.

### 4.2 P02 End bumper angle (described for P02-a, the −X one)

Cross-section in the XY plane (constant along z from −6.000 to +6.000):
(x −23.8750, y −3.5000) → (−23.8750, −0.5000) → (−19.8750, −0.5000) → arc R0.25 centre (−20.1250, −0.5000) through
(−19.9482, −0.6768) → (−20.1250, −0.7500) → (−23.3750, −0.7500) → arc R0.25 centre (−23.3750, −1.0000) through
(−23.5518, −0.8232) → (−23.6250, −1.0000) → (−23.6250, −3.2500) → arc R0.25 centre (−23.8750, −3.2500) through
(−23.6982, −3.4268) → back to (−23.8750, −3.5000).
So: horizontal leg 4.000 (x −23.875 … −19.875, y −0.75 … −0.50), vertical leg 3.000 hanging down (y −3.5 … −0.5,
x −23.875 … −23.625), sharp heel at (−23.875, −0.5).
Holes in the horizontal leg (along Y), width 0.560:
- two slots on the +Z side, centre line from z = 0.000 to z = 4.740 (semicircular ends R0.28), at x = −22.75 and x = −20.50;
- two round holes Ø0.560 at z = −4.740, x = −22.75 and x = −20.50.

### 4.3 P03 Flanged wheel (described for P03-a: axis parallel to Z through (x −18, y 2), flange toward +Z)

Revolved about its axis; half profile (r = distance from the axis, z):
(0.7875, 1.9400) → (0.9375, 1.9400) → (0.9375, 2.1710) → (1.3750, 2.1710) → (1.3750, 1.9400) → (1.5083, 1.9400) → tread
cone to (1.5860, 2.5243) [half-angle 7.575° from the axis] → concave arc R0.16542 centre (1.7500, 2.5025) to (1.7014,
2.6606) → flange cone to (1.9559, 2.7389) [half-angle 72.897°] → convex arc R0.0625 centre (1.9375, 2.7987) to (2.0000,
2.7987) → (2.0000, 2.9400) → (1.7500, 2.9400) → arc R0.4375 centre (1.7500, 2.5025) to (1.3125, 2.5025) → (1.3125, 2.4210)
→ arc R0.0625 centre (1.2500, 2.4210) to (1.2500, 2.3585) → (1.0625, 2.3585) → arc R0.0625 centre (1.0625, 2.4210) to
(1.0000, 2.4210) → (1.0000, 2.6275) → arc R0.0625 centre (0.9375, 2.6275) to (0.9375, 2.6900) → (0.8500, 2.6900) → arc
R0.0625 centre (0.8500, 2.6275) to (0.7875, 2.6275) → back to (0.7875, 1.9400).
So: bore Ø1.575, inner face z = 1.94, outer face z = 2.94, a recess R0.9375 … R1.375 × 0.231 deep in the inner face
(holds P04), a toroidal recess (R0.4375) in the outer face, OD 4.000.

### 4.4 P04 Bearing cover ring (P04-a, same axis as P03-a)

Revolved; half profile (r, z): (1.3125, 1.9400) → (1.3125, 2.0460) → arc R0.0625 centre (1.2500, 2.0460) to (1.2500, 2.1085)
→ (1.0625, 2.1085) → arc R0.0625 centre (1.0625, 2.0460) to (1.0000, 2.0460) → (1.0000, 1.9400) → arc R0.0625 centre
(0.9375, 1.9400) to (0.9375, 1.8775) → (0.7875, 1.8775) → (0.7875, 1.9400) → (0.9375, 1.9400) → (0.9375, 2.1710) →
(1.3750, 2.1710) → (1.3750, 1.9400) → (1.5083, 1.9400) → (1.5000, 1.8775) → (1.3750, 1.8775) → arc R0.0625 centre
(1.3750, 1.9400) to back to (1.3125, 1.9400).
So P04 is a pressed shield 0.0625 thick with a U cross-section that opens toward −Z: inner wall R0.9375 … R1.0000 and
outer wall R1.3125 … R1.3750 rising to the closed top z 2.1085 … 2.1710 (inside corners R0.0625), plus an inner flange
R0.7875 … R0.9375 and an outer flange R1.3750 … R1.5083 at z 1.8775 … 1.9400 (the outer flange edge is the short cone from
R1.5000 at z 1.8775 to R1.5083 at z 1.9400). The U sits in the wheel's inner recess; the flanges lie on the wheel's inner face.

### 4.5 H1 Wheel axle (H1-a, axis parallel to Z through (−18, 2), pointing +Z)

Revolved, from the inner end: flat end face Ø0.835 at z = 1.8385; 55° cone (half-angle) out to Ø1.125 at z = 1.9400; flat
annular shoulder z = 1.9400 out to Ø1.575; collar Ø1.575 from z 1.9400 to 2.4120 (top face z = 2.412); hex 1.000 across flats
from z 2.4120 to 3.0000 (one pair of flats normal to X), top corners chamfered 30° to a Ø1.000 bearing circle at z = 3.000;
stud Ø0.500 from z 3.0000 to 4.3173, 45° chamfer to the end face Ø0.385 at z = 4.3750. Thread 1/2-13 modelled helically from
z = 3.25 to the end (minor Ø0.400).

### 4.6 H2 Flat washer

OD 1.2030, ID 0.5000, thickness 0.1210, plain.

### 4.7 H3 Split lock washer

OD 0.8690, ID 0.5000, thickness 0.1250, flat (no helix offset). It is cut by a 5° radial gap: one gap face is the plane
through the axis in the gap direction, the other is rotated 5° from it (gap directions per instance in §5).

### 4.8 H4 Hex nut

0.750 across flats (one pair of flats normal to the first in-plane axis given in §5), 0.4375 thick, plain Ø0.500 hole, both
faces chamfered 30° (cone half-angle 60°) down to a Ø0.750 bearing circle.

### 4.9 H5 / H6 Hex bolts (axis parallel to Y, head up)

Head 0.750 across flats (one pair of flats normal to X), from y = −0.2500 to +0.0625 (0.3125 tall), top corners chamfered 30°
(cone half-angle 60°) to a Ø0.750 circle at the top face, flat bearing face at y = −0.25. Shank Ø0.500 down to the end; end
chamfer 45° to an end face Ø0.385.
- H5: end at y = −2.0000; thread 1/2-13 from y = −0.75 to the end.
- H6: end at y = −2.5000; thread 1/2-13 from y = −1.00 to the end.

### 4.10 H7 Tapered square washer (H7-a, at (−1.125, z 4.74))

Square 1.250 × 1.250 in X and Z (x −1.750 … −0.500, z 4.115 … 5.365), flat bottom y = −1.125, top an inclined plane from
y = −0.781 at x = −1.750 down to y = −1.000 at x = −0.500 (slope 9.94°, falls toward +X, i.e. toward the trolley centre).
Hole Ø0.560 on the vertical axis through (−1.125, 4.74). The instances on the +X side fall toward −X (mirror in X).

## 5. Assembly and placements

All axes are parallel to the global axes. Every instance listed below is a separate solid.

**P01 / P02.** P01-a is the long angle of §4.1 (vertical leg z 3.00 … 3.25, horizontal leg toward +Z). P01-b = P01-a rotated 180° about Y (vertical leg z −3.25 … −3.00, horizontal leg toward −Z; its holes and end stops follow the rotation, e.g. its small Ø0.530 holes are at (x, y) = (+12.50, 2.50) and (−18.75, 2.50)). P02-a is the bumper angle of §4.2 (at −X); P02-b = P02-a rotated 180° about Y (at +X, vertical leg x 23.625 … 23.875, slots on the −Z side).

**P03 — flanged wheels (axis parallel to Z)**

| Instance | axis through (x, y) | z span | flange side |
|---|---|---|---|
| P03-a | (-18.000, 2.000) | 1.9400 … 2.9400 | +Z (as described) |
| P03-b | (-18.000, 2.000) | -2.9400 … -1.9400 | −Z (mirror of the described one in z = 0) |
| P03-c | (18.000, 2.000) | 1.9400 … 2.9400 | +Z (as described) |
| P03-d | (18.000, 2.000) | -2.9400 … -1.9400 | −Z (mirror of the described one in z = 0) |

Each P04 shield, H1 axle, wheel-side H2 washer, H3 lock washer and H4 nut shares its wheel's axis. On the −Z side everything is mirrored in z = 0 (the axle head is toward the trolley centre, the nut outside the long angle).

**P04 — bearing shields**

| Instance | axis through (x, y) | z span |
|---|---|---|
| P04-a | (-18.0000, 2.0000) | 1.8775 … 2.1710 |
| P04-b | (-18.0000, 2.0000) | -2.1710 … -1.8775 |
| P04-c | (18.0000, 2.0000) | 1.8775 … 2.1710 |
| P04-d | (18.0000, 2.0000) | -2.1710 … -1.8775 |

**H1 — wheel axles**

| Instance | axis through (x, y) | z span |
|---|---|---|
| H1-a | (-18.0000, 2.0000) | 1.8385 … 4.3750 |
| H1-b | (-18.0000, 2.0000) | -4.3750 … -1.8385 |
| H1-c | (18.0000, 2.0000) | 1.8385 … 4.3750 |
| H1-d | (18.0000, 2.0000) | -4.3750 … -1.8385 |

**H2 — flat washers**

| Instance | axis | span |
|---|---|---|
| H2-a | Y through (x -22.7500, z 4.7400) | y -0.8710 … -0.7500 |
| H2-b | Y through (x -22.7500, z -4.7400) | y -0.8710 … -0.7500 |
| H2-c | Y through (x -20.5000, z 4.7400) | y -0.8710 … -0.7500 |
| H2-d | Y through (x -20.5000, z -4.7400) | y -0.8710 … -0.7500 |
| H2-e | Z through (x -18.0000, y 2.0000) | z 3.2500 … 3.3710 |
| H2-f | Z through (x -18.0000, y 2.0000) | z -3.3710 … -3.2500 |
| H2-g | Y through (x -1.1250, z 4.7400) | y -1.2460 … -1.1250 |
| H2-h | Y through (x -1.1250, z -4.7400) | y -1.2460 … -1.1250 |
| H2-i | Y through (x 1.1250, z 4.7400) | y -1.2460 … -1.1250 |
| H2-j | Y through (x 1.1250, z -4.7400) | y -1.2460 … -1.1250 |
| H2-k | Z through (x 18.0000, y 2.0000) | z 3.2500 … 3.3710 |
| H2-l | Z through (x 18.0000, y 2.0000) | z -3.3710 … -3.2500 |
| H2-m | Y through (x 20.5000, z 4.7400) | y -0.8710 … -0.7500 |
| H2-n | Y through (x 20.5000, z -4.7400) | y -0.8710 … -0.7500 |
| H2-o | Y through (x 22.7500, z 4.7400) | y -0.8710 … -0.7500 |
| H2-p | Y through (x 22.7500, z -4.7400) | y -0.8710 … -0.7500 |

**H3 — split lock washers**

| Instance | axis | span | 5° gap |
|---|---|---|---|
| H3-a | Y through (x -22.7500, z 4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-b | Y through (x -22.7500, z -4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-c | Y through (x -20.5000, z 4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-d | Y through (x -20.5000, z -4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-e | Z through (x -18.0000, y 2.0000) | z 3.3710 … 3.4960 | between the directions +Y and 5° from +Y toward +X (one gap face is the plane x = -18 on the +Y side) |
| H3-f | Z through (x -18.0000, y 2.0000) | z -3.4960 … -3.3710 | between the directions +Y and 5° from +Y toward −X (one gap face is the plane x = -18 on the +Y side) |
| H3-g | Y through (x -1.1250, z 4.7400) | y -1.3710 … -1.2460 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-h | Y through (x -1.1250, z -4.7400) | y -1.3710 … -1.2460 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-i | Y through (x 1.1250, z 4.7400) | y -1.3710 … -1.2460 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-j | Y through (x 1.1250, z -4.7400) | y -1.3710 … -1.2460 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-k | Z through (x 18.0000, y 2.0000) | z 3.3710 … 3.4960 | between the directions +Y and 5° from +Y toward +X (one gap face is the plane x = 18 on the +Y side) |
| H3-l | Z through (x 18.0000, y 2.0000) | z -3.4960 … -3.3710 | between the directions +Y and 5° from +Y toward −X (one gap face is the plane x = 18 on the +Y side) |
| H3-m | Y through (x 20.5000, z 4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-n | Y through (x 20.5000, z -4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-o | Y through (x 22.7500, z 4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = 4.74 on the +X side and that plane turned 5° about the axis toward −Z) |
| H3-p | Y through (x 22.7500, z -4.7400) | y -0.9960 … -0.8710 | between the directions +X and 5° from +X toward −Z (gap faces: the plane z = -4.74 on the +X side and that plane turned 5° about the axis toward −Z) |

**H4 — hex nuts (one pair of flats normal to X)**

| Instance | axis | span |
|---|---|---|
| H4-a | Y through (x -22.7500, z 4.7400) | y -1.4335 … -0.9960 |
| H4-b | Y through (x -22.7500, z -4.7400) | y -1.4335 … -0.9960 |
| H4-c | Y through (x -20.5000, z 4.7400) | y -1.4335 … -0.9960 |
| H4-d | Y through (x -20.5000, z -4.7400) | y -1.4335 … -0.9960 |
| H4-e | Z through (x -18.0000, y 2.0000) | z 3.4960 … 3.9335 |
| H4-f | Z through (x -18.0000, y 2.0000) | z -3.9335 … -3.4960 |
| H4-g | Y through (x -1.1250, z 4.7400) | y -1.8085 … -1.3710 |
| H4-h | Y through (x -1.1250, z -4.7400) | y -1.8085 … -1.3710 |
| H4-i | Y through (x 1.1250, z 4.7400) | y -1.8085 … -1.3710 |
| H4-j | Y through (x 1.1250, z -4.7400) | y -1.8085 … -1.3710 |
| H4-k | Z through (x 18.0000, y 2.0000) | z 3.4960 … 3.9335 |
| H4-l | Z through (x 18.0000, y 2.0000) | z -3.9335 … -3.4960 |
| H4-m | Y through (x 20.5000, z 4.7400) | y -1.4335 … -0.9960 |
| H4-n | Y through (x 20.5000, z -4.7400) | y -1.4335 … -0.9960 |
| H4-o | Y through (x 22.7500, z 4.7400) | y -1.4335 … -0.9960 |
| H4-p | Y through (x 22.7500, z -4.7400) | y -1.4335 … -0.9960 |

**H5 — hex bolts 2.0625 (head up, one pair of head flats normal to X)**

| Instance | axis through (x, z) | y span |
|---|---|---|
| H5-a | (-22.7500, 4.7400) | -2.0000 … 0.0625 |
| H5-b | (-22.7500, -4.7400) | -2.0000 … 0.0625 |
| H5-c | (-20.5000, 4.7400) | -2.0000 … 0.0625 |
| H5-d | (-20.5000, -4.7400) | -2.0000 … 0.0625 |
| H5-e | (20.5000, 4.7400) | -2.0000 … 0.0625 |
| H5-f | (20.5000, -4.7400) | -2.0000 … 0.0625 |
| H5-g | (22.7500, 4.7400) | -2.0000 … 0.0625 |
| H5-h | (22.7500, -4.7400) | -2.0000 … 0.0625 |

**H6 — hex bolts 2.5625 (head up)**

| Instance | axis through (x, z) | y span |
|---|---|---|
| H6-a | (-1.1250, 4.7400) | -2.5000 … 0.0625 |
| H6-b | (-1.1250, -4.7400) | -2.5000 … 0.0625 |
| H6-c | (1.1250, 4.7400) | -2.5000 … 0.0625 |
| H6-d | (1.1250, -4.7400) | -2.5000 … 0.0625 |

**H7 — tapered washers (top falls toward the trolley centre x = 0)**

| Instance | hole axis through (x, z) | y span |
|---|---|---|
| H7-a | (-1.1250, 4.7400) | -1.1250 … -0.7810 |
| H7-b | (-1.1250, -4.7400) | -1.1250 … -0.7810 |
| H7-c | (1.1250, 4.7400) | -1.1250 … -0.7810 |
| H7-d | (1.1250, -4.7400) | -1.1250 … -0.7810 |

Stack order on the bumper bolts (top to bottom): bolt head on the long angle's horizontal leg (y −0.25), long angle leg, bumper angle leg (y −0.75 … −0.50), H2 washer y −0.871 … −0.750, H3 y −0.996 … −0.871, H4 y −1.4335 … −0.996. At the centre bolts: head, long-angle leg, H7 (y −1.125 … −0.781/−1.000), H2 y −1.246 … −1.125, H3 y −1.371 … −1.246, H4 y −1.8085 … −1.371. Wheel side: wheel z 1.94 … 2.94, long-angle leg z 3.00 … 3.25, H2 z 3.250 … 3.371, H3 z 3.371 … 3.496, H4 z 3.496 … 3.9335 (mirrored on −Z).

Interference: no two bodies overlap (all 172 touching pairs have zero common volume); washers, nuts, heads and legs touch face to face.

## 6. Acceptance targets

Per body (inch; V in in³ and mm³, A in in² and mm², CoM in inch, bbox in inch, F = reference face count):

| Body | Description | V in³ | V mm³ | A in² | A mm² | CoM x | CoM y | CoM z | xmin | xmax | ymin | ymax | zmin | zmax | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-a | Wheel axle (collar + hex + 1/2-13 stud) | 1.73309 | 28400.24 | 11.4392 | 7380.10 | -18.0000 | 2.0000 | 2.5144 | -18.7875 | -17.2125 | 1.2125 | 2.7875 | 1.8385 | 4.3750 | 57 |
| H1-b | Wheel axle (collar + hex + 1/2-13 stud) | 1.73309 | 28400.24 | 11.4392 | 7380.10 | -18.0000 | 2.0000 | -2.5144 | -18.7875 | -17.2125 | 1.2125 | 2.7875 | -4.3750 | -1.8385 | 57 |
| H1-c | Wheel axle (collar + hex + 1/2-13 stud) | 1.73309 | 28400.24 | 11.4392 | 7380.10 | 18.0000 | 2.0000 | 2.5144 | 17.2125 | 18.7875 | 1.2125 | 2.7875 | 1.8385 | 4.3750 | 57 |
| H1-d | Wheel axle (collar + hex + 1/2-13 stud) | 1.73309 | 28400.24 | 11.4392 | 7380.10 | 18.0000 | 2.0000 | -2.5144 | 17.2125 | 18.7875 | 1.2125 | 2.7875 | -4.3750 | -1.8385 | 57 |
| H2-a | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -22.7500 | -0.8105 | 4.7400 | -23.3515 | -22.1485 | -0.8710 | -0.7500 | 4.1385 | 5.3415 | 6 |
| H2-b | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -22.7500 | -0.8105 | -4.7400 | -23.3515 | -22.1485 | -0.8710 | -0.7500 | -5.3415 | -4.1385 | 6 |
| H2-c | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -20.5000 | -0.8105 | 4.7400 | -21.1015 | -19.8985 | -0.8710 | -0.7500 | 4.1385 | 5.3415 | 6 |
| H2-d | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -20.5000 | -0.8105 | -4.7400 | -21.1015 | -19.8985 | -0.8710 | -0.7500 | -5.3415 | -4.1385 | 6 |
| H2-e | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -18.0000 | 2.0000 | 3.3105 | -18.6015 | -17.3985 | 1.3985 | 2.6015 | 3.2500 | 3.3710 | 6 |
| H2-f | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -18.0000 | 2.0000 | -3.3105 | -18.6015 | -17.3985 | 1.3985 | 2.6015 | -3.3710 | -3.2500 | 6 |
| H2-g | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -1.1250 | -1.1855 | 4.7400 | -1.7265 | -0.5235 | -1.2460 | -1.1250 | 4.1385 | 5.3415 | 6 |
| H2-h | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | -1.1250 | -1.1855 | -4.7400 | -1.7265 | -0.5235 | -1.2460 | -1.1250 | -5.3415 | -4.1385 | 6 |
| H2-i | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 1.1250 | -1.1855 | 4.7400 | 0.5235 | 1.7265 | -1.2460 | -1.1250 | 4.1385 | 5.3415 | 6 |
| H2-j | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 1.1250 | -1.1855 | -4.7400 | 0.5235 | 1.7265 | -1.2460 | -1.1250 | -5.3415 | -4.1385 | 6 |
| H2-k | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 18.0000 | 2.0000 | 3.3105 | 17.3985 | 18.6015 | 1.3985 | 2.6015 | 3.2500 | 3.3710 | 6 |
| H2-l | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 18.0000 | 2.0000 | -3.3105 | 17.3985 | 18.6015 | 1.3985 | 2.6015 | -3.3710 | -3.2500 | 6 |
| H2-m | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 20.5000 | -0.8105 | 4.7400 | 19.8985 | 21.1015 | -0.8710 | -0.7500 | 4.1385 | 5.3415 | 6 |
| H2-n | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 20.5000 | -0.8105 | -4.7400 | 19.8985 | 21.1015 | -0.8710 | -0.7500 | -5.3415 | -4.1385 | 6 |
| H2-o | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 22.7500 | -0.8105 | 4.7400 | 22.1485 | 23.3515 | -0.8710 | -0.7500 | 4.1385 | 5.3415 | 6 |
| H2-p | Flat washer OD 1.203 | 0.11377 | 1864.43 | 2.5279 | 1630.92 | 22.7500 | -0.8105 | -4.7400 | 22.1485 | 23.3515 | -0.8710 | -0.7500 | -5.3415 | -4.1385 | 6 |
| H3-a | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -22.7549 | -0.9335 | 4.7402 | -23.1845 | -22.3155 | -0.9960 | -0.8710 | 4.3055 | 5.1745 | 10 |
| H3-b | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -22.7549 | -0.9335 | -4.7398 | -23.1845 | -22.3155 | -0.9960 | -0.8710 | -5.1745 | -4.3055 | 10 |
| H3-c | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -20.5049 | -0.9335 | 4.7402 | -20.9345 | -20.0655 | -0.9960 | -0.8710 | 4.3055 | 5.1745 | 10 |
| H3-d | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -20.5049 | -0.9335 | -4.7398 | -20.9345 | -20.0655 | -0.9960 | -0.8710 | -5.1745 | -4.3055 | 10 |
| H3-e | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -18.0002 | 1.9951 | 3.4335 | -18.4345 | -17.5655 | 1.5655 | 2.4345 | 3.3710 | 3.4960 | 10 |
| H3-f | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -17.9998 | 1.9951 | -3.4335 | -18.4345 | -17.5655 | 1.5655 | 2.4345 | -3.4960 | -3.3710 | 10 |
| H3-g | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -1.1299 | -1.3085 | 4.7402 | -1.5595 | -0.6905 | -1.3710 | -1.2460 | 4.3055 | 5.1745 | 8 |
| H3-h | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | -1.1299 | -1.3085 | -4.7398 | -1.5595 | -0.6905 | -1.3710 | -1.2460 | -5.1745 | -4.3055 | 8 |
| H3-i | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 1.1201 | -1.3085 | 4.7402 | 0.6905 | 1.5595 | -1.3710 | -1.2460 | 4.3055 | 5.1745 | 8 |
| H3-j | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 1.1201 | -1.3085 | -4.7398 | 0.6905 | 1.5595 | -1.3710 | -1.2460 | -5.1745 | -4.3055 | 8 |
| H3-k | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 17.9998 | 1.9951 | 3.4335 | 17.5655 | 18.4345 | 1.5655 | 2.4345 | 3.3710 | 3.4960 | 10 |
| H3-l | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 18.0002 | 1.9951 | -3.4335 | 17.5655 | 18.4345 | 1.5655 | 2.4345 | -3.4960 | -3.3710 | 10 |
| H3-m | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 20.4951 | -0.9335 | 4.7402 | 20.0655 | 20.9345 | -0.9960 | -0.8710 | 4.3055 | 5.1745 | 10 |
| H3-n | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 20.4951 | -0.9335 | -4.7398 | 20.0655 | 20.9345 | -0.9960 | -0.8710 | -5.1745 | -4.3055 | 10 |
| H3-o | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 22.7451 | -0.9335 | 4.7402 | 22.3155 | 23.1845 | -0.9960 | -0.8710 | 4.3055 | 5.1745 | 10 |
| H3-p | Split lock washer OD 0.869 | 0.04891 | 801.41 | 1.3587 | 876.61 | 22.7451 | -0.9335 | -4.7398 | 22.3155 | 23.1845 | -0.9960 | -0.8710 | -5.1745 | -4.3055 | 10 |
| H4-a | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -22.7500 | -1.2148 | 4.7400 | -23.1250 | -22.3750 | -1.4335 | -0.9960 | 4.3070 | 5.1730 | 24 |
| H4-b | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -22.7500 | -1.2148 | -4.7400 | -23.1250 | -22.3750 | -1.4335 | -0.9960 | -5.1730 | -4.3070 | 24 |
| H4-c | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -20.5000 | -1.2148 | 4.7400 | -20.8750 | -20.1250 | -1.4335 | -0.9960 | 4.3070 | 5.1730 | 24 |
| H4-d | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -20.5000 | -1.2148 | -4.7400 | -20.8750 | -20.1250 | -1.4335 | -0.9960 | -5.1730 | -4.3070 | 24 |
| H4-e | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -18.0000 | 2.0000 | 3.7148 | -18.3750 | -17.6250 | 1.5670 | 2.4330 | 3.4960 | 3.9335 | 22 |
| H4-f | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -18.0000 | 2.0000 | -3.7148 | -18.3750 | -17.6250 | 1.5670 | 2.4330 | -3.9335 | -3.4960 | 22 |
| H4-g | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -1.1250 | -1.5898 | 4.7400 | -1.5000 | -0.7500 | -1.8085 | -1.3710 | 4.3070 | 5.1730 | 22 |
| H4-h | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | -1.1250 | -1.5898 | -4.7400 | -1.5000 | -0.7500 | -1.8085 | -1.3710 | -5.1730 | -4.3070 | 22 |
| H4-i | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 1.1250 | -1.5898 | 4.7400 | 0.7500 | 1.5000 | -1.8085 | -1.3710 | 4.3070 | 5.1730 | 22 |
| H4-j | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 1.1250 | -1.5898 | -4.7400 | 0.7500 | 1.5000 | -1.8085 | -1.3710 | -5.1730 | -4.3070 | 22 |
| H4-k | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 18.0000 | 2.0000 | 3.7148 | 17.6250 | 18.3750 | 1.5670 | 2.4330 | 3.4960 | 3.9335 | 22 |
| H4-l | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 18.0000 | 2.0000 | -3.7148 | 17.6250 | 18.3750 | 1.5670 | 2.4330 | -3.9335 | -3.4960 | 22 |
| H4-m | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 20.5000 | -1.2148 | 4.7400 | 20.1250 | 20.8750 | -1.4335 | -0.9960 | 4.3070 | 5.1730 | 24 |
| H4-n | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 20.5000 | -1.2148 | -4.7400 | 20.1250 | 20.8750 | -1.4335 | -0.9960 | -5.1730 | -4.3070 | 24 |
| H4-o | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 22.7500 | -1.2148 | 4.7400 | 22.3750 | 23.1250 | -1.4335 | -0.9960 | 4.3070 | 5.1730 | 24 |
| H4-p | Hex nut 1/2-13, 3/4 AF | 0.12630 | 2069.75 | 2.3598 | 1522.44 | 22.7500 | -1.2148 | -4.7400 | 22.3750 | 23.1250 | -1.4335 | -0.9960 | -5.1730 | -4.3070 | 24 |
| H5-a | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | -22.7499 | -0.7495 | 4.7401 | -23.1250 | -22.3750 | -2.0000 | 0.0625 | 4.3070 | 5.1730 | 88 |
| H5-b | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | -22.7499 | -0.7495 | -4.7399 | -23.1250 | -22.3750 | -2.0000 | 0.0625 | -5.1730 | -4.3070 | 88 |
| H5-c | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | -20.4999 | -0.7495 | 4.7401 | -20.8750 | -20.1250 | -2.0000 | 0.0625 | 4.3070 | 5.1730 | 88 |
| H5-d | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | -20.4999 | -0.7495 | -4.7399 | -20.8750 | -20.1250 | -2.0000 | 0.0625 | -5.1730 | -4.3070 | 88 |
| H5-e | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | 20.5001 | -0.7495 | 4.7401 | 20.1250 | 20.8750 | -2.0000 | 0.0625 | 4.3070 | 5.1730 | 88 |
| H5-f | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | 20.5001 | -0.7495 | -4.7399 | 20.1250 | 20.8750 | -2.0000 | 0.0625 | -5.1730 | -4.3070 | 88 |
| H5-g | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | 22.7501 | -0.7495 | 4.7401 | 22.3750 | 23.1250 | -2.0000 | 0.0625 | 4.3070 | 5.1730 | 88 |
| H5-h | Hex bolt 1/2-13 x 2.0625 | 0.44903 | 7358.30 | 5.5759 | 3597.37 | 22.7501 | -0.7495 | -4.7399 | 22.3750 | 23.1250 | -2.0000 | 0.0625 | -5.1730 | -4.3070 | 88 |
| H6-a | Hex bolt 1/2-13 x 2.5625 | 0.53961 | 8842.62 | 6.5284 | 4211.83 | -1.1248 | -0.9745 | 4.7403 | -1.5000 | -0.7500 | -2.5000 | 0.0625 | 4.3070 | 5.1730 | 60 |
| H6-b | Hex bolt 1/2-13 x 2.5625 | 0.53961 | 8842.62 | 6.5284 | 4211.83 | -1.1248 | -0.9745 | -4.7397 | -1.5000 | -0.7500 | -2.5000 | 0.0625 | -5.1730 | -4.3070 | 60 |
| H6-c | Hex bolt 1/2-13 x 2.5625 | 0.53961 | 8842.62 | 6.5284 | 4211.83 | 1.1252 | -0.9745 | 4.7403 | 0.7500 | 1.5000 | -2.5000 | 0.0625 | 4.3070 | 5.1730 | 60 |
| H6-d | Hex bolt 1/2-13 x 2.5625 | 0.53961 | 8842.62 | 6.5284 | 4211.83 | 1.1252 | -0.9745 | -4.7397 | 0.7500 | 1.5000 | -2.5000 | 0.0625 | -5.1730 | -4.3070 | 60 |
| H7-a | Tapered square washer 1.25 | 0.30865 | 5057.87 | 4.2375 | 2733.89 | -1.2377 | -0.9979 | 4.7400 | -1.7500 | -0.5000 | -1.1250 | -0.7810 | 4.1150 | 5.3650 | 8 |
| H7-b | Tapered square washer 1.25 | 0.30865 | 5057.87 | 4.2375 | 2733.89 | -1.2377 | -0.9979 | -4.7400 | -1.7500 | -0.5000 | -1.1250 | -0.7810 | -5.3650 | -4.1150 | 8 |
| H7-c | Tapered square washer 1.25 | 0.30865 | 5057.87 | 4.2375 | 2733.89 | 1.2377 | -0.9979 | 4.7400 | 0.5000 | 1.7500 | -1.1250 | -0.7810 | 4.1150 | 5.3650 | 8 |
| H7-d | Tapered square washer 1.25 | 0.30865 | 5057.87 | 4.2375 | 2733.89 | 1.2377 | -0.9979 | -4.7400 | 0.5000 | 1.7500 | -1.1250 | -0.7810 | -5.3650 | -4.1150 | 8 |
| P01-a | Side angle 4 x 3 x 1/4, 47 long | 81.01247 | 1327556.60 | 659.7290 | 425630.77 | 0.0050 | 0.7714 | 3.6758 | -23.5000 | 23.5000 | -0.5000 | 3.5000 | 1.6800 | 6.0000 | 45 |
| P01-b | Side angle 4 x 3 x 1/4, 47 long | 81.01247 | 1327556.60 | 659.7290 | 425630.77 | -0.0050 | 0.7714 | -3.6758 | -23.5000 | 23.5000 | -0.5000 | 3.5000 | -6.0000 | -1.6800 | 45 |
| P02-a | End bumper angle 4 x 3 x 1/4, 12 long | 18.51555 | 303415.47 | 161.3966 | 104126.65 | -22.7476 | -1.2698 | -0.1541 | -23.8750 | -19.8750 | -3.5000 | -0.5000 | -6.0000 | 6.0000 | 23 |
| P02-b | End bumper angle 4 x 3 x 1/4, 12 long | 18.51555 | 303415.47 | 161.3966 | 104126.65 | 22.7476 | -1.2698 | 0.1541 | 19.8750 | 23.8750 | -3.5000 | -0.5000 | -6.0000 | 6.0000 | 23 |
| P03-a | Flanged wheel OD 4.000 | 4.19968 | 68820.43 | 41.0978 | 26514.64 | -18.0000 | 2.0000 | 2.4988 | -20.0000 | -16.0000 | 0.0000 | 4.0000 | 1.9400 | 2.9400 | 36 |
| P03-b | Flanged wheel OD 4.000 | 4.19968 | 68820.43 | 41.0978 | 26514.64 | -18.0000 | 2.0000 | -2.4988 | -20.0000 | -16.0000 | 0.0000 | 4.0000 | -2.9400 | -1.9400 | 36 |
| P03-c | Flanged wheel OD 4.000 | 4.19968 | 68820.43 | 41.0978 | 26514.64 | 18.0000 | 2.0000 | 2.4988 | 16.0000 | 20.0000 | 0.0000 | 4.0000 | 1.9400 | 2.9400 | 36 |
| P03-d | Flanged wheel OD 4.000 | 4.19968 | 68820.43 | 41.0978 | 26514.64 | 18.0000 | 2.0000 | -2.4988 | 16.0000 | 20.0000 | 0.0000 | 4.0000 | -2.9400 | -1.9400 | 36 |
| P04-a | Wheel bearing cover ring | 0.53225 | 8721.96 | 17.1576 | 11069.37 | -18.0000 | 2.0000 | 2.0329 | -19.5083 | -16.4917 | 0.4917 | 3.5083 | 1.8775 | 2.1710 | 26 |
| P04-b | Wheel bearing cover ring | 0.53225 | 8721.96 | 17.1576 | 11069.37 | -18.0000 | 2.0000 | -2.0329 | -19.5083 | -16.4917 | 0.4917 | 3.5083 | -2.1710 | -1.8775 | 26 |
| P04-c | Wheel bearing cover ring | 0.53225 | 8721.96 | 17.1576 | 11069.37 | 18.0000 | 2.0000 | 2.0329 | 16.4917 | 19.5083 | 0.4917 | 3.5083 | 1.8775 | 2.1710 | 26 |
| P04-d | Wheel bearing cover ring | 0.53225 | 8721.96 | 17.1576 | 11069.37 | 18.0000 | 2.0000 | -2.0329 | 16.4917 | 19.5083 | 0.4917 | 3.5083 | -2.1710 | -1.8775 | 26 |

Assembly: V = 236.5251 in³ (3 875 952.55 mm³), A = 2108.6441 in² (1 360 412.82 mm²), CoM (0.0000, 0.5160, 0.0000), bbox x −23.875 … 23.875, y −3.500 … 4.000, z −6.000 … 6.000.

## 7. Source conflicts and undetermined items

- Thread start angle (phase) of the modelled helical threads on H1, H5, H6: undetermined; the count, pitch, diameters and
  lengths are given.
- The catalogue drawing gives "9.48 in Max" and "3.36 in Max" for adjustable widths; the model is built at a wider setting
  (long angles 6.000 apart at their vertical legs). Follow the model.
- The wheels' tread taper (7.575°) and flange cone (72.897°) are measured values, not catalogue data.
