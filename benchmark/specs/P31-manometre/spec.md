# Design specification: rear-stem dial gauge for pressure, 12 bodies

A small dial pressure gauge for boilers as a simplified catalogue model: a solid cylindrical case, a rolled bezel ring, a
domed-edge flat lens, a dial plate with an engraved dual scale, a brass socket with a wrench square and a tapered pipe
thread, a plain stem rod projecting beyond the thread, two pointers, two hub caps and two stop pins. This document is
the only source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **Z is the gauge axis.** The dial faces **+Z**; the socket, thread and stem rod point to **-Z**.
  - **Origin = the centre of the case back face**: the case back boss face (the face the socket seats against) is the
    plane **z = 0**. The case front (top) face is z = 0.82, the bezel front z = 1.02, the socket end z = -2.0, the stem
    rod tip z = -2.96.
  - Every round part (case, bezel, lens, dial outline, socket, stem rod) is coaxial with the Z axis (x = 0, y = 0).
  - The **sub-dial centre** (pressure scale, second pointer) is the point **(0, -0.375)** in XY. The main pointer turns
    about (0, 0).
  - X / Y: the main scale arc lies on the +Y half of the dial; the sub-dial lies on -Y. The wrench square of the socket
    has its four flats normal to +/-X and +/-Y.
- **Half-section convention:** for a body of revolution, "(r, z)" is a point of the half-section in the plane through the
  Z axis (r = distance from the axis >= 0). Revolve the closed profile 360 deg about Z. "Arc R a about (rc, zc)" = the
  **minor** circular arc of radius a about that centre between the two listed points.
- **Plan convention:** "(x, y)" = outline in a plane normal to Z, extruded along Z between the stated z values.
- Angles in the XY plane are measured from +X toward +Y (counter-clockwise seen from +Z).
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description and source simplifications

Dial gauge, 2.5 dial (case) diameter, 2.64 over the bezel, centre back connection with a 1/4 tapered pipe thread
(male), 2.0 from the case back to the end of the socket, with a 0.31 diameter stem rod that projects 0.96 beyond the
thread end. Dual scale: temperature (deg C inner, deg F outer) on the main dial; pressure (psi and feet of water) on the
sub-dial. Product data: painted steel case, brass connection, acrylic lens; dry dial; 0 to 75 psi.

**Simplifications that exist in the source model and must be reproduced:**
- **The case is a solid cylinder** (no movement inside, no hollow). The dial plate lies on its front face.
- The socket has a **blind bore** for the stem rod only (diameter 0.31, 0.4018 deep from the socket end); otherwise it is
  solid (no pressure passage). The stem rod is a plain solid rod with a rounded end.
- The **pipe thread is modelled** as a real helical tapered thread (section 4, P05). The wrench section is a **square
  with rounded corners** (four flats), not a hexagon.
- The **lens skirt overlaps the dial rim** (section 5): reproduce the overlap as it is; do not trim either body.
- The dial graphics (graduations, numerals, text) are **engraved only 0.001 deep** (section 4, P04).
- The stop pin H2-b carries a 0.001 thin sliver cut where one dial numeral crosses it (section 4, H2); it may be ignored.

## 3. Part list

8 distinct custom bodies and 2 distinct small hardware items used twice: **12 bodies in total.**

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Case, 2.5 dia, solid | custom | painted steel |
| P02 | 1 | Bezel ring, rolled sheet | custom | not stated |
| P03 | 1 | Lens with skirt | custom | acrylic |
| P04 | 1 | Dial plate with engraved dual scale | custom | not stated |
| P05 | 1 | Socket: seat flange, wrench square, shank, tapered thread | custom | brass |
| P06 | 1 | Stem rod, 0.31 dia, rounded end | custom | not stated |
| P07 | 1 | Main pointer (about (0, 0)) | custom | not stated |
| P08 | 1 | Sub-dial pointer (about (0, -0.375)) | custom | not stated |
| H1 | 2 | Hub cap (H1-a at (0, 0), H1-b at (0, -0.375)) | hardware | not stated |
| H2 | 2 | Stop pin, 0.05 dia x 0.1 (H2-a, H2-b) | hardware | not stated |

