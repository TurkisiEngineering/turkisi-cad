# Design specification: two-bolt flange mounted ball bearing, set-screw insert, 3/4 in bore

Cast two-bolt flange housing with a spherical seat, carrying a self-aligning insert bearing (outer ring and an inner ring with an extended collar and two set screws), plus a grease fitting. This document is the only source for the rebuild. Every dimension below was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. Do not change the origin or the axes.
- **Global frame (use exactly, no realignment):**
  - The **bearing (bore) axis is the X axis**. +X is the collar / set-screw side, -X the mounting side.
  - The **mounting face** (back face of the flange) is the plane **x = -0.7376**. The origin is at the middle of the overall width: the collar end face of the inner ring is at x = +0.7376.
  - The two bolt holes are on the **Z axis** side by side: bolt axes parallel to X through (y, z) = (0, +1.766) and (0, -1.766).
  - The grease fitting points into the **+Y +Z quadrant** at 45 deg.
- "(x, r)" means a profile in a half plane containing the X axis, r being the distance from the X axis, revolved 360 deg about X.
- Angles round the X axis: phi is measured in the YZ plane from +Y toward +Z; a direction at angle phi is (0, cos phi, sin phi).
- Every body is modelled in place in this frame (identity placement).

## 2. Product description

The cast-iron housing (P01) is a flat diamond-shaped flange with a cylindrical hub. The hub holds the bearing outer ring (P02) in a spherical seat; two loading slots in the seat allow the ring to be swung in. The inner ring (P03) has an extended collar on +X with two threaded set-screw holes, each with a hex-socket set screw (H1-a, H1-b). A grease fitting (H2) sits in a blind hole in the hub.

**Simplifications that exist in the source model and must be reproduced:**
- No rolling elements, cage or seals: the outer ring bore and the inner ring outer diameter are the same cylinder (R0.555), face contact.
- The grease fitting hole is blind and does not reach the seat; the fitting shank and hole are plain (no thread).
- The set-screw threads and the matching internal threads **are modelled** as real helical threads (section 4, P03 and H1), in phase so that screw and hole do not overlap.
- No lettering or cast marks.

## 3. Part list

3 custom parts and 2 distinct hardware items, **6 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Flange housing, two-bolt | custom casting | cast iron, powder coated |
| P02 | 1 | Bearing outer ring (spherical OD) | custom | bearing steel |
| P03 | 1 | Bearing inner ring with extended collar | custom | bearing steel |
| H1 | 2 | Hex-socket set screw, 1/4-28 x 0.18, flat point | hardware (H1-a, H1-b) | steel |
| H2 | 1 | Grease fitting, straight, hex 5/16 | hardware | steel |

## 4. Part geometry

### P01 Flange housing (one solid, 124 faces in the master)

**H1. Flange plate.** Outline in the YZ plane = the convex hull of the circle R1.187 centred at the origin and the two **ear circles R0.4585** centred at (y, z) = (0, +/-1.766). The four straight hull lines are tangent to both circles; their end points are (y, z) = (+/-1.0813, +/-0.48965) on the R1.187 circle and (+/-0.41767, +/-1.95514) on the ear circles (plane normals (0, +/-0.911, +/-0.4125)). Extrude from x = -0.7376 (mounting face) to x = -0.44627 (flange thickness 0.29133).

**H2. Ear bosses (2x),** one per ear, from x = -0.7376 to x = -0.3006 (boss thickness 0.437). Outline in YZ for the +Z ear: half circle R0.4585 centred (0, 1.766) on the outer side (z >= 1.766), straight sides y = +/-0.4585 running inward from z = 1.766 into the hub. Mirror for the -Z ear. The boss's outer half circle coincides with the flange ear circle.

**H3. Hub.** Cylinder R1.187 about X from x = -0.7376 to the front face x = 0.4044. (In Y the flange outline and the hub coincide at |y| = 1.187.)

**H4. Bolt holes (2x),** dia 0.437 (R0.2185), axes parallel to X through (0, 0, +/-1.766), through the boss (x = -0.7376 to -0.3006).

