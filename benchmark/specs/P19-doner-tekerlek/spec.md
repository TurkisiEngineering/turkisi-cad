# Design specification: swivel plate caster, 4 in rubber-tread wheel, with foot-pedal total lock

Plate-mount swivel caster: a moulded plastic fork hangs under a stamped steel top plate on a kingpin; a 4 in wheel
(rubber tread on a plastic core) turns on an axle pin at a horizontal offset from the swivel axis; a foot pedal sits
between the fork legs at the rear. This document is the only source for the rebuild. Every dimension below was measured
from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres by multiplying every value by 25.4; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **+Y is up.** The top face of the top plate (the mounting face) is **y = 2.75**; the bottom of the wheel is
    **y = -2.75**.
  - **The swivel axis (kingpin axis) is the Y axis** (x = 0, z = 0).
  - **The wheel axis is the line x = 1.515, y = -0.75, parallel to Z.** The wheel therefore trails the swivel axis by
    1.515 toward +X. The brake pedal is at the +X end of the fork.
  - The whole assembly is **mirror-symmetric about the plane z = 0**, except the kingpin lug (P03, on -X) which is
    itself symmetric about z = 0 too. Nothing in the model is asymmetric in Z.
- **Profile coordinate conventions:**
  - "(x, y)" = profile in a plane normal to Z (side view); "(x, z)" = profile in a plane normal to Y (top view).
  - "(r, y)" = half-section of a body of revolution about the Y axis (r = radius from the Y axis).
  - "(rho, z)" = half-section of a body of revolution about the wheel axis (rho = radius from the wheel axis).
  - "arc R c=(a, b) to (p, q)" = circular arc of radius R about centre (a, b) from the current point to (p, q),
    the short way unless stated; "cw" / "ccw" are seen with the first coordinate to the right and the second up.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description

A U-shaped plastic **fork** (P01) carries the wheel between two legs. Its top ("crown") is round at the back (around the
swivel axis) and runs forward as a sloping deck. The **top plate** (P02) is a 0.1 thick steel plate with four mounting
slots and a pressed (dished) centre. A **kingpin** (P03) passes down through the plate centre and the fork deck. Between
the plate's pressed centre and the fork top sit a round **bearing washer** (P04) and a **hex bearing ring** (P05); the
swivel balls are not modelled. The **brake pedal** (P06) is a block that fills the space between the fork legs at the
rear and ends in a wider foot plate outside the fork.

The wheel consists of five solids: a **rubber tread** (P07), a thin **insert ring** (P08) under the tread, a solid
**core centre disc** (P09) and two dished **core side flanges** (P10-a on -Z, P10-b on +Z). An **axle pin** (H1)
passes through the fork legs and the wheel.

**Simplifications that exist in the source model and must be reproduced:**
- No balls, no seals, no bearing races other than P04 / P05, no brake mechanism inside the fork, no springs.
- The kingpin is not riveted over; its top is flush with the plate top (y = 2.75).
- The core centre disc P09 is a **solid disc without an axle hole**; the axle pin H1 passes straight through it
  (they overlap, see section 5). Reproduce as is.
- The axle pin is a plain cylinder: no head, no thread, no nut.
- No text, logos, ejector marks or tread pattern.

## 3. Part list

10 distinct custom parts and 1 hardware item, 11 distinct, **12 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Fork (swivel yoke), one moulding | custom | plastic, gray |
| P02 | 1 | Top plate, stamped | custom | zinc-plated steel |
| P03 | 1 | Kingpin with anti-rotation lug | custom | steel |
| P04 | 1 | Bearing washer, round | custom | steel |
| P05 | 1 | Hex bearing ring | custom | steel |
| P06 | 1 | Brake pedal | custom | plastic |
| P07 | 1 | Wheel tread | custom | rubber, gray |
| P08 | 1 | Wheel insert ring (thin sleeve between core and tread) | custom | plastic, white |
| P09 | 1 | Wheel core centre disc | custom | polypropylene |
| P10 | 2 | Wheel core side flange (P10-a at z < 0, P10-b at z > 0, mirror images about z = 0) | custom | polypropylene |
| H1 | 1 | Axle pin, plain cylinder | hardware | steel |

## 4. Part geometry

