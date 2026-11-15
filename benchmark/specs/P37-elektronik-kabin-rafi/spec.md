# Design specification: freestanding open electronics rack, 24 rack units, two-post, bent sheet-steel structure

An open two-post floor rack for standard 19 in wide rack-mounted equipment, 24 rack units high. It is a simplified
catalogue model made of five formed sheet-steel parts (two base feet, two upright channels, one top cap) and four small
threaded grounding studs. This document is the only source for the rebuild. Every dimension below was measured from the
original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **Y is vertical (up).** The floor plane (underside of the feet) is **y = -24.022625**; the top of the top cap is
    **y = 24.097375**. The two uprights run from y = -24.022625 to y = +24.022625 (they are centred on y = 0).
  - **X runs across the rack** (left / right). The rack is mirror-symmetric about the plane **x = 0** (only the
    grounding stud positions break this symmetry, see H1). The uprights are at x = -10.23 ... -8.875 and
    x = +8.875 ... +10.23.
  - **Z is the depth direction** (front / back). The rack is mirror-symmetric about the plane **z = 0**. The uprights
    occupy z = -1.5 ... +1.5; the feet extend to z = +/-7.5.
  - Overall: X [-10.23, 10.23], Y [-24.022625, 24.097375], Z [-7.5, 7.5] (20.46 x 48.12 x 15.00).
- **Profile conventions:** a "profile in the YZ plane" is a closed outline given as (y, z) points and extruded along X
  between the stated x values; "profile in the XZ plane" = (x, z) points extruded along Y. "Arc centre (a, b) R r" is a
  circular arc of radius r about that centre, joining the neighbouring points tangentially. Bends are concentric pairs
  of arcs (inner radius + sheet thickness = outer radius).
- **Body count: 9 solids.** The source file also contains 16 empty shells (no volume); they are not part of the model.

## 2. Product description and source simplifications

- Two-post open rack: two vertical C-channel uprights face each other across the rack, their open sides pointing to
  the rack centre. Equipment panels (19 in wide, 1.75 in per rack unit) are fastened to the front and back flanges of
  the uprights through a column of mounting holes.
- The uprights stand on two L-shaped base feet (one in front, one behind) that run across the whole rack width and
  rest on the floor. A shallow inverted U-channel caps the tops of both uprights.
- Four short threaded grounding studs stand on the inner faces of the upright webs (two per upright).
- Material: painted steel (black). Not needed for the geometry.
- **Source simplifications (rebuild them the same way):**
  - The equipment mounting holes are **plain round holes at diameter 0.19** (the 10-32 major diameter). Their thread is
    **not modelled**; leave them plain.
  - **No fasteners** join the parts. The parts only touch each other (no overlap; see section 5). There are no welds,
    no paint thickness, no hole for the foot-to-upright joint.
  - The grounding studs carry a **modelled helical thread** (see H1).
  - Sheet parts are solid bodies with exact concentric bend arcs; there are no bend reliefs.

## 3. Part list

| Spec name | Kind | Qty | Equivalence group | Description |
|---|---|---|---|---|
| P01-a, P01-b | custom | 2 | P01 | Base foot: L-angle, 0.25 thick, 20.26 long; P01-a at +Z, P01-b at -Z (mirror image about z = 0, i.e. the same part turned 180 deg about Y) |
| P02-a, P02-b | custom | 2 | P02 | Upright: C-channel, 0.1 thick, 48.04525 long, with 101 holes; P02-a at -X, P02-b at +X (mirror image about x = 0, i.e. the same part turned 180 deg about Y) |
| P03 | custom | 1 | P03 | Top cap: inverted U-channel, 0.0598 thick, 20.26 long, 4 holes |
| H1-a ... H1-d | hardware | 4 | H1 | Grounding stud 10-32 x 0.63, modelled thread |

Distinct part types: 4 (P01, P02, P03, H1). Total bodies: 9.

## 4. Part geometry

### P01 Base foot (2 bodies, 18 faces each)

**P01-a (+Z side).** An L-angle (a floor leg and a vertical leg joined by one bend), constant section along X,
extruded from **x = -10.13 to x = +10.13** (length 20.26).

Profile in the YZ plane, (y, z), counter-clockwise from the top of the vertical leg:

1. (-20.032625, 1.5)  start, inner face of the vertical leg, top end
2. (-23.397625, 1.5)  line down the vertical leg (face z = 1.5)
3. outer bend: arc centre (-23.397625, 2.125) R 0.625, to (-24.022625, 2.125)
4. (-24.022625, 7.5)  line along the floor (underside y = -24.022625)
5. (-23.772625, 7.5)  end face of the floor leg (z = 7.5), 0.25 high
6. (-23.772625, 2.125)  top face of the floor leg (y = -23.772625)
7. inner bend: arc centre (-23.397625, 2.125) R 0.375, to (-23.397625, 1.75)
8. (-20.032625, 1.75)  line up the vertical leg (face z = 1.75)
9. close to point 1 (top end face y = -20.032625, 0.25 wide)

So: sheet thickness 0.25; vertical leg faces z = 1.5 / 1.75, top end y = -20.032625 (leg height above the floor
3.99); floor leg faces y = -24.022625 / -23.772625, free end z = 7.5 (foot depth from z = 1.5 to 7.5 = 6.0); bend
inside radius 0.375, outside radius 0.625, bend axis parallel to X through (y = -23.397625, z = 2.125).

**Corner rounds:** the four outer corners at the two leg tips are rounded **R 0.05** in the view along the leg:

- floor-leg tip: the edges where the end faces x = +/-10.13 meet the face z = 7.5 (edges parallel to Y) are rounded
  R 0.05 (round centre lines x = +/-10.08, z = 7.45);
- vertical-leg tip: the edges where the end faces x = +/-10.13 meet the face y = -20.032625 (edges parallel to Z) are
  rounded R 0.05 (round centre lines x = +/-10.08, y = -20.082625).

**Holes:** 2 through holes **dia 0.75** in the floor leg, axis parallel to Y, at **(x, z) = (+8.25, 5.5)** and
**(-8.25, 5.5)** (16.5 apart; 2.0 from the floor-leg end).

**P01-b (-Z side)** = P01-a mirrored in the plane z = 0 (vertical leg faces z = -1.5 / -1.75, floor leg to z = -7.5,
holes at (+/-8.25, -5.5)).

The inner face of the vertical leg (z = +/-1.5) touches the outer flange faces of both uprights.

### P02 Upright channel (2 bodies, 408 faces each)

**P02-a (-X side).** A C-channel (web plus two flanges, two bends), constant section along Y, extruded from
**y = -24.022625 to y = +24.022625** (length 48.04525). The web lies at the outside of the rack; the flanges point to
+X (toward the rack centre).

Profile in the XZ plane, (x, z), outer contour then inner contour, closed as one loop:

1. (-8.875, 1.5)  tip of the +Z flange, outer face
2. (-10.105, 1.5)  outer face of the +Z flange (z = 1.5)
3. outer bend: arc centre (-10.105, 1.375) R 0.125, to (-10.23, 1.375)
4. (-10.23, -1.375)  outer face of the web (x = -10.23)
5. outer bend: arc centre (-10.105, -1.375) R 0.125, to (-10.105, -1.5)
6. (-8.875, -1.5)  outer face of the -Z flange (z = -1.5)
7. (-8.875, -1.4)  tip of the -Z flange (face x = -8.875, 0.1 wide)
8. (-10.105, -1.4)  inner face of the -Z flange (z = -1.4)
9. inner bend: arc centre (-10.105, -1.375) R 0.025, to (-10.13, -1.375)
10. (-10.13, 1.375)  inner face of the web (x = -10.13)
11. inner bend: arc centre (-10.105, 1.375) R 0.025, to (-10.105, 1.4)
12. (-8.875, 1.4)  inner face of the +Z flange, back to point 1

So: sheet thickness 0.1 everywhere; channel depth 3.0 (z -1.5 ... 1.5) by width 1.355 (x -10.23 ... -8.875); bend
inside radius 0.025, outside radius 0.125. Both ends (y = +/-24.022625) are flat cuts normal to Y.

**Holes in the flanges** (all through **both** flanges, axis parallel to Z; every hole exists at the same (x, y) in the
+Z flange and in the -Z flange):

