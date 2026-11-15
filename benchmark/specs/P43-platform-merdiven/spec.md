# Design specification: fibreglass two-sided platform step ladder (6 ft, 46 in platform)

A complete two-sided platform step ladder as one assembly of **248 separate solids**: four fibreglass C-channel side
rails (two climbing sides), eight ribbed metal steps (four per side), a ribbed standing platform made of two plates,
a round handle bar at the top, two top caps with side plates and hinge plates, lattice spreader braces and step-end
shoes at the bottom, foot sleeves, foot plates and ribbed foot pads, step brace straps, platform supports and lock
castings, thin label strips, and the rivets / discs that hold it together. This document is the only source for the
rebuild. Every number below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inch.** Every length in this document is in inches, angles in degrees. (1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - **Y is up.** The floor is the plane **y = -46** (underside of the four foot pads). The top face of the standing
    platform is the plane **y = 0**. The highest point (top caps) is y = 26.0098.
  - **X runs across the ladder (left / right)**, the assembly is mirror-symmetric about the plane **x = 0** in its
    main parts. **Z runs front / back**: the two climbing sides lie at z < 0 and z > 0; the ladder is open (spread)
    position, the feet stand at z = ±21.5 .. ±24.8.
  - Overall extents: x -12.5938 .. 12.5938, y -46 .. 26.0098, z -24.7961 .. 24.7961.
- **Every body is a separate solid.** Identical bodies are described once in a local frame (u, v, w) and placed with
  the transformations of section 6.

## 2. Product description

The ladder has two identical climbing sides (a front side at z < 0 and a back side at z > 0, each the other turned
180 deg about the Y axis). Each side has two **side rails** (P01, P02; P02 is the mirror image of P01), splayed so the
side is 25.19 wide at the feet and narrower at the top, and **four ribbed steps** (P03 lowest .. P06 top, same section,
different lengths) whose ends sit inside the rail channels. Under each of the three upper steps two **brace straps**
(P22) run diagonally from the step to the rails. The **lowest step** carries two **end shoes** (P11, P12) and the bottom
of each rail carries a **lattice spreader brace** (P09, P10), a **foot sleeve** (P14, P15), a **foot plate** (P24 / P25)
and a **ribbed foot pad** (P13). At the top, two **top caps** are built from side plates (P16 .. P19), **rail top caps**
(P20, P21) and **hinge plates** (P28, P29) on two **hinge spacer drums** (P30); a round **handle bar** (P08) spans the
top. The **standing platform** at y = 0 consists of two **ribbed plates** (P07) on two **support angles** (P23) with
**corner brackets** (P31, P32) and **lock castings** (P26, P27). **Label strips** (P33 .. P35, 0.005 / 0.002 thick) lie
on the rail faces. Hardware: rivets (H01 .. H03), rivet tail discs, collars and small discs (H04 .. H10).

**Simplifications that exist in the source model and must be reproduced:**
- No rivet holes are modelled: rivets and discs pass through the solid rails, steps and straps, and the step ends lie
  inside the rail channels. These bodies overlap (section 7); keep the overlaps, do not cut holes.
- The rails are plain channels (no texture), the steps and platform carry only the grooves described.
- The foot plates are not all alike: one (P24) has sharp corners, three (P25) have R0.1 corners.
- The label strips are modelled as very thin solids (0.005 and 0.002 thick).
- Several mirror pairs exist (type A / type B); a type B body is the exact mirror image of its type A body.

## 3. Part list

35 distinct custom parts and 10 distinct hardware items, **248 bodies in total** (the original file has 248 solids
and no empty shells). V and A are per body; "local box" is the extent along local u, v, w.

| ID | Name | Kind | Count | Faces | V (in³) | A (in²) | Local box u x v x w |
|---|---|---|---|---|---|---|---|
| P01 | Side rail, type A | custom | 2 | 14 | 24.62231 | 784.9589 | 1.1814 x 75.5548 x 3.0304 |
| P02 | Side rail, type B (mirror of P01) | custom | 2 | 14 | 24.62231 | 784.9589 | 1.1814 x 75.5548 x 3.0304 |
| P03 | Ribbed step, 23.016 in (lowest) | custom | 2 | 28 | 11.69392 | 293.3827 | 1.5 x 23.016 x 3.4467 |
| P04 | Ribbed step, 20.739 in | custom | 2 | 28 | 10.52663 | 264.1847 | 1.5 x 20.7387 x 3.4467 |
| P05 | Ribbed step, 18.462 in | custom | 2 | 28 | 9.35935 | 234.9867 | 1.5 x 18.4615 x 3.4467 |
| P06 | Ribbed step, 16.184 in (top) | custom | 2 | 28 | 8.19206 | 205.7887 | 1.5 x 16.1842 x 3.4467 |
| P07 | Ribbed platform plate | custom | 2 | 32 | 11.28099 | 227.8980 | 0.15 x 7.9355 x 12.75 |
| P08 | Top handle bar | custom | 1 | 4 | 9.63857 | 37.8630 | 10.7878 x 1.0692 x 2.1231 |
| P09 | Lattice spreader brace, type A | custom | 2 | 149 | 8.87665 | 184.3586 | 2.663 x 4.7825 x 14.1777 |
| P10 | Lattice spreader brace, type B (mirror of P09) | custom | 2 | 149 | 8.87665 | 184.3586 | 2.663 x 4.7825 x 14.1777 |
| P11 | Lower step end shoe, type A | custom | 2 | 38 | 3.88915 | 88.4944 | 1.7044 x 6.9217 x 3.669 |
| P12 | Lower step end shoe, type B (mirror of P11) | custom | 2 | 38 | 3.88915 | 88.4944 | 1.7044 x 6.9217 x 3.669 |
| P13 | Ribbed foot pad | custom | 4 | 48 | 2.03674 | 14.2756 | 0.6 x 1.29 x 3.2999 |
| P14 | Rail foot sleeve, type A | custom | 2 | 10 | 1.88797 | 61.8224 | 1.2439 x 4.8269 x 5.3991 |
| P15 | Rail foot sleeve, type B (mirror of P14) | custom | 2 | 10 | 1.88797 | 61.8224 | 1.2439 x 4.8269 x 5.3991 |
| P16 | Top cap side plate, type A | custom | 1 | 50 | 1.56245 | 32.2213 | 0.1995 x 5.4646 x 3.5308 |
| P17 | Top cap side plate, type A, mirror (B) | custom | 1 | 50 | 1.56244 | 32.2213 | 0.1995 x 5.4646 x 3.5308 |
| P18 | Top cap side plate, second form | custom | 1 | 33 | 1.55515 | 32.2717 | 0.199 x 4.8657 x 4.5489 |
| P19 | Top cap side plate, second form, mirror | custom | 1 | 33 | 1.55515 | 32.2717 | 0.199 x 4.8657 x 4.5489 |
| P20 | Rail top cap, type A | custom | 2 | 17 | 1.47836 | 40.5720 | 1.2439 x 3.2746 x 4.6266 |
| P21 | Rail top cap, type B (mirror of P20) | custom | 2 | 17 | 1.47836 | 40.5720 | 1.2439 x 3.2746 x 4.6266 |
| P22 | Step brace strap | custom | 12 | 6 | 1.18432 | 18.3178 | 0.15 x 1.1875 x 7.9635 |
| P23 | Platform support angle | custom | 2 | 14 | 1.16091 | 48.3401 | 0.75 x 0.75 x 16.6993 |
| P24 | Foot plate, sharp corners | custom | 1 | 6 | 0.63854 | 9.8908 | 0.15 x 1.29 x 3.2999 |
| P25 | Foot plate, rounded corners | custom | 3 | 10 | 0.63725 | 9.8479 | 0.15 x 1.29 x 3.2999 |
| P26 | Platform lock casting, type A | custom | 1 | 38 | 0.59529 | 5.4261 | 0.45 x 1.4078 x 2.2396 |
| P27 | Platform lock casting, type B (mirror of P26) | custom | 1 | 38 | 0.59529 | 5.4261 | 0.45 x 1.4078 x 2.2396 |
| P28 | Top hinge plate, type A | custom | 2 | 30 | 0.53223 | 17.0751 | 0.1625 x 2.5999 x 3.7252 |
| P29 | Top hinge plate, type B (mirror of P28) | custom | 2 | 30 | 0.53223 | 17.0751 | 0.1625 x 2.5999 x 3.7252 |
| P30 | Hinge spacer drum | custom | 2 | 11 | 0.26834 | 2.3661 | 0.475 x 0.875 x 0.875 |
| P31 | Platform corner bracket, type A | custom | 2 | 25 | 0.11747 | 3.5001 | 0.9809 x 0.9903 x 1.5298 |
| P32 | Platform corner bracket, type B (mirror of P31) | custom | 2 | 25 | 0.11747 | 3.5001 | 0.9809 x 0.9903 x 1.5298 |
| P33 | Thin strip (label), 0.005 in | custom | 23 | 6 | 0.01467 | 5.9040 | 0.005 x 1.25 x 2.7183 |
| P34 | Thin strip (label), 0.002 in, form A | custom | 11 | 6 | 0.00587 | 5.8821 | 0.002 x 1.2548 x 2.6925 |
| P35 | Thin strip (label), 0.002 in, form B | custom | 11 | 6 | 0.00575 | 5.7677 | 0.002 x 1.2373 x 2.6557 |
| H01 | Rivet, 0.55 in long | hardware | 12 | 10 | 0.09700 | 1.2018 | 0.55 x 0.5 x 0.5 |
| H02 | Rivet, 0.40 in long | hardware | 12 | 10 | 0.06754 | 0.9662 | 0.4 x 0.5 x 0.5 |
| H03 | Rivet, 0.3375 in long, recessed tail | hardware | 32 | 13 | 0.05227 | 0.9055 | 0.3375 x 0.5 x 0.5 |
| H04 | Rivet tail disc, 0.10 x 0.50 | hardware | 20 | 6 | 0.01787 | 0.4967 | 0.1 x 0.5 x 0.5 |
| H05 | Collar, 0.325 dia x 0.15 | hardware | 4 | 6 | 0.01215 | 0.3020 | 0.15 x 0.325 x 0.325 |
| H06 | Disc, 0.375 dia x 0.10 | hardware | 16 | 6 | 0.00975 | 0.2983 | 0.1 x 0.375 x 0.375 |
| H07 | Disc, 0.325 dia x 0.10 | hardware | 4 | 6 | 0.00779 | 0.2450 | 0.1 x 0.325 x 0.325 |
| H08 | Disc, 0.25 dia x 0.05 | hardware | 22 | 6 | 0.00223 | 0.1242 | 0.05 x 0.25 x 0.25 |
| H09 | Domed cap, 0.25 dia | hardware | 4 | 4 | 0.00150 | 0.1085 | 0.05 x 0.25 x 0.25 |
| H10 | Disc, 0.15 dia x 0.05 | hardware | 8 | 6 | 0.00076 | 0.0507 | 0.05 x 0.15 x 0.15 |

## 4. Local frames and placement convention

- Each distinct part is described in its own **local frame (u, v, w)** (inch). Unless stated otherwise the part's local
  box starts at u = v = w = 0 (all local coordinates of the part are ≥ 0, small negative values are noted).
- **Placement** (section 6): a global point is **p = O + u·U + v·V + w·W**, where O is the instance origin and U, V, W
  are the global unit directions of the local axes (listed as orientation Q##). All orientations are proper rotations.
- **Mirror parts (type B):** the local geometry of a type B part is the type A geometry mirrored in the plane
  u = (local u extent) / 2, i.e. every local point (u, v, w) of type A becomes (e - u, v, w) with e the local u extent
  of the part (given with the part). Faces, radii and sections are otherwise identical.
- **Round hardware and the spacer drum (axisymmetric):** described by an axial half-section in (u, r) with u along the
  axis from the head face (u = 0) and r the radial distance; placement = axis point P (centre of the head face, u = 0)
  and axis direction D (toward +u).
- **Section notation:** "loop" = closed outline listed as points; "–" joins points by a straight line; "arc cC RR via M"
  is a circular arc of radius R about centre C through the point M to the next point. A "blend curve via M" is a
  free-form transition (rolling round) through M. "plane n(a, b, c), n·p = d" is the plane a·u + b·v + c·w = d;
  "extent (..)..(..)" is the local bounding box of that face. Cylinders give axis direction, a point on the axis near the
  face and the radius; tori give axis, centre, major R and minor r.
- A **"prism" part** is its section extruded along the named local axis through the whole local box, then bounded by
  the listed end / cut faces. Other parts list sections plus their complete face list.

## 5. Part geometry

### P01 Side rail, type A (2 bodies, 14 faces each)

Straight C-channel rail along local v. Section (u, w): web 0.0625 thick on u = 0 .. 0.0625 (outer web face u = 0), two flanges along w = 0 and w = 3.0304 whose faces carry a 1.6 deg draft (normals (∓0.0282, 0, ±0.9996)), flange edges at u = 1.1814, four R0.1 corner rounds at the web / flange corners (two outside, two inside). Both ends are cut by parallel planes with normal (0.0987, 0.9539, -0.2833): the foot end n·p = 0.1079 (open channel). At the top end the outer faces run to n·p = 71.2324, the channel inside (between the flanges, u ≥ 0.0625) stops at n·p = 71.1699, so the last 0.0625 is a solid cap filling the outline closed across u = 1.1814.

Local box: u 0 .. 1.1814, v 0 .. 75.5548, w 0 .. 3.0304.

Section at v = 37.7774 (coordinates u, w):
  - loop: (0, 2.8998) – arc c(0.1, 2.8998) R0.1 via (0.0283, 2.9696) – (0.0972, 2.9998) – (1.1814, 3.0304) – (1.1814, 2.9679) – (0.1597, 2.939) – arc c(0.1625, 2.8391) R0.1 via (0.0908, 2.9088) – (0.0625, 2.8391) – (0.0625, 0.1643) – arc c(0.1625, 0.1643) R0.1 via (0.0928, 0.0926) – (0.1653, 0.0643) – (1.1814, 0.093) – (1.1814, 0.0305) – (0.1028, 0) – arc c(0.1, 0.1) R0.1 via (0.0303, 0.0283) – (0, 0.1) – (0, 2.8998)
Face list (all 14 faces):
  - cylinder axis dir(0, 1, 0) through (0.1, 38.2646, 2.8998) R0.1; extent (0, 0.9744, 2.8998)..(0.0972, 75.5548, 2.9998)
  - cylinder axis dir(0, 1, 0) through (0.1, 37.4023, 0.1) R0.1; extent (0, 0.1025, 0)..(0.1028, 74.7021, 0.1)
  - cylinder axis dir(0, -1, 0) through (0.1625, 37.3821, 0.1643) R0.1; extent (0.0625, 0.1151, 0.0642)..(0.1653, 74.6492, 0.1643)
  - cylinder axis dir(0, -1, 0) through (0.1625, 38.2073, 2.8391) R0.1; extent (0.0625, 0.9499, 2.8391)..(0.1597, 75.4647, 2.9391)
  - plane n(0.0987, 0.9539, -0.2833), n·p = 0.1079; extent (0, 0, 0)..(1.1814, 0.9955, 3.0304)
  - plane n(-0.0282, 0, 0.9996), n·p = 0.0596; extent (0.1653, 0.0186, 0.0643)..(1.1814, 74.6088, 0.093)
  - plane n(0.0282, 0, -0.9996), n·p = -2.9334; extent (0.1597, 0.8725, 2.939)..(1.1814, 75.4633, 2.9679)
  - plane n(1, 0, 0), n·p = 0.0625; extent (0.0625, 0.1555, 0.1642)..(0.0625, 75.4436, 2.8391)
  - plane n(0.0987, 0.9539, -0.2833), n·p = 71.1699; extent (0.0625, 74.5123, 0.0643)..(1.1814, 75.4647, 2.9679)
  - plane n(-0.0282, 0, 0.9996), n·p = -0.0029; extent (0.1028, 0, 0)..(1.1814, 74.6617, 0.0305)
  - plane n(0.0987, 0.9539, -0.2833), n·p = 71.2324; extent (0, 74.5592, 0)..(1.1814, 75.5548, 3.0304)
  - plane n(-1, 0, 0), n·p = -1.1814; extent (1.1814, 0, 0.0304)..(1.1814, 75.4503, 3.0304)
  - plane n(0.0282, 0, -0.9996), n·p = -2.9959; extent (0.0972, 0.891, 2.9998)..(1.1814, 75.5533, 3.0304)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0.1428, 0.1)..(0, 75.5337, 2.8999)

### P02 Side rail, type B (mirror of P01) (2 bodies, 14 faces each)

Mirror image of P01: take P01's local geometry and replace u by (1.1814 - u). Same faces, radii and volume.

### P03 Ribbed step, 23.016 in (lowest) (2 bodies, 28 faces each)

Ribbed step tread, an extrusion along local v (the step length) of the section below, both ends cut by planes 5.66 deg off the section plane (normals (0.0987, ±0.9951, 0)) so the step is a trapezoid in plan. Section (u, w): tread face u = 0 from w = 0.4477 to 3.4467 with nine semicircular grooves R0.075 centred on the tread face (u = 0) at w = 0.7082, 0.8943, 1.6384, 1.8244, 2.0104, 2.1964, 2.9405, 3.1265, 3.3125; two legs 0.1 thick (u 0 .. 0.1 at the tread, inclined 16.6 deg) running to two feet at u = 1.5 (w 0 .. 0.1044 and w 2.8947 .. 2.999). No holes are modelled.

Local box: u 0 .. 1.5, v 0 .. 23.016, w 0 .. 3.4467.

Section at v = 11.508 (coordinates u, w):
  - loop: (0, 3.3875) – arc c(0, 3.3125) R0.075 via (0.075, 3.3125) – (0, 3.2375) – (0, 3.2015) – arc c(0, 3.1265) R0.075 via (0.075, 3.1265) – (0, 3.0515) – (0, 3.0155) – arc c(0, 2.9405) R0.075 via (0.075, 2.9405) – (0, 2.8655) – (0, 2.2714) – arc c(0, 2.1964) R0.075 via (0.075, 2.1964) – (0, 2.1214) – (0, 2.0854) – arc c(0, 2.0104) R0.075 via (0.075, 2.0104) – (0, 1.9354) – (0, 1.8994) – arc c(0, 1.8244) R0.075 via (0.075, 1.8244) – (0, 1.7494) – (0, 1.7134) – arc c(0, 1.6384) R0.075 via (0.075, 1.6384) – (0, 1.5634) – (0, 0.9693) – arc c(0, 0.8943) R0.075 via (0.075, 0.8943) – (0, 0.8193) – (0, 0.7832) – arc c(0, 0.7082) R0.075 via (0.075, 0.7082) – (0, 0.6332) – (0, 0.4477) – (1.5, 0) – (1.5, 0.1044) – (0.1, 0.5222) – (0.1, 3.3125) – (1.5, 2.8947) – (1.5, 2.999) – (0, 3.4467) – (0, 3.3875)
Faces not parallel to v (end faces, cuts, cross features):
  - plane n(0.0987, -0.9951, 0), n·p = -22.7557; extent (0, 22.8673, 0)..(1.5, 23.016, 3.4467)
  - plane n(0.0987, 0.9951, 0), n·p = 0.148; extent (0, 0, 0)..(1.5, 0.1487, 3.4467)

### P04 Ribbed step, 20.739 in (2 bodies, 28 faces each)

Same section as P03 (section and grooves identical), extruded along local v; local v extent 20.7387. End faces:

  - plane n(0.0987, -0.9951, 0), n·p = -20.4896; extent (0, 20.59, 0)..(1.5, 20.7387, 3.4467)
  - plane n(0.0987, 0.9951, 0), n·p = 0.148; extent (0, 0, 0)..(1.5, 0.1487, 3.4467)

### P05 Ribbed step, 18.462 in (2 bodies, 28 faces each)

Same section as P03 (section and grooves identical), extruded along local v; local v extent 18.4615. End faces:

  - plane n(0.0987, -0.9951, 0), n·p = -18.2234; extent (0, 18.3128, 0)..(1.5, 18.4615, 3.4467)
  - plane n(0.0987, 0.9951, 0), n·p = 0.148; extent (0, 0, 0)..(1.5, 0.1487, 3.4467)

### P06 Ribbed step, 16.184 in (top) (2 bodies, 28 faces each)

Same section as P03 (section and grooves identical), extruded along local v; local v extent 16.1842. End faces:

  - plane n(0.0987, -0.9951, 0), n·p = -15.9573; extent (0, 16.0355, 0)..(1.5, 16.1842, 3.4467)
  - plane n(0.0987, 0.9951, 0), n·p = 0.148; extent (0, 0, 0)..(1.5, 0.1487, 3.4467)

### P07 Ribbed platform plate (2 bodies, 32 faces each)

Ribbed platform plate: a 0.15 thick plate (u 0 .. 0.15, top face u = 0) extruded along local w from 0 to 12.75. Section (u, v): nine semicircular grooves R0.125 centred on the top face at v = 0.5, 1.0, 1.5, 3.459, 3.9454, 4.4317, 6.3907, 6.8907, 7.3907; two V-notches 0.125 deep with flanks at ±65 deg to the face (50 deg between flanks) and a flat bottom; the rear edge (v = 7.89 .. 7.9355) is bevelled. No holes are modelled.

Local box: u 0 .. 0.15, v 0 .. 7.9355, w 0 .. 12.75.

Section at w = 6.375 (coordinates u, v):
  - loop: (0, 6.2657) – arc c(0, 6.3907) R0.125 via (0.125, 6.3907) – (0, 6.5157) – (0, 6.7657) – arc c(0, 6.8907) R0.125 via (0.125, 6.8907) – (0, 7.0157) – (0, 7.2657) – arc c(0, 7.3907) R0.125 via (0.125, 7.3907) – (0, 7.5157) – (0, 7.8907) – (0.15, 7.9355) – (0.15, 0) – (0, 0) – (0, 0.375) – arc c(0, 0.5) R0.125 via (0.125, 0.5) – (0, 0.625) – (0, 0.875) – arc c(0, 1) R0.125 via (0.125, 1) – (0, 1.125) – (0, 1.375) – arc c(0, 1.5) R0.125 via (0.125, 1.5) – (0, 1.625) – (0, 2.781) – (0.125, 2.8393) – (0.125, 3.1061) – (0, 3.1644) – (0, 3.334) – arc c(0, 3.459) R0.125 via (0.125, 3.459) – (0, 3.584) – (0, 3.8204) – arc c(0, 3.9454) R0.125 via (0.125, 3.9454) – (0, 4.0704) – (0, 4.3067) – arc c(0, 4.4317) R0.125 via (0.125, 4.4317) – (0, 4.5567) – (0, 4.7263) – (0.125, 4.7846) – (0.125, 5.0515) – (0, 5.1097) – (0, 6.2657)
Faces not parallel to w (end faces, cuts, cross features):
  - plane n(0, 0, 1), n·p = 12.75; extent (0, 0, 12.75)..(0.15, 7.9355, 12.75)
  - plane n(0, 0, 1), n·p = 0; extent (0, 0, 0)..(0.15, 7.9355, 0)

### P08 Top handle bar (1 bodies, 4 faces each)

Solid round bar R0.5346 (diameter 1.0692). The axis is the line through local (5.367, 0.5346, 0.5269) with direction (-0.9951, 0, 0.0987); one end is the plane u = 0, the other the plane n(-0.9805, 0, 0.1963)·p = -10.4744.

Local box: u 0 .. 10.7878, v 0 .. 1.0692, w -0.5268 .. 1.5963.

Section at u = 5.3939 (coordinates v, w):
  - loop: (0, 0.5243) – blend curve via (0.5346, -0.0129) – (1.0692, 0.5243) – blend curve via (0.5346, 1.0615) – (0, 0.5243)
Face list (all 4 faces):
  - cylinder axis dir(-0.9951, 0, 0.0987) through (5.367, 0.5346, 0.5269) R0.5346; extent (0, 0, -0.5268)..(10.6823, 1.0692, 1.059)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0.5218)..(0, 1.0692, 1.5963)
  - plane n(-0.9805, 0, 0.1963), n·p = -10.4744; extent (10.5768, 0, -0.5268)..(10.7878, 1.0692, 0.5268)
  - cylinder axis dir(-0.9951, 0, 0.0987) through (5.367, 0.5346, 0.5269) R0.5346; extent (0, 0, 0)..(10.7878, 1.0692, 1.5963)

### P09 Lattice spreader brace, type A (2 bodies, 149 faces each)

Lattice spreader brace: a channel (U) section with two side walls 0.125 thick (u 0 .. 0.125 and 2.538 .. 2.663) joined by an inclined web, the side walls cut into a triangulated lattice; the outer faces of the side walls carry 0.05 deep recessed panels (face planes u = 0.05 and u = 2.613) and the top end has a cylindrical cut R5.4166. The face list below is complete (145 planes, 2 cylinders, 2 free-form blends); build the walls as the section outlines show and trim with the listed planes.

Local box: u 0 .. 2.663, v 0 .. 4.7825, w 0 .. 14.1777.

Section at u = 0.0666 (coordinates v, w):
  - loop: (1.3487, 10.352) – (2.5714, 0.5532) – (3.9099, 1.8662) – (3.9099, 9.6144) – (4.2398, 9.9381) – (0.8166, 14.1635) – (0.0139, 13.3761) – (0.0964, 13.2743) – blend curve via (0.9297, 11.8947) – (1.3487, 10.352)
