# Design specification: bimetal dial thermometer, 3 in dial, side (back-left) threaded connection, 1/4 in stem 4 in long

A direct-reading dial thermometer for mounting in tight spaces: a round stainless case with a rolled bezel and a glass
lens, a 1/2 in taper pipe thread spigot with a hex on the left side of the case back, and a 1/4 in stem that runs out to
the left, parallel to the dial. The dial carries 100 raised scale marks, the texts "-40", "°F" and "160", and a needle
pointer on a hub. A small slotted calibration screw head sits on the case back. This document is the only source for
the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** The source is built in round millimetres (for example dial face z 28.5, case radius 41.3);
  the few inch-based sizes (stem diameter 6.35 = 1/4 in, thread pitch 25.4/14) are given in mm with the inch value in
  brackets. Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - **The dial axis is the Z axis** (x = 0, y = 0). The dial looks toward **+Z**; the lens front is at z = 36.5 (bezel
    top), the case back at z = 13.5.
  - **The stem axis is the X axis** (y = 0, z = 0). The stem, thread and hex lie on the **-X side**; the stem tip is at
    x = -142.9.
  - **+Y is "12 o'clock" on the dial**: the scale is symmetric about the YZ plane, its gap (with the texts) is at -Y.
  - Origin: intersection of the two axes (it lies inside the boss under the case back).
- Azimuth around the X axis (used for the thread) is written **az**, measured **from +Z toward +Y** (az 0 = +Z,
  az 90 = +Y, az 180 = -Z, az 270 = -Y). Polar angle in the dial plane is written **θ**, measured from +X toward +Y.

## 2. Product description and source simplifications

The case (one solid with the boss, the neck, the hex, the threaded spigot, the stem, the dial face and the pointer) is
P01. The glass lens P02 is a plain disc in the bezel bore. P03 is the head of the external calibration screw, a small
disc with a cross recess, lying on the case back.

**Simplifications that exist in the source model and must be reproduced:**
- The case is **solid**: no internal cavity, no bimetal coil, no movement. The dial face is a flat plane of P01 at
  z = 28.5; the scale marks and the texts are **raised 0.01** on it (part of P01). The pointer and its hub are part of
  P01 too.
- The pipe thread **is modelled** as a single helical groove of a 60 degree profile cut into the taper (section 4.3).
- The calibration screw head P03 is a separate disc that only touches the case back; there is no hole in the case
  under it and no screw shank.
- The lens is a plain disc; its edge touches the bezel bore exactly (same radius).
- The source lens carries 132 zero-area (degenerate) planar faces in the file; they are not geometry. Model a plain
  4-face disc.
- No hex-socket, no gasket, no lens retaining ring.

Product data (for information): case, stem and spigot stainless steel; lens glass; range -40 to 160 °F.

## 3. Part list

3 distinct parts, **3 bodies in total**. No hardware.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Case with boss, neck, hex, threaded spigot, stem, dial face, scale and pointer | custom | stainless steel |
| P02 | 1 | Lens | custom | glass |
| P03 | 1 | Calibration screw head | custom | undetermined |

## 4. Part geometry

### P01 Case, stem, dial and pointer (one solid, 687 faces in the original)

P01 is the union of: 4.1 a body of revolution about Z (boss, back, case wall, bezel, dial face), 4.2 a body of
revolution about X (neck, shoulder, threaded spigot blank, stem) plus the hex, 4.3 the thread groove cut into the spigot,
4.4 the neck to boss blend, 4.5 the pointer, 4.6 the scale marks, 4.7 the texts.

