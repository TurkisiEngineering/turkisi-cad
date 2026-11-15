# Design specification: two-start ball screw shaft, 3 ft long (P14)

A solid round steel shaft with two identical helical ball grooves (two starts, right-hand) running its full length, and
a 45 degree chamfer at each end. This document is the only source for the rebuild. Every value was measured from the
master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (mm in brackets where useful; 1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - The **shaft axis is the Z axis**. The shaft runs from the end face **Z = -18** to the end face **Z = +18**
    (length 36), centred on the origin.
  - Polar angle theta is measured in the XY plane from +X towards +Y (counter-clockwise seen from +Z).
- Notation: "(r, z)" = a profile in the half-plane Y = 0, X > 0 (theta = 0), r = distance from the Z axis.
- One body, one solid. Name: **P01 Screw shaft**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Two-start ball screw shaft (no nut, no pins) | custom |

## 3. Data

| Item | Value |
|---|---|
| Outside diameter | **0.655** (radius 0.3275) [16.637 mm] |
| Length | **36.000** (Z = -18 to +18) [914.4 mm] |
| Number of groove starts | **2**, identical, 180 degrees apart |
| Hand | right-hand |
| Lead (axial advance of one groove per turn) | **0.376** [9.5504 mm] |
| Pitch (axial distance between neighbouring grooves) | **0.188** [4.7752 mm] |
| Groove form (axial section) | circular arc, radius **0.0465** [1.1811 mm], centre on the outside diameter (r = 0.3275) |
| Groove width at the outside diameter | 0.093 |
| Groove depth | 0.0465, root diameter 0.562 |
| Land (outside-diameter strip) axial width | 0.095 |
| End chamfers | 0.0655 x 45 degrees, both ends |
| Centre holes, flats, cross holes | none |

## 4. Geometry of P01 (build in this order)

**F1. Blank.** Solid of revolution about Z. (r, z) outline: (0, -18) - (0.262, -18) - (0.3275, -17.9345) -
(0.3275, 17.9345) - (0.262, 18) - (0, 18). This is a cylinder diameter 0.655 with a 0.0655 x 45 degree chamfer at both
ends; the flat end faces are full discs of radius 0.262.

**F2. Groove 1.** Cut the solid swept by a circle of radius 0.0465 lying in the half-plane through the axis, by a
right-hand screw motion about Z with lead 0.376: rotating the circle by an angle phi about +Z (counter-clockwise seen
from +Z) raises it along +Z by 0.376 x phi / 360. Its centre at theta = 0 is the point (r, z) = (0.3275, 0.046)
(and every z = 0.046 + k x 0.376, k integer). Run the cut over the whole length and beyond both ends, so the groove runs
out through both chamfers (it does not reach the end faces: groove bottom r = 0.281 > 0.262).

**F3. Groove 2.** The same as F2, turned 180 degrees about Z (equivalently shifted by one pitch 0.188 along Z): its
centre at theta = 0 is at z = 0.046 + 0.188 + k x 0.376.

Resulting check pattern: in the half-plane theta = 0 the groove centres are at z = 0.046 + k x 0.188 (all k, both
grooves together); at theta = 90 degrees they are at z = 0.140 + k x 0.188; at theta = 180 degrees again at
z = 0.046 + k x 0.188. The lands (cylinder r = 0.3275) span, at theta = 0, z from 0.0925 to 0.1875 (+ k x 0.188),
i.e. from 0.046 + 0.0465 to 0.046 + 0.188 - 0.0465.

All groove edges are sharp (no rounds). Nothing else is cut.

**Source note:** the master's groove surface is a spline approximation of this helical sweep; it deviates from the
exact form by up to 0.00012 in (0.003 mm). Build the exact form.

## 5. Acceptance targets

| ID | Volume in3 | Area in2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Screw shaft | 10.8662 | 90.7308 | 0.0000 | 0.0000 | 0.0017 | -0.3275 | 0.3275 | -0.3275 | 0.3275 | -18.0000 | 18.0000 | 394 |

Same in mm: volume 178065.8 mm3, area 58535.9 mm2, CoM (0, 0, 0.043), bbox X / Y +/-8.3185, Z +/-457.2.

Volume note: B-rep integration on the master gives 178065.8 mm3; integrating the exact form of this specification gives
178089.9 mm3 (+0.014 %) and a centre of mass exactly on the origin (the exact form has a two-fold symmetry axis). Either
is within tolerance. The face count 394 is the master's (each land half-turn is a separate face); a clean rebuild may
have far fewer faces.

Check values: outside diameter 0.655, root diameter 0.562, length 36.000, lead 0.376, pitch 0.188, 2 starts.

## 6. Undetermined items

- The ball nut, the reversing pins and the balls are not part of this model.
- Material and hardness are product data only.
