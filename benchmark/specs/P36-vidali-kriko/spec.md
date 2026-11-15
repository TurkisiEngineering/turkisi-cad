# Design specification: lifting jack with power screw, swivel saddle and carry handle

Manual screw jack in its lowest position: a cast iron base with a flared foot and a carrying handle, a lifting screw with a
square-shouldered trapezoidal thread, a cross-drilled head for a turning bar and a ball on top, a swivel saddle with a
studded top face, and three set screws that retain the saddle on the ball. This document is the only source for the
rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The jack axis is the Y axis** (x = 0, z = 0); +Y points up, from the floor to the saddle.
  - **y = 0 is the floor:** the flat underside of the base.
  - **The carrying handle is on the +X side** of the base; it is symmetric about the plane z = 0.
  - **The inspection window of the base is on the -Z side.**
  - Azimuth angles "az" are measured in the XZ plane **from +X toward +Z** (az 90 = +Z, az 180 = -X, az 270 = -Z).
- **Profile conventions:**
  - "(r, y)" = half-section of a body of revolution about the Y axis (r = radius from the Y axis).
  - "(x, y)" = profile in the plane z = 0 (or a plane parallel to it).
  - "arc R c=(a, b) to (p, q)" = circular arc of radius R about centre (a, b), ending at (p, q), the short way.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description

The **base** (P01) is a hollow body of revolution: a wide flat foot flaring up along concave arcs into a cylindrical
neck with a small rounded lip at the top. Its bore is a plain cylinder at the top and widens downward along a concave
arc. A C-shaped **carrying handle** is cast onto the +X side of the neck and the flare, and an **elliptical window**
pierces the neck wall on the -Z side. The **lifting screw** (P02) stands in the bore: a threaded shank, a relief
groove, a cylindrical head with two crossing through holes for the turning bar, a neck and a **ball** on top. The
**saddle** (P03) sits on the ball (spherical socket); its top face carries 36 small conical studs. Three **set screws**
(H1-a, H1-b, H1-c) pass through the saddle skirt and touch the ball.

**Simplifications that exist in the source model and must be reproduced:**
- The base bore is **plain** (no internal thread): the screw thread crests just touch the bore (radius 0.75).
- The screw thread **is modelled** as a helical groove (section 4, P02). The set screws carry **no thread** (plain
  cylinders of the hole diameter).
- No turning bar, no internal bearing or washers. The jack is shown fully lowered.
- The saddle socket is the exact ball sphere (no clearance); the saddle bottom opening is smaller than the screw neck,
  so the saddle and the screw neck overlap (section 5). Reproduce this as is.

## 3. Part list

3 distinct custom parts and 1 distinct hardware item, 4 distinct, **6 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Base with carrying handle | custom | iron |
| P02 | 1 | Lifting screw with ball head | custom | steel (undetermined) |
| P03 | 1 | Swivel saddle | custom | steel (undetermined) |
| H1 | 3 | Socket set screw, plain diameter 0.125 (H1-a, H1-b, H1-c) | hardware | steel (undetermined) |

## 4. Part geometry

### P01 Base (one solid, 86 faces in the original)

**B1. Body of revolution about Y**, closed half-section (r, y), counter-clockwise from the floor at the bore:
- (1.875, 0) to (3.024872, 0): flat underside (floor), y = 0.
- **Foot round R0.0625** c=(3.024872, 0.0625) to (3.081087, 0.089816) (115.92 deg of arc; the outermost radius of the
  base is 3.087372 at y = 0.0625, diameter 6.174745).
- **Outer flare: concave arc R20.570191** c=(21.582691, 9.08) to (1.0125, 9.08) (tangent to the foot round at its
  start; vertical tangent at its end).
- **Neck:** line r = 1.0125 (diameter 2.025) from y = 9.08 up to y = 11.699251.
- **Concave fillet R0.10125** c=(1.11375, 11.699251) to (1.065789, 11.788422).
- **Lip bead: convex arc R0.1125** c=(1.0125, 11.8875) over its outermost point (1.125, 11.8875) to (1.0125, 12.0)
  (151.73 deg, tangent to the fillet and to the top face).
- **Top face** y = 12.0 from r = 1.0125 in to r = 0.75.
- **Bore:** line r = 0.75 (diameter 1.5) from y = 12.0 down to y = 9.08.
- **Inner flare: concave arc R37.205344** c=(37.955344, 9.08) from (0.75, 9.08) down to (1.875, 0) (vertical tangent at
  the top), closing the profile.