Equivalence groups: H1-a and H1-b are identical (translated copies). H2-a and H2-b are identical cylinders (H2-b also has
the sliver cut noted above).

## 4. Part geometry

### P01 Case (one solid of revolution, 11 faces)

Half-section, closed profile, going round counter-clockwise from the axis on the back boss:
1. (0, 0) to (0.4356, 0) - back boss face z = 0.
2. Arc R0.03 about (0.4356, 0.03) from (0.4356, 0) to (0.46158, 0.015) (convex), then arc R0.03 about (0.48756, 0) from
   (0.46158, 0.015) to (0.48756, 0.03) (concave): an S-shaped (ogee) boss edge, the two arcs tangent at (0.46158, 0.015).
3. (0.48756, 0.03) to (1.2, 0.03) - the case back face z = 0.03 (the boss stands 0.03 proud of it).
4. Arc R0.05 about (1.2, 0.08) from (1.2, 0.03) to (1.25, 0.08) - back edge round.
5. (1.25, 0.08) to (1.25, 0.82) - case wall, **diameter 2.5**.
6. (1.25, 0.82) to (0, 0.82) - front face z = 0.82 (flat, full disc).

### P02 Bezel ring (one solid of revolution, 30 faces)

A rolled sheet ring about 0.01 thick that hugs the case rim and turns in over the lens edge. Half-section, closed
profile (all centres exact; arcs are minor arcs):
1. (1.25, 0.76827) to (1.25945, 0.765) - straight (bottom edge of the sheet; inner corner on the case wall radius).
2. Arc R0.38554 about (1.62385, 0.63910) from (1.25945, 0.765) to (1.30445, 0.85502) (outer face, convex outward, mid
   point (1.27900, 0.81148)).
3. Arc R0.09063 about (1.22937, 0.90578) from (1.30445, 0.85502) to (1.30942, 0.94828) (outer bulge, mid point
   (1.31987, 0.90096); maximum radius 1.32 at z = 0.90578, so the outside **diameter is 2.64**).
4. Arc R0.015 about (1.29617, 0.94125) from (1.30942, 0.94828) to (1.29617, 0.95625).
5. Arc R0.015 about (1.29617, 0.97125) from (1.29617, 0.95625) to (1.28735, 0.95912) (concave).
6. Straight line (cone, 54.0 deg half angle) from (1.28735, 0.95912) to (1.20751, 1.01713).
7. Arc R0.015 about (1.19869, 1.005) from (1.20751, 1.01713) to (1.19869, 1.02).
8. (1.19869, 1.02) to (1.1, 1.02) - front face z = 1.02 (annulus, **inner diameter 2.2**).
9. (1.1, 1.02) to (1.1, 1.01) - inner edge (cylinder R1.1, 0.01 high).
10. (1.1, 1.01) to (1.19869, 1.01) - underside of the lip z = 1.01.
11. Arc R0.005 about (1.19869, 1.005) from (1.19869, 1.01) to (1.20163, 1.00904).
12. Straight line (cone) from (1.20163, 1.00904) to (1.28147, 0.95103) (parallel to 6, 0.01 inside).
13. Arc R0.025 about (1.29617, 0.97125) from (1.28147, 0.95103) to (1.29617, 0.94625).
14. Arc R0.005 about (1.29617, 0.94125) from (1.29617, 0.94625) to (1.30058, 0.94359).
15. Arc R0.08063 about (1.22937, 0.90578) from (1.30058, 0.94359) to (1.29617, 0.86062) (inner face of the bulge, mid
    point (1.30989, 0.90149)).
16. Arc R0.39554 about (1.62385, 0.63910) from (1.29617, 0.86062) to (1.25, 0.76827) (inner face, mid point
    (1.27006, 0.81596)); closes the profile.

The bezel spans z = 0.765 to 1.02; it touches the case wall only along the circle r = 1.25, z = 0.76827 and does not
overlap the case, the lens or the dial.

### P03 Lens (one solid of revolution with a shallow marker recess, 14 faces)

