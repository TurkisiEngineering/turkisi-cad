# Design specification: closed-body turnbuckle, clevis to clevis, 5/16-24 threads (left hand and right hand)

A closed-body turnbuckle in its fully retracted position: a round body with plain bores in both ends, two threaded
T-bolts (one left-hand, one right-hand) whose cross bars sit in two bent-strap clevises, two hex jam nuts, two headed
clevis pins and two split rings. This document is the only source for the rebuild. Every dimension below was measured
from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The turnbuckle axis is the X axis** (y = 0, z = 0). The body is centred on the origin (x from -2.5625 to 2.5625).
  - **The clevis pins are parallel to Y**, heads at +Y; their axes are the lines **x = +/-4.3125, z = 0** (pin centre
    distance 8.625).
  - The split rings hang toward **-Y** below the pins.
  - **The plane x = 0 is a mirror plane of the whole assembly:** every body on the -X side is the exact mirror image
    (x -> -x) of its partner on the +X side. A mirror image of a left-hand thread is a right-hand thread, of a
    left-hand helix a right-hand helix.
- **Notation:**
  - "(x, r)" = half-section of a body of revolution about the X axis (r = distance from the X axis), revolved 360 deg.
  - "theta" for threads = angle about the X axis, **theta = 0 on +Y, theta = 90 deg on +Z** (right-hand rotation about +X).
  - "phi" for the rings = angle about the ring axis (parallel to Z), measured from +X toward +Y.
  - "arc R c=(a, b) from P to Q" = circular arc of radius R about centre (a, b), the short way.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description

The **body** (P01) is a turned tube, 5.125 long, diameter 0.5 in the middle, necked to 0.40625 at both ends, with a
small cross hole in the middle. Each end has a plain bore of diameter 0.3125 (the thread major diameter); the body's
internal threads are **not modelled**. A **T-bolt** (P04-a at +X, P04-b at -X) runs from inside the body bore out to
a cross bar that lies in the bend of a **clevis** (P02-a / P02-b), a U-shaped bent strap whose two legs carry the
**clevis pin** (P03-a / P03-b). The **jam nut** (H2-a / H2-b) sits on the T-bolt against the body end face. A
**split ring** (H1-a / H1-b) of round wire, two turns, passes through the cross hole of each pin.

**Simplifications that exist in the source model and must be reproduced:**
- The body's internal threads are not modelled: both end bores are plain cylinders of diameter 0.3125.
- The T-bolt threads and the jam nut threads **are modelled** as real helical threads (section 4, "Thread"), left-hand
  on the +X side, right-hand on the -X side, in phase so that nut and bolt do not overlap.
- No forging draft, no cotter in the clevis, no lettering.

## 3. Part list

4 distinct custom parts and 2 distinct hardware items (6 kinds), **11 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Turnbuckle body, closed | custom | stainless steel |
| P02 | 2 | Clevis, bent strap (P02-a at +X, P02-b at -X, mirror images) | custom | stainless steel |
| P03 | 2 | Clevis pin with head and cross hole (P03-a, P03-b) | custom | stainless steel |
| P04 | 2 | T-bolt, 5/16-24, P04-a left-hand at +X, P04-b right-hand at -X (mirror images) | custom | stainless steel |
| H1 | 2 | Split ring, round wire, two turns (H1-a, H1-b, mirror images) | hardware | stainless steel |
| H2 | 2 | Hex jam nut 5/16-24, H2-a left-hand at +X, H2-b right-hand at -X (mirror images) | hardware | stainless steel |

## 4. Part geometry

All parts are described on the +X side; the -X partner is its mirror image in the plane x = 0 (section 5 lists the
placements).

### Thread (common definition: T-bolt P04 and jam nut H2)

5/16-24 single-start thread, **pitch P = 1/24 = 0.0416667**, 60 deg included angle:
- **Major radius 0.15625** (diameter 0.3125), **minor radius 0.1291867** (diameter 0.2583733); depth 0.0270633
  (= 0.75 x 0.866025 P).
- **Profile in any half-plane containing the X axis:** a symmetric trapezoid groove; the flanks are straight lines at
  30 deg to the radial direction; **flat crest 0.0052083 wide (P/8) on the major radius and flat root 0.0052083 wide
  (P/8) on the minor radius**; each flank spans 0.015625 axially.