**B2. Elliptical window** on the -Z side: a through opening, its walls parallel to Z, from the outside of the neck into
the bore. Outline in the XY plane: **ellipse centred (x 0, y 10.375), semi-axis 0.28125 along X (width 0.5625) and
0.421875 along Y (height 0.84375)**; it is cut only through the -Z wall (z < 0). Both window edges are rounded
**R0.05625**: on the neck outside (r = 1.0125; the round runs from y = 9.896875 to the wall at 9.953125 in the plane
x = 0) and on the bore (r = 0.75, same widths).

**B3. Carrying handle** (added to B1). A constant cross-section swept along a planar path in z = 0.
- **Path (x, y), three tangent arcs, concave toward the neck:**
  - Upper bend: centre **T = (1.0125, 10.125)**, path radius **1.125**.
  - Middle arc: centre **M = (-1.262602, 9.088704)**, path radius **3.625**, from az -24.4897 deg to +24.4897 deg
    about M (tangent points (2.036297, 10.591332) and (2.036295, 7.586076); outermost point (2.362398, 9.088704)).
  - Lower bend: centre **B = (1.125, 8.001165)**, path radius **1.001379**.
  - The upper bend runs from its tangent point with the middle arc (direction 24.4897 deg from T) up and over to
    90 deg (point (1.0125, 11.25)); the lower bend runs from its tangent point (direction -24.4897 deg from B) down to
    -90 deg (point (1.125, 6.999786)). At both ends extend the section straight in the -X direction to **x = 0.9**, so
    it is buried in the neck / flare wall (the extension never reaches the bore).
- **Cross-section** (in the plane normal to the path; s = distance from the bend centre, measured outward, z across):
  a rectangle **s from (path radius - 0.125) to (path radius + 0.125)** (0.25 thick radially), **z from -0.3125 to
  0.3125** (0.625 wide). All four long edges are rounded **R0.07**. On the outer face (s = path radius + 0.125) runs a
  **central bead**: a convex half-round **R0.07 centred on the outer face at z = 0** (it stands 0.07 proud; on the
  middle arc it reaches s = 3.82), blended to the outer face by **concave R0.1 coves** whose centres are at
  s = path radius + 0.225, z = +/-0.137477 (the coves meet the flat outer face at |z| = 0.137477 and the bead at
  |z| = 0.056608). So on the middle arc: inner face R3.5, outer face R3.75, bead top R3.82; upper bend R1.0 / R1.25 /
  R1.32; lower bend R0.876379 / R1.126379 / R1.196379.
- **Junctions:** where the handle meets the neck and the flare, all its edges are blended with **R0.06** (free-form
  faces in the source, e.g. the side faces z = +/-0.3125 meet the neck along vertical R0.06 blends whose axes are at
  (x 1.005734, z +/-0.3725)).

### P02 Lifting screw (one solid, 110 faces)

**S1. Body of revolution about Y** (before the thread groove), half-section (r, y) from the bottom:
- Bottom face y = 0.32 from r = 0.1125 to r = 0.57.
- **45 deg chamfer** cone to (0.630682, 0.380682), then a **40.783 deg cone** (half-angle to the axis) to
  (0.75, 0.518994).
- **Thread crest cylinder r = 0.75 (diameter 1.5)** up to y = 11.333333.
- **45 deg cone** inward to (0.578333, 11.505).
- **Relief groove** cylinder r = 0.578333 (diameter 1.156667) up to y = 12.0.
- **Head:** underside y = 12.0 out to r = 1.05975; 45 deg chamfer to (1.125, 12.06525); **cylinder r = 1.125 (diameter
  2.25)** up to y = 14.0175; 45 deg chamfer to (0.9675, 14.175); top face y = 14.175 in to r = 0.65.
- **Neck** cylinder r = 0.65 (diameter 1.3) up to y = 14.550834.
- **Ball: sphere R0.75 centred (0, 14.925, 0)** up to its apex y = 15.675.

**S2. Bottom centre hole:** diameter 0.225 (R0.1125), from the bottom face y = 0.32 up to a flat end at y = 0.82
(0.5 deep).

**S3. Turning-bar holes:** two **through holes diameter 0.87 (R0.435)** through the head, one along X and one along Z,
both axes at **y = 13.0875**; they cross at the screw axis. The mouth edges on the head cylinder have a small edge
break (free-form in the source; at the top and bottom of each mouth it runs from the hole wall at 0.0499 inside the
head surface to the head surface 0.0238 above / below the hole; at the sides from 0.0653 to 0.0451). Its exact form is
undetermined; follow those set-backs.

**S4. Thread:** single-start, **right-hand**, **pitch p = 0.333333 (3 threads per inch)**, cut as one helical groove
into S1. Profile in any half-plane containing the Y axis:
- **Crest flat** on r = 0.75, axial width **0.13434**.
- **Flanks**: straight, at **14.5 deg to the plane normal to the axis** (29 deg included); each flank spans 0.166667
  radially and **0.043103 axially**.
