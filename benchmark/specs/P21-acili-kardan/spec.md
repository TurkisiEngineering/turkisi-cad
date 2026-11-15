# Design specification: geared single universal joint, extreme-angle (P21)

A single universal joint whose two yokes carry meshing crown-type gear rings instead of a cross. Each yoke is one solid:
a tubular shaft end with a blind bore for a 1/2 in shaft, a flared ruled-surface yoke shell, three hinge knuckles on a
common pivot axis, and a gear core with 15 round-crowned teeth. The two yokes are the **same design**: yoke Y2 is yoke
Y1 turned half a turn about the joint and swung 3 degrees about the pivot axis, with two small differences at the pin
end (section 5). The master is two solids. This document is the only source for the rebuild. Every value was measured
from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. Millimetre values in brackets are exact conversions (1 in = 25.4 mm). Where a
  value is not a round inch figure, both are given; use the millimetre value when in doubt.
- **Global frame (use exactly, no realignment):**
  - **Yoke Y1's shaft axis is the X axis**; its shaft end points to **-X** (end face x = -5.125). The gear teeth of Y1
    face **+X**.
  - **Pivot axis** (common hinge axis of both yokes): the line **x = 0, z = -0.5625**, parallel to **Y**.
  - The knuckle end faces are the planes y = +1.375 and y = -1.375 (overall height 2.75 along Y).
  - Yoke Y2's shaft points to +X, tilted 3 deg downward (section 5).
- "(x, r) profile" = closed profile in a half plane containing the X axis of Y1, r = distance from the X axis,
  revolved 360 deg about the X axis.
- "phi" = angle about the X axis in the YZ plane, **measured from +Y toward +Z** (phi = 0 on +Y, phi = 90 on +Z).
- Everything in sections 3 and 4 is written in Y1's own position. Y2 is built by the rigid motion of section 5.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| Y1 | 1 | Yoke with gear ring, shaft along -X | custom |
| Y2 | 1 | Same yoke, mirrored position (rotated copy), shaft along +X, swung 3 deg | custom (same design as Y1, two pin-end details differ) |

No pin, side links or fasteners are modelled: the knuckles are solid discs, and the pin is only suggested by a shallow
ring groove and a hex socket on the outermost knuckle face of each yoke. The two yokes interleave: their knuckles
alternate along Y without overlap, and their gear rings mesh near the origin. The master's two solids overlap slightly
(about 70.7 mm3, mostly where the two flat front faces of the yoke shells cross each other near the top, plus small tooth
contacts); keep the geometry as specified, do not trim one against the other.

## 3. Yoke Y1: shaft end, shell, knuckles

### F1. Shaft end (revolved), (x, r) profile, closed, revolved about X

1. (-5.125, 0.25) to (-5.125, 0.345) (shaft end face, annulus)
2. line to (-5.095, 0.375) (0.03 x 45 deg end chamfer)
3. line to (-3.405, 0.375) (shaft end, **diameter 0.75**)
4. line to (-3.375, 0.345) (45 deg relief cone: the radius **decreases** by 0.03 toward +X)
5. line to (-3.375, 0.4125) (step face, facing -X)
6. line to (-1.175, 0.4125) (hub, **diameter 0.825**)
7. line to (-1.175, 0) (this face continues outward as the base of the shell, F2: the shell base circle has radius 0.4425,
   so a step face x = -1.175 from r 0.4125 to 0.4425 shows, facing -X)
8. close back along the axis to x = -4.0, then line to (-4.0, 0.25) and to the start: **blind bore diameter 0.5,
   depth 1.125** (flat floor at x = -4.0, no drill point, no chamfer at the mouth).

### F2. Yoke shell: ruled loft

The outer surface of the shell is a **ruled surface** (straight-line loft) between two closed curves:

- **Base curve A**: circle of **radius 0.4425** [11.2395 mm] in the plane **x = -1.175** [-29.845 mm], centred on the
  X axis.
