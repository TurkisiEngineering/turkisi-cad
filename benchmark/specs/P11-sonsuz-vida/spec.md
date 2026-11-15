# Design specification: steel worm, module 1, single start, 6 mm bore, with set screw (P11)

A cylindrical steel worm (single-start, right-hand thread, module 1) with a plain through bore and one radial tapped
hole that holds a hex socket set screw. This document is the only source for the rebuild. Every value was measured
from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - The **worm / bore axis is the Z axis**. The worm runs from the end face Z = -16 to the end face Z = +16.
  - The **set-screw hole axis** is the line X = 0, Z = 11, parallel to Y; the hole opens on the **+Y** side only.
  - Polar angle theta is measured in the XY plane from +X towards +Y (counter-clockwise seen from +Z).
- Notation: "(r, z)" = a profile in the half-plane Y = 0, X > 0 (theta = 0), r = distance from the Z axis.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Worm (core, thread, bore, set-screw hole; one solid) | custom |
| H1 | 1 | Hex socket set screw, M4, seated in the radial hole | bought-in hardware |

Two separate solids. They touch (the screw fills the hole at the same diameter) but do not overlap.

## 3. Worm data

| Item | Value |
|---|---|
| Module | 1 |
| Number of starts | 1 |
| Hand | right-hand |
| Pitch (reference) diameter | 16.000 (radius 8) |
| Outside (tip) diameter | 18.000 (radius 9) |
| Root diameter | 13.68596 (radius 6.84298) |
| Lead = axial pitch | **3.144821** (measured; note it is 0.1 % larger than pi) |
| Lead angle on the pitch diameter | 3.580 (tan = 3.144821 / (pi x 16)) |
| Axial pressure angle (flank angle in the axial section) | 20.075 below r = 8, 20.048 above r = 8 (straight segments, see F2) |
| Axial tooth thickness on the pitch diameter | 1.57080 (= pi / 2) |
| Axial space width on the pitch diameter | 1.57402 (= lead - pi / 2) |
| Face length | 32.000 (Z = -16 to +16) |

## 4. Geometry of P01 (build in this order)

**F1. Core.** A solid cylinder about Z, radius 6.84298 (the root radius), long enough to pass both end faces.

**F2. Thread tooth (helical).** One tooth profile in the half-plane Y = 0, X > 0, swept by a right-hand screw motion
about Z: rotating the profile by an angle phi about +Z (counter-clockwise seen from +Z) raises it along +Z by
3.144821 x phi / 360. Run the sweep over enough turns to cover Z = -16 .. +16 completely (the ends are trimmed in F3).
Unite with F1.

The profile is symmetric about its centre line. At theta = 0 the tooth centre lines lie at

    z_c = 2.63451 + k x 3.144821   (k integer)

and at polar angle theta the same tooth is at z_c + 3.144821 x theta / 360. The tooth's half-thickness along Z at
radius r is:

    h(r) = 0.78540 + 0.36545 x (8 - r)    for 6.84298 <= r <= 8
    h(r) = 0.78540 + 0.36491 x (8 - r)    for 8 <= r <= 9

so each flank is two straight segments in the axial section, meeting at r = 8 (a 0.03 degree change of slope).
Profile vertices for the tooth with k = 0 (r, z), closed polygon:

| Vertex | r | z | note |
|---|---|---|---|
| a | 6.84298 | 1.42628 | root, lower flank |
| b | 8.00000 | 1.84911 | pitch circle, lower flank |
| c | 9.00000 | 2.21402 | tip, lower flank |
| d | 9.00000 | 3.05500 | tip, upper flank |
| e | 8.00000 | 3.41991 | pitch circle, upper flank |
| f | 6.84298 | 3.84274 | root, upper flank |

(For a clean union, extend the profile slightly below r = 6.84298 into the core along the same flank lines.)
Check values: tooth axial width 2.41647 at the root, 1.57080 at r = 8, 0.84098 at the tip; root land (space at
r = 6.84298) 0.72835 wide; tip land (r = 9) is a cylinder surface 0.84098 wide. Root and tip corners are sharp: no
fillets or rounds anywhere on the thread.