### P01 Fork (one solid, 111 faces in the original)

The fork is symmetric about z = 0. It is built from four volumes, then rounded:
**F = (OUTER + RIDGE) - GAP - holes**, then the edge rounds of F10.

**F1. Outer side profile P_out** (plane normal to Z, (x, y)). Closed contour, start at
A = (1.01841, -0.80829):
1. arc R0.5 c=(1.515, -0.75), ccw (under the axle), to (1.515, -1.25);
2. arc R0.5508 c=(1.515, -0.6992), ccw, to (2.0658, -0.6992);
3. line to (2.06496, 0.58138) (nearly vertical, leans 0.04 deg);
4. arc R0.683 c=(2.74786, 0.56946), cw (concave, the material is outside this circle), to (2.72879, 1.25219);
5. line to (3.54269, 1.27493) (rises 0.02274 over 0.8139);
6. arc R0.15 c=(3.5385, 1.42487), ccw, to (3.6885, 1.42487);
7. line (the leg end, x = 3.6885) to (3.6885, 1.61657);
8. arc R0.15 c=(3.5385, 1.61657), ccw, to (3.5987, 1.75396);
9. arc R8.622 c=(0.13847, -6.14324), ccw (the convex sloping top of the deck), to (1.28005, 2.40286);
10. line (front bevel) to (1.221, 2.464);
11. line (the flat top, y = 2.464) toward -X, past x = -1.029 (for example to (-1.2, 2.464));
12. down to the R2.5 circle and along **arc R2.5 c=(-1.46454, -1.09977)**, cw, back to A. On this circle
    y = 0.92634 at x = 0 and y = 1.3862 at x = -1.2. The material lies outside the R2.5 circle (this is the concave
    front edge of the legs, facing the wheel).

**OUTER** = P_out extruded symmetrically to **|z| <= 1.029**, then trimmed behind the swivel axis: keep the part with
x >= 0 plus the part inside the **cylinder of radius 1.029 about the Y axis**. Behind x = 0 the fork is therefore round
in top view (radius 1.029), in front of x = 0 it is bounded by the flat outer faces z = +/-1.029, and the flat faces are
tangent to the round at x = 0.

**F2. Ridge (raised band on the outer faces and around the crown).** Side profile R_xy (plane normal to Z), closed,
start at (-1.2, 2.098):
1. line (y = 2.098) to (0.21544, 2.098);
2. arc R1.3 c=(0.21544, 0.798), cw, to (0.42225, 2.08144);
3. arc R1.5 c=(0.18362, 0.60055), cw, to (1.656, 0.314);
4. arc R0.185 c=(1.471, 0.314), cw (a half circle through (1.471, 0.129)), to (1.286, 0.314);
5. arc R1.7 c=(-0.40784, 0.16942), ccw, to (1.2176, 0.66736);
6. arc R1.5 c=(-0.21661, 0.228), ccw (tangent continuation of the R1.7 arc), to its top point (-0.21661, 1.728);
7. line (y = 1.728) to (-1.2, 1.728); close.
**RIDGE** = R_xy extruded to **|z| <= 1.133**, kept for x >= 0 plus inside the **cylinder of radius 1.133 about Y**.
Result: on each flat outer face a curved band stands 0.104 proud (z from 1.029 to 1.133), shaped like a hook that runs
from the crown down the leg and ends in the R0.185 half circle above the axle; behind x = 0 it continues as a ring
band around the crown, radius 1.029 to 1.133, between y = 1.728 and y = 2.098. The band walls are normal to the outer
face (parallel to Z) and meet the outer face with a sharp concave edge.

**F3. GAP between the legs** (removed). In the region **|z| < 0.83**, remove:
- for x >= 0: the region below the ceiling contour, side profile (x, y): from (0, 2.184) along y = 2.184 to
  (1.10215, 2.184), line (bevel, parallel to the outer bevel and 0.28 below it) to (1.14698, 2.13758),
  arc R8.342 c=(0.13847, -6.14324), cw (concentric with the R8.622 top), to (2.4615, 1.86879); then a vertical wall at
  x = 2.4615 up through the top. For x > 2.4615 everything between the legs is removed (this is where the pedal sits).
  The gap is open downward (it runs out through the bottom of the legs).
