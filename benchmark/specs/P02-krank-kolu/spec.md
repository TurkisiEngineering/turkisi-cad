# Design specification: cast crank handle with offset arm and fixed grip (P2)

A one-piece cast crank: a cylindrical hub with a plain through bore, an S-shaped offset arm, and a fixed turned grip.
This document is the only source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - The **hub / bore axis is the X axis**. The hub's bottom (mounting) face is the plane X = 0; the hub rises toward +X.
  - The arm runs from the hub toward **-Y**. The **grip axis** is the line Y = -100, Z = 0, parallel to X.
  - The part is symmetric about the plane Z = 0.
- Notation: "(x, r)" = a profile in a half-plane containing the stated axis, r = distance from that axis. "(y, z)" = a
  profile in a plane normal to X.
- One body, one solid. Name: **P01 Crank handle**. The grip is part of the same solid (no separate grip body).

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Crank handle (hub, arm and grip, one solid) | custom |

## 3. Geometry of P01

The body is the union of (A) a solid of revolution about the X axis trimmed by a prism along X, and (B) a solid of
revolution about the grip axis; then (C) the bore is cut.

**A1. Hub-and-arm revolve about the X axis.** Closed profile in (x, r), revolved 360 degrees about X. Start at (0, 0),
go in this order, the last segment closes on the start:
1. line to (0, 14)
2. line to (18.153, 14)  (hub cylinder, diameter 28)
3. concave arc R2.5, centre (18.153, 16.5), to (20.63435, 16.19512)
4. arc R18, centre (38.5, 14), to (30.8125, 30.27582)  (inner side of the S-neck)
5. arc R30, centre (18, 57.40224), to (48, 57.40224)  (tangent to step 4 and to step 6; reverse curvature)
6. line to (48, 112)  (inner face of the arm, plane X = 48)
7. line to (52.68507, 112)
8. line to (52.68507, 54.40268)  (outer face of the arm, plane X = 52.68507)
9. arc R37.5, centre (15.21507, 55.90244), to (32.53906, 22.64391)  (meets step 8 with a 2.3 degree kink, not tangent)
10. arc R10.5, centre (38.5, 14), to (28, 14)  (concentric with step 4; meets step 9 with a small kink)
11. line to (28, 0)  (hub top face, plane X = 28)
12. line to (0, 0).
The radial extent 112 is only a construction value; step A2 trims it.

**A2. Plan outline, prism along X.** Closed outline in (y, z), extruded through the whole X range of A1; intersect A1
with it (keep the common volume). The outline is the union of:
- a circle radius 15.5 centred (0, 0) (this produces the hub collar, diameter 31, between the R2.5 and R10.5 arcs of A1);
- a circle radius 8 centred (-100, 0) (the grip boss);
- the arm strip between the two lines z = +(8.25150 + 0.0150150 y) and z = -(8.25150 + 0.0150150 y) (half-width 8.2515
  at y = 0 and 6.7500 at y = -100: a 0.86 degree taper per side), for y from -100 to -9;
- four concave blend arcs, tangent to the strip lines and to the circles:
  - R22.5 centred (-22.78408, +/-30.41193): tangent to the strip line at (-22.44628, +/-7.91447) and to the R15.5 circle
    at (-9.29351, +/-12.40487);
  - R13.5 centred (-93.07860, +/-20.35545): tangent to the strip line at (-92.87592, +/-6.85697) and to the R8 circle at
    (-97.42460, +/-7.57412).
Result: the arm's two flat faces (the tapered strip lines) blend into the hub collar with R22.5 and into the grip boss
with R13.5; the collar is a cylinder R15.5 from x = 20.444 to x = 28.108.

**B. Grip revolve about the grip axis (Y = -100, Z = 0).** Closed profile in (x, r), revolved 360 degrees, united with A:
1. start (48, 0), line to (48, 8)
2. line to (60.5, 8)  (boss, diameter 16, from x = 48 to 60.5)
3. convex arc R0.5, centre (60.5, 7.5), to (61, 7.5)
4. line to (61, 6.5)  (shoulder, plane x = 61)
5. line to (67, 6.5)  (neck, diameter 13)
6. line to (67, 9)  (shoulder, plane x = 67)
7. line to (72.96886, 9)  (collar, diameter 18)
8. concave arc R17.1, centre (82.729, 23.041), to (89.40919, 7.29981)
9. convex arc R40.502, centre (103.95, -30.502), to (125.58325, 3.73854)  (barrel grip, max diameter 20.0 at x = 103.95)
10. convex arc R4.1, centre (123.9, 0), to (128, 0)  (spherical end, a sphere radius 4.1 centred on the grip axis at
    x = 123.9; it meets step 9 with a kink)
11. line back to (48, 0).
Steps 7/8 and 8/9 meet with kinks (not tangent); use the given points.

**C. Bore.** A plain through bore, diameter 10, on the X axis from x = 0 to x = 28. At the bottom face x = 0 the bore
has a 120 degree (included) countersink: a cone from diameter 13.4641 at x = 0 to diameter 10 at x = 1.
No set-screw hole, no thread, no keyway.

All edges not mentioned are sharp (no other rounds).

**Source artefact (do not reproduce):** the master file contains 16 empty, zero-size closed shells (96 faces of zero
area) at the point (48.0, -53.626, -6.249). They have no volume. A clean rebuild has one shell and about 32-42 faces.

## 4. Acceptance targets

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Crank handle | 39620 | 12592.2 | 48.96 | -48.59 | 0.00 | 0.000 | 128.000 | -110.000 | 15.500 | -15.500 | 15.500 | 42 (+96 empty) |

Volume note: B-rep integration on the master gives 39621.1, triangulated integration 39613.6; take 39620 +/- 0.05 %.

Check values: hub diameter 28, hub length 28 (x = 0 to 28), bore 10, collar diameter 31, crank radius (hub axis to grip
axis) 100, overall length along X 128, grip barrel diameter 20, grip length from the arm's outer face 128 - 48 = 80,
boss diameter 16, overall extent along Y 125.5 (from -110 to 15.5).

## 5. Undetermined items

- Draft angles and casting tolerances: none are modelled beyond the 0.86 degree taper of the arm faces.
- Material (iron, black powder coat; grip zinc-plated steel) is from the product data only; the master has the grip and
  arm as one solid, keep it so.
