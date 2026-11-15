# Design specification: panel-mount needle valve, 90 deg elbow body, five-lobe knob, tapered pipe ports

Manual flow-adjustment needle valve for panel mounting, as supplied: a brass elbow body (sphere-trimmed cube with a
bottom port and a side port), a threaded bonnet sleeve that carries a panel nut, a gland nut, a plain stem, a moulded
five-lobe knob with knurled scallops, and a set screw that clamps the knob to the stem. This document is the only
source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild
  may work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The valve (stem) axis is the line x = -0.032, z = 0, parallel to Y.** +Y points from the bottom port up to the
    knob. Every body of revolution in this document is about this axis unless another axis is named.
  - The bottom port mouth face is **y = -1.52**, the knob top face is **y = +1.52**.
  - **The side port axis is the line y = -0.585, z = 0, parallel to X**; the side port points toward **+X** and its
    mouth face is **x = 0.907**.
  - The plane z = 0 is a plane of symmetry of the valve body, the knob outline and all hexagons; it is broken only by
    the helical threads, the set screw (on the -Z side) and the knob's core holes.
- **Conventions:**
  - rho = radius from the valve axis: rho = sqrt((x + 0.032)^2 + z^2).
  - "(rho, y)" = half-section of a body of revolution about the valve axis.
  - **Plan angle** psi = angle in the XZ plane about the valve axis, measured **from +X toward +Z** (psi = 90 deg is
    +Z, psi = 270 deg is -Z).
  - A hexagon "with flats normal to X" has two flats normal to X and four flats whose normals are at plan angles
    +/-60 deg and +/-120 deg; AF = across flats.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description and the source's own simplifications

From the bottom up: the **valve body** (P01) is a cube trimmed by a sphere, with a round boss down to the bottom port
and a round boss out to the side port, and on top a neck, a wrench hexagon and a short round spigot with a
counterbore. The **bonnet sleeve** (P02) sits in that counterbore; its outside carries the panel thread (9/16 in,
18 per inch) on which the **panel nut** (H1) is screwed; its inside carries a 7/16 in, 20 per inch thread into which
the **gland nut** (P03) is screwed. The **stem** (P04) is a plain rod through the gland nut. The **knob** (P05) sits
on the top of the stem and is held by the **set screw** (H2).

**Simplifications that exist in the source model and must be reproduced:**
- **No flow passages and no needle tip.** Both ports are blind; they do not meet each other or the stem bore. The
  stem is a plain cylinder with flat ends (no needle point, no stem thread, no packing).
- **The stem overlaps the valve body.** The body's stem bore stops at y = -0.0425, but the stem continues down to
  y = -0.21. Inside the body there is a closed internal void exactly the size of the stem's lowest 0.0325
  (section 4, B10). The overlap between stem and body is 107.73 mm3 and is part of the source.
- **Four helical threads are modelled** (T1 to T4, section 4). Mating threads share the same surfaces exactly (zero
  clearance): gland nut and sleeve fill each other's thread completely, and so do sleeve and panel nut.
- The set screw and its hole in the knob are plain cylinders (no thread). The knob is a hollow shell open at the
  bottom (moulded part).

## 3. Part list

5 distinct custom parts and 2 distinct hardware items, 7 distinct, **7 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Valve body, elbow | custom | brass |
| P02 | 1 | Bonnet sleeve, threaded inside and outside | custom | brass |
| P03 | 1 | Gland nut (packing nut) | custom | brass |
| P04 | 1 | Stem, plain rod diameter 0.249 | custom | stainless steel |
| P05 | 1 | Five-lobe knob | custom | plastic |
| H1 | 1 | Panel nut, hexagon AF 0.687 | hardware | brass |
| H2 | 1 | Set screw, diameter 0.125, hexagon socket | hardware | steel |

## 4. Part geometry

### Threads (common definitions)

Each thread is a helical groove of constant cross-section. In any half-plane that contains the thread axis, the
profile is a **trapezoidal groove: two straight flanks at 30 deg to the plane normal to the axis (60 deg included),
a flat at the outer radius and a flat at the inner radius** (the flats are parallel to the axis). Widths below are
axial widths. **Phase:** for each thread a reference half-plane (theta = 0) and the axial positions of the flat centres
in it are given; at angle theta (in the stated direction) every position moves by **+ p * theta / 360 deg**, i.e.
deeper along the stated depth coordinate a. **All four threads are right-hand.**

