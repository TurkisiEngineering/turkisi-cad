# Design specification: cold plate with a four-pass bent tube (P13)

A liquid cold plate: a rectangular metal plate with four parallel open channels in its top face, and one continuous
bent tube that lies in the channels, making four passes along the plate with three U-bends, both ends leaving the plate
on the same side as straight legs. This document is the only source for the rebuild. Every value was measured from the
master 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm (1 in = 25.4 mm exactly).
- **Global frame (use exactly, no realignment):**
  - The plate is centred on the origin in X and Y: X from -3 to 3 (length 6), Y from -1.75 to 1.75 (width 3.5).
  - **Z is the thickness direction.** The channelled top face is z = 0.1875; the flat bottom face is z = -0.3125.
  - The tube centreline lies in the plane **z = 0**; the passes run parallel to **X** at y = 1.5, 0.5, -0.5, -1.5.
    The two straight legs leave the plate toward **+X** and end at x = 5.
- Every body is modelled in place in this frame (identity placement).

## 2. Body list

2 bodies, 2 distinct parts.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Plate with four channels | custom | aluminium |
| P02 | 1 | Four-pass tube (one bent tube) | custom | 316 stainless steel |

The tube touches the plate face to face in the channel bottoms (zero clearance, no overlap). Keep the two as separate
solids; no fittings, no filler, no bonding layer.

## 3. P01 Plate (one solid, 22 faces)

**P1. Block.** Rectangular block X -3..3, Y -1.75..1.75, Z -0.3125..0.1875 (6 x 3.5 x 0.5). All block edges sharp.

**P2. Channels.** Four identical channels, each running straight along X through the full length (open at both end
faces x = ±3), centred at y = y_c with y_c = 1.5, 0.5, -0.5, -1.5 (pitch 1.0). Cross-section of each channel in a
plane normal to X ("U" profile, open at the top):
- two parallel side walls y = y_c ± 0.1875 (channel width 0.375) from the top face z = 0.1875 down to z = 0;
- a half-cylinder bottom of radius 0.1875 about the line (y = y_c, z = 0), parallel to X, reaching down to z = -0.1875.
The bottom is tangent to both side walls. Channel edges at the top face are sharp.

Resulting checks: material under each channel bottom 0.125 (z -0.3125 to -0.1875); land between channels 0.625 wide;
outer lands 0.0625 wide (y 1.6875 to 1.75 and mirrored); the top face consists of 5 separate strips.

## 4. P02 Four-pass tube (one solid)

**Cross-section:** a round tube, outside diameter 0.375 (R0.1875), wall 0.02, inside diameter 0.335 (R0.1675),
constant along the whole path. Hollow through; both ends open, cut square (flat annular end faces normal to X at x = 5).

**Centreline** (all in the plane z = 0), as a continuous chain of straight lines and tangent arcs, starting at the upper
leg end:
1. line from (5, 1.5) to (-3, 1.5)  (upper leg + pass 1, length 8)
2. arc R0.5, centre (-3, 1.0), from (-3, 1.5) through (-3.5, 1.0) to (-3, 0.5)  (U-bend 1, 180°)
3. line from (-3, 0.5) to (3, 0.5)  (pass 2, length 6)
4. arc R0.5, centre (3, 0), from (3, 0.5) through (3.5, 0) to (3, -0.5)  (U-bend 2)
5. line from (3, -0.5) to (-3, -0.5)  (pass 3, length 6)
6. arc R0.5, centre (-3, -1.0), from (-3, -0.5) through (-3.5, -1.0) to (-3, -1.5)  (U-bend 3)
7. line from (-3, -1.5) to (5, -1.5)  (pass 4 + lower leg, length 8).
Total centreline length 28 + 1.5π = 32.71239. Sweep the annular cross-section along it (the bends are exact toroidal
sections, centreline radius 0.5).

So the tube's straight passes lie exactly in the four plate channels (tube axis = channel bottom axis, tube OD = channel
width), the tube top is flush with the plate top z = 0.1875, the U-bends stand off the plate ends (outer bend extreme at
x = ±3.6875), and the two legs project 2 beyond the plate end x = 3.

## 5. Acceptance targets (from the master)

| ID | Volume in3 (mm3) | Area in2 (mm2) | CoM x, y, z (in) | Bbox X | Bbox Y | Bbox Z | faces |
|---|---|---|---|---|---|---|---|
| P01 plate | 7.48714 (122692.25) | 64.6329 (41698.55) | 0, 0, -0.09469 | -3 .. 3 | -1.75 .. 1.75 | -0.3125 .. 0.1875 | 22 |
| P02 tube | 0.72966 (11956.98) | 73.0106 (47103.52) | 0.32881, 0, 0 | -3.6875 .. 5 | -1.6875 .. 1.6875 | -0.1875 .. 0.1875 | 38 |

**Whole assembly:** 2 bodies; volume 8.21680 in3 (134649.24 mm3); area 137.6435 in2 (88802.07 mm2); centre of mass
(0.02920, 0, -0.08628) in; bounding box X -3.6875 .. 5, Y -1.75 .. 1.75, Z -0.3125 .. 0.1875 (mm: X -93.6625 .. 127,
Y -44.45 .. 44.45, Z -7.9375 .. 4.7625). No overlap between the bodies (contact only).

Check values: plate 6 x 3.5 x 0.5; channel width 0.375, depth 0.375 from the top, pitch 1.0; tube OD 0.375, wall 0.02;
bend centreline radius 0.5; tube ends at x = 5.

The face counts are those of the master; the master splits the tube faces into more patches than needed (38). Any
patch layout of the same surfaces is fine.

## 6. Undetermined items and source notes

- **Source artefact (do not reproduce):** the master plate carries 22 empty, zero-area closed shells (132 faces) at
  the point (1.5, -0.875, 0.1339) in. They have no volume. A clean rebuild has one shell per body.
- No tube end chamfers, no fittings, no fastening holes and no channel edge breaks are modelled. Keep it so.
- Nothing else is undetermined.