An inverted shallow cup: a flat plate 0.05 thick with a skirt hanging down to the dial. Half-section, closed profile:
1. (0, 0.959) to (1.17592, 0.959) - underside of the plate z = 0.959.
2. Arc R0.02408 about (1.17592, 0.93492) from (1.17592, 0.959) to (1.2, 0.93492) (inner corner round).
3. (1.2, 0.93492) to (1.2, 0.821) - inside of the skirt, **diameter 2.4**.
4. (1.2, 0.821) to (1.25, 0.821) - skirt bottom z = 0.821 (0.05 wide).
5. (1.25, 0.821) to (1.25, 0.93492) - outside of the skirt, **diameter 2.5**.
6. Arc R0.07408 about (1.17592, 0.93492) from (1.25, 0.93492) to (1.17592, 1.009) (outer edge round, quarter circle).
7. (1.17592, 1.009) to (0, 1.009) - front face z = 1.009.

**Marker recess:** a triangular recess 0.001 deep in the front face: floor z = 1.008, vertical walls, outline with
corners (0.82653, 0.17569), (1.16209, 0.24701), (1.10788, 0.42901); the side between the last two corners is the arc of
radius 1.18805 about the Z axis (where the floor plane meets the edge round). Straight sides: (1.10788, 0.42901) to
(0.82653, 0.17569) and (0.82653, 0.17569) to (1.16209, 0.24701).

### P04 Dial plate (one solid, 1690 faces in the original because of the engraving)

**Plate:** disc **diameter 2.5** about the Z axis from **z = 0.82 to z = 0.84** (0.02 thick), sharp edges.
**Four through holes** (z = 0.82 to 0.84):
- diameter 0.08 (R0.04) at (0, 0) and at (0, -0.375) (the two pointer hubs);
- diameter 0.05 (R0.025) at (-0.3375, -0.375) and at (0.33237, -0.43361) (the stop pins: both lie on the circle of radius
  0.3375 about the sub-dial centre (0, -0.375), at 180 deg and at -10 deg).

**Engraving (all graphics are recesses 0.001 deep: floor z = 0.839, vertical walls).** A plain plate without the
engraving deviates by only 0.001 (0.0254 mm) from the original surface; its volume is 0.25 percent larger (the engraving
removes about 3.97 mm3) and its area about 0.5 percent smaller. Reproduce the graphics as far as practical; their exact
glyph shapes are not given here (see section 7). What is modelled:
- **Main (temperature) scale about (0, 0), upper half (about -0.8 deg through 90 deg to 180.8 deg):** two concentric
  engraved arc lines 0.01 wide, the inner one between radii **0.73007 and 0.74007**, the outer one between **0.76007 and
  0.77007** (the 0.02 band between them is not engraved). Inner graduations (deg C, 20 to 160 in steps of 2: **71 marks,
  2.571 deg apart**, the first and last at 0 and 180 deg) run inward from the inner line, the longest (major) marks
  reaching radius about 0.665. Outer graduations (deg F, 70 to 320 in steps of 5: about 51 marks) run outward from the
  outer line, the longest reaching radius about 0.839. Numerals 20 ... 160 (every 20) stand inside the scale between
  radius about 0.50 and 0.65; numerals 70, 120, 170, 220, 270, 320 stand outside, radially, between radius 0.82 and
  0.89. The labels "deg C" and "deg F" (with degree signs) lie below the right end near (0.61, -0.09) and (0.78, -0.11).
- **Sub-dial (pressure) scale about (0, -0.375), lower side (about -170 deg through -90 deg to -10 deg):** two engraved
  arc lines 0.01 wide between radii **0.43018 and 0.44018** and between **0.46017 and 0.47017**. Inner graduations (psi,
  0 to 75 every 5: 16 marks) run inward to radius about 0.406; outer graduations (feet of water, 0 to 170 every 10:
  about 18 marks) outward to about 0.493. Numerals 0, 20, 40, 60, 75 inside and 50, 100, 150, 170 outside; the word
  "PRESSURE" centred near (0.0, -1.0) (letters between y = -1.035 and -0.96); the text "feet H2O psi" (subscript 2) at
  x = -0.975 to -0.595, y = -0.396 to -0.294.
- Total engraved floor area 0.2435 in2 (engraved volume 3.99 mm3).

### P05 Socket (one solid, 46 faces)

Built from these zones along Z (all about the Z axis):
1. **Seat flange:** cylinder **diameter 0.81 (R0.405)** from z = -0.03 to **z = 0** (its +Z face is flat and seats on
   the case boss).
