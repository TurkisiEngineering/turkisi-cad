# Design specification: water-to-air fin heat exchanger with copper tube coil, axial fan, finger guard and power cord

A compact liquid-to-air cooler: a serpentine copper tube coil (12 straight passes, 6 hairpin tubes, 5 return bends) held
between two tube sheets, a pack of thin wavy fin strips, two bent sheet-metal side channels with mounting slots, a square
axial fan (frame, hub, five blades) with a finger guard on its outlet side, two 37 deg flare tube connections with hex
nuts, and a flat two-conductor power cord, coiled, ending in a two-blade plug. This document is the only source for the
rebuild. Every number below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm (1 in = 25.4 mm exactly). A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment). Every body is modelled in place in this frame (identity placement), each
  body as a separate solid. 103 bodies.**
  - **The fan axis is the X axis** (y = 0, z = 0). Air flows toward +X: coil and fins at the -X end, the fan from x = 0.92
    to 2.396, the finger guard from x = 2.396 to 2.676.
  - **The tube passes run parallel to Z.** The hairpin bends are at +Z (top of z), the return bends and the two tube
    connections at -Z.
  - **The side channels lie at +Y and -Y** (y = +/-2.465 to +/-2.89).
  - The power cord and plug hang toward -Y (down to y = -10.19).
- **Tube rows.** Row A: tube axes at **x = 0.172**. Row B: tube axes at **x = -0.47752** for the straight tube legs, the
  tube sheet holes and the fins; but the parts at the -Z end of row B (return bends, collar rings, connection stubs,
  fittings, nuts) are on **x = -0.453** (0.02452 off; reproduce this as stated, it creates the overlaps listed in
  section 5). Pass positions (y of the tube axis): row A **y = -1.6875, -0.9375, -0.1875, 0.5625, 1.3125, 2.0625**; row B
  **y = -2.0625, -1.3125, -0.5625, 0.1875, 0.9375, 1.6875** (0.75 pitch in each row, rows staggered by 0.375; the
  distance from an A axis to its B neighbour is exactly 0.75 because 0.172 - (-0.47752) = 0.64952 = 0.375 * sqrt 3).
- **Profile conventions:** "(x, y) profile" = closed outline in a plane normal to Z, extruded along Z between the stated
  z values; "(y, z) outline" = outline in a plane normal to X; "(r, z)" / "(r, x)" = half-section of a body of revolution
  about the stated axis; "arc c=(a, b) R" = circular arc of radius R about centre (a, b), the short way. Angles in the
  (y, z) plane are measured from +Y toward +Z (a positive rotation about +X).

## 2. Product description and source simplifications

**Coil.** Six **hairpin tubes** (P01) each form an A pass and the neighbouring B pass with a 180 deg bend above the top
tube sheet. At the bottom, five **return bends** (P02) join the remaining pass pairs, so the water path is one serpentine
from the B-row stub at y = -2.0625 to the B-row stub at y = 1.6875. Each of the two open ends carries a **tube stub**
(P03) down to a **37 deg flare end fitting** (P05) with a **hex nut** (P06) on the stub. Twelve **collar rings** (P04)
sit on the tube ends just below the bottom tube sheet. Two **tube sheets** (P07) hold the passes at z = +/-2.53.
**Fins:** 41 equal wavy fin strips (P08) at 0.12 pitch plus one thinner strip (P09) beside the bottom tube sheet.
**Frame:** two bent **side channels** (P10 at +Y, P11 at -Y; not mirror images), four **fork clips** (P12) that join the
tube sheets to the channels, and four small **spacer blocks** (P13) on the channel webs.
**Fan:** a square **fan frame** (P14) with a rear motor support and an integral outlet grill, a **hub** (P15, the motor),
five **blades** (P16), a **finger guard** (P17) on the outlet face, four **pan head screws** (H1) through frame and guard,
and four **washers** (H2) under the screw heads.
**Electrical:** a flat **power cord** (P18) leaving the fan frame through a boss, a **plug body** (P19) and two **plug
blades** (P20).

**Simplifications that exist in the source model and must be reproduced:**
- The tubes of the coil (hairpins and return bends) are **solid round bars** (no bore). Only the two connection stubs
  (P03) are hollow.
- The fin strips **do not touch the tubes**: they are narrow wavy strips beside row B on the -X side (x = -0.92 to -0.742).
- The finger guard has **no screw holes**: the four screws pass through solid guard material (overlap, section 5).
- The screws have a modelled helical thread; no other thread is modelled (the flare fittings and nuts are plain).
- No water passages inside the fittings beyond the stated bores; no motor internals, no wires inside the cord.
- The cord is one solid of flat rounded-rectangle section; its coil is a helix of 3.25 turns.
- Material (product data): copper tube and copper fins; other materials undetermined.

## 3. Part list

20 distinct custom parts and 2 distinct hardware items, 22 distinct items, **103 bodies in total** (the original file has
103 solids and no empty shells; nothing was dropped).

| ID | Qty | Name | Type | Instances (placement in section 4) |
|---|---|---|---|---|
| P01 | 6 | Hairpin tube | custom | P01-a ... P01-f |
| P02 | 5 | Return bend | custom | P02-a ... P02-e |
| P03 | 2 | Connection tube stub (hollow) | custom | P03-a, P03-b |
| P04 | 12 | Tube collar ring | custom | P04-a ... P04-l |
| P05 | 2 | 37 deg flare end fitting | custom | P05-a, P05-b |
| P06 | 2 | Hex nut 0.625 across flats | custom | P06-a, P06-b |
| P07 | 2 | Tube sheet | custom | P07-a (bottom), P07-b (top) |
| P08 | 41 | Fin strip 0.06 thick | custom | P08-01 ... P08-41 |
| P09 | 1 | End fin strip 0.04 thick | custom | P09 |
| P10 | 1 | Side channel, +Y | custom | P10 |
| P11 | 1 | Side channel, -Y | custom | P11 |
| P12 | 4 | Fork clip | custom | P12-a ... P12-d |
| P13 | 4 | Spacer block | custom | P13-a ... P13-d |
| P14 | 1 | Fan frame with outlet grill | custom | P14 |
| P15 | 1 | Fan hub (motor) | custom | P15 |
| P16 | 5 | Fan blade | custom | P16-a ... P16-e |
| P17 | 1 | Finger guard | custom | P17 |
| P18 | 1 | Power cord | custom | P18 |
| P19 | 1 | Plug body | custom | P19 |
| P20 | 2 | Plug blade | custom | P20-a, P20-b |
| H1 | 4 | Pan head screw, thread 0.170 x 0.05 pitch | hardware | H1-a ... H1-d |
| H2 | 4 | Washer 0.29 / 0.36 | hardware | H2-a ... H2-d |

