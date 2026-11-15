# Design specification: diaphragm air pulse valve body with cover (filter cleaning), 90 deg elbow, tapered pipe threads

Normally closed diaphragm pulse valve as supplied without its solenoid: a cast aluminium body with a side inlet and a
bottom outlet, a flat diaphragm, a cover with a threaded pilot port on top, and three pan head screws. This document is
the only source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. Many values
  are round millimetres; where so, the mm value is given in brackets and is the exact one. A rebuild may work in
  millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The valve axis is the Y axis** (x = 0, z = 0); +Y points from the outlet (bottom) to the pilot port (top).
  - **y = 0.125 is the joint face** between the body and the diaphragm (top face of the body flange).
  - **The inlet port points toward +X**; its axis is the line **y = -0.24803 [-6.3 mm], z = 0**, parallel to X.
  - The whole assembly is symmetric about the plane z = 0 except the screw positions and their cross recesses
    (section 4, H1).
- **Profile coordinate conventions:**
  - "(r, y)" = half-section of a body of revolution about the Y axis (r = radius from the Y axis).
  - "(x, y)" = profile in a plane normal to Z; "(z, y)" = profile in a plane normal to X.
  - "arc R c=(a, b) to (p, q)" = circular arc of radius R about centre (a, b) to (p, q), the short way.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description

The **body** (P01) has a round flange on top (joint face y = 0.125), a round barrel below it whose underside is cut by a
25 deg inclined plane, a round outlet boss on the axis ending in the bottom face with the outlet thread, and a
U-shaped inlet boss running out to +X with the inlet thread. The **diaphragm** (P03) is a thin flat disc on the joint
face. The **cover** (P02) is a round disc with a central hub carrying the threaded pilot port. Three **pan head screws**
(H1-a, H1-b, H1-c) pass through the cover and the diaphragm into blind holes in the body flange.

**Simplifications that exist in the source model and must be reproduced:**
- No internal valve passages: the outlet bore, the inlet bore and the pilot port are blind; the body top face
  (y = 0.125) is closed; no diaphragm seat, no spring, no solenoid, no seals.
- The three pipe threads ARE modelled as tapered helical grooves (section 4, "Threads"). The screw holes in the body
  are plain (unthreaded) holes of the screw shank diameter; the screw shanks are plain cylinders (no thread).
- The diaphragm is a plain disc (no convolutions).

## 3. Part list

3 distinct custom parts and 1 distinct hardware item, 4 distinct, **6 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Valve body | custom | aluminium |
| P02 | 1 | Cover with pilot port | custom | aluminium |
| P03 | 1 | Diaphragm, flat disc | custom | nitrile rubber |
| H1 | 3 | Pan head cross-recess screw, plain shank diameter 0.138 (H1-a, H1-b, H1-c) | hardware | brass |

## 4. Part geometry

### Threads (common definition, used in P01 and P02)

All three ports are **internal tapered pipe threads, right-hand, with a 60 deg thread form**, modelled as one helical
groove cut into a tapered bore:
- **Taper:** every thread surface (crest cone and root cone) has a half-angle of **1.783 deg** about the port axis:
  the radius changes by **0.031127 per unit of axial length**, the port being wider at its mouth.