- **Equipment mounting holes: 72 holes dia 0.19** on the column **x = -9.155** (1.075 from the web outer face).
  They form 24 groups (one per rack unit) of 3 holes with a group pitch of 1.75:
  y = -19.497625 + 1.75 k + d, with k = 0 ... 23 and d in {0, 0.625, 1.125}.
  Inside a group the spacing is 0.625 then 0.5; from the third hole of one group to the first of the next it is 0.625.
  The lowest hole is at y = -19.497625 (4.525 above the bottom end), the highest at y = 21.877375 (2.14525 below the
  top end). The full list is in the placement table below.
- **Small holes: 24 holes dia 0.15** on the column **x = -9.5** (0.73 from the web outer face), one per rack unit:
  y = -18.622625 + 1.75 k, k = 0 ... 23 (from y = -18.622625, 5.4 above the bottom end, to y = 21.627375).

Placement table of the flange holes (y values; same for both flanges and, at x = +9.155 / +9.5, for P02-b):

| k | dia 0.19, d = 0 | dia 0.19, d = 0.625 | dia 0.19, d = 1.125 | dia 0.15 |
|---|---|---|---|---|
| 0 | -19.497625 | -18.872625 | -18.372625 | -18.622625 |
| 1 | -17.747625 | -17.122625 | -16.622625 | -16.872625 |
| 2 | -15.997625 | -15.372625 | -14.872625 | -15.122625 |
| 3 | -14.247625 | -13.622625 | -13.122625 | -13.372625 |
| 4 | -12.497625 | -11.872625 | -11.372625 | -11.622625 |
| 5 | -10.747625 | -10.122625 | -9.622625 | -9.872625 |
| 6 | -8.997625 | -8.372625 | -7.872625 | -8.122625 |
| 7 | -7.247625 | -6.622625 | -6.122625 | -6.372625 |
| 8 | -5.497625 | -4.872625 | -4.372625 | -4.622625 |
| 9 | -3.747625 | -3.122625 | -2.622625 | -2.872625 |
| 10 | -1.997625 | -1.372625 | -0.872625 | -1.122625 |
| 11 | -0.247625 | 0.377375 | 0.877375 | 0.627375 |
| 12 | 1.502375 | 2.127375 | 2.627375 | 2.377375 |
| 13 | 3.252375 | 3.877375 | 4.377375 | 4.127375 |
| 14 | 5.002375 | 5.627375 | 6.127375 | 5.877375 |
| 15 | 6.752375 | 7.377375 | 7.877375 | 7.627375 |
| 16 | 8.502375 | 9.127375 | 9.627375 | 9.377375 |
| 17 | 10.252375 | 10.877375 | 11.377375 | 11.127375 |
| 18 | 12.002375 | 12.627375 | 13.127375 | 12.877375 |
| 19 | 13.752375 | 14.377375 | 14.877375 | 14.627375 |
| 20 | 15.502375 | 16.127375 | 16.627375 | 16.377375 |
| 21 | 17.252375 | 17.877375 | 18.377375 | 18.127375 |
| 22 | 19.002375 | 19.627375 | 20.127375 | 19.877375 |
| 23 | 20.752375 | 21.377375 | 21.877375 | 21.627375 |

**Holes in the web** (through the web, axis parallel to X):

| Hole | dia | y | z |
|---|---|---|---|
| W1 | 0.19 | -23.647625 (0.375 above the bottom end) | 0 |
| W2 | 0.3125 | -20.892625 | +0.625 |
| W3 | 0.3125 | -20.892625 | -0.625 |
| W4 | 0.3125 | 16.097375 | +0.625 |
| W5 | 0.3125 | 16.097375 | -0.625 |

(W2-W5: pairs 1.25 apart in Z, the two pairs 36.99 apart in Y. In the source the dia 0.3125 hole centres sit at
z = +/-0.625005; use +/-0.625.)

Upright hole total: 72 + 24 + 5 = 101 holes; no other features (no fillets on the flange tips, no end notches).

**P02-b (+X side)** = P02-a mirrored in the plane x = 0: web outer face x = +10.23, web inner face x = +10.13, flange tips x = +8.875, bend centres (+10.105, +/-1.375); equipment holes at
x = +9.155, small holes at x = +9.5; all y and z values unchanged, web holes identical in y and z.

The upright tops (y = 24.022625) are 0.01495 below the inner face of the top cap web; the upright outer flange faces
(z = +/-1.5) touch the inner faces of the top cap flanges and of the feet.

### P03 Top cap (1 body, 26 faces)