**H5. Bore, seat and front recess** (revolved cut about X). Closed profile (x, r), start on the axis:
1. (-0.7376, 0) to (-0.7376, 0.95616)
2. arc R0.00656 c=(-0.73104, 0.95616) to (-0.73104, 0.9496) (edge round at the mounting face)
3. line to (-0.345, 0.9496) (rear bore R0.9496)
4. arc R0.0786 c=(-0.345, 0.871) to (-0.2664, 0.871) (rounded corner of the rear bore)
5. line to (-0.2664, 0.82219) (shoulder face)
6. arc R0.871 c=(0.02109, 0) to (0.30857, 0.82219) (**spherical seat**, sphere R0.871 centred (0.02109, 0, 0))
7. line to (0.30857, 0.93737)
8. arc R0.00656 c=(0.31513, 0.93737) to (0.31876, 0.94283) (123.6 deg)
9. line to (0.39422, 0.89266) (undercut cone, 33.6 deg to the axis, opening toward -X)
10. arc R0.00656 c=(0.39785, 0.89812) through (0.39785, 0.89157) to (0.4044, 0.89812) (123.6 deg)
11. line to (0.4044, 0), close along the axis.

**H6. Loading slots (2x)** in the seat, at +Z and -Z. For the +Z slot: cross-section in YZ bounded by the planes y = +/-0.4355, below by the axis region (inside the bore) and above by a **circular arc through (y, z) = (-0.4355, 0.79586), (0, 0.9103), (0.4355, 0.79586)** (centre (0, 0.02401), R0.88619). Extrude this section from the mounting side up to the slot end face x = 0.02109 (slot open toward -X into the rear bore). Mirror about z = 0 for the -Z slot. Slot edges sharp.

**H7. Grease fitting hole,** dia 0.25 (R0.125), axis direction (0, 0.70711, 0.70711) (phi = 45 deg) through the point (0.0794, 0, 0); blind, from the hub surface inward to a flat bottom at distance 0.9995 from the X axis (measured along the hole axis). No thread, does not reach the seat.

**H8. Rounds and fillets.**
- Convex R0.01311 on the whole outer edge of the mounting face (x = -0.7376): along the flange hull lines, around the ear circles and along the hub arcs (round centres at x = -0.72449).
- Convex R0.01311 on both ends of each bolt hole (at x = -0.7376 and x = -0.3006).
- Convex R0.0437 on the hub front edge (centre (x, r) = (0.3607, 1.1433)).
- Convex R0.0437 on the ear boss front edge (x = -0.3006): around the half circle and along the straight sides (centre lines at x = -0.3443, inset 0.0437).
- Concave R0.11811 vertical fillet (axis parallel to X) between each boss side face (y = +/-0.4585) and the hub cylinder; centres at (y, z) = (+/-0.57661, +/-1.17083). The boss front-edge round R0.0437 continues around it (convex, tube centre radius 0.16181).
- Concave R0.0437 between the boss front face (x = -0.3006) and the hub (tube centre at x = -0.2569, radius 1.2307).
- On the flange front face x = -0.44627 (the four recesses beside the bosses): concave R0.0437 to the boss sides and to the R0.11811 fillets (radius 0.07441 tube), concave R0.0437 to the hub (tube centre x = -0.40257, radius 1.2307), convex R0.0437 on the outer edge along the four hull lines (centre lines at x = -0.48997, inset 0.0437).
- The corners where these rounds meet are smooth blends.

### P02 Bearing outer ring (one solid, 16 faces)

Revolved about X. Closed profile (x, r):
(-0.2664, 0.555) → (-0.2664, 0.81542) → arc R0.0095 c=(-0.2569, 0.81542) to the sphere → **spherical OD R0.871 centred (0.02109, 0, 0)** → arc R0.0095 c=(0.29908, 0.81542) to (0.30857, 0.81542) → (0.30857, 0.78879) → 45 deg line to (0.27517, 0.75539) → (0.27517, 0.68859) → 45 deg line to (0.30857, 0.6552) → (0.30857, 0.555) → close along the bore r = 0.555.
- The +X face carries a trapezoidal ring groove 0.0334 deep (between r 0.6552 and 0.78879 at the face, floor x = 0.27517 from r 0.68859 to 0.75539). The -X face is plain.
- Width x = -0.2664 to 0.30857 (0.57497); bore R0.555. The R0.0095 rounds are tangent to the end face and to the sphere.

### P03 Inner ring with extended collar (one solid, 58 faces)

**I1. Ring.** Tube about X: bore R0.375 (dia 0.75), OD R0.555 (dia 1.11), from x = -0.2664 to x = 0.7376. Convex R0.01875 round on all four circular edges.