- **Bolt (external):** material inside the minor radius everywhere; the tooth (crest flat at r = 0.15625) is centred
  between two root flats (at r = 0.1291867).
- **Nut (internal):** the exact complement. The nut's crest flats are on the minor radius 0.1291867, its root flats on
  the major radius 0.15625, so that each bolt tooth fills a nut groove exactly (zero clearance, zero overlap).
- **Hand and phase, +X side (P04-a, H2-a): LEFT-HAND.** In the half-plane theta = 0 (z = 0, y > 0) the bolt crest-flat
  centres (= the nut root-flat centres) lie at **x = 1.514531 + k P** and the bolt root-flat centres (= nut crest-flat
  centres) at **x = 1.535365 + k P** (k integer). For any other theta all these positions move by
  **-P x theta / 360 deg** (toward -X as theta increases: at theta = 90 deg, the half-plane y = 0, z > 0, the bolt
  crest centres are at x = 1.504115 + k P; at theta = 180 deg at x = 1.493698 + k P).
- **-X side (P04-b, H2-b): RIGHT-HAND**, the mirror image: at theta = 0 the bolt crest centres are at
  x = -(1.514531 + k P), root centres at x = -(1.535365 + k P), and the positions move by **+P x theta / 360 deg**.

### P01 Turnbuckle body (one solid, 42 faces)

**B1. Body of revolution about X**, symmetric about x = 0. Outer profile (x, r) for x >= 0 (mirror for x < 0):
- cylinder **r = 0.25** (diameter 0.5) from x = 0 to **x = 1.304841**;
- convex **arc R1.5 c=(1.304841, -1.25)** from (1.304841, 0.25) to (1.444852, 0.243451) (tangent to the cylinder);
- straight taper line from (1.444852, 0.243451) to (1.805148, 0.209674) (5.356 deg to the axis), tangent to both
  arcs;
- concave **arc R1.5 c=(1.945159, 1.703125)** from (1.805148, 0.209674) to (1.945159, 0.203125);
- neck cylinder **r = 0.203125** (diameter 0.40625) from x = 1.945159 to 2.5375;
- convex round **arc R0.025 c=(2.5375, 0.178125)** from (2.5375, 0.203125) to (2.5625, 0.178125);
- **end face x = 2.5625** from r = 0.178125 in to r = 0.163194.

Inner profile (x, r) for x >= 0 (a through bore, mirror for x < 0):
- 45 deg entry chamfer from (2.5625, 0.163194) to (2.555556, 0.15625) (0.006944 x 45 deg);
- **end bore r = 0.15625 (diameter 0.3125)** from x = 2.555556 to 0.572917 (plain, no thread);
- 45 deg step cone from (0.572917, 0.15625) to (0.541343, 0.124676);
- **centre bore r = 0.124676** (diameter 0.249352) from x = 0.541343 to x = 0 (and on to -0.541343).

**B2. Cross hole:** one hole **diameter 0.15625 (R0.078125)**, axis = the Z axis (x = 0, y = 0), through both walls
(it opens into the centre bore). No chamfers.

### P02 Clevis, bent strap (+X: P02-a; one solid, 24 faces)

A strap **0.0625 thick and 0.742188 wide** (z from -0.371094 to 0.371094) bent into a U around the **bend axis: the line
x = 3.346354, y = 0, parallel to Z**, open toward +X:
- **C1. U section** (in every plane z = const, before the cuts of C2 to C4): bend = half annulus about (x, y) =
  (3.346354, 0), inner radius **0.15625**, outer radius **0.21875**, on the side x <= 3.346354; two straight legs
  continue it from x = 3.346354 to x = 4.683594: leg 1 between **y = 0.15625 and 0.21875**, leg 2 between
  **y = -0.21875 and -0.15625**. Inside width between the legs **0.3125**; outer width 0.4375. Extrude this section
  from z = -0.371094 to z = 0.371094.
- **C2. Round leg ends:** seen along Y, each leg ends in a half circle **R0.371094 about the pin axis (x 4.3125, z 0)**
  (the leg outline is the rectangle x <= 4.3125, |z| <= 0.371094 plus that half circle; leg tip at x = 4.683594).
- **C3. Pin hole:** **diameter 0.332031 (R0.166016)** about the pin axis (x 4.3125, z 0, parallel to Y), through both
  legs.
