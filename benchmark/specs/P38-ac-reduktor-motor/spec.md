# Design specification: synchronous motor with gearbox, small assembly

## 1. Units, frame, deliverable

- **Units: inch.** Every length below is in inch, every angle in degrees. (The source model is inch-based; values are round in
  inch.) Your STEP may be written in any unit the exporter supports, as long as the geometry is at the true size.
- **Global frame (use it exactly, do not re-centre or rotate anything):**
  - **+Z** = the output-shaft direction. The output shaft tip is at Z = +0.67, the bottom of the motor can at Z = -0.67.
  - **X = 0** is the mirror plane of the whole product (everything is symmetric about X = 0 except the D-flat of the output
    shaft, the boss pattern on the cover and the two bottom holes / two wide slots of the motor can, which are listed exactly).
  - **Y** runs along the "pear" outline of the gearbox, from the lead-wire exit (Y negative) to the output shaft (Y positive).
  - Two vertical axes (parallel to Z) carry most of the geometry:
    - **Motor axis M** through (X, Y) = (0, -0.3396).
    - **Output axis S** through (X, Y) = (0, 0.71). M to S distance = 1.0496.
  - Z = 0 is the plane of the output hub's lower face and of the rotor pin's lower end.
- **Deliverable:** one STEP file with **14 separate solids** (one solid per body in section 3, not fused). Body names are given
  for reference; the grader matches bodies by shape and position.
- The source model has no empty shells (0 dropped). All bodies are closed solids.

## 2. Product

A small synchronous (constant-speed) AC gearmotor: a round motor can on the back of a flat, pear-shaped gearbox, an output
shaft with a D-profile on the gearbox front, two mounting ears with holes, and two lead wires leaving the motor can on the
-Y side. Product data (for context only, not modelled): 115 V AC single phase, 50/60 Hz, about 1.5 rpm, 6.9 in·lbf rated
torque, sleeve bearings, spur gears in acetal, zinc-plated steel enclosure, wire leads.

Source simplifications (keep them):
- No gears, rotor, windings or bearings inside: the gearbox is an empty sheet-metal cup closed by a solid cover plate; the
  motor is an empty can with one solid stator disc inside.
- The lead wires are straight, 6.0 long insulated cylinders; each ends in a short twisted stranded conductor (section 4.13).
- The cover plate is a solid 0.05 plate (no inner detail); the bosses on it are small solid cones.
- Bodies touch each other face-to-face; nothing in the source overlaps by more than 2 mm³ (see section 7).

## 3. Part list (14 solids)

| Name | Count | Kind | Description |
|---|---|---|---|
| P01 | 1 | custom | Gearbox housing: drawn 0.02 sheet cup, pear outline, 9 crimp tabs, 2 mounting ears |
| P02 | 1 | custom | Gearbox cover plate, 0.05 thick, raised pad, 7 conical bosses, 2 holes |
| P03 | 1 | custom | Motor can: drawn 0.02 sheet cup Ø1.75, bottom holes and slots, rolled bead, lead notch |
| P04 | 1 | custom | Stator disc Ø1.61 × 0.05 inside the can |
| P05 | 1 | custom | Output hub Ø0.4 with counterbore and lower pin |
| P06 | 1 | custom | Output shaft Ø0.25 with a half-section D-profile |
| P07 | 1 | custom | Rotor pin Ø0.1 with domed end (motor axis, through the cover) |
| P08 | 1 | custom | Hub bearing tube Ø0.1 / Ø0.08 under the hub |
| P09 | 1 | custom | Lead guide channel (thin U plate inside the can at the lead exit) |
| P10 | 1 | custom | Lead grommet block with two square lead holes |
| W1-a, W1-b | 2 | hardware | Lead insulation, Ø0.08 × 6.0 (identical, placed at X = +0.0475 and X = -0.0475) |
| W2-a, W2-b | 2 | hardware | Stripped, twisted 15-strand conductor end, 0.25 long (identical, same two X positions) |