Section at u = 1.3315 (coordinates v, w):
  - loop: (4.0466, 9.4023) – (4.3321, 9.6824) – (0.9913, 13.806) – (1.0809, 13.894) – (4.5042, 9.6686) – (4.1743, 9.3449) – (4.1743, 1.5967) – (2.8358, 0.2837) – (2.8155, 0.4465) – (4.0466, 1.6542) – (4.0466, 9.4023)
Section at u = 2.5964 (coordinates v, w):
  - loop: (1.8775, 9.813) – (3.1002, 0.0142) – (4.4387, 1.3272) – (4.4387, 9.0754) – (4.7686, 9.3991) – (1.3453, 13.6245) – (0.5427, 12.8371) – (0.6252, 12.7353) – blend curve via (1.4585, 11.3557) – (1.8775, 9.813)
Section at v = 4.3043 (coordinates u, w):
  - loop: (2.613, 1.9012) – (2.613, 2.0874) – (2.663, 2.0874) – (2.663, 2.2182) – (2.613, 2.2182) – (2.613, 3.3816) – (2.663, 3.3816) – (2.663, 3.5877) – (2.613, 3.5877) – (2.613, 4.962) – (2.663, 4.962) – (2.663, 5.062) – (2.613, 5.062) – (2.613, 5.1739) – (2.663, 5.1739) – (2.663, 5.2959) – (2.613, 5.2959) – (2.613, 6.5425) – (2.663, 6.5425) – (2.663, 6.6425) – (2.613, 6.6425) – (2.613, 6.6502) – (2.663, 6.6502) – (2.663, 6.7722) – (2.613, 6.7722) – (2.613, 8.1229) – (2.663, 8.1229) – (2.663, 8.2229) – (2.613, 8.2229) – (2.613, 9.8163) – (2.663, 9.8163) – (2.663, 9.9752) – (2.598, 9.9752) – (2.598, 9.9723) – (0.3749, 9.8724) – (1.9535, 9.2124) – (1.9535, 1.4642) – (2.598, 1.1947) – (2.598, 1.1676) – (2.663, 1.1676) – (2.663, 1.3076) – (2.613, 1.3076) – (2.613, 1.8012) – (2.663, 1.8012) – (2.663, 1.9012) – (2.613, 1.9012)
  - loop: (2.538, 9.1507) – (1.1985, 9.7108) – (2.538, 9.7709) – (2.538, 9.1507)
Face list (all 149 faces):
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 0.6916, 8.8052)..(2.613, 3.8234, 13.4619)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.7958, 1.8512)..(2.613, 4.3526, 3.3585)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.9236, 2.1775)..(2.613, 4.3526, 3.3816)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.6048, 3.4316)..(2.613, 4.275, 4.889)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.4035, 5.0327)..(2.613, 4.3526, 6.5025)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.6733, 3.547)..(2.613, 4.3526, 4.962)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.2017, 6.6324)..(2.613, 4.3153, 8.1199)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.5209, 5.2621)..(2.613, 4.3526, 6.5425)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.3719, 6.7384)..(2.613, 4.3526, 8.1229)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.124, 8.2229)..(2.613, 4.6476, 10.3709)
  - plane n(1, 0, 0), n·p = 2.613; extent (2.613, 2.9901, 0.2129)..(2.613, 4.3526, 1.8012)
  - plane n(-1, 0, 0), n·p = -2.663; extent (2.663, 0.5566, 0)..(2.663, 4.7825, 13.6103)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.9901, 0.2129)..(2.663, 3.1883, 1.8012)
  - plane n(0, 0.7003, -0.7139), n·p = 2.0808; extent (2.613, 3.1883, 0.2129)..(2.663, 4.3526, 1.355)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 1.355)..(2.663, 4.3526, 1.8012)
  - plane n(0, 0, 1), n·p = 1.8012; extent (2.613, 2.9901, 1.8012)..(2.663, 4.3526, 1.8012)
  - plane n(0, 0, -1), n·p = -8.2229; extent (2.613, 2.2288, 8.2229)..(2.663, 4.3526, 8.2229)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 8.2229)..(2.663, 4.3526, 9.1032)
  - plane n(0, 0.7003, -0.7139), n·p = -3.4502; extent (2.613, 4.3526, 9.1032)..(2.663, 4.6476, 9.3926)
  - plane n(0, 0.777, 0.6295), n·p = 9.5238; extent (2.613, 3.855, 9.3926)..(2.663, 4.6476, 10.3709)
  - plane n(0, -0.7003, 0.7139), n·p = 4.7036; extent (2.613, 2.159, 8.7071)..(2.663, 3.855, 10.3709)
  - plane n(0, 0.7139, 0.7003), n·p = 7.6387; extent (2.613, 2.124, 8.7071)..(2.663, 2.159, 8.7428)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.124, 8.2535)..(2.663, 2.185, 8.7428)
  - plane n(0, -0.5729, -0.8196), n·p = -8.0166; extent (2.613, 2.185, 8.2229)..(2.663, 2.2288, 8.2535)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 6.7384)..(2.663, 4.3526, 8.1229)
  - plane n(0, 0, 1), n·p = 8.1229; extent (2.613, 2.3719, 8.1229)..(2.663, 4.3526, 8.1229)
  - plane n(0, -0.5729, -0.8196), n·p = -8.0166; extent (2.613, 2.3719, 6.7384)..(2.663, 4.3526, 8.1229)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 5.2621)..(2.663, 4.3526, 6.5425)
  - plane n(0, 0, 1), n·p = 6.5425; extent (2.613, 2.5209, 6.5425)..(2.663, 4.3526, 6.5425)
  - plane n(0, -0.5729, -0.8196), n·p = -6.8066; extent (2.613, 2.5209, 5.2621)..(2.663, 4.3526, 6.5425)
  - plane n(0, -0.5729, -0.8196), n·p = -6.8066; extent (2.613, 2.3868, 6.6324)..(2.663, 2.3923, 6.6362)
  - plane n(0, 1, 0), n·p = 2.3923; extent (2.613, 2.3923, 6.6324)..(2.663, 2.3923, 6.6425)
  - plane n(0, 0, -1), n·p = -6.6425; extent (2.613, 2.3923, 6.6425)..(2.663, 4.3153, 6.6425)
  - plane n(0, 0.5729, 0.8196), n·p = 7.9166; extent (2.613, 2.2017, 6.6425)..(2.663, 4.3153, 8.1199)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.2017, 6.6362)..(2.663, 2.3868, 8.1199)
  - plane n(0, -0.6444, -0.7647), n·p = -5.5171; extent (2.613, 2.6733, 3.547)..(2.663, 4.3526, 4.962)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 3.547)..(2.663, 4.3526, 4.962)
  - plane n(0, 0, 1), n·p = 4.962; extent (2.613, 2.6733, 4.962)..(2.663, 4.3526, 4.962)
  - plane n(0, -0.6444, -0.7647), n·p = -5.5171; extent (2.613, 2.5866, 5.0327)..(2.663, 2.5895, 5.0351)
  - plane n(0, 1, 0), n·p = 2.5895; extent (2.613, 2.5895, 5.0327)..(2.663, 2.5895, 5.062)
  - plane n(0, 0, -1), n·p = -5.062; extent (2.613, 2.5895, 5.062)..(2.663, 4.3526, 5.062)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 5.062)..(2.663, 4.3526, 5.1401)
  - plane n(0, 0.5729, 0.8196), n·p = 6.7066; extent (2.613, 2.4035, 5.1401)..(2.663, 4.3526, 6.5025)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.4035, 5.0351)..(2.663, 2.5866, 6.5025)
  - plane n(0, 1, 0), n·p = 2.7867; extent (2.613, 2.7867, 3.4316)..(2.663, 2.7867, 3.4816)
  - plane n(0, 0, -1), n·p = -3.4816; extent (2.613, 2.7867, 3.4816)..(2.663, 4.275, 3.4816)
  - plane n(0, 0.6444, 0.7647), n·p = 5.4171; extent (2.613, 2.6048, 3.4816)..(2.663, 4.275, 4.889)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.6048, 3.4316)..(2.663, 2.7867, 4.889)
  - plane n(0, -0.6444, -0.7647), n·p = -4.4699; extent (2.613, 2.9236, 2.1775)..(2.663, 4.3526, 3.3816)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 2.1775)..(2.663, 4.3526, 3.3816)
  - plane n(0, 0, 1), n·p = 3.3816; extent (2.613, 2.9236, 3.3816)..(2.663, 4.3526, 3.3816)
  - plane n(0, 0.6444, 0.7647), n·p = 4.3699; extent (2.613, 2.7958, 2.0467)..(2.663, 4.3526, 3.3585)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 2.7958, 1.8512)..(2.663, 2.9839, 3.3585)
  - plane n(0, 1, 0), n·p = 2.9839; extent (2.613, 2.9839, 1.8512)..(2.663, 2.9839, 1.9012)
  - plane n(0, 0, -1), n·p = -1.9012; extent (2.613, 2.9839, 1.9012)..(2.663, 4.3526, 1.9012)
  - plane n(0, 1, 0), n·p = 4.3526; extent (2.613, 4.3526, 1.9012)..(2.663, 4.3526, 2.0467)
  - plane n(0, -0.9923, -0.1238), n·p = -3.1901; extent (2.613, 1.9907, 8.8052)..(2.663, 2.1162, 9.8112)
  - plane n(0, 0.7003, -0.7139), n·p = -4.8036; extent (2.613, 2.1162, 8.8052)..(2.663, 3.7884, 10.4456)
  - plane n(0, -0.7139, -0.7003), n·p = -10.0194; extent (2.613, 3.7884, 10.4099)..(2.663, 3.8234, 10.4456)
  - plane n(0, 0.777, 0.6295), n·p = 9.5238; extent (2.613, 1.3508, 10.4099)..(2.663, 3.8234, 13.4619)
  - plane n(0, -0.7003, 0.7139), n·p = 8.6639; extent (2.613, 0.6916, 12.8152)..(2.663, 1.3508, 13.4619)
  - plane n(0, -0.7769, -0.6296), n·p = -8.6063; extent (2.613, 0.6916, 12.7841)..(2.663, 0.7168, 12.8152)
  - free-form (blend) face; extent (2.613, 0.7168, 9.8112)..(2.663, 1.9907, 12.7841)
  - plane n(0, 0.7003, -0.7139), n·p = 2.1808; extent (2.598, 3.1141, 0)..(2.663, 4.4526, 1.313)
  - plane n(0, 1, 0), n·p = 4.4526; extent (2.598, 4.4526, 1.313)..(2.663, 4.4526, 9.0612)
  - plane n(0, 0.7003, -0.7139), n·p = -3.3502; extent (2.598, 4.4526, 9.0612)..(2.663, 4.7825, 9.3849)
  - plane n(0, 0.777, 0.6295), n·p = 9.6238; extent (2.598, 1.3593, 9.3849)..(2.663, 4.7825, 13.6103)
  - plane n(0, -0.7003, 0.7139), n·p = 8.7639; extent (2.598, 1.3579, 13.609)..(2.663, 1.3593, 13.6103)
  - plane n(0, -0.9923, -0.1238), n·p = -3.0901; extent (2.598, 3.1111, 0)..(2.663, 3.1141, 0.0242)
  - plane n(-1, 0, 0), n·p = -2.598; extent (2.598, 1.3579, 0)..(2.598, 4.7825, 13.6103)
  - plane n(0, -0.6444, -0.7647), n·p = -4.5451; extent (0, 2.367, 2.7449)..(0.05, 3.796, 3.949)
  - plane n(0, -0.6444, -0.7647), n·p = -4.4451; extent (0, 2.2392, 2.6141)..(0.05, 3.796, 3.9259)
  - plane n(0, -0.6444, -0.7647), n·p = -5.5923; extent (0, 2.03, 5.6001)..(0.05, 2.0329, 5.6025)
  - plane n(0, -0.6444, -0.7647), n·p = -5.5923; extent (0, 2.1167, 4.1144)..(0.05, 3.796, 5.5294)
  - plane n(0, -0.6444, -0.7647), n·p = -5.4923; extent (0, 2.0482, 4.049)..(0.05, 3.7184, 5.4564)
  - plane n(0, 0.5729, 0.8196), n·p = 6.9527; extent (0, 1.9643, 5.8295)..(0.05, 3.796, 7.1099)
  - plane n(0, 0.5729, 0.8196), n·p = 6.8527; extent (0, 1.8469, 5.7075)..(0.05, 3.796, 7.0699)
  - plane n(0, 0.5729, 0.8196), n·p = 6.9527; extent (0, 1.8302, 7.1998)..(0.05, 1.8357, 7.2036)
  - plane n(0, 0.5729, 0.8196), n·p = 8.1627; extent (0, 1.8153, 7.3058)..(0.05, 3.796, 8.6903)
  - plane n(0, 0.5729, 0.8196), n·p = 8.0627; extent (0, 1.6451, 7.2099)..(0.05, 3.7587, 8.6873)
  - plane n(0, 0.5729, 0.8196), n·p = 8.1627; extent (0, 1.6284, 8.7903)..(0.05, 1.6722, 8.8209)
  - plane n(0, -0.7139, -0.7003), n·p = -7.6387; extent (0, 1.5674, 9.2745)..(0.05, 1.6024, 9.3102)
  - plane n(0, 0.7003, -0.7139), n·p = -5.4985; extent (0, 1.6024, 9.2745)..(0.05, 3.2984, 10.9383)
  - plane n(0, 0.7139, 0.7003), n·p = 10.0194; extent (0, 3.2318, 10.9773)..(0.05, 3.2668, 11.013)
  - plane n(0, 0.7003, -0.7139), n·p = -5.5985; extent (0, 1.5596, 9.3726)..(0.05, 3.2318, 11.013)
  - plane n(0, 0, 1), n·p = 8.7903; extent (0, 1.6722, 8.7903)..(0.05, 3.796, 8.7903)
  - plane n(0, 0, 1), n·p = 8.6903; extent (0, 1.8153, 8.6903)..(0.05, 3.796, 8.6903)
  - plane n(0, -1, 0), n·p = -1.8357; extent (0, 1.8357, 7.1998)..(0.05, 1.8357, 7.2099)
  - plane n(0, 0, 1), n·p = 7.1099; extent (0, 1.9643, 7.1099)..(0.05, 3.796, 7.1099)
  - plane n(0, 0, 1), n·p = 4.049; extent (0, 2.2301, 4.049)..(0.05, 3.7184, 4.049)
  - plane n(0, -1, 0), n·p = -2.2301; extent (0, 2.2301, 3.999)..(0.05, 2.2301, 4.049)
  - plane n(0, 0, 1), n·p = 5.6294; extent (0, 2.0329, 5.6294)..(0.05, 3.796, 5.6294)
  - plane n(0, 0, 1), n·p = 2.4686; extent (0, 2.4273, 2.4686)..(0.05, 3.796, 2.4686)
  - plane n(0, -1, 0), n·p = -2.4273; extent (0, 2.4273, 2.4186)..(0.05, 2.4273, 2.4686)
  - plane n(0, 0, 1), n·p = 2.3686; extent (0, 2.4335, 2.3686)..(0.05, 3.796, 2.3686)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 1.5674, 8.7903)..(0.05, 4.091, 10.9383)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 8.7903)..(0.05, 3.796, 9.6706)
  - plane n(0, 0.7003, -0.7139), n·p = 1.286; extent (0, 2.6317, 0.7803)..(0.05, 3.796, 1.9224)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 1.5674, 8.8209)..(0.05, 1.6284, 9.3102)
  - free-form (blend) face; extent (0, 0.1602, 10.3786)..(0.05, 1.434, 13.3514)
  - plane n(0, -0.7769, -0.6296), n·p = -8.5311; extent (0, 0.1349, 13.3514)..(0.05, 0.1602, 13.3826)
  - plane n(0, -0.7003, 0.7139), n·p = 9.4587; extent (0, 0.1349, 13.3826)..(0.05, 0.7942, 14.0293)
  - plane n(0, 0.777, 0.6295), n·p = 9.4485; extent (0, 3.2984, 9.96)..(0.05, 4.091, 10.9383)
  - plane n(0, 0.7003, -0.7139), n·p = -4.2451; extent (0, 3.796, 9.6706)..(0.05, 4.091, 9.96)
  - plane n(0.286, -0.671, 0.684), n·p = 4.0969; extent (0.125, 3.7944, 9.1453)..(2.538, 4.5843, 9.9395)
  - plane n(0.286, -0.671, 0.684), n·p = -1.2031; extent (0.125, 2.5633, 0.1894)..(2.538, 4.2988, 1.9113)
  - plane n(1, 0, 0), n·p = 0.125; extent (0.125, 0.0261, 0.7035)..(0.125, 4.0799, 14.0631)
  - plane n(0.0283, -0.7767, -0.6292), n·p = -9.4197; extent (0.125, 0.7391, 9.4254)..(2.538, 4.5843, 14.0631)
  - plane n(-1, 0, 0), n·p = -2.538; extent (2.538, 0.5305, 0.1894)..(2.538, 4.5843, 13.549)
  - plane n(0.2046, -0.9788, 0), n·p = -3.6886; extent (0.125, 3.7944, 1.3971)..(2.538, 4.2988, 9.6594)
  - plane n(-0.1781, 0.9764, 0.1218), n·p = 2.5664; extent (0, 1.3348, 0)..(2.663, 3.1141, 10.3662)
  - plane n(-0.0282, 0.7766, 0.6294), n·p = 8.4278; extent (2.538, 0.5305, 12.7211)..(2.663, 0.6391, 12.8495)
  - cylinder axis dir(0.9582, 0.2003, -0.2042) through (3.1593, -3.4955, 9.2387) R5.4166; extent (2.538, 0.613, 9.7988)..(2.663, 1.8914, 12.7477)
  - plane n(0.286, -0.671, 0.684), n·p = -1.3281; extent (0, 2.5575, 0)..(2.663, 4.439, 1.8804)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0.5674)..(0, 4.2259, 14.1777)
  - plane n(0.0283, -0.7767, -0.6292), n·p = -9.5447; extent (0, 0.8026, 9.3987)..(2.663, 4.769, 14.1777)
  - plane n(-0.0282, 0.7766, 0.6294), n·p = 8.4278; extent (0, 0, 13.2618)..(0.125, 0.1086, 13.3903)
  - cylinder axis dir(0.9582, 0.2003, -0.2042) through (0.6214, -4.026, 9.7794) R5.4166; extent (0, 0.0825, 10.3396)..(0.125, 1.3609, 13.2885)
  - plane n(0.286, -0.671, 0.684), n·p = 9.1594; extent (0, 0, 12.8229)..(2.663, 1.3593, 14.1777)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 2.4335, 0.7803)..(0.05, 3.796, 2.3686)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 1.9224)..(0.05, 3.796, 2.3686)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 2.4335, 0.7803)..(0.05, 2.6317, 2.3686)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 2.0482, 3.999)..(0.05, 3.7184, 5.4564)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 2.0482, 3.999)..(0.05, 2.2301, 5.4564)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 2.2392, 2.4186)..(0.05, 3.796, 3.9259)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 2.4686)..(0.05, 3.796, 2.6141)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 2.2392, 2.4186)..(0.05, 2.4273, 3.9259)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 1.9643, 5.8295)..(0.05, 3.796, 7.1099)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 5.8295)..(0.05, 3.796, 7.1099)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 1.8153, 7.3058)..(0.05, 3.796, 8.6903)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 7.3058)..(0.05, 3.796, 8.6903)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 0.1349, 9.3726)..(0.05, 3.2668, 14.0293)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 1.434, 9.3726)..(0.05, 1.5596, 10.3786)
  - plane n(0, 0.777, 0.6295), n·p = 9.4485; extent (0, 0.7942, 10.9773)..(0.05, 3.2668, 14.0293)
  - plane n(0, 0, 1), n·p = 7.2099; extent (0, 1.8357, 7.2099)..(0.05, 3.7587, 7.2099)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 1.6451, 7.1998)..(0.05, 3.7587, 8.6873)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 1.6451, 7.2036)..(0.05, 1.8302, 8.6873)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 5.6294)..(0.05, 3.796, 5.7075)
  - plane n(0, -1, 0), n·p = -2.0329; extent (0, 2.0329, 5.6001)..(0.05, 2.0329, 5.6294)
  - plane n(0, 0, 1), n·p = 5.5294; extent (0, 2.1167, 5.5294)..(0.05, 3.796, 5.5294)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 2.1167, 4.1144)..(0.05, 3.796, 5.5294)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 4.1144)..(0.05, 3.796, 5.5294)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 1.8469, 5.6001)..(0.05, 3.796, 7.0699)
  - plane n(0, -0.9923, -0.1238), n·p = -2.7081; extent (0, 1.8469, 5.6025)..(0.05, 2.03, 7.0699)
  - plane n(0, 0, 1), n·p = 3.949; extent (0, 2.367, 3.949)..(0.05, 3.796, 3.949)
  - plane n(-1, 0, 0), n·p = -0.05; extent (0.05, 2.367, 2.7449)..(0.05, 3.796, 3.949)
  - plane n(0, 1, 0), n·p = 3.796; extent (0, 3.796, 2.7449)..(0.05, 3.796, 3.949)
  - plane n(0.286, -0.671, 0.684), n·p = 3.9719; extent (0, 3.896, 9.075)..(2.598, 4.769, 9.9523)
  - plane n(0.2046, -0.9788, 0), n·p = -3.8136; extent (0, 3.896, 1.3269)..(2.598, 4.439, 9.6286)

### P10 Lattice spreader brace, type B (mirror of P09) (2 bodies, 149 faces each)

Mirror image of P09: take P09's local geometry and replace u by (2.6629 - u). Same faces, radii and volume.

### P11 Lower step end shoe, type A (2 bodies, 38 faces each)

Lower step end shoe: an extrusion along local w of the section below (a short ribbed tread with nine R0.075 grooves on the tread face u = 0, two inclined legs and a foot), cut at both ends by planes tilted 5.66 deg (normal (0.0987, 0, -0.9951), n·p = 0 and -3.4829).

Local box: u 0 .. 1.7044, v 0 .. 6.9217, w 0 .. 3.669.

Section at w = 1.8345 (coordinates u, v):
  - loop: (0, 3.4012) – arc c(0, 3.4762) R0.075 via (0.075, 3.4762) – (0, 3.5512) – (0, 3.5872) – arc c(0, 3.6622) R0.075 via (0.075, 3.6622) – (0, 3.7372) – (0, 3.7732) – arc c(0, 3.8482) R0.075 via (0.075, 3.8482) – (0, 3.9232) – (0, 4.5173) – arc c(0, 4.5923) R0.075 via (0.075, 4.5923) – (0, 4.6673) – (0, 4.7033) – arc c(0, 4.7783) R0.075 via (0.075, 4.7783) – (0, 4.8533) – (0, 4.8893) – arc c(0, 4.9643) R0.075 via (0.075, 4.9643) – (0, 5.0393) – (0, 5.0754) – arc c(0, 5.1504) R0.075 via (0.075, 5.1504) – (0, 5.2254) – (0, 5.8194) – arc c(0, 5.8944) R0.075 via (0.075, 5.8944) – (0, 5.9694) – (0, 6.0055) – arc c(0, 6.0805) R0.075 via (0.075, 6.0805) – (0, 6.1555) – (0, 6.4155) – (1.6958, 6.9217) – (1.6958, 6.7073) – (1.6, 6.6787) – (1.6, 6.7887) – (0.1, 6.341) – (0.1, 3.342) – (1.6, 3.7897) – (1.6, 3.8997) – (1.6958, 3.9283) – (1.6958, 3.7139) – (0.1, 3.2376) – (0.1, 0.1044) – (1.6, 0.1044) – (1.6, 0.3544) – (1.7044, 0.3544) – (1.7044, 0) – (0, 0) – (0, 3.4012)
Section at w = 0.0734 (coordinates u, v):
  - loop: (0, 3.4012) – arc c(0, 3.4762) R0.075 via (0.075, 3.4762) – (0, 3.5512) – (0, 3.5872) – arc c(0, 3.6622) R0.075 via (0.075, 3.6622) – (0, 3.7372) – (0, 3.7732) – arc c(0, 3.8482) R0.075 via (0.075, 3.8482) – (0, 3.9232) – (0, 4.5173) – arc c(0, 4.5923) R0.075 via (0.075, 4.5923) – (0, 4.6673) – (0, 4.7033) – arc c(0, 4.7783) R0.075 via (0.075, 4.7783) – (0, 4.8533) – (0, 4.8893) – arc c(0, 4.9643) R0.075 via (0.075, 4.9643) – (0, 5.0393) – (0, 5.0754) – arc c(0, 5.1504) R0.075 via (0.075, 5.1504) – (0, 5.2254) – (0, 5.8194) – arc c(0, 5.8944) R0.075 via (0.075, 5.8944) – (0, 5.9694) – (0, 6.0055) – arc c(0, 6.0805) R0.075 via (0.075, 6.0805) – (0, 6.1555) – (0, 6.4155) – (0.7402, 6.6364) – (0.7402, 6.5321) – (0.1, 6.341) – (0.1, 3.342) – (0.7402, 3.533) – (0.7402, 3.4287) – (0.1, 3.2376) – (0.1, 0.1044) – (0.7402, 0.1044) – (0.7402, 0) – (0, 0) – (0, 3.4012)
