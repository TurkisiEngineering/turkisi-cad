# Design specification: calibration plate (P0)

A flat rectangular plate with four corner through-holes, one central blind round pocket and rounded vertical corners.
This document is the only source for the rebuild. It is a calibration part: every value is exact by design.

## 1. Units and global frame

- **Units: millimetres.**
- **Global frame (use exactly, no realignment):**
  - The plate bottom face lies on the XY plane (Z = 0). The plate occupies Z = 0 to Z = 10.
  - The plate is centred on the origin in X and Y. Its length runs along X (X = -50 to 50), its width along Y
    (Y = -30 to 30).
  - +Z is up; the pocket opens on the top face Z = 10.
- One body, one solid. Name: **P01 Plate**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Plate | custom |

## 3. Geometry of P01 (build in this order)

**F1. Plate block.** Rectangle in the XY plane, X = -50 to 50, Y = -30 to 30, extruded from Z = 0 to Z = 10.

**F2. Corner rounds.** The four vertical edges at the corners (X = +/-50, Y = +/-30, parallel to Z) are rounded with
radius 3. The round centres are at (X, Y) = (+/-47, +/-27). The top and bottom outline edges stay sharp.

**F3. Corner holes.** Four plain through-holes, diameter 6, axes parallel to Z, through the full thickness (Z = 0 to 10).
Hole centres at (X, Y) = (-42, -22), (42, -22), (-42, 22), (42, 22), i.e. 8 from each adjacent outer edge.
Hole-centre spacing 84 along X and 44 along Y. No chamfer, counterbore or countersink.

**F4. Central pocket.** A blind cylindrical pocket, diameter 20, axis on the Z axis (X = 0, Y = 0), cut from the top face
Z = 10 down to a flat floor at Z = 6 (depth 4). The floor is flat and the floor-to-wall edge is sharp (no corner
radius, no drill point). The pocket rim at Z = 10 is sharp.

All other edges are sharp.

## 4. Acceptance targets

Measured on the reference geometry in this frame. A one-to-one rebuild should match volume within 0.5 %, centre of mass
within 0.05 mm, bounding box within 0.01 mm. Face count is for information only.

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Plate | 57535.133 | 15912.159 | 0.0000 | 0.0000 | 4.9345 | -50.000 | 50.000 | -30.000 | 30.000 | 0.000 | 10.000 | 16 |

Check values: 4 holes of diameter 6; pocket diameter 20, depth 4 (floor plane Z = 6); corner radius 3; plate
100 x 60 x 10.

## 5. Undetermined items

None. The part has no threads, chamfers or draft.