## 4. Part geometry

### P01 Hairpin tube (6 identical bodies, 8 faces each)

Solid round bar **diameter 0.375 (R0.1875)**. Two straight legs parallel to Z from the flat end **z = -2.56** up to
**z = 2.6945**: leg A on (x 0.172, y_A), leg B on (x -0.47752, y_B = y_A - 0.375). At the top the legs are joined by a
**180 deg bend of centreline radius 0.375** in the plane that contains both leg axes: bend centre at
(x -0.15276, y_A - 0.1875, z 2.6945), bend axis direction (-0.5, 0.86603, 0) (the bend is a half torus, major radius
0.375, tube radius 0.1875; its top is at z = 3.257).

| Instance | y_A (leg A) | y_B (leg B) |
|---|---|---|
| P01-a | -1.6875 | -2.0625 |
| P01-b | -0.9375 | -1.3125 |
| P01-c | -0.1875 | -0.5625 |
| P01-d | 0.5625 | 0.1875 |
| P01-e | 1.3125 | 0.9375 |
| P01-f | 2.0625 | 1.6875 |

### P02 Return bend (5 identical bodies, 10 faces each)

Solid round bar diameter 0.375. A 180 deg bend of **centreline radius 0.375** in the plane x = x_R, bend centre
(x_R, y_c, **z -2.7105**), so the bottom of the bar is at **z = -3.273**. From the two bend ends straight legs run up (+Z):
the leg on the **higher y** (y_c + 0.375) ends at a flat face **z = -2.5** (inside the tube sheet hole), the leg on the
**lower y** (y_c - 0.375) ends at **z = -2.56**.

| Instance | x_R | y_c | legs at y |
|---|---|---|---|
| P02-a | 0.172 | -1.3125 | -1.6875 (to -2.56), -0.9375 (to -2.5) |
| P02-b | -0.453 | -0.9375 | -1.3125 (to -2.56), -0.5625 (to -2.5) |
| P02-c | 0.172 | 0.1875 | -0.1875 (to -2.56), 0.5625 (to -2.5) |
| P02-d | -0.453 | 0.5625 | 0.1875 (to -2.56), 0.9375 (to -2.5) |
| P02-e | 0.172 | 1.6875 | 1.3125 (to -2.56), 2.0625 (to -2.5) |

### P03 Connection tube stub (2 identical bodies, 6 faces)

Tube **OD 0.375, ID 0.335** (wall 0.02), axis parallel to Z on (x -0.453, y_s), from **z = -3.9894** to **z = -2.56**
(flat ends). **P03-a: y_s = -2.0625; P03-b: y_s = 1.6875.**

### P04 Tube collar ring (12 identical bodies, 6 faces)

Ring **ID 0.375, OD 0.436** (R0.1875 / R0.218), from **z = -2.71 to -2.56**, coaxial with a pass. Positions (x, y), in
the order a ... l: (-0.453, -2.0625), (0.172, -1.6875), (-0.453, -1.3125), (0.172, -0.9375), (-0.453, -0.5625),
(0.172, -0.1875), (-0.453, 0.1875), (0.172, 0.5625), (-0.453, 0.9375), (0.172, 1.3125), (-0.453, 1.6875),
(0.172, 2.0625). (Row B rings use x = -0.453.)

### P05 37 deg flare end fitting (2 identical bodies, 14 faces)

Body of revolution about the stub axis (x -0.453, y_s), half-section (r, z), closed: (0.1875, -3.9894) -> (0.2175,
-3.9894) -> (0.2175, -4.2394) -> (0.25, -4.2394) -> (0.25, -4.4269) -> (0.2175, -4.4269) -> straight (cone) to
(0.25, -4.47) -> (0.21875, -4.47) -> straight (cone) to (0.1875, -4.4285) -> back up the bore r = 0.1875 to the start.
Both cones have a **37 deg half angle**. The bore (diameter 0.375) is empty. **P05-a on y_s = -2.0625, P05-b on
y_s = 1.6875.** Its top face z = -3.9894 touches the stub end.

### P06 Hex nut (2 identical bodies, 22 faces)

Hexagonal prism **0.625 across flats** (two flats normal to X at x_axis +/- 0.3125; corners toward +/-Y at 0.36084 from
the axis), from **z = -3.5684 to -3.1309** (0.4375 long), coaxial with the stub (x -0.453, y_s), **bore diameter 0.375**
(fits the stub OD). Both ends chamfered by a **45 deg cone** (half angle 45 deg) that passes through radius 0.3125 at the
end face (the end faces are rings r 0.1875 to 0.3125). P06-a on y_s = -2.0625, P06-b on y_s = 1.6875.

### P07 Tube sheet (2 identical bodies, 32 faces)

(x, y) profile: rectangle **x -0.92 to 0.857, y -2.465 to 2.465** with the two +X corners cut by **45 deg chamfers 0.125 x
0.125** (vertices (0.732, +/-2.465), (0.857, +/-2.34)). **12 through holes diameter 0.375** on all 12 pass positions,
row A at x = 0.172 and row B at **x = -0.47752**. Thickness 0.06: **P07-a z = -2.56 to -2.5; P07-b z = 2.5 to 2.56.**

### P08 Fin strip (41 identical bodies, 38 faces) and P09 end fin strip (1 body)

A wavy band of constant width **0.075**, extruded along Z. Its centreline is a chain of tangent arcs: **R0.405 about the
row B centres B_j = (x -0.47752, y -2.0625 + 0.75 j), j = 0 ... 5**, alternating with **R0.33 about the points
A'_i = (x -1.10966, y -1.6875 + 0.75 i), i = 0 ... 4** (|B_j A'_i| = 0.735 = 0.405 + 0.33, so neighbouring arcs are
tangent). The band is therefore bounded by:
- the **outer (-X) edge**: arcs **R0.4425 about B_j** (reaching x = -0.92002 at y = y_Bj) and **R0.2925 about A'_i**
  (reaching x = -0.81716 at y = y_Ai), meeting at the tangent points (-0.85809, y_Ai +/- 0.14923);