An inverted U-channel (web on top, two flanges hanging down over the uprights), constant section along X, extruded from
**x = -10.13 to x = +10.13** (length 20.26).

Profile in the YZ plane, (y, z):

1. (22.127375, 1.5)  bottom of the +Z flange, inner face
2. (24.022625, 1.5)  inner face of the +Z flange (z = 1.5)
3. inner bend: arc centre (24.022625, 1.48505) R 0.01495, to (24.037575, 1.48505)
4. (24.037575, -1.48505)  underside of the web (y = 24.037575)
5. inner bend: arc centre (24.022625, -1.48505) R 0.01495, to (24.022625, -1.5)
6. (22.127375, -1.5)  inner face of the -Z flange (z = -1.5)
7. (22.127375, -1.5598)  bottom end of the -Z flange (y = 22.127375)
8. (24.022625, -1.5598)  outer face of the -Z flange (z = -1.5598)
9. outer bend: arc centre (24.022625, -1.48505) R 0.07475, to (24.097375, -1.48505)
10. (24.097375, 1.48505)  top face of the web (y = 24.097375)
11. outer bend: arc centre (24.022625, 1.48505) R 0.07475, to (24.022625, 1.5598)
12. (22.127375, 1.5598)  outer face of the +Z flange, back to point 1

So: sheet thickness 0.0598; cap height 1.97 (y 22.127375 ... 24.097375); outer width 3.1196 (z +/-1.5598), inner width
3.0 (it fits over the 3.0 deep uprights); bend inside radius 0.01495, outside radius 0.07475.

**Corner rounds:** the four lower outer corners of the flanges, where the end faces x = +/-10.13 meet the flange
bottoms y = 22.127375 (edges parallel to Z), are rounded **R 0.05** (round centre lines x = +/-10.08, y = 22.177375).

**Holes:** 4 through holes **dia 0.19** in the web, axis parallel to Y, at **(x, z) = (+/-4.5, +/-1.0)** (9.0 apart in
X, 2.0 apart in Z).

### H1 Grounding stud (4 bodies, 47 faces each)

A short fully threaded stud, axis parallel to X, standing on the inner face of an upright web and pointing toward the
rack centre.

- Axis on the line (y = y_s, z = 0). Base face (flat, normal to X) on the web inner face **x = -10.13** (left studs) or
  **x = +10.13** (right studs); free end face at **x = -9.5** / **x = +9.5**. Length **0.63**.
- Thread **10-32 (UNF), external, modelled as a true helical thread**: major diameter **0.19**, pitch **1/32 = 0.03125**,
  **right hand**, 60 deg symmetric flanks, minor (root) diameter **0.1494** (thread depth 0.0203), narrow flats at crest
  and root (basic profile, flat width about P/8 = 0.0039). The thread runs over the full length and is cut off by the
  base plane, so the base face is the thread section (not a full disc).
- Free end: **45 deg chamfer** from the major diameter down to an end face of **dia 0.1431** (chamfer length 0.0234
  along the axis).
- Thread phase (as measured): a crest centre line lies on the +Y side of the axis (direction +Y from the axis) at
  0.0332 from the free end face, on every stud. A rebuild with another start phase changes the volume only marginally.

| Body | Upright | Base face x | Free end x | Axis y (z = 0) |
|---|---|---|---|---|
| H1-a | P02-a (-X) | -10.13 | -9.5 | 7.597375 |
| H1-b | P02-a (-X) | -10.13 | -9.5 | 6.977375 |
| H1-c | P02-b (+X) | +10.13 | +9.5 | -6.902625 |
| H1-d | P02-b (+X) | +10.13 | +9.5 | -7.522625 |

Each pair is 0.62 apart in Y. Note that the two pairs are **not** mirror images of each other: the left pair sits
around y = +7.29, the right pair around y = -7.21. The studs touch the web faces only (no hole in the web under them).

## 5. Assembly

- Positions are fixed by the global coordinates above; no part needs further placement.
- Contacts (touching faces, zero overlap): feet vertical legs (z = +/-1.5) against the outer flange faces of both
  uprights; top cap flange inner faces (z = +/-1.5) against the same flange faces; stud base faces against the web inner
  faces (x = +/-10.13). The feet and the uprights both start at the floor plane y = -24.022625.