Section at w = 3.5956 (coordinates u, v):
  - loop: (0.9642, 0) – (1.7044, 0) – (1.7044, 0.3544) – (1.6, 0.3544) – (1.6, 0.1044) – (0.9642, 0.1044) – (0.9642, 0)
  - loop: (0.9642, 6.7033) – (0.9642, 6.5989) – (1.6, 6.7887) – (1.6, 6.6787) – (1.6958, 6.7073) – (1.6958, 6.9217) – (0.9642, 6.7033)
  - loop: (0.9642, 3.5999) – (0.9642, 3.4955) – (1.6958, 3.7139) – (1.6958, 3.9283) – (1.6, 3.8997) – (1.6, 3.7897) – (0.9642, 3.5999)
Faces not parallel to w (end faces, cuts, cross features):
  - plane n(0.0987, 0, -0.9951), n·p = -3.4829; extent (0, 0, 3.5)..(1.7044, 6.9217, 3.669)
  - plane n(0.0987, 0, -0.9951), n·p = 0; extent (0, 0, 0)..(1.7044, 6.9217, 0.169)

### P12 Lower step end shoe, type B (mirror of P11) (2 bodies, 38 faces each)

Mirror image of P11: take P11's local geometry and replace u by (1.7044 - u). Same faces, radii and volume.

### P13 Ribbed foot pad (4 bodies, 48 faces each)

Ribbed foot pad: a block 0.6 x 1.29 x 3.2999 (u x v x w) with R0.1 rounds on its four edges parallel to u, four transverse grooves R0.25 cut into the bottom face u = 0.6 (axes along v at w = 0.72, 1.34, 1.96, 2.58, axis on the face), R0.0375 rounds along every groove and bottom edge, spherical corners R0.0375.

Local box: u 0 .. 0.6, v 0 .. 1.29, w 0 .. 3.2999.

Section at v = 0.645 (coordinates u, w):
  - loop: (0.5674, 0.9679) – arc c(0.5625, 1.005) R0.0375 via (0.5907, 0.9803) – (0.6, 1.005) – (0.6, 1.0549) – arc c(0.5625, 1.0549) R0.0375 via (0.5907, 1.0797) – (0.5674, 1.0921) – arc c(0.6, 1.34) R0.25 via (0.35, 1.34) – (0.5674, 1.5878) – arc c(0.5625, 1.625) R0.0375 via (0.5907, 1.6003) – (0.6, 1.625) – (0.6, 1.6749) – arc c(0.5625, 1.6749) R0.0375 via (0.5907, 1.6996) – (0.5674, 1.7121) – arc c(0.6, 1.96) R0.25 via (0.35, 1.96) – (0.5674, 2.2078) – arc c(0.5625, 2.245) R0.0375 via (0.5907, 2.2203) – (0.6, 2.245) – (0.6, 2.2949) – arc c(0.5625, 2.2949) R0.0375 via (0.5907, 2.3196) – (0.5674, 2.3321) – arc c(0.6, 2.5799) R0.25 via (0.35, 2.5799) – (0.5674, 2.8278) – arc c(0.5625, 2.865) R0.0375 via (0.5907, 2.8403) – (0.6, 2.865) – (0.6, 3.2624) – arc c(0.5625, 3.2624) R0.0375 via (0.589, 3.2889) – (0.5625, 3.2999) – (0, 3.2999) – (0, 0) – (0.5625, 0) – arc c(0.5625, 0.0375) R0.0375 via (0.589, 0.011) – (0.6, 0.0375) – (0.6, 0.4349) – arc c(0.5625, 0.4349) R0.0375 via (0.5907, 0.4597) – (0.5674, 0.4721) – arc c(0.6, 0.72) R0.25 via (0.35, 0.72) – (0.5674, 0.9679)
Section at u = 0.18 (coordinates v, w):
  - loop: (1.19, 3.2999) – arc c(1.19, 3.1999) R0.1 via (1.2607, 3.2706) – (1.29, 3.1999) – (1.29, 0.1) – arc c(1.19, 0.1) R0.1 via (1.2607, 0.0293) – (1.19, 0) – (0.1, 0) – arc c(0.1, 0.1) R0.1 via (0.0293, 0.0293) – (0, 0.1) – (0, 3.1999) – arc c(0.1, 3.1999) R0.1 via (0.0293, 3.2706) – (0.1, 3.2999) – (1.19, 3.2999)
Face list (all 48 faces):
  - torus axis dir(0, -1, 0) centre (0.6, 1.2525, 0.72) major R0.2875 minor r0.0375; extent (0.3125, 1.2525, 0.4349)..(0.6, 1.29, 1.0075)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 1.005) R0.0375; extent (0.5674, 0.0001, 0.9679)..(0.6, 1.2899, 1.005)
  - sphere centre (0.5625, 1.2525, 0.4349) R0.0375; extent (0.5625, 1.2525, 0.4349)..(0.6, 1.29, 0.4721)
  - torus axis dir(0, 1, 0) centre (0.6, 0.0375, 0.72) major R0.2875 minor r0.0375; extent (0.3125, 0, 0.4349)..(0.6, 0.0375, 1.0075)
  - cylinder axis dir(0, 0, 1) through (0.5625, 1.2525, 0.2675) R0.0375; extent (0.5625, 1.2525, 0.1)..(0.6, 1.29, 0.4349)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 0.4349) R0.0375; extent (0.5674, 0.0375, 0.4349)..(0.6, 1.2525, 0.4721)
  - sphere centre (0.5625, 0.0375, 0.4349) R0.0375; extent (0.5625, 0, 0.4349)..(0.6, 0.0375, 0.4721)
  - torus axis dir(1, 0, 0) centre (0.5625, 1.19, 0.1) major R0.0625 minor r0.0375; extent (0.5625, 1.19, 0)..(0.6, 1.29, 0.1)
  - cylinder axis dir(0, 0, -1) through (0.5625, 0.0375, 0.2675) R0.0375; extent (0.5625, 0, 0.1)..(0.6, 0.0375, 0.4349)
  - cylinder axis dir(0, 1, 0) through (0.5625, 0.645, 0.0375) R0.0375; extent (0.5625, 0.1, 0)..(0.6, 1.19, 0.0375)
  - torus axis dir(1, 0, 0) centre (0.5625, 0.1, 0.1) major R0.0625 minor r0.0375; extent (0.5625, 0, 0)..(0.6, 0.1, 0.1)
  - torus axis dir(0, -1, 0) centre (0.6, 1.2525, 1.34) major R0.2875 minor r0.0375; extent (0.3125, 1.2525, 1.0525)..(0.6, 1.29, 1.6275)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 1.625) R0.0375; extent (0.5674, 0.0001, 1.5878)..(0.6, 1.2899, 1.625)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 1.0549) R0.0375; extent (0.5674, 0.0001, 1.0549)..(0.6, 1.2899, 1.0921)
  - torus axis dir(0, 1, 0) centre (0.6, 0.0375, 1.34) major R0.2875 minor r0.0375; extent (0.3125, 0, 1.0525)..(0.6, 0.0375, 1.6275)
  - torus axis dir(0, -1, 0) centre (0.6, 1.2525, 1.96) major R0.2875 minor r0.0375; extent (0.3125, 1.2525, 1.6725)..(0.6, 1.29, 2.2475)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 2.245) R0.0375; extent (0.5674, 0.0001, 2.2078)..(0.6, 1.2899, 2.245)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 1.6749) R0.0375; extent (0.5674, 0.0001, 1.6749)..(0.6, 1.2899, 1.7121)
  - torus axis dir(0, 1, 0) centre (0.6, 0.0375, 1.96) major R0.2875 minor r0.0375; extent (0.3125, 0, 1.6725)..(0.6, 0.0375, 2.2475)
  - cylinder axis dir(0, 0, 1) through (0.5625, 1.2525, 3.0325) R0.0375; extent (0.5625, 1.2525, 2.865)..(0.6, 1.29, 3.1999)
  - sphere centre (0.5625, 1.2525, 2.865) R0.0375; extent (0.5625, 1.2525, 2.8278)..(0.6, 1.29, 2.865)
  - torus axis dir(1, 0, 0) centre (0.5625, 1.19, 3.1999) major R0.0625 minor r0.0375; extent (0.5625, 1.19, 3.1999)..(0.6, 1.29, 3.2999)
  - torus axis dir(0, -1, 0) centre (0.6, 1.2525, 2.5799) major R0.2875 minor r0.0375; extent (0.3125, 1.2525, 2.2924)..(0.6, 1.29, 2.865)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 2.865) R0.0375; extent (0.5674, 0.0375, 2.8278)..(0.6, 1.2525, 2.865)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 3.2624) R0.0375; extent (0.5625, 0.1, 3.2624)..(0.6, 1.19, 3.2999)
  - cylinder axis dir(0, -1, 0) through (0.5625, 0.645, 2.2949) R0.0375; extent (0.5674, 0.0001, 2.2949)..(0.6, 1.2899, 2.3321)
  - sphere centre (0.5625, 0.0375, 2.865) R0.0375; extent (0.5625, 0, 2.8278)..(0.6, 0.0375, 2.865)
  - torus axis dir(1, 0, 0) centre (0.5625, 0.1, 3.1999) major R0.0625 minor r0.0375; extent (0.5625, 0, 3.1999)..(0.6, 0.1, 3.2999)
  - torus axis dir(0, 1, 0) centre (0.6, 0.0375, 2.5799) major R0.2875 minor r0.0375; extent (0.3125, 0, 2.2924)..(0.6, 0.0375, 2.865)
  - cylinder axis dir(0, 0, -1) through (0.5625, 0.0375, 3.0325) R0.0375; extent (0.5625, 0, 2.865)..(0.6, 0.0375, 3.1999)
  - cylinder axis dir(0, -1, 0) through (0.6, 0.645, 2.5799) R0.25; extent (0.35, 0.0375, 2.3321)..(0.5674, 1.2525, 2.8278)
  - cylinder axis dir(0, -1, 0) through (0.6, 0.645, 1.96) R0.25; extent (0.35, 0.0375, 1.7121)..(0.5674, 1.2525, 2.2078)
  - cylinder axis dir(0, -1, 0) through (0.6, 0.645, 1.34) R0.25; extent (0.35, 0.0375, 1.0921)..(0.5674, 1.2525, 1.5878)
  - cylinder axis dir(0, -1, 0) through (0.6, 0.645, 0.72) R0.25; extent (0.35, 0.0375, 0.4721)..(0.5674, 1.2525, 0.9679)
  - cylinder axis dir(-1, 0, 0) through (0.2812, 1.19, 3.1999) R0.1; extent (0, 1.19, 3.1999)..(0.5625, 1.29, 3.2999)
  - cylinder axis dir(-1, 0, 0) through (0.2812, 1.19, 0.1) R0.1; extent (0, 1.19, 0)..(0.5625, 1.29, 0.1)
  - cylinder axis dir(-1, 0, 0) through (0.2812, 0.1, 0.1) R0.1; extent (0, 0, 0)..(0.5625, 0.1, 0.1)
  - cylinder axis dir(-1, 0, 0) through (0.2812, 0.1, 3.1999) R0.1; extent (0, 0, 3.1999)..(0.5625, 0.1, 3.2999)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.29, 3.2999)
  - plane n(1, 0, 0), n·p = 0.6; extent (0.6, 0.0375, 2.865)..(0.6, 1.2525, 3.2624)
  - plane n(0, 0, 1), n·p = 0; extent (0, 0.1, 0)..(0.5625, 1.19, 0)
  - plane n(0, -1, 0), n·p = -1.29; extent (0, 1.29, 0.1)..(0.6, 1.29, 3.1999)
  - plane n(0, 0, -1), n·p = -3.2999; extent (0, 0.1, 3.2999)..(0.5625, 1.19, 3.2999)
  - plane n(0, 1, 0), n·p = 0; extent (0, 0, 0.1)..(0.6, 0, 3.1999)
  - plane n(1, 0, 0), n·p = 0.6; extent (0.6, 0.0375, 0.0375)..(0.6, 1.2525, 0.4349)
  - plane n(1, 0, 0), n·p = 0.6; extent (0.6, 0, 1.005)..(0.6, 1.29, 1.0549)
  - plane n(1, 0, 0), n·p = 0.6; extent (0.6, 0, 1.625)..(0.6, 1.29, 1.6749)
  - plane n(1, 0, 0), n·p = 0.6; extent (0.6, 0, 2.245)..(0.6, 1.29, 2.2949)

### P14 Rail foot sleeve, type A (2 bodies, 10 faces each)

Rail foot sleeve, a bent sheet 0.0625 thick: a base wall u 0 .. 0.0625 and two flanges (planes n·p = 1.5015 / 1.564 and n·p = -4.6253 / -4.5628 with normals (∓0.0282, ±0.9582, ±0.2846)) reaching u = 1.2439, the whole trimmed by the two end planes with normal (0.0987, 0, -0.9951) (n·p = 0 and -5.25).

Local box: u 0 .. 1.2439, v 0 .. 4.8269, w 0 .. 5.3991.

Section at w = 2.6995 (coordinates u, v):
  - loop: (1.2439, 3.9965) – (1.2439, 4.0617) – (0, 4.0251) – (0, 0.7652) – (1.2439, 0.8018) – (1.2439, 0.867) – (0.0625, 0.8323) – (0.0625, 3.9617) – (1.2439, 3.9965)
Section at v = 2.4135 (coordinates u, w):
  - loop: (0, 5.2757) – (0.0625, 5.2819) – (0.0625, 0.0062) – (0, 0) – (0, 5.2757)
Face list (all 10 faces):
  - plane n(0.0987, 0, -0.9951), n·p = -5.25; extent (0, 0, 5.2757)..(1.2439, 3.2599, 5.3991)
  - plane n(-1, 0, 0), n·p = -1.2439; extent (1.2439, 3.1947, 0.1233)..(1.2439, 4.8269, 5.3991)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 4.8269, 5.2757)
  - plane n(0.0282, -0.9582, -0.2846), n·p = -4.6253; extent (0, 3.2599, 0)..(1.2439, 4.8269, 5.3991)
  - plane n(-1, 0, 0), n·p = -1.2439; extent (1.2439, 0, 0.1233)..(1.2439, 1.6322, 5.3991)
  - plane n(-0.0282, 0.9582, 0.2846), n·p = 1.5015; extent (0, 0, 0)..(1.2439, 1.567, 5.3991)
  - plane n(1, 0, 0), n·p = 0.0625; extent (0.0625, 0.0652, 0.0062)..(0.0625, 4.7617, 5.2819)
  - plane n(0.0282, -0.9582, -0.2846), n·p = -4.5628; extent (0.0625, 3.1947, 0.0062)..(1.2439, 4.7617, 5.3991)
  - plane n(-0.0282, 0.9582, 0.2846), n·p = 1.564; extent (0.0625, 0.0652, 0.0062)..(1.2439, 1.6322, 5.3991)
  - plane n(0.0987, 0, -0.9951), n·p = 0; extent (0, 1.567, 0)..(1.2439, 4.8269, 0.1233)

### P15 Rail foot sleeve, type B (mirror of P14) (2 bodies, 10 faces each)

Mirror image of P14: take P14's local geometry and replace u by (1.2439 - u). Same faces, radii and volume.

### P16 Top cap side plate, type A (1 bodies, 50 faces each)

Top cap side plate (pressed sheet 0.0995 thick, faces u = 0 and u ≈ 0.0995) with one hole R0.25, four raised round bosses (torus R0.2706 / r0.075 and R0.1125 / r0.1 around centres (v, w) = (0.5801, 3.027), (1.1207, 1.2071), (2.4786, 3.027), (3.0192, 1.2071)) and a bent edge flange whose bends are free-form blends.

Local box: u 0 .. 0.1995, v 0 .. 5.4646, w 0 .. 3.5308.

Section at u = 0.0499 (coordinates v, w):
  - loop: (1.7997, 1.867) – arc c(1.7997, 2.117) R0.25 via (2.0497, 2.117) – (1.7997, 2.367) – arc c(1.7997, 2.117) R0.25 via (1.5497, 2.117) – (1.7997, 1.867)
  - loop: (0.2, 3.5221) – arc c(0.2005, 3.3216) R0.2005 via (0.0586, 3.4632) – (0, 3.3211) – arc c(0.2019, 3.3211) R0.2019 via (0.0021, 3.2921) – (0.0084, 3.2636) – (0.9336, 0.1484) – arc c(1.1256, 0.2051) R0.2001 via (1.0058, 0.0448) – (1.1253, 0.0049) – (4.2415, 0.0049) – arc c(4.2415, 0.2042) R0.1992 via (4.288, 0.0104) – (4.3319, 0.0266) – arc c(6.2955, 2.5144) R3.1694 via (3.2561, 1.6161) – (3.2885, 3.5157) – arc c(3.2385, 3.323) R0.1991 via (3.2637, 3.5205) – (3.2385, 3.5221) – (0.2, 3.5221)
Face list (all 50 faces):
  - torus axis dir(-1, 0, 0) centre (0.1745, 1.1207, 1.2071) major R0.2706 minor r0.075; extent (0.0995, 1.1207, 0.9364)..(0.1424, 1.3913, 1.4777)
  - torus axis dir(-1, 0, 0) centre (0.1745, 0.5801, 3.027) major R0.2706 minor r0.075; extent (0.0995, 0.5801, 2.7564)..(0.1424, 0.8507, 3.2976)
  - torus axis dir(-1, 0, 0) centre (0.1745, 2.4786, 3.027) major R0.2706 minor r0.075; extent (0.0995, 2.4786, 2.7564)..(0.1424, 2.7493, 3.2976)
  - torus axis dir(-1, 0, 0) centre (0.1745, 3.0192, 1.2071) major R0.2706 minor r0.075; extent (0.0995, 3.0192, 1.3939)..(0.1424, 3.1245, 1.4777)
  - torus axis dir(-1, 0, 0) centre (0.1745, 3.0192, 1.2071) major R0.2706 minor r0.075; extent (0.0995, 2.7486, 0.9364)..(0.1424, 3.0192, 1.4777)
  - torus axis dir(1, 0, 0) centre (0.0995, 3.0192, 1.2071) major R0.1125 minor r0.1; extent (0.1424, 2.8164, 1.0042)..(0.1995, 3.0192, 1.4099)
  - torus axis dir(1, 0, 0) centre (0.0995, 3.0192, 1.2071) major R0.1125 minor r0.1; extent (0.1424, 3.0192, 1.294)..(0.1995, 3.1464, 1.4099)
  - torus axis dir(1, 0, 0) centre (0.0995, 2.4786, 3.027) major R0.1125 minor r0.1; extent (0.1424, 2.2758, 2.8242)..(0.1995, 2.4786, 3.2299)
  - torus axis dir(1, 0, 0) centre (0.0995, 1.1207, 1.2071) major R0.1125 minor r0.1; extent (0.1424, 0.9178, 1.0042)..(0.1995, 1.1207, 1.4099)
  - torus axis dir(1, 0, 0) centre (0.0995, 0.5801, 3.027) major R0.1125 minor r0.1; extent (0.1424, 0.3772, 2.8242)..(0.1995, 0.5801, 3.2299)
  - cylinder axis dir(1, 0, 0) through (0.0498, 1.7997, 2.117) R0.25; extent (0, 1.7997, 1.867)..(0.0995, 2.0497, 2.367)
  - cylinder axis dir(0.9951, 0, 0.0987) through (0.0596, 0.2, 3.3221) R0.2; extent (0, 0, 3.3162)..(0.0995, 0.2, 3.527)
  - free-form (blend) face; extent (0.1094, 3.1464, 1.3456)..(0.1503, 3.2401, 1.4219)
  - free-form (blend) face; extent (0.1143, 3.1616, 1.2046)..(0.1549, 3.3139, 1.4024)
  - free-form (blend) face; extent (0.0995, 3.0981, 1.3618)..(0.1474, 3.2143, 1.4564)
  - free-form (blend) face; extent (0.1094, 3.2179, 1.1824)..(0.1503, 3.3139, 1.2174)
  - free-form (blend) face; extent (0.0995, 3.2051, 1.0987)..(0.1474, 3.3086, 1.1872)
  - free-form (blend) face; extent (0.1474, 3.0907, 1.1824)..(0.1995, 3.2182, 1.3618)
  - plane n(1, 0, 0), n·p = 0.1995; extent (0.1995, 1.0082, 1.0946)..(0.1995, 1.2332, 1.3196)
  - plane n(1, 0, 0), n·p = 0.1995; extent (0.1995, 2.9067, 1.0946)..(0.1995, 3.1317, 1.3196)
  - plane n(1, 0, 0), n·p = 0.1995; extent (0.1995, 2.3661, 2.9145)..(0.1995, 2.5911, 3.1395)
  - plane n(1, 0, 0), n·p = 0.1995; extent (0.1995, 0.4676, 2.9145)..(0.1995, 0.6926, 3.1395)
  - cylinder axis dir(0.9951, 0, 0.0987) through (0.0371, 1.1253, 0.2047) R0.2; extent (0, 0.9336, 0)..(0.0995, 1.1253, 0.1534)
  - cylinder axis dir(0.9951, 0, 0.0987) through (0.1191, 3.2385, 3.328) R0.2; extent (0.0267, 3.2385, 3.4946)..(0.1748, 3.3431, 3.5308)
  - cylinder axis dir(0.9951, 0, 0.0987) through (0.0843, 4.2415, 0.2093) R0.2; extent (0.0158, 4.2415, 0.0016)..(0.1846, 4.3997, 0.0963)
  - free-form (blend) face; extent (0.0327, 3.0897, 0.0103)..(0.099, 4.4899, 3.52)
  - free-form (blend) face; extent (0, 2.9697, 0)..(0.0327, 4.2939, 3.52)
  - plane n(1, 0, 0), n·p = 0.099; extent (0.099, 3.364, 0.2049)..(0.099, 5.4646, 3.4001)
  - free-form (blend) face; extent (0.1216, 3.044, 0.0121)..(0.199, 4.4851, 3.5308)
  - plane n(-1, 0, 0), n·p = -0.0995; extent (0.0995, 0, 0.0099)..(0.0995, 4.0814, 3.527)
  - plane n(0.0987, 0, -0.9951), n·p = 0; extent (0, 1.1253, 0)..(0.129, 4.2415, 0.0128)
  - plane n(0.0282, -0.9582, -0.2846), n·p = -0.9355; extent (0, 0.0084, 0.1435)..(0.0995, 0.9336, 3.2686)
  - plane n(-0.0987, 0, 0.9951), n·p = 3.5; extent (0, 0.2, 3.5172)..(0.1362, 3.2385, 3.5307)
  - plane n(-0.0841, 0.5227, 0.8484), n·p = 4.7061; extent (0.0716, 3.3431, 2.3023)..(0.199, 5.2828, 3.5049)
  - plane n(1, 0, 0), n·p = 0.199; extent (0.199, 3.364, 0.2087)..(0.199, 5.4646, 3.4084)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 4.1186, 3.5172)
  - free-form (blend) face; extent (0.099, 5.2828, 1.2345)..(0.199, 5.4646, 2.3122)
  - plane n(0.0604, 0.7908, -0.609), n·p = 3.4319; extent (0.0802, 4.3997, 0.0859)..(0.199, 5.2828, 1.2444)
  - free-form (blend) face; extent (0.0995, 3.2672, 0.0099)..(0.1216, 4.2193, 1.2174)
  - free-form (blend) face; extent (0.0995, 2.9526, 1.4024)..(0.1216, 3.2401, 3.5292)
  - cylinder axis dir(0.9951, 0, 0.0987) through (0.0469, 0.2, 3.3208) R0.2; extent (0, 0, 3.2587)..(0.0995, 0.0084, 3.326)
  - cylinder axis dir(1, 0, 0) through (0.0498, 1.7997, 2.117) R0.25; extent (0, 1.5497, 1.867)..(0.0995, 1.7997, 2.367)
  - torus axis dir(1, 0, 0) centre (0.0995, 0.5801, 3.027) major R0.1125 minor r0.1; extent (0.1424, 0.5801, 2.8242)..(0.1995, 0.7829, 3.2299)
  - torus axis dir(1, 0, 0) centre (0.0995, 1.1207, 1.2071) major R0.1125 minor r0.1; extent (0.1424, 1.1207, 1.0042)..(0.1995, 1.3235, 1.4099)
  - torus axis dir(1, 0, 0) centre (0.0995, 2.4786, 3.027) major R0.1125 minor r0.1; extent (0.1424, 2.4786, 2.8242)..(0.1995, 2.6815, 3.2299)
  - torus axis dir(1, 0, 0) centre (0.0995, 3.0192, 1.2071) major R0.1125 minor r0.1; extent (0.1424, 3.0192, 1.0042)..(0.1995, 3.218, 1.1932)
  - torus axis dir(-1, 0, 0) centre (0.1745, 3.0192, 1.2071) major R0.2706 minor r0.075; extent (0.0995, 3.0192, 0.9364)..(0.1424, 3.2672, 1.1258)
  - torus axis dir(-1, 0, 0) centre (0.1745, 2.4786, 3.027) major R0.2706 minor r0.075; extent (0.0995, 2.208, 2.7564)..(0.1424, 2.4786, 3.2976)
  - torus axis dir(-1, 0, 0) centre (0.1745, 0.5801, 3.027) major R0.2706 minor r0.075; extent (0.0995, 0.3095, 2.7564)..(0.1424, 0.5801, 3.2976)
  - torus axis dir(-1, 0, 0) centre (0.1745, 1.1207, 1.2071) major R0.2706 minor r0.075; extent (0.0995, 0.85, 0.9364)..(0.1424, 1.1207, 1.4777)