Distinct part kinds: 12 (P01–P10, W1, W2). Equivalence groups: W1-a = W1-b (mirror-identical, a cylinder), W2-a = W2-b
(**translated** copy, ΔX = -0.095; the twist sense is the same, it is not mirrored).

## 4. Body geometry

Notation: "Pear outline O(r1, r2)" = the convex outline formed by a circle of radius r1 about axis M, a circle of radius r2
about axis S, and the two straight lines tangent to both (external tangents). For all outlines used here r1 - r2 = 0.3704, so
the tangent lines always have the same outward unit normals **n+ = (0.935662, 0.352896)** (right line, X > 0) and
**n- = (-0.935662, 0.352896)** (left line). A right tangent line with circle radius r1 about M is the line
n+ · (x, y) = r1 - 0.119843 (0.119843 = 0.352896 × 0.3396). The tangent points on the M circle are at polar angle
20.665° (right) and 159.335° (left) about M; on the S circle at the same angles about S.
Along-wall coordinate on the right tangent wall: u = t · (x, y) with t = (-0.352896, 0.935662).

### 4.1 P01 gearbox housing (sheet thickness 0.02)

A drawn cup, open towards +Z.
- **Cup**: outer outline O(0.9404, 0.57) extruded from Z = -0.2 to Z = 0.276; hollowed by the inner outline O(0.9204, 0.55)
  from Z = -0.18 up through the top. So walls and floor are 0.02 thick; floor from Z = -0.2 to -0.18; rim at Z = 0.276.
- **Floor-to-wall edge rounds**: outer edge R0.03 (all around, the lower outer edge at Z = -0.2), inner edge R0.01 (at
  Z = -0.18). The bottom face of the floor is therefore flat inside O(0.9104, 0.54).
- **Floor holes**: Ø1.69 (R0.845) about M (the opening to the motor can) and Ø0.1 about S.
- **9 crimp tabs** at the rim. Each tab site has a **notch** cut through the wall from the rim down to Z = 0.246, 0.08 wide
  (measured between two parallel planes, ±0.04 from the tab centre line). Inside the notch a **tab 0.07 wide** (±0.035)
  rises from the wall and is bent inward over the cover plate:
  - tab section (in the plane through the tab centre line, r = distance from the tab's reference axis or wall line,
    see below): the wall continues to Z = 0.246; on top of it a quarter-round of **R0.02** centred at (r = inner wall, Z = 0.246)
    turning from the outer wall face (r = inner wall + 0.02, Z = 0.246) to the top (r = inner wall, Z = 0.266); then a flat
    lip from Z = 0.246 to Z = 0.266 reaching inward to a flat **end face** (sharp inside corner, no inner radius). The lip
    underside lies on Z = 0.246, the cover top plane.
  - Arc tabs: the R0.02 bend is a torus about the arc's axis; tab sides and notch sides are planes parallel to the radial
    direction through the tab centre; the end face is a plane normal to that radial direction.
  - Straight tabs: the bend is a cylinder R0.02 along the wall line; end face parallel to the wall.

  | Tab | Position (tab centre line) | Inner wall | End face (distance from axis / line) |
  |---|---|---|---|
  | T1, T2 | radial from M at 0° and 180° (the ±X sides, Y = -0.3396) | R0.9204 about M | 0.909748 from M |
  | T3 | radial from M at 270° (bottom, X = 0) | R0.9204 about M | 0.909748 from M |
  | T4, T5 | radial from M at 315° and 225° | R0.9204 about M | 0.909748 from M |
  | T6, T7 | radial from S at 45° and 135° | R0.55 about S | 0.538595 from S |
  | T8 | right tangent wall, centre at u = 0.348070 | n+ · p = 0.800556 | n+ · p = 0.790556 |
  | T9 | mirror of T8 (left tangent wall) | | |

  (Angles are polar angles about the axis, from +X counter-clockwise seen from +Z.)