- Interference: **none** (no pair of bodies overlaps by more than a contact).
- The top-cap web sits 0.01495 above the upright tops; the feet ends x = +/-10.13 are flush with the upright web inner
  faces, and the uprights' webs stick out 0.1 beyond the feet and the cap at each side (overall width 20.46).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (studs
2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-a | Ground stud, -X upright, Y 7.5974 | 0.01429 | 234.16 | 0.6241 | 402.65 | -9.8159 | 7.5975 | 0.0002 | -10.1300 | -9.5000 | 7.5024 | 7.6924 | -0.0950 | 0.0950 | 47 |
| H1-b | Ground stud, -X upright, Y 6.9774 | 0.01429 | 234.16 | 0.6241 | 402.65 | -9.8159 | 6.9775 | 0.0002 | -10.1300 | -9.5000 | 6.8824 | 7.0724 | -0.0950 | 0.0950 | 47 |
| H1-c | Ground stud, +X upright, Y -6.9026 | 0.01430 | 234.34 | 0.6241 | 402.65 | 9.8167 | -6.9024 | -0.0000 | 9.5000 | 10.1300 | -6.9976 | -6.8076 | -0.0950 | 0.0950 | 47 |
| H1-d | Ground stud, +X upright, Y -7.5226 | 0.01430 | 234.34 | 0.6241 | 402.65 | 9.8167 | -7.5224 | -0.0000 | 9.5000 | 10.1300 | -7.6176 | -7.4276 | -0.0950 | 0.0950 | 47 |
| P01-a | Base foot, +Z side | 48.02471 | 786984.03 | 400.2470 | 258223.38 | -0.0000 | -23.1086 | 3.4286 | -10.1300 | 10.1300 | -24.0226 | -20.0326 | 1.5000 | 7.5000 | 18 |
| P01-b | Base foot, -Z side | 48.02471 | 786984.03 | 400.2470 | 258223.38 | -0.0000 | -23.1086 | -3.4286 | -10.1300 | 10.1300 | -24.0226 | -20.0326 | -7.5000 | -1.5000 | 18 |
| P02-a | Upright channel, -X side | 25.63700 | 420115.09 | 534.7478 | 344997.90 | -9.8796 | -0.0188 | 0.0000 | -10.2300 | -8.8750 | -24.0226 | 24.0226 | -1.5000 | 1.5000 | 408 |
| P02-b | Upright channel, +X side | 25.63700 | 420115.09 | 534.7478 | 344997.90 | 9.8796 | -0.0188 | -0.0000 | 8.8750 | 10.2300 | -24.0226 | 24.0226 | -1.5000 | 1.5000 | 408 |
| P03 | Top cap channel | 8.35459 | 136907.18 | 282.8038 | 182453.73 | 0.0000 | 23.5217 | -0.0000 | -10.1300 | 10.1300 | 22.1274 | 24.0974 | -1.5598 | 1.5598 | 26 |

**Whole assembly:** 9 bodies; total volume 155.73518 in3 (2552042.41 mm3); total area 2155.2900 in2
(1390506.90 mm2); centre of mass (0.0000, -12.9965, 0.0000) in; bounding box X [-10.23, 10.23],
Y [-24.022625, 24.097375], Z [-7.5, 7.5] in (mm: X [-259.842, 259.842], Y [-610.17468, 612.07333], Z [-190.5, 190.5]).

**Key functional checks:** overall 20.46 wide x 48.12 high x 15.00 deep; upright depth 3.00; equipment hole columns
18.31 apart (x = +/-9.155), holes dia 0.19 (10-32 size, plain); rack unit pitch 1.75 with holes at 0 / 0.625 / 1.125
inside each unit; 24 units; feet 0.25 thick, uprights 0.1 thick, top cap 0.0598 thick.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs. The catalogue drawing agrees with the model on every printed
dimension it can be checked against (20.46, 48.12, 15.00, 3.00, rack unit 1.75, hole size 10-32 shown as plain dia 0.19
holes). Its "for component width 19 in" is the nominal panel width and has no single feature in the model.

**Undetermined (not in the source model):** the threads of the 72 x 2 equipment mounting holes (plain in the model),
the purpose of the dia 0.15 holes and the web holes, fasteners between feet / cap and uprights (none modelled), any
levelling feet or casters, paint. The 16 empty shells of the source file carry no geometry.