- **Far curve B**, in the plane **x = 0.1** [2.54 mm] (beyond the part; the loft is trimmed long before it), coordinates
  (y, z):
  - C1 = (1.671182, -0.53125) [42.44802, -13.49375]
  - C2 = (-1.344441, -0.53125) [-34.14880, -13.49375]
  - C3 = (-1.344441, -0.84375) [-34.14880, -21.43125]
  - C4 = (1.671182, -0.84375) [42.44802, -21.43125]
  - TA = (0.615116, 0.582999) [15.62396, 14.80817], TB = (-0.714403, 0.455943) [-18.14585, 11.58095]
  - Curve B runs C1 -> straight line -> TA -> **circular arc radius 0.8475** [21.5265 mm] centred on the X axis, over
    the top through (0, 0.8475) -> TB -> straight line -> C2 -> straight line -> C3 -> straight line (bottom) -> C4 ->
    straight line -> C1. The two upper lines are tangent to the arc at TA and TB. B is not symmetric about y = 0.
- **Correspondence (which point of A is joined to which point of B).** A is split at six points, given by phi on the
  circle of radius 0.4425; each arc of A is joined to one segment of B, and within each pair points are matched by
  equal fractions of length (A by angle, B by arc length):

| A from phi | to phi | B segment |
|---|---|---|
| -9.7977 | 58.0138 | C1 -> TA (line) |
| 58.0138 | 138.3955 | TA -> TB (arc R0.8475) |
| 138.3955 | 190.7806 | TB -> C2 (line) |
| 190.7806 | 202.2100 | C2 -> C3 (line) |
| 202.2100 | 339.6805 | C3 -> C4 (bottom line) |
| 339.6805 | 350.2023 (= -9.7977) | C4 -> C1 (line) |

  (The split points on A are at (y, z) = (0.436047, -0.075299), (0.234399, 0.375318), (-0.330878, 0.293813),
  (-0.434689, -0.082768), (-0.409669, -0.167268), (0.414965, -0.153661) in inch.) The ruled surface is a smooth single
  surface across TA and TB; it has four sharp corner edges (rulings) A(-9.7977)-C1, A(190.7806)-C2, A(202.21)-C3,
  A(339.6805)-C4, which are rounded in F6.
- The solid is the volume enclosed by the ruled surface between x = -1.175 and x = 0.1, closed by the two end planes.

### F3. Trims and cuts of the shell (applied to the F2 solid only)

1. **Front face:** keep only the side x <= tan(1.5 deg) * (z + 0.875). This plane contains the line x = 0, z = -0.875
   (parallel to Y) and leans 1.5 deg so that it moves to +X as z increases (at z = 0.7 it is at x = 0.04124).
2. **Y limits:** keep only -1.145 <= y <= 1.375.
3. **Central cavity** (revolved about X), remove: for x >= -0.882772 [-22.4224 mm], everything with r < r_cav(x), where
   r_cav = 0.25 + (x + 0.882772) * tan(30 deg) up to x = -0.125 (a cone of 30 deg half angle opening toward +X, r 0.25
   at x = -0.882772, r 0.6875 at x = -0.125), and r_cav = **0.6875** (bore diameter 1.375) from x = -0.125 to the front.
4. **Clearance slots for the other yoke's knuckles,** in the two Y bands **-0.915 < y < 0.685** and **0.915 < y < 1.145**
   only. In the XZ view the slot outline is a circle of **radius 0.3375** about the pivot axis (x = 0, z = -0.5625)
   swept along the direction (-1, 0, -1) (45 deg down and toward -X): remove every point within 0.3375 of the pivot
   axis, plus every point within 0.3375 of the ray that starts on the pivot axis and runs in the direction (-1, 0, -1)
   (the band between the two lines z = x - 0.085203 and z = x - 1.039797, on the -X/-Z side of the pivot). The upper flat
   of the slot is the plane z = x - 0.085203 [x - 2.16416 mm], tangent to the R0.3375 circle at (x, z) = (-0.238648,
   -0.323852). Walls of the slots are the planes y = -0.915, 0.685, 0.915, 1.145.

### F4. Knuckles (united after F3)

Three solid discs, **diameter 0.625** (radius 0.3125), coaxial with the pivot axis (x = 0, z = -0.5625), between the
planes:
- y = 0.685 to 0.915,
- y = 1.145 to 1.375 (outermost, carries the pin-end details F8),
- y = -1.145 to -0.915.

Each disc is united with the shell; nothing else is added at the knuckles (the slot cuts of F3 do not touch them).

### F5. Gear core (revolved, united), (x, r) profile, closed