**4.1 Body of revolution about Z.** Closed half-section in the half-plane y = 0, x ≥ 0, given as (r, z) with r = x,
going round from the axis at the bottom. "Arc c(...)" gives the arc centre; every arc is the short arc between its end
points.
1. (0, -11.1) to (7.673, -11.1): boss bottom face.
2. Line to (8.673, -10.1): **1 x 45 deg chamfer**.
3. Line to (8.673, 12.0): **boss cylinder diameter 17.346**.
4. Arc R1.5 c(10.173, 12.0) to (10.173, 13.5): concave blend boss to back.
5. Line to (31.5402, 13.5): **case back plane z = 13.5**.
6. Arc R1.5 c(31.5402, 15.0) to (33.0401, 14.9867): convex round.
7. Arc R2.5 c(35.54, 14.9645) to (33.7722, 16.7322): concave cove.
8. Line to (34.1007, 17.0607): 45 deg cone.
9. Arc R1.5 c(35.1613, 16.0) to (35.1613, 17.5): convex round.
10. Line to (36.322, 17.5): step face (plane z = 17.5, facing -Z).
11. Arc R2.5 c(36.322, 20.0) to (38.822, 20.0): concave.
12. Line to (38.822, 27.5): **case wall cylinder diameter 77.644**.
13. Arc R2.5 c(38.8, 30.0) to (41.3, 30.0): bezel lower round (the source centre is at z 29.9999).
14. Line to (41.3, 34.0): **bezel cylinder diameter 82.6** (the largest diameter).
15. Arc R2.5 c(38.8, 34.0) to (38.8, 36.5): bezel outer round.
16. Line to (37.605, 36.5): **bezel top plane z = 36.5**.
17. Arc R2.5 c(37.605, 34.0) to (35.105, 34.0): bezel inner round (convex).
18. Line to (35.105, 28.5): **bezel bore diameter 70.21**.
19. Line to (0, 28.5): **dial face plane z = 28.5**; back along the axis to the start.

**4.2 Body of revolution about X** (with the hex). Closed half-section in the half-plane y = 0, z ≥ 0, given as
(x, r) with r = z, from the stem tip:
1. (-142.9, 0) to (-142.9, 1.675): stem tip face.
2. Arc R1.5 c(-141.4, 1.675) to (-141.4, 3.175): tip round.
3. Line to (-58.675, 3.175): **stem cylinder diameter 6.35 (1/4 in)**.
4. Arc R1.5 c(-58.675, 4.675) to (-57.175, 4.675): concave blend stem to spigot end face.
5. Line to (-57.175, 8.768608): **spigot end face x = -57.175**.
6. Line to (-55.81495, 10.21607): **end chamfer cone, 46.7833 deg half-angle** (45 deg to the taper line).
7. Line to (-44.51669, 10.567848): **thread crest cone (the taper)**, r = 10.668 + 0.0311351 (x + 41.3), half-angle
   **1.783333 deg** (1 deg 47 min); diameter 21.336 (0.840 in) at x = -41.3 if extended.
8. Line to (-43.11429, 9.250138): **thread run-out cone, 43.2167 deg half-angle** (45 deg to the taper line).
9. Line to (-41.3, 9.306631): **relief**, a cone of the same 1.783333 deg taper, 1.81429 long (one pitch).
10. Line to (-41.3, 10.668): face x = -41.3 of the hex (annulus).
11. The hex occupies x -41.3 to -30.5652 (see below); under it the solid continues at any radius ≤ 9.3, then:
12. (-30.5652, 9.516045) to (-29.5652, 9.516045): **collar cylinder diameter 19.03209**, 1.0 long.
13. Line to (-28.97846, 8.929305): 45 deg chamfer.
14. Line to (-28.97846, 8.342565): shoulder plane x = -28.97846.
15. Line to (-28.3917, 8.02252): cone 28.6105 deg half-angle (tan = 6/11).
16. Line to the boss: **neck cylinder diameter 16.04504** (r 8.02252) up to the boss (it may run to x = 0; the part
    inside the boss does not show).

**Hex:** a regular hexagonal prism on the X axis from x = **-41.3 to -30.5652** (length 10.7348), **across flats 22.23
(0.875 in)**, across corners 25.669 (corner radius 12.8345). Two flats are horizontal (normals ±Y; planes y = ±11.115);
the other four have normals at ±60 deg from +Y; the **corners point to ±Z**. Both ends carry a **30 deg chamfer**: the
hex is intersected with two cones of 60 deg half-angle about X: one through (x -41.3, r 10.668) widening toward +X (it
reaches the corners at x = -40.0492), one through (x -30.5652, r 9.516045) widening toward -X (corners at
x = -32.4811). The end at x = -30.5652 has no flat face: the cone runs straight into the collar cylinder.

