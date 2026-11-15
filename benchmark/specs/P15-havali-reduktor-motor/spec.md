# Design specification: air-driven gear motor (P15)

A rotary-vane air motor (rear) bolted into a worm-gear speed-reducer housing (front) that carries a keyed output shaft
and a cast base with two feet; a muffler is screwed into one of the two air ports on top of the motor. The master is
three solids. This document is the only source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (Millimetre values in brackets are exact conversions, 1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - The **output shaft / motor axis is the Z axis**. The output shaft points to **+Z**; its end face is z = 2.63.
    The front face of the gear housing (where the shaft leaves it) is the plane **z = 0**. The motor is at negative z.
  - **+Y is up.** The underside of the feet is the plane **y = -3.56**.
  - The two air ports are on top of the motor at **x = +1.25 and x = -1.25, z = -6.38**; the muffler sits in the port at
    x = +1.25.
  - The assembly is symmetric about the plane x = 0 except for the muffler and the thread phases.
- "(r, z) profile" = a closed profile in a half plane containing the Z axis, r = distance from Z, revolved 360 deg.
- All three bodies are modelled in place in this frame.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Air motor body (barrel, rear hex, front spigot and stub shaft, top boss with two threaded air ports) | custom |
| P02 | 1 | Muffler (threaded nipple, hex, cup) | bought-in |
| P03 | 1 | Gear housing with base, feet and output shaft (one solid) | custom |

Contacts (no gaps, no clearances in the master): the P01 spigot and stub shaft fill a matching stepped recess in the
back of P03 exactly; the P01 flange face z = -5.28 lies on the P03 rear face; the P02 nipple is screwed into the +X port
of P01 with its end face on the port floor. The modelled threads of P01 and P02 overlap slightly (see section 7).

## 3. P01 Air motor body

**F1. Revolved body.** (r, z) profile, closed, revolved about Z. Start on the axis at the rear and go in order:
1. (0, -8.99) to (0.625, -8.99) (rear end face)
2. line to (0.71169, -8.93995) (corner chamfer of the hex, cone at 60 deg to the axis; see F2)
3. line to (0.71169, -8.615) (turned hex corners)
4. line to (0.7375, -8.615) (shoulder face z = -8.615, facing -Z)
5. line to (0.8125, -8.54) (45 deg chamfer)
6. line to (0.8125, -8.305) (rear neck, diameter 1.625)
7. concave arc R0.5, centre (1.3125, -8.305), to (1.3125, -7.805)
8. line to (1.72, -7.805) (rear flange back face)
9. line to (1.72, -7.43) (rear flange, diameter 3.44)
10. line to (1.67, -7.43) (step face, facing +Z)
11. convex arc R11.05, centre (-9.33, -6.38), through (1.72, -6.38), to (1.67, -5.33) (barrel; its centre lies on the
    opposite side of the axis: the surface is a barrel of maximum diameter 3.44 at z = -6.38 and end diameter 3.34)
12. line to (1.72, -5.33) (step face, facing -Z)
13. line to (1.72, -5.28) (front flange)
14. line to (1.5, -5.28) (front flange face, sits on P03)
15. line to (1.5, -4.25) (front spigot, diameter 3.0)
16. line to (0.25, -4.25)
17. line to (0.25, -3.13) (stub shaft, diameter 0.5, plain, no key)
18. line to (0, -3.13), close along the axis.

**F2. Rear hex.** Between z = -8.99 and z = -8.615 the body is additionally bounded by a regular hexagonal prism along Z,
**1.25 across flats**, flats normal to +-X and to +-60 deg from X (corners on +-Y). Inside that z range the solid is
the intersection of the hex prism with F1: the hex corners are turned to diameter 1.42338 (r 0.71169) and chamfered by
the 60 deg cone of step 2 (the rear end face is the full circle r 0.625, which is the inscribed circle of the hex). The
shoulder z = -8.615 runs from the hex out to r 0.7375.

**F3. Top boss.** An obround (slot-shaped) prism along Y, united with F1: in plan (x, z) it is the outline of two
circles of radius 0.5 centred (x, z) = (+-1.25, -6.38) joined by the tangent lines z = -6.88 and z = -5.88 (overall
x from -1.75 to 1.75, width 1.0). It extends from y = 0 to y = 1.72 (top face y = 1.72). All edges of the prism top
and bottom outline are rounded **R0.05**. Only the parts outside the barrel show: the top face, the long sides above
the barrel, the two round ends (they stand 0.03 proud of the barrel sides near x = +-1.75), and a sliver of the bottom
R0.05 round near y = 0.004 to 0.05 at x = +-1.72 to 1.75. Between x = -0.36154 and +0.36154 the barrel rises above
y = 1.67 at the long sides, so the R0.05 round there blends the top face directly into the barrel (rolling-ball blend,
radius 0.05).

**F4. Two air ports (identical, translated copies),** vertical axes at (x, z) = (+-1.25, -6.38):
- port floor: flat, at **y = 1.3182** (depth 0.4018 below the top face y = 1.72); no drill point;
- 45 deg countersink: cone from r 0.27602 at y = 1.72 down to r 0.26484 at depth 0.01117;
- **internal tapered pipe thread, modelled** (1/4 NPT form), right hand, **18 threads per inch** (pitch P = 0.055556),
  60 deg included flank angle (flanks at 30 deg to the radial direction). With d = depth below y = 1.72:
  - major (root) radius r = 0.27 - 0.031131 d (taper half angle 1.7833 deg, 1:16 on the diameter);
  - minor (crest) radius = major radius - 0.03084;
  - axial lengths per pitch: root flat 0.00604 (0.1533 mm) on the major cone, crest flat 0.0139 (0.353 mm) on the minor
    radius, the rest is the two flanks;
  - **phase** (same for both ports, measured in each port's own half planes): the root flat is centred at depth
    d = 0.01692 + k P in the half plane pointing to +X from the port axis, 0.01692 + P/4 + k P toward +Z,
    + P/2 toward -X, + 3P/4 toward -Z (k integer);
  - the thread runs from the countersink to the floor; the floor cuts it off.

## 4. P02 Muffler

Axis: the vertical line x = 1.25, z = -6.38. "(r, y)" = profile about that axis.

**F1. Revolved body.** (r, y) profile, closed, revolved:
1. (0, 1.3182) to (0.20939, 1.3182) (nipple end face, on the port floor of P01)
2. 45 deg chamfer to (0.22087, 1.32968) (it cuts the first thread turn)
3. threaded nipple (F2) up to y = 1.9128, then plain neck r 0.27 from y = 1.9128 to 1.96835
4. step face y = 1.96835 from r 0.27 out to the hex (F3)
5. hex region y = 1.96835 to 2.29648 (F3)
6. concave arc R0.42243, centre (0.625, 1.99932), from (0.32476, 2.29648) to (0.625, 2.42175)
7. line to (0.625, 2.52175) (neck, diameter 1.25)
8. line to (0.75, 2.52175) (shoulder face, facing -Y)
9. line to (0.75, 3.57) (cup, diameter 1.5)
10. concave arc R0.06, centre (0.81, 3.57), to (0.81, 3.63)
11. convex arc R0.05, centre (0.81, 3.68), through (0.86, 3.68), to (0.81, 3.73) (rim bead, outside diameter 1.72)
12. line to (0, 3.73) (flat top), close along the axis.
The muffler is solid (no internal cavity in the master).

**F2. External tapered pipe thread, modelled** (1/4 NPT form), right hand, 18 threads per inch (P = 0.055556), 60 deg:
- crest (major) radius r = 0.27 - 0.031131 (1.9128 - y); root (minor) radius = crest radius - 0.03533;
- axial lengths per pitch: crest flat 0.0078 (0.198 mm) on the crest cone, root flat 0.00694 (0.1764 mm) on the root
  radius, the rest is the two flanks;
- **phase:** the crest flat is centred at y = 1.41933 + k P in the half plane pointing to +X from the muffler axis;
  at y = 1.41933 - P/4 + k P toward +Z, - P/2 toward -X, - 3P/4 toward -Z;
- lower end: cut by the 45 deg end chamfer; upper end (run-out): the thread groove ends against a 15 deg cone (half
  angle 15 deg to the axis) of radius 0.27 at y = 1.9128 and radius 0.25933 at y = 1.87301; material inside that cone
  is not cut, so the groove fades out between about y = 1.77 and 1.9128.

**F3. Hex,** 0.5625 across flats (flats normal to +-Z and +-60 deg from Z; corners on +-X of the muffler axis), from
y = 1.96835 to y = 2.29648, intersected with: a bottom chamfer cone at 60 deg to the axis from r 0.28125 at
y = 1.96835 to r 0.32476 (the corner radius) at y = 1.99346; and a top chamfer cone at 44.7047 deg to the axis from
r 0.28125 at y = 2.25252 to r 0.32476 at y = 2.29648. The arc of F1 step 6 starts on the corner circle r 0.32476 at
y = 2.29648.

## 5. P03 Gear housing, base and output shaft (one solid)

**F1. Revolved body.** (r, z) profile, closed, revolved about Z:
1. (0, -3.13) to (0.25, -3.13) (bottom of the stub-shaft bore, matches P01)
2. line to (0.25, -4.25); line to (1.5, -4.25); line to (1.5, -5.28) (stepped rear recess, exactly the P01 spigot)
3. line to (2.5, -5.28) (rear face, facing -Z)
4. line to (2.77298, -4.53) (cone, 20 deg to the axis)
5. line to (3.05, -4.53); line to (3.05, -4.155) (rear band, diameter 6.1)
6. line to (3.0, -4.155)
7. convex arc R13.0213, centre (-9.971, -3.015), through (3.05, -3.015), to (3.0, -1.875) (housing barrel, max
   diameter 6.1)
8. line to (3.05, -1.875); line to (3.05, -1.5) (front band)
9. line to (1.625, -1.5) (front face of the housing body, facing +Z)
10. line to (1.625, -0.375) (front boss, diameter 3.25)
11. line to (1.5, -0.375); line to (1.5, 0) (pilot, diameter 3.0)
12. line to (0.5, 0) (mounting face z = 0)
13. line to (0.5, 2.58); line to (0.45, 2.63) (output shaft diameter 1.0, 0.05 x 45 deg end chamfer)
14. line to (0, 2.63), close along the axis.

**F2. Keyway** in the output shaft, on +Y: width 0.25 (between the planes x = -0.125 and x = 0.125), flat floor at
y = 0.359 (0.141 below the shaft surface at the centre, 0.125 at the keyway sides), from a flat square end at z = 0.57
to the shaft end z = 2.63 (open; the end chamfer cuts across it).

**F3. Four tapped holes** in the face z = 0, axes parallel to Z at (x, y) = (0, 1.25), (1.25, 0), (0, -1.25),
(-1.25, 0) (on a 2.5 diameter circle):
- flat floor at z = -0.44 (no drill point); 45 deg countersink from r 0.13041 at z = 0;
- **internal thread, modelled, 1/4-20 UNC form**, right hand, pitch 0.05, 60 deg; major (root) radius 0.125, minor
  (crest) radius 0.09794; axial lengths per pitch: root flat 0.00625, crest flat 0.0125;
- **phase** of the hole at (0, 1.25): root flat centred at depth 0.003125 + 0.05k below z = 0 in the half plane
  pointing to +Y (radially outward), 0.015625 + 0.05k toward +X, 0.028125 + 0.05k toward -Y, 0.040625 + 0.05k
  toward -X. The other three holes are this hole rotated about the Z axis by -90, 180 and +90 deg (thread included).

**F4. Base.** Added to F1 (united):
- **Pedestal:** box x from -1.75 to 1.75, z from -4.015 to -2.015, from its underside y = -3.51 up into the barrel
  (its side faces x = +-1.75 end where they meet the barrel, at about y = -2.451).
- **Two feet,** mirror images about x = 0. Right foot: box x from 1.54 to 3.04, y from -3.56 to -3.06 (thickness
  0.5), z from -4.265 to -1.765. The feet stand 0.05 below the pedestal underside.
- **Foot holes:** four through holes diameter 0.34, vertical, at (x, z) = (+-2.625, -3.89) and (+-2.625, -2.14),
  through the foot thickness.
- **Rounds R0.125 on each foot:** the four vertical corner edges (corner axes at (x, z) = (1.665, -4.14),
  (2.915, -4.14), (2.915, -1.89), (1.665, -1.89)); all exposed top edges of the foot (y = -3.06) convex R0.125, with
  spherical corners R0.125 at the outer corners.
- **Fillets R0.125 (concave)** between the foot top y = -3.06 and the pedestal sides x = +-1.75 (axis x = +-1.875,
  y = -2.935) and the pedestal ends z = -4.015 / -2.015 (axes y = -2.935, z = -4.14 / -1.89); and vertical fillets
  between the pedestal ends and the inner face x = +-1.54 of the foot parts that stick out beyond the pedestal (axes at
  (x, z) = (+-1.415, -4.14) and (+-1.415, -1.89), from the pedestal underside y = -3.51 to y = -3.185). The corner
  patches where these fillets and the foot top rounds meet are R0.125 blends (torus, tube centre circle R0.25).
- The pedestal underside and its edges are sharp; the pedestal meets the barrel without a fillet.

## 6. Acceptance targets

| ID | Volume in3 | Area in2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 34.0273 | 67.663 | 0.0000 | 0.0375 | -6.2685 | -1.75 | 1.75 | -1.72 | 1.72 | -8.99 | -3.13 | 101 |
| P02 | 2.59752 | 12.6167 | 1.2500 | 2.9808 | -6.3800 | 0.39 | 2.11 | 1.3182 | 3.73 | -7.24 | -5.52 | 70 |
| P03 | 118.3418 | 189.963 | 0.0000 | -0.2105 | -2.8678 | -3.05 | 3.05 | -3.56 | 3.05 | -5.28 | 2.63 | 196 |

In millimetres: P01 557607 mm3, 43653.5 mm2; P02 42565.8 mm3, 8139.8 mm2; P03 1939275 mm3, 122556.3 mm2.
Whole assembly: 154.967 in3, 270.242 in2, CoM (0.0210, -0.1026, -3.6734), bounding box X [-3.05, 3.05],
Y [-3.56, 3.73], Z [-8.99, 2.63].

Check values: output shaft diameter 1.0, length 2.63 from the face z = 0; shaft centre 3.56 above the base; feet holes
5.25 across and 1.75 along, diameter 0.34; front tapped holes on a 2.5 circle; ports 2.5 apart; port axis to shaft end
9.01; housing diameter 6.1; motor barrel diameter 3.44; muffler rim diameter 1.72, top at y = 3.73.

## 7. Source simplifications and undetermined items

- The motor, gear set, vanes and all internals are not modelled: P01 and P03 are solid (except the P03 rear recess
  filled by P01, and the tapped holes / ports). Reproduce them solid.
- No fasteners and no key are modelled (the product includes a key; the master does not).
- The external thread of P02 and the internal thread of the P01 port are modelled with the phases given; they do not
  mate exactly (crest of one against the flank of the other); leave the phases as given.
- The catalogue's overall sizes 11 1/2 (length), 6 (width) and 7 1/4 (height) disagree with the master (11.620, 6.100
  over the flange / 6.080 over the feet, 7.290); follow the master values in this document.
- Material (iron housing) is product data only. Nothing else is undetermined.
