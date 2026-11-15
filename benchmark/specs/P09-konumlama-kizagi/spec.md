# Design specification: manual dovetail positioning slide with lead screw and handwheel

Hand-operated linear positioning slide, 1.5 in travel, 0.05 in of travel per handwheel turn. A dovetail carriage slides
on a dovetail base and is driven by a lead screw turned by a handwheel with a crank handle. This document is the only
source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in inches or in millimetres (multiply every value by 25.4). The origin and the axes do not change either way.
- **Global frame (use exactly, no realignment):**
  - +Y is up. The carriage top is the highest flat face (y = 0.41044). The base underside (the mounting face on the
    machine table) is the plane **y = -0.39456**. Y = 0 is not on any face.
  - Z is the slide (travel) direction. **z = 0 is the end face of the base opposite the handwheel**; the base runs
    from z = 0 to z = 4.0 and the handwheel is at the +Z end.
  - X is across the slide. The slide is symmetric about the plane x = 0 (except the screw thread and one tiny source
    artefact, section 4 P02).
  - **The lead screw axis is the line x = 0, y = 0.04244, parallel to Z.** The handwheel shares this axis.
- **Y values:** most heights are round offsets from the screw axis height Y0 = 0.0424438 (for example base underside
  = Y0 - 0.437, base top = Y0 + 0.313). The document gives absolute y to 5 decimals; that rounding (< 0.000005 in) is
  far below any tolerance.
- **Profile coordinate conventions:**
  - "(x, y)" = profile in a plane normal to Z (a cross-section), extruded along Z between the stated z limits.
  - "(z, r)" = revolve profile, r being the radius from the stated axis, z the global z.
  - "(r, w)" = revolve profile in a hardware local frame (radius r, axial coordinate w).
- All custom parts (P01 to P08) are located directly in the global frame; their coordinates are global. The four
  screws are defined once in a local frame and placed by a pose table (section 5).
- Arc notation: "arc R c=(a,b) to (p,q)" is a circular arc of radius R centred at (a,b) from the current point to (p,q),
  taking the minor arc.

## 2. Product description and operation

An aluminium base of rectangular section has a dovetail way along its full length (Z) and a deeper centre groove under
the way. Two countersunk holes in the groove floor take the fasteners that hold the base on a machine table. A thin
end plate closes the z = 0 end; a thicker bearing end block closes the z = 4.0 end. Each is held by two button-head
screws threaded into the base end faces.

The carriage (table) is a dovetail slide that sits in the base way. Four thin wear strips (low-friction plastic in the
real product) are part of the carriage solid and are the only surfaces that touch the base. The carriage top has four
small tapped holes on its centre line for mounting work, and a large round hole in its middle that holds a round drive
nut. The nut reaches down into the base groove and engages the lead screw.

The lead screw (1/4 in diameter, pitch 0.05, right-hand) runs along the screw axis, is supported in the end block, and
carries the handwheel on its +Z end. A crank handle stands on the outer face of the handwheel.

**Simplifications that exist in the source geometry and must be reproduced:**
- The drive nut is a plain solid cylinder with **no bore and no thread**. The lead screw passes straight through it
  (volumetric overlap, section 5).
- The handwheel hub is solid, with **no bore**. The plain screw shaft end enters 0.313 into the hub (overlap, section 5).
- The lead screw thread **is modelled** (real helical groove). No other thread is modelled: the carriage holes, the
  base end holes and the button-head screws are plain cylinders at the thread major diameter.
- The end block bore is empty: no bearing bush, collar or retaining ring exists.
- No knurl on the handwheel, no drive recess in the screw heads, no set screw in the nut.
- The four wear strips are part of the carriage solid, not separate bodies.

## 3. Part list

8 distinct custom parts and 1 distinct hardware item, 9 distinct, **12 bodies in total**.