- **2 mounting ears** (the +X ear is given; the -X ear is its mirror in X = 0). Each ear is a flat flange 0.02 thick
  (Z = 0.256 to 0.276) bent outward from the wall top:
  - **Ear zone on the wall**: between line A, n_A · p = 0.730294 with n_A = (0.769221, -0.638982), and line B,
    n_B · p = 0.179151 with n_B = (-0.178528, 0.983935) (the ear side lies on n_A · p < 0.730294 and n_B · p < 0.179151; only
    the part of the wall with X > 0.6 is concerned). Line A crosses the large arc near (0.89, -0.07); line B crosses the right
    tangent wall near (0.75, 0.32). In this zone the wall stops at Z = 0.251 and turns outward through a **bend**: a
    quarter-round with outer radius **R0.025** and inner radius **R0.005**, both centred on the bend axis at Z = 0.251, the
    bend axis following the contour 0.005 outside the outer wall (radius 0.9454 about M on the arc, the line
    n+ · p = 0.825557 on the tangent wall). The bend joins the wall (r from inner wall to outer wall at Z = 0.251) to the
    flange (Z = 0.256 to 0.276).
  - **Flange outline** (Z = 0.256 to 0.276): starts on the bend axis contour, from the point where line B meets
    n+ · p = 0.825557 (0.761537, 0.320251), along that line to its tangent point (0.884575, -0.005972), along the R0.9454 arc
    about M to line A (0.902139, -0.056887), along line A to (1.050191, 0.121343), round the **R0.14 end arc** centred at
    **(0.9425, 0.2108)** (through (1.0825, 0.2108)) to (0.917506, 0.348551), back along line B. Lines A and B are tangent to the
    R0.14 arc.
  - **Ear hole Ø0.14** at (±0.9425, 0.2108), through the flange. Ear hole spacing 1.885.
  - **Relief slots**: on the outer side of each ear side line the wall is slit 0.005 wide (between n_A · p = 0.730294 and
    0.735294, and between n_B · p = 0.179151 and 0.184151) from the rim down to Z = 0.246, through the wall thickness.
  - Outside the ear zones and notches the rim is at Z = 0.276 (flat, sharp edges).

### 4.2 P02 gearbox cover plate