- the **inner (+X) edge**: arcs **R0.3675 about B_j** (reaching x = -0.84502) and **R0.3675 about A'_i** (reaching
  x = -0.74216), meeting at (-0.79359, y_Ai +/- 0.1875);
- straight ends: from the last arcs at y = 1.6875 (B_5) and y = -2.0625 (B_0) the band continues straight along Y between
  **x = -0.92002 and -0.84502** to the end lines **y = +2.465** and **y = -2.465**.

Profile vertices, starting at the top end (x, y): (-0.92002, 2.465) -> (-0.84502, 2.465) -> (-0.84502, 1.6875) -> arc
R0.3675 c=B_5 -> (-0.79359, 1.5) -> arc R0.3675 c=A'_4 -> (-0.79359, 1.125) -> arc R0.3675 c=B_4 -> (-0.84502, 0.9375)
-> ... repeating down to (-0.84502, -2.0625) -> (-0.84502, -2.465) -> (-0.92002, -2.465) -> (-0.92002, -2.0625) -> arc
R0.4425 c=B_0 -> (-0.85809, -1.83673) -> arc R0.2925 c=A'_0 -> (-0.85809, -1.53827) -> arc R0.4425 c=B_1 ... -> arc
R0.2925 c=A'_4 -> (-0.85809, 1.46173) -> arc R0.4425 c=B_5 -> (-0.92002, 1.6875) -> back to the start.
Extent x -0.92002 to -0.74216, y -2.465 to 2.465.

- **P08: thickness 0.06.** Instance P08-k (k = 1 ... 41) spans **z = -2.40 + 0.12 (k - 1) to z = -2.34 + 0.12 (k - 1)**,
  i.e. centres z = -2.37, -2.25, ..., 2.43 (pitch 0.12; P08-01 at z -2.40..-2.34, P08-41 at z 2.40..2.46).
- **P09: same profile, thickness 0.04, z = -2.50 to -2.46** (it touches the bottom tube sheet P07-a).

### P10 Side channel, +Y (one solid, 43 faces) and P11 Side channel, -Y (one solid, 43 faces)

Bent sheet 0.063 thick, extruded along Z from **z = -2.875 to 2.875** (length 5.75). Three walls: a **-X leg**
(x -0.92 to -0.857) standing outward to |y| = 2.89, a **web** in the plane |y| = 2.465 to 2.528, and a **+X leg**
(x 0.857 to 0.92) turned inward to |y| = 1.84.

**P10 (x, y) profile** (closed): (-0.857, 2.78375) -> (-0.92, 2.78375) -> (-0.92, 2.502) -> arc c=(-0.883, 2.502) R0.037
-> (-0.883, 2.465) -> (0.82, 2.465) -> arc c=(0.82, 2.428) R0.037 -> (0.857, 2.428) -> (0.857, 1.84) -> (0.92, 1.84) ->
(0.92, 2.428) -> arc c=(0.82, 2.428) R0.1 -> (0.82, 2.528) -> (-0.757, 2.528) -> arc c=(-0.757, 2.628) R0.1 -> (-0.857,
2.628) -> close. The profile stops at y = 2.78375 only at the two end faces: the -X leg reaches **y = 2.89** everywhere
else, its two outer corners being cut by **45 deg chamfers 0.10625 x 0.10625** (from (y 2.78375, z +/-2.875) to (y 2.89,
z +/-2.76875)).

**P11 (x, y) profile** (closed; note the -X bend is reversed compared with P10): (-0.92, -2.78375) -> (-0.857, -2.78375) ->
(-0.857, -2.565) -> arc c=(-0.82, -2.565) R0.037 -> (-0.82, -2.528) -> (0.82, -2.528) -> arc c=(0.82, -2.428) R0.1 ->
(0.92, -2.428) -> (0.92, -1.84) -> (0.857, -1.84) -> (0.857, -2.428) -> arc c=(0.82, -2.428) R0.037 -> (0.82, -2.465) ->
(-0.82, -2.465) -> arc c=(-0.82, -2.565) R0.1 -> (-0.92, -2.565) -> close; -X leg to **y = -2.89**, corners chamfered
0.10625 x 0.10625 as on P10.

**Cut-outs (both channels; s = +1 for P10, -1 for P11):**
- **-X leg: three U-slots, width 0.22**, at **z = 0, -2.5, +2.5**, cut through the leg along X from the free edge
  |y| = 2.89 inward: straight sides z = z_slot +/- 0.11, round end **R0.11 centred at y = s 2.69** (slot bottom at
  |y| = 2.58, slot depth 0.31).
- **+X leg: one rectangular cut-out** from the free edge |y| = 1.84 to **|y| = 2.25**, for **-1.31 <= z <= 1.31** (sharp
  corners).
- **+X leg: two holes diameter 0.1875** (axis along X) at **(y s 2.055, z +/-2.0625)** and **two holes diameter 0.25** at
  **(y s 2.0555, z +/-2.5)**.

### P12 Fork clip (4 identical bodies, 14 faces)

Described for a clip centred at (y_c, z_c): a **plate** x 0.92 to 0.97, y y_c +/- 0.1875, z z_c +/- 0.07, and a **tongue**
x 0.77 to 0.92, y y_c +/- 0.0675, z z_c +/- 0.07, split by a **slot 0.06 wide** (z_c - 0.03 to z_c + 0.03) running through
the whole tongue length (x 0.77 to 0.92, open at x = 0.77). The tongue passes through the 0.25 hole of the channel and
its slot holds the tube sheet edge. Centres (y_c, z_c): **P12-a (2.055, 2.53), P12-b (-2.055, 2.53), P12-c (-2.055,
-2.53), P12-d (2.055, -2.53)**.

### P13 Spacer block (4 identical bodies, 6 faces)

Rectangular block **x -0.1 to 0, |y| 2.528 to 2.578** (on the outside of a channel web), **z z_c +/- 0.125**.
P13-a (+Y, z_c -2.25), P13-b (+Y, z_c 2.25), P13-c (-Y, z_c 2.25), P13-d (-Y, z_c -2.25).

### Grill pattern G (used by P14 and P17)

All on the X axis, in the (y, z) plane; the material of a grill inside its opening is:
- a **centre disc r <= 0.4375**;
- **five rings**: r 0.775 to 0.875, 1.125 to 1.225, 1.475 to 1.575, 1.825 to 1.925, and **2.295 to 2.395** (the last one is
  clipped by the opening, see below);