2. **Neck:** cylinder **diameter 0.54 (R0.27)** from z = -0.08 to z = -0.03.
3. **Wrench square (z = -0.30 to -0.08):** the solid of revolution with half-section (0.27, -0.08) - (0.324, -0.11118)
   [60 deg chamfer, i.e. the line makes 60 deg with the axis] - (0.324, -0.26882) - (0.27, -0.30), intersected with the
   square prism **|x| <= 0.28, |y| <= 0.28** (four flats **0.56 across**, normal to X and Y). The corners of the square are
   therefore the cylinder R0.324 (0.648 across the corners) with 60 deg chamfers at both ends; the flats run from
   z = -0.29423 to -0.08577 at the middle of each flat (where the chamfer cones cut them they end in hyperbolic arcs).
4. **Shank:** cylinder **diameter 0.54 (R0.27)** from z = -1.5982 to z = -0.30.
5. **Threaded zone z = -2.0 to -1.5982** (tapered pipe thread, see below).
6. **Blind bore:** diameter **0.31 (R0.155)** from the end face z = -2.0 up to a flat bottom at **z = -1.5982**
   (0.4018 deep). The end face z = -2.0 is the annulus from R0.155 to R0.2144.

**Tapered thread (modelled, right-hand, 18 threads per inch, pitch P = 1/18 = 0.055556):**
- **Crest cone:** radius **r_c(z) = 0.27 - 0.03113 (-1.5982 - z)** (half angle 1.783 deg, taper about 1 : 16 on the
  diameter); r_c = 0.27 at z = -1.5982, 0.25750 at z = -2.0. The crests are narrow flats on this cone.
- **Root cone:** r_root(z) = r_c(z) - 0.03688 (root radius 0.22219 at z = -1.94918; 0.23085 at z = -1.67118).
- **Thread form** in any half-section through the axis, per pitch: crest flat 0.0061 long (along the axis), flank
  0.0213, root flat 0.0070, flank 0.0213; the flanks make **30 deg with the radial direction** (60 deg included angle,
  symmetric about the plane normal to the axis).
- **Phase:** in the half-plane at angle 0 (the +X side, y = 0, x > 0) the crest flats are centred at
  **z = -1.92093 + k P** (k = 0, 1, ..., 5; crest flat from -1.92398 to -1.91790 for k = 0), and the root flats at
  z = -1.94918 + k P. Right-hand: at angle theta (deg) the same features lie **theta / 360 x P higher** (e.g. at 90 deg the
  crest is centred at z = -1.90704).
- **End of the threaded zone at z = -2.0:** 45 deg end chamfer: the material lies inside the cone r = 0.2144 + (z + 2.0)
  (from R0.2144 at z = -2.0 up to the crest cone at about z = -1.9555 / -1.9671).
- **Run-out at the top:** the groove is cut only outside the 45 deg cone r = 0.27 + (z + 1.5982) (r = 0.27 at z = -1.5982,
  narrowing downward); where the groove would go deeper than this cone the cone surface remains. The groove therefore
  fades out between z = -1.6364 and z = -1.5982, and the shank R0.27 continues above z = -1.5982.
- In the original the flanks and the root are free-form surfaces and the crest strips are cone patches; describe them in
  any way that gives the same shape.

### P06 Stem rod (one solid of revolution, 7 faces)

Half-section: (0, -1.5982) - (0.155, -1.5982) - (0.155, -2.84330) [cylinder **diameter 0.31**] - arc R0.07092 about
(0.08408, -2.84330) to (0.14365, -2.88179) - arc R0.17102 about (0, -2.78898) to (0, -2.96) [spherical end]. The two arcs
are tangent to each other and to the cylinder. Its top face z = -1.5982 meets the bottom of the socket bore; the rod fills
the bore and projects **0.96 beyond the socket end** (tip z = -2.96).

### P07 Main pointer (flat plate, z = 0.87 to 0.88, 0.01 thick, 9 faces)