**I2. Set-screw holes (2x),** both at x = 0.5606, each a threaded through hole from the bore to the OD:
- Hole A: axis direction W = (0, -0.96593, -0.25882) (phi = 195 deg) through (0.5606, 0, 0).
- Hole B: axis direction W = (0, 0.70711, -0.70711) (phi = 315 deg) through (0.5606, 0, 0).
- Local frame per hole: origin O = (0.5606, 0, 0), W as above (pointing outward), U = (1, 0, 0), V = W x U. w is the distance along W from O, theta is measured from U toward V.
- **Internal thread 1/4-28, right hand, single start, pitch P = 1/28 = 0.0357143**, 60 deg. Root (major) radius 0.125, crest (minor) radius 0.1018, depth 0.0232. Profile per pitch: flats of P/8 (0.00446) at both major and minor radius, straight 30 deg flanks. **Phase:** at theta = 0 (the +X side) the minor-radius flat is centred at w = 0.0260 + kP and the major-radius flat at w = 0.0081 + kP; right hand: the profile advances +P along +W per turn of theta.
- The thread runs through the whole wall. **Mouth chamfers** (45 deg cones on the hole axis): at the OD r = w - 0.43 (radius 0.125 at w = 0.555, widening outward); at the bore r = 0.47856 - w (widening inward, radius 0.10356 at w = 0.375).

### H1 Set screw (2 instances, identical; one solid, 39 faces)

Local frame as for its hole (O, U, V, W). Instance H1-a is in hole A, H1-b in hole B.
- **Body:** external thread 1/4-28 right hand, major radius 0.125, minor radius 0.1018, flats P/8, **same phase as the hole** (minor flat centred at w = 0.0260 + kP at theta = 0), so the screw thread coincides with the hole thread without overlap.
- **Point:** flat tip face w = 0.375, radius 0.1; 45 deg chamfer from (r 0.1, w 0.375) to (r 0.125, w 0.4).
- **Top:** flat face w = 0.555; 45 deg chamfer from (r 0.125, w 0.53) to (r 0.1, w 0.555). Length 0.18 (w = 0.375 to 0.555).
- **Hex socket:** across flats 0.09375 (3/32), flats normal to V (corners on U, corner radius 0.05413), from the top face down to w = 0.48469. At w = 0.48469 the socket has a flat ledge from the corners in to radius 0.04688 and then a 120 deg drill-point cone to the apex at w = 0.45762. The 120 deg countersink at the socket mouth touches only the hex corners (radius 0.05413 at w = 0.555): it may be omitted.

### H2 Grease fitting (one solid, 21 faces)

Local frame: origin O = (0.0794, 0, 0), axis G = (0, 0.70711, 0.70711), w along G, r from the axis. 
- **Shank:** plain cylinder R0.125 from the flat bottom w = 0.9995 to w = 1.187 (no thread).
- **Hex:** across flats 0.3125 (5/16), flats normal to X (corners on the direction (0, -0.70711, 0.70711)), from w = 1.187 upward, intersected with the head solid of revolution below.
- **Head (solid of revolution about G), profile (r, w):** start (0, 1.187); line to (0.18907, 1.187); line to (0.18907, 1.28984); arc R0.0833 c=(0.18907, 1.37314) from its lowest point through (0.10576, 1.37314) to (0.12303, 1.42391) (concave neck); arc R0.03125 c=(0.09825, 1.44295) to (0.12303, 1.462) (convex bead); line (22.47 deg cone) to (0.06594, 1.6); line to (0.02706, 1.6); arc R0.03125 c=(0, 1.58437) to (0, 1.61562) (ball tip); close along the axis. The hex part of H2 = hex prism (w 1.187 to 1.62) intersected with this solid: the R0.0833 arc cuts the hex corners from w = 1.29028 (at the corner radius 0.18042) upward; above the neck the head is fully round.
- Union shank + head.

## 5. Assembly

All six bodies are built in place with identity placement, as supplied.

| Instance | Part | Local origin O | W (axis) | U |
|---|---|---|---|---|
| H1-a | H1 | (0.5606, 0, 0) | (0, -0.96593, -0.25882) | (1, 0, 0) |
| H1-b | H1 | (0.5606, 0, 0) | (0, 0.70711, -0.70711) | (1, 0, 0) |
| H2 | H2 | (0.0794, 0, 0) | (0, 0.70711, 0.70711) | (1, 0, 0) |