| ID | Qty | Name | Type | Material / finish (where known) |
|---|---|---|---|---|
| P01 | 1 | Base with dovetail way | custom | Aluminium, bare |
| P02 | 1 | Carriage (table) with integral wear strips | custom | Aluminium, bare |
| P03 | 1 | Drive nut, round | custom | Copper-coloured (bronze look) |
| P04 | 1 | Bearing end block (handwheel end) | custom | Aluminium, bare |
| P05 | 1 | End plate (far end) | custom | Aluminium, bare |
| P06 | 1 | Lead screw, 0.25 dia, pitch 0.05 RH | custom | Stainless steel |
| P07 | 1 | Handwheel | custom | Aluminium, bright, knurled rim in the product (knurl not modelled) |
| P08 | 1 | Crank handle | custom | Aluminium, bright |
| H1 | 4 | Button-head screw, 0.164 dia x 0.6871 shank | hardware | Steel |

Aluminium base and carriage and the stainless lead screw are stated by the product data. Other finishes come from the
product photographs; the 3D geometry carries no colour.

## 4. Part geometry

All coordinates are global. Features are listed in an order that constructs each part.

### P01 Base (one solid, 34 faces in the original)

**F1. Block**, extrude z = 0 to 4.0. Cross-section in (x, y), closed polygon:
(-1.25, -0.39456), (1.25, -0.39456), (1.25, 0.35544), (0.66249, 0.35544), (0.87900, -0.01956), (0.56200, -0.01956),
(0.56200, -0.13456), (-0.56200, -0.13456), (-0.56200, -0.01956), (-0.87900, -0.01956), (-0.66249, 0.35544),
(-1.25, 0.35544), close.

This is a 2.5 wide x 0.75 high block with:
- a dovetail way open at the top: top opening x = +/-0.66249 at y = 0.35544, floor y = -0.01956 (0.375 below the top),
  floor width x = +/-0.87900. The flanks lean outward going down at **60 degrees to the horizontal** (undercut);
- a centre groove in the way floor: x = +/-0.562, floor y = -0.13456 (0.115 below the way floor, 0.26 above the
  underside). All edges sharp.

**F2. Two countersunk mounting holes**, axes parallel to Y at (x, z) = (-0.343, 0.5) and (0.343, 3.5). From the groove
floor down: countersink cone, dia 0.385 at y = -0.13456, 82 degrees included (41 degrees half angle), down to dia 0.198
at y = -0.24212; then straight hole dia 0.198 through the underside y = -0.39456. Revolve profile about each hole axis
in (y, r): (-0.13456, 0.1925), (-0.24212, 0.099), (-0.39456, 0.099). The countersink opens upward (screws are inserted
from the groove side).

**F3. Four end holes** (plain, at the 0.164 major diameter of the screws), dia 0.164, axes parallel to Z at
(x, y) = (+/-1.031, -0.01956):
- two from the z = 0 face to flat bottoms at z = 0.625;
- two from the z = 4.0 face to flat bottoms at z = 3.375.

No other features; all edges of the base are sharp.

### P02 Carriage (one solid, 63 faces in the original)

**F1. Body**, extrude z = 1.5 to 4.0. Cross-section in (x, y), closed outline, start at (-0.62308, 0.41044):
1. line to (0.62308, 0.41044) (top face, 1.24616 wide)
2. line to (0.86383, -0.00656) (dovetail flank, 60 degrees to the horizontal, widening downward)
3. line to (0.56452, -0.00656) (underside)
4. line to (0.43750, 0.21344) (channel wall, 60 degrees to the horizontal)
5. line to (0.16142, 0.21344) (channel ceiling)
6. arc R0.312 c=(0, -0.05356) through (0, 0.25844) to (-0.16142, 0.21344) (channel crown, 62.4 degree arc)
7. line to (-0.43750, 0.21344)
8. line to (-0.56452, -0.00656)
9. line to (-0.86383, -0.00656)
10. line to start.

The carriage flank planes sit 0.00664 (normal distance) inside the base flank planes; only the strips (F2) touch the base.

**F2. Four wear strips**, join to the body. Same cross-section for all four, mirrored for the -X side; extruded
z = 1.6 to 2.1 and z = 3.4 to 3.9 on each side (each strip 0.5 long, 0.1 in from the carriage end). +X strip profile in
(x, y), closed:
(0.56542, -0.00656), (0.56542, -0.01956), (0.86210, -0.01956), arc R0.01 c=(0.86210, -0.00956) to (0.87076, -0.00456)
(120 degree convex round, tangent to both neighbours), line to (0.66291, 0.35544), line to (0.65685, 0.35194) (square
end, on the carriage flank), line to (0.86383, -0.00656) (along the carriage flank, inside the body), line to start.

