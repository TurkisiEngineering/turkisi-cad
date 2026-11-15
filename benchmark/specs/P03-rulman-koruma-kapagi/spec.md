# Design specification: moulded bearing guard (P3)

A thin-walled moulded cover (wall 0.125 in) that fits over a base-mounted bearing: a tent-shaped body along X with a
U-shaped hump across it, three small round bosses on top, and a flat flange around the open bottom. This document is
the only source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches** (1 in = 25.4 mm exactly). Angles in degrees. Model in inches, or multiply every value by 25.4; do
  not move the origin or the axes either way.
- **Global frame (use exactly, no realignment):**
  - **+Y is up.** The flange bottom (the mounting face) is the plane y = -1.53125; the flange top is y = -1.40625.
  - **X** is the long direction of the body (overall X extent +/-3.891473), **Z** the width direction.
  - The crown and hump arcs are cylinders whose axes are parallel to Z through (x, y) = (0, -0.09375).
  - The part is symmetric about the plane x = 0. It is symmetric about z = 0 except for the flange outline (section 3.6).
- Plane notation: "a x + b y + c z = d". All walls are drafted 4 degrees: sin 4 = 0.069756, cos 4 = 0.997564.
- One body, one solid. Name: **P01 Guard**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Bearing guard (one moulded solid) | custom |

## 3. Geometry of P01

Build an **outer solid** (3.1-3.3), add the flange (3.6) and the bosses (3.4), then remove the **inner cavity** (3.5)
and the boss recesses. Wall thickness is 0.125 everywhere: every inner surface is the matching outer surface offset
0.125 inward, so the result equals shelling the outer solid inward by 0.125 with the bottom face open. Outer and inner
values are both given.

### 3.1 Tent (main body), profile in XY extruded along Z, trimmed by the side walls

Closed profile in the XY plane, symmetric about x = 0, from the bottom y = -1.53125 up:
- **End walls** (drafted 4 degrees, leaning inward going up):
  outer 0.997564 |x| + 0.069756 y = 2.902310 (x = 3.007731 at y = -1.40625);
  inner 0.997564 |x| + 0.069756 y = 2.777310 (passes through (+/-2.8125, -0.40625)).
- **Slopes** (46.17 degrees above horizontal):
  outer 0.721392 |x| + 0.692527 y = 1.872576; inner 0.721392 |x| + 0.692527 y = 1.747576.
  The inner slope is the line through (2.8125, -0.40625) tangent to the inner crown circle.
- **End-wall / slope corner**, sharp: outer (+/-2.934036, -0.352353); inner (+/-2.8125, -0.40625).
- **Crown**: arc about (0, -0.09375), outer R1.9375, inner R1.8125, tangent to the slopes at outer
  (+/-1.397697, 1.248021) and inner (+/-1.307523, 1.161455). Crown top: outer y = 1.84375, inner y = 1.71875.

Extrude through Z, then keep only the slab between the **side walls** (drafted 4 degrees):
outer 0.069756 y + 0.997564 |z| = 0.860129 (|z| = 0.960563 at y = -1.40625);
inner 0.069756 y + 0.997564 |z| = 0.735129 (|z| = 0.835258 at y = -1.40625).

### 3.2 Hump (bearing housing bulge), profile in XY extruded along Z, trimmed by its end faces

Closed U profile in XY from the bottom y = -1.53125 up:
- **Legs** (drafted 4 degrees): outer 0.997564 |x| + 0.069756 y = 1.305960 (|x| = 1.407483 at y = -1.40625);
  inner 0.997564 |x| + 0.069756 y = 1.180960.
- **Arch**: arc about (0, -0.09375), outer R1.3125, inner R1.1875, **tangent** to the legs at outer
  (+/-1.309303, -0.002195) and inner (+/-1.184607, -0.010914). Arch top: outer y = 1.21875, inner 1.09375 (lower than
  the crown, so the hump only shows on the sides of the tent).

Extrude through Z, keep the slab between the **hump end faces** (drafted 4 degrees):
outer 0.069756 y + 0.997564 |z| = 1.608303 (|z| = 1.710564 at y = -1.40625);
inner 0.069756 y + 0.997564 |z| = 1.483303.
Unite the hump with the tent.

### 3.3 Rounds of the outer solid (inner values in brackets)

1. **Convex R0.375 [R0.25]** on every edge of the tent's two side walls except the bottom: the end-wall / side-wall
   edges, the slope / side-wall edges and the crown / side-wall edges (one continuous round along each side). Apply
   before uniting the hump.
2. **Convex R0.375 [R0.25]** on every edge of the hump's two end faces except the bottom (leg / end-face and
   arch / end-face edges). Apply before uniting.
3. **Concave R0.125 [R0.25]** along the whole intersection of the hump with the tent (hump legs and arch against the
   tent side walls and their rounds), on both sides.
4. Sharp: the end-wall / slope edges (lines along Z), the slope / crown junction (tangent), and the walls where they meet
   the flange top.