- **C4. Window:** a cut through the whole strap along Y with the outline (seen along Y) **|z| <= 0.175781 for
  x <= 3.424479, closed by a half circle R0.175781 about (x 3.424479, z 0)** (window width 0.351562, it ends at
  x = 3.600260). It removes the middle of the bend and of the leg roots; the bend survives only for
  0.175781 <= |z| <= 0.371094.
- All edges sharp.

### P03 Clevis pin (+X: P03-a; one solid, 15 faces)

Body of revolution about the **pin axis x = 4.3125, z = 0 (parallel to Y)**, head up. Half-section (s, y), s = radius
from the pin axis:
(0, -0.427083) -> (0.125, -0.427083) -> (0.15625, -0.395833) [45 deg end chamfer 0.03125] -> **shank s = 0.15625
(diameter 0.3125)** up to (0.15625, 0.21875) -> head underside y = 0.21875 out to (0.213867, 0.21875) -> 45 deg chamfer
to (0.21875, 0.223633) -> **head cylinder s = 0.21875 (diameter 0.4375)** up to (0.21875, 0.283854) -> 45 deg chamfer
to (0.179687, 0.322917) -> **head top y = 0.322917** to the axis. Overall length 0.75.

**Cross hole:** **diameter 0.117188 (R0.058594)**, axis **parallel to X through y = -0.322917, z = 0**, through the
shank.

### H1 Split ring (+X: H1-a; one solid: 2 swept faces + 2 flat wire ends)

Round wire **diameter 0.046875 (R0.0234375)** swept along a **helix**: axis parallel to Z through
**(x, y) = (4.3125, -0.791667)**, **centreline radius 0.46875**, **pitch 0.0520833 per turn**, **left-hand about +Z**
(z increases while phi decreases). Centreline:
x = 4.3125 + 0.46875 cos(phi), y = -0.791667 + 0.46875 sin(phi), z = -0.029297 + 0.0520833 x (90 deg - phi) / 360 deg,
for **phi from 90 deg down to -607.5 deg (697.5 deg of sweep, about 1.94 turns)**: it starts at the top point
(4.3125, -0.322917, -0.029297), which is on the pin cross-hole axis (the wire runs through the pin hole along X), and
ends at phi = -607.5 deg (= 112.5 deg) at (4.133121, -0.358598, 0.071615). The wire cross-section is a circle normal to
the centreline; both wire ends are flat discs normal to the centreline. Ring outer diameter 0.984375, inner 0.890625.

### H2 Hex jam nut (+X: H2-a, left-hand; one solid, 45 faces)

- **Hex prism** along X from **x = 2.5625 to 2.75** (0.1875 thick), **0.5 across flats**; flats at **z = +/-0.25** and
  the four flats with normals (0, +/-0.866025, +/-0.5) at 0.25 from the axis (corners on the +/-Y directions).
- **Corners turned** to **diameter 0.558012 (R0.279006)** (cylinder about X).
- **30 deg face chamfers on both faces:** material is kept only inside the cones r <= 0.25 + 1.732051 (x - 2.5625)
  and r <= 0.25 + 1.732051 (2.75 - x) (cone half-angle 60 deg about X; each starts at r = 0.25 on the face).
- **Threaded bore:** internal thread (section "Thread", left-hand) through the full length; **45 deg bore chamfers**
  on both faces from r = 0.163194 on the face to r = 0.15625 (0.006944 deep), continuing at 45 deg into the thread.

### P04 T-bolt (+X: P04-a, left-hand; one solid, 131 faces)

- **Shank:** cylinder **r = 0.15625** about X from the **end x = 0.65625** to x = 3.346354 (the bar axis).
- **End chamfer:** flat end face x = 0.65625 out to r = 0.132812, then a **45 deg cone** to r = 0.15625 at
  x = 0.679688 (the thread runs out through it).
- **Thread:** external thread (section "Thread", left-hand) from the end x = 0.65625 to the run-out. **Run-out:** the
  thread groove is cut only where r >= 0.15625 - 1.732051 (2.938802 - x), i.e. it ends against a **cone of half-angle
  60 deg about X** that reaches the minor radius at x = 2.923177 and the major radius at x = 2.938802. From x = 2.938802
  to the bar the shank is plain (diameter 0.3125).
