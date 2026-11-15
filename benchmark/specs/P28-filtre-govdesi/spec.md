# Design specification: plastic in-line filter housing (head and bowl), tapered pipe ports

Sediment filter housing as supplied: a moulded **head** with an in-line pair of threaded pipe ports, two mounting
bridges, a pressure-relief button and raised lettering, and a ribbed **bowl** below it. This document is the only
source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild
  may work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The housing axis is the Y axis** (x = 0, z = 0); +Y points from the bowl bottom up to the head.
  - **y = 4.3 is the joint plane** between bowl (below) and head (above).
  - **The two ports lie on the line y = 5.06, z = 0, parallel to X**; the port mouths are the faces x = -2.375 and
    x = +2.375.
  - Plane z = 0 is a plane of symmetry of the head except for its lettering and the port threads. The head is also
    symmetric about x = 0 except for the relief button (at -X), the lettering and the threads.
- **Conventions:** rho = distance from the Y axis = sqrt(x^2 + z^2); "(rho, y)" = half-section of a body of revolution
  about the Y axis. Plan angle psi = angle in the XZ plane measured **from +X toward +Z** (psi = 90 deg is +Z).
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description and the source's own simplifications

The **head** (P01) is a disc with a raised rim and a shallow dish, crossed by a trapezoidal bar along X that carries
both ports. Across the bar stand two **mounting bridges** with two holes each. Near the -X end a moulded **relief
button** stands in a round boss. Each end of the bar is a raised block with embossed letters ("IN" at -X, "OUT" at
+X). The **bowl** (P02) is a ribbed cylinder hanging below the head.

**Simplifications that exist in the source model and must be reproduced:**
- **The bowl is a solid** (no cavity, no filter cartridge, no thread to the head, no O-ring). Head and bowl meet face
  to face on y = 4.3.
- **The head has no inner flow path** other than a straight bore that joins the two ports. The relief button is part
  of the head solid (one body).
- Both ports are modelled as tapered helical threads (section 4, "Threads").

## 3. Part list

2 distinct parts, **2 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Head with ports, bridges, relief button | custom | plastic |
| P02 | 1 | Bowl, ribbed, solid | custom | plastic |

## 4. Part geometry

### Threads (both ports of P01)

**Tapered pipe thread, 18 per inch (p = 0.055556), right-hand, internal.** In any half-plane that contains the port
axis the groove is a trapezoid with two straight flanks at 30 deg to the plane normal to the axis (60 deg included),
a flat on the root cone and a flat on the crest cone (each flat parallel to the axis; widths are axial).
- Both cones have the half-angle **1.7833 deg** (radius changes by 0.031135 per unit of depth a; the port is wider at
  the mouth). **Root cone r_r = 0.27000 - 0.031135 a** (diameter 0.540 at the mouth); **crest cone
  r_c = 0.23316 - 0.031135 a**; thread depth 0.03684.
- Root flats 0.00605 wide, crest flats 0.00694 wide.
- **Phase:** for each port a reference half-plane (theta = 0) and the flat centres in it are given; at angle theta (in
  the stated direction) every position moves by + p * theta / 360 deg.
- **+X port:** a = 2.375 - x. theta = 0 toward **+Z**, theta increases toward **+Y**. Root flats centred at
  **a = 0.04469 + n p**, crest flats at **a = 0.07292 + n p** (n = 0, 1, 2, ...). At theta = 90 deg (toward +Y): root
  0.05858, 0.11414, ...
- **-X port:** a = x + 2.375. theta = 0 toward **+Z**, theta increases toward **-Y**. Root flats centred at
  **a = 0.01691 + n p**, crest flats at **a = 0.04514 + n p**. At theta = 90 deg (toward -Y): root 0.03081, 0.08636, ...
- Extent: from the mouth chamfer to the flat port bottom; the groove runs out into both.

### P01 Head (one solid, 195 faces in the original)

Build it as the union of H1 to H6, then cut H7 to H10, then add the lettering H11.

**H1. Plan outline and base.** The head's plan outline is the **circle rho = 2.375 united with the rectangle
|x| <= 2.375, |z| <= 0.747879** (the rectangle adds two small flat-ended "ears" at x = +/-2.375). The base is this
outline from the **bottom face y = 4.3** up to **y = 4.8016**, then:
- the circular part of the top outer edge is rounded **R0.0625** (round centre at rho 2.3125, y 4.7391); the ears
  are not rounded (their sides z = +/-0.747879 and ends x = +/-2.375 are flat up to y = 4.8016);
- a **dish** is sunk inside **rho = 2.25** down to the **floor y = 4.6141** (0.1875 deep), leaving a rim
  rho 2.25 to 2.375 with its top at y = 4.8016.