So each strip is L-shaped, 0.013 thick under the carriage (bottom y = -0.01956, resting on the base way floor)
and 0.007 thick on the flank (strip flank plane 0.86603 |x| + 0.5 y = 0.75182), ending at y = 0.35544 (base top level).
The -X strips are the mirror images about x = 0.

**F3. Nut bore**, dia 0.995, axis parallel to Y through (x, z) = (0, 2.75), from the top face down through into the
channel (cut through all Y).

**F4. Four top holes** (plain, 0.164 major diameter of the threaded holes), dia 0.164, axes parallel to Y at x = 0 and
z = 1.718, 2.156, 3.344, 3.78, from the top face y = 0.41044 down until they break into the channel crown (cut through
all Y). Spacings 0.438, 1.188, 0.436; outer pair 2.062 apart; first hole 0.218 from the z = 1.5 end, last 0.22 from the
z = 4.0 end.

**F5. Source artefact (optional, +X side only).** For z = 1.5 to 2.3125 and z = 3.1875 to 4.0, a sliver is removed from
the underside next to the channel: the region between the plane y = -0.00656 and the plane through the lines
(x, y) = (0.59562, -0.00656) and (0.56437, -0.00631) (both parallel to Z). It is at most 0.00025 in (0.0064 mm) thick.
Reproducing it or not changes nothing measurable; it is stated only for completeness.

All other edges of the carriage are sharp.

### P03 Drive nut

Solid cylinder dia 0.995 (R0.4975), axis parallel to Y through (x, z) = (0, 2.75), from y = -0.11156 to y = 0.41044
(height 0.522). Its top is flush with the carriage top; it fills the carriage nut bore exactly and projects 0.10500
below the carriage underside into the base groove (bottom 0.023 above the groove floor). No bore, no thread, sharp edges.

### P04 Bearing end block

Block x = -1.25 to 1.25, y = -0.38456 to 0.40544, z = 4.0 to 4.625 (its underside is 0.01 above the base underside,
its top 0.05 above the base top). Features:
- Two clearance holes dia 0.201, through (Z), axes at (x, y) = (+/-1.031, -0.01956).
- Stepped bore on the screw axis (x = 0, y = 0.04244), through. Revolve profile about the screw axis in (z, r):
  dia 0.28125 from z = 4.0 to 4.155; dia 0.339 from z = 4.155 to 4.375; dia 0.375 from z = 4.375 to 4.625 (opens on
  the handwheel side). Flat steps.
All edges sharp.

### P05 End plate

Plate x = -1.25 to 1.25, y = -0.38456 to 0.35544, z = -0.062 to 0 (0.062 thick). Two through holes dia 0.185, axes
parallel to Z at (x, y) = (+/-1.031, -0.01956). No centre hole. All edges sharp.

### P06 Lead screw

Axis = the screw axis (x = 0, y = 0.04244, parallel to Z).

**F1. Turned blank**, revolve, profile in (z, r), closed:
(0.5, 0), (0.5, 0.08711), line to (0.56563, 0.125) (end chamfer cone, 30 degrees half angle measured from the axis),
(4.0, 0.125), (4.0, 0.109), (5.0, 0.109), (5.0, 0), close along the axis.
Threaded section z = 0.5 to 4.0 at major dia 0.25; plain shaft end dia 0.218 from z = 4.0 to 5.0; flat ends, no chamfer at
z = 5.0.

**F2. Helical thread groove (modelled), right-handed, single start, pitch 0.05**, cut in the threaded section only.
- Groove profile in a half-plane through the axis, (dz, r) relative to the root centre: (-0.003125, 0.09252),
  (0.003125, 0.09252), (0.021875, 0.125), (-0.021875, 0.125), continued outward along the same flank lines past
  r = 0.125. Root dia 0.18504, depth 0.03248, root land 0.00625, crest land 0.00625, flanks 30 degrees from the radial
  direction (60 degree included).
- Phase and hand: measure the angle theta about the screw axis from the +X direction toward the +Y direction. The root
  centre lies at **z = 0.515625 + 0.05 (k + theta/360)** for integer k. At theta = 0 (the +X side) root centres are at
  z = 0.515625, 0.565625, ... ; z increases with theta (right-hand).