**T1. Bottom port, tapered pipe thread, 18 per inch (p = 0.055556)**, internal, in P01.
- Axis: valve axis. **Depth a = y + 1.52** (a = 0 at the mouth face y = -1.52, increasing upward).
- theta = 0 in the half-plane toward **+X**; theta increases toward **-Z**.
- Both cones have the half-angle **1.7833 deg** (radius changes by 0.031135 per unit of a, the port being wider at
  the mouth). **Root cone** (outer radius) **r_r = 0.27000 - 0.031135 a** (diameter 0.540 at the mouth).
  **Crest cone** (inner radius) **r_c = 0.23316 - 0.031135 a**. Thread depth 0.03684.
- Root flats 0.00605 wide, centred (theta = 0) at **a = 0.05858 + n p** (n = 0, 1, 2, ...: 0.05858, 0.11414,
  0.16969, ...). Crest flats 0.00694 wide, centred at **a = 0.08681 + n p** (0.08681, 0.14236, ...). Example: at
  theta = 90 deg (half-plane toward -Z) the root flats are centred at 0.07247, 0.12803, ...
- Extent: the groove runs out into the mouth chamfer and into the bottom cone of the port (P01, B8).

**T2. Side port, tapered pipe thread, 18 per inch (p = 0.055556)**, internal, in P01. Same profile as T1.
- Axis: side port axis. **Depth a = 0.907 - x** (a = 0 at the mouth face x = 0.907, increasing toward -X).
- theta = 0 in the half-plane toward **+Z**; theta increases toward **+Y**.
- Root cone **r_r = 0.27000 - 0.031135 a**; crest cone **r_c = 0.23316 - 0.031135 a**.
- Root flats 0.00605 wide centred (theta = 0) at **a = 0.04470 + n p**; crest flats 0.00694 wide at
  **a = 0.07292 + n p**. Example: at theta = 90 deg (toward +Y) the root flats are at 0.05858, 0.11414, ...
- Extent: runs out into the mouth chamfer and into the bottom cone (P01, B9).

**T3. Gland thread, straight, 20 per inch (p = 0.05)**, external on P03, internal in P02 (same surfaces).
- Axis: valve axis. **Depth a = y.** theta = 0 toward **+X**, theta increases toward **-Z**.
- **Outer radius 0.21875** (diameter 0.4375), **inner radius 0.18627** (depth 0.03248).
- Outer flats 0.00625 wide centred (theta = 0) at **y = 0.00408 + 0.05 n**; inner flats 0.00625 wide centred at
  **y = 0.02908 + 0.05 n**. Example: at theta = 0 the outer flats in the range of P03 are centred at
  y = 0.05408, 0.10408, ..., 0.40408; at theta = 90 deg (toward -Z) at 0.06658, 0.11658, ...

**T4. Panel thread, straight, 18 per inch (p = 0.055556)**, external on P02, internal in H1 (same surfaces).
- Axis: valve axis. **Depth a = y.** theta = 0 toward **+X**, theta increases toward **-Z**.
- **Outer radius 0.28125** (diameter 0.5625), **inner radius 0.24517** (depth 0.03608).
- Outer flats 0.00694 wide centred (theta = 0) at **y = 0.05292 + n p** (..., 0.22014, 0.27569, 0.33125, 0.38681);
  inner flats 0.00694 wide centred at **y = 0.02514 + n p** (..., 0.19236, 0.24792, 0.30347, 0.35903, 0.41458).

### P01 Valve body (one solid, 112 faces in the original)

**B1. Central block:** the box **x from -0.4035 to 0.3395, y from -0.96 to -0.21, z from -0.3715 to 0.3715**
(0.743 x 0.75 x 0.743, centred on (-0.032, -0.585, 0)), **intersected with the sphere of radius 0.52538 centred at
(-0.032, -0.585, 0)**. Each of the six box faces is therefore a flat disc (radius 0.3715 on the four side faces,
0.368 on the top and bottom faces) and the sphere forms the corners.

**B2. Bottom boss:** cylinder **R0.35** about the valve axis from the block bottom y = -0.96 down to the **bottom
face y = -1.52**; the outer bottom edge is rounded **R0.045** (round centre at rho = 0.305, y = -1.475).