- **Cross bar:** cylinder **R0.15625 about the bar axis (x 3.346354, y 0, parallel to Z)**, united with the shank (equal
  radii; the two cylinders meet in two planar elliptic curves). **Bar ends:** the bar keeps only the material with
  |z| <= 0.152995 or inside one of the two **cap cylinders R0.169271 whose axes are parallel to Y through
  (x 3.346354, z +0.152995) and (x 3.346354, z -0.152995)**. Bar length (cap to cap, on the bar axis) 0.644531
  (z = +/-0.322266).
- **Cap-edge blends:** each edge where the bar cylinder meets a cap cylinder carries a **straight (chordal) blend of
  the R0.025 rolling ball**: construct the R0.025 round between the two faces, then replace the round by the ruled
  surface that joins its two tangent lines straight across (every cross-section normal to the edge is the chord of
  the R0.025 arc). Checks: on top of the bar (x = 3.346354) the blend runs from y = 0.15625, z = 0.297266 (bar) to
  y = 0.13125, z = 0.322266 (cap), a 45 deg line; in the plane y = 0 it runs from (x 3.190104, z 0.212891) to
  (x 3.192360, z 0.223270).

## 5. Assembly

All eleven bodies are built in place with identity placement, in this pose (retracted):

| ID | Placement |
|---|---|
| P01 | centred on the origin, axis X, cross hole along Z |
| P04-a | shank on the X axis from x = 0.65625 to the bar; bar axis x = 3.346354; thread left-hand, phase as in section 4 |
| P04-b | mirror image of P04-a: x from -3.502604 to -0.65625, bar axis x = -3.346354; thread right-hand |
| H2-a | x = 2.5625 to 2.75, face against the body end face; thread mates with P04-a |
| H2-b | mirror image: x = -2.75 to -2.5625 |
| P02-a | bend axis x = 3.346354, legs toward +X, pin hole at x = 4.3125 |
| P02-b | mirror image: bend axis x = -3.346354, legs toward -X, pin hole at x = -4.3125 |
| P03-a | axis x = 4.3125, z = 0, head up (+Y), cross hole along X at y = -0.322917 |
| P03-b | axis x = -4.3125, z = 0, head up, cross hole along X at y = -0.322917 |
| H1-a | helix axis through (4.3125, -0.791667), left-hand, as in section 4 |
| H1-b | mirror image: axis through (-4.3125, -0.791667), right-hand; centreline x = -4.3125 - 0.46875 cos(phi), same y and z as H1-a for the same phi (it starts at (-4.3125, -0.322917, -0.029297) and ends at (-4.133121, -0.358598, 0.071615)) |

- The T-bolt shank (diameter 0.3125) lies in the plain body bore (diameter 0.3125): face contact; the bolt end is
  0.65625 from the body centre. The bar cylinder (R0.15625) lies in the clevis bend (inner R0.15625, coaxial): face
  contact. The pin head underside y = 0.21875 sits on the leg face y = 0.21875; the pin shank (0.3125) is in the leg
  holes (0.332031) with clearance. The nut face touches the body end face; nut and bolt threads mate.