- Extent: the groove starts beyond the z = 0.5 end (it runs out through the end chamfer and end face). It is clipped at
  the plane z = 4.0 (it does not enter the plain shaft end) and the helical sweep **stops in the half-plane theta = 270
  degrees (the -Y side of the axis) on the turn whose root centre there is at z = 4.003125**. Beyond that angle the last
  partial groove (which would reach down to z = 3.98125) is not cut, leaving a flat radial end face in the plane x = 0
  on the -Y side between z = 3.98125 and 4.0.

### P07 Handwheel

Revolve about the screw axis, profile in (z, r), closed:
(4.687, 0), (4.687, 0.335), (5.062, 0.335), (5.062, 0.855), (5.082, 0.875), (5.417, 0.875), (5.437, 0.855),
(5.437, 0), close.
Hub dia 0.67 x 0.375 long (its face is 0.062 from the end block), rim dia 1.75 between z = 5.062 and 5.437 with
0.02 x 45 degree chamfers on both rim edges. Solid, no bore, no knurl.

### P08 Crank handle

Revolve about the axis parallel to Z through (x, y) = (0, -0.58856) (0.631 below the screw axis, on the -Y side).
Profile in (z, r), closed:
(5.437, 0), (5.437, 0.125), (5.59303, 0.125),
concave arc R1.25 c=(5.87399, 1.34309) to (6.15495, 0.125) (waist, smallest dia 0.18604 at z = 5.87399),
(6.43699, 0.125),
convex arc R0.12449 c=(6.43771, 0.00051) to (6.5622, 0) (rounded end, practically a hemisphere R0.125; top at
z = 6.5622),
close along the axis.
The flat base face z = 5.437 sits on the handwheel outer face.

### Hardware

**H1 Button-head screw**, local frame: origin O at the centre of the under-head face, W along the screw axis pointing
from the shank into the head, U and V any right-handed pair (the part is axisymmetric). Revolve profile in (r, w),
closed:
(0, -0.6871), (0.082, -0.6871), (0.082, 0), (0.187, 0), (0.187, 0.02), convex arc R0.15 c=(0.05434, -0.05) to
(0.05434, 0.1), (0, 0.1), close.
Shank dia 0.164 x 0.6871 long with a flat end, head dia 0.374 x 0.1 high, domed (toroidal) top with a flat of dia
0.10868. No thread, no drive recess.

## 5. Assembly

P01 to P08 are defined directly in global coordinates (no transform). The pose below is the pose as supplied, and it is
to be reproduced exactly.

Hardware instance pose: local origin O and local axes U, V, W expressed in global coordinates. R = [U V W] maps local to
global; a local point p maps to O + R p. All triads are right-handed (U x V = W).

| Instance | Part | Origin O (x, y, z) | U | V | W |
|---|---|---|---|---|---|
| H1-a | H1 (end block, +X) | (1.031, -0.01956, 4.625) | (1,0,0) | (0,1,0) | (0,0,1) |
| H1-b | H1 (end block, -X) | (-1.031, -0.01956, 4.625) | (1,0,0) | (0,1,0) | (0,0,1) |
| H1-c | H1 (end plate, +X) | (1.031, -0.01956, -0.062) | (1,0,0) | (0,-1,0) | (0,0,-1) |
| H1-d | H1 (end plate, -X) | (-1.031, -0.01956, -0.062) | (1,0,0) | (0,-1,0) | (0,0,-1) |

H1-a/b pass through the end block into the base holes (shank tip z = 3.9379, only 0.0621 into the 0.625 deep hole).
H1-c/d pass through the end plate; their shank tips reach z = 0.6251, 0.0001 past the hole bottoms (overlap
0.0346 mm3 each, negligible, reproduce as is). The shanks fill the base holes exactly (same diameter).

**Kinematics and relations:**
- **Carriage travel:** the carriage, its strips and the drive nut translate together along Z. Supplied at the **+Z
  limit**: carriage z = 1.5 to 4.0, its +Z end face touching the end block face z = 4.0. The other limit is carriage
  z = 0 to 2.5 against the end plate face z = 0. Travel 1.5 = base length 4.0 minus carriage length 2.5.