- **Crest cone** = the bore surface left between the grooves (smallest radius). **Root cone** = the groove bottom.
- **Groove cross-section** (in any half-plane that contains the port axis): a trapezoid whose two flanks are straight
  lines at **30 deg to the plane normal to the axis**, with a flat on the crest cone and a flat on the root cone. The
  widths given below are axial widths. The groove is symmetric about the plane normal to the axis through its root
  flat centre; it is defined by the root flat (centre and width, on the root cone) and the two 30 deg flanks, which run
  until they meet the crest cone. (Because of the taper the two flanks reach the crest cone at slightly different
  radii; the groove width quoted at the crest cone is the mean.) In the original each crest flat and each root flat is
  parallel to the axis (constant radius over its short length, equal to the cone radius at the flat's centre); the
  cones are the envelope. On the long crest flats of T2 this differs from the cone by at most 0.0008.
- **Phase:** for each thread a reference half-plane (angle theta = 0) and the axial positions a of the root flat
  centres in it are given. For other angles theta (measured in the stated direction) every position moves by
  **a + p * theta / 360 deg** (deeper into the port as theta increases); this is a right-hand thread.
- **Depth coordinate a** is measured along the port axis from the stated origin, positive into the port.

**T1. Outlet thread** (P01, bottom port; 18 threads per inch, pitch p = 0.055556): axis = Y axis; **a = -y** (a = 0 at
y = 0, increasing downward toward the bottom face); theta = 0 in the half-plane toward +X, theta increases toward +Z.
- Crest cone r_c = 0.20214 + 0.031127 a (r_c = 0.20986 at the shoulder, 0.23315 at the bottom face).
- Root cone r_r = 0.23899 + 0.031127 a (r_r = 0.26999, diameter 0.540, at the bottom face). Groove depth 0.03685.
- Groove: 0.04862 wide at the crest cone, root flat 0.00604 wide; crest flats 0.00694 wide.
- Root flat centres at theta = 0: a = 0.27081 + n p (n = 0, 1, ...); crest flat centres a = 0.29815 + n p. Example:
  in the half-plane z = 0, x > 0 the crest flats run from a = 0.29467 to 0.30162, 0.35023 to 0.35717, ...
- Extent: the whole bore from the shoulder plane y = -0.24803 [-6.3 mm] to the bottom face y = -0.99606 [-25.3 mm]
  (19.0 mm long). The groove runs out through both ends; no chamfer at the mouth.

**T2. Inlet thread** (P01, side port; 18 per inch, p = 0.055556): axis = line y = -0.24803, z = 0; **a = 1.18898 - x**
(a = 0 at the inlet end face x = 1.18898 [30.2 mm], increasing toward -X); theta = 0 in the half-plane toward +Z,
theta increases toward +Y.
- Crest cone r_c = 0.26623 - 0.031127 a. Root cone r_r = 0.26999 - 0.031127 a (diameter 0.540 at the end face).
  **This groove is very shallow: depth 0.00376.**
- **The groove is undercut (dovetail):** 0.00348 wide at the crest cone and 0.0078 wide at the root cone; both flanks
  lean outward (away from the groove centre) at 30 deg going deeper. The crest flats are 0.05208 wide.
- Root flat centres at theta = 0: a = 0.07337 + n p (0.07337, 0.12893, 0.18448, ...).
- Extent: from the mouth chamfer (below) to the shoulder plane x = 0.68898 (a = 0.5).
- **Mouth chamfer:** cone of half-angle 46.783 deg about the inlet axis, diameter 0.60454 (r 0.30227) at the end face,
  narrowing into the port until it meets the thread (about a = 0.035).

**T3. Pilot thread** (P02, top port; 27 per inch, p = 0.037037): axis = Y axis; **a = 0.99606 - y** (a = 0 at the hub
top face y = 0.99606 [25.3 mm], increasing downward); theta = 0 toward +X, theta increases toward +Z.
- Crest cone r_c = 0.17793 - 0.031127 a. Root cone r_r = 0.20250 - 0.031127 a. Groove depth 0.02457.
- Groove: 0.03241 wide at the crest cone, root flat 0.00403 wide; crest flats 0.00463 wide.
- Root flat centres at theta = 0: a = 0.03909 + n p; crest flat centres a = 0.05791 + n p.
- Extent: from the mouth chamfer to the flat port bottom y = 0.6211 (a = 0.37496); the groove runs out through the
  bottom.
- **Mouth chamfer:** cone of half-angle 46.783 deg about Y, diameter 0.46954 (r 0.23477) at the hub top face, narrowing
  downward until it meets the thread.

### P01 Valve body (one solid, 93 faces in the original)

**B1. Flange:** cylinder **R0.81496 [41.4 mm diameter]** about Y from **y = -0.025** to the joint face **y = 0.125**
(0.15 thick). The lower outer edge is rounded **R0.03125** (round centre at r = 0.78371, y = 0.00625); the flange
underside y = -0.025 remains between the barrel (r = 0.50246) and r = 0.78371.

**B2. Barrel:** cylinder **R0.50246 [25.525 mm diameter]** about Y, from the flange underside y = -0.025 down to the
**inclined plane** **y = -0.45316 - 0.46631 x** (25.0 deg to the XZ plane, descending toward +X; normal
(-0.42262, -0.90631, 0)). Everything of the barrel below that plane is removed.

**B3. Outlet boss:** cylinder **R0.36496 [18.54 mm diameter]** about Y, from the inclined plane down to the bottom
face **y = -0.99606 [-25.3 mm]**. The bottom outer edge is rounded **R0.0625** (round centre at r = 0.30246,
y = -0.93356); the bottom face is the ring from the thread out to r = 0.30246.

**B4. Rounds at the inclined plane:** convex **R0.03125** where the inclined plane meets the barrel, concave **R0.03125**
where it meets the outlet boss (both sweep 65 deg in the section z = 0).

**B5. Inlet boss**, added: profile in the plane normal to X, (z, y): the U-shape **|z| <= 0.375, y from -0.25 up to
0.125**, with the bottom a half circle **R0.375 centred (z 0, y -0.25)** (lowest point y = -0.625), extruded along X
from inside the barrel (x = 0) to the **end face x = 1.18898 [30.2 mm]**. Its top is flush with the joint face
y = 0.125; its sides z = +/-0.375 cut the flange (the flange round ends at x = 0.72356). No rounds on the inlet boss.

**B6. Outlet port** (on the Y axis, from the bottom face up): thread T1 from y = -0.99606 to the **shoulder plane
y = -0.24803**, then a **plain bore diameter 0.33716 (R0.16858)** up to a flat end at **y = -0.18553**.

**B7. Inlet port** (on the inlet axis, from the end face inward): mouth chamfer and thread T2 down to the **shoulder
plane x = 0.68898**, then a **plain bore diameter 0.38386 (R0.19193)** to a flat end at **x = 0.31398** (0.875 from
the end face). The outlet and inlet bores do not meet.

**B8. Screw holes:** three **blind holes diameter 0.138 (R0.069)**, parallel to Y, from the joint face y = 0.125 down
to a flat bottom at **y = 0.03125** (0.09375 deep), at **(x, z) = (-0.67996, 0), (0.33998, -0.58886),
(0.33998, 0.58886)** (radius 0.67996 from the axis, 120 deg apart, one on -X).

### P02 Cover (one solid, 46 faces)

**C1. Body of revolution about Y**, half-section (r, y), from the axis outward: underside **y = 0.15625** from r = 0
to **r = 0.81496**; outer cylinder up to y = 0.328125; convex round **R0.015625** c=(0.799335, 0.328125) to
(0.799335, 0.34375); disc top **y = 0.34375** in to r = 0.375; concave fillet **R0.0625** c=(0.375, 0.40625) to
(0.3125, 0.40625); **hub R0.3125 (diameter 0.625)** up to y = 0.96481; convex round **R0.03125** c=(0.28125, 0.96481)
to (0.28125, 0.99606); hub top face **y = 0.99606** in to the pilot port (r = 0.23477).

**C2. Pilot port:** chamfer and thread T3 from the hub top down to a flat bottom at **y = 0.6211** (0.375 deep).

**C3. Screw holes:** three through holes diameter 0.138 at the same (x, z) positions as B8.

### P03 Diaphragm (one solid; 12 real faces)

Flat disc **y = 0.125 to 0.15625 (0.03125 thick)**, outer radius **0.81496**, edge **fully rounded R0.015625** (the
edge is a half torus: tube radius 0.015625 about the circle r = 0.79934, y = 0.140625). Three through holes diameter
0.138 at the B8 positions. (The original file also carries 16 empty zero-area shells in this body; they are not
geometry and are ignored.)

### H1 Pan head screw (3 identical bodies, 28 faces each)

Described for **H1-a on the axis x = -0.67996, z = 0**, head up; local radius s from the screw axis:
- **Shank:** plain cylinder **diameter 0.138 (R0.069)** from a flat end at **y = 0.03125** (the body hole bottom) up to
  the head underside **y = 0.34375** (the cover top).
- **Head** (body of revolution, half-section (s, y)): underside y = 0.34375 from s = 0.069 to 0.125; convex round
  R0.01 c=(0.125, 0.35375) to (0.135, 0.35375); **cylinder s = 0.135 (head diameter 0.27)** up to y = 0.39913; convex
  round R0.01 c=(0.125, 0.39913) to (0.13132, 0.40685), tangent to the **dome: sphere R0.20725 centred on the screw axis at
  y = 0.2465** (apex would be y = 0.45375).
- **Cross recess** cut into the dome: flat floor **y = 0.40380**; floor outline (16 vertices, in (u, w) = (x - x_axis,
  z - z_axis)): (0.08, 0.01), (0.02, 0.01), (0.01, 0.02), (0.01, 0.08), (-0.01, 0.08), (-0.01, 0.02), (-0.02, 0.01),
  (-0.08, 0.01), (-0.08, -0.01), (-0.02, -0.01), (-0.01, -0.02), (-0.01, -0.08), (0.01, -0.08), (0.01, -0.02),
  (0.02, -0.01), (0.08, -0.01): two arms 0.02 wide reaching 0.08 from the axis along u and w, with a 45 deg flat
  across each inner corner. All recess walls are drafted **5 deg** so the recess opens upward; the walls end at the
  dome. The highest point left on the screw is y = 0.452.
- **H1-b** at (x, z) = (0.33998, -0.58886) and **H1-c** at (0.33998, 0.58886) are copies of H1-a rotated about the Y
  axis (by -120 deg and +120 deg respectively, i.e. the recess arms of H1-b and H1-c point at 30 deg / 120 deg in the
  XZ plane instead of 0 / 90 deg).

## 5. Assembly

All six bodies are built in place with identity placement.
- Stack on the joint: body flange top y = 0.125, diaphragm y = 0.125 to 0.15625, cover underside y = 0.15625 (face
  contacts). Body, diaphragm and cover share the outer radius 0.81496 and the axis.
- Each screw shank (diameter 0.138) fills its holes in cover, diaphragm and body exactly (same diameter, face contact),
  its end on the hole bottom y = 0.03125, its head underside on the cover top y = 0.34375.
- **No body pair overlaps** (all contacts are face contacts with zero overlap volume).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (screws
2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Valve body | 0.91185 | 14942.59 | 12.3250 | 7951.62 | 0.1901 | -0.2065 | 0.0001 | -0.8150 | 1.1890 | -0.9961 | 0.1250 | -0.8150 | 0.8150 | 93 |
| P02 | Cover | 0.54265 | 8892.36 | 7.1436 | 4608.77 | 0.0000 | 0.3614 | 0.0000 | -0.8150 | 0.8150 | 0.1562 | 0.9961 | -0.8150 | 0.8150 | 46 |
| P03 | Diaphragm | 0.06327 | 1036.77 | 4.2151 | 2719.39 | 0.0000 | 0.1406 | 0.0000 | -0.8150 | 0.8150 | 0.1250 | 0.1563 | -0.8150 | 0.8150 | 12 |
| H1-a | Screw at (-0.68, 0) | 0.00926 | 151.74 | 0.3277 | 211.44 | -0.6800 | 0.2855 | 0.0000 | -0.8150 | -0.5450 | 0.0313 | 0.4520 | -0.1350 | 0.1350 | 28 |
| H1-b | Screw at (0.34, -0.589) | 0.00926 | 151.74 | 0.3277 | 211.44 | 0.3400 | 0.2855 | -0.5889 | 0.2050 | 0.4750 | 0.0313 | 0.4520 | -0.7239 | -0.4539 | 28 |
| H1-c | Screw at (0.34, +0.589) | 0.00926 | 151.74 | 0.3277 | 211.44 | 0.3400 | 0.2855 | 0.5889 | 0.2050 | 0.4750 | 0.0313 | 0.4520 | 0.4539 | 0.7239 | 28 |

Exact extremes: body X from -0.81496 to 1.18898 [-20.7 to 30.2 mm], Y from -0.99606 to 0.125; cover Y to 0.99606
[25.3 mm]. **Whole assembly:** 6 bodies; total volume 1.54554 in3 (25326.93 mm3); total area 24.6669 in2
(15914.11 mm2); centre of mass (0.1121, 0.0159, 0.0000) in; bounding box X [-0.81496, 1.18898], Y [-0.99606, 0.99606],
Z [-0.81496, 0.81496] in (mm: X [-20.7, 30.2], Y [-25.3, 25.3], Z [-20.7, 20.7]).

**Key functional checks:** overall height 1.9921 (outlet face to pilot port face); overall width 2.0039 (flange edge to
inlet face); flange / cover / diaphragm diameter 1.6299; outlet and inlet 1/4 pipe threads 18 per inch (root cone
diameter 0.540 at the mouth), pilot 1/8 pipe thread 27 per inch; screw circle radius 0.68.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Diameter (bottom view) | 1.62 (drawing); overall length 1 5/8 (product data) | 1.6299 [41.4 mm] | Follow the 3D. |
| Overall width | 2.00 (drawing), 2 (product data) | 2.0039 | Agree within rounding. |
| Overall height | 1.99 (drawing), 2 (product data) | 1.9921 | Agree within rounding. |
| Inlet thread | 1/4 NPT | 18 per inch tapered, but only 0.0038 deep and undercut | Follow the 3D. |
| Top port | not named | 27 per inch tapered (1/8 pipe size) | Follow the 3D. |

**Undetermined:** internal passages, diaphragm seat, solenoid and pilot mechanism (none modelled); the screw thread size
(shank modelled plain at 0.138); the exact run-out of the thread grooves where they meet the mouth chamfers.