- **No body pair overlaps** (largest common volume 0.002 mm3, ring wire in the pin hole).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body
(hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Turnbuckle body | 0.51267 | 8401.10 | 12.4579 | 8037.33 | -0.0000 | -0.0000 | 0.0000 | -2.5625 | 2.5625 | -0.2500 | 0.2500 | -0.2500 | 0.2500 | 42 |
| P02-a | Clevis +X | 0.11073 | 1814.53 | 4.2968 | 2772.14 | 3.8921 | -0.0000 | 0.0000 | 3.1276 | 4.6836 | -0.2187 | 0.2188 | -0.3711 | 0.3711 | 24 |
| P02-b | Clevis -X | 0.11073 | 1814.53 | 4.2968 | 2772.14 | -3.8921 | 0.0000 | 0.0000 | -4.6836 | -3.1276 | -0.2187 | 0.2188 | -0.3711 | 0.3711 | 24 |
| P03-a | Clevis pin +X | 0.06043 | 990.34 | 1.1102 | 716.23 | 4.3125 | 0.0005 | 0.0000 | 4.0937 | 4.5312 | -0.4271 | 0.3229 | -0.2187 | 0.2187 | 15 |
| P03-b | Clevis pin -X | 0.06043 | 990.34 | 1.1102 | 716.23 | -4.3125 | 0.0005 | 0.0000 | -4.5312 | -4.0937 | -0.4271 | 0.3229 | -0.2187 | 0.2187 | 15 |
| P04-a | T-bolt +X (left-hand) | 0.21390 | 3505.22 | 4.5456 | 2932.64 | 2.2577 | 0.0000 | 0.0000 | 0.6562 | 3.5026 | -0.1563 | 0.1563 | -0.3223 | 0.3223 | 131 |
| P04-b | T-bolt -X (right-hand) | 0.21383 | 3504.10 | 4.5458 | 2932.74 | -2.2577 | 0.0000 | 0.0000 | -3.5026 | -0.6562 | -0.1563 | 0.1563 | -0.3223 | 0.3223 | 131 |
| H1-a | Split ring +X | 0.00985 | 161.43 | 0.8441 | 544.55 | 4.3154 | -0.8064 | 0.0212 | 3.8203 | 4.8047 | -1.2839 | -0.2995 | -0.0527 | 0.0950 | 4 |
| H1-b | Split ring -X | 0.00985 | 161.43 | 0.8441 | 544.55 | -4.3154 | -0.8064 | 0.0212 | -4.8047 | -3.8203 | -1.2839 | -0.2995 | -0.0527 | 0.0950 | 4 |
| H2-a | Jam nut +X (left-hand) | 0.02765 | 453.18 | 0.8508 | 548.91 | 2.6563 | -0.0002 | -0.0001 | 2.5625 | 2.7500 | -0.2790 | 0.2790 | -0.2500 | 0.2500 | 45 |
| H2-b | Jam nut -X (right-hand) | 0.02765 | 453.18 | 0.8508 | 548.91 | -2.6563 | -0.0002 | -0.0001 | -2.7500 | -2.5625 | -0.2790 | 0.2790 | -0.2500 | 0.2500 | 45 |

Note on the T-bolts: they are exact mirror images; the two listed volumes differ by 0.03 % only through the
integration of the thread surfaces. Their centre of mass lies on the shank axis (y = z = 0, from a fine-mesh integral);
a kernel volume integration of the original reports up to 0.025 in off-axis, which is a numerical artefact.

Exact extremes: body x +/-2.5625, r 0.25; clevis x 3.127604 to 4.683594, y +/-0.21875, z +/-0.371094; pin
y -0.427083 to 0.322917; ring x 3.820312 to 4.804688, y -1.283854 to -0.299479, z -0.052731 to 0.095048; nut
y +/-0.279006, z +/-0.25; T-bolt x 0.65625 to 3.502604, y +/-0.15625, z +/-0.322266 (all mirrored on -X).
**Whole assembly:** 11 bodies; total volume 1.35774 in3 (22249.37 mm3); total area 35.7529 in2 (23066.37 mm2); centre of mass (0.0002, -0.0039, 0.0047) in; bounding box
X [-4.804688, 4.804688], Y [-1.283854, 0.322917], Z [-0.371094, 0.371094] in
(mm: X [-122.039, 122.039], Y [-32.610, 8.202], Z [-9.426, 9.426]).

**Key functional checks:** pin centre distance (retracted length) 8.625; body length 5.125; clevis inside width 0.3125;
pin diameter 0.3125; threads 5/16-24, left-hand at +X, right-hand at -X; jam nut 0.5 across flats, 0.1875 thick.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Retracted length | 8.625 | pin centre distance 8.625 | Agree; the model is at the retracted length |
| Extended length 12.375, maximum adjustment 3.75 | drawing | not a modelled pose | Informational, do not model |
| Body length | 5.125 | 5.125 | Agree |
| Clevis inside width, pin diameter | 0.313 (5/16) | 0.3125 | Agree within rounding |
| Thread hands | right-hand at one end, left-hand at the other | left-hand at +X, right-hand at -X | Follow the 3D |
| Body internal threads | 5/16-24 | plain bores 0.3125 | Follow the 3D (not modelled) |
| End fittings "forged" | product data | bent strap of constant thickness 0.0625 | Follow the 3D |

**Undetermined:** forging shapes and draft (not modelled); the body's real thread length (not modelled); thread
tolerance class and clearances (the model has zero clearance).