### P17 Top cap side plate, type A, mirror (B) (1 bodies, 50 faces each)

Mirror image of P16: take P16's local geometry and replace u by (0.1995 - u). Same faces, radii and volume.

### P18 Top cap side plate, second form (1 bodies, 33 faces each)

Top cap side plate, second form (sheet 0.099 thick, faces u = 0 and u = 0.099) with one hole R0.25 and four raised round bosses (centres (v, w) = (0.5028, 2.0494), (0.5028, 3.948), (2.3227, 1.5089), (2.3227, 3.4074); boss tops plane u = 0.199).

Local box: u 0 .. 0.199, v 0 .. 4.8657, w 0 .. 4.5489.

Section at u = 0.0497 (coordinates v, w):
  - loop: (1.3416, 2.4888) – arc c(1.4127, 2.7284) R0.25 via (1.6524, 2.6572) – (1.4839, 2.9681) – arc c(1.4127, 2.7284) R0.25 via (1.1731, 2.7996) – (1.3416, 2.4888)
  - loop: (4.4833, 0.8862) – (3.1823, 0) – arc c(3.1891, 0.1741) R0.1742 via (3.1606, 0.0022) – (3.1395, 0.0071) – (0.125, 0.9024) – arc c(0.1751, 1.0702) R0.1751 via (0.0347, 0.9656) – (0, 1.0705) – (0, 4.3727) – arc c(0.1757, 4.3731) R0.1757 via (0.0705, 4.5138) – (0.2251, 4.5417) – (3.2071, 3.656) – (4.615, 2.2224) – arc c(3.9907, 1.6093) R0.875 via (4.8615, 1.5235) – (4.4833, 0.8862)
Face list (all 33 faces):
  - torus axis dir(1, 0, 0) centre (0.174, 2.3227, 1.5089) major R0.2706 minor r0.075; extent (0.099, 2.2457, 1.2382)..(0.1419, 2.5933, 1.7683)
  - torus axis dir(1, 0, 0) centre (0.174, 0.5028, 2.0494) major R0.2706 minor r0.075; extent (0.099, 0.4257, 1.7788)..(0.1419, 0.7734, 2.3088)
  - torus axis dir(1, 0, 0) centre (0.174, 2.3227, 3.4074) major R0.2706 minor r0.075; extent (0.099, 2.2457, 3.1368)..(0.1419, 2.5933, 3.6668)
  - torus axis dir(1, 0, 0) centre (0.174, 0.5028, 3.948) major R0.2706 minor r0.075; extent (0.099, 0.4257, 3.6773)..(0.1419, 0.7734, 4.2074)
  - torus axis dir(1, 0, 0) centre (0.099, 0.5028, 2.0494) major R0.1125 minor r0.1; extent (0.1419, 0.2999, 1.855)..(0.199, 0.5605, 2.2523)
  - torus axis dir(1, 0, 0) centre (0.099, 2.3227, 1.5089) major R0.1125 minor r0.1; extent (0.1419, 2.1199, 1.3144)..(0.199, 2.3805, 1.7117)
  - torus axis dir(1, 0, 0) centre (0.099, 2.3227, 3.4074) major R0.1125 minor r0.1; extent (0.1419, 2.1199, 3.2129)..(0.199, 2.3805, 3.6102)
  - torus axis dir(1, 0, 0) centre (0.099, 0.5028, 3.948) major R0.1125 minor r0.1; extent (0.1419, 0.2999, 3.7535)..(0.199, 0.5605, 4.1508)
  - cylinder axis dir(1, 0, 0) through (0.0495, 1.4127, 2.7284) R0.25; extent (0, 1.3416, 2.4784)..(0.099, 1.6627, 2.9681)
  - plane n(1, 0, 0), n·p = 0.199; extent (0.199, 2.2102, 1.3964)..(0.199, 2.4352, 1.6214)
  - plane n(1, 0, 0), n·p = 0.199; extent (0.199, 0.3903, 1.9369)..(0.199, 0.6153, 2.1619)
  - plane n(1, 0, 0), n·p = 0.199; extent (0.199, 0.3903, 3.8355)..(0.199, 0.6153, 4.0605)
  - plane n(1, 0, 0), n·p = 0.199; extent (0.199, 2.2102, 3.2949)..(0.199, 2.4352, 3.5199)
  - plane n(0, 0.5629, -0.8265), n·p = 1.7915; extent (0, 3.1823, 0)..(0.099, 4.4833, 0.8862)
  - free-form (blend) face; extent (0, 3.1395, 0)..(0.099, 3.1823, 0.0071)
  - plane n(0, 0.2847, 0.9586), n·p = 0.9007; extent (0, 0.125, 0.0071)..(0.099, 3.1395, 0.9024)
  - free-form (blend) face; extent (0, 0, 0.9024)..(0.099, 0.125, 1.0705)
  - plane n(0, 1, 0), n·p = 0; extent (0, 0, 1.0705)..(0.099, 0, 4.3727)
  - free-form (blend) face; extent (0, 0, 4.3727)..(0.099, 0.2251, 4.5489)
  - plane n(0, -0.2847, -0.9586), n·p = -4.4178; extent (0, 0.2251, 3.656)..(0.099, 3.2071, 4.5417)
  - plane n(0, -0.7135, -0.7007), n·p = -4.8499; extent (0, 3.2071, 2.2224)..(0.099, 4.615, 3.656)
  - cylinder axis dir(-1, 0, 0) through (0.0495, 3.9907, 1.6093) R0.875; extent (0, 4.4833, 0.8862)..(0.099, 4.8657, 2.2224)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 4.8657, 4.5489)
  - plane n(1, 0, 0), n·p = 0.099; extent (0.099, 0, 0)..(0.099, 4.8657, 4.5489)
  - cylinder axis dir(1, 0, 0) through (0.0495, 1.4127, 2.7284) R0.25; extent (0, 1.1627, 2.4888)..(0.099, 1.4839, 2.9784)
  - torus axis dir(1, 0, 0) centre (0.099, 0.5028, 3.948) major R0.1125 minor r0.1; extent (0.1419, 0.445, 3.7451)..(0.199, 0.7056, 4.1424)
  - torus axis dir(1, 0, 0) centre (0.099, 2.3227, 3.4074) major R0.1125 minor r0.1; extent (0.1419, 2.265, 3.2045)..(0.199, 2.5256, 3.6019)
  - torus axis dir(1, 0, 0) centre (0.099, 2.3227, 1.5089) major R0.1125 minor r0.1; extent (0.1419, 2.265, 1.306)..(0.199, 2.5256, 1.7033)
  - torus axis dir(1, 0, 0) centre (0.099, 0.5028, 2.0494) major R0.1125 minor r0.1; extent (0.1419, 0.445, 1.8466)..(0.199, 0.7056, 2.2439)
  - torus axis dir(1, 0, 0) centre (0.174, 0.5028, 3.948) major R0.2706 minor r0.075; extent (0.099, 0.2321, 3.6885)..(0.1419, 0.5798, 4.2186)
  - torus axis dir(1, 0, 0) centre (0.174, 2.3227, 3.4074) major R0.2706 minor r0.075; extent (0.099, 2.0521, 3.148)..(0.1419, 2.3998, 3.678)
  - torus axis dir(1, 0, 0) centre (0.174, 0.5028, 2.0494) major R0.2706 minor r0.075; extent (0.099, 0.2321, 1.79)..(0.1419, 0.5798, 2.32)
  - torus axis dir(1, 0, 0) centre (0.174, 2.3227, 1.5089) major R0.2706 minor r0.075; extent (0.099, 2.0521, 1.2494)..(0.1419, 2.3998, 1.7795)

### P19 Top cap side plate, second form, mirror (1 bodies, 33 faces each)

Mirror image of P18: take P18's local geometry and replace u by (0.199 - u). Same faces, radii and volume.

### P20 Rail top cap, type A (2 bodies, 17 faces each)

Rail top cap: a bent channel-like cap 0.0575 / 0.1 thick around the rail top with one cross hole R0.175 (three cylinder faces on the same axis).

Local box: u 0 .. 1.2439, v 0 .. 3.2746, w 0 .. 4.6266.

Section at w = 2.3133 (coordinates u, v):
  - loop: (0.0575, 0.0166) – (0, 0.015) – (0, 3.2122) – (1.2439, 3.2473) – (1.2439, 3.1473) – (0.1, 3.115) – (0.1, 3.0984) – (0.0575, 3.0984) – (0.0575, 0.0166)
Section at w = 0.4627 (coordinates u, v):
  - loop: (0.0575, 0.0045) – (0, 0.0029) – (0, 1.238) – (1.2439, 1.6918) – (1.2439, 1.322) – (0.1, 0.9047) – (0.0575, 0.9047) – (0.0575, 0.0045)
Section at u = 0.622 (coordinates v, w):
  - loop: (3.2512, 4.439) – arc c(3.0815, 4.3912) R0.1762 via (3.2172, 4.5038) – (3.1599, 4.5491) – (3.1124, 1.0323) – (0.0181, 0.1585) – (0.0168, 0.0593) – arc c(0.0123, 0.2335) R0.1742 via (0.0384, 0.0612) – (0.0596, 0.0658) – (3.086, 0.9204) – arc c(3.0381, 1.0889) R0.1751 via (3.1771, 0.9824) – (3.2132, 1.0868) – (3.2578, 4.3886) – arc c(3.0811, 4.391) R0.1767 via (3.2563, 4.4141) – (3.2512, 4.439)
Face list (all 17 faces):
  - cylinder axis dir(-0.9951, -0.0268, 0.0949) through (0.613, 3.0825, 4.3923) R0.175; extent (0, 3.0182, 4.3797)..(1.2439, 3.2679, 4.6266)
  - plane n(0.0282, -0.9995, 0.0135), n·p = 0.0016; extent (0, 0, 0)..(1.2439, 0.0349, 0.2179)
  - plane n(0.0276, -0.9996, 0.0065), n·p = 0.0001; extent (0, 0.0013, 0.2124)..(0.0575, 0.0261, 3.7747)
  - cylinder axis dir(-0.9951, -0.0268, 0.0949) through (0.6331, 3.0385, 1.0886) R0.175; extent (0, 3.0692, 0.8611)..(1.2439, 3.23, 1.1462)
  - plane n(0, 1, 0), n·p = 3.0984; extent (0.0575, 3.0984, 1.0821)..(0.1, 3.0984, 4.6183)
  - plane n(0.0282, -0.9995, 0.0135), n·p = -3.0794; extent (0.1, 3.0984, 0.973)..(1.2439, 3.1767, 4.5989)
  - plane n(1, 0, 0), n·p = 0.1; extent (0.1, 3.0984, 1.0821)..(0.1, 3.1458, 4.6144)
  - plane n(0.0282, -0.9995, 0.0135), n·p = -3.1794; extent (0, 3.1965, 1.0275)..(1.2439, 3.2745, 4.448)
  - plane n(-0.0987, 0.2704, -0.9577), n·p = -0.1083; extent (0, 0.0429, 0.0065)..(1.2439, 3.1027, 0.9798)
  - cylinder axis dir(0.9951, 0.0268, -0.0949) through (0.639, 0.0123, 0.2334) R0.175; extent (0, 0, 0)..(1.2439, 0.0764, 0.1252)
  - plane n(0, 0.2718, -0.9624), n·p = -0.1994; extent (0.0575, 0.0028, 0.208)..(0.1, 3.0984, 1.0821)
  - plane n(1, 0, 0), n·p = 0.0575; extent (0.0575, 0.0028, 0.208)..(0.0575, 3.0984, 4.6211)
  - plane n(-0.0987, 0.2704, -0.9577), n·p = -0.2083; extent (0.1, 0.004, 0.0992)..(1.2439, 3.1292, 1.0821)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0.1187)..(0, 3.241, 4.6266)
  - plane n(-1, 0, 0), n·p = -1.2439; extent (1.2439, 0.0335, 0)..(1.2439, 3.2746, 4.4897)
  - plane n(-0.0987, 0.2704, -0.9577), n·p = -3.6083; extent (0, 0.0246, 3.7692)..(0.0575, 3.0197, 4.6201)
  - cylinder axis dir(-0.9951, -0.0268, 0.0949) through (0.6244, 3.0828, 4.3912) R0.175; extent (0, 3.2344, 4.3293)..(1.2439, 3.2746, 4.4984)

### P21 Rail top cap, type B (mirror of P20) (2 bodies, 17 faces each)

Mirror image of P20: take P20's local geometry and replace u by (1.2439 - u). Same faces, radii and volume.

### P22 Step brace strap (12 bodies, 6 faces each)

Flat brace strap 0.15 thick (u 0 .. 0.15), outline in (v, w) a quadrilateral with two parallel long sides v = 0 and v = 1.1875.

Local box: u 0 .. 0.15, v 0 .. 1.1875, w 0 .. 7.9635.

Section at u = 0.075 (coordinates v, w):
  - loop: (1.1875, 6.7957) – (0, 7.9635) – (0, 0) – (1.1875, 1.4616) – (1.1875, 6.7957)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0.15; extent (0.15, 0, 0)..(0.15, 1.1875, 7.9635)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.1875, 7.9635)

### P23 Platform support angle (2 bodies, 14 faces each)

Equal angle 0.75 x 0.75 x 0.05 along local w (legs u 0.7 .. 0.75 and v 0.7 .. 0.75), both ends bevelled by planes with normals (0, 0.286, ±0.9582); in the middle (w 8.0996 .. 8.5996) the leg v 0.7 .. 0.75 and the part of the other leg above v = 0.4 are cut away.

Local box: u 0 .. 0.75, v 0 .. 0.75, w 0 .. 16.6993.

Section at w = 4.1748 (coordinates u, v):
  - loop: (0, 0.7) – (0, 0.75) – (0.75, 0.75) – (0.75, 0) – (0.7, 0) – (0.7, 0.7) – (0, 0.7)
Section at w = 8.3496 (coordinates u, v):
  - loop: (0.75, 0.4) – (0.7, 0.4) – (0.7, 0) – (0.75, 0) – (0.75, 0.4)
Face list (all 14 faces):
  - plane n(0, 0, -1), n·p = -8.0996; extent (0, 0.4, 8.0996)..(0.75, 0.75, 8.0996)
  - plane n(0, 0, 1), n·p = 8.5996; extent (0, 0.4, 8.5996)..(0.75, 0.75, 8.5996)
  - plane n(0, -1, 0), n·p = -0.4; extent (0.7, 0.4, 8.0996)..(0.75, 0.4, 8.5996)
  - plane n(0, 0.286, 0.9582), n·p = 16.0017; extent (0, 0, 16.4754)..(0.75, 0.75, 16.6993)
  - plane n(0, 0.286, -0.9582), n·p = 0; extent (0, 0, 0)..(0.75, 0.75, 0.2239)
  - plane n(-1, 0, 0), n·p = 0; extent (0, 0.7, 0.2089)..(0, 0.75, 8.0996)
  - plane n(0, -1, 0), n·p = -0.7; extent (0, 0.7, 0.2089)..(0.7, 0.7, 8.0996)
  - plane n(-1, 0, 0), n·p = -0.7; extent (0.7, 0, 0)..(0.7, 0.7, 16.6993)
  - plane n(0, -1, 0), n·p = 0; extent (0.7, 0, 0)..(0.75, 0, 16.6993)
  - plane n(1, 0, 0), n·p = 0.75; extent (0.75, 0, 0)..(0.75, 0.75, 16.6993)
  - plane n(0, 1, 0), n·p = 0.75; extent (0, 0.75, 0.2239)..(0.75, 0.75, 8.0996)
  - plane n(-1, 0, 0), n·p = 0; extent (0, 0.7, 8.5996)..(0, 0.75, 16.4903)
  - plane n(0, -1, 0), n·p = -0.7; extent (0, 0.7, 8.5996)..(0.7, 0.7, 16.4903)
  - plane n(0, 1, 0), n·p = 0.75; extent (0, 0.75, 8.5996)..(0.75, 0.75, 16.4754)

### P24 Foot plate, sharp corners (1 bodies, 6 faces each)

Flat plate 0.15 x 1.29 x 3.2999 with sharp corners.

Local box: u 0 .. 0.15, v 0 .. 1.29, w 0 .. 3.2999.

Section at u = 0.075 (coordinates v, w):
  - loop: (0, 3.2999) – (0, 0) – (1.29, 0) – (1.29, 3.2999) – (0, 3.2999)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.29, 3.2999)
  - plane n(1, 0, 0), n·p = 0.15; extent (0.15, 0, 0)..(0.15, 1.29, 3.2999)

### P25 Foot plate, rounded corners (3 bodies, 10 faces each)

Flat plate 0.15 x 1.29 x 3.2999 with R0.1 corners (outline in (v, w)).

Local box: u 0 .. 0.15, v 0 .. 1.29, w 0 .. 3.2999.

Section at u = 0.075 (coordinates v, w):
  - loop: (1.29, 0.1) – arc c(1.19, 0.1) R0.1 via (1.2607, 0.0293) – (1.19, 0) – (0.1, 0) – arc c(0.1, 0.1) R0.1 via (0.0293, 0.0293) – (0, 0.1) – (0, 3.1999) – arc c(0.1, 3.1999) R0.1 via (0.0293, 3.2706) – (0.1, 3.2999) – (1.19, 3.2999) – arc c(1.19, 3.1999) R0.1 via (1.2607, 3.2706) – (1.29, 3.1999) – (1.29, 0.1)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.29, 3.2999)
  - plane n(1, 0, 0), n·p = 0.15; extent (0.15, 0, 0)..(0.15, 1.29, 3.2999)

### P26 Platform lock casting, type A (1 bodies, 38 faces each)

Platform lock casting: a block 0.45 thick in u with a round boss R0.625 (cylinder axis along u), a stepped round recess (cone 30 deg half-angle, tori) on the u = 0 side, rounded outline arcs R0.1797 / R0.4393 and R0.015 edge rounds; the complete face list follows.

Local box: u 0 .. 0.45, v 0 .. 1.4078, w -0.0219 .. 2.2177.

Section at w = 1.0979 (coordinates u, v):
  - loop: (0.45, 0.1531) – blend curve via (0.4439, 0.131) – (0.435, 0.1252) – (0.14, 0.1252) – blend curve via (0.1311, 0.131) – (0.125, 0.1531) – (0.125, 0.6669) – blend curve via (0.1211, 0.7818) – (0.125, 0.8987) – (0.125, 1.1395) – blend curve via (0.1305, 1.159) – (0.14, 1.1646) – (0.435, 1.1646) – blend curve via (0.4445, 1.159) – (0.45, 1.1395) – (0.45, 0.1531)
Section at u = 0.225 (coordinates v, w):
  - loop: (0.2089, 0.8508) – arc c(0.7828, 0.6031) R0.625 via (0.3106, 0.1936) – (0.9468, 0) – arc c(0.7828, 0.6031) R0.625 via (1.4034, 0.6767) – (0.8013, 1.2278) – arc c(0.8138, 1.6519) R0.4243 via (0.5094, 1.3564) – (0.3895, 1.6519) – (0.3895, 2.0229) – arc c(0.1947, 2.0229) R0.1947 via (0.1947, 2.2177) – (0, 2.0229) – (0, 1.2809) – arc c(0.1947, 1.2809) R0.1947 via (0.0305, 1.1763) – (0.1124, 1.1044) – arc c(0.0301, 0.9279) R0.1947 via (0.2122, 0.9972) – (0.2089, 0.8508)
Face list (all 38 faces):
  - torus axis dir(1, 0, 0) centre (0.435, 0.7828, 0.6031) major R0.61 minor r0.015; extent (0.435, 0.1578, -0.0219)..(0.45, 0.9468, 0.8508)
  - torus axis dir(1, 0, 0) centre (0.14, 0.7828, 0.6031) major R0.61 minor r0.015; extent (0.125, 0.1578, -0.0219)..(0.14, 0.9468, 0.8508)
  - torus axis dir(1, 0, 0) centre (0.1, 0.7828, 0.6031) major R0.5082 minor r0.025; extent (0.1125, 0.2746, 0.0949)..(0.125, 0.9162, 1.0935)
  - torus axis dir(-1, 0, 0) centre (0.05, 0.7828, 0.6031) major R0.1125 minor r0.025; extent (0.05, 0.6703, 0.4906)..(0.075, 0.8123, 0.7116)
  - torus axis dir(-1, 0, 0) centre (0.1, 0.7828, 0.6031) major R0.4504 minor r0.025; extent (0.075, 0.6589, 0.1475)..(0.0875, 1.2549, 1.0752)
  - torus axis dir(-1, 0, 0) centre (0.05, 0.7828, 0.6031) major R0.0375 minor r0.05; extent (0, 0.7598, 0.5187)..(0.05, 0.8703, 0.6906)
  - cone axis dir(1, 0, 0) through (0.1, 0.7828, 0.6031) R0.4938, half-angle 30 deg; extent (0.0875, 0.2962, 0.1166)..(0.1125, 0.9105, 1.0726)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.7828, 0.6031) R0.625; extent (0.14, 0.1578, -0.0219)..(0.435, 0.9468, 0.8508)
  - torus axis dir(1, 0, 0) centre (0.435, 0.0301, 0.9279) major R0.2097 minor r0.015; extent (0.435, 0.1124, 0.8448)..(0.45, 0.2399, 1.118)
  - torus axis dir(1, 0, 0) centre (0.435, 0.1947, 1.2809) major R0.1797 minor r0.015; extent (0.435, 0, 1.1044)..(0.45, 0.1188, 1.2809)
  - torus axis dir(1, 0, 0) centre (0.435, 0.8138, 1.6519) major R0.4393 minor r0.015; extent (0.435, 0.3745, 1.2128)..(0.45, 0.8013, 1.6519)
  - cylinder axis dir(0, 0, 1) through (0.435, 0.015, 1.6519) R0.015; extent (0.435, 0, 1.2809)..(0.45, 0.015, 2.0229)
  - cylinder axis dir(0, 0, -1) through (0.435, 0.3745, 1.8374) R0.015; extent (0.435, 0.3745, 1.6519)..(0.45, 0.3895, 2.0229)
  - torus axis dir(1, 0, 0) centre (0.435, 0.1947, 2.0229) major R0.1797 minor r0.015; extent (0.435, 0, 2.0229)..(0.45, 0.3895, 2.2177)
  - torus axis dir(1, 0, 0) centre (0.14, 0.0301, 0.9279) major R0.2097 minor r0.015; extent (0.125, 0.1124, 0.8448)..(0.14, 0.2399, 1.118)
  - torus axis dir(1, 0, 0) centre (0.14, 0.1947, 1.2809) major R0.1797 minor r0.015; extent (0.125, 0, 1.1044)..(0.14, 0.1188, 1.2809)
  - torus axis dir(1, 0, 0) centre (0.14, 0.8138, 1.6519) major R0.4393 minor r0.015; extent (0.125, 0.3745, 1.2128)..(0.14, 0.8013, 1.6519)
  - cylinder axis dir(0, 0, -1) through (0.14, 0.015, 1.6519) R0.015; extent (0.125, 0, 1.2809)..(0.14, 0.015, 2.0229)
  - cylinder axis dir(0, 0, 1) through (0.14, 0.3745, 1.8374) R0.015; extent (0.125, 0.3745, 1.6519)..(0.14, 0.3895, 2.0229)
  - torus axis dir(1, 0, 0) centre (0.14, 0.1947, 2.0229) major R0.1797 minor r0.015; extent (0.125, 0, 2.0229)..(0.14, 0.3895, 2.2177)
  - plane n(-1, 0, 0), n·p = 0; extent (0, 0.7453, 0.5656)..(0, 0.8203, 0.6406)
  - plane n(-1, 0, 0), n·p = -0.075; extent (0.075, 0.3323, 0.1526)..(0.075, 1.2332, 1.0535)
  - plane n(1, 0, 0), n·p = 0.45; extent (0.45, 0.015, -0.0069)..(0.45, 1.3928, 2.2027)
  - plane n(1, 0, 0), n·p = 0.125; extent (0.125, 0.015, -0.0069)..(0.125, 1.3928, 2.2027)
  - plane n(0, -1, 0), n·p = -0.3895; extent (0.14, 0.3895, 1.6519)..(0.435, 0.3895, 2.0229)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.8138, 1.6519) R0.4243; extent (0.14, 0.3895, 1.2278)..(0.435, 0.8013, 1.6519)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.0301, 0.9279) R0.1947; extent (0.14, 0.1124, 0.8508)..(0.435, 0.2249, 1.1044)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.1947, 1.2809) R0.1947; extent (0.14, 0, 1.1044)..(0.435, 0.1124, 1.2809)
  - plane n(0, 1, 0), n·p = 0; extent (0.14, 0, 1.2809)..(0.435, 0, 2.0229)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.1947, 2.0229) R0.1947; extent (0.14, 0, 2.0229)..(0.435, 0.3895, 2.2177)
  - cylinder axis dir(1, 0, 0) through (0.2875, 0.7828, 0.6031) R0.625; extent (0.14, 0.8013, 0)..(0.435, 1.4078, 1.2278)
  - cone axis dir(1, 0, 0) through (0.1, 0.7828, 0.6031) R0.4938, half-angle 30 deg; extent (0.0875, 0.6551, 0.1336)..(0.1125, 1.2693, 1.0896)
  - torus axis dir(-1, 0, 0) centre (0.05, 0.7828, 0.6031) major R0.0375 minor r0.05; extent (0, 0.6953, 0.5156)..(0.05, 0.8057, 0.6875)
  - torus axis dir(-1, 0, 0) centre (0.1, 0.7828, 0.6031) major R0.4504 minor r0.025; extent (0.075, 0.3107, 0.131)..(0.0875, 0.9067, 1.0586)
  - torus axis dir(-1, 0, 0) centre (0.05, 0.7828, 0.6031) major R0.1125 minor r0.025; extent (0.05, 0.7533, 0.4945)..(0.075, 0.8953, 0.7156)
  - torus axis dir(1, 0, 0) centre (0.1, 0.7828, 0.6031) major R0.5082 minor r0.025; extent (0.1125, 0.6494, 0.1127)..(0.125, 1.291, 1.1113)
  - torus axis dir(1, 0, 0) centre (0.14, 0.7828, 0.6031) major R0.61 minor r0.015; extent (0.125, 0.8008, 0)..(0.14, 1.4078, 1.2278)
  - torus axis dir(1, 0, 0) centre (0.435, 0.7828, 0.6031) major R0.61 minor r0.015; extent (0.435, 0.8008, 0)..(0.45, 1.4078, 1.2278)