**B3. Side boss:** cylinder **R0.35** about the side port axis from the block face x = 0.3395 out to the **end face
x = 0.907**; the outer end edge is rounded **R0.045** (round centre 0.305 from the side port axis at x = 0.862).

**B4. Neck:** cylinder **R0.311** about the valve axis from the block top y = -0.21 up to y = -0.1775.

**B5. Body hexagon:** hexagonal prism **AF 0.687** (flats at rho 0.3435), flats normal to X, from **y = -0.1775 to
y = -0.0425**; its six corners are rounded **R0.09375** (corner axes parallel to Y at distance 0.288386 from the valve
axis, plan angles 30, 90, 150, 210, 270, 330 deg; largest radius 0.382136). Both ends are chamfered by cones about the
valve axis with **half-angle 60 deg**: bottom cone through (rho 0.3435, y -0.1775) widening upward, rho = 0.3435 +
1.73205 (y + 0.1775); top cone through (rho 0.34, y -0.0425) widening downward, rho = 0.34 + 1.73205 (-0.0425 - y).
The flat bottom face of the hexagon is the ring y = -0.1775 between rho 0.311 and 0.3435.

**B6. Spigot:** cylinder **R0.34** from y = -0.0425 up to the **top face y = 0.1475**.

**B7. Stem bores (from the top):** counterbore **R0.21875** from y = 0.1475 down to a flat floor at **y = 0.0525**,
then bore **R0.1245** down to a flat end at **y = -0.0425**.

**B8. Bottom port** (thread T1). From the mouth up: mouth chamfer = cone about the valve axis, **half-angle 46.7833
deg**, radius **0.28434 at the mouth face y = -1.52**, narrowing upward (rho = 0.28434 - 1.06427 (y + 1.52)) until it
meets the thread; the threaded bore T1; a **bottom cone** of the same half-angle, rho = 0.21181 + 1.06427 (-1.0275 - y),
from the thread up to a **flat bottom at y = -1.0275 (radius 0.21181)**. The mouth face is the ring y = -1.52 between
rho 0.28434 and 0.305.

**B9. Side port** (thread T2). From the mouth inward: mouth chamfer = cone about the side port axis, **half-angle 45
deg**, radius **0.28389 at x = 0.907**, narrowing inward (r = 0.28389 - (0.907 - x)); the threaded bore T2; a bottom
cone of half-angle 45 deg, r = 0.21158 + (x - 0.407), down to a **flat bottom at x = 0.407 (radius 0.21158)**.