(-0.882772, 0) -> (-0.882772, 0.25) -> (-0.624264, 0.25) [-15.8563 mm] -> line (30 deg cone) to (-0.125, 0.53825)
[13.67155 mm] -> (-0.066, 0.53825) -> (-0.066, 0) -> close along the axis.

The core and the shell are joined only through the neck r <= 0.25 at x <= -0.624264; between the core cone and the
cavity cone (both 30 deg) a conical slot of constant width 0.129 [3.283 mm] remains open toward +X (the other yoke's gear
ring swings into it). The core front face is the plane **x = -0.066** [-1.6764 mm].

**Ring groove in the core front face:** an annular groove between r = 0.21375 and r = 0.21875 (width 0.005), floor at
x = -0.126 (depth 0.06), with 45 deg chamfers at its mouth: outer edge from (x, r) = (-0.086, 0.21875) to
(-0.066, 0.23875); inner edge from (-0.076, 0.21375) to (-0.066, 0.20375).

### F6. Rounds of the shell

- **R0.09** [2.286 mm] constant-radius round along the edge where the front face (F3.1) meets the upper ruled surface
  (the part generated by A from phi -9.7977 to 190.7806), from the top of the -Y knuckle to the top of the +Y knuckle
  (it ends where that edge meets the knuckle discs).
- **R0.12** [3.048 mm] constant-radius rounds on the four corner rulings of F2 (A(-9.7977)-C1, A(190.7806)-C2,
  A(202.21)-C3, A(339.6805)-C4). Each round fades to zero width at the base circle A, where the adjoining surfaces are
  tangent, and runs to where the ruling leaves the solid.
- All other edges of Y1 are sharp.

## 4. Yoke Y1: gear teeth

**15 teeth**, equally spaced, pitch 24 deg, standing on the core around the X axis and facing +X. Tooth k (k = 0..14)
is centred at **phi = 24 k deg**, so **tooth 0 is centred on +Y** (phi = 0) and there is a tooth space centred on -Y.

**Tooth flanks:** both flanks of every tooth are planes **containing the X axis** at phi = 24k - 4.5 and phi = 24k + 4.5
(tooth angular thickness 9 deg, space 15 deg). The flanks are flat and radial; there is no involute.

**Tooth section** (the same in every radial half plane inside the 9 deg sector), (x, r):
- inner face: the core front face x = -0.066 from r 0.42025 up (the tooth sits on the core);
- underside: cylinder **r = 0.42025** [10.67435 mm] from x = -0.066 to x = 0 (the tooth overhangs the core: below it,
  for x > -0.066, there is no material);
- back: convex circular arc, centre (x, r) = (-0.128797, 0.576417) [-3.27143, 14.641 mm], **radius 0.202428**
  [5.14166 mm], from (0, 0.42025) to the tangent point (0.070001, 0.53825) [1.77802, 13.67155 mm];
- **crown:** circular arc, centre (x, r) = (-0.0275, 0.556969) [-0.6985, 14.14702 mm], **radius 0.099281**
  [2.52173 mm], internally tangent to the back arc at (0.070001, 0.53825), running over the top (maximum
  r = 0.65625 [16.66875 mm] at x = -0.0275, maximum x = 0.071781, minimum x = -0.126781) and down to the plane
  x = -0.125, where it ends at r = 0.538297 and steps radially by 0.00005 to the core corner (-0.125, 0.53825).
- In other words: tooth sector solid = (disc of the crown circle) united with (rectangle x -0.066..0, r 0.42025..0.53825)
  united with (disc of the back-arc circle limited to x >= 0 and r 0.42025..0.53825), everything also united with the
  core; the part of the crown below x = -0.125 overhangs the conical slot slightly.

**Tooth spaces:** between two teeth the surface is the core only: cylinder r = 0.53825 from x = -0.125 to -0.066
and the core front face x = -0.066 up to r 0.53825.

## 5. Yoke Y2 and the pin-end details

**F7. Y2 = Y1 moved rigidly:** take Y1 completely (sections 3 and 4, including the gear teeth and the pin-end ring
groove, but see F8 for the hex), then
1. rotate it **180 deg about the Z axis** (x, y, z) -> (-x, -y, z); then
2. rotate it **+3 deg about the pivot axis** (the line x = 0, z = -0.5625, direction +Y), right-hand rule: the +X
   direction tips toward -Z, i.e. a point (x, y, z) goes to
   (x cos3 + (z + 0.5625) sin3, y, -x sin3 + (z + 0.5625) cos3 - 0.5625).