- P02 sits in the housing seat: both spheres are R0.871 about (0.02109, 0, 0) (face contact). P02 spans x = -0.2664 to 0.30857, exactly the seat's shoulder face to the front seat face.
- P03 sits in P02: OD and bore R0.555 coincide (face contact). P03 starts flush with P02 at x = -0.2664 and its collar projects to x = 0.7376.
- The set screw tips (w = 0.375) are tangent to the bore line; the tops (w = 0.555) are at the OD radius.
- The grease fitting bottom w = 0.9995 rests on the housing hole bottom; the hex underside w = 1.187 is at the hub radius.
- **Interference: none.** All 15 body pairs overlap 0.0000 mm3 in the master. Rotation: P03 (with the screws) turns about X with the shaft; P02 can swivel in the seat about (0.02109, 0, 0).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. Faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Flange housing | 2.98100 | 48849.88 | 26.4623 | 17072.41 | -0.2540 | -0.0024 | -0.0024 | -0.7376 | 0.4044 | -1.1870 | 1.1870 | -2.2245 | 2.2245 | 124 |
| P02 | Bearing outer ring | 0.74893 | 12272.77 | 7.5708 | 4884.37 | 0.0156 | 0.0000 | 0.0000 | -0.2664 | 0.3086 | -0.8710 | 0.8710 | -0.8710 | 0.8710 | 16 |
| P03 | Inner ring with collar | 0.51229 | 8394.87 | 7.1008 | 4581.16 | 0.2262 | 0.0017 | 0.0065 | -0.2664 | 0.7376 | -0.5550 | 0.5550 | -0.5550 | 0.5550 | 58 |
| H1-a | Set screw A | 0.00653 | 106.93 | 0.3018 | 194.69 | 0.5607 | -0.4446 | -0.1195 | 0.4356 | 0.6856 | -0.5620 | -0.3363 | -0.2567 | 0.0152 | 39 |
| H1-b | Set screw B | 0.00653 | 106.93 | 0.3018 | 194.69 | 0.5607 | 0.3258 | -0.3253 | 0.4356 | 0.6856 | 0.1945 | 0.4632 | -0.4632 | -0.1945 | 39 |
| H2 | Grease fitting | 0.02988 | 489.66 | 0.6053 | 390.49 | 0.0794 | 0.8958 | 0.8958 | -0.0769 | 0.2356 | 0.6184 | 1.1780 | 0.6184 | 1.1780 | 21 |

**Whole assembly:** 6 bodies (3 custom + 3 hardware instances); total volume 4.28515 in3 (70221.04 mm3); total area 42.3427 in2 (27317.82 mm2); centre of mass (-0.1447, 0.0046, 0.0047) in; bounding box X [-0.7376, 0.7376], Y [-1.187, 1.187], Z [-2.2245, 2.2245] in (mm: X [-18.735, 18.735], Y [-30.1498, 30.1498], Z [-56.5023, 56.5023]).

**Key functional checks:** bolt spacing 3.532; overall length 4.449; overall height 2.374 (hub dia); overall width 1.475; flange at the bolts 0.437 thick; bolt holes dia 0.437; bore dia 0.750; seat sphere dia 1.742.

## 7. Source conflicts and undetermined items

**Authority:** the master 3D geometry governs.

| Item | Drawing / product data | Master 3D | Decision |
|---|---|---|---|
| Bolt spacing, overall length, height, width | 3.532, 4.449, 2.374, 1.475 (product data: 3 17/32, 4 7/16, 2 3/8, 1 15/32) | 3.532, 4.449, 2.374, 1.4752 | Follow the 3D (drawing agrees) |
| Flange thickness | 0.437 (7/16) | 0.437 at the bolt bosses; 0.29133 elsewhere | Follow the 3D |
| Bore | 0.7500 (+0.0007 / +0.0002) | 0.75 nominal | Model at 0.75 |
| Grease fitting | 1/4-28 UNF | plain R0.125 shank, blind plain hole | Follow the 3D |
| Bearing internals, seals | sealed ball bearing | two solid rings in contact, no balls | Follow the 3D |

**Undetermined:** rolling-element and seal geometry; the real fit between the rings; casting draft (none modelled); the grease passage into the bearing (not modelled).