**B10. Internal void:** a closed cylindrical cavity **R0.1245** on the valve axis from **y = -0.21 to y = -0.1775**,
not connected to anything (it is where the stem's lower end sits).

### P02 Bonnet sleeve (one solid, 43 faces)

Body of revolution, threaded both sides. Half-section outer contour (rho, y), from the bottom:
- bottom face **y = 0.0525**, ring from the T3 thread out to **rho 0.21875**;
- cylinder **rho 0.21875** up to y = 0.1475 (this part sits in the body counterbore B7);
- shoulder **y = 0.1475** out to **rho 0.239152**; cylinder rho 0.239152 up to y = 0.174846;
- 45 deg cone rho = 0.28125 - (0.216944 - y) up to (0.28125, 0.216944);
- **external thread T4** up to the top chamfer: cone **rho = 0.267361 + (0.4175 - y)** (45 deg) from rho 0.28125
  (y = 0.403611) to the **top face y = 0.4175**; the T4 groove runs out into both 45 deg cones;
- top face y = 0.4175, ring from rho 0.267361 in to the internal thread.
- **Inside: internal thread T3 over the full length** y = 0.0525 to 0.4175 (outer radius 0.21875, inner radius
  0.18627), no chamfers; the groove runs out through both end faces. Between y = 0.0525 and 0.1475 the outside radius
  (0.21875) equals the groove's outer radius, so along the helical outer flat of the groove the wall has zero
  thickness there (the outer cylinder is cut into a helical band). This is how the source is; keep it.

### P03 Gland nut (one solid, 50 faces)

- **Through bore R0.1245** (the stem diameter) from y = 0.0525 to y = 0.6422.
- **External thread T3** from the bottom face **y = 0.0525** up to y = 0.44431, where a 45 deg cone
  **rho = 0.180861 + (0.4822 - y)** steps down to the **neck cylinder rho 0.180861** (y = 0.4822 to 0.5222). The
  groove runs out through the bottom face and into the cone.
- **Hexagon AF 0.437** (flats at rho 0.2185, normal to X), sharp corners, from **y = 0.5222 to the top face
  y = 0.6422**; both ends chamfered by 60 deg half-angle cones: bottom rho = 0.2185 + 1.73205 (y - 0.5222), top
  rho = 0.2185 + 1.73205 (0.6422 - y) (they only cut the corners, down to the AF circle at the end faces).

### P04 Stem (one solid, 4 faces)

Cylinder **R0.1245 (diameter 0.249)** on the valve axis from **y = -0.21 to y = 1.08**, flat ends.

### P05 Knob (one solid, 255 faces)

The knob is a five-lobe moulded shell open at the bottom, on a central hub. Plan geometry (all axes parallel to Y):

**K1. Outer plan outline** (between y = 1.12 and 1.37, before knurling): the circle **rho = 0.875** minus five
**scallop** circles of **radius 0.3125** whose centres lie on rho = 0.9 at plan angles **psi = 36, 108, 180, 252, 324
deg** (centres (0.696115, 0.529007), (-0.310115, 0.855951), (-0.932, 0), (-0.310115, -0.855951), (0.696115, -0.529007)
as (x, z)). The five lobes (centred at psi = 0, 72, 144, 216, 288 deg) are joined to the scallops by convex vertical
**corner rounds R0.06**, tangent to the lobe circle and to the scallop circle (round axes on rho = 0.815, at
psi = +/-11.552 deg from each lobe centre, e.g. (0.76649, +/-0.163215)).

**K2. Outer vertical profile:**
- **Bottom face y = 1.08.** Bottom edge chamfer 0.04 x 45 deg all round the outline: lobe arcs rho = 0.875 - (1.12 - y),
  scallops r' = 0.3525 - (y - 1.08) (r' = distance from the scallop axis), corner rounds 0.06 - (1.12 - y) about the
  round axis (y from 1.08 to 1.12).
- **Top surface:** flat disc **y = 1.52 for rho <= 0.375**, then a shallow cone **y = 1.52 - (rho - 0.375) tan 5 deg**
  (falls 0.0875 per unit radius).
- **Top edge chamfers 45 deg:** over the lobes the cone about the valve axis **rho = 0.725 + (1.52 - y)** from the
  lobe wall (rho 0.875, y 1.37) up to the top cone (rho 0.758586, y 1.486414); over each scallop the cone about the
  scallop axis **r' = 0.3125 + (y - 1.37)** from y = 1.37 up to the top cone. The corner round cylinders run up until
  they meet these two cones (they carry no chamfer of their own).

**K3. Knurl in the scallops:** each scallop wall carries **8 straight V-grooves parallel to Y**. In a scallop's local
polar coordinates (r' from the scallop axis, angle phi measured at the scallop axis, phi = 0 pointing at the valve
axis, symmetric about phi = 0) the knurled wall is the zigzag through the **ridges at r' = 0.3125, phi = k x 16.5330
deg (k = -3 ... 3)** and the **groove bottoms at r' = 0.3425, phi = (k + 1/2) x 16.5330 deg (k = -4 ... 3)**, joined by
straight flanks (each groove is a V between two neighbouring ridge points). The ridges are sharp (no land). The two
outermost flanks run from the groove bottom at phi = +/-57.8656 deg toward the point r' = 0.3125, phi = +/-66.132 deg
(which lies just beyond the corner round's tangent point at phi = +/-64.890 deg) and end where they meet the corner
round (at about r' 0.3128, phi +/-66.01 deg). The grooves are open
at the bottom (they run out through the bottom chamfer, where the groove bottom leaves it at y = 1.09) and end at a
**flat horizontal end y = 1.365**; above it the plain scallop cylinder r' = 0.3125 remains from 1.365 to 1.37.
Example (scallop at psi = 180 deg, centre (-0.932, 0)): ridge points (x, z) (-0.6195, 0), (-0.632420, +/-0.088927),
(-0.670112, +/-0.170502), (-0.729459, +/-0.237977); groove bottoms (-0.593059, +/-0.049244), (-0.621085, +/-0.143660),
(-0.674821, +/-0.226197), (-0.749822, +/-0.290030).

**K4. Shell (cavity open at the bottom):** the lobe ring and the top are a shell of **wall 0.1** (measured normal to
the outer surface, knurl and corner rounds not offset). Inner surfaces:
- **Ceiling:** y = 1.419618 - (rho - 0.375) tan 5 deg (the top cone offset 0.1 down), from the hub (rho 0.375) outward.
- **Lobe inner walls rho = 0.775** (y 1.16 to 1.328579), **scallop inner walls r' = 0.4125** about the same five
  scallop axes; inner corners sharp (no rounds).
- Inner top chamfers 45 deg (offset of the outer ones): lobes rho = 0.654289 + (1.449289 - y), scallops
  r' = 0.383211 + (y - 1.299289), each from the inner wall up to the ceiling (over the lobes they meet the ceiling at
  rho 0.713579, y 1.39).
- **Bottom lip** (offset of the bottom chamfer, so the wall is thicker at the bottom): lobes rho = 0.775 - (1.16 - y),
  scallops r' = 0.4125 + (1.16 - y), from y = 1.16 down to the bottom face y = 1.08 (rho 0.695, r' 0.4925 there).