**4.3 Thread groove** (single start, **right-hand**, **pitch 1.814286 = 25.4/14 (14 per inch)**, 1/2 in taper pipe
thread). Cut one helical groove into 4.2 along the spigot. In every half-plane containing the X axis the groove section
is the same trapezoid:
- **Root flat**: a segment **parallel to the axis, 0.2268 long** (axial), at radius r_root.
- **Flanks**: straight, at **30 deg to the plane normal to the axis** (60 deg included), running outward from the root
  flat ends through the crest cone (make them long enough, at least 2.5 radially, to clear the material).
- **Helix**: the root-flat centre follows a right-hand conical helix about X: at **az 0 (+Z) one root-flat centre is at
  x = -55.2473, r_root = 9.0800**; turning by az moves it to x = -55.2473 - (az/360)·1.814286 (+ n·1.814286), and the
  radius follows the taper: **r_root = 9.0800 + 0.0311351 (x + 55.2473)**. Examples of root flats (x from .. to, r):
  az 0: -55.3607..-55.1339 (9.0800), -53.5464..-53.3196 (9.1362); az 90: -55.8143..-55.5875 (9.0658); az 180:
  -56.2679..-56.0411 (9.0514), -54.4536..-54.2268 (9.1076); az 270: -54.9071..-54.6804 (9.0938). The thread rises
  toward +X when turning from +Z toward -Y.
- Resulting crest flat on the crest cone: about 0.2544 long axially; thread depth from the crest cone about 1.154.
- **Extent:** start the groove beyond the free end (it leaves the material through the 46.78 deg end chamfer; the root
  lies above the end face edge r 8.768608, so the end face keeps a full circle). **Stop it with the root-flat centre at
  x = -43.0** (any az): the groove leaves the material through the 43.22 deg run-out cone near x = -43.3, passes over
  the relief (r ≤ 9.31, below the root) without touching it, and must not reach the hex face x = -41.3.

**4.4 Neck to boss blend:** **R1.5** rolling round on the intersection edge of the neck cylinder (diameter 16.04504,
axis X) with the boss cylinder (diameter 17.346, axis Z); concave. In the plane y = 0 it runs from (x -10.173,
z ±8.02252) to (x -8.673, z ±9.5225).

**4.5 Pointer** (part of P01, on the dial face):
- **Hub**: cylinder diameter 6.0 on the Z axis from z = 28.5 to 30.0 (top face z = 30), **except the slice z 29.0 to
  29.5**, where only the pointer plate exists (the hub is two discs 0.5 thick, 28.5 to 29.0 and 29.5 to 30.0).
- **Pointer plate**: thickness 0.5 (z 29.0 to 29.5), outline the triangle **T (3.3410, 27.2100)**, **A (0.3074,
  -13.9078)**, **B (-3.6628, -13.4203)**. It is isosceles, its axis passes through the dial centre and points at **7.0
  deg from +Y toward +X** (θ = 83 deg); tip 27.414 from the centre; tail edge AB 4.000 long, 13.767 behind the centre.
- The plate, the two hub discs and the dial face are one solid.

**4.6 Scale marks:** **100 rectangular marks**, raised **0.01** above the dial face (z 28.5 to 28.51), each **0.25
wide**, running radially from **r 28.910 to r 32.214** (length 3.304), centred on the radial line at
**θ_k = -50 + k·(280/99) deg, k = 0..99** (first mark at θ = -50, last at θ = 230; pitch 2.828283 deg; the 280 deg
scale is symmetric about +Y and open at -Y). Mark long sides are parallel to the radial line.

**4.7 Texts** (raised 0.01, z 28.5 to 28.51, upright, read from +Z with +Y up; plain sans-serif):
- **"-40"**: minus sign = rectangle x -16.9868..-16.0253, y -21.313..-21.0566; "4" in the box x -15.833..-14.1343,
  y -22.1463..-19.5822; "0" (a closed ring) in the box x -13.9099..-12.2112, y -22.2104..-19.5822.
- **"°"**: ring, outer box x -2.2885..-0.8654, y -22.2177..-20.8331, inner box x -2.0192..-1.1346, y -21.9869..-21.0638
  (centre about (-1.577, -21.525)).
- **"F"**: polygon (0.7885, -23.91), (1.0577, -23.91), (1.0577, -22.4485), (2.25, -22.4485), (2.25, -22.1408),
  (1.0577, -22.1408), (1.0577, -21.2177), (2.25, -21.2177), (2.25, -20.91), (0.7885, -20.91).