### P27 Platform lock casting, type B (mirror of P26) (1 bodies, 38 faces each)

Mirror image of P26: take P26's local geometry and replace u by (0.45 - u). Same faces, radii and volume.

### P28 Top hinge plate, type A (2 bodies, 30 faces each)

Top hinge plate 0.1625 thick (faces u = 0 and u = 0.1625) with rounded-end outline (R0.25 corners) and four raised dimples (torus R0.0875 / r0.075 with flat tops) at (v, w) = (0.25, 0.3961), (0.25, 2.6847), (2.3499, 1.0199), (2.3499, 3.3084).

Local box: u 0 .. 0.1625, v 0 .. 2.5999, w -0.0103 .. 3.7149.

Section at u = 0.0406 (coordinates v, w):
  - loop: (2.5999, 3.4649) – arc c(2.3499, 3.4649) R0.25 via (2.4995, 3.6653) – (2.2788, 3.7045) – (0.1788, 3.0808) – arc c(0.25, 2.8412) R0.25 via (0.0496, 2.9907) – (0, 2.8412) – (0, 0.2397) – arc c(0.25, 0.2397) R0.25 via (0.1005, 0.0393) – (0.3212, 0) – (2.4211, 0.6237) – arc c(2.3499, 0.8634) R0.25 via (2.5503, 0.7139) – (2.5999, 0.8634) – (2.5999, 3.4649)
Face list (all 30 faces):
  - torus axis dir(1, 0, 0) centre (0.0875, 2.3499, 3.3084) major R0.0875 minor r0.075; extent (0.0875, 2.3037, 3.1526)..(0.1625, 2.5124, 3.4709)
  - torus axis dir(1, 0, 0) centre (0.0875, 2.3499, 1.0199) major R0.0875 minor r0.075; extent (0.0875, 2.3037, 0.8641)..(0.1625, 2.5124, 1.1824)
  - torus axis dir(1, 0, 0) centre (0.0875, 0.25, 2.6847) major R0.0875 minor r0.075; extent (0.0875, 0.2037, 2.5289)..(0.1625, 0.4125, 2.8472)
  - torus axis dir(1, 0, 0) centre (0.0875, 0.25, 0.3961) major R0.0875 minor r0.075; extent (0.0875, 0.2037, 0.2404)..(0.1625, 0.4125, 0.5586)
  - cylinder axis dir(-1, 0, 0) through (0.075, 0.25, 2.6847) R0.1625; extent (0.0625, 0.2037, 2.5289)..(0.0875, 0.4125, 2.8472)
  - cylinder axis dir(-1, 0, 0) through (0.075, 0.25, 0.3961) R0.1625; extent (0.0625, 0.2037, 0.2404)..(0.0875, 0.4125, 0.5586)
  - cylinder axis dir(-1, 0, 0) through (0.075, 2.3499, 1.0199) R0.1625; extent (0.0625, 2.3037, 0.8641)..(0.0875, 2.5124, 1.1824)
  - cylinder axis dir(-1, 0, 0) through (0.075, 2.3499, 3.3084) R0.1625; extent (0.0625, 2.3037, 3.1526)..(0.0875, 2.5124, 3.4709)
  - plane n(1, 0, 0), n·p = 0.1625; extent (0.1625, 0.1625, 2.5972)..(0.1625, 0.3375, 2.7722)
  - plane n(1, 0, 0), n·p = 0.1625; extent (0.1625, 0.1625, 0.3086)..(0.1625, 0.3375, 0.4836)
  - plane n(1, 0, 0), n·p = 0.1625; extent (0.1625, 2.2624, 0.9324)..(0.1625, 2.4374, 1.1074)
  - plane n(1, 0, 0), n·p = 0.1625; extent (0.1625, 2.2624, 3.2209)..(0.1625, 2.4374, 3.3959)
  - cylinder axis dir(-1, 0, 0) through (0.0313, 2.3499, 3.4649) R0.25; extent (0, 2.2788, 3.4649)..(0.0625, 2.5999, 3.7149)
  - cylinder axis dir(-1, 0, 0) through (0.0313, 0.25, 0.2397) R0.25; extent (0, 0, -0.0103)..(0.0625, 0.3212, 0.2397)
  - cylinder axis dir(-1, 0, 0) through (0.0313, 0.25, 2.8412) R0.25; extent (0, 0, 2.8412)..(0.0625, 0.1788, 3.0808)
  - cylinder axis dir(-1, 0, 0) through (0.0313, 2.3499, 0.8634) R0.25; extent (0, 2.4211, 0.6237)..(0.0625, 2.5999, 0.8634)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, -0.0103)..(0, 2.5999, 3.7149)
  - plane n(1, 0, 0), n·p = 0.0625; extent (0.0625, 0, -0.0103)..(0.0625, 2.5999, 3.7149)
  - plane n(0, 0.2847, -0.9586), n·p = -2.9024; extent (0, 0.1788, 3.0808)..(0.0625, 2.2788, 3.7045)
  - plane n(0, -1, 0), n·p = -2.5999; extent (0, 2.5999, 0.8634)..(0.0625, 2.5999, 3.4649)
  - plane n(0, -0.2847, 0.9586), n·p = -0.0914; extent (0, 0.3212, 0)..(0.0625, 2.4211, 0.6237)
  - plane n(0, 1, 0), n·p = 0; extent (0, 0, 0.2397)..(0.0625, 0, 2.8412)
  - cylinder axis dir(-1, 0, 0) through (0.075, 2.3499, 3.3084) R0.1625; extent (0.0625, 2.1874, 3.1459)..(0.0875, 2.3962, 3.4642)
  - cylinder axis dir(-1, 0, 0) through (0.075, 2.3499, 1.0199) R0.1625; extent (0.0625, 2.1874, 0.8574)..(0.0875, 2.3962, 1.1756)
  - cylinder axis dir(-1, 0, 0) through (0.075, 0.25, 0.3961) R0.1625; extent (0.0625, 0.0875, 0.2336)..(0.0875, 0.2963, 0.5519)
  - cylinder axis dir(-1, 0, 0) through (0.075, 0.25, 2.6847) R0.1625; extent (0.0625, 0.0875, 2.5222)..(0.0875, 0.2963, 2.8405)
  - torus axis dir(1, 0, 0) centre (0.0875, 0.25, 0.3961) major R0.0875 minor r0.075; extent (0.0875, 0.0875, 0.2336)..(0.1625, 0.2963, 0.5519)
  - torus axis dir(1, 0, 0) centre (0.0875, 0.25, 2.6847) major R0.0875 minor r0.075; extent (0.0875, 0.0875, 2.5222)..(0.1625, 0.2963, 2.8405)
  - torus axis dir(1, 0, 0) centre (0.0875, 2.3499, 1.0199) major R0.0875 minor r0.075; extent (0.0875, 2.1874, 0.8574)..(0.1625, 2.3962, 1.1756)
  - torus axis dir(1, 0, 0) centre (0.0875, 2.3499, 3.3084) major R0.0875 minor r0.075; extent (0.0875, 2.1874, 3.1459)..(0.1625, 2.3962, 3.4642)

### P29 Top hinge plate, type B (mirror of P28) (2 bodies, 30 faces each)

Mirror image of P28: take P28's local geometry and replace u by (0.1625 - u). Same faces, radii and volume.

### P30 Hinge spacer drum (2 bodies, 11 faces each)

Hinge spacer drum diameter 0.875: head face u = 0 with an R0.1 edge round, cylinder R0.4375, tail rim at u = 0.475 (R0.0375 rounds) around a central face recessed to u = 0.45 (radius up to 0.3625).

Local extent: u 0 .. 0.475, radius 0.4375.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.1, -0.4375) – arc c(0.1, -0.3375) R0.1 via (0.0293, -0.4082) – (0, -0.3375) – (0, 0.3375) – arc c(0.1, 0.3375) R0.1 via (0.0293, 0.4082) – (0.1, 0.4375) – (0.4375, 0.4375) – arc c(0.4375, 0.4) R0.0375 via (0.464, 0.4265) – (0.475, 0.4) – (0.475, 0.3979) – arc c(0.4375, 0.3979) R0.0375 via (0.4681, 0.3762) – (0.45, 0.3625) – (0.45, -0.3625) – arc c(0.4375, -0.3979) R0.0375 via (0.4681, -0.3762) – (0.475, -0.3979) – (0.475, -0.4) – arc c(0.4375, -0.4) R0.0375 via (0.464, -0.4265) – (0.4375, -0.4375) – (0.1, -0.4375)

### P31 Platform corner bracket, type A (2 bodies, 25 faces each)

Platform corner bracket: a bent strip 0.1 thick with two short legs and a free-form twist (one B-spline face); the face list is complete.

Local box: u 0 .. 0.9809, v -0.0002 .. 0.9901, w 0 .. 1.5298.

Section at u = 0.4904 (coordinates v, w):
  - loop: (0.9403, 1.3178) – (0.9401, 1.3178)
  - loop: (0.9403, 1.3178) – arc c(1.144, 1.5984) R0.3467 via (0.9646, 1.3017) – (0.9901, 1.2877) – (0.9901, 0.505) – (0.9401, 0.505) – (0.9401, 1.3178)
Section at v = 0.4949 (coordinates u, w):
  - loop: (0, 0.4051) – (0.1, 0.4051) – (0.1, 0.07) – arc c(-1.7194, 4.2465) R4.5556 via (0.0501, 0.0487) – (0, 0.0279) – (0, 0.4051)
  - loop: (0, 1.1548) – (0.1, 1.1548) – (0.1, 1.5298) – (0, 1.5) – (0, 1.1548)
Face list (all 25 faces):
  - cylinder axis dir(0, -1, 0) through (0.5914, 0.9651, 0.9416) R0.3895; extent (0.48, 0.9401, 0.5684)..(0.9809, 0.9901, 1.3311)
  - cylinder axis dir(0.9582, 0, 0.286) through (0.0579, 0.1823, 1.4651) R0.05; extent (0, 0.1326, 1.453)..(0.1, 0.1823, 1.5298)
  - cylinder axis dir(0.9996, -0.0283, 0) through (0.0507, 0.1578, 1.2048) R0.05; extent (0, 0.1064, 1.1548)..(0.1, 0.1593, 1.2096)
  - cylinder axis dir(1, 0, 0) through (0.05, 0.5517, 1.1048) R0.05; extent (0, 0.5517, 1.1001)..(0.1, 0.6017, 1.1548)
  - cylinder axis dir(1, 0, 0) through (0.05, 0.49, 0.4548) R0.05; extent (0, 0.49, 0.4048)..(0.1, 0.5398, 0.4501)
  - cylinder axis dir(-0.9996, 0.0283, 0) through (0.0507, 0.0771, 0.3548) R0.05; extent (0, 0.0259, 0.3596)..(0.1, 0.0785, 0.4048)
  - cylinder axis dir(-0.9582, 0, -0.286) through (0.0436, 0.0498, 0.0652) R0.05; extent (0, -0.0002, 0)..(0.1, 0.0498, 0.0872)
  - cylinder axis dir(-0.8642, 0.4321, -0.2579) through (0.1695, 0.9593, 0.2005) R0.2; extent (0, 0.7809, 0.238)..(0.1826, 0.9741, 0.4132)
  - free-form (blend) face; extent (0, 0.1701, 0)..(0.1001, 0.8309, 0.2678)
  - cylinder axis dir(-0.9582, 0, -0.286) through (0.0666, 0.696, 1.4155) R0.1; extent (0, 0.696, 1.4125)..(0.1001, 0.7947, 1.5298)
  - cylinder axis dir(-0.9582, 0, -0.286) through (0.2444, 1.1401, 1.5443) R0.35; extent (0, 0.7947, 1.1744)..(0.6296, 0.9901, 1.4423)
  - plane n(0, 0, -1), n·p = -1.1548; extent (0, 0.1564, 1.1548)..(0.1, 0.5517, 1.1548)
  - plane n(0, 0, 1), n·p = 0.4048; extent (0, 0.0757, 0.4048)..(0.1, 0.49, 0.4048)
  - plane n(0, -0.9955, 0.0946), n·p = -0.4948; extent (0, 0.5398, 0.4501)..(0.1, 0.6015, 1.1001)
  - plane n(0.286, 0, -0.9582), n·p = -1.4373; extent (0, 0.1823, 1.5)..(0.1, 0.696, 1.5298)
  - plane n(-0.0282, -0.9951, 0.0945), n·p = 0.0054; extent (0, 0.1066, 1.2096)..(0.1, 0.1326, 1.4828)
  - plane n(-0.0282, -0.9951, 0.0945), n·p = 0.0054; extent (0, 0, 0.0573)..(0.1, 0.0287, 0.3596)
  - plane n(-1, 0, 0), n·p = -0.1; extent (0.1, -0.0002, 0.0298)..(0.1001, 0.7901, 1.5298)
  - cylinder axis dir(0, 0, -1) through (0.25, 0.7901, 0.8749) R0.15; extent (0.1, 0.7901, 0.289)..(0.25, 0.9401, 1.4608)
  - cylinder axis dir(0, 0, 1) through (0.15, 0.8401, 0.7712) R0.15; extent (0, 0.8401, 0.2592)..(0.15, 0.9901, 1.2832)
  - plane n(1, 0, 0), n·p = 0; extent (0, -0.0002, 0)..(0.0001, 0.8401, 1.5)
  - plane n(-0.286, 0, 0.9582), n·p = 0; extent (0, 0.0498, 0)..(0.1, 0.2201, 0.0298)
  - plane n(-0.286, 0, 0.9582), n·p = 0.3437; extent (0.0826, 0.9241, 0.3833)..(0.7028, 0.9901, 0.5684)
  - plane n(0, 1, 0), n·p = 0.9901; extent (0.15, 0.9901, 0.4034)..(0.9809, 0.9901, 1.3293)
  - plane n(0, -1, 0), n·p = -0.9401; extent (0.25, 0.9401, 0.4333)..(0.9809, 0.9401, 1.3311)

### P32 Platform corner bracket, type B (mirror of P31) (2 bodies, 25 faces each)

Mirror image of P31: take P31's local geometry and replace u by (0.7028 - u). Same faces, radii and volume.

### P33 Thin strip (label), 0.005 in (23 bodies, 6 faces each)

Thin label strip 0.005 thick, outline a quadrilateral in (v, w).

Local box: u 0 .. 0.005, v 0 .. 1.25, w 0 .. 2.7183.

Section at u = 0.0025 (coordinates v, w):
  - loop: (1.25, 2.347) – (0, 2.7183) – (0, 0.3713) – (1.25, 0) – (1.25, 2.347)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0.005; extent (0.005, 0, 0)..(0.005, 1.25, 2.7183)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.25, 2.7183)

### P34 Thin strip (label), 0.002 in, form A (11 bodies, 6 faces each)

Thin label strip 0.002 thick, quadrilateral outline.

Local box: u 0 .. 0.002, v 0 .. 1.2548, w 0 .. 2.6925.

Section at u = 0.001 (coordinates v, w):
  - loop: (0, 0.3546) – (1.2548, 0) – (1.2548, 2.338) – (0, 2.6925) – (0, 0.3546)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.2548, 2.6925)
  - plane n(1, 0, 0), n·p = 0.002; extent (0.002, 0, 0)..(0.002, 1.2548, 2.6925)

### P35 Thin strip (label), 0.002 in, form B (11 bodies, 6 faces each)

Thin label strip 0.002 thick, quadrilateral outline.

Local box: u 0 .. 0.002, v 0 .. 1.2373, w 0 .. 2.6557.

Section at u = 0.001 (coordinates v, w):
  - loop: (1.2373, 2.325) – (1.2373, 0) – (0, 0.3306) – (0, 2.6557) – (1.2373, 2.325)
Faces not parallel to u (end faces, cuts, cross features):
  - plane n(1, 0, 0), n·p = 0.002; extent (0.002, 0, 0)..(0.002, 1.2373, 2.6557)
  - plane n(1, 0, 0), n·p = 0; extent (0, 0, 0)..(0, 1.2373, 2.6557)

### H01 Rivet, 0.55 in long (12 bodies, 10 faces each)

Rivet 0.55 long: flat head face u = 0 (diameter 0.26) rounding with R0.12 into the body diameter 0.5; tail rim with an R0.025 round reaching u = 0.55 around a central recess diameter 0.4 whose floor is u = 0.5.

Local extent: u 0 .. 0.55, radius 0.25.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.525, -0.2) – arc c(0.525, -0.225) R0.025 via (0.55, -0.225) – (0.525, -0.25) – (0.12, -0.25) – arc c(0.12, -0.13) R0.12 via (0.0351, -0.2149) – (0, -0.13) – (0, 0.13) – arc c(0.12, 0.13) R0.12 via (0.0351, 0.2149) – (0.12, 0.25) – (0.525, 0.25) – arc c(0.525, 0.225) R0.025 via (0.55, 0.225) – (0.525, 0.2) – (0.5, 0.2) – (0.5, -0.2) – (0.525, -0.2)

### H02 Rivet, 0.40 in long (12 bodies, 10 faces each)

Rivet 0.40 long: as H01, rim reaching u = 0.4, recess diameter 0.4 with its floor at u = 0.35.

Local extent: u 0 .. 0.4, radius 0.25.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.375, -0.2) – arc c(0.375, -0.225) R0.025 via (0.4, -0.225) – (0.375, -0.25) – (0.12, -0.25) – arc c(0.12, -0.13) R0.12 via (0.0351, -0.2149) – (0, -0.13) – (0, 0.13) – arc c(0.12, 0.13) R0.12 via (0.0351, 0.2149) – (0.12, 0.25) – (0.375, 0.25) – arc c(0.375, 0.225) R0.025 via (0.4, 0.225) – (0.375, 0.2) – (0.35, 0.2) – (0.35, -0.2) – (0.375, -0.2)

### H03 Rivet, 0.3375 in long, recessed tail (32 bodies, 13 faces each)

Rivet 0.3375 long: head as H01, body diameter 0.5, tail rim with two R0.02 rounds reaching u = 0.3375, recess diameter 0.4 with its floor at u = 0.2625.

Local extent: u 0 .. 0.3375, radius 0.25.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.12, 0.25) – arc c(0.12, 0.13) R0.12 via (0.0351, 0.2149) – (0, 0.13) – (0, -0.13) – arc c(0.12, -0.13) R0.12 via (0.0351, -0.2149) – (0.12, -0.25) – (0.3175, -0.25) – arc c(0.3175, -0.23) R0.02 via (0.3316, -0.2441) – (0.3375, -0.23) – (0.3375, -0.22) – arc c(0.3175, -0.22) R0.02 via (0.3316, -0.2059) – (0.3175, -0.2) – (0.2625, -0.2) – (0.2625, 0.2) – (0.3175, 0.2) – arc c(0.3175, 0.22) R0.02 via (0.3316, 0.2059) – (0.3375, 0.22) – (0.3375, 0.23) – arc c(0.3175, 0.23) R0.02 via (0.3316, 0.2441) – (0.3175, 0.25) – (0.12, 0.25)

### H04 Rivet tail disc, 0.10 x 0.50 (20 bodies, 6 faces each)

Disc diameter 0.5, 0.1 thick, R0.075 round on the u = 0.1 edge.

Local extent: u 0 .. 0.1, radius 0.25.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.025, 0.25) – arc c(0.025, 0.175) R0.075 via (0.078, 0.228) – (0.1, 0.175) – (0.1, -0.175) – arc c(0.025, -0.175) R0.075 via (0.078, -0.228) – (0.025, -0.25) – (0, -0.25) – (0, 0.25) – (0.025, 0.25)

### H05 Collar, 0.325 dia x 0.15 (4 bodies, 6 faces each)

Collar diameter 0.325, 0.15 long, R0.0375 round on the u = 0.15 edge.

Local extent: u 0 .. 0.15, radius 0.1625.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.1125, -0.1625) – arc c(0.1125, -0.125) R0.0375 via (0.139, -0.1515) – (0.15, -0.125) – (0.15, 0.125) – arc c(0.1125, 0.125) R0.0375 via (0.139, 0.1515) – (0.1125, 0.1625) – (0, 0.1625) – (0, -0.1625) – (0.1125, -0.1625)

### H06 Disc, 0.375 dia x 0.10 (16 bodies, 6 faces each)

Disc diameter 0.375, 0.1 thick, R0.075 round on the u = 0.1 edge.

Local extent: u 0 .. 0.1, radius 0.1875.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.1, 0.1125) – arc c(0.025, 0.1125) R0.075 via (0.078, 0.1655) – (0.025, 0.1875) – (0, 0.1875) – (0, -0.1875) – (0.025, -0.1875) – arc c(0.025, -0.1125) R0.075 via (0.078, -0.1655) – (0.1, -0.1125) – (0.1, 0.1125)

### H07 Disc, 0.325 dia x 0.10 (4 bodies, 6 faces each)

Disc diameter 0.325, 0.1 thick, R0.05 round on the u = 0.1 edge.

Local extent: u 0 .. 0.1, radius 0.1625.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.05, 0.1625) – arc c(0.05, 0.1125) R0.05 via (0.0854, 0.1479) – (0.1, 0.1125) – (0.1, -0.1125) – arc c(0.05, -0.1125) R0.05 via (0.0854, -0.1479) – (0.05, -0.1625) – (0, -0.1625) – (0, 0.1625) – (0.05, 0.1625)

### H08 Disc, 0.25 dia x 0.05 (22 bodies, 6 faces each)

Disc diameter 0.25, 0.05 thick, R0.0375 round on the u = 0.05 edge.

Local extent: u 0 .. 0.05, radius 0.125.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.05, 0.0875) – arc c(0.0125, 0.0875) R0.0375 via (0.039, 0.114) – (0.0125, 0.125) – (0, 0.125) – (0, -0.125) – (0.0125, -0.125) – arc c(0.0125, -0.0875) R0.0375 via (0.039, -0.114) – (0.05, -0.0875) – (0.05, 0.0875)

### H09 Domed cap, 0.25 dia (4 bodies, 4 faces each)

Domed cap diameter 0.25, 0.05 high: base face u = 0, a toroidal dome (profile arc R0.125 about (u, r) = (-0.075, 0.025)) up to a flat top of radius 0.025 at u = 0.05.

Local extent: u 0 .. 0.05, radius 0.125.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.05, -0.025) – arc c(-0.075, -0.025) R0.125 via (0.0368, -0.0809) – (0, -0.125) – (0, 0.125) – arc c(-0.075, 0.025) R0.125 via (0.0368, 0.0809) – (0.05, 0.025) – (0.05, -0.025)

### H10 Disc, 0.15 dia x 0.05 (8 bodies, 6 faces each)

Disc diameter 0.15, 0.05 thick, R0.0375 round on the u = 0.05 edge.

Local extent: u 0 .. 0.05, radius 0.075.

Axial section in the (u, v) plane through the axis (u = along the axis from the head face, v = radial); the solid is this outline revolved about the u axis:
  - (0.0125, 0.075) – arc c(0.0125, 0.0375) R0.0375 via (0.039, 0.064) – (0.05, 0.0375) – (0.05, -0.0375) – arc c(0.0125, -0.0375) R0.0375 via (0.039, -0.064) – (0.0125, -0.075) – (0, -0.075) – (0, 0.075) – (0.0125, 0.075)

## 6. Placements

Orientations (global unit directions of the local axes U, V, W):