- The rim bottom face y = 1.08 is the ring between this lip and the outer bottom chamfer.

**K5. Hub:** cylinder **rho = 0.375** from its **bottom face y = 0.82** up into the ceiling; the bottom outer edge is
rounded **R0.005**. Inside the hub:
- **Stem bore R0.1245** from y = 0.82 up to a flat end at **y = 1.42**.
- **Seven core holes R0.03125** parallel to Y, blind, from y = 0.82 up to flat ends at **y = 1.08**, on the circle
  rho = 0.24975 at **psi = 0, 45, 90, 135, 180, 225 and 315 deg** (none at 270 deg). Example centres (x, z):
  (0.21775, 0), (0.1446, 0.1766), (-0.032, 0.24975), (-0.2086, 0.1766), (-0.28175, 0), (-0.2086, -0.1766),
  (0.1446, -0.1766).
- **Set screw hole R0.0625**, plain, axis parallel to Z through (x -0.032, y 0.95), from the stem bore out through
  the hub wall on the **-Z** side.

### H1 Panel nut (one solid, 41 faces)

- **Hexagon AF 0.687** (flats at rho 0.3435, normal to X), corners rounded **R0.0625** (round axes at distance
  0.324471 from the valve axis, plan angles 30, 90, ... 330 deg; largest radius 0.386971), from **y = 0.2355 to
  y = 0.3295** (0.094 thick).
- Both faces chamfered by 60 deg half-angle cones from the AF circle: rho = 0.3435 + 1.73205 (y - 0.2355) and
  rho = 0.3435 + 1.73205 (0.3295 - y).
- **Internal thread T4**; both ends countersunk by 45 deg half-angle cones of radius **0.288194 at the faces**:
  rho = 0.288194 - (y - 0.2355) and rho = 0.288194 - (0.3295 - y), each until it meets the thread.

### H2 Set screw (one solid, 21 faces)

- Cylinder **R0.0625 (diameter 0.125)**, axis parallel to Z through (x -0.032, y 0.95), from the **inner end
  z = -0.1245** (flat, it touches the stem along a line) to the **outer end z = -0.369755** (length 0.245255).
- Both ends chamfered 45 deg by 0.00625 (radius 0.05625 at the end faces).
- **Hexagon socket AF 0.0625** in the outer end, flats normal to Y (y = 0.91875 and 0.98125) and at +/-60 deg to
  them, **0.0625 deep** (flat floor z = -0.307255); the mouth has a 120 deg countersink (60 deg half-angle cone of
  radius 0.036084 at the end face, i.e. through the hexagon corners, down to the AF circle). No thread.

## 5. Assembly

All seven bodies are built in place with identity placement.
- The bonnet sleeve's lower cylinder (rho 0.21875, y 0.0525 to 0.1475) fills the body counterbore B7 (face contact);
  its shoulder y = 0.1475 lies on the body top face.