- **Plate**: outline O(0.9204, 0.55) (fits the housing's inner wall exactly), Z = 0.196 to 0.246 (0.05 thick). Top outer
  edge rounded **R0.01** (bottom edge sharp).
- **Holes**: Ø0.4 about S, through, its top edge rounded R0.01; Ø0.1 about M, through plate and pad, sharp.
- **Raised pad**, Z = 0.246 to 0.256 (0.01 high), its whole top edge rounded **R0.01** (a full quarter-round, so the pad has
  no vertical side face). Pad footprint at Z = 0.246: arc R0.6204 about M (lower part), two corner arcs R0.15 centred at
  (±0.310544, 0.17), the straight top edge Y = 0.32 between (±0.310544, 0.32), and two side lines tangent to the R0.6204 arc
  and the corner arcs (normals n+ / n-, i.e. n+ · p = 0.500557). The flat pad top (Z = 0.256) is the same outline offset
  inward by 0.01 (R0.6104, R0.14, Y = 0.31).
- **7 conical bosses** on the pad: each a 45° cone frustum from Ø0.1 at Z = 0.256 to the top plane Z = 0.266, top edge
  rounded R0.01 (flat top Ø≈0.0717). Centres (X, Y):
  (0, 0.17), (0.45, -0.0896), (0.45, -0.6096), (0.33, -0.5896), (0.05, -0.6896), (0.11, -0.8096), (-0.25, -0.5896).

### 4.3 P03 motor can (sheet thickness 0.02)

Revolved about axis M, open towards +Z (rim at Z = -0.2, against the housing floor). Half-section (r = radius from M):
- outer wall r = 0.875 from Z = -0.2 down to -0.57; a concave **bead** arc R0.065 centred at (r 0.935, Z -0.595) to
  (0.875, -0.62); r = 0.875 down to -0.64; outer bottom corner R0.03 centred (0.845, -0.64) to (0.845, -0.67); bottom face
  Z = -0.67 to the axis.
- inside: bottom Z = -0.65 out to r 0.845; inner corner R0.01 centred (0.845, -0.64) to (0.855, -0.64); inner wall r = 0.855 up
  to the bead; inner bead arc R0.085 centred (0.935, -0.595) (it bulges inward to r 0.85 at Z -0.595, meeting r = 0.855 at
  Z = -0.623723 and -0.566277); inner wall r = 0.855 up to Z = -0.2.
- **Bottom openings** (through the 0.02 bottom), positions as polar angle about M:
  - centre hole Ø0.1 on M;
  - two holes Ø0.15 on radius 0.595 at 45° and 225° (centres (0.420729, 0.081129) and (-0.420729, -0.760329));
  - four radial slots, each from radius 0.2975 to 0.76125 (square ends): two 0.1 wide at 90° and 270° (along X = 0), two
    0.2 wide at 160° and 340°; each slot symmetric about its radial centre line.
- **Lead notch**: the wall is cut away on the -Y side between X = -0.125 and X = 0.125, from the rim (Z = -0.2) down to
  Z = -0.5525 (flat notch bottom, sharp corners).

### 4.4 P04 stator disc
Cylinder Ø1.61 about M, Z = -0.63 to -0.58.

### 4.5 P05 output hub (about S)
- Cylinder Ø0.4 from Z = 0 to 0.406, top outer edge rounded R0.01.
- Counterbore Ø0.25 from the top down to Z = 0.306 (flat bottom), its top edge rounded R0.01.
- Pin below: Ø0.07 from Z = 0 down to Z = -0.185; end face: flat annulus at Z = -0.185 from Ø0.07 to Ø0.05, then a
  spherical dome R0.028333 centred on S at Z = -0.171667 (apex at Z = -0.2).

### 4.6 P06 output shaft (about S)
- Cylinder Ø0.25 from Z = 0.306 (sits on the hub counterbore floor) to Z = 0.67.
- **D-profile**: above Z = 0.406 the half X < 0 is removed (flat face on the plane X = 0, 0.264 long, from the step at
  Z = 0.406 to the end at Z = 0.67).
- Chamfers 0.01 × 45°: on the half-circle step edge at Z = 0.406 (X < 0 half) and on the half-circle end edge at Z = 0.67
  (X > 0 half). The straight edges of the flat are sharp.

### 4.7 P07 rotor pin (about M)
Cylinder Ø0.1 from Z = 0 to Z = 0.236, closed by a spherical cap R0.0725 centred on M at Z = 0.1835 (apex Z = 0.256; the cap
meets the cylinder with an edge, not tangent). It passes through the Ø0.1 cover hole.

### 4.8 P08 hub bearing tube (about S)
Tube Ø0.1 outside, Ø0.08 inside, Z = -0.2 to 0 (in the Ø0.1 floor hole of P01, around the hub pin).

### 4.9 P09 lead guide channel
A U-shaped thin part inside the can at the lead exit, Z = -0.65 to -0.2:
- plate X = -0.225..0.225, Y = -1.14085..-1.13085 (0.01 thick);
- two side legs 0.01 thick, X = 0.215..0.225 and X = -0.225..-0.215, from Y = -1.14085 back (towards -Y) to the can's inner
  wall cylinder (R0.855 about M), which bounds them.

### 4.10 P10 lead grommet
Prism along Y from Y = -1.28 to Y = -1.14085. Section (X, Z): rectangle X = -0.11..0.11, Z = -0.5325..-0.4225, its two
lower corners rounded R0.02 (centres (±0.09, -0.5125)). Two rectangular through holes along Y: X = 0.0075..0.095 and
X = -0.095..-0.0075, both Z = -0.5175..-0.4375 (0.0875 × 0.08).

### 4.11 W1 lead insulation (W1-a at X = +0.0475, W1-b at X = -0.0475)
Cylinder Ø0.08 along Y, axis (X, Z) = (±0.0475, -0.4775), from Y = -1.14085 to Y = -7.14085 (6.0 long). The free end has a
centred recess Ø0.06, 0.03 deep (flat bottom at Y = -7.11085).

### 4.12 Placement summary of the lead parts
| Body | Axis (X, Z) | Y range |
|---|---|---|
| W1-a | (0.0475, -0.4775) | -7.14085 .. -1.14085 |
| W1-b | (-0.0475, -0.4775) | -7.14085 .. -1.14085 |
| W2-a | (0.0475, -0.4775) | -7.36085 .. -7.11085 |
| W2-b | (-0.0475, -0.4775) | -7.36085 .. -7.11085 |

### 4.13 W2 stripped twisted conductor (freeform)
- Starts at the bottom of the insulation recess (Y = -7.11085) and ends at Y = -7.36085 (0.25 long; 0.22 outside the
  insulation).
- **Section** (in every plane Y = const): the filled outer boundary of 15 circles of radius 0.0075 whose centres lie on a
  circle of radius 0.0225 about the wire axis, spaced 24° (a scalloped disc, overall Ø0.06, no hole in the middle).
- Strand angle θ = atan2(Z - Zc, X - Xc) about the wire axis (Xc = ±0.0475, Zc = -0.4775). At Y = -7.11085 the strand
  centres are at θ = -90° + 24°·k (k = 0..14). The section turns about the wire axis by Δ(Y) (θ decreases as Y decreases),
  total -180°, so at Y = -7.36085 the centres are at θ = +90° + 24°·k:

  | Y | -7.11085 | -7.13585 | -7.16085 | -7.18585 | -7.21085 | -7.23585 | -7.26085 | -7.28585 | -7.31085 | -7.33585 | -7.36085 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Δ (deg) | 0 | 0 | -2.94 | -13.65 | -30.96 | -53.07 | -77.62 | -104.71 | -131.75 | -157.25 | -180 |

  A smooth loft through these 11 rotated sections reproduces the source within about 0.15 % volume. The ends are flat.
- W2-b is W2-a moved by ΔX = -0.095 (same twist).

## 5. Assembly relations (all already given by the coordinates above)
- Cover P02 sits inside the housing P01: its outline equals the housing's inner wall; its top
  (Z = 0.246) carries the tab lips.
- Motor can P03 rim (Z = -0.2) touches the housing floor underside; can and housing share axis M.
- Output hub P05 passes through the Ø0.4 cover hole; shaft P06 sits in the hub counterbore; tube P08 surrounds the hub pin.
- Rotor pin P07 passes through the Ø0.1 cover hole on M.
- Grommet P10 sits in the can's lead notch; leads W1 pass through the grommet holes and start at the guide plate P09
  (Y = -1.14085).

## 6. Target table (original STEP, per body)

V = volume, A = surface area, CoM = centre of mass, bbox in inch; faces = source face count (for information only).

| Body | Description | V in³ | V mm³ | A in² | A mm² | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Gearbox housing | 0.09087 | 1489.07 | 9.3942 | 6060.77 | 0.0000 | 0.0669 | -0.0131 | -1.0825 | 1.0825 | -1.2800 | 1.2800 | -0.2000 | 0.2760 | 162 |
| P02 | Gearbox cover plate | 0.17879 | 2929.88 | 7.0459 | 4545.71 | 0.0004 | -0.1261 | 0.2232 | -0.9204 | 0.9204 | -1.2600 | 1.2600 | 0.1960 | 0.2660 | 64 |
| P03 | Motor can | 0.08799 | 1441.98 | 9.0467 | 5836.56 | 0.0000 | -0.3223 | -0.5349 | -0.8750 | 0.8750 | -1.2146 | 0.5354 | -0.6700 | -0.2000 | 48 |
| P04 | Stator disc | 0.10179 | 1668.06 | 4.3246 | 2790.03 | 0.0000 | -0.3396 | -0.6050 | -0.8050 | 0.8050 | -1.1446 | 0.4654 | -0.6300 | -0.5800 | 4 |
| P05 | Output hub | 0.04680 | 766.84 | 0.8727 | 563.02 | 0.0000 | 0.7100 | 0.1821 | -0.2000 | 0.2000 | 0.5100 | 0.9100 | -0.2000 | 0.4060 | 16 |
| P06 | Output shaft | 0.01135 | 185.99 | 0.3417 | 220.42 | 0.0303 | 0.7100 | 0.4593 | -0.1250 | 0.1250 | 0.5850 | 0.8350 | 0.3060 | 0.6700 | 9 |
| P07 | Rotor pin | 0.00194 | 31.73 | 0.0911 | 58.78 | -0.0000 | -0.3396 | 0.1233 | -0.0500 | 0.0500 | -0.3896 | -0.2896 | 0.0000 | 0.2560 | 5 |
| P08 | Hub bearing tube | 0.00057 | 9.27 | 0.1188 | 76.61 | -0.0000 | 0.7100 | -0.1000 | -0.0500 | 0.0500 | 0.6600 | 0.7600 | -0.2000 | 0.0000 | 6 |
| P09 | Lead guide channel | 0.00225 | 36.86 | 0.4692 | 302.72 | -0.0000 | -1.1376 | -0.4250 | -0.2250 | 0.2250 | -1.1671 | -1.1309 | -0.6500 | -0.2000 | 10 |
| P10 | Lead grommet | 0.00140 | 22.87 | 0.2027 | 130.80 | 0.0000 | -1.2104 | -0.4766 | -0.1100 | 0.1100 | -1.2800 | -1.1409 | -0.5325 | -0.4225 | 16 |
| W1-a | Lead insulation, +X | 0.03007 | 492.83 | 1.5237 | 983.01 | 0.0475 | -4.1324 | -0.4775 | 0.0075 | 0.0875 | -7.1409 | -1.1408 | -0.5175 | -0.4375 | 7 |
| W1-b | Lead insulation, -X | 0.03007 | 492.83 | 1.5237 | 983.01 | -0.0475 | -4.1324 | -0.4775 | -0.0875 | -0.0075 | -7.1409 | -1.1408 | -0.5175 | -0.4375 | 7 |
| W2-a | Stripped conductor, +X | 0.00067 | 11.04 | 0.0556 | 35.85 | 0.0475 | -7.2357 | -0.4775 | 0.0175 | 0.0776 | -7.3609 | -7.1108 | -0.5075 | -0.4475 | 32 |
| W2-b | Stripped conductor, -X | 0.00067 | 11.04 | 0.0556 | 35.85 | -0.0475 | -7.2357 | -0.4775 | -0.0775 | -0.0174 | -7.3609 | -7.1108 | -0.5075 | -0.4475 | 32 |

**Assembly** (14 solids): V = 0.58523 in³ (9590.28 mm³), A = 35.0659 in² (22623.14 mm²), CoM = (0.0007, -0.5142, -0.1487),
bbox X -1.0825..1.0825, Y -7.36085..1.28, Z -0.67..0.67 (2.165 × 8.64085 × 1.34).

## 7. Checks you can make
- Width over the ears 2.165; housing height 2.56; output axis to housing bottom 1.99; shaft end to can bottom 1.34;
  D-flat length 0.264; shaft Ø0.25.
- No two bodies overlap by more than 8 mm³ (largest source overlap: stator disc / lead guide legs 1.9 mm³, a source artefact;
  you may keep or avoid it).

## 8. Undetermined / not in the source
- Gear train, rotor, winding, bearings, wire colours: not modelled; do not add.
- The exact twist law of the stranded conductor ends (W2) is freeform in the source; the table in 4.13 is sampled from it.
- Material and finish are not part of the geometry.