| Q | U | V | W |
|---|---|---|---|
| Q01 | (0.995122, -0.098655, 0.000000) | (-0.094571, -0.953933, -0.284724) | (0.028089, 0.283335, -0.958609) |
| Q02 | (-0.995122, -0.098655, -0.000000) | (0.094571, -0.953933, 0.284724) | (-0.028089, 0.283335, 0.958609) |
| Q03 | (0.995122, 0.098655, 0.000000) | (0.094571, -0.953933, -0.284724) | (-0.028089, 0.283335, -0.958609) |
| Q04 | (-0.995122, 0.098655, 0.000000) | (-0.094571, -0.953933, 0.284724) | (0.028089, 0.283335, 0.958609) |
| Q05 | (0.000000, -1.000000, 0.000000) | (1.000000, 0.000000, 0.000000) | (0.000000, 0.000000, 1.000000) |
| Q06 | (0.000000, -1.000000, 0.000000) | (-1.000000, 0.000000, 0.000000) | (0.000000, 0.000000, -1.000000) |
| Q07 | (0.000000, -1.000000, 0.000000) | (0.000000, 0.000000, -1.000000) | (1.000000, 0.000000, 0.000000) |
| Q08 | (0.000000, -1.000000, 0.000000) | (0.000000, 0.000000, 1.000000) | (-1.000000, 0.000000, 0.000000) |
| Q09 | (0.995122, -0.098655, -0.000000) | (0.000000, -0.000000, 1.000000) | (-0.098655, -0.995122, -0.000000) |
| Q10 | (0.000000, -0.286006, 0.958228) | (-0.713853, 0.671042, 0.200289) | (-0.700295, -0.684034, -0.204167) |
| Q11 | (0.000000, -0.286006, -0.958228) | (0.713853, 0.671042, -0.200289) | (0.700295, -0.684034, 0.204167) |
| Q12 | (0.000000, 0.286006, -0.958228) | (0.713853, 0.671042, 0.200289) | (0.700295, -0.684034, -0.204167) |
| Q13 | (0.000000, 0.286006, 0.958228) | (-0.713853, 0.671042, -0.200289) | (-0.700295, -0.684034, 0.204167) |
| Q14 | (0.000000, 1.000000, 0.000000) | (0.000000, 0.000000, -1.000000) | (-1.000000, 0.000000, 0.000000) |
| Q15 | (0.000000, 1.000000, 0.000000) | (0.000000, 0.000000, 1.000000) | (1.000000, 0.000000, 0.000000) |
| Q16 | (0.995122, -0.098655, 0.000000) | (0.000000, -0.000000, -1.000000) | (0.098655, 0.995122, 0.000000) |
| Q17 | (-0.995122, -0.098655, -0.000000) | (-0.000000, -0.000000, 1.000000) | (-0.098655, 0.995122, 0.000000) |
| Q18 | (0.995122, 0.098655, 0.000000) | (0.000000, 0.000000, -1.000000) | (-0.098655, 0.995122, 0.000000) |
| Q19 | (-0.995122, 0.098655, 0.000000) | (0.000000, 0.000000, 1.000000) | (0.098655, 0.995122, 0.000000) |
| Q20 | (0.995122, 0.098655, -0.000000) | (0.000000, 0.000000, 1.000000) | (0.098655, -0.995122, 0.000000) |
| Q21 | (-0.995122, 0.098655, 0.000000) | (-0.028089, -0.283335, -0.958609) | (-0.094571, -0.953933, 0.284724) |
| Q22 | (-0.995122, -0.098655, 0.000000) | (0.028089, -0.283335, -0.958609) | (0.094571, -0.953933, 0.284724) |
| Q23 | (-0.995122, -0.098655, 0.000000) | (-0.026810, 0.270434, -0.962365) | (0.094942, -0.957670, -0.271760) |
| Q24 | (0.995122, -0.098655, -0.000000) | (0.026810, 0.270434, 0.962365) | (-0.094942, -0.957670, 0.271760) |
| Q25 | (-0.995122, 0.098655, 0.000000) | (0.026810, 0.270434, -0.962365) | (-0.094942, -0.957670, -0.271760) |
| Q26 | (0.995122, 0.098655, 0.000000) | (-0.026810, 0.270434, 0.962365) | (0.094942, -0.957670, 0.271760) |
| Q27 | (0.000000, -0.286006, 0.958228) | (-0.630584, 0.743701, 0.221976) | (-0.776121, -0.604243, -0.180351) |
| Q28 | (0.000000, 0.286006, -0.958228) | (0.630584, 0.743701, 0.221976) | (0.776121, -0.604243, -0.180351) |
| Q29 | (-0.000000, 0.286006, 0.958228) | (-0.630584, 0.743701, -0.221976) | (-0.776121, -0.604243, 0.180351) |
| Q30 | (-0.000000, -0.286006, -0.958228) | (0.630584, 0.743701, -0.221976) | (0.776121, -0.604243, 0.180351) |
| Q31 | (-1.000000, 0.000000, 0.000000) | (0.000000, 1.000000, 0.000000) | (0.000000, 0.000000, -1.000000) |
| Q32 | (1.000000, 0.000000, 0.000000) | (0.000000, 1.000000, 0.000000) | (0.000000, 0.000000, 1.000000) |
| Q33 | (0.000000, 1.000000, 0.000000) | (-1.000000, 0.000000, 0.000000) | (0.000000, 0.000000, 1.000000) |
| Q34 | (0.000000, 1.000000, 0.000000) | (1.000000, 0.000000, 0.000000) | (0.000000, 0.000000, -1.000000) |
| Q35 | (-1.000000, 0.000000, 0.000000) | (0.000000, -0.964941, -0.262468) | (0.000000, -0.262468, 0.964941) |
| Q36 | (-0.995122, -0.098655, 0.000000) | (0.028089, -0.283335, 0.958609) | (-0.094571, 0.953933, 0.284724) |
| Q37 | (0.995122, -0.098655, -0.000000) | (-0.028089, -0.283335, -0.958609) | (0.094571, 0.953933, -0.284724) |
| Q38 | (-0.995122, 0.098655, 0.000000) | (-0.028089, -0.283335, 0.958609) | (0.094571, 0.953933, 0.284724) |
| Q39 | (0.995122, 0.098655, 0.000000) | (0.028089, -0.283335, -0.958609) | (-0.094571, 0.953933, -0.284724) |
| Q40 | (0.000000, -0.286006, 0.958228) | (1.000000, 0.000000, 0.000000) | (0.000000, 0.958228, 0.286006) |
| Q41 | (0.000000, -0.286006, -0.958228) | (-1.000000, 0.000000, 0.000000) | (0.000000, 0.958228, -0.286006) |
| Q42 | (0.000000, 0.286006, -0.958228) | (-1.000000, 0.000000, 0.000000) | (0.000000, 0.958228, 0.286006) |
| Q43 | (0.000000, 0.286006, 0.958228) | (1.000000, 0.000000, 0.000000) | (0.000000, 0.958228, -0.286006) |
| Q44 | (0.995122, -0.098655, -0.000000) | (-0.098655, -0.995122, 0.000000) | (-0.000000, 0.000000, -1.000000) |
| Q45 | (0.995122, 0.098655, 0.000000) | (-0.098655, 0.995122, -0.000000) | (-0.000000, -0.000000, 1.000000) |
| Q46 | (0.995122, 0.098655, 0.000000) | (0.098655, -0.995122, 0.000000) | (0.000000, 0.000000, -1.000000) |
| Q47 | (0.995122, -0.098655, -0.000000) | (0.098655, 0.995122, -0.000000) | (0.000000, 0.000000, 1.000000) |
| Q48 | (-0.995122, -0.098655, 0.000000) | (-0.098655, 0.995122, 0.000000) | (-0.000000, -0.000000, -1.000000) |
| Q49 | (-0.995122, -0.098655, 0.000000) | (0.098655, -0.995122, -0.000000) | (0.000000, -0.000000, 1.000000) |
| Q50 | (0.995122, -0.098655, 0.000000) | (0.083370, 0.840949, 0.534654) | (-0.052746, -0.532046, 0.845071) |
| Q51 | (0.995122, -0.098655, 0.000000) | (-0.083370, -0.840949, -0.534654) | (0.052746, 0.532046, -0.845071) |
| Q52 | (0.995122, 0.098655, -0.000000) | (0.084113, -0.848446, -0.522555) | (-0.051552, 0.520006, -0.852606) |
| Q53 | (0.995122, 0.098655, -0.000000) | (-0.084113, 0.848446, 0.522555) | (0.051552, -0.520006, 0.852606) |

Axis directions of the axisymmetric parts:

| D | direction |
|---|---|
| D01 | (0.995122, -0.098655, 0.000000) |
| D02 | (-0.995122, -0.098655, 0.000000) |
| D03 | (-0.000000, -0.286006, 0.958228) |
| D04 | (-0.000000, -0.286006, -0.958228) |
| D05 | (-0.995122, 0.098655, -0.000000) |
| D06 | (0.995122, 0.098655, -0.000000) |
| D07 | (0.000000, 0.286006, -0.958228) |
| D08 | (0.000000, 0.286006, 0.958228) |
| D09 | (-1.000000, -0.000000, 0.000000) |
| D10 | (1.000000, -0.000000, 0.000000) |
| D11 | (0.000000, 1.000000, 0.000000) |
| D12 | (0.995102, -0.098851, 0.000000) |
| D13 | (-0.995102, -0.098851, 0.000000) |

Instances (O = local origin in global inch; for axisymmetric parts P = head-face centre):

| Body | Orientation | Origin |
|---|---|---|
| P01-01 | Q01 | (-5.426, 25.9824, -0.3234) |
| P01-02 | Q02 | (5.426, 25.9824, 0.3234) |
| P02-01 | Q03 | (4.2503, 25.8659, -0.3234) |
| P02-02 | Q04 | (-4.2503, 25.8659, 0.3234) |
| P03-01 | Q05 | (-11.508, -34.5, -21.8848) |
| P03-02 | Q06 | (11.5079, -34.5, 21.8848) |
| P04-01 | Q05 | (-10.3694, -23.0146, -18.4567) |
| P04-02 | Q06 | (10.3693, -23.0146, 18.4567) |
| P05-01 | Q05 | (-9.2307, -11.5293, -15.0286) |
| P05-02 | Q06 | (9.2306, -11.5293, 15.0286) |
| P06-01 | Q06 | (8.092, -0.0439, -8.1538) |
| P06-02 | Q05 | (-8.0921, -0.0439, 8.1538) |
| P07-01 | Q07 | (-6.375, 0, -0.25) |
| P07-02 | Q08 | (6.375, 0, 0.25) |
| P08 | Q09 | (-5.2629, 26.3607, -2.5196) |
| P09-01 | Q10 | (-1.9173, -36.0281, -21.7832) |
| P09-02 | Q11 | (1.9173, -36.0281, 21.7832) |
| P10-01 | Q12 | (1.9173, -36.7897, -19.2315) |
| P10-02 | Q13 | (-1.9173, -36.7897, 19.2315) |
| P11-01 | Q07 | (6.725, -34.4, -15.0961) |
| P11-02 | Q08 | (-6.725, -34.4, 15.0961) |
| P12-01 | Q14 | (-6.725, -36.1044, -15.0961) |
| P12-02 | Q15 | (6.725, -36.1044, 15.0961) |
| P13-01 | Q05 | (-12.5706, -45.4, -24.7961) |
| P13-02 | Q06 | (12.5706, -45.4, -21.4962) |
| P13-03 | Q05 | (-12.5706, -45.4, 21.4962) |
| P13-04 | Q06 | (12.5706, -45.4, 24.7961) |
| P14-01 | Q16 | (-12.5506, -45.25, -19.9492) |
| P14-02 | Q17 | (12.5506, -45.25, 19.9492) |
| P15-01 | Q18 | (11.3128, -45.3727, -19.9492) |
| P15-02 | Q19 | (-11.3128, -45.3727, 19.9492) |
| P16 | Q20 | (5.4871, 26, -4.5896) |
| P17 | Q09 | (-5.6856, 26.0197, -4.5896) |
| P18 | Q21 | (-5.3982, 26.8963, 3.3673) |
| P19 | Q22 | (5.5962, 26.9159, 3.3673) |
| P20-01 | Q23 | (5.4763, 26.1083, -0.2845) |
| P20-02 | Q24 | (-5.4763, 26.1083, 0.2845) |
| P21-01 | Q25 | (-4.2385, 25.9856, -0.2845) |
| P21-02 | Q26 | (4.2385, 25.9856, 0.2845) |
| P22-01 | Q27 | (-4.367, -23.1755, -17.9527) |
| P22-02 | Q28 | (4.367, -23.2184, -17.8089) |
| P22-03 | Q29 | (-4.367, -23.2184, 17.8089) |
| P22-04 | Q30 | (4.367, -23.1755, 17.9527) |
| P22-05 | Q27 | (-3.2284, -11.6901, -14.5246) |
| P22-06 | Q28 | (3.2284, -11.733, -14.3808) |
| P22-07 | Q29 | (-3.2284, -11.733, 14.3808) |
| P22-08 | Q30 | (3.2284, -11.6901, 14.5246) |
| P22-09 | Q27 | (-2.0897, -0.2048, -11.0965) |
| P22-10 | Q28 | (2.0897, -0.2477, -10.9528) |
| P22-11 | Q29 | (-2.0897, -0.2477, 10.9528) |
| P22-12 | Q30 | (2.0897, -0.2048, 11.0965) |
| P23-01 | Q31 | (-5.675, -0.7, 8.3496) |
| P23-02 | Q32 | (5.675, -0.7, -8.3496) |
| P24 | Q05 | (-12.5706, -45.25, -24.7961) |
| P25-01 | Q33 | (12.5706, -45.4, -24.7961) |
| P25-02 | Q34 | (-12.5706, -45.4, 24.7961) |
| P25-03 | Q06 | (12.5706, -45.25, 24.7961) |
| P26 | Q35 | (6.875, 0.2136, -0.2189) |
| P27 | Q35 | (-6.425, 0.2136, -0.2189) |
| P28-01 | Q36 | (5.6687, 22.9004, -4.1289) |
| P28-02 | Q37 | (-5.6687, 22.9004, 4.1289) |
| P29-01 | Q38 | (-5.507, 22.8844, -4.1289) |
| P29-02 | Q39 | (5.507, 22.8844, 4.1289) |
| P30-01 | D01 | P (-6.0825, 24.2918, 0) |
| P30-02 | D02 | P (6.0825, 24.2918, 0) |
| P31-01 | Q40 | (-7.4151, -1.0437, -8.387) |
| P31-02 | Q41 | (7.4151, -1.0437, 8.387) |
| P32-01 | Q42 | (7.4151, -1.2447, -7.7136) |
| P32-02 | Q43 | (-7.4151, -1.2447, 7.7136) |
| P33-01 | Q44 | (-11.2543, -32.7562, 20.965) |
| P33-02 | Q45 | (11.3726, -34.0006, 18.2467) |
| P33-03 | Q44 | (-11.0816, -31.0147, 20.4452) |
| P33-04 | Q46 | (11.0766, -31.0152, 20.4452) |
| P33-05 | Q47 | (-11.0323, -30.5172, 17.2071) |
| P33-06 | Q45 | (11.0273, -30.5177, 17.2071) |
| P33-07 | Q47 | (-9.5713, -15.78, 12.8085) |
| P33-08 | Q46 | (9.443, -14.5366, 15.5267) |
| P33-09 | Q47 | (-9.3986, -14.0385, 12.2887) |
| P33-10 | Q45 | (9.3936, -14.039, 12.2887) |
| P33-11 | Q47 | (-9.226, -12.2971, 11.7689) |
| P33-12 | Q45 | (9.221, -12.2976, 11.7689) |
| P33-13 | Q44 | (-7.8402, 1.6808, 10.6864) |
| P33-14 | Q46 | (7.8353, 1.6803, 10.6864) |
| P33-15 | Q47 | (-7.7909, 2.1783, 7.4484) |
| P33-16 | Q46 | (7.6626, 3.4217, 10.1666) |
| P33-17 | Q47 | (-7.6183, 3.9198, 6.9286) |
| P33-18 | Q45 | (7.6133, 3.9193, 6.9286) |
| P33-19 | Q45 | (6.1428, 20.2333, 1.9171) |
| P33-20 | Q44 | (-5.8353, 21.9042, 4.6503) |
| P33-21 | Q45 | (5.9537, 22.1412, 1.3477) |
| P33-22 | Q48 | (5.786, 22.4017, -1.4122) |
| P33-23 | Q49 | (5.49, 25.3871, -3.6107) |
| P34-01 | Q50 | (-11.2375, -32.5674, -20.8933) |
| P34-02 | Q50 | (-11.0649, -30.8259, -20.3736) |
| P34-03 | Q50 | (-10.8923, -29.0844, -19.8538) |
| P34-04 | Q51 | (-9.4686, -14.7245, -12.5088) |
| P34-05 | Q51 | (-9.296, -12.9831, -11.989) |
| P34-06 | Q51 | (-9.1233, -11.2416, -11.4693) |
| P34-07 | Q51 | (-7.9842, 0.2484, -8.0398) |
| P34-08 | Q50 | (-7.7742, 2.3672, -10.4663) |
| P34-09 | Q51 | (-7.639, 3.7314, -7.0002) |
| P34-10 | Q51 | (-5.9793, 20.4718, -2.0036) |
| P34-11 | Q50 | (-5.7425, 22.8604, -4.3496) |
| P35-01 | Q52 | (11.2288, -32.5505, -17.8713) |
| P35-02 | Q52 | (11.0593, -30.8401, -17.3608) |
| P35-03 | Q52 | (10.8897, -29.1298, -16.8503) |
| P35-04 | Q52 | (9.4548, -14.656, -12.5303) |
| P35-05 | Q53 | (9.2524, -12.6144, -14.9306) |
| P35-06 | Q53 | (9.0829, -10.9041, -14.4201) |
| P35-07 | Q53 | (7.9641, 0.3806, -11.0519) |
| P35-08 | Q52 | (7.8274, 1.7597, -7.6306) |
| P35-09 | Q52 | (7.6578, 3.47, -7.1201) |
| P35-10 | Q52 | (6.0279, 19.9113, -2.2128) |
| P35-11 | Q53 | (5.7992, 22.2179, -4.534) |
| H01-01 | D03 | P (-10.0157, -26.7651, -19.298) |
| H01-02 | D03 | P (10.0157, -26.7651, -19.298) |
| H01-03 | D04 | P (-10.0157, -26.7651, 19.298) |
| H01-04 | D04 | P (10.0157, -26.7651, 19.298) |
| H01-05 | D03 | P (-8.8771, -15.2797, -15.8699) |
| H01-06 | D03 | P (8.8771, -15.2797, -15.8699) |
| H01-07 | D04 | P (-8.8771, -15.2797, 15.8699) |
| H01-08 | D04 | P (8.8771, -15.2797, 15.8699) |
| H01-09 | D03 | P (-7.7384, -3.7944, -12.4418) |
| H01-10 | D03 | P (7.7384, -3.7944, -12.4418) |
| H01-11 | D04 | P (-7.7384, -3.7944, 12.4418) |
| H01-12 | D04 | P (7.7384, -3.7944, 12.4418) |
| H02-01 | D03 | P (-5.7079, -23.4292, -18.2371) |
| H02-02 | D03 | P (5.7079, -23.4292, -18.2371) |
| H02-03 | D04 | P (-5.7079, -23.4292, 18.2371) |
| H02-04 | D04 | P (5.7079, -23.4292, 18.2371) |
| H02-05 | D03 | P (-4.5693, -11.9438, -14.809) |
| H02-06 | D03 | P (4.5693, -11.9438, -14.809) |
| H02-07 | D04 | P (-4.5693, -11.9438, 14.809) |
| H02-08 | D04 | P (4.5693, -11.9438, 14.809) |
| H02-09 | D03 | P (-3.4306, -0.4585, -11.3809) |
| H02-10 | D03 | P (3.4306, -0.4584, -11.3809) |
| H02-11 | D04 | P (-3.4306, -0.4584, 11.3809) |
| H02-12 | D04 | P (3.4306, -0.4585, 11.3809) |
| H03-01 | D03 | P (-10.8931, -35.6153, -21.9396) |
| H03-02 | D03 | P (10.8931, -35.6153, -21.9396) |
| H03-03 | D04 | P (-10.8931, -35.6153, 21.9396) |
| H03-04 | D04 | P (10.8931, -35.6153, 21.9396) |
| H03-05 | D03 | P (-10.8218, -34.8966, -21.7251) |
| H03-06 | D03 | P (10.8218, -34.8966, -21.7251) |
| H03-07 | D04 | P (-10.8218, -34.8966, 21.7251) |
| H03-08 | D04 | P (10.8218, -34.8966, 21.7251) |
| H03-09 | D03 | P (-9.7545, -24.13, -18.5115) |
| H03-10 | D03 | P (9.7544, -24.13, -18.5115) |
| H03-11 | D04 | P (-9.7544, -24.13, 18.5115) |
| H03-12 | D04 | P (9.7545, -24.13, 18.5115) |
| H03-13 | D03 | P (-9.6832, -23.4113, -18.297) |
| H03-14 | D03 | P (9.6832, -23.4113, -18.297) |
| H03-15 | D04 | P (-9.6832, -23.4113, 18.297) |
| H03-16 | D04 | P (9.6832, -23.4113, 18.297) |
| H03-17 | D03 | P (-8.6158, -12.6446, -15.0834) |
| H03-18 | D03 | P (8.6158, -12.6446, -15.0834) |
| H03-19 | D04 | P (-8.6158, -12.6446, 15.0834) |
| H03-20 | D04 | P (8.6158, -12.6446, 15.0834) |
| H03-21 | D03 | P (-8.5446, -11.9259, -14.8689) |
| H03-22 | D03 | P (8.5446, -11.9259, -14.8689) |
| H03-23 | D04 | P (-8.5446, -11.9259, 14.8689) |
| H03-24 | D04 | P (8.5446, -11.9259, 14.8689) |
| H03-25 | D03 | P (-7.4772, -1.1592, -11.6553) |
| H03-26 | D03 | P (7.4772, -1.1592, -11.6553) |
| H03-27 | D04 | P (-7.4772, -1.1592, 11.6553) |
| H03-28 | D04 | P (7.4772, -1.1592, 11.6553) |
| H03-29 | D03 | P (-7.4059, -0.4406, -11.4408) |
| H03-30 | D03 | P (7.4059, -0.4406, -11.4408) |
| H03-31 | D04 | P (-7.4059, -0.4406, 11.4408) |
| H03-32 | D04 | P (7.4059, -0.4406, 11.4408) |
| H04-01 | D05 | P (-12.4767, -44.5037, -23.7047) |
| H04-02 | D06 | P (12.4767, -44.5037, -23.7047) |
| H04-03 | D05 | P (-12.4767, -44.5037, -22.1422) |
| H04-04 | D06 | P (12.4767, -44.5037, -22.1422) |
| H04-05 | D05 | P (-12.4767, -44.5037, 22.1422) |
| H04-06 | D06 | P (12.4767, -44.5037, 22.1422) |
| H04-07 | D05 | P (-12.4767, -44.5037, 23.7047) |
| H04-08 | D06 | P (12.4767, -44.5037, 23.7047) |
| H04-09 | D03 | P (-11.5002, -40.9582, -20.2352) |
| H04-10 | D03 | P (11.5002, -40.9582, -20.2352) |
| H04-11 | D04 | P (-11.5002, -40.9582, 20.2352) |
| H04-12 | D04 | P (11.5002, -40.9582, 20.2352) |
| H04-13 | D07 | P (-11.4997, -40.9539, -23.4939) |
| H04-14 | D07 | P (11.4997, -40.9539, -23.4939) |
| H04-15 | D08 | P (-11.4997, -40.9539, 23.4939) |
| H04-16 | D08 | P (11.4997, -40.9539, 23.4939) |
| H04-17 | D07 | P (-5.3184, -35.0308, -21.5955) |
| H04-18 | D07 | P (5.3184, -35.0308, -21.5955) |
| H04-19 | D08 | P (-5.3184, -35.0308, 21.5955) |
| H04-20 | D08 | P (5.3184, -35.0308, 21.5955) |
| H05-01 | D09 | P (-6.475, -0.3105, -7.551) |
| H05-02 | D10 | P (6.475, -0.3105, -7.551) |
| H05-03 | D09 | P (-6.475, -0.3105, 7.551) |
| H05-04 | D10 | P (6.475, -0.3105, 7.551) |
| H06-01 | D11 | P (-11.8072, -45.1875, -23.9517) |
| H06-02 | D11 | P (11.8072, -45.1875, -23.9517) |
| H06-03 | D11 | P (-11.8056, -45.1875, -22.3034) |
| H06-04 | D11 | P (11.8056, -45.1875, -22.3034) |
| H06-05 | D11 | P (-11.8056, -45.1875, 22.3034) |
| H06-06 | D11 | P (11.8056, -45.1875, 22.3034) |
| H06-07 | D11 | P (-11.8072, -45.1875, 23.9517) |
| H06-08 | D11 | P (11.8072, -45.1875, 23.9517) |
| H06-09 | D12 | P (-12.229, -44.5407, -23.6288) |
| H06-10 | D13 | P (12.229, -44.5407, -23.6288) |
| H06-11 | D12 | P (-12.229, -44.5407, -22.1288) |
| H06-12 | D13 | P (12.229, -44.5407, -22.1288) |
| H06-13 | D12 | P (-12.229, -44.5407, 22.1288) |
| H06-14 | D13 | P (12.229, -44.5407, 22.1288) |
| H06-15 | D12 | P (-12.229, -44.5407, 23.6288) |
| H06-16 | D13 | P (12.229, -44.5407, 23.6288) |
| H07-01 | D03 | P (-7.3489, -0.2919, -8.1626) |
| H07-02 | D03 | P (7.3489, -0.2919, -8.1626) |
| H07-03 | D04 | P (-7.3489, -0.2919, 8.1626) |
| H07-04 | D04 | P (7.3489, -0.2919, 8.1626) |
| H08-01 | D09 | P (-6.425, -0.5053, -1.682) |
| H08-02 | D10 | P (6.425, -0.5053, -1.682) |
| H08-03 | D09 | P (-6.425, -0.5053, 1.682) |
| H08-04 | D09 | P (-6.425, -0.3105, -0.966) |
| H08-05 | D10 | P (6.425, -0.3105, -0.966) |
| H08-06 | D09 | P (-6.425, -0.3105, 0.966) |
| H08-07 | D11 | P (-5.8625, 0.05, -7.4098) |
| H08-08 | D11 | P (5.8625, 0.05, -7.4098) |
| H08-09 | D11 | P (-5.8625, 0.05, -5.2619) |
| H08-10 | D11 | P (5.8625, 0.05, -5.2619) |
| H08-11 | D11 | P (-5.8625, 0.05, -1.682) |
| H08-12 | D11 | P (5.8625, 0.05, -1.682) |
| H08-13 | D11 | P (-5.8625, 0.05, -0.966) |
| H08-14 | D11 | P (5.8625, 0.05, -0.966) |
| H08-15 | D11 | P (-5.8625, 0.05, 0.966) |
| H08-16 | D11 | P (5.8625, 0.05, 0.966) |
| H08-17 | D11 | P (-5.8625, 0.05, 1.682) |
| H08-18 | D11 | P (5.8625, 0.05, 1.682) |
| H08-19 | D11 | P (-5.8625, 0.05, 5.2619) |
| H08-20 | D11 | P (5.8625, 0.05, 5.2619) |
| H08-21 | D11 | P (-5.8625, 0.05, 7.4098) |
| H08-22 | D11 | P (5.8625, 0.05, 7.4098) |
| H09-01 | D09 | P (-6.75, -0.5052, 1.682) |
| H09-02 | D10 | P (6.75, -0.5053, 1.682) |
| H09-03 | D09 | P (-6.75, -0.3105, 0.966) |
| H09-04 | D10 | P (6.75, -0.3105, 0.966) |
| H10-01 | D03 | P (-7.0567, -0.8539, -8.226) |
| H10-02 | D03 | P (7.0567, -0.8539, -8.226) |
| H10-03 | D04 | P (-7.0567, -0.8539, 8.226) |
| H10-04 | D04 | P (7.0567, -0.8539, 8.226) |
| H10-05 | D03 | P (-6.9509, 0.213, -7.9076) |
| H10-06 | D03 | P (6.9509, 0.213, -7.9076) |
| H10-07 | D04 | P (-6.9509, 0.213, 7.9076) |
| H10-08 | D04 | P (6.9509, 0.213, 7.9076) |