- The gland nut is screwed into the sleeve (T3 surfaces shared); both bottom faces are at y = 0.0525 (on the
  counterbore floor).
- The panel nut sits on the sleeve thread T4 from y = 0.2355 to 0.3295.
- The stem passes through the gland nut bore and the body bore (same radius 0.1245, face contact) and into the knob
  bore up to y = 1.08; its lower end is in the void B10 and it **overlaps the body by 107.73 mm3** between
  y = -0.1775 and -0.0425 (source condition, keep it).
- The set screw's inner end touches the stem; its outer end is 0.005 below the hub surface.
- **The only overlapping pair is stem / valve body (107.73 mm3).** All other contacts are zero-volume.

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body
(hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information
only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Valve body | 0.75703 | 12405.43 | 9.1056 | 5874.60 | 0.0693 | -0.6052 | -0.0000 | -0.4035 | 0.9070 | -1.5200 | 0.1475 | -0.3821 | 0.3821 | 112 |
| P02 | Bonnet sleeve | 0.02428 | 397.94 | 1.7701 | 1141.98 | -0.0326 | 0.2748 | -0.0002 | -0.3133 | 0.2493 | 0.0525 | 0.4175 | -0.2813 | 0.2813 | 43 |
| P03 | Gland nut | 0.05020 | 822.55 | 1.8781 | 1211.68 | -0.0318 | 0.3626 | -0.0002 | -0.2508 | 0.1868 | 0.0525 | 0.6422 | -0.2523 | 0.2523 | 50 |
| P04 | Stem | 0.06282 | 1029.39 | 1.1065 | 713.87 | -0.0320 | 0.4350 | 0.0000 | -0.1565 | 0.0925 | -0.2100 | 1.0800 | -0.1245 | 0.1245 | 4 |
| P05 | Knob | 0.55465 | 9089.03 | 10.1341 | 6538.08 | -0.0320 | 1.2440 | 0.0010 | -0.8339 | 0.8430 | 0.8200 | 1.5200 | -0.8698 | 0.8698 | 255 |
| H1 | Panel nut | 0.01585 | 259.71 | 0.7294 | 470.61 | -0.0329 | 0.2825 | 0.0009 | -0.3755 | 0.3115 | 0.2355 | 0.3295 | -0.3870 | 0.3870 | 41 |
| H2 | Set screw | 0.00278 | 45.60 | 0.1311 | 84.59 | -0.0320 | 0.9500 | -0.2401 | -0.0945 | 0.0305 | 0.8875 | 1.0125 | -0.3698 | -0.1245 | 21 |

Exact extremes: body X from -0.4035 to 0.907, Y from -1.52 to 0.1475; knob Y from 0.82 to 1.52, X from -0.83393 to
0.843, Z +/-0.86985. **Whole assembly:** 7 bodies; total volume 1.46760 in3 (24049.65 mm3, the stem / body overlap
counted twice); total area 24.8549 in2 (16035.41 mm2); centre of mass (0.0202, 0.1984, -0.0001) in; bounding box
X [-0.83393, 0.907], Y [-1.52, 1.52], Z [-0.86985, 0.86985] in (mm: X [-21.182, 23.038], Y [-38.608, 38.608],
Z [-22.094, 22.094]).

**Key functional checks:** overall height 3.04 (bottom port face to knob top); body width 1.3105 (block face x =
-0.4035 to side port face); side port face 0.939 from the valve axis; ports tapered 18 per inch (root diameter 0.540 at
the mouth); panel thread diameter 0.5625, 18 per inch; knob diameter 1.75 over the lobes.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall height | 3.04 (drawing), 3 1/16 (product data) | 3.04 | Follow the 3D (agrees with the drawing). |
| Overall length | 1.31 (drawing), 1 5/16 (product data) | 1.3105 | Agree. |
| Port-to-port length | 0.94 (drawing), 15/16 (product data) | 0.939 | Agree. |
| Panel cutout diameter | 0.562 | panel thread outer diameter 0.5625 | Agree. |
| Stem | needle valve | plain rod, no needle, overlaps the body | Follow the 3D. |

**Undetermined:** the internal flow path, seat, needle point and packing (not modelled); the thread of the set screw
(modelled plain); the exact run-out shape of each thread groove where it meets a chamfer or cone (the groove is simply
cut through those surfaces).