- **Root flat** on r = 0.583333 (root diameter 1.166667, depth 0.166667), axial width **0.112787**.
- **Phase:** in the half-plane at azimuth az (from +X toward +Z) the crest flats start (lower end) at
  **y = 0.583333 - (az / 360) p + n p** and end 0.13434 higher. Examples: az 0 (+X): crest from 0.583333 to 0.717673,
  0.916667 to 1.051006, ...; az 90 (+Z): 0.5 to 0.63434, 0.833333 to 0.967673, ...; az 270 (-Z): 0.666667 to 0.801009,
  ... (the thread rises when the screw turns from +X toward -Z: right-hand).
- **Extent:** the groove runs along the whole shank and out at both ends: at the bottom through the 45 deg and
  40.783 deg cones (the root cylinder meets the 45 deg cone at y = 0.333333), at the top through the 45 deg cone into
  the relief groove (r 0.578333 is below the root, so the groove leaves no mark there). The last full crest flat at az
  0 runs from 10.916667 to 11.051006; the crest cylinder ends at y = 11.333333.

### P03 Saddle (one solid, 168 faces)

**D1. Body of revolution about Y**, half-section (r, y) from the bottom opening:
- Bottom face y = 14.3 from r = 0.414578 (edge of the socket) to r = 0.942327.
- **Round R0.03** c=(0.942327, 14.33) to (0.971871, 14.324791).
- **Skirt:** line to (1.094665, 15.021191), a cone of **10 deg half-angle** widening upward.
- **Concave cove R0.3744** c=(1.463377, 14.956177) to (1.276177, 15.280417) (50 deg of arc).
- **Shoulder:** line to (1.425, 15.36634) (30 deg above horizontal; cone of half-angle 60 deg).
- **Round R0.03** c=(1.41, 15.392321) to (1.44, 15.392321).
- **Rim cylinder r = 1.44 (diameter 2.88)** up to y = 15.72; **round R0.03** c=(1.41, 15.72) to (1.41, 15.75).
- **Top face y = 15.75** in to the axis.
- **Ball socket:** the sphere **R0.75 centred (0, 14.925, 0)** (the same sphere as the screw ball), from the bottom
  opening (r 0.414578 at y = 14.3) up to its apex y = 15.675 (closed top).

**D2. 36 studs on the top face:** each a **cone of base diameter 0.25 (R0.125) on the face y = 15.75, half-angle
49.485 deg** (it would come to a point at y = 15.856821), its tip rounded by a **sphere R0.06125 centred on the stud
axis at y = 15.77625** (tangent to the cone; stud top y = 15.8375, 0.0875 above the face). Stud axes (x, z):
- the 16 points x, z each in {-0.48, -0.16, 0.16, 0.48} (pitch 0.32);
- (+/-1.19, z) for z in {-0.48, -0.16, 0.16, 0.48} (8 studs);
- (x, +/-1.19) for x in {-0.48, -0.16, 0.16, 0.48} (8 studs);
- (+/-0.835, +/-0.835) (4 studs).

**D3. Set screw holes:** three **through holes diameter 0.125 (R0.0625)**, from the skirt into the socket, at **az 90,
210 and 330 deg**. Each axis lies in the vertical half-plane of its azimuth, passes through the point **(0, 14.855184,
0)** on the jack axis and points outward and **down at 10 deg** below horizontal (normal to the skirt cone). For az 90
the axis direction is (0, -0.173648, 0.984808); it meets the skirt at distance 1.04921 from (0, 14.855184, 0) (point
(0, 14.673, 1.0333)).

### H1 Set screw (3 identical bodies, 22 faces each)

Described in the frame of its hole (D3): distance **s** along the hole axis from **C = (0, 14.855184, 0)**, outward.
- **Body:** cylinder **diameter 0.125 (R0.0625)** on the hole axis.
- **Outer end:** flat face at **s = 1.04921** (flush with the skirt at the axis); edge chamfer **0.01 x 45 deg**
  (radius 0.0525 at the face, 0.0625 at s = 1.03921).
- **Hex socket:** **0.0625 across flats** (corner radius 0.036084), from the outer face to a flat bottom at **s =
  0.99921** (0.05 deep). Flat orientation: with e1 = horizontal unit vector perpendicular to the axis (for H1-a,
  e1 = +X) and e2 = axis x e1, the flat normals are at **49.702 deg + k 60 deg** from e1 toward e2. The socket mouth has
  a **120 deg countersink** (cone of half-angle 60 deg) whose diameter at the outer face is 0.072169 (it just nicks the
  middle of each flat).
- **Inner end (tip):** the cylinder ends on the **ball sphere R0.75 centred (0, 14.925, 0)** (the tip is that spherical
  surface; on the axis at s = 0.73464), with a small edge break of about 0.008 radially between the side and the tip
  (free-form in the source; its exact form is undetermined).