- **Drive:** the handwheel, the handle and the lead screw rotate together about the screw axis. Lead 0.05 per turn
  (single start), 30 turns for the full travel. In the supplied pose the handle is straight below the axis (-Y side).
- **Strips on the base:** the strip bottoms lie on the way floor y = -0.01956 (contact). The strip flank planes lie 0.00036
  (normal) beyond the base flank planes, an intended zero-clearance fit; this gives a total overlap of 4.97 mm3
  between P01 and P02 (all four strips). Reproduce as is.
- **Volumetric overlaps as supplied (reproduce as is):**
  - P03 drive nut with P06 lead screw: the screw runs through the solid nut, 608.7 mm3 (0.0371 in3).
  - P06 lead screw with P07 handwheel: plain shaft end z = 4.687 to 5.0 inside the solid hub, 191.4 mm3 (0.0117 in3).
- The nut fills the carriage bore exactly (shared cylindrical surface, no overlap). All other neighbours touch or have
  clearance: carriage underside 0.013 above the way floor, nut 0.023 above the groove floor, plain shaft end (dia 0.218)
  0.0316 radially inside the smallest end block bore (dia 0.28125), handwheel hub 0.062 from the end block.

## 6. Acceptance targets

Measure each body at the supplied pose. Suggested tolerance for a one-to-one rebuild: volume within 0.5 percent per
body, centre of mass within 0.02 in, bounding box within 0.005 in; for the screws accept volume within 2 percent.

Coordinates in inches. The "faces" column is information only (face count in the original; a correct rebuild may
differ, e.g. where a CAD system splits or merges faces).

| ID | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Base | 4.5937 | 75276.8 | 35.896 | 23158.6 | 0.0000 | -0.1019 | 2.0000 | -1.2500 | 1.2500 | -0.3946 | 0.3554 | 0.0000 | 4.0000 | 34 |
| P02 Carriage | 0.8300 | 13600.9 | 10.704 | 6906.1 | 0.0000 | 0.2243 | 2.7500 | -0.8721 | 0.8721 | -0.0196 | 0.4104 | 1.5000 | 4.0000 | 63 |
| P03 Drive nut | 0.4059 | 6651.3 | 3.187 | 2056.0 | 0.0000 | 0.1494 | 2.7500 | -0.4975 | 0.4975 | -0.1116 | 0.4104 | 2.2525 | 3.2475 | 4 |
| P04 End block | 1.1376 | 18642.1 | 9.266 | 5978.3 | 0.0000 | 0.0099 | 4.3108 | -1.2500 | 1.2500 | -0.3846 | 0.4054 | 4.0000 | 4.6250 | 18 |
| P05 End plate | 0.1114 | 1825.0 | 4.066 | 2623.4 | 0.0000 | -0.0144 | -0.0310 | -1.2500 | 1.2500 | -0.3846 | 0.3554 | -0.0620 | 0.0000 | 10 |
| P06 Lead screw | 0.1685 | 2761.5 | 4.926 | 3178.3 | 0.0000 | 0.0424 | 2.7523 | -0.1250 | 0.1250 | -0.0826 | 0.1674 | 0.5000 | 5.0000 | 293 |
| P07 Handwheel | 1.0320 | 16911.6 | 7.532 | 4859.2 | 0.0000 | 0.0424 | 5.2015 | -0.8750 | 0.8750 | -0.8326 | 0.9174 | 4.6870 | 5.4370 | 11 |
| P08 Crank handle | 0.0447 | 733.0 | 0.861 | 555.5 | 0.0000 | -0.5886 | 5.9992 | -0.1250 | 0.1250 | -0.7136 | -0.4636 | 5.4370 | 6.5622 | 10 |
| H1-a Screw | 0.0225 | 369.0 | 0.628 | 404.9 | 1.0310 | -0.0196 | 4.4179 | 0.8440 | 1.2180 | -0.2066 | 0.1674 | 3.9379 | 4.7250 | 9 |
| H1-b Screw | 0.0225 | 369.0 | 0.628 | 404.9 | -1.0310 | -0.0196 | 4.4179 | -1.2180 | -0.8440 | -0.2066 | 0.1674 | 3.9379 | 4.7250 | 9 |
| H1-c Screw | 0.0225 | 369.0 | 0.628 | 404.9 | 1.0310 | -0.0196 | 0.1451 | 0.8440 | 1.2180 | -0.2066 | 0.1674 | -0.1620 | 0.6251 | 9 |
| H1-d Screw | 0.0225 | 369.0 | 0.628 | 404.9 | -1.0310 | -0.0196 | 0.1451 | -1.2180 | -0.8440 | -0.2066 | 0.1674 | -0.1620 | 0.6251 | 9 |