Results: Y2's shaft axis passes through (0.029439, 0, -0.000771) [0.74775, 0, -0.01958 mm] with direction
(cos3, 0, -sin3); its shaft end face centre is at (5.147415, 0, -0.268993); its knuckles are y = -0.915 to -0.685,
y = -1.375 to -1.145 (outermost) and y = 0.915 to 1.145. Y2's tooth k is centred on phi measured about its own axis from
-Y (the image of Y1's +Y). The teeth of the two yokes interleave at the mesh near the origin (they touch, see section 2).

**F8. Pin-end details** (in the outermost knuckle face of each yoke, coaxial with the pivot axis):

| | Y1 (face y = +1.375) | Y2 (face y = -1.375) |
|---|---|---|
| Ring groove (annulus r 0.15625 to 0.16125 [3.96875 to 4.09575 mm]) | floor y = 1.3125 (depth **0.0625**) | floor y = -1.315 (depth **0.06**) |
| Hex socket, 0.156 [3.9624 mm] across flats, flat floor | floor y = 1.2815 (depth **0.0935**) | floor y = -1.285 (depth **0.09**) |
| Hex orientation | two flats on the planes x = +-0.078 (flats normal to +-X and +-60 deg from X in the XZ plane, corners on +-Z) | the same, **in the global frame** (NOT rotated by the 3 deg swing): flats x = +-0.078 |

The island inside the ring groove (r < 0.15625) stays flush with the knuckle face, with the hex socket in it. Apart from
F8, Y2 equals the moved Y1 exactly (measured face by face, within 0.001 mm).

## 6. Acceptance targets

| ID | Name | V in3 | V mm3 | A in2 | A mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Y1 | Yoke Y1 (shaft along -X) | 3.35809 | 55029.18 | 28.7340 | 18538.03 | -1.6973 | 0.0449 | -0.0443 | -5.1250 | 0.3125 | -1.1450 | 1.3750 | -0.8750 | 0.7957 | 171 |
| Y2 | Yoke Y2 (shaft toward +X, swung 3 deg) | 3.35817 | 55030.59 | 28.7271 | 18533.59 | 1.7221 | -0.0449 | -0.1339 | -0.3125 | 5.1655 | -1.3750 | 1.1450 | -0.8750 | 0.7915 | 171 |

Whole assembly: 6.71626 in3 (110059.8 mm3), 57.4611 in2, CoM (0.0124, 0.0000, -0.0891), bounding box X [-5.125, 5.16547],
Y [-1.375, 1.375], Z [-0.875, 0.79574].

Check values: shaft end diameter 0.75, hub diameter 0.825, bore 0.5 x 1.125 deep; shaft end face 5.125 from the pivot
plane x = 0 (10.25 overall when the joint is straight); pivot axis 0.5625 from each shaft axis; knuckle diameter 0.625,
knuckle width and gaps 0.23; height over the knuckles 2.75; 15 teeth, crown tip diameter 1.3125, tooth root diameter
0.8405 under the teeth, space land diameter 1.0765; yoke front bore diameter 1.375; clearance slot radius 0.3375.

## 7. Source simplifications and undetermined items

- The knuckles are solid; no pin, no pin hole, no side links, no lubrication fittings. The pin is only represented by the
  F8 ring groove and hex socket. Reproduce as specified.
- The flat front faces of the two shells cross each other near the top (the master overlaps there by about 70 mm3);
  this is the source's geometry, keep it.
- The two yokes are modelled in one fixed position, 3 deg off straight; the catalogue's overall length 10 1/4 refers to
  the straight joint (2 x 5.125).
- The small differences of F8 between the two yokes (ring groove and hex depths, hex not following the swing) are in the
  master; keep them.
- Material (steel) and the 136 deg maximum operating angle are product data only.
- Undetermined: nothing on the analytic geometry. The ruled shell (F2) and its rounds (F6) are free-form in the master;
  the correspondence rule given in F2 reproduces the master's ruled surfaces within 0.02 mm.