### 3.4 Bosses (three) and their recesses

Each boss is a round pad, **diameter 0.8125**, whose flat top lies **0.0875** above the outer surface measured on the
boss axis, with a **concave R0.1 round** between its side and the surrounding surface (the boss is lower than 0.1, so
the round runs straight into the top edge on most of the circumference). Each boss is hollow from inside: a recess
**diameter 0.5625** coaxial with the boss, cut from the cavity side up to a flat bottom 0.0875 beyond the inner surface
(0.125 below the boss top).
- **Top boss**: axis = the Y axis (x = 0, z = 0). Top face y = 1.93125. Recess bottom y = 1.80625.
- **Two slope bosses**: axis normal to the slope (direction (+/-0.721392, 0.692527, 0)) through the point
  (+/-1.369085, 1.277826, 0) on the outer slope plane. Top face 0.721392 |x| + 0.692527 y = 1.960076; recess bottom
  0.721392 |x| + 0.692527 y = 1.835076. The R0.1 base round on the slope side is a torus (tube-centre circle radius
  0.50625, 0.1 above the slope plane).

### 3.5 Inner cavity and opening edge

The cavity is the inner solid of 3.1-3.3 (inner values), extended down through the flange so the bottom is open.
The opening's bottom edge (inner walls meeting the plane y = -1.53125) has a **convex R0.1 round** all around
(the round centres lie at y = -1.43125).

### 3.6 Flange

Plate from y = -1.53125 to y = -1.40625 (0.125 thick), united with the body, with the cavity cut through it. Outline in
the XZ plane (coordinates (x, z)); go in this order, it closes on the start:
1. start (3.891473, -0.594612), line to (3.891473, 0.594612)
2. arc R1.249693 centre (2.641780, 0.594612) to (2.641780, 1.844305) (quarter, convex)
3. line to (1.995220, 1.844305)  (inside corner, sharp)
4. arc R0.980580 centre (1.042140, 1.613720) to (1.043100, 2.594305) (convex, 76.3 degree sweep, tangent to step 5)
5. line to (-1.043100, 2.594305)
6. arc R0.980580 centre (-1.042140, 1.613720) to (-1.995220, 1.844305)
7. line to (-2.641780, 1.844305)
8. arc R1.249693 centre (-2.641780, 0.594612) to (-3.891473, 0.594612)
9. line to (-3.891473, -0.594612)
10. arc R1.249693 centre (-2.641780, -0.594612) to (-2.641780, -1.844305)
11. line to (-2.186970, -1.844305)  (inside corner, sharp)
12. arc R1.249693 centre (-1.041530, -1.344612) to (-1.041530, -2.594305) (convex, 66.4 degree sweep, tangent to step 13)
13. line to (1.041530, -2.594305)
14. arc R1.249693 centre (1.041530, -1.344612) to (2.186970, -1.844305)
15. line to (2.641780, -1.844305)
16. arc R1.249693 centre (2.641780, -0.594612) to the start.
Note the source asymmetry: the two tab corners on +Z use R0.980580, those on -Z use R1.249693. Reproduce it.
Flange edges are sharp.

### 3.7 Source conditions

- Near x = 0 (|x| < 0.13), under the top boss, the master's crown / side-wall rounds (outer and inner) are locally up
  to 0.02 lower than a constant-radius round. This is a local irregularity of the source; build the constant-radius
  round of 3.3.
- The master file contains 18 empty, zero-size closed shells (108 faces of zero area) at
  (0.2162, -1.2252, 1.5854) in. They have no volume; do not reproduce them.
- The surface texture seen on product photos is not modelled.

## 4. Acceptance targets

| ID | Volume in3 | Volume mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Guard | 8.3375 | 136628 | 135.55 | 87451 | 0.0000 | -0.3633 | -0.0056 | -3.891473 | 3.891473 | -1.53125 | 1.93125 | -2.594305 | 2.594305 | 174 (+108 empty) |

Same box in mm: X +/-98.8434, Y -38.8938 to 49.0538, Z +/-65.8953. CoM in mm: (0.000, -9.229, -0.142).

Volume note: measured by triangulated integration (converged to 0.01 %). A B-rep property calculation on the master
reads 139956 mm3, a known integration error on two badly parametrised faces; it is not the target.

Check values: wall 0.125; inner end walls 5.625 apart at y = -0.40625; flange 0.125 thick; overall height 3.4625
(flange bottom to top boss); bosses diameter 0.8125, recesses 0.5625; draft 4 degrees on all walls.

## 5. Undetermined items

- The catalogue "inside height 3.063" and "inside width 1.5" do not correspond to one face pair: the inner side walls
  are drafted (1.4738 apart at y = 0, 1.5 apart at y = -0.187) and no inner surface lies at y = 1.53125. Follow the
  geometry above.
- Why the flange tabs differ between +Z and -Z is not known (source condition, keep it).
- Material (yellow ABS) is from the product data, not from the 3D master.