- for x < 0: the inside of the **cylinder of radius 0.83 about the Y axis**, from the bottom up to the flat ceiling
  y = 2.184.
Result: two legs 0.199 thick (|z| from 0.83 to 1.029), joined by the deck (y 2.184 to 2.464, 0.28 thick) and the round
crown at the back; the inside of the U is a half cylinder R0.83 at the back.

**F4. Kingpin hole:** cylinder diameter 1.0 (R0.5) on the Y axis, through the deck from y = 2.184 to y = 2.464.

**F5. Axle bore:** diameter 0.6 (R0.3) on the wheel axis (x = 1.515, y = -0.75), through both legs.

**F6. Faces that result (check list):** outer faces z = +/-1.029; inner faces z = +/-0.83; top y = 2.464 (from the crown
round to x = 1.221); front bevel plane through (1.221, 2.464) and (1.28005, 2.40286), 46.0 deg from the top face
(normal (0.7193, 0.6947, 0)); top surface R8.622 to the leg end; leg end x = 3.6885; ceiling y = 2.184 inside the U;
gap end wall x = 2.4615 between y = 1.86879 and the R8.622 top (2.15992).

**F10. Edge rounds** (all convex, constant radius):
- **R0.06** on every edge of the two outer faces z = +/-1.029 with the side walls of P_out (R2.5, R0.5, R0.5508, the
  nearly vertical line, R0.683, the bottom line, the lower and upper R0.15 corners, R8.622, the bevel) and on the
  edges of the top face y = 2.464 with the outer faces and with the crown round (around the back, radius 1.029). In the
  section x = 0 these rounds reduce the outer face to the band between y = 0.99993 and y = 2.404. Where the R2.5 wall
  meets the crown round (behind x = 0) the R0.06 round runs on as a blend along their intersection curve.
- **R0.125** on the vertical edge between the leg end face x = 3.6885 and each outer face (the flat end face is left
  only for |z| <= 0.904); where it meets the R0.06 rounds of the two R0.15 corners there are small blends.
- **R0.04** on the outer (top) edges of the ridge: along both long edges of the band top face z = +/-1.133, around
  the R0.185 end, and on the two edges of the crown ring band (radius 1.133 with the planes y = 1.728 and y = 2.098).
  Where the R1.5 lower wall of the band runs into the crown ring (x between -0.217 and 0) the R0.04 round is a blend.
- No rounds on: the ridge foot (band wall to outer face), the inner faces z = +/-0.83 and the gap, the bores, the
  ceiling, the bottom edges of the gap.

### P02 Top plate (one solid, 45 faces)

**T1. Flat plate** between **y = 2.65 and y = 2.75** (0.1 thick), outline in (x, z): rectangle |x| <= 1.8125,
|z| <= 1.25 (3.625 x 2.5) with the four vertical corner edges rounded **R0.25** (centres (+/-1.5625, +/-1.0)).

**T2. Four mounting slots**, through the plate, one per quadrant: obround of width **0.3125** (end radius 0.15625),
long axis along X, end-arc centres at x = +/-1.40625 and x = +/-1.53125, z = +/-0.875. Slot centres at
(+/-1.46875, +/-0.875): centre to centre 2.9375 along X and 1.75 along Z; slot length 0.4375 overall.

**T3. Pressed centre** (body of revolution about the Y axis, replaces the plate inside r = 0.75). Half-section (r, y),
closed loop:
- top surface: from (0.719, 2.75) [flat top beyond] arc R0.25 c=(0.719, 2.5) (convex, turning down) to
  (0.57754, 2.70610); straight cone line down and inward to (0.37560, 2.56750) (the cone makes 34.458 deg with the
  plate plane, i.e. a half-angle of 55.542 deg about Y); arc R0.1 c=(0.319, 2.65) (concave) to (0.3595, 2.55860);
- centre hole: line straight down r = 0.3595 to y = 2.502; a 0.001 ledge out to (0.3605, 2.502); arc R0.015
  c=(0.3605, 2.487) to (0.3755, 2.487); line straight down r = 0.3755 to (0.3755, 2.45330) (the lowest point of the
  plate);