## 7. Assembly contacts and overlaps

The original has 137 body pairs that overlap by more than 0.0005 in³ (8 mm³): the rivets / discs through unholed parts and the step ends inside the rail channels. They come out of the placements above; do not remove them. Pairs (overlap in in³):

- P30-01/P18 0.0595; P30-01/P17 0.0601; P22-01/H02-01 0.0295; P22-01/H01-01 0.0295; H02-04/P22-04 0.0295; H02-04/P04-02 0.0196
- H01-04/P01-02 0.0123; H01-04/P22-04 0.0295; H03-22/P05-01 0.0196; H03-22/P02-01 0.0123; P06-02/P01-02 0.0068; P06-02/H02-12 0.0196
- P06-02/H03-31 0.0196; P06-02/H03-27 0.0196; P06-02/H02-11 0.0196; P06-02/H03-32 0.0196; P06-02/P02-02 0.0068; P06-02/H03-28 0.0196
- P16/P30-02 0.0601; H01-08/P01-02 0.0123; H01-08/P22-08 0.0295; H03-23/P05-02 0.0196; H03-23/P02-02 0.0123; P04-01/H02-01 0.0196
- P04-01/H03-14 0.0196; P04-01/P02-01 0.0068; P04-01/H03-13 0.0196; P04-01/H03-10 0.0196; P04-01/P01-01 0.0068; P04-01/H02-02 0.0196
- P04-01/H03-09 0.0196; H03-30/P02-01 0.0123; H03-30/P06-01 0.0196; P01-02/H03-16 0.0123; P01-02/H01-12 0.0123; P01-02/H03-12 0.0123
- P01-02/H03-08 0.0123; P01-02/P04-02 0.0068; P01-02/H03-04 0.0123; P01-02/H03-24 0.0123; P01-02/P03-02 0.0068; P01-02/H03-32 0.0123
- P01-02/P05-02 0.0068; P01-02/H03-20 0.0123; P01-02/H03-28 0.0123; P05-01/H03-21 0.0196; P05-01/H03-18 0.0196; P05-01/P02-01 0.0068
- P05-01/H03-17 0.0196; P05-01/P01-01 0.0068; P05-01/H02-05 0.0196; P05-01/H02-06 0.0196; H03-21/P01-01 0.0123; P22-09/H01-09 0.0295
- P22-09/H02-09 0.0295; H03-02/P02-01 0.0123; H03-02/P03-01 0.0196; P30-02/P19 0.0595; H03-16/P04-02 0.0196; H03-19/P05-02 0.0196
- H03-19/P02-02 0.0123; H03-11/P04-02 0.0196; H03-11/P02-02 0.0123; P22-11/H02-11 0.0295; P22-11/H01-11 0.0295; H02-12/P22-12 0.0295
- H03-03/P03-02 0.0196; H03-03/P02-02 0.0123; H03-15/P04-02 0.0196; H03-15/P02-02 0.0123; H02-08/P22-08 0.0295; H02-08/P05-02 0.0196
- P21-01/P34-11 0.0037; H03-31/P02-02 0.0123; H01-12/P22-12 0.0295; H03-12/P04-02 0.0196; H03-14/P02-01 0.0123; P33-22/P35-11 0.0014
- H08-06/P27 0.0022; H03-08/P03-02 0.0196; P27/H08-03 0.0022; P04-02/H02-03 0.0196; P04-02/P02-02 0.0068; H03-18/P02-01 0.0123
- H02-07/P05-02 0.0196; H02-07/P22-07 0.0295; H03-04/P03-02 0.0196; P33-21/P19 0.0103; H01-06/P02-01 0.0123; H01-06/P22-06 0.0295
- H03-27/P02-02 0.0123; P22-02/H02-02 0.0295; P22-02/H01-02 0.0295; P02-01/H03-26 0.0123; P02-01/H03-10 0.0123; P02-01/P03-01 0.0068
- P02-01/H03-06 0.0123; P02-01/P06-01 0.0068; P02-01/H01-02 0.0123; P02-01/H01-10 0.0123; H03-26/P06-01 0.0196; H02-03/P22-03 0.0295
- H03-05/P01-01 0.0123; H03-05/P03-01 0.0196; H01-03/P22-03 0.0295; H01-03/P02-02 0.0123; P22-06/H02-06 0.0295; H03-13/P01-01 0.0123
- H03-24/P05-02 0.0196; H03-25/P01-01 0.0123; H03-25/P06-01 0.0196; H03-17/P01-01 0.0123; P22-10/H02-10 0.0295; P22-10/H01-10 0.0295
- H03-01/P01-01 0.0123; H03-01/P03-01 0.0196; P01-01/P03-01 0.0068; P01-01/H01-05 0.0123; P01-01/P06-01 0.0068; P01-01/H01-01 0.0123
- P01-01/H03-29 0.0123; P01-01/H03-09 0.0123; P01-01/H01-09 0.0123; P03-01/H03-06 0.0196; H01-05/P22-05 0.0295; H01-07/P02-02 0.0123
- H01-07/P22-07 0.0295; P03-02/P02-02 0.0068; P03-02/H03-07 0.0196; H02-05/P22-05 0.0295; P06-01/H02-10 0.0196; P06-01/H03-29 0.0196
- P06-01/H02-09 0.0196; H01-11/P02-02 0.0123; P05-02/H03-20 0.0196; P05-02/P02-02 0.0068; P02-02/H03-07 0.0123

## 8. Acceptance targets

Assembly (all 248 bodies): volume 317.3209 in³ (5199957.2 mm³), area 8110.472 in², centre of mass (0.0006, -15.5993, -0.0517), box x -12.5938 .. 12.5938, y -46 .. 26.0098,
z -24.7961 .. 24.7961.

Per body (inch): volume and area are those of the part in section 3; centre of mass and bounding box per instance:

| Body | CoM x | CoM y | CoM z | x min | x max | y min | y max | z min | z max |
|---|---|---|---|---|---|---|---|---|---|
| P01-01 | -8.7036 | -9.9915 | -12.6225 | -12.4878 | -4.2495 | -45.2500 | 25.8745 | -24.7109 | -0.3526 |
| P01-02 | 8.7036 | -9.9915 | 12.6225 | 4.2495 | 12.4878 | -45.2500 | 25.8745 | 0.3526 | 24.7109 |
| P02-01 | 8.7036 | -9.9915 | -12.6225 | 4.2495 | 12.4878 | -45.2500 | 25.8745 | -24.7109 | -0.3526 |
| P02-02 | -8.7036 | -9.9915 | 12.6225 | -12.4878 | -4.2495 | -45.2500 | 25.8745 | 0.3526 | 24.7109 |
| P03-01 | -0.0001 | -34.9824 | -20.1024 | -11.5080 | 11.5080 | -36.0000 | -34.5000 | -21.8848 | -18.4381 |
| P03-02 | -0.0001 | -34.9824 | 20.1024 | -11.5080 | 11.5080 | -36.0000 | -34.5000 | 18.4381 | 21.8848 |
| P04-01 | -0.0001 | -23.4972 | -16.6743 | -10.3694 | 10.3694 | -24.5146 | -23.0146 | -18.4567 | -15.0100 |
| P04-02 | -0.0001 | -23.4972 | 16.6743 | -10.3694 | 10.3694 | -24.5146 | -23.0146 | 15.0100 | 18.4567 |
| P05-01 | -0.0000 | -12.0121 | -13.2463 | -9.2307 | 9.2307 | -13.0293 | -11.5293 | -15.0286 | -11.5819 |
| P05-02 | -0.0000 | -12.0121 | 13.2463 | -9.2307 | 9.2307 | -13.0293 | -11.5293 | 11.5819 | 15.0286 |
| P06-01 | -0.0000 | -0.5271 | -9.8183 | -8.0921 | 8.0921 | -1.5439 | -0.0439 | -11.6006 | -8.1538 |
| P06-02 | -0.0000 | -0.5271 | 9.8183 | -8.0921 | 8.0921 | -1.5439 | -0.0439 | 8.1538 | 11.6006 |
| P07-01 | 0.0000 | -0.0821 | -4.2104 | -6.3750 | 6.3750 | -0.1500 | 0.0000 | -8.1855 | -0.2500 |
| P07-02 | 0.0000 | -0.0821 | 4.2104 | -6.3750 | 6.3750 | -0.1500 | 0.0000 | 0.2500 | 8.1855 |
| P08 | -0.0002 | 25.3056 | -1.9850 | -5.4204 | 5.4204 | 24.7723 | 25.8415 | -2.5196 | -1.4503 |
| P09-01 | -9.3148 | -39.2022 | -21.3403 | -12.4188 | -4.1403 | -45.1875 | -34.6814 | -24.5170 | -18.6078 |
| P09-02 | 9.3148 | -39.2022 | 21.3403 | 4.1403 | 12.4188 | -45.1875 | -34.6814 | 18.6078 | 24.5170 |
| P10-01 | 9.3148 | -39.2022 | -21.3403 | 4.1403 | 12.4188 | -45.1875 | -34.6814 | -24.5170 | -18.6078 |
| P10-02 | -9.3148 | -39.2022 | 21.3403 | -12.4188 | -4.1403 | -45.1875 | -34.6814 | 18.6078 | 24.5170 |
| P11-01 | 8.5247 | -34.9018 | -18.2557 | 6.7250 | 10.3940 | -36.1044 | -34.4000 | -22.0178 | -15.0961 |
| P11-02 | -8.5247 | -34.9018 | 18.2557 | -10.3940 | -6.7250 | -36.1044 | -34.4000 | 15.0961 | 22.0178 |
| P12-01 | -8.5247 | -34.9018 | -18.2557 | -10.3940 | -6.7250 | -36.1044 | -34.4000 | -22.0178 | -15.0961 |
| P12-02 | 8.5247 | -34.9018 | 18.2557 | 6.7250 | 10.3940 | -36.1044 | -34.4000 | 15.0961 | 22.0178 |
| P13-01 | -11.9256 | -45.6511 | -23.1462 | -12.5706 | -11.2806 | -46.0000 | -45.4000 | -24.7961 | -21.4962 |
| P13-02 | 11.9256 | -45.6511 | -23.1462 | 11.2806 | 12.5706 | -46.0000 | -45.4000 | -24.7961 | -21.4962 |
| P13-03 | -11.9256 | -45.6511 | 23.1462 | -12.5706 | -11.2806 | -46.0000 | -45.4000 | 21.4962 | 24.7961 |
| P13-04 | 11.9256 | -45.6511 | 23.1462 | 11.2806 | 12.5706 | -46.0000 | -45.4000 | 21.4962 | 24.7961 |
| P14-01 | -11.9898 | -42.6250 | -22.3627 | -12.5506 | -10.7802 | -45.2500 | -40.0000 | -24.7761 | -19.9492 |
| P14-02 | 11.9898 | -42.6250 | 22.3627 | 10.7802 | 12.5506 | -45.2500 | -40.0000 | 19.9492 | 24.7761 |
| P15-01 | 11.9898 | -42.6250 | -22.3627 | 10.7802 | 12.5506 | -45.2500 | -40.0000 | -24.7761 | -19.9492 |
| P15-02 | -11.9898 | -42.6250 | 22.3627 | -12.5506 | -10.7802 | -45.2500 | -40.0000 | 19.9492 | 24.7761 |
| P16 | 5.7469 | 24.2325 | -1.9357 | 5.4871 | 6.0223 | 22.5000 | 26.0000 | -4.5896 | 0.8750 |
| P17 | -5.7469 | 24.2325 | -1.9357 | -6.0223 | -5.4871 | 22.5000 | 26.0000 | -4.5896 | 0.8750 |
| P18 | -5.7155 | 24.2272 | 1.9505 | -5.9953 | -5.4871 | 22.5000 | 26.0098 | -0.8750 | 4.6197 |
| P19 | 5.7155 | 24.2272 | 1.9505 | 5.4871 | 5.9953 | 22.5000 | 26.0098 | -0.8750 | 4.6197 |
| P20-01 | 5.2479 | 24.6986 | -2.8052 | 4.2371 | 5.8340 | 22.5000 | 26.0000 | -4.6197 | -0.3168 |
| P20-02 | -5.2479 | 24.6986 | 2.8052 | -5.8340 | -4.2371 | 22.5000 | 26.0000 | 0.3168 | 4.6197 |
| P21-01 | -5.2479 | 24.6986 | -2.8052 | -5.8340 | -4.2371 | 22.5000 | 26.0000 | -4.6197 | -0.3168 |
| P21-02 | 5.2479 | 24.6986 | 2.8052 | 4.2371 | 5.8340 | 22.5000 | 26.0000 | 0.3168 | 4.6197 |
| P22-01 | -7.8603 | -25.2319 | -18.4882 | -10.5476 | -4.3670 | -28.0302 | -23.1755 | -19.3889 | -17.8089 |
| P22-02 | 7.8603 | -25.2319 | -18.4882 | 4.3670 | 10.5476 | -28.0302 | -23.1755 | -19.3889 | -17.8089 |
| P22-03 | -7.8603 | -25.2319 | 18.4882 | -10.5476 | -4.3670 | -28.0302 | -23.1755 | 17.8089 | 19.3889 |
| P22-04 | 7.8603 | -25.2319 | 18.4882 | 4.3670 | 10.5476 | -28.0302 | -23.1755 | 17.8089 | 19.3889 |
| P22-05 | -6.7216 | -13.7465 | -15.0601 | -9.4090 | -3.2284 | -16.5449 | -11.6901 | -15.9608 | -14.3808 |
| P22-06 | 6.7216 | -13.7465 | -15.0601 | 3.2284 | 9.4090 | -16.5449 | -11.6901 | -15.9608 | -14.3808 |
| P22-07 | -6.7216 | -13.7465 | 15.0601 | -9.4090 | -3.2284 | -16.5449 | -11.6901 | 14.3808 | 15.9608 |
| P22-08 | 6.7216 | -13.7465 | 15.0601 | 3.2284 | 9.4090 | -16.5449 | -11.6901 | 14.3808 | 15.9608 |
| P22-09 | -5.5830 | -2.2611 | -11.6320 | -8.2703 | -2.0897 | -5.0595 | -0.2048 | -12.5327 | -10.9528 |
| P22-10 | 5.5830 | -2.2611 | -11.6320 | 2.0897 | 8.2703 | -5.0595 | -0.2048 | -12.5327 | -10.9528 |
| P22-11 | -5.5830 | -2.2611 | 11.6320 | -8.2703 | -2.0897 | -5.0595 | -0.2048 | 10.9528 | 12.5327 |
| P22-12 | 5.5830 | -2.2611 | 11.6320 | 2.0897 | 8.2703 | -5.0595 | -0.2048 | 10.9528 | 12.5327 |
| P23-01 | -6.2217 | -0.1610 | 0.0000 | -6.4250 | -5.6750 | -0.7000 | 0.0500 | -8.3496 | 8.3496 |
| P23-02 | 6.2217 | -0.1610 | 0.0000 | 5.6750 | 6.4250 | -0.7000 | 0.0500 | -8.3496 | 8.3496 |
| P24 | -11.9256 | -45.3250 | -23.1462 | -12.5706 | -11.2806 | -45.4000 | -45.2500 | -24.7961 | -21.4962 |
| P25-01 | 11.9256 | -45.3250 | -23.1462 | 11.2806 | 12.5706 | -45.4000 | -45.2500 | -24.7961 | -21.4962 |
| P25-02 | -11.9256 | -45.3250 | 23.1462 | -12.5706 | -11.2806 | -45.4000 | -45.2500 | 21.4962 | 24.7961 |
| P25-03 | 11.9256 | -45.3250 | 23.1462 | 11.2806 | 12.5706 | -45.4000 | -45.2500 | 21.4962 | 24.7961 |
| P26 | 6.5995 | -0.6265 | 0.4475 | 6.4250 | 6.8750 | -1.3250 | -0.0750 | -0.4674 | 1.8767 |
| P27 | -6.5995 | -0.6265 | 0.4475 | -6.8750 | -6.4250 | -1.3250 | -0.0750 | -0.4674 | 1.8767 |
| P28-01 | 5.4949 | 24.2955 | -2.3553 | 5.2511 | 5.6777 | 22.8032 | 25.7886 | -4.0710 | -0.6396 |
| P28-02 | -5.4949 | 24.2955 | 2.3553 | -5.6777 | -5.2511 | 22.8032 | 25.7886 | 0.6396 | 4.0710 |
| P29-01 | -5.4949 | 24.2955 | -2.3553 | -5.6777 | -5.2511 | 22.8032 | 25.7886 | -4.0710 | -0.6396 |
| P29-02 | 5.4949 | 24.2955 | 2.3553 | 5.2511 | 5.6777 | 22.8032 | 25.7886 | 0.6396 | 4.0710 |
| P30-01 | -5.8515 | 24.2689 | 0.0000 | -6.1163 | -5.5702 | 23.8131 | 24.7178 | -0.4375 | 0.4375 |
| P30-02 | 5.8515 | 24.2689 | 0.0000 | 5.5702 | 6.1163 | 23.8131 | 24.7178 | -0.4375 | 0.4375 |
| P31-01 | -6.7448 | -0.3319 | -7.9925 | -7.4154 | -6.4250 | -1.0437 | 0.3937 | -8.3870 | -7.1615 |
| P31-02 | 6.7448 | -0.3319 | 7.9925 | 6.4250 | 7.4154 | -1.0437 | 0.3937 | 7.1615 | 8.3870 |
| P32-01 | 6.7448 | -0.3319 | -7.9925 | 6.4250 | 7.4154 | -1.0437 | 0.3937 | -8.3870 | -7.1615 |
| P32-02 | -6.7448 | -0.3319 | 7.9925 | -7.4154 | -6.4250 | -1.0437 | 0.3937 | 7.1615 | 8.3870 |
| P33-01 | -11.3134 | -33.3784 | 19.6058 | -11.3776 | -11.2493 | -34.0006 | -32.7562 | 18.2467 | 20.9650 |
| P33-02 | 11.3134 | -33.3784 | 19.6058 | 11.2493 | 11.3776 | -34.0006 | -32.7562 | 18.2467 | 20.9650 |
| P33-03 | -11.1408 | -31.6369 | 19.0861 | -11.2049 | -11.0766 | -32.2591 | -31.0147 | 17.7269 | 20.4452 |
| P33-04 | 11.1408 | -31.6369 | 19.0861 | 11.0766 | 11.2049 | -32.2591 | -31.0147 | 17.7269 | 20.4452 |
| P33-05 | -10.9681 | -29.8955 | 18.5663 | -11.0323 | -10.9040 | -30.5177 | -29.2733 | 17.2071 | 19.9254 |
| P33-06 | 10.9681 | -29.8955 | 18.5663 | 10.9040 | 11.0323 | -30.5177 | -29.2733 | 17.2071 | 19.9254 |
| P33-07 | -9.5071 | -15.1583 | 14.1676 | -9.5713 | -9.4430 | -15.7805 | -14.5361 | 12.8085 | 15.5267 |
| P33-08 | 9.5071 | -15.1583 | 14.1676 | 9.4430 | 9.5713 | -15.7805 | -14.5361 | 12.8085 | 15.5267 |
| P33-09 | -9.3345 | -13.4168 | 13.6478 | -9.3986 | -9.2703 | -14.0390 | -12.7946 | 12.2887 | 15.0070 |
| P33-10 | 9.3345 | -13.4168 | 13.6478 | 9.2703 | 9.3986 | -14.0390 | -12.7946 | 12.2887 | 15.0070 |
| P33-11 | -9.1618 | -11.6754 | 13.1280 | -9.2260 | -9.0977 | -12.2976 | -11.0532 | 11.7689 | 14.4872 |
| P33-12 | 9.1618 | -11.6754 | 13.1280 | 9.0977 | 9.2260 | -12.2976 | -11.0532 | 11.7689 | 14.4872 |
| P33-13 | -7.8994 | 1.0586 | 9.3273 | -7.9636 | -7.8353 | 0.4364 | 1.6808 | 7.9681 | 10.6864 |
| P33-14 | 7.8994 | 1.0586 | 9.3273 | 7.8353 | 7.9636 | 0.4364 | 1.6808 | 7.9681 | 10.6864 |
| P33-15 | -7.7268 | 2.8000 | 8.8075 | -7.7909 | -7.6626 | 2.1778 | 3.4222 | 7.4484 | 10.1666 |
| P33-16 | 7.7268 | 2.8000 | 8.8075 | 7.6626 | 7.7909 | 2.1778 | 3.4222 | 7.4484 | 10.1666 |
| P33-17 | -7.5541 | 4.5415 | 8.2877 | -7.6183 | -7.4900 | 3.9193 | 5.1637 | 6.9286 | 9.6469 |
| P33-18 | 7.5541 | 4.5415 | 8.2877 | 7.4900 | 7.6183 | 3.9193 | 5.1637 | 6.9286 | 9.6469 |
| P33-19 | 6.0836 | 20.8555 | 3.2763 | 6.0195 | 6.1478 | 20.2333 | 21.4777 | 1.9171 | 4.6354 |
| P33-20 | -5.8945 | 21.2820 | 3.2911 | -5.9586 | -5.8304 | 20.6598 | 21.9042 | 1.9320 | 4.6503 |
| P33-21 | 5.8945 | 22.7634 | 2.7068 | 5.8304 | 5.9586 | 22.1412 | 23.3856 | 1.3477 | 4.0660 |
| P33-22 | 5.7219 | 23.0234 | -2.7713 | 5.6577 | 5.7860 | 22.4012 | 23.6456 | -4.1305 | -1.4122 |
| P33-23 | 5.5492 | 24.7649 | -2.2516 | 5.4851 | 5.6134 | 24.1427 | 25.3871 | -3.6107 | -0.8924 |
| P34-01 | -11.2552 | -32.7561 | -19.4202 | -11.3796 | -11.1309 | -34.0001 | -31.5121 | -20.5937 | -18.2467 |
| P34-02 | -11.0826 | -31.0146 | -18.9004 | -11.2069 | -10.9583 | -32.2586 | -29.7706 | -20.0739 | -17.7269 |
| P34-03 | -10.9100 | -29.2732 | -18.3806 | -11.0343 | -10.7856 | -30.5172 | -28.0292 | -19.5541 | -17.2071 |
| P34-04 | -9.4489 | -14.5360 | -13.9820 | -9.5733 | -9.3246 | -15.7800 | -13.2920 | -15.1555 | -12.8085 |
| P34-05 | -9.2763 | -12.7945 | -13.4622 | -9.4006 | -9.1520 | -14.0385 | -11.5505 | -14.6357 | -12.2887 |
| P34-06 | -9.1036 | -11.0531 | -12.9424 | -9.2280 | -8.9793 | -12.2971 | -9.8091 | -14.1159 | -11.7689 |
| P34-07 | -7.9645 | 0.4370 | -9.5129 | -8.0889 | -7.8402 | -0.8070 | 1.6810 | -10.6864 | -8.3394 |
| P34-08 | -7.7919 | 2.1784 | -8.9931 | -7.9162 | -7.6676 | 0.9344 | 3.4224 | -10.1666 | -7.8196 |
| P34-09 | -7.6193 | 3.9199 | -8.4734 | -7.7436 | -7.4949 | 2.6759 | 5.1639 | -9.6469 | -7.2999 |
| P34-10 | -5.9596 | 20.6604 | -3.4768 | -6.0840 | -5.8353 | 19.4164 | 21.9044 | -4.6503 | -2.3033 |
| P34-11 | -5.7602 | 22.6717 | -2.8764 | -5.8846 | -5.6359 | 21.4277 | 23.9157 | -4.0499 | -1.7029 |
| P35-01 | 11.2134 | -32.3848 | -19.3267 | 11.0919 | 11.3349 | -33.6002 | -31.1693 | -20.5002 | -18.1532 |
| P35-02 | 11.0439 | -30.6744 | -18.8162 | 10.9224 | 11.1653 | -31.8899 | -29.4590 | -19.9897 | -17.6427 |
| P35-03 | 10.8743 | -28.9641 | -18.3057 | 10.7528 | 10.9958 | -30.1795 | -27.7486 | -19.4792 | -17.1322 |
| P35-04 | 9.4394 | -14.4903 | -13.9857 | 9.3179 | 9.5609 | -15.7057 | -13.2748 | -15.1592 | -12.8122 |
| P35-05 | 9.2698 | -12.7800 | -13.4752 | 9.1483 | 9.3913 | -13.9954 | -11.5645 | -14.6487 | -12.3017 |
| P35-06 | 9.1003 | -11.0696 | -12.9647 | 8.9788 | 9.2217 | -12.2851 | -9.8542 | -14.1382 | -11.7912 |
| P35-07 | 7.9815 | 0.2151 | -9.5965 | 7.8600 | 8.1030 | -1.0004 | 1.4305 | -10.7700 | -8.4230 |
| P35-08 | 7.8120 | 1.9254 | -9.0860 | 7.6905 | 7.9334 | 0.7099 | 3.1408 | -10.2595 | -7.9125 |
| P35-09 | 7.6424 | 3.6357 | -8.5755 | 7.5209 | 7.7639 | 2.4203 | 4.8512 | -9.7490 | -7.4020 |
| P35-10 | 6.0124 | 20.0770 | -3.6682 | 5.8910 | 6.1339 | 18.8615 | 21.2924 | -4.8417 | -2.4947 |
| P35-11 | 5.8166 | 22.0524 | -3.0786 | 5.6951 | 5.9381 | 20.8369 | 23.2678 | -4.2521 | -1.9051 |
| H01-01 | -10.0157 | -26.8420 | -19.0405 | -10.2657 | -9.7657 | -27.1558 | -26.5548 | -19.3402 | -18.7056 |
| H01-02 | 10.0157 | -26.8420 | -19.0405 | 9.7657 | 10.2657 | -27.1558 | -26.5548 | -19.3402 | -18.7056 |
| H01-03 | -10.0157 | -26.8420 | 19.0405 | -10.2657 | -9.7657 | -27.1558 | -26.5548 | 18.7056 | 19.3402 |
| H01-04 | 10.0157 | -26.8420 | 19.0405 | 9.7657 | 10.2657 | -27.1558 | -26.5548 | 18.7056 | 19.3402 |
| H01-05 | -8.8771 | -15.3566 | -15.6124 | -9.1271 | -8.6271 | -15.6705 | -15.0695 | -15.9121 | -15.2775 |
| H01-06 | 8.8771 | -15.3566 | -15.6124 | 8.6271 | 9.1271 | -15.6705 | -15.0695 | -15.9121 | -15.2775 |
| H01-07 | -8.8771 | -15.3566 | 15.6124 | -9.1271 | -8.6271 | -15.6705 | -15.0695 | 15.2775 | 15.9121 |
| H01-08 | 8.8771 | -15.3566 | 15.6124 | 8.6271 | 9.1271 | -15.6705 | -15.0695 | 15.2775 | 15.9121 |
| H01-09 | -7.7384 | -3.8712 | -12.1843 | -7.9884 | -7.4884 | -4.1851 | -3.5841 | -12.4840 | -11.8494 |
| H01-10 | 7.7384 | -3.8712 | -12.1843 | 7.4884 | 7.9884 | -4.1851 | -3.5841 | -12.4840 | -11.8494 |
| H01-11 | -7.7384 | -3.8712 | 12.1843 | -7.9884 | -7.4884 | -4.1851 | -3.5841 | 11.8494 | 12.4840 |
| H01-12 | 7.7384 | -3.8712 | 12.1843 | 7.4884 | 7.9884 | -4.1851 | -3.5841 | 11.8494 | 12.4840 |
| H02-01 | -5.7079 | -23.4845 | -18.0515 | -5.9579 | -5.4579 | -23.7770 | -23.2189 | -18.2793 | -17.7884 |
| H02-02 | 5.7079 | -23.4845 | -18.0515 | 5.4579 | 5.9579 | -23.7770 | -23.2189 | -18.2793 | -17.7884 |
| H02-03 | -5.7079 | -23.4845 | 18.0515 | -5.9579 | -5.4579 | -23.7770 | -23.2189 | 17.7884 | 18.2793 |
| H02-04 | 5.7079 | -23.4845 | 18.0515 | 5.4579 | 5.9579 | -23.7770 | -23.2189 | 17.7884 | 18.2793 |
| H02-05 | -4.5693 | -11.9992 | -14.6234 | -4.8193 | -4.3193 | -12.2917 | -11.7336 | -14.8512 | -14.3603 |
| H02-06 | 4.5693 | -11.9992 | -14.6234 | 4.3193 | 4.8193 | -12.2917 | -11.7336 | -14.8512 | -14.3603 |
| H02-07 | -4.5693 | -11.9992 | 14.6234 | -4.8193 | -4.3193 | -12.2917 | -11.7336 | 14.3603 | 14.8512 |
| H02-08 | 4.5693 | -11.9992 | 14.6234 | 4.3193 | 4.8193 | -12.2917 | -11.7336 | 14.3603 | 14.8512 |
| H02-09 | -3.4306 | -0.5138 | -11.1954 | -3.6806 | -3.1806 | -0.8063 | -0.2482 | -11.4231 | -10.9322 |
| H02-10 | 3.4306 | -0.5138 | -11.1954 | 3.1806 | 3.6806 | -0.8063 | -0.2482 | -11.4231 | -10.9322 |
| H02-11 | -3.4306 | -0.5138 | 11.1954 | -3.6806 | -3.1806 | -0.8063 | -0.2482 | 10.9322 | 11.4231 |
| H02-12 | 3.4306 | -0.5138 | 11.1954 | 3.1806 | 3.6806 | -0.8063 | -0.2482 | 10.9322 | 11.4231 |
| H03-01 | -10.8931 | -35.6599 | -21.7901 | -11.1431 | -10.6431 | -35.9465 | -35.4051 | -21.9818 | -21.5496 |
| H03-02 | 10.8931 | -35.6599 | -21.7901 | 10.6431 | 11.1431 | -35.9465 | -35.4051 | -21.9818 | -21.5496 |
| H03-03 | -10.8931 | -35.6599 | 21.7901 | -11.1431 | -10.6431 | -35.9465 | -35.4051 | 21.5496 | 21.9818 |
| H03-04 | 10.8931 | -35.6599 | 21.7901 | 10.6431 | 11.1431 | -35.9465 | -35.4051 | 21.5496 | 21.9818 |
| H03-05 | -10.8218 | -34.9412 | -21.5756 | -11.0718 | -10.5718 | -35.2278 | -34.6864 | -21.7673 | -21.3351 |
| H03-06 | 10.8218 | -34.9412 | -21.5756 | 10.5718 | 11.0718 | -35.2278 | -34.6864 | -21.7673 | -21.3351 |
| H03-07 | -10.8218 | -34.9412 | 21.5756 | -11.0718 | -10.5718 | -35.2278 | -34.6864 | 21.3351 | 21.7673 |
| H03-08 | 10.8218 | -34.9412 | 21.5756 | 10.5718 | 11.0718 | -35.2278 | -34.6864 | 21.3351 | 21.7673 |
| H03-09 | -9.7544 | -24.1746 | -18.3620 | -10.0044 | -9.5044 | -24.4612 | -23.9197 | -18.5537 | -18.1215 |
| H03-10 | 9.7544 | -24.1746 | -18.3620 | 9.5044 | 10.0044 | -24.4612 | -23.9197 | -18.5537 | -18.1215 |
| H03-11 | -9.7544 | -24.1746 | 18.3620 | -10.0044 | -9.5044 | -24.4612 | -23.9197 | 18.1215 | 18.5537 |
| H03-12 | 9.7544 | -24.1746 | 18.3620 | 9.5044 | 10.0044 | -24.4612 | -23.9197 | 18.1215 | 18.5537 |
| H03-13 | -9.6832 | -23.4559 | -18.1475 | -9.9332 | -9.4332 | -23.7425 | -23.2010 | -18.3392 | -17.9070 |
| H03-14 | 9.6832 | -23.4559 | -18.1475 | 9.4332 | 9.9332 | -23.7425 | -23.2010 | -18.3392 | -17.9070 |
| H03-15 | -9.6832 | -23.4559 | 18.1475 | -9.9332 | -9.4332 | -23.7425 | -23.2010 | 17.9070 | 18.3392 |
| H03-16 | 9.6832 | -23.4559 | 18.1475 | 9.4332 | 9.9332 | -23.7425 | -23.2010 | 17.9070 | 18.3392 |
| H03-17 | -8.6158 | -12.6892 | -14.9339 | -8.8658 | -8.3658 | -12.9758 | -12.4344 | -15.1256 | -14.6934 |
| H03-18 | 8.6158 | -12.6892 | -14.9339 | 8.3658 | 8.8658 | -12.9758 | -12.4344 | -15.1256 | -14.6934 |
| H03-19 | -8.6158 | -12.6892 | 14.9339 | -8.8658 | -8.3658 | -12.9758 | -12.4344 | 14.6934 | 15.1256 |
| H03-20 | 8.6158 | -12.6892 | 14.9339 | 8.3658 | 8.8658 | -12.9758 | -12.4344 | 14.6934 | 15.1256 |
| H03-21 | -8.5446 | -11.9705 | -14.7194 | -8.7946 | -8.2946 | -12.2571 | -11.7157 | -14.9111 | -14.4789 |
| H03-22 | 8.5446 | -11.9705 | -14.7194 | 8.2946 | 8.7946 | -12.2571 | -11.7157 | -14.9111 | -14.4789 |
| H03-23 | -8.5446 | -11.9705 | 14.7194 | -8.7946 | -8.2946 | -12.2571 | -11.7157 | 14.4789 | 14.9111 |
| H03-24 | 8.5446 | -11.9705 | 14.7194 | 8.2946 | 8.7946 | -12.2571 | -11.7157 | 14.4789 | 14.9111 |
| H03-25 | -7.4772 | -1.2039 | -11.5059 | -7.7272 | -7.2272 | -1.4904 | -0.9490 | -11.6975 | -11.2653 |
| H03-26 | 7.4772 | -1.2039 | -11.5059 | 7.2272 | 7.7272 | -1.4904 | -0.9490 | -11.6975 | -11.2653 |
| H03-27 | -7.4772 | -1.2039 | 11.5059 | -7.7272 | -7.2272 | -1.4904 | -0.9490 | 11.2653 | 11.6975 |
| H03-28 | 7.4772 | -1.2039 | 11.5059 | 7.2272 | 7.7272 | -1.4904 | -0.9490 | 11.2653 | 11.6975 |
| H03-29 | -7.4059 | -0.4852 | -11.2914 | -7.6559 | -7.1559 | -0.7718 | -0.2303 | -11.4830 | -11.0508 |
| H03-30 | 7.4059 | -0.4852 | -11.2914 | 7.1559 | 7.6559 | -0.7718 | -0.2303 | -11.4830 | -11.0508 |
| H03-31 | -7.4059 | -0.4852 | 11.2914 | -7.6559 | -7.1559 | -0.7718 | -0.2303 | 11.0508 | 11.4830 |
| H03-32 | 7.4059 | -0.4852 | 11.2914 | 7.1559 | 7.6559 | -0.7718 | -0.2303 | 11.0508 | 11.4830 |
| H04-01 | -12.5232 | -44.4990 | -23.7047 | -12.5938 | -12.4520 | -44.7524 | -44.2520 | -23.9547 | -23.4547 |
| H04-02 | 12.5232 | -44.4990 | -23.7047 | 12.4520 | 12.5938 | -44.7524 | -44.2520 | -23.9547 | -23.4547 |
| H04-03 | -12.5232 | -44.4990 | -22.1422 | -12.5938 | -12.4520 | -44.7524 | -44.2520 | -22.3922 | -21.8922 |
| H04-04 | 12.5232 | -44.4990 | -22.1422 | 12.4520 | 12.5938 | -44.7524 | -44.2520 | -22.3922 | -21.8922 |
| H04-05 | -12.5232 | -44.4990 | 22.1422 | -12.5938 | -12.4520 | -44.7524 | -44.2520 | 21.8922 | 22.3922 |
| H04-06 | 12.5232 | -44.4990 | 22.1422 | 12.4520 | 12.5938 | -44.7524 | -44.2520 | 21.8922 | 22.3922 |
| H04-07 | -12.5232 | -44.4990 | 23.7047 | -12.5938 | -12.4520 | -44.7524 | -44.2520 | 23.4547 | 23.9547 |
| H04-08 | 12.5232 | -44.4990 | 23.7047 | 12.4520 | 12.5938 | -44.7524 | -44.2520 | 23.4547 | 23.9547 |
| H04-09 | -11.5002 | -40.9716 | -20.1904 | -11.7502 | -11.2502 | -41.2081 | -40.7187 | -20.3067 | -20.0862 |
| H04-10 | 11.5002 | -40.9716 | -20.1904 | 11.2502 | 11.7502 | -41.2081 | -40.7187 | -20.3067 | -20.0862 |
| H04-11 | -11.5002 | -40.9716 | 20.1904 | -11.7502 | -11.2502 | -41.2081 | -40.7187 | 20.0862 | 20.3067 |
| H04-12 | 11.5002 | -40.9716 | 20.1904 | 11.2502 | 11.7502 | -41.2081 | -40.7187 | 20.0862 | 20.3067 |
| H04-13 | -11.4997 | -40.9406 | -23.5387 | -11.7497 | -11.2497 | -41.1935 | -40.7041 | -23.6429 | -23.4224 |
| H04-14 | 11.4997 | -40.9406 | -23.5387 | 11.2497 | 11.7497 | -41.1935 | -40.7041 | -23.6429 | -23.4224 |
| H04-15 | -11.4997 | -40.9406 | 23.5387 | -11.7497 | -11.2497 | -41.1935 | -40.7041 | 23.4224 | 23.6429 |
| H04-16 | 11.4997 | -40.9406 | 23.5387 | 11.2497 | 11.7497 | -41.1935 | -40.7041 | 23.4224 | 23.6429 |
| H04-17 | -5.3184 | -35.0174 | -21.6403 | -5.5684 | -5.0684 | -35.2703 | -34.7809 | -21.7445 | -21.5240 |
| H04-18 | 5.3184 | -35.0174 | -21.6403 | 5.0684 | 5.5684 | -35.2703 | -34.7809 | -21.7445 | -21.5240 |
| H04-19 | -5.3184 | -35.0174 | 21.6403 | -5.5684 | -5.0684 | -35.2703 | -34.7809 | 21.5240 | 21.7445 |
| H04-20 | 5.3184 | -35.0174 | 21.6403 | 5.0684 | 5.5684 | -35.2703 | -34.7809 | 21.5240 | 21.7445 |
| H05-01 | -6.5484 | -0.3105 | -7.5510 | -6.6250 | -6.4750 | -0.4730 | -0.1480 | -7.7135 | -7.3885 |
| H05-02 | 6.5484 | -0.3105 | -7.5510 | 6.4750 | 6.6250 | -0.4730 | -0.1480 | -7.7135 | -7.3885 |
| H05-03 | -6.5484 | -0.3105 | 7.5510 | -6.6250 | -6.4750 | -0.4730 | -0.1480 | 7.3885 | 7.7135 |
| H05-04 | 6.5484 | -0.3105 | 7.5510 | 6.4750 | 6.6250 | -0.4730 | -0.1480 | 7.3885 | 7.7135 |
| H06-01 | -11.8072 | -45.1418 | -23.9517 | -11.9947 | -11.6197 | -45.1875 | -45.0875 | -24.1392 | -23.7642 |
| H06-02 | 11.8072 | -45.1418 | -23.9517 | 11.6197 | 11.9947 | -45.1875 | -45.0875 | -24.1392 | -23.7642 |
| H06-03 | -11.8056 | -45.1418 | -22.3034 | -11.9931 | -11.6181 | -45.1875 | -45.0875 | -22.4909 | -22.1159 |
| H06-04 | 11.8056 | -45.1418 | -22.3034 | 11.6181 | 11.9931 | -45.1875 | -45.0875 | -22.4909 | -22.1159 |
| H06-05 | -11.8056 | -45.1418 | 22.3034 | -11.9931 | -11.6181 | -45.1875 | -45.0875 | 22.1159 | 22.4909 |
| H06-06 | 11.8056 | -45.1418 | 22.3034 | 11.6181 | 11.9931 | -45.1875 | -45.0875 | 22.1159 | 22.4909 |
| H06-07 | -11.8072 | -45.1418 | 23.9517 | -11.9947 | -11.6197 | -45.1875 | -45.0875 | 23.7642 | 24.1392 |
| H06-08 | 11.8072 | -45.1418 | 23.9517 | 11.6197 | 11.9947 | -45.1875 | -45.0875 | 23.7642 | 24.1392 |
| H06-09 | -12.1835 | -44.5452 | -23.6288 | -12.2475 | -12.1180 | -44.7301 | -44.3541 | -23.8163 | -23.4413 |
| H06-10 | 12.1835 | -44.5452 | -23.6288 | 12.1180 | 12.2475 | -44.7301 | -44.3541 | -23.8163 | -23.4413 |
| H06-11 | -12.1835 | -44.5452 | -22.1288 | -12.2475 | -12.1180 | -44.7301 | -44.3541 | -22.3163 | -21.9413 |
| H06-12 | 12.1835 | -44.5452 | -22.1288 | 12.1180 | 12.2475 | -44.7301 | -44.3541 | -22.3163 | -21.9413 |
| H06-13 | -12.1835 | -44.5452 | 22.1288 | -12.2475 | -12.1180 | -44.7301 | -44.3541 | 21.9413 | 22.3163 |
| H06-14 | 12.1835 | -44.5452 | 22.1288 | 12.1180 | 12.2475 | -44.7301 | -44.3541 | 21.9413 | 22.3163 |
| H06-15 | -12.1835 | -44.5452 | 23.6288 | -12.2475 | -12.1180 | -44.7301 | -44.3541 | 23.4413 | 23.8163 |
| H06-16 | 12.1835 | -44.5452 | 23.6288 | 12.1180 | 12.2475 | -44.7301 | -44.3541 | 23.4413 | 23.8163 |
| H07-01 | -7.3489 | -0.3054 | -8.1171 | -7.5114 | -7.1864 | -0.4640 | -0.1362 | -8.2091 | -8.0325 |
| H07-02 | 7.3489 | -0.3054 | -8.1171 | 7.1864 | 7.5114 | -0.4640 | -0.1362 | -8.2091 | -8.0325 |
| H07-03 | -7.3489 | -0.3054 | 8.1171 | -7.5114 | -7.1864 | -0.4640 | -0.1362 | 8.0325 | 8.2091 |
| H07-04 | 7.3489 | -0.3054 | 8.1171 | 7.1864 | 7.5114 | -0.4640 | -0.1362 | 8.0325 | 8.2091 |
| H08-01 | -6.4484 | -0.5053 | -1.6820 | -6.4750 | -6.4250 | -0.6303 | -0.3803 | -1.8070 | -1.5570 |
| H08-02 | 6.4484 | -0.5053 | -1.6820 | 6.4250 | 6.4750 | -0.6303 | -0.3803 | -1.8070 | -1.5570 |
| H08-03 | -6.4484 | -0.5053 | 1.6820 | -6.4750 | -6.4250 | -0.6303 | -0.3803 | 1.5570 | 1.8070 |
| H08-04 | -6.4484 | -0.3105 | -0.9660 | -6.4750 | -6.4250 | -0.4355 | -0.1855 | -1.0910 | -0.8410 |
| H08-05 | 6.4484 | -0.3105 | -0.9660 | 6.4250 | 6.4750 | -0.4355 | -0.1855 | -1.0910 | -0.8410 |
| H08-06 | -6.4484 | -0.3105 | 0.9660 | -6.4750 | -6.4250 | -0.4355 | -0.1855 | 0.8410 | 1.0910 |
| H08-07 | -5.8625 | 0.0734 | -7.4098 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | -7.5348 | -7.2848 |
| H08-08 | 5.8625 | 0.0734 | -7.4098 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | -7.5348 | -7.2848 |
| H08-09 | -5.8625 | 0.0734 | -5.2619 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | -5.3869 | -5.1369 |
| H08-10 | 5.8625 | 0.0734 | -5.2619 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | -5.3869 | -5.1369 |
| H08-11 | -5.8625 | 0.0734 | -1.6820 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | -1.8070 | -1.5570 |
| H08-12 | 5.8625 | 0.0734 | -1.6820 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | -1.8070 | -1.5570 |
| H08-13 | -5.8625 | 0.0734 | -0.9660 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | -1.0910 | -0.8410 |
| H08-14 | 5.8625 | 0.0734 | -0.9660 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | -1.0910 | -0.8410 |
| H08-15 | -5.8625 | 0.0734 | 0.9660 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | 0.8410 | 1.0910 |
| H08-16 | 5.8625 | 0.0734 | 0.9660 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | 0.8410 | 1.0910 |
| H08-17 | -5.8625 | 0.0734 | 1.6820 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | 1.5570 | 1.8070 |
| H08-18 | 5.8625 | 0.0734 | 1.6820 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | 1.5570 | 1.8070 |
| H08-19 | -5.8625 | 0.0734 | 5.2619 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | 5.1369 | 5.3869 |
| H08-20 | 5.8625 | 0.0734 | 5.2619 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | 5.1369 | 5.3869 |
| H08-21 | -5.8625 | 0.0734 | 7.4098 | -5.9875 | -5.7375 | 0.0500 | 0.1000 | 7.2848 | 7.5348 |
| H08-22 | 5.8625 | 0.0734 | 7.4098 | 5.7375 | 5.9875 | 0.0500 | 0.1000 | 7.2848 | 7.5348 |
| H09-01 | -6.7689 | -0.5053 | 1.6820 | -6.8000 | -6.7500 | -0.6303 | -0.3803 | 1.5570 | 1.8070 |
| H09-02 | 6.7689 | -0.5053 | 1.6820 | 6.7500 | 6.8000 | -0.6303 | -0.3803 | 1.5570 | 1.8070 |
| H09-03 | -6.7689 | -0.3105 | 0.9660 | -6.8000 | -6.7500 | -0.4355 | -0.1855 | 0.8410 | 1.0910 |
| H09-04 | 6.7689 | -0.3105 | 0.9660 | 6.7500 | 6.8000 | -0.4355 | -0.1855 | 0.8410 | 1.0910 |
| H10-01 | -7.0567 | -0.8603 | -8.2046 | -7.1317 | -6.9817 | -0.9309 | -0.7820 | -8.2474 | -8.1658 |
| H10-02 | 7.0567 | -0.8603 | -8.2046 | 6.9817 | 7.1317 | -0.9309 | -0.7820 | -8.2474 | -8.1658 |
| H10-03 | -7.0567 | -0.8603 | 8.2046 | -7.1317 | -6.9817 | -0.9309 | -0.7820 | 8.1658 | 8.2474 |
| H10-04 | 7.0567 | -0.8603 | 8.2046 | 6.9817 | 7.1317 | -0.9309 | -0.7820 | 8.1658 | 8.2474 |
| H10-05 | -6.9509 | 0.2066 | -7.8862 | -7.0259 | -6.8759 | 0.1359 | 0.2848 | -7.9290 | -7.8474 |
| H10-06 | 6.9509 | 0.2066 | -7.8862 | 6.8759 | 7.0259 | 0.1359 | 0.2848 | -7.9290 | -7.8474 |
| H10-07 | -6.9509 | 0.2066 | 7.8862 | -7.0259 | -6.8759 | 0.1359 | 0.2848 | 7.8474 | 7.9290 |
| H10-08 | 6.9509 | 0.2066 | 7.8862 | 6.8759 | 7.0259 | 0.1359 | 0.2848 | 7.8474 | 7.9290 |

## 9. Undetermined items and notes

- The free-form blend faces (rolling rounds) of the lattice braces (P09, P10: 2 faces), the top cap side plates
  (P16 .. P19: 12 / 3 faces), the lock castings (P26, P27: rounds) and the corner brackets (P31, P32: 1 face) are not
  given as exact surfaces; their positions and extents are listed, model them as smooth transitions between the
  neighbouring faces.
- Materials are not part of the geometry (rails fibreglass, steps / platform / castings metal, pads rubber).
- The catalogue drawing gives 25.25 for the base width; the 3D model is 25.1876 (follow the 3D). Its "22 in" platform
  depth corresponds to the rails' outer spread at platform height (22.41 at y = 0).