- **five curved spokes**: spoke k (k = 0 ... 4) is part of the circular band between radii **R2.1652 and R2.2652** about
  the centre **C_k at radius 1.8277 from the axis, polar angle 9 + 72 k deg**: C_0 = (y 1.8052, z 0.2859),
  C_1 = (0.2859, 1.8052), C_2 = (-1.6285, 0.8298), C_3 = (-1.2924, -1.2924), C_4 = (0.8298, -1.6285). Of that band only
  the half on the **counter-clockwise side of the line from the axis through C_k** (angles theta_k to theta_k + 180 deg)
  is kept: it starts inside the centre disc and runs outward to the r = 2.295 ring. At r = 1.375 the spoke centreline
  passes through polar angle theta_k + 86.30 deg (for C_0: (y -0.1271, z 1.3691); C_3: (0.9075, -1.0330)).
The space between these members inside the opening is open (through the grill thickness).

### P14 Fan frame (one solid, 205 faces)

- **Envelope:** square **y, z from -2.45 to 2.45** with the four edges parallel to X rounded **R0.1** (centres (+/-2.35,
  +/-2.35)), from **x = 0.92 to 2.396**.
- **Corner recesses:** between **x = 1.02 and 2.296** all material outside the circle **R2.77657** about the X axis is
  removed (the four corners), leaving a **rear flange x 0.92 to 1.02** and a **front flange x 2.296 to 2.396** at full
  square size. The side walls between the recesses are the flat faces |y| = 2.45, |z| = 2.45 (each 2.613 wide).
- **Air opening:** from **x = 1.02 to 2.346** the region inside the square |y|, |z| <= 2.275 **and** inside the circle
  **R2.57657** is removed (wall 0.175 thick at the flats).
- **Rear flange opening (x 0.92 to 1.02):** the circle **R2.275** is open except for a **hub disc R1.0** and **four
  straight struts 0.29 wide** from the hub to the circle, centrelines through the axis at polar angles **45.07, 135.07,
  225.07, 315.07 deg** (strut side lines e.g. from (y -0.5981, z 0.8014) to (-1.5049, 1.7061) and from (-0.8029, 0.5961)
  to (-1.7097, 1.5008)). The **hub disc R1.0 extends from x = 0.92 to 1.17** (its face x = 1.17 carries P15).
- **Front grill (x 2.346 to 2.396, 0.05 thick):** the opening (square |y|, |z| <= 2.275 and circle R2.57657) is filled
  with grill pattern G; the outer ring 2.295 to 2.395 merges with the frame where the square cuts it.
- **Four corner holes diameter 0.21** parallel to X through both flanges at (y, z) = **(2.06, 2.065), (-2.065, 2.06),
  (-2.06, -2.065), (2.065, -2.06)** (a 90 deg rotational pattern; not symmetric about the planes y = 0 or z = 0).
- **Cord exit boss** on the +Z wall: a cylinder **diameter 0.36** whose axis has direction **(0, -0.5020, 0.8648)** (in
  the YZ plane, 30.1 deg from +Z toward -Y) and passes through **G = (1.658, -1.62929, 2.44810)**. Its top is the plane
  normal to the axis **0.06 beyond G** (outward); the top edge is a full **R0.06 round** (flat top r <= 0.12). A
  **recess 0.12 (along X) x 0.26 (in the YZ plane), 0.06 deep** with corner radii R0.01 is cut into the top, centred on
  the axis; its floor is the plane through G normal to the axis. Downward the boss runs into the frame corner where it
  blends into the recess surface R2.77657 (blend free-form in the original; its exact shape is undetermined).

### P15 Fan hub (motor) (one solid, 6 faces)

Cylinder **diameter 2.0** about X from **x = 1.17 to 2.296**; the front edge rounded **R0.1** (front face a disc R0.9 at
x = 2.296).

### P16 Fan blade (5 identical bodies, 9 faces each)

Described for **P16-a**; P16-b ... P16-e are P16-a rotated about the X axis by **-72, -144, -216, -288 deg**.
P16-a is the intersection of:
- the slab **outside** the cylinder **S1** (axis parallel to Y through (x -4.0373, z 4.1799), **R6.70083**) and **inside**
  the cylinder **S2** (axis parallel to Y through (x -4.1909, z 4.3793), **R7.0**) (blade about 0.06 to 0.08 thick);
- **1.0 <= r <= 2.275** (r = distance from the X axis; the root sits on the hub);
- **z >= 0** and **0.8192 y + 0.5736 z <= 0** (between the half-planes at polar angles 125 and 180 deg);
- the corner between z = 0 and the tip rounded **R0.125** (axis parallel to X through (y -2.1464, z 0.125)), the corner
  between the tip and the 125 deg side rounded **R0.64131** (axis parallel to X through (y -1.3872, z 0.8630));
- **inside** the cylinder parallel to Y through (x -0.6571, z 2.5053), **R3.0** (trims the outlet-side corner).
Resulting extent of P16-a: x 1.2001 to 2.1710, y -2.2714 to -0.5736, z 0 to 1.5043.

### P17 Finger guard (one solid, 143 faces)

Plate **x 2.396 to 2.676** (0.28 thick), square **y, z from -2.265 to 2.265**, the four corners rounded **R0.2** (centres
(+/-2.065, +/-2.065)). Opening: the region inside the square |y|, |z| <= 2.185 **and** inside the circle **R2.57657** is
cut through and filled with grill pattern G (through the full 0.28 thickness). **No screw holes.**

### H1 Pan head screw (4 identical bodies, 95 faces)

Axis parallel to X; axis positions (y, z): **H1-a (-2.05, 2.065), H1-b (-2.05, -2.06), H1-c (2.06, -2.06),
H1-d (2.06, 2.065)**.
- **Head:** underside **x = 2.676**, cylinder **diameter 0.29** to x = 2.776, top edge round **R0.05**, flat top
  **x = 2.826** (r <= 0.095). **Cross recess** depth 0.06 (floor x = 2.766), arms along Y and Z, arm half-width 0.0098 at
  the floor and 0.015 at the top, arm reach from the axis 0.0785 at the floor and 0.0837 at the top (walls drafted 5 deg).
- **Shank:** modelled **right-hand helical thread, pitch 0.05**, crest diameter **0.170**, root diameter about 0.115
  (rounded root), flanks about 30 deg to the radial plane, crest flat about 0.013 wide, from the flat end **x = 0.92** to
  the head underside x = 2.676. Phase (H1-a): in the half-plane toward +Y from the axis the crest flat centres lie at
  x = 0.02675 + 0.05 n.