Plan outline (extrude z = 0.87 to 0.88):
- Hub: arc R0.115 about (0, 0) from (-0.11325, -0.01997) the long way round through (0.115, 0) to (-0.10806, 0.03933).
- Straight edge from (-0.10806, 0.03933) to (-0.89630, 0.08343).
- Tip: arc R0.005 about (-0.89658, 0.07844) from (-0.89630, 0.08343) round the outside through (-0.90158, 0.07844) to
  (-0.89717, 0.07348) (tip centre at radius 0.9 and angle 175 deg; the two straight edges are tangent to this circle and
  lie 0.0332 from (0, 0)).
- Straight edge from (-0.89717, 0.07348) back to (-0.11325, -0.01997).
- Hole: circle R0.04 (diameter 0.08) about (0, 0), through.

### P08 Sub-dial pointer (flat plate, z = 0.87 to 0.88, 10 faces)

Plan outline (extrude z = 0.87 to 0.88), hub centre (0, -0.375):
- Hub: arc R0.115 about (0, -0.375) from (0.11486, -0.38058) the long way round through (0, -0.26) and (-0.115, -0.375)
  to (0.09668, -0.43727).
- Straight edge from (0.09668, -0.43727) to (0.68427, -0.59972).
- Tip: arc R0.005 about (0.68560, -0.59490) from (0.68427, -0.59972) round the outside to (0.68732, -0.59020) (tip
  centre at distance 0.72 from the hub centre, angle -17.78 deg).
- Straight edge from (0.68732, -0.59020) back to (0.11486, -0.38058).
- Hole: circle R0.04 (diameter 0.08) about (0, -0.375), through.

### H1 Hub cap (2 identical bodies of revolution, 12 faces each)

Half-section about its own axis (H1-a: (0, 0); H1-b: (0, -0.375)): (0, 0.82) - (0.04, 0.82) - (0.04, 0.88) [pin
**diameter 0.08** through the dial and the pointer hole] - (0.1, 0.88) - (0.1, 0.8925) [cap **diameter 0.2**] -
(0.0925, 0.9) [45 deg chamfer 0.0075] - (0.015, 0.9) - (0.015, 0.88) - (0, 0.88): the cap has a central blind hole
**diameter 0.03, 0.02 deep** from its top z = 0.9. The pin stands on the case front face (z = 0.82) and fills the dial and
pointer holes exactly.

### H2 Stop pin (2 identical cylinders, 4 faces; H2-b 11 faces)

Cylinder **diameter 0.05 (R0.025)**, from **z = 0.82 to z = 0.92**, through the dial holes. H2-a axis (-0.3375, -0.375);
H2-b axis (0.33237, -0.43361) (radius 0.3375 about the sub-dial centre at 180 deg and at -10 deg).
H2-b only: a 0.001 thick sliver (z = 0.839 to 0.840) is cut into its side by the engraving of one sub-dial numeral; it
removes 0.007 mm3 (it adds 0.54 mm2, 4 percent, to the pin area) and may be left out.

## 5. Assembly

- Stack along Z: socket flange (z = -0.03 to 0) on the case back boss (z = 0); case to z = 0.82; dial plate z = 0.82 to
  0.84; pointers z = 0.87 to 0.88 on the hub pins; hub caps to z = 0.9; stop pins to z = 0.92; lens z = 0.821 to 1.009;
  bezel z = 0.765 to 1.02 (the bezel lip underside z = 1.01 is 0.001 above the lens front face).
- **Interference in the source (reproduce it):** the lens skirt (r = 1.2 to 1.25, from z = 0.821) overlaps the dial plate
  rim (r = 1.2 to 1.25, up to z = 0.84): ring 0.05 wide x 0.019 high, **119.82 mm3**. All other contacts are face
  contacts with zero overlap volume (checked pairwise).
