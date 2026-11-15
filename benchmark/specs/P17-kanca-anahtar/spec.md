# Design specification: hook spanner wrench for side-slot round nuts (P17)

A flat one-piece hook spanner: a C-shaped head with a short pin that engages a slot on the side of a round nut, and a
straight handle with rounded long edges, a semicircular end and an obround hanging slot. This document is the only
source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (mm values in brackets where useful; 1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - The wrench is a plate of thickness 0.12 lying between the planes **Y = -0.06 and Y = +0.06** (symmetric about Y = 0).
  - Its outline is drawn in the **XZ plane** and extruded along Y. The handle runs along **+X**; the head is at -X.
  - The handle's upper straight edge is the line **Z = 0**; the whole part lies in Z <= 0.
- Notation: "(x, z)" = a point of the outline in the XZ plane.
- One body, one solid. Name: **P01 Spanner**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Hook spanner wrench | custom |

## 3. Geometry of P01 (build in this order)

**F1. Outline, extruded symmetric 0.12 along Y (Y = -0.06 to +0.06).** Closed outline in (x, z), counter-clockwise
seen from -Y, segments in this order (the last closes on the start):

1. line from (-1.354007, 0) to (1.970605, 0) (handle top edge);
2. arc R0.194895, centre (1.970605, -0.194895), convex, from (1.970605, 0) through (2.165500, -0.194895) to
   (1.970605, -0.389790) (semicircular handle end, tangent to both handle edges);
3. line to (-0.703984, -0.389790) (handle bottom edge; handle width 0.389790);
4. concave arc R0.468750 (15/32), centre (-0.703984, -0.858540), from (-0.703984, -0.389790) to (-1.024250, -0.516259)
   (tangent to step 3);
5. convex arc R0.707013, centre (-1.507307, 0), to (-2.159435, -0.273121) passing through its lowest point
   (-1.507307, -0.707013) (the outer back of the head; tangent to step 4 and step 6);
6. convex arc R0.078125 (5/64), centre (-2.087375, -0.242941), to (-2.104284, -0.166668) (round tip of the hook;
   passes through the leftmost point x = -2.165500);
7. line to (-1.931443, -0.128350) (top face of the hook, tangent to step 6);
8. line to (-1.864243, -0.193720) (front face of the pin; 56.710 degrees to step 7's face);
9. line to (-1.922674, -0.215905) (underside of the pin, length 0.0625; 65.000 degrees to the front face);
10. concave arc R0.312500 (5/16), centre (-1.696750, 0) (on the line Z = 0), from (-1.922674, -0.215905) to
    (-1.411824, -0.128350) (the jaw that fits a 0.625 diameter nut; the material is outside this circle);
11. line back to (-1.354007, 0).

The pin tip (-1.864243, -0.193720) and the jaw arc's end points lie inside the R0.3125 jaw circle's extent; steps 7-9
form the pin that enters the nut's slot. Points (-1.931443, -0.128350) and (-1.411824, -0.128350) are at the same Z.

**F2. Obround slot, through Y.** Two semicircle centres (1.918717, -0.194895) and (1.944702, -0.194895), radius
0.064965 (slot width 0.129930, centre distance 0.025985), joined by the tangent lines Z = -0.129930 and Z = -0.259860.
The slot is centred on the handle's mid-height Z = -0.194895. Through the full thickness, plain (no chamfer).

**F3. Edge rounds R0.015625 (1/64) on the handle.** On both faces (Y = +0.06 and Y = -0.06), round the outline edges
of the handle with radius 0.015625:
- the top edge (Z = 0) from x = -0.441484 to x = 1.970605,
- the semicircular end (step 2), all the way round (toroidal round),
- the bottom edge (Z = -0.389790) from x = 1.970605 back to x = -0.441484.
So the round centre lines are at Y = +/-0.044375 and Z = -0.015625 (top) / Z = -0.374165 (bottom); around the end
they are circles of radius 0.179270 about the end centre. The side face of the semicircular end is therefore a cylinder
R0.194895 only between Y = -0.044375 and +0.044375.

**F4. Run-out of the rounds (4 places).** At x = -0.441484 each of the four straight rounds ends in a short conical
run-out that brings the edge back to sharp at x = -0.478189: about the same centre line (parallel to X), the surface is
a cone whose radius grows from 0.015625 at x = -0.441484 at 10 degrees half-angle,
r(x) = 0.015625 + tan(10 degrees) x (-0.441484 - x), and reaches the original sharp corner (r = 0.022097) at
x = -0.478189. Remove the corner material outside this cone between those two x values. For x < -0.478189 the plate
edges are sharp.

**F5. Everything else is sharp:** the whole head (steps 3-11 except the run-out zone), the slot edges and the pin.

**Source artefact (do not reproduce):** the master solid carries 19 empty micro-boxes (114 faces of zero area) at the
point (-1.39213, 0.01320, -0.12491). They have no volume. A clean rebuild has 27 faces.

## 4. Acceptance targets

| ID | Volume in3 | Area in2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Spanner | 0.208501 | 4.612036 | -0.088238 | 0.000000 | -0.251719 | -2.165500 | 2.165500 | -0.060000 | 0.060000 | -0.707013 | 0.000000 | 27 (+114 empty) |

Same in mm: volume 3416.715 mm3, area 2975.501 mm2, CoM (-2.2412, 0, -6.3936), bbox X +/-55.0037, Y +/-1.524,
Z -17.9581 .. 0.

Check values: overall length 4.331 (110.007 mm); thickness 0.12; handle width 0.38979; jaw radius 0.3125 (fits a
0.625 diameter circle); pin underside 0.0625 long; handle-end radius 0.194895; head height 0.707013.

## 5. Undetermined items

- Material and finish: product data only.
- The angle the pin makes is given by its vertices; no separate design angle is stated in the master.