**H2. Bar along X**, from x = -2.375 to x = +2.375 (flush with the ear ends). Cross-section (z, y), symmetric about
z = 0: the **sloped sides are the planes 0.25882 y + 0.96593 |z| = 1.965142** (15 deg from vertical, normal
(0, 0.25882, +/-0.96593)); they run from the floor (|z| = 0.79819 at y = 4.6141) up to the **bar top y = 5.72**
(|z| = 0.50186). Below y = 4.8016 the bar is limited by the plan outline of H1 (in the ears its sides are the ear
planes |z| = 0.747879; the sloped plane passes exactly through |z| = 0.747879 at y = 4.8016).

**H3. Raised end blocks:** for **2.01875 <= |x| <= 2.375** the bar section continues up to **y = 5.82** (same sloped
sides) with an inner face x = +/-2.01875 that stands 0.1 above the bar top. All edges of the block above the bar top
except those on the outer end face are rounded **R0.0625**: top / inner face (round axis parallel to Z through
x = +/-2.08125, y = 5.7575), top / sloped sides (round axes parallel to X through y = 5.7575, z = +/-0.427042), inner
face / sloped sides (round axes parallel to the slope, i.e. direction (0, 0.96593, -/+0.25882)), with spherical
corners (sphere R0.0625 centred at (+/-2.08125, 5.7575, +/-0.427042)). The outer end face x = +/-2.375 has no rounds.
Flat top y = 5.82 for |x| from 2.08125 to 2.375, |z| <= 0.427042.

**H4. Two mounting bridges**, at x = +0.875 and x = -0.875. Each is a stadium in plan: the rectangle
**|x - x_b| <= 0.21875, |z| <= 0.6875** plus half circles of **radius 0.21875 centred at (x_b, +/-0.6875)**, standing
from the floor y = 4.6141 up to its **flat top y = 5.845**. (Where it rises out of the bar its flat sides x = x_b
+/- 0.21875 are visible; the round ends form posts outside the bar.)

**H5. Relief button boss** at **(x, z) = (-1.51875, 0)**: cylinder **R0.28125** from the bar top y = 5.72 up to
**y = 5.82**, top outer edge rounded **R0.03125** (round centre rho' 0.25, y 5.78875 about the boss axis).

**H6. Relief button pin** on the same axis: a cone of **half-angle 2 deg**, radius **0.21875 at y = 5.47**, tapering
upward to a **flat top at y = 6.18** (radius 0.19396 there).

**H7. Button pocket:** hole **R0.21875** on the button axis from the boss top y = 5.82 down to **y = 5.47**, where it
meets the pin's base circle; the pin stands free in the pocket (the gap widens upward from zero at y = 5.47; there is
no pocket floor face).