- bottom surface: arc R0.1 c=(0.35, 2.55) (convex) from (0.3755, 2.4533) to (0.40660, 2.46750); straight cone line up
  and outward (parallel to the upper one, same 55.542 deg half-angle) to (0.60855, 2.60610); arc R0.25 c=(0.75, 2.4)
  to (0.75, 2.65) and on as the flat underside y = 2.65.
So the centre is a conical dish 0.2967 deep below the top face, with a stepped hole: diameter 0.719 at the top part,
0.751 at the bottom lip (0.034 high).

### P03 Kingpin (one solid, 33 faces)

**K1. Body of revolution about the Y axis**, half-section (r, y), closed loop from the axis:
(0, 2.136) [apex of a drill-point cone] line to (0.236, 2.0728) (cone half-angle 75 deg, 150 deg included); line down
r = 0.236 to (0.236, 1.7767) [blind bore diameter 0.472, open at the bottom]; 45 deg chamfer to (0.2557, 1.757); bottom
face y = 1.757 to (0.2732, 1.757); 45 deg chamfer to (0.29285, 1.7767); shank r = 0.29285 (diameter 0.5857) up to
(0.29285, 2.367); concave round R0.015 c=(0.30785, 2.367) to (0.30785, 2.382); collar underside y = 2.382 to
(0.3605, 2.382); convex round R0.015 c=(0.3605, 2.397) to (0.3755, 2.397); collar r = 0.3755 (diameter 0.751) up to
(0.3755, 2.487); convex round R0.015 c=(0.3605, 2.487) to (0.3605, 2.502); collar top y = 2.502 in to (0.3115, 2.502);
concave round R0.015 c=(0.3115, 2.517) to (0.2965, 2.517); upper shank r = 0.2965 (diameter 0.593) up to
(0.2965, 2.7303); 45 deg chamfer to (0.2768, 2.75); flat top y = 2.75 to the axis.

**K2. Anti-rotation lug** on the -X side, on the collar top, from **y = 2.502 up to a flat top y = 2.6**. Plan outline
(x, z): a circular boss **R0.063 centred (-0.2965, 0)** (reaching x = -0.3595), joined to the upper shank (R0.2965) by
two concave rounds **R0.0394 centred (-0.3208, +/-0.0995)**; the outline runs: shank circle at (-0.2832, 0.0878),
concave R0.0394 to (-0.3115, 0.0612), boss R0.063 round the outside through (-0.3595, 0) to (-0.3115, -0.0612),
concave R0.0394 to (-0.2832, -0.0878), back along the shank. The lug walls are parallel to Y. The R0.015 round at the
collar top / upper shank (K1) stops at the lug.

### P04 Bearing washer (one solid, 8 faces)