### H2 Washer (4 identical bodies, 6 faces)

Flat ring **ID 0.29, OD 0.36**, **x = 2.676 to 2.711**, axis parallel to X at (y, z): **H2-a (-2.065, 2.06),
H2-b (-2.06, -2.065), H2-c (2.065, -2.06), H2-d (2.06, 2.065)**.

### P18 Power cord (one solid, 26 faces)

Flat cord: section **0.10 along X by 0.25 across**, a rounded rectangle with corner radii **R0.02**; the 0.10 side always
parallel to X, the 0.25 side normal to the path in the YZ plane. Path of the section centre:
1. **Start face at G = (1.658, -1.62929, 2.44810)** (inside the boss recess), straight for **3.0** in direction
   **(0, -sin 34, cos 34) = (0, -0.55919, 0.82904)** to (1.658, -3.30686, 4.93521).
2. **Helix** about the line parallel to X through **(y -4.96494, z 3.81683)**, **radius 2.0**, tangent to step 1: polar
   angle (from +Y toward +Z about that line) from **34 deg increasing by 1170 deg (3.25 turns)** to 1204 deg (= 124 deg);
   **x decreases linearly from 1.658 to 1.3005** (0.11 per turn).
3. Straight **3.0** from (1.3005, -6.08332, 5.47491) in direction **(0, -cos 34, -sin 34) = (0, -0.82904, -0.55919)** to
   the **end face centre O = (1.3005, -8.57043, 3.79733)** (end face normal to the path).
Extent: x 1.2505 to 1.708, y -8.6403 to -1.5257, z 1.6919 to 5.9418.

### Plug frame (for P19, P20)

Origin **O = (1.3005, -8.57043, 3.79733)** (cord end), **u = (0, -0.82904, -0.55919)** (cord direction, toward the blade
tips), **x' = +X**, **w = (0, -0.55919, 0.82904)**. A point (x', w, u) is O + x'(1, 0, 0) + w w_dir + u u_dir. Every
section of P19 normal to u is a rectangle |x'| <= a, |w| <= b with its four corners rounded by rho.

### P19 Plug body (one solid, 147 faces)

| u from | u to | a | b | rho | remarks |
|---|---|---|---|---|---|
| 0 | 0.24 | 0.175 | 0.2494 + 0.17633 u (10 deg taper) | 0.02 | strain relief ribs, grooves below |
| 0.24 | 0.34 | 0.175 | 0.2917 | 0.02 | last rib |
| 0.34 | 0.465 | 0.29 | 0.378 | 0.06 | collar; all edges of both end faces rounded R0.03 |
| 0.465 | 0.965 | 0.2305 | 0.18719 + 0.20701 u (0.2834 to 0.3870) | 0.05 | tapered neck |
| 0.965 | 1.0901 | 0.3683 | 0.487 | 0.06 | head; all edges of both end faces rounded R0.03 |

**Strain relief grooves:** at **u 0.035 to 0.07, 0.12 to 0.155, 0.205 to 0.24** the section is reduced to a core rectangle
**|x'| <= 0.125, |w| <= 0.1418** (corners R0.02) plus a **centre web |x'| <= 0.025** over the full height b(u). The end
face u = 0 (0.35 x 0.4988) meets the cord end face.

### P20 Plug blade (2 identical bodies, 10 faces)