**F3. End trimming (keep only the material inside this envelope).** Intersect the worm with a solid of revolution about Z
whose (r, z) outline is:
- end planes Z = +16 and Z = -16, from r = 0 to r = 6.84298;
- at each end a conical chamfer inclined **30 degrees to the end plane** (half-angle 60 degrees to the axis), starting on
  the end plane at r = 6.84298 and reaching r = 9 at Z = +/-14.75466:
  z = +(16 - 0.577350 x (r - 6.84298)) at the +Z end, z = -(16 - 0.577350 x (r - 6.84298)) at the -Z end;
- the cylinder r = 9 between Z = -14.75466 and +14.75466.
Result: flat end faces are full annuli out to the root radius 6.84298; every tooth that reaches an end is cut by the
30 degree cone; the thread's start and end are not otherwise finished.

**F4. Bore.** Through bore diameter **6.000** on the Z axis. Both bore edges have a **45 degree x 0.45** chamfer: a cone from
diameter 6.90 on the end plane (Z = +/-16) to diameter 6.00 at Z = +/-15.55.

**F5. Set-screw hole.** Plain hole diameter **4.000** (the M4 thread is not modelled; the hole is at the nominal major
diameter), axis X = 0, Z = 11, parallel to Y, from the bore out through all material on the +Y side (it breaks through
the bore wall and out through the thread teeth). No hole on the -Y side; no counterbore or chamfer.

No keyway, flats, markings or other holes.

## 5. Geometry of H1 (set screw)

A plain cylinder (thread not modelled) on the hole axis (X = 0, Z = 11, along Y):
- diameter **4.000** from Y = 3.5 to Y = 6.34298;
- inner end: 45 degree chamfer, cone from diameter 4.0 at Y = 3.5 to diameter 3.0 at Y = 3.0; flat end face diameter 3.0
  at **Y = 3.0** (this end sits at the bore surface line X = 0);
- outer end: 45 degree chamfer, cone from diameter 4.0 at Y = 6.34298 to diameter 3.0 at Y = 6.84298; flat end face at
  **Y = 6.84298** (flush with the root radius, below the thread tips);
- hex socket in the outer face: regular hexagon **2.000 across flats** (2.30940 across corners), two flats parallel to the
  XY plane at Z = 10 and Z = 12, corners at X = +/-1.15470 on Z = 11; depth **1.000** (flat bottom at Y = 5.84298).
Overall length 3.84298.

## 6. Acceptance targets

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Worm | 5415.1 | 3989.6 | -0.014 | -0.087 | -0.130 | -9.000 | 9.000 | -9.000 | 9.000 | -16.000 | 16.000 | 63 |
| H1 Set screw | 41.948 | 72.341 | 0.000 | 4.804 | 11.000 | -2.000 | 2.000 | 3.000 | 6.843 | 9.000 | 13.000 | 15 |
| Assembly | 5457.0 | 4061.9 | -0.014 | -0.049 | -0.044 | -9.000 | 9.000 | -9.000 | 9.000 | -16.000 | 16.000 | |

Volume note (P01): B-rep integration on the master 5415.09, triangulated integration 5414.03; an exact rebuild to this
specification gives 5414.76. Take 5415 +/- 0.05 %. The P01 centre of mass is off-axis only because of the thread phase
and the set-screw hole; it comes from triangulated integration.

Check values: 18.000 outside diameter, 13.686 root diameter, 6.000 bore, 32.000 length, set-screw hole diameter 4.000
with its axis 5.000 from the +Z end face, lead 3.144821 right-hand.

## 7. Undetermined items

- Thread of the set screw and of its hole: not modelled in the master; leave both plain.
- Tooth flank form beyond the axial section (whether the flank is an involute or a straight-sided axial profile):
  the master's axial section is the two straight segments given in F2 to within 0.0002 mm; build it that way.
- Material (steel) and heat treatment are product data only.