Body of revolution about Y, half-section (r, y): bottom y = 2.464 from r = 0.401 to 0.872; outer r = 0.872 (diameter
1.744) up to y = 2.539; top y = 2.539 in to r = 0.5107; conical bore down and inward along the same 55.542 deg cone as
the plate underside (T3) to (0.4066, 2.4675); arc R0.1 c=(0.35, 2.55) (the same circle as the plate's lower R0.1) down to
(0.401, 2.464). The washer sits on the fork top (y = 2.464) and its bore touches the plate underside.

### P05 Hex bearing ring (one solid, 12 faces)

Regular hexagonal prism from **y = 2.539 to y = 2.614** (0.075 thick), **1.51 across flats**, two flats normal to Z
(z = +/-0.755), the other four at +/-60 deg; corners on the X axis at x = +/-0.87180. Bore (revolution about Y,
half-section (r, y)): from (0.5107, 2.539) up and outward along the 55.542 deg cone to (0.60855, 2.6061), then arc R0.25
c=(0.75, 2.4) (the same circle as the plate's lower R0.25) to (0.6208, 2.614). It stacks on P04 and touches the plate
underside.

### P06 Brake pedal (one solid, 72 faces)

The pedal is the union of a **stem** (between the fork legs) and a wider **foot plate**, plus six raised grip ribs.

**B1. Stem.** Side profile (x, y), extruded to **|z| <= 0.825** (0.005 clear of each fork leg). Closed contour, start
(2.4615, 1.18953):
1. line up (back face x = 2.4615) to (2.4615, 2.15992);
2. arc R8.622 c=(0.13847, -6.14324), cw (the same circle as the fork top), to (3.5987, 1.75396);
3. arc R0.15 c=(3.5385, 1.6166), cw, to (3.60992, 1.74847);
4. arc R9.0 c=(0.03345, -6.51039), cw, to (3.6885, 1.714);
5. line down (front face x = 3.6885) to (3.6885, 1.42487);
6. arc R0.15 c=(3.5385, 1.42487), cw, to (3.54269, 1.27493);
7. line (bottom, the same line as the fork bottom) to (2.72879, 1.25219);
8. arc R0.683 c=(2.74786, 0.56946), ccw (the same circle as the fork), to the start.

**B2. Foot plate**, from x = 3.6885 to x = 4.2985, = intersection of two extrusions, then rounded:
- Side profile (x, y) extruded to **|z| <= 1.05**, closed contour (symmetric about y = 1.5195), start (3.6885, 1.38078):
  line up to (3.6885, 1.65822); arc R0.05 c=(3.7385, 1.65822), cw, to (3.74187, 1.70811); top arc **R0.643
  c=(3.7857, 2.3496)** (concave upward, lowest point y = 1.7066 at x = 3.7857), ccw, to (4.08040, 1.77815); arc R0.15
  c=(4.1485, 1.6445), cw, to (4.2985, 1.6445); line down (front face) to (4.2985, 1.3945); arc R0.15
  c=(4.1485, 1.3945), cw, to (4.0804, 1.26085); bottom arc **R0.643 c=(3.7857, 0.6894)** (highest point y = 1.3324),
  ccw, to (3.74187, 1.33089); arc R0.05 c=(3.7385, 1.38078), cw, to the start.
- Plan outline (x, z) extruded along Y through the foot plate, closed, symmetric about z = 0: back x = 3.6885 for
  |z| <= 1.01; R0.04 corners c=(3.7285, +/-1.01) to (3.7285, +/-1.05); side lines z = +/-1.05 to x = 3.8139; arc R0.25
  c=(3.8139, +/-0.8) to (3.94710, +/-1.01157); arc **R1.0 c=(3.4144, +/-0.1653)** to (4.25988, +/-0.69922); arc R0.25
  c=(4.0485, +/-0.5657) to (4.2985, +/-0.5657); front line x = 4.2985 for |z| <= 0.5657. All these arcs are convex.
- **Rounds R0.04** on every edge where a side face of the plan outline (the flats z = +/-1.05, the R0.25, R1.0 and R0.25
  arcs) meets the top or bottom surfaces of the side profile (R0.643 arcs, R0.15 nose corners, R0.05 back corners).
  Along the flats z = +/-1.05 these are exact tori (major radius 0.683 about the R0.643 centres, 0.01 about the R0.05
  centres); where the curved plan arcs meet the curved profile they are blends of the same R0.04.
- The foot plate's back face x = 3.6885 is exposed only outside the stem (|z| from 0.825 to 1.01 between y = 1.38078 and
  1.65822, and below the stem between y = 1.38078 and 1.42487). Above the foot plate's back top corner the stem front face
  rises to y = 1.714, a 0.0558 step.

**B3. Grip ribs** (raised, half-round, added): cylinders **R0.025** parallel to Z with flat ends:
- three on the stem top, |z| <= 0.675, axes at (2.5865, 2.1107), (2.7115, 2.0682), (2.8365, 2.0334);
- three on the foot plate top, |z| <= 0.875, axes at (3.7885, 1.7045), (3.8885, 1.7140), (3.9885, 1.7376).
Each rib is the part of its cylinder outside the stem / foot plate (the axes lie 0.001 to 0.018 below the surface, so each rib
shows as a low half-round bead). No rounds on the stem edges.

### P07 Wheel tread (one solid, 10 faces)

Ring about the wheel axis: bore **rho = 1.56375** (diameter 3.1275), outer **rho = 2.0** (diameter 4.0), width
**|z| <= 0.625** (1.25). The two outer edges are rounded **R0.2** (section (rho, z): centres (1.8, +/-0.425)); the flat
side faces run from rho = 1.56375 to 1.8, the cylindrical tread from z = -0.425 to 0.425. Inner edges sharp.

### P08 Wheel insert ring (one solid, 6 faces)

Plain ring: rho from **1.51375 to 1.56375** (0.05 wall), |z| <= 0.625. It fills the space between the core and the tread
(face contact on both sides).

### P09 Wheel core centre disc (one solid, 4 faces)

Solid cylinder **rho <= 1.51375** (diameter 3.0275), **|z| <= 0.3125**. No hole.

### P10 Wheel core side flange (P10-a at z < 0; P10-b its mirror image about z = 0; 11 faces each)

Described for P10-a. Body of revolution about the wheel axis, half-section (rho, z):
- inner (flat) face **z = -0.3125** from the hub hole rho = 0.305 to the rim rho = 1.51375 (contact with P09);
- rim cylinder **rho = 1.51375** from z = -0.3125 out to z = -0.61060;
- convex round **R0.02** c=(rho 1.49375, z -0.6106) from the rim onto the outer face;
- **dished outer face**: in the half-section it is an arc of **radius 3.75269 centred at (rho 0.305, z +2.92770)**
  (the surface is a torus: tube radius 3.75269 about a centre circle of radius 0.305 in the plane z = 2.9277). It is
  lowest (z = -0.82499) at the hub and rises toward the rim (z about -0.6296 where the rim round starts);
- convex round **R0.02** c=(rho 0.325, z -0.8049) from the dished face into the hub hole;
- hub hole **rho = 0.305** (diameter 0.61) from z = -0.8049 to the inner face z = -0.3125.
P10-b: the same with z replaced by -z (dish centre at z = -2.9277, inner face z = +0.3125).

### H1 Axle pin (one solid, 4 faces)

Solid cylinder **diameter 0.6** on the wheel axis from **z = -1.034 to z = 1.034** (length 2.068). Sharp ends. It fills
the fork axle bores exactly (same radius 0.3) and stands 0.005 proud of each fork outer face.

## 5. Assembly

All twelve bodies are built in place with identity placement, wheel and swivel in the positions of section 1.

- **Mount stack on the swivel axis:** plate P02 (top y = 2.75); hex ring P05 (y 2.539 to 2.614) and washer P04
  (y 2.464 to 2.539) between the plate's pressed cone and the fork top y = 2.464; fork P01; kingpin P03 from y = 1.757
  (inside the fork U) to y = 2.75 (flush with the plate top). The kingpin collar (diameter 0.751, y 2.382 to 2.502) sits
  inside the fork kingpin hole (diameter 1.0) and inside the plate's bottom lip (diameter 0.751, face contact); the lug
  sits in the plate's centre hole (diameter 0.719, the lug reaches r = 0.3595, face contact).
- The hex ring corners point along X; the plate slots run along X; the pedal is at +X.
- **Wheel on the axle (x = 1.515, y = -0.75):** core disc P09 (|z| <= 0.3125), side flanges P10-a / P10-b against
  its faces, insert ring P08 around the core and flanges, tread P07 around the ring. Wheel bottom y = -2.75, wheel top
  y = 1.25. The flanges' hub holes (diameter 0.61) clear the axle pin (diameter 0.6).
- **Axle pin H1** passes through both fork legs and through the solid core disc: **interference P09-H1 = 2895.83 mm3
  (0.17671 in3, the pin volume inside |z| <= 0.3125). Reproduce as is.** No other body pair overlaps (other contacts are
  face contacts with zero overlap).
- **Pedal P06** between the legs: |z| <= 0.825 against the leg inner faces |z| = 0.83 (0.005 clearance), its top on the
  same R8.622 circle as the fork top, its back face x = 2.4615 against the fork gap end wall.

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (axle
pin 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Fork | 5.06749 | 83041.35 | 50.1952 | 32383.96 | 0.9987 | 1.5153 | 0.0000 | -1.1330 | 3.6885 | -1.2500 | 2.4640 | -1.1330 | 1.1330 | 111 |
| P02 | Top plate | 0.83205 | 13634.85 | 18.5321 | 11956.18 | 0.0000 | 2.6876 | 0.0000 | -1.8125 | 1.8125 | 2.4533 | 2.7500 | -1.2500 | 1.2500 | 45 |
| P03 | Kingpin | 0.23072 | 3780.80 | 3.1492 | 2031.77 | -0.0009 | 2.3584 | 0.0000 | -0.3755 | 0.3755 | 1.7570 | 2.7500 | -0.3755 | 0.3755 | 33 |
| P04 | Bearing washer | 0.12992 | 2129.02 | 4.2445 | 2738.41 | 0.0000 | 2.5004 | 0.0000 | -0.8720 | 0.8720 | 2.4640 | 2.5390 | -0.8720 | 0.8720 | 8 |
| P05 | Hex bearing ring | 0.07254 | 1188.77 | 2.7849 | 1796.70 | 0.0000 | 2.5740 | 0.0000 | -0.8718 | 0.8718 | 2.5390 | 2.6140 | -0.7550 | 0.7550 | 12 |
| P06 | Brake pedal | 1.90479 | 31213.86 | 11.7309 | 7568.34 | 3.2588 | 1.5941 | 0.0000 | 2.4615 | 4.2985 | 1.1895 | 2.1599 | -1.0500 | 1.0500 | 72 |
| P07 | Wheel tread | 5.89220 | 96555.90 | 35.5529 | 22937.33 | 1.5150 | -0.7500 | 0.0000 | -0.4850 | 3.5150 | -2.7500 | 1.2500 | -0.6250 | 0.6250 | 10 |
| P08 | Wheel insert ring | 0.60427 | 9902.14 | 25.1375 | 16217.68 | 1.5150 | -0.7500 | 0.0000 | -0.0487 | 3.0787 | -2.3138 | 0.8137 | -0.6250 | 0.6250 | 6 |
| P09 | Wheel core centre disc | 4.49923 | 73729.17 | 20.3420 | 13123.86 | 1.5150 | -0.7500 | 0.0000 | 0.0013 | 3.0288 | -2.2638 | 0.7638 | -0.3125 | 0.3125 | 4 |
| P10-a | Core side flange, -Z | 2.93150 | 48038.63 | 17.8824 | 11537.03 | 1.5150 | -0.7500 | -0.5290 | 0.0013 | 3.0288 | -2.2638 | 0.7638 | -0.8249 | -0.3125 | 11 |
| P10-b | Core side flange, +Z | 2.93150 | 48038.63 | 17.8824 | 11537.03 | 1.5150 | -0.7500 | 0.5290 | 0.0013 | 3.0288 | -2.2638 | 0.7638 | 0.3125 | 0.8249 | 11 |
| H1 | Axle pin | 0.58471 | 9581.73 | 4.4636 | 2879.72 | 1.5150 | -0.7500 | 0.0000 | 1.2150 | 1.8150 | -1.0500 | -0.4500 | -1.0340 | 1.0340 | 4 |

**Whole assembly:** 12 bodies; total volume 25.68092 in3 (420834.84 mm3, the sum of the bodies, P09-H1 overlap
counted twice); total area 211.8978 in2 (136708.01 mm2); centre of mass (1.4678, 0.0360, 0.0000) in; bounding box
X [-1.8125, 4.2985], Y [-2.75, 2.75], Z [-1.25, 1.25] in (mm: X [-46.0375, 109.1819], Y [-69.85, 69.85],
Z [-31.75, 31.75]).

**Key functional checks:** mounting height 5.5 (wheel bottom to plate top); wheel diameter 4.0, width 1.25; swivel
offset 1.515 (kingpin axis to axle axis, along X); plate 3.625 x 2.5 x 0.1; slots 2.9375 x 1.75 on centres, 0.3125
wide; fork legs 0.199 thick with a 1.66 gap; fork outer width 2.058 (2.266 over the ridges).

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Plate length | 3.625 (drawing); 3 11/16 (product data) | 3.625 | Follow the 3D. |
| Slot spacing along | 2.938 (drawing); 2 15/16 (product data) | 2.9375 | Agree. |
| Wheel bearing / swivel bearing | sealed ball bearings | not modelled (solid core, plain axle, washer and hex ring only) | Follow the 3D. |
| Total lock mechanism | pedal brakes the wheel and locks the swivel | pedal block only, no mechanism | Follow the 3D. |

**Undetermined:** the real ball bearings, the brake and swivel-lock mechanism, the rivet head of the kingpin, the
fasteners (not included). The exact shape of the small blend patches named in F10 and B2 (where two rounds meet) is
not given beyond their radii; any smooth blend of that radius is acceptable.
