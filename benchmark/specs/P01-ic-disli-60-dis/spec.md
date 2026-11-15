# Design specification: internal spur gear, module 0.5, 60 teeth (P1)

A flat steel ring with 60 involute teeth cut on its inside. This document is the only source for the rebuild. Every
value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - The gear axis is the Z axis. The ring is symmetric about the XY plane: faces at Z = -2.5 and Z = +2.5.
  - Angular position: one **tooth** (material) is centred on the +X axis (polar angle 0). Polar angle is measured from
    +X towards +Y.
- One body, one solid. Name: **P01 Gear**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Internal spur gear | custom |

## 3. Gear data

| Item | Value |
|---|---|
| Module m | 0.5 |
| Number of teeth z | 60 |
| Pressure angle | 20 |
| Pitch diameter d = m z | 30.000 |
| Base circle diameter d cos 20 | 28.19078 (radius 14.09539) |
| Profile shift | 0 (measured: tooth thickness = space width = 0.78540 = pi m / 2 on the pitch circle) |
| Tip (inner) diameter d - 2m | 29.000 (radius 14.5) |
| Root diameter d + 2.5m | 31.250 (radius 15.625) |
| Outside diameter | 50.000 |
| Face width | 5.000 (Z = -2.5 to 2.5) |
| Helix | none (straight spur teeth, parallel to Z) |
| Angular pitch | 6 |

## 4. Geometry of P01 (build in this order)

**F1. Blank ring.** Annulus, inner radius 14.5, outer radius 25, from Z = -2.5 to Z = 2.5.

**F2. Bore-edge rounds.** The two circular edges of the inner cylinder (radius 14.5) at Z = +2.5 and Z = -2.5 are
rounded with radius **0.16775**. The round surfaces are tori about Z: tube-centre circle radius 14.66775 at
Z = +/-2.33225, tube radius 0.16775. The outer edges (radius 25) are sharp.

**F3. Tooth spaces, 60 places.** Cut 60 tooth spaces through the full face width. Spaces are centred at polar angles
3 + 6k (k = 0..59); teeth are centred at 6k. Each flank is an exact involute of the base circle radius 14.09539,
running from the tip circle (r = 14.5) to the root circle (r = 15.625). For the tooth centred at polar angle 0, its two
flanks are at polar angle +/- theta(r):

    theta(r) = 180/(2 z) + inv(alpha_r) - inv(20 deg)   [in radians: pi/120 + inv(alpha_r) - 0.0149044]
    alpha_r  = arccos(14.09539 / r),   inv(a) = tan(a) - a

Check values (half tooth angle theta, and the flank point for the +Y flank of the tooth on +X):

| r | theta (deg) | half space (deg) | flank point (x, y) |
|---|---|---|---|
| 14.500 (tip) | 0.90543 | 2.09457 | (14.49819, 0.22913) |
| 14.750 | 1.17573 | 1.82427 | (14.74689, 0.30265) |
| 15.000 (pitch) | 1.50000 | 1.50000 | (14.99486, 0.39265) |
| 15.250 | 1.86826 | 1.13174 | (15.24189, 0.49717) |
| 15.500 | 2.27395 | 0.72605 | (15.48779, 0.61500) |
| 15.625 (root) | 2.48930 | 0.51070 | (15.61026, 0.67864) |

The space bottom is the root circle arc r = 15.625 between the two flanks (angular width 1.02140, centred on the
space). **Root corners are sharp** (flank meets root circle with no fillet) and **tip corners are sharp** (flank meets
the tip circle r = 14.5 with no round) in 59 of the 60 spaces.

**F4. Root fillets in one space only (source condition, reproduce it).** The space centred at polar angle **-3**
(between the tooth on +X and the tooth at -6) has root fillets of radius **0.16775** on both sides, parallel to Z,
tangent to the flank and to the root circle:
- fillet next to the flank at polar angle -1.5 (pitch circle): centre (15.43767, -0.77774), tangent to the flank at
  (15.51429, -0.62851) (r = 15.527) and to the root circle at (15.60542, -0.77774);
- fillet next to the flank at polar angle -4.5: centre (15.43440, -0.84019), tangent to the root circle at
  (15.60190, -0.84931) and to the flank at (15.49499, -0.99662).
The other 59 spaces have no root fillet.

**F5. Rounds at the tooth tips.** The F2 rounds remain only on the tip lands (they are trimmed by the flanks): each tip
land keeps its R0.16775 toroidal round at both faces; the flank-to-face edges are sharp.

No bore keyway, holes, chamfers or markings exist.

## 5. Acceptance targets

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Gear | 6272.1 | 4231.20 | 0.000 | 0.000 | 0.000 | -25.000 | 25.000 | -25.000 | 25.000 | -2.500 | 2.500 | 370 |

Volume note: measured by triangulated integration (6272.0) and by an exact rebuild to this specification (6272.17); a
B-rep property calculation on the master file reads 6258.3, which is a known integration error on the flank surfaces
and is not the target. Centre of mass is on the axis within 0.001.

Check values: 60 teeth; tip diameter 29.0; root diameter 31.25; outside diameter 50.0; face width 5.0; tooth
thickness on the pitch circle 0.7854; pitch 6 degrees.

## 6. Undetermined items

None for the geometry. Material (steel, black oxide) is from the product data, not from the 3D master.