- **Placement:** **H1-a** in the az 90 hole (axis (0, -0.173648, 0.984808)); **H1-b** in the az 210 hole (axis
  (-0.852869, -0.173648, -0.492404)); **H1-c** in the az 330 hole (axis (0.852869, -0.173648, -0.492404)). H1-b and
  H1-c are H1-a rotated about the Y axis by 120 deg and 240 deg (from +X toward +Z), hex orientation included.

## 5. Assembly

All six bodies are built in place with identity placement.
- The screw stands in the base bore: thread crests (r 0.75) on the bore (r 0.75), face contact over y 9.08 to 12.0; the
  head underside y = 12.0 rests on the base top face y = 12.0.
- The saddle socket and the screw ball are the same sphere (face contact); the saddle bottom opening (r 0.414578) is
  smaller than the screw neck (r 0.65), so **the saddle overlaps the screw neck** between y = 14.3 and y = 14.550834
  (a ring of overlap, see section 6). Keep it.
- Each set screw fills its saddle hole exactly (same diameter) and its tip lies on the ball sphere (face contact).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (set
screws 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Base with handle | 59.70921 | 978458.65 | 228.1612 | 147200.50 | 0.0298 | 3.2264 | 0.0015 | -3.0874 | 3.0874 | 0.0000 | 12.0000 | -3.0874 | 3.0874 | 86 |
| P02 | Lifting screw | 24.79424 | 406304.77 | 119.2907 | 76961.58 | -0.0001 | 8.6023 | 0.0003 | -1.1250 | 1.1250 | 0.3200 | 15.6750 | -1.1250 | 1.1250 | 110 |
| P03 | Saddle | 4.81024 | 78825.64 | 28.1663 | 18171.75 | 0.0000 | 15.2290 | 0.0000 | -1.4400 | 1.4400 | 14.3000 | 15.8375 | -1.4400 | 1.4400 | 168 |
| H1-a | Set screw at az 90 | 0.00367 | 60.19 | 0.1550 | 100.01 | 0.0000 | 14.7012 | 0.8714 | -0.0625 | 0.0625 | 14.6132 | 14.7871 | 0.7073 | 1.0424 | 22 |
| H1-b | Set screw at az 210 | 0.00367 | 60.19 | 0.1550 | 100.01 | -0.7547 | 14.7012 | -0.4357 | -0.9222 | -0.5950 | 14.6132 | 14.7871 | -0.5661 | -0.3104 | 22 |
| H1-c | Set screw at az 330 | 0.00367 | 60.19 | 0.1550 | 100.01 | 0.7547 | 14.7012 | -0.4357 | 0.5950 | 0.9222 | 14.6132 | 14.7871 | -0.5661 | -0.3104 | 22 |

Exact extremes: base X and Z +/-3.087372, Y 0 to 12.0; screw Y 0.32 to 15.675; saddle Y 14.3 to 15.8375.
**Whole assembly:** 6 bodies; total volume 89.32470 in3 (1463769.64 mm3); total area 376.0832 in2 (242633.85 mm2);
centre of mass (0.0199, 5.3664, 0.0011) in; bounding box X [-3.087372, 3.087372], Y [0, 15.8375], Z [-3.087372,
3.087372] in (mm: X [-78.4193, 78.4193], Y [0, 402.2725], Z [-78.4193, 78.4193]).

**Overlap in the original** (keep): saddle P03 with screw P02, **0.09048 in3 (1482.79 mm3)**: the ring between the neck cylinder r 0.65 and the socket sphere, y 14.3 to 14.550834. All other pairs touch with zero
overlap.

**Key functional checks:** height to the saddle top face 15.75 (to the stud tops 15.8375); saddle diameter 2.88; base
height 12.0; base outer diameter 6.1747; thread 1.5 diameter, 3 per inch, root diameter 1.166667; turning-bar holes
diameter 0.87 at y 13.0875.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Base diameter | 6.25 (drawing), 6 1/4 (product data) | 6.1747 over the foot round (6.0497 flat underside) | Follow the 3D. |
| Minimum height | 15.75 | 15.75 to the saddle face, 15.8375 to the stud tops | Agree (studs excluded). |
| Saddle diameter | 2.88 (drawing), 2 7/8 (product data) | 2.88 | Agree. |
| Maximum height 25.5, lift 9.75, swivel 9 deg | drawing | not modelled (single lowered pose, no swivel clearance) | Not geometry. |

**Undetermined:** materials of the screw, saddle and set screws; the exact form of the free-form edge breaks at the
turning-bar hole mouths and at the set screw tips; the exact shape of the R0.06 handle junction blends (follow R0.06);
the buried ends of the handle sweep (any end inside the wall that does not reach the bore gives the same solid).