Flat blade **x' from -0.1309 to 0.1201** (0.251 wide), **0.0585 thick**, from the plug face **u = 1.0901 to u = 1.7691**;
the two tip corners chamfered **0.05 x 0.05** (45 deg); a **hole diameter 0.125** through the thickness at
**(x' -0.0054, u 1.6068)**. **P20-a: w from -0.2773 to -0.2188; P20-b: w from 0.2188 to 0.2773.**

## 5. Assembly

All 103 bodies are built in place with identity placement.
- The hairpin legs pass through both tube sheets (hole = tube diameter, face contact). The fins and the tubes do not
  touch. The tube sheets touch the clips (slot fit) and the end fin P09 touches P07-a.
- Fork clip tongues pass through the 0.25 holes of the channel +X legs; the clip plates bear on the leg faces x = 0.92;
  the channel +X legs (x 0.857 to 0.92) touch the fan frame rear face x = 0.92.
- Fan hub P15 sits on the frame hub disc (x = 1.17); blade roots touch the hub cylinder; the guard rear face x = 2.396
  touches the frame front face; washers lie on the guard front face x = 2.676.
- **Body overlaps in the original (reproduce; volumes in mm3):**

| Pair | Overlap | Cause |
|---|---|---|
| P02-a / P01-b, P02-c / P01-d, P02-e / P01-f | 108.59 each | return bend leg (to z -2.5) inside the hairpin leg end, row A |
| P02-b / P01-c, P02-d / P01-e | 99.56 each | same in row B (offset 0.02452 in x) |
| P02-b / P07-a, P02-d / P07-a | 9.03 each | row B bend legs at x -0.453 cut into the tube sheet beside the hole at x -0.47752 |
| H1-a ... H1-d / P17 | 86.09 each | screw shanks through the solid guard (no holes) |

Smaller overlaps below 8 mm3: H1-a / H2-a 2.63, H1-b / H2-b 1.86, H1-c / H2-c 0.83, P14 / P18 0.84.

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (screws,
cord, plug body, grill parts 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is
information only. Repeated instances differ only in position.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01-a | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | -1.8750 | 0.3577 | -0.6650 | 0.3595 | -2.2500 | -1.5000 | -2.5600 | 3.2570 | 8 |
| P01-b | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | -1.1250 | 0.3577 | -0.6650 | 0.3595 | -1.5000 | -0.7500 | -2.5600 | 3.2570 | 8 |
| P01-c | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | -0.3750 | 0.3577 | -0.6650 | 0.3595 | -0.7500 | 0.0000 | -2.5600 | 3.2570 | 8 |
| P01-d | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | 0.3750 | 0.3577 | -0.6650 | 0.3595 | -0.0000 | 0.7500 | -2.5600 | 3.2570 | 8 |
| P01-e | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | 1.1250 | 0.3577 | -0.6650 | 0.3595 | 0.7500 | 1.5000 | -2.5600 | 3.2570 | 8 |
| P01-f | Hairpin tube | 1.29080 | 21152.43 | 13.9894 | 9025.42 | -0.1528 | 1.8750 | 0.3577 | -0.6650 | 0.3595 | 1.5000 | 2.2500 | -2.5600 | 3.2570 | 8 |
| P02-a | Return bend | 0.16999 | 2785.61 | 2.0341 | 1312.32 | 0.1720 | -1.2979 | -2.8829 | -0.0155 | 0.3595 | -1.8750 | -0.7500 | -3.2730 | -2.5000 | 10 |
| P02-b | Return bend | 0.16999 | 2785.61 | 2.0341 | 1312.32 | -0.4530 | -0.9229 | -2.8829 | -0.6405 | -0.2655 | -1.5000 | -0.3750 | -3.2730 | -2.5000 | 10 |
| P02-c | Return bend | 0.16999 | 2785.61 | 2.0341 | 1312.32 | 0.1720 | 0.2021 | -2.8829 | -0.0155 | 0.3595 | -0.3750 | 0.7500 | -3.2730 | -2.5000 | 10 |
| P02-d | Return bend | 0.16999 | 2785.61 | 2.0341 | 1312.32 | -0.4530 | 0.5771 | -2.8829 | -0.6405 | -0.2655 | -0.0000 | 1.1250 | -3.2730 | -2.5000 | 10 |
| P02-e | Return bend | 0.16999 | 2785.61 | 2.0341 | 1312.32 | 0.1720 | 1.7021 | -2.8829 | -0.0155 | 0.3595 | 1.1250 | 2.2500 | -3.2730 | -2.5000 | 10 |
| P03-a | Inlet / outlet tube stub | 0.03188 | 522.46 | 3.2329 | 2085.72 | -0.4530 | -2.0625 | -3.2747 | -0.6405 | -0.2655 | -2.2500 | -1.8750 | -3.9894 | -2.5600 | 6 |
| P03-b | Inlet / outlet tube stub | 0.03188 | 522.46 | 3.2329 | 2085.72 | -0.4530 | 1.6875 | -3.2747 | -0.6405 | -0.2655 | 1.5000 | 1.8750 | -3.9894 | -2.5600 | 6 |
| P04-a | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | -2.0625 | -2.6350 | -0.6710 | -0.2350 | -2.2805 | -1.8445 | -2.7100 | -2.5600 | 6 |
| P04-b | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | -1.6875 | -2.6350 | -0.0460 | 0.3900 | -1.9055 | -1.4695 | -2.7100 | -2.5600 | 6 |
| P04-c | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | -1.3125 | -2.6350 | -0.6710 | -0.2350 | -1.5305 | -1.0945 | -2.7100 | -2.5600 | 6 |
| P04-d | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | -0.9375 | -2.6350 | -0.0460 | 0.3900 | -1.1555 | -0.7195 | -2.7100 | -2.5600 | 6 |
| P04-e | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | -0.5625 | -2.6350 | -0.6710 | -0.2350 | -0.7805 | -0.3445 | -2.7100 | -2.5600 | 6 |
| P04-f | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | -0.1875 | -2.6350 | -0.0460 | 0.3900 | -0.4055 | 0.0305 | -2.7100 | -2.5600 | 6 |
| P04-g | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | 0.1875 | -2.6350 | -0.6710 | -0.2350 | -0.0305 | 0.4055 | -2.7100 | -2.5600 | 6 |
| P04-h | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | 0.5625 | -2.6350 | -0.0460 | 0.3900 | 0.3445 | 0.7805 | -2.7100 | -2.5600 | 6 |
| P04-i | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | 0.9375 | -2.6350 | -0.6710 | -0.2350 | 0.7195 | 1.1555 | -2.7100 | -2.5600 | 6 |
| P04-j | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | 1.3125 | -2.6350 | -0.0460 | 0.3900 | 1.0945 | 1.5305 | -2.7100 | -2.5600 | 6 |
| P04-k | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | -0.4530 | 1.6875 | -2.6350 | -0.6710 | -0.2350 | 1.4695 | 1.9055 | -2.7100 | -2.5600 | 6 |
| P04-l | Tube collar ring | 0.00583 | 95.51 | 0.4599 | 296.70 | 0.1720 | 2.0625 | -2.6350 | -0.0460 | 0.3900 | 1.8445 | 2.2805 | -2.7100 | -2.5600 | 6 |
| P05-a | Flare end fitting | 0.02750 | 450.57 | 1.4788 | 954.05 | -0.4530 | -2.0625 | -4.2650 | -0.7030 | -0.2030 | -2.3125 | -1.8125 | -4.4700 | -3.9894 | 14 |
| P05-b | Flare end fitting | 0.02750 | 450.57 | 1.4788 | 954.05 | -0.4530 | 1.6875 | -4.2650 | -0.7030 | -0.2030 | 1.4375 | 1.9375 | -4.4700 | -3.9894 | 14 |
| P06-a | Hex nut | 0.09876 | 1618.45 | 1.8726 | 1208.13 | -0.4530 | -2.0625 | -3.3497 | -0.7655 | -0.1405 | -2.4233 | -1.7017 | -3.5684 | -3.1309 | 22 |
| P06-b | Hex nut | 0.09876 | 1618.45 | 1.8726 | 1208.13 | -0.4530 | 1.6875 | -3.3497 | -0.7655 | -0.1405 | 1.3267 | 2.0483 | -3.5684 | -3.1309 | 22 |
| P07-a | Tube sheet | 0.44518 | 7295.15 | 16.4835 | 10634.52 | -0.0116 | -0.0000 | -2.5300 | -0.9200 | 0.8570 | -2.4650 | 2.4650 | -2.5600 | -2.5000 | 32 |
| P07-b | Tube sheet | 0.44518 | 7295.15 | 16.4835 | 10634.52 | -0.0116 | -0.0000 | 2.5300 | -0.9200 | 0.8570 | -2.4650 | 2.4650 | 2.5000 | 2.5600 | 32 |
| P08-01 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -2.3700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -2.4000 | -2.3400 | 38 |
| P08-02 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -2.2500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -2.2800 | -2.2200 | 38 |
| P08-03 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -2.1300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -2.1600 | -2.1000 | 38 |
| P08-04 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -2.0100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -2.0400 | -1.9800 | 38 |
| P08-05 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.8900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.9200 | -1.8600 | 38 |
| P08-06 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.7700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.8000 | -1.7400 | 38 |
| P08-07 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.6500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.6800 | -1.6200 | 38 |
| P08-08 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.5300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.5600 | -1.5000 | 38 |
| P08-09 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.4100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.4400 | -1.3800 | 38 |
| P08-10 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.2900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.3200 | -1.2600 | 38 |
| P08-11 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.1700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.2000 | -1.1400 | 38 |
| P08-12 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -1.0500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -1.0800 | -1.0200 | 38 |
| P08-13 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.9300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.9600 | -0.9000 | 38 |
| P08-14 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.8100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.8400 | -0.7800 | 38 |
| P08-15 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.6900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.7200 | -0.6600 | 38 |
| P08-16 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.5700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.6000 | -0.5400 | 38 |
| P08-17 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.4500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.4800 | -0.4200 | 38 |
| P08-18 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.3300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.3600 | -0.3000 | 38 |
| P08-19 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.2100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.2400 | -0.1800 | 38 |
| P08-20 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | -0.0900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -0.1200 | -0.0600 | 38 |
| P08-21 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.0300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.0000 | 0.0600 | 38 |
| P08-22 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.1500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.1200 | 0.1800 | 38 |
| P08-23 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.2700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.2400 | 0.3000 | 38 |
| P08-24 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.3900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.3600 | 0.4200 | 38 |
| P08-25 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.5100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.4800 | 0.5400 | 38 |
| P08-26 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.6300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.6000 | 0.6600 | 38 |
| P08-27 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.7500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.7200 | 0.7800 | 38 |
| P08-28 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.8700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.8400 | 0.9000 | 38 |
| P08-29 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 0.9900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 0.9600 | 1.0200 | 38 |
| P08-30 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.1100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.0800 | 1.1400 | 38 |
| P08-31 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.2300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.2000 | 1.2600 | 38 |
| P08-32 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.3500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.3200 | 1.3800 | 38 |
| P08-33 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.4700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.4400 | 1.5000 | 38 |
| P08-34 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.5900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.5600 | 1.6200 | 38 |
| P08-35 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.7100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.6800 | 1.7400 | 38 |
| P08-36 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.8300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.8000 | 1.8600 | 38 |
| P08-37 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 1.9500 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 1.9200 | 1.9800 | 38 |
| P08-38 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 2.0700 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 2.0400 | 2.1000 | 38 |
| P08-39 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 2.1900 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 2.1600 | 2.2200 | 38 |
| P08-40 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 2.3100 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 2.2800 | 2.3400 | 38 |
| P08-41 | Fin | 0.02302 | 377.22 | 1.3901 | 896.87 | -0.8443 | -0.0068 | 2.4300 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | 2.4000 | 2.4600 | 38 |
| P09 | End fin, thin | 0.01535 | 251.48 | 1.1825 | 762.92 | -0.8443 | -0.0068 | -2.4800 | -0.9200 | -0.7422 | -2.4650 | 2.4650 | -2.5000 | -2.4600 | 38 |
| P10 | Side channel, +Y | 0.93407 | 15306.68 | 30.3790 | 19599.31 | 0.0094 | 2.4773 | -0.0000 | -0.9200 | 0.9200 | 1.8400 | 2.8900 | -2.8750 | 2.8750 | 43 |
| P11 | Side channel, -Y | 0.91282 | 14958.47 | 30.3681 | 19592.28 | 0.0297 | -2.4763 | 0.0000 | -0.9200 | 0.9200 | -2.8900 | -1.8400 | -2.8750 | 2.8750 | 43 |
| P12-a | Fork clip | 0.00425 | 69.56 | 0.2615 | 168.71 | 0.9068 | 2.0550 | 2.5300 | 0.7700 | 0.9700 | 1.8675 | 2.2425 | 2.4600 | 2.6000 | 14 |
| P12-b | Fork clip | 0.00425 | 69.56 | 0.2615 | 168.71 | 0.9068 | -2.0550 | 2.5300 | 0.7700 | 0.9700 | -2.2425 | -1.8675 | 2.4600 | 2.6000 | 14 |
| P12-c | Fork clip | 0.00424 | 69.56 | 0.2615 | 168.71 | 0.9068 | -2.0550 | -2.5300 | 0.7700 | 0.9700 | -2.2425 | -1.8675 | -2.6000 | -2.4600 | 14 |
| P12-d | Fork clip | 0.00425 | 69.56 | 0.2615 | 168.71 | 0.9068 | 2.0550 | -2.5300 | 0.7700 | 0.9700 | 1.8675 | 2.2425 | -2.6000 | -2.4600 | 14 |
| P13-a | Spacer block | 0.00125 | 20.48 | 0.0850 | 54.84 | -0.0500 | 2.5530 | -2.2500 | -0.1000 | 0.0000 | 2.5280 | 2.5780 | -2.3750 | -2.1250 | 6 |
| P13-b | Spacer block | 0.00125 | 20.48 | 0.0850 | 54.84 | -0.0500 | 2.5530 | 2.2500 | -0.1000 | 0.0000 | 2.5280 | 2.5780 | 2.1250 | 2.3750 | 6 |
| P13-c | Spacer block | 0.00125 | 20.48 | 0.0850 | 54.84 | -0.0500 | -2.5530 | 2.2500 | -0.1000 | 0.0000 | -2.5780 | -2.5280 | 2.1250 | 2.3750 | 6 |
| P13-d | Spacer block | 0.00125 | 20.48 | 0.0850 | 54.84 | -0.0500 | -2.5530 | -2.2500 | -0.1000 | 0.0000 | -2.5780 | -2.5280 | -2.3750 | -2.1250 | 6 |
| P14 | Fan frame | 6.37720 | 104503.58 | 97.2375 | 62733.73 | 1.5716 | -0.0053 | 0.0079 | 0.9200 | 2.3960 | -2.4500 | 2.4500 | -2.4500 | 2.5684 | 205 |
| P15 | Fan hub (motor) | 3.52425 | 57752.12 | 13.0839 | 8441.23 | 1.7310 | 0.0000 | -0.0000 | 1.1700 | 2.2960 | -1.0000 | 1.0000 | -1.0000 | 1.0000 | 6 |
| P16-a | Fan blade | 0.13758 | 2254.57 | 4.7226 | 3046.86 | 1.7129 | -1.4713 | 0.7083 | 1.2001 | 2.1710 | -2.2714 | -0.5736 | -0.0000 | 1.5043 | 9 |
| P16-b | Fan blade | 0.13758 | 2254.57 | 4.7226 | 3046.86 | 1.7129 | 0.2190 | 1.6181 | 1.2001 | 2.1710 | -0.6694 | 1.0334 | 0.7986 | 2.2750 | 9 |
| P16-c | Fan blade | 0.13758 | 2254.57 | 4.7226 | 3046.86 | 1.7129 | 1.6066 | 0.2918 | 1.2001 | 2.1710 | 0.8090 | 2.2708 | -0.5241 | 1.2855 | 9 |
| P16-d | Fan blade | 0.13758 | 2254.57 | 4.7226 | 3046.86 | 1.7129 | 0.7739 | -1.4378 | 1.2001 | 2.1710 | -0.0263 | 1.7880 | -2.1548 | -0.5878 | 9 |
| P16-e | Fan blade | 0.13758 | 2254.57 | 4.7226 | 3046.86 | 1.7129 | -1.1283 | -1.1804 | 1.2001 | 2.1710 | -1.8907 | -0.3090 | -2.1277 | -0.2924 | 9 |
| P17 | Finger guard | 2.31122 | 37874.04 | 52.8212 | 34078.15 | 2.5360 | -0.0040 | -0.0006 | 2.3960 | 2.6760 | -2.2650 | 2.2650 | -2.2650 | 2.2650 | 143 |
| P18 | Power cord | 1.15306 | 18895.30 | 31.1893 | 20122.12 | 1.4793 | -4.9347 | 3.9799 | 1.2505 | 1.7080 | -8.6403 | -1.5257 | 1.6919 | 5.9418 | 26 |
| P19 | Plug body | 0.34939 | 5725.44 | 4.5642 | 2944.65 | 1.3005 | -9.1246 | 3.4235 | 0.9322 | 1.6687 | -9.7348 | -8.4310 | 2.7957 | 4.0041 | 147 |
| P20-a | Plug blade | 0.00911 | 149.22 | 0.4397 | 283.66 | 1.2951 | -9.6010 | 2.8031 | 1.1696 | 1.4206 | -9.9147 | -9.3191 | 2.5783 | 3.0065 | 10 |
| P20-b | Plug blade | 0.00911 | 149.22 | 0.4397 | 283.66 | 1.2951 | -9.8784 | 3.2143 | 1.1696 | 1.4206 | -10.1920 | -9.5964 | 2.9895 | 3.4177 | 10 |
| H1-a | Pan head screw | 0.04209 | 689.67 | 1.5517 | 1001.08 | 2.0008 | -2.0520 | 2.0635 | 0.9200 | 2.8260 | -2.1950 | -1.9050 | 1.9200 | 2.2100 | 95 |
| H1-b | Pan head screw | 0.04209 | 689.67 | 1.5517 | 1001.08 | 2.0008 | -2.0520 | -2.0615 | 0.9200 | 2.8260 | -2.1950 | -1.9050 | -2.2050 | -1.9150 | 95 |
| H1-c | Pan head screw | 0.04209 | 689.67 | 1.5517 | 1001.08 | 2.0008 | 2.0580 | -2.0615 | 0.9200 | 2.8260 | 1.9150 | 2.2050 | -2.2050 | -1.9150 | 95 |
| H1-d | Pan head screw | 0.04209 | 689.67 | 1.5517 | 1001.08 | 2.0008 | 2.0580 | 2.0635 | 0.9200 | 2.8260 | 1.9150 | 2.2050 | 1.9200 | 2.2100 | 95 |
| H2-a | Washer | 0.00125 | 20.50 | 0.1429 | 92.22 | 2.6935 | -2.0650 | 2.0600 | 2.6760 | 2.7110 | -2.2450 | -1.8850 | 1.8800 | 2.2400 | 6 |
| H2-b | Washer | 0.00125 | 20.50 | 0.1429 | 92.22 | 2.6935 | -2.0600 | -2.0650 | 2.6760 | 2.7110 | -2.2400 | -1.8800 | -2.2450 | -1.8850 | 6 |
| H2-c | Washer | 0.00125 | 20.50 | 0.1429 | 92.22 | 2.6935 | 2.0650 | -2.0600 | 2.6760 | 2.7110 | 1.8850 | 2.2450 | -2.2400 | -1.8800 | 6 |
| H2-d | Washer | 0.00125 | 20.50 | 0.1429 | 92.22 | 2.6935 | 2.0600 | 2.0650 | 2.6760 | 2.7110 | 1.8800 | 2.2400 | 1.8850 | 2.2450 | 6 |

**Whole assembly:** 103 bodies; total volume 27.29391 in3 (447267.00 mm3); total area 496.2401 in2 (320154.24 mm2);
centre of mass (0.8619, -0.3322, 0.1799) in; bounding box X [-0.92002, 2.826], Y [-10.19204, 2.89], Z [-4.47, 5.94183] in
(mm: X [-23.368, 71.780], Y [-258.878, 73.406], Z [-113.538, 150.922]).

**Key functional checks:** coil width over the bends 6.530 (z -3.273 to 3.257); channel length 5.75; height over the
channels 5.78 (y -2.89 to 2.89); depth from the channel back to the guard front 3.596; tube OD 0.375; tube pitch 0.75;
fin pitch 0.12 (41 fins + 1 end fin); fan frame 4.9 square, 1.476 deep; mounting slots 0.22 wide, 0.31 deep.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall depth | 3.60 (drawing), 3 5/8 (product data) | 3.596 (channel back x -0.92 to guard front x 2.676) | Follow the 3D. |
| Overall width | 6.53 (drawing), 6 1/2 (product data) | 6.530 over the tube bends | Follow the 3D. |
| Overall height | 5.78 (drawing), 5 3/4 (product data) | 5.78 over the channels | Follow the 3D. |
| Cord length | 2 ft (drawing note) | flat cord, 3.0 + 3.25-turn helix R2.0 + 3.0 (about 46.8 along its centreline) | Follow the 3D. |
| Row B position | - | x -0.47752 for legs, sheet holes and fins, x -0.453 for the -Z end parts | Reproduce both. |
| Screw / hole / washer centres | - | screws, frame holes, washers and channel holes differ by up to 0.015 (section 4) | Reproduce each as stated. |

**Undetermined:** the exact free-form blend between the cord exit boss and the frame corner surface; the exact flank
shape and root rounding of the screw thread (modelled free-form; pitch, crest diameter and hand are given); the exact
section orientation of the cord inside the helix (free-form sweep in the original); materials other than copper for tube
and fins; motor, wiring and water passages (not modelled).