**Whole assembly:**
- Instance count: 12 bodies (8 custom + 4 hardware).
- Total volume: 8.4138 in3 (137 878 mm3). Total surface area, sum over bodies: 78.949 in2 (50 935 mm2).
- Centre of mass, uniform density: (0.0000, -0.0224, 2.8277) in.
- Bounding box, in: X [-1.25, 1.25], Y [-0.83256, 0.91744], Z [-0.162, 6.5622]. In mm: X [-31.750, 31.750],
  Y [-21.147, 23.303], Z [-4.115, 166.680].

**Key functional checks:**
- Base 2.5 wide x 0.75 high x 4.0 long; dovetail flanks 60 degrees; way floor 0.375 below the base top.
- Carriage 2.5 long, top face 1.24616 wide, 0.417 high (top to underside), 1.7442 wide over the strips.
- Height from base underside to carriage top 0.805.
- Mounting holes dia 0.198 with 82 degree countersink to dia 0.385, 3.0 apart along Z, 0.26 of material under the
  countersink.
- Carriage holes 4 x dia 0.164 on the centre line, outer pair 2.062 apart, inner pair 1.188 apart.
- Lead screw dia 0.25, pitch 0.05 RH, threaded z = 0.5 to 4.0, plain shaft end dia 0.218 to z = 5.0.
- Handwheel dia 1.75; its lowest point is 0.438 below the base underside. Overall length, end-plate screw heads to
  handle end: 6.7242.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs all dimensions. The supplied dimensioned drawing and product data were
compared with it.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall length | 6.72 | 6.7242 (z -0.162 to 6.5622) | Same to rounding. Use the 3D. |
| Base length, width | 4, 2.5 | 4.0, 2.5 | Agree |
| Carriage length | 2.5 | 2.5 | Agree |
| Carriage width | 1.25 | top face 1.24616; 1.7442 over the strips | Use the 3D. |
| Height | 0.81 | 0.805 (base underside to carriage top) | Use the 3D. |
| Travel length | 1.5 | base 4.0 minus carriage 2.5 | Agree (kinematic, not a feature) |
| Carriage hole spacings | 2.062, 1.188, 0.219, 0.656 | 2.062, 1.188, 0.218, 0.656 | Use the 3D. |
| Carriage thread | 8-32, 0.2 deep | plain dia 0.164 holes running through into the channel (0.163 deep at the hole wall) | Follow the 3D: plain through holes. |
| Base mounting holes | for 10-32 fastener, 3 apart, 0.26 | dia 0.198 with 82 degree countersink, 3.0 apart along Z (offset +/-0.343 in X), 0.26 under the countersink | Follow the 3D. |
| Handwheel | dia 1.75, overhang 0.44 | dia 1.75, 0.438 below the base underside | Same to rounding. |
| Travel per turn | 0.05 | thread pitch 0.05, single start | Agree |
| Nut, handwheel bore | photos show a socket screw in the nut | nut and hub solid, screw overlaps both | Follow the 3D. |
| Screw heads | photos show cross-recess heads | plain domed heads | Follow the 3D. |
| Handwheel rim | photos show a knurl | plain cylinder | Follow the 3D. |

**Undetermined, not recoverable from the sources:**
- Thread data of the carriage holes and base end holes beyond the 0.164 major diameter (no thread modelled).
- The thread standard of the lead screw beyond the modelled profile (pitch 0.05, major 0.25, root 0.18504).
- Any bearing bush, thrust collar or retention of the lead screw in the end block (none modelled).
- How the nut is fixed in the carriage (the photos show a screw; none modelled) and how it engages the screw.
- Materials other than the aluminium base and carriage and the stainless lead screw; strip material is from the product
  data only (no separate body).
- The angular position of the handwheel/handle in use (any angle is valid kinematically; reproduce the supplied one).