- The stem rod sits in the socket bore (contact only).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (small
hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-a | Hub cap at (0, 0) | 0.00090 | 14.72 | 0.0895 | 57.76 | 0.0000 | 0.0000 | 0.8764 | -0.1000 | 0.1000 | -0.1000 | 0.1000 | 0.8200 | 0.9000 | 12 |
| H1-b | Hub cap at (0, -0.375) | 0.00090 | 14.72 | 0.0895 | 57.76 | 0.0000 | -0.3750 | 0.8764 | -0.1000 | 0.1000 | -0.4750 | -0.2750 | 0.8200 | 0.9000 | 12 |
| H2-a | Stop pin at (-0.3375, -0.375) | 0.00020 | 3.22 | 0.0196 | 12.67 | -0.3375 | -0.3750 | 0.8700 | -0.3625 | -0.3125 | -0.4000 | -0.3500 | 0.8200 | 0.9200 | 4 |
| H2-b | Stop pin at (0.33237, -0.43361) | 0.00020 | 3.21 | 0.0205 | 13.21 | 0.3324 | -0.4336 | 0.8701 | 0.3074 | 0.3574 | -0.4586 | -0.4086 | 0.8200 | 0.9200 | 11 |
| P01 | Case | 3.89382 | 63808.22 | 15.8840 | 10247.71 | -0.0000 | 0.0000 | 0.4233 | -1.2500 | 1.2500 | -1.2500 | 1.2500 | 0.0000 | 0.8200 | 11 |
| P02 | Bezel ring | 0.03305 | 541.63 | 6.7587 | 4360.42 | -0.0000 | 0.0000 | 0.9279 | -1.3200 | 1.3200 | -1.3200 | 1.3200 | 0.7650 | 1.0200 | 30 |
| P03 | Lens | 0.29032 | 4757.49 | 12.0049 | 7745.06 | -0.0001 | -0.0000 | 0.9664 | -1.2500 | 1.2500 | -1.2500 | 1.2500 | 0.8210 | 1.0090 | 14 |
| P04 | Dial plate | 0.09765 | 1600.23 | 10.0145 | 6460.98 | 0.0001 | 0.0006 | 0.8300 | -1.2500 | 1.2500 | -1.2500 | 1.2500 | 0.8200 | 0.8400 | 1690 |
| P05 | Socket with threaded shank | 0.43215 | 7081.71 | 5.2668 | 3397.94 | -0.0000 | 0.0001 | -0.8708 | -0.4050 | 0.4050 | -0.4050 | 0.4050 | -2.0000 | 0.0000 | 46 |
| P06 | Stem rod | 0.09953 | 1631.05 | 1.4108 | 910.17 | 0.0000 | 0.0000 | -2.2579 | -0.1550 | 0.1550 | -0.1550 | 0.1550 | -2.9600 | -1.5982 | 7 |
| P07 | Main pointer | 0.00064 | 10.46 | 0.1527 | 98.54 | -0.1766 | 0.0154 | 0.8750 | -0.9016 | 0.1150 | -0.1150 | 0.1150 | 0.8700 | 0.8800 | 9 |
| P08 | Sub-dial pointer | 0.00058 | 9.43 | 0.1366 | 88.15 | 0.1204 | -0.4136 | 0.8750 | -0.1150 | 0.6906 | -0.5999 | -0.2600 | 0.8700 | 0.8800 | 10 |

**Whole assembly:** 12 bodies; total volume 4.84993 in3 (79476.10 mm3); total area 51.8482 in2 (33450.38 mm2); centre of
mass (0.0000, -0.0001, 0.2974) in; bounding box X [-1.32, 1.32], Y [-1.32, 1.32], Z [-2.96, 1.02] in (mm: X [-33.528,
33.528], Y [-33.528, 33.528], Z [-75.184, 25.908]).

**Key functional checks:** bezel diameter 2.64; case diameter 2.5; case back to bezel front 1.02; case back to socket end
2.0; stem rod diameter 0.31 projecting 0.96 beyond the socket end; thread 1/4 tapered pipe thread, 18 per inch,
outside diameter 0.54 at the top of the thread.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs. The catalogue drawing agrees with the model on every printed dimension
(2.64, 1.02, 2.00, 0.96, 0.31, 1/4 NPT). The drawing shows the wrench section as a hexagon; the model has a square with
four flats 0.56 across (follow the model). The product data's "1 in stem length" is not a single model dimension (the
rod projects 0.96 beyond the socket end; the threaded zone is 0.4018 long).

**Undetermined (not given or not in the source model):** the exact glyph outlines of the engraved numerals and text on
the dial (font, exact positions to better than about 0.01) and the exact lengths and widths of the individual graduation
marks; the case interior, the Bourdon tube and movement; a pressure passage through the socket and the rod; the colour
of the dial graphics; which scale the main pointer reads (it points at 175 deg, near the deg C 20 end of the scale).