- **"160"**: "1" in the box x 12.1791..12.7881, y -22.1463..-19.6463; "6" in the box x 13.8458..15.3843,
  y -22.2104..-19.5822; "0" in the box x 15.6407..17.3394, y -22.2104..-19.5822.
- The exact glyph outlines (other than the minus sign and the F) are undetermined; any font filling these boxes. Their
  volume (about 0.08 mm3 in all) and area are negligible.

### P02 Lens (one solid, 4 faces)

Disc **diameter 70.21** (r 35.105) on the Z axis, **z = 31.0 to 34.0** (thickness 3.0). Its rim lies on the bezel bore
of P01 (same radius); its front face is 2.5 below the bezel top; its back face is 1.0 above the hub top.

### P03 Calibration screw head (one solid, 17 faces)

Disc **diameter 4.5** on a vertical axis at **(x 20.0, y 0)**, **z = 12.5 to 13.5** (thickness 1.0; its top face lies
on the case back z = 13.5). Cut through it a **cross recess**: two slots **0.4 wide**, one along X and one along Y,
crossing at the disc centre, each with **full round ends R0.2 whose centres are 1.25 from the disc centre** (slot length
2.9 overall); through the full thickness.

## 5. Assembly

- P02 sits in the bezel bore of P01, rim on the bore cylinder (face contact), lens back face z 31.0 free (1.0 above the
  hub top z 30.0, 2.5 above the dial face).
- P03 touches the case back z = 13.5 with its top face (face contact) at x = 20, y = 0, inside the back face annulus
  (r 10.173 to 31.5402).
- **No overlap** between any two bodies in the original (all pairs: zero common volume).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (P03 2
percent), centre of mass within 0.05 mm, bounding box within 0.05 mm. Volumes in cm3 and mm3, areas in cm2 and mm2, all
coordinates in mm. The faces column is information only.

| ID | Name | Vol cm3 | Vol mm3 | Area cm2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Case, stem, dial and pointer | 99.74986 | 99749.86 | 237.3113 | 23731.13 | -7.5803 | -0.0002 | 17.9347 | -142.9000 | 41.3000 | -41.3000 | 41.3000 | -12.8345 | 36.5000 | 687 |
| P02 | Lens | 11.61473 | 11614.73 | 84.0487 | 8404.87 | 0.0000 | 0.0000 | 32.5000 | -35.1050 | 35.1050 | -35.1050 | 35.1050 | 31.0000 | 34.0000 | 4 |
| P03 | Calibration screw head | 0.01381 | 13.81 | 0.5268 | 52.68 | 20.0000 | 0.0000 | 13.0000 | 17.7500 | 22.2500 | -2.2500 | 2.2500 | 12.5000 | 13.5000 | 17 |

Exact extremes: P01 X -142.9 (stem tip) to 41.3 (bezel), Y ±41.3, Z -12.8345 (hex corner) to 36.5 (bezel top).
**Whole assembly:** 3 bodies; total volume 111378.40 mm3; total area 32188.67 mm2; centre of mass (-6.7864, -0.0002,
19.4530); bounding box X [-142.9, 41.3], Y [-41.3, 41.3], Z [-12.8345, 36.5].

**Key functional checks:** overall length 184.2 (7.25 in) from the stem tip to the bezel; stem tip to hex face
x = -41.3: 101.6 (4.0 in); bezel diameter 82.6 (3.25 in); boss bottom to bezel top 47.6 (1.87 in); hex 22.23 across
flats (0.875 in); stem diameter 6.35 (0.25 in); thread 14 per inch on a 1.7833 deg taper.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall length | 7.25 in (drawing), 7 1/2 in (product data) | 184.2 = 7.252 in | Follow the 3D (agrees with the drawing). |
| Dial diameter | 3 in (product data), 3.25 in (drawing, case) | bezel 82.6 = 3.252 in; bezel bore 70.21 | Follow the 3D. |
| Pipe thread taper | 1/2 NPT (1:16 on diameter = 1.7899 deg) | 1.783333 deg half-angle | Follow the 3D. |
| Graduations | 2 °F over -40 to 160 (101 marks) | 100 equal marks over 280 deg | Follow the 3D. |

**Undetermined:** the glyph outlines of the digits and the degree ring (boxes given in 4.7); the material of P03; the
exact start of the thread groove beyond the free end (any start that clears the material gives the same solid).