**H8. Bridge holes:** four holes **R0.09375** parallel to Y at **(x, z) = (+/-0.875, +/-0.6875)**, from the bridge top
y = 5.845 down to a **sloped bottom that is the bar side plane 0.25882 y + 0.96593 |z| = 1.965142** (so each hole ends
on the extension of the bar's slope: about y = 5.377 on its inner side and y = 4.677 on its outer side).

**H9. Central recess:** cylinder **R0.3125** on the Y axis from the bar top y = 5.72 down to a flat floor
**y = 5.6575** (0.0625 deep).

**H10. Ports and bore** (axis y = 5.06, z = 0):
- each port: mouth chamfer = cone of **half-angle 45 deg**, radius **0.2835 at the end face** x = +/-2.375, narrowing
  inward until it meets the thread; the tapered thread (above); a **flat port bottom at x = +/-1.9732** (0.4018 deep);
- a **through bore R0.2025** from x = -1.9732 to x = +1.9732 joining the two ports.

**H11. Lettering**, raised **0.03125** (vertical walls) from the end-block tops y = 5.82 to **y = 5.85125**. Outlines
in the (x, z) plane:
- **-X end ("IN"):**
  - I: rectangle x from -2.263257 to -2.08125, z from 0.077003 to 0.102671.
  - N: polygon (-2.08125, 0.009334), (-2.08125, 0.035001), (-2.263257, 0.035001), (-2.263257, 0.00789),
    (-2.12742, -0.079336), (-2.263257, -0.079336), (-2.263257, -0.105004), (-2.08125, -0.105004),
    (-2.08125, -0.07787), (-2.21704, 0.009334). (The two slanted edges lie on the lines 0.54034 x + 0.84145 z =
    -1.21629 and = -1.190103.)
- **+X end ("OUT"):**
  - T: crossbar x from 2.130493 to 2.151494, z from -0.260176 to -0.117838; stem x from 2.151494 to 2.3125, z from
    -0.201841 to -0.176173.
  - U: two legs z from -0.089837 to -0.064169 and z from 0.024501 to 0.050169, both from x = 2.130493 to about
    x = 2.235, joined at the +X end by a rounded bow: outer edge a smooth curve through (2.2352, -0.0898),
    (2.2939, -0.0747), (2.3148, -0.0203), (2.2941, 0.0353), (2.2352, 0.0502); inner edge through (2.2340, -0.0642),
    (2.2771, -0.0556), (2.2915, -0.0183), (2.2764, 0.0162), (2.2340, 0.0245).
  - O: a ring; outer edge a smooth closed curve through (2.3148, 0.1692), (2.2883, 0.2320), (2.2239, 0.2555),
    (2.1559, 0.2335), (2.1282, 0.1691), (2.1553, 0.1054), (2.2218, 0.0828), (2.2879, 0.1055); inner edge through
    (2.2938, 0.1693), (2.2729, 0.2146), (2.2242, 0.2298), (2.1712, 0.2162), (2.1492, 0.1689), (2.1714, 0.1229),
    (2.2216, 0.1085), (2.2722, 0.1232). (Close to ellipses: outer semi-axes 0.0933 in x and 0.0864 in z, inner 0.0723
    and 0.0607, centre (2.2215, 0.1691).)

### P02 Bowl (one solid, 86 faces)

**W1. Core, body of revolution about Y.** Half-section (rho, y): top face **y = 4.3** from the axis out to
**rho 2.375**; cylinder rho 2.375 down to **y = 2.7415**; 45 deg cone in to **(2.1875, 2.554)**; flat ring y = 2.554
(facing down) in to **rho 2.1375**; main **cylinder rho 2.1375** down to y = -5.195; bottom edge round **R0.5**
(centre rho 1.6375, y -5.195) to the **bottom face y = -5.695**, flat in to the axis.

**W2. Eight ribs.** Each rib is a flat slab **0.25 thick** (+/-0.125 about a vertical plane through the Y axis),
reaching radially from the axis out to an **outer face at rho' = 2.1875** (0.05 proud of the core cylinder), from
**y = -5.82** (0.125 below the core bottom) up to a flat top at **y = 2.554**. The outer lower corner of each rib is
rounded **R0.5** (round axis normal to the rib plane at 1.6875 from the Y axis, y = -5.32). The rib centre planes are
at plan angles **psi = 0, 90, 180, 270 deg and psi = -10, 80, 170, 260 deg** (two crosses, the second turned
-10 deg about Y, i.e. from +X toward -Z). Below the core (y -5.82 to -5.695) the ribs form a star of eight blades
that meet at the axis.

## 5. Assembly

Both bodies in place, identity placement. The bowl's top face and the head's bottom face are both y = 4.3 (the head
outline overhangs the bowl only at the two ears). **No overlap between the bodies.**

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body,
centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Head | 12.64402 | 207198.39 | 69.4799 | 44825.64 | -0.0080 | 4.8440 | 0.0000 | -2.3750 | 2.3750 | 4.3000 | 6.1800 | -2.3750 | 2.3750 | 195 |
| P02 | Bowl | 149.69833 | 2453116.03 | 177.7309 | 114664.88 | -0.0000 | -0.5389 | 0.0000 | -2.3750 | 2.3750 | -5.8200 | 4.3000 | -2.3750 | 2.3750 | 86 |

**Whole assembly:** 2 bodies; total volume 162.34235 in3 (2660314.42 mm3); total area 247.2108 in2 (159490.51 mm2);
centre of mass (-0.0006, -0.1197, 0.0000) in; bounding box X [-2.375, 2.375], Y [-5.82, 6.18], Z [-2.375, 2.375] in
(mm: X [-60.325, 60.325], Y [-147.828, 156.972], Z [-60.325, 60.325]).

**Key functional checks:** overall height 12.00 (bowl rib bottoms to button top); housing diameter 4.75; ports
18 per inch tapered (root diameter 0.540 at the mouth), mouths 4.75 apart; bridge holes on a 1.75 x 1.375 rectangle.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs. No dimensioned drawing of this part was available; product data
name the ports 1/4 pipe size, which agrees with the modelled thread (18 per inch, 0.540 root diameter at the mouth).

**Undetermined:** the exact free-form outlines of the letters O and U (given as point lists and near-ellipses above);
the run-out of the thread grooves at the mouth chamfers and at the port bottoms; any cartridge, seal or internal
geometry of the bowl (not modelled: the bowl is solid).
