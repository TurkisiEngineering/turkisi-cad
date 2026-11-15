# Design specification: pneumatic toggle clamp with forked arm, hold-down type

Pneumatic hold-down toggle clamp, rated 600 lb holding capacity. A double-acting air cylinder, pivoting on trunnions in a
sheet-metal base bracket, drives a toggle linkage that swings a forked clamp arm down onto the work. The arm carries an
adjustable holding screw in its open slot. This document is the only source for the rebuild. Every dimension below was
measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres by multiplying every value by 25.4; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - +Y is up. **Y = 0 is the mounting face** (underside of the base bracket).
  - **Z = 0 is the front face of the base bracket.** The clamp arm and holding screw point toward +Z; the air cylinder
    points toward -Z (rear).
  - X is across the clamp. The whole assembly is symmetric about the plane x = 0 except the few features stated below.
  - Holding screw axis: the line x = 0, z = 3.21, parallel to Y.
- **Profile coordinate conventions:**
  - "(z, y)" = profile in a plane normal to X; "(x, z)" = profile in a plane normal to Y; "(x, y)" = profile in a plane
    normal to Z.
  - "(w, r)" = revolve profile: w along the stated axis, r = radius from it.
  - Arcs are given as "arc ... via (a, b) to (p, q)": a circular arc from the current point through the via point to the end
    point, or as "arc R c=(a, b) to (p, q)" (centre given, minor arc).
- **Cylinder frame C** (used for P06 and P07): origin **OC = (0, 2.44, -3.81)** (the trunnion axis centre), axes
  - U = (1, 0, 0)
  - V = (0, 0.960846, -0.277081)
  - W = (0, 0.277081, 0.960846) (the cylinder and piston-rod axis, rising toward +Z at 16.0861 degrees above the -Z..+Z
    horizontal). U x V = W (right-handed). A local point (u, v, w) is at global OC + u U + v V + w W.
  - The cylinder axis passes exactly through the trunnion centre OC and through the top linkage pin centre (0, 3.432, -0.37),
    which lies at w = 3.58018, v = 0.

## 2. Product description and operation

A U-shaped base bracket (P01) is screwed to the machine table through 4 holes. Inside it, at the front, a riser made of
two angle brackets (P02, with a riveted pin) carries the clamp arm pivot. The forked clamp arm (P03) pivots on that pin
(y = 2.182, z = -1.62). The arm is pulled by a short channel-section connecting link (P04), whose upper end and the clevis
of the piston rod (P06) share the upper pin of a pair of side links (P05). The side links pivot at their lower pin in the
riser. The air cylinder (P07) pivots at the rear of the base bracket on two trunnion pins; air in one port extends the rod
(clamps), air in the other retracts it (opens).

The holding screw (H1, 3/8-16, hex head down) passes through the arm slot and is clamped to the arm by two saddle washers
(H2) and two hex nuts (H3). A plug (H4) closes the front port of the cylinder.

**Simplifications in the source geometry that must be reproduced:**
- The pin of the arm-to-link pivot (y = 2.182, z = -0.37) is **not modelled**; there are only the holes.
- The piston, seals and cylinder bore are not modelled. The cylinder (P07) is one solid with a 0.62992 dia blind bore for
  the rod, three socket screw heads, two trunnion pins (with hex sockets) and the ports, all fused.
- Pins are fused into their parts: the riser pin into P02, both side-link pins into P05.
- The holding screw thread is modelled (helical). The two rear cylinder ports carry a modelled helical tapered thread. The
  front cylinder port is a plain taper. The port plug has ring ridges (not helical). The nuts have a plain bore at the
  thread minor diameter (no thread).
- No rubber tip on the holding screw; the screw's lower end is its hex head.

## 3. Part list

7 distinct custom parts and 4 distinct hardware items, 11 distinct, **13 bodies in total**.

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Base bracket, bent sheet U-channel with trunnion bosses | custom, steel sheet 0.122 |
| P02 | 1 | Arm riser: two angle brackets joined by a riveted pin | custom, steel sheet 0.122 |
| P03 | 1 | Clamp arm, open (forked) | custom, steel |
| P04 | 1 | Connecting link, channel section | custom, steel sheet 0.122 |
| P05 | 1 | Side links (two jogged straps) with two pins | custom, steel |
| P06 | 1 | Piston rod with flattened clevis end | custom, steel |
| P07 | 1 | Air cylinder (head block, tube, rear cap, trunnions, screw heads, ports) | custom, aluminium / steel |
| H1 | 1 | Holding screw, 3/8-16 x 2.75 thread, hex head | hardware |
| H2 | 2 | Saddle washer (H2-a above the arm, H2-b below) | hardware |
| H3 | 2 | Hex nut 0.56 across flats (H3-a above, H3-b below) | hardware |
| H4 | 1 | Tapered port plug with hex socket | hardware |

Materials are inferred from the product photos (zinc-plated steel brackets and links, bright aluminium cylinder). The 3D
carries no colour.

## 4. Part geometry

All coordinates are global unless a local frame is named. Features are listed in an order that constructs each part.

### P01 Base bracket (58 faces in the original)

**F1. U-channel.** Profile in (x, y), extruded z = -4.22 to 0 (start at (-1.312, 0), in order, closing on the start):
1. line to (1.312, 0)
2. arc R0.12 c=(1.312, 0.12) to (1.432, 0.12) (outer bend)
3. line to (1.432, 3.2) (any height above 2.85)
4. line to (1.31, 3.2)
5. line to (1.31, 0.182)
6. arc R0.06 c=(1.25, 0.182) to (1.25, 0.122) (inner bend)
7. line to (-1.25, 0.122)
8. arc R0.06 c=(-1.25, 0.182) to (-1.31, 0.182)
9. line to (-1.31, 3.2), line to (-1.432, 3.2), line to (-1.432, 0.12)
10. arc R0.12 c=(-1.312, 0.12) to (-1.312, 0)

Sheet thickness 0.122. The outer and inner bend arcs are deliberately not concentric (as in the source).

**F2. Side outline.** Intersect F1 with this profile in (z, y), extruded through all X:
(0, 0), (0, 0.122), arc R0.12 c=(-0.12, 0.122) to (-0.0495, 0.2191), line to (-3.5693, 2.7719) (tangent),
arc R0.41 c=(-3.81, 2.44) via (-3.81, 2.85) to (-4.22, 2.44), line to (-4.22, 0), close.
The sloped top edge is 35.95 degrees from the base. The base plate itself (y below 0.122) is a full rectangle
x = -1.312..1.312, z = -4.22..0.

**F3. Trunnion bosses**, on the inner face of each side wall, axis parallel to X through (y, z) = (2.44, -3.81), both sides
mirror-symmetric (shown for +X):
- ring outer R0.31 from x = 1.162 to 1.297,
- neck R0.2235 from x = 1.297 to 1.31 (joins the ring to the wall),
- hole R0.157 through ring, neck and wall (x = 1.162 to 1.432).

**F4. Mounting holes**, 4x through the base plate (y = 0 to 0.122), at z = -0.38 and z = -1.63, on both sides of x = 0.
Each is a short obround: two half-circles R0.17 centred at x = 0.890 and x = 0.893 (for +X; -0.890 and -0.893 for -X),
joined by straight sides (length 0.003 along X). Hole width 0.34.

All other edges sharp.

### P02 Arm riser (61 faces)

Two bent angles (one per side) plus a pin. Sheet 0.122.

**F1. Angle sections**, profiles in (x, y), each extruded z = -1.96 to 0.14 (then trimmed by F2 and F3):
- Left angle, start (-0.1575, 2.6): line to (-0.2795, 2.6), line to (-0.2795, 0.364), arc R0.12 c=(-0.3995, 0.364) to
  (-0.3995, 0.244), line to (-1.2675, 0.244), line to (-1.2675, 0.122), line to (-0.3975, 0.122), arc R0.24
  c=(-0.3975, 0.362) to (-0.1575, 0.362), close.
- Right angle, start (0.1575, 2.6): line to (0.1575, 0.364), arc R0.242 c=(0.3995, 0.364) to (0.3995, 0.122), line to
  (1.2675, 0.122), line to (1.2675, 0.244), line to (0.3995, 0.244), arc R0.12 c=(0.3995, 0.364) to (0.2795, 0.364), line to
  (0.2795, 2.6), close.
  (Left and right inner bend radii differ, 0.24 vs 0.242, as in the source.) The flanges sit on the base plate of P01
  (y = 0.122 to 0.244); the uprights are x = +/-0.1575 to +/-0.2795.

**F2. Upright outline**, intersect with this profile in (z, y), through all X:
(-1.96, 0), (-1.96, 2.182), arc R0.34 c=(-1.62, 2.182) via (-1.7563, 2.4935) to (-1.3893, 2.4317), line to
(-0.0918, 1.2332) (tangent), arc R0.41 c=(-0.37, 0.932) via (0.0391, 0.9595) to (-0.054, 0.6708), line to (-0.054, 0), close.

**F3. Flange plan outline**, intersect with this profile in (x, z), through all Y: rectangle x = -1.2675..1.2675,
z = -1.96..-0.054 with its four corners rounded by R0.25 arcs centred at (+/-1.018, -0.304) and (+/-1.018, -1.71) (each arc
runs from the side x = +/-1.2675 at z = -0.2879 / -1.7261 to the end edge at x = +/-1.018); united with the strip
x = -0.5..0.5, z = -0.054..0.2 (so the uprights' front arc can bulge to z = 0.04).

**F4. Holes:**
- 4x flange holes dia 0.34 (R0.17) through Y at (x, z) = (+/-0.893, -0.38) and (+/-0.893, -1.63), coaxial with P01's holes.
- Through both uprights, axis parallel to X: R0.125 at (y, z) = (0.932, -0.37) and R0.0945 at (1.619, -1.477).
- **+X upright only:** R0.19 hole, axis parallel to X, at (y, z) = (0.8837, -1.24).

**F5. Punched disc (+X upright only).** A disc R0.19 whose axis has direction a = (0.8578, -0.4084, -0.3122) and passes
through (0.3699, 0.8533, -1.2515); the disc lies between the planes a . p = 0.2482 and a . p = 0.3596 (p = global point).
It sits in the F4 R0.19 hole, tilted 30.93 degrees to the upright, and is joined to P02 (boolean union).

**F6. Riveted pin**, axis parallel to X through (y, z) = (2.182, -1.62): cylinder R0.1265 from x = -0.2795 to 0.2795, plus a
head on each end: revolve profile (w, r) with w measured outward from the upright face x = +/-0.2795:
(0, 0), (0, 0.1659), quarter arc R0.03937 c=(0, 0.1265) to (0.03937, 0.1265), (0.03937, 0), close. Join all.

### P03 Clamp arm (44 faces)

**F1. Forked arm, plan profile in (x, z), extruded y = 1.7885 to 2.5755** (0.787 tall). Right half, start (0.157, -0.3):
1. line to (0.157, 0.396)
2. arc R0.0785 c=(0.2355, 0.396) via (0.1597, 0.4163) to (0.1675, 0.4352)
3. line to (0.3049, 0.6741)
4. arc R0.402 c=(-0.0435, 0.8746) via (0.3449, 0.7708) to (0.3585, 0.8746)
5. line to (0.3585, 3.213)
6. arc R0.3585 c=(0, 3.213) via (0.2742, 3.4439) to (0.0611, 3.5662) (arm tip)
7. line to (0.02, 3.413) (tip V-gap, 15 degree flanks)
8. arc R0.201 c=(0, 3.213) via (0.1490, 3.3479) to (0.201, 3.213) (slot tip end)
9. line to (0.201, 0.862)
10. arc R0.201 c=(0, 0.862) via (0.1942, 0.8101) to (0.1742, 0.7618)
11. line to (0.0209, 0.4953)
12. arc R0.157 c=(0.157, 0.417) via (0.0053, 0.4575) to (0, 0.417)

then the mirror image (x -> -x) of steps 12..1 back to (-0.157, -0.3), and close along z = -0.3.
Result: two tines 0.1575 thick (x = +/-0.201 to +/-0.3585) around an open slot 0.402 wide; the slot end-arc centres are
2.351 apart (z = 0.862 and 3.213). At the tip the tines nearly meet, leaving a 0.04 wide V-gap.

**F2. Pivot head, profile in (z, y), extruded x = -0.157 to 0.157** (union with F1). Start (0, 1.7885):
line to (-0.0032, 1.7885), arc R0.185 c=(-0.0032, 1.6035) via (-0.0548, 1.7812) to (-0.1022, 1.7597),
arc R0.5 c=(-0.37, 2.182) via (-0.2611, 1.694) to (-0.4328, 1.686), line to (-1.6631, 1.8417),
arc R0.343 c=(-1.62, 2.182) via (-1.8773, 1.9552) to (-1.963, 2.182), arc same circle via (-1.8773, 2.4088) to
(-1.6631, 2.5223), line to (-0.4328, 2.678), arc R0.5 c=(-0.37, 2.182) via (-0.2611, 2.67) to (-0.1022, 2.6043),
arc R0.185 c=(-0.0032, 2.7605) via (-0.0548, 2.5828) to (-0.0032, 2.5755), line to (0, 2.5755), close.

**F3. Holes, axes parallel to X:** R0.189 through at (y, z) = (2.182, -1.62) and (2.182, -0.37). At (2.182, 0.126): from the
+X face a blind hole R0.0885 from x = 0.157 to a flat bottom at x = -0.0628, and from the -X face a blind hole R0.0875 from
x = -0.157 to a flat bottom at x = -0.1256.

### P04 Connecting link (40 faces)

**F1. Channel, plan profile in (x, z), extruded y = 1.8 to 3.9** (trimmed later). Start (0.2865, -0.68): line to
(0.2865, 0.132), arc R0.12 c=(0.1665, 0.132) to (0.1665, 0.252), line to (-0.1665, 0.252), arc R0.12 c=(-0.1665, 0.132) to
(-0.2865, 0.132), line to (-0.2865, -0.68), line to (-0.1645, -0.68), line to (-0.1645, 0.1), arc R0.03 c=(-0.1345, 0.1) to
(-0.1345, 0.13), line to (0.1345, 0.13), arc R0.03 c=(0.1345, 0.1) to (0.1645, 0.1), line to (0.1645, -0.68), close.
(Side plates x = +/-0.1645..+/-0.2865, web z = 0.13..0.252, all 0.122 thick.)

**F2. Side outline**, intersect F1 with this profile in (z, y), through all X. Start (-0.06, 2.182): line to (-0.06, 2.515),
arc R0.12 c=(0.06, 2.515) to (0.06, 2.635), line to (0.4, 2.635), line to (0.4, 3.505), line to (0.0591, 3.505),
arc R0.31 c=(-0.25, 3.482) via (-0.0391, 3.7092) to (-0.25, 3.792), line to (-0.37, 3.792), arc R0.31 c=(-0.37, 3.482) via
(-0.5892, 3.7012) to (-0.68, 3.482), line to (-0.68, 2.182), arc R0.31 c=(-0.37, 2.182) via (-0.37, 1.872) to (-0.06, 2.182).

**F3. Web bottom.** Below the web the bottom edge drops to y = 2.605: add the part of F1 inside this (x, y) region, extruded
through the web (z = 0.06..0.4): (-0.155, 2.635), concave arc R0.03 c=(-0.155, 2.605) to (-0.125, 2.605), line to
(0.125, 2.605), concave arc R0.03 c=(0.155, 2.605) to (0.155, 2.635), line to (0.155, 2.7), line to (-0.155, 2.7), close.

**F4. Web top cut:** remove a cylinder R0.31, axis parallel to Z through (x, y) = (0, 3.475), for z >= 0.0591.

**F5. Holes through both plates, axes parallel to X:** R0.1265 at (y, z) = (2.182, -0.37), R0.188 at (3.432, -0.37).

### P05 Side links with pins (64 faces)

**F1. Two jogged straps**, profiles in (x, y) extruded z = -0.68 to -0.06. Right strap, start (0.286, 0.5):
line to (0.286, 1.7073), arc R0.061 c=(0.347, 1.7073) to (0.3039, 1.7504), line to (0.3901, 1.8367), arc R0.061
c=(0.347, 1.8798) to (0.408, 1.8798), line to (0.408, 2.7342), arc R0.061 c=(0.347, 2.7342) to (0.3901, 2.7773), line to
(0.3039, 2.8636), arc R0.061 c=(0.347, 2.9067) to (0.286, 2.9067), line to (0.286, 3.9), line to (0.408, 3.9), line to
(0.408, 2.9573), arc R0.061 c=(0.469, 2.9573) to (0.4259, 2.9141), line to (0.5121, 2.8279), arc R0.061 c=(0.469, 2.7847)
to (0.53, 2.7847), line to (0.53, 1.8293), arc R0.061 c=(0.469, 1.8293) to (0.5121, 1.7861), line to (0.4259, 1.6999),
arc R0.061 c=(0.469, 1.6567) to (0.408, 1.6567), line to (0.408, 0.5), close. Left strap = mirror in x.
(Straps 0.122 thick: x = 0.286..0.408 at the ends, jogged outward to 0.408..0.53 between y = 1.88 and 2.73, 45 degree jogs.)

**F2. Stadium outline**, intersect with this profile in (z, y), through all X: z = -0.68..-0.06, y from 0.932 to 3.432 with
semicircular ends R0.31 centred at (z, y) = (-0.37, 0.932) and (-0.37, 3.432).

**F3. Upper pin**, axis parallel to X through (y, z) = (3.432, -0.37): cylinder R0.188 from x = -0.408 to 0.408, plus heads on
both ends, revolve profile (w, r), w outward from x = +/-0.408: (0, 0), (0, 0.2274), quarter arc R0.03937 c=(0, 0.188) to
(0.03937, 0.188), (0.03937, 0), close.

**F4. Lower pin**, axis parallel to X through (0.932, -0.37): cylinder R0.125 from x = -0.408 to 0.408, plus heads, profile
(w, r) from x = +/-0.408: (0, 0), (0, 0.1644), (0.0236, 0.1644), 45 degree chamfer to (0.0394, 0.1486), (0.0394, 0), close.
Join everything.

### P06 Piston rod (20 faces)

Local frame: origin **O6 = (0, 3.432, -0.37)** (= cylinder frame w = 3.58018), axes U, V, W of the cylinder frame C.
1. Revolve about W, profile (w, r): (-5.1732, 0), (-5.1732, 0.1606), 45 degree chamfer to (-5.1370, 0.19685),
   (-4.3661, 0.19685), (-4.3661, 0.31496), (-0.6839, 0.31496), cone to (-0.6496, 0.29528), (0.0197, 0.29528), then a
   spherical end R0.29528 centred at (w, r) = (0.0197, 0) to (0.3150, 0). Rod dia 0.62992 (16 mm), rear spigot dia 0.3937.
2. Clevis flats: remove all material with |u| > 0.124 for w > -0.4749, with a 45 degree run-out from (w, |u|) = (-0.4749,
   0.124) to (-0.6462, 0.29528). Tongue thickness 0.248, flats normal to U (global X).
3. Cross hole R0.188 along U through O6.

### P07 Air cylinder (167 faces)

All coordinates in the cylinder frame C (u, v, w).

**F1. Tube.** Profile in (u, v), extruded w = -4.2126 to -0.3937: circle R1.04331 (dia 2.0866) minus four slots that run the
full length:
- Two T-slots at polar angles 167 and 193 degrees (measured from +u toward +v). In a slot's own coordinates (s along the
  slot centre line from the axis outward, t across): mouth |t| <= 0.1024 from s = 0.9855 out through the surface; chamber
  |t| <= 0.128 from s = 0.8584 to 0.9855.
- Two keyhole slots at polar angles +10 and -10 degrees: |t| <= 0.06 from s = 0.9451 out through the surface, plus a
  circle R0.0827 centred at s = 0.9451.

**F2. Front head block.** Rounded rectangle u = -1.1614..1.1614, v = -1.04331..1.04331, corner radius R0.2362 (centres
(+/-0.9252, +/-0.8071)), extruded w = -0.3937 to 0.5512. Join to F1.

**F3. Rear cap flats**, for w = -4.2126 to -3.5827 only: two flat cuts at distance 0.9843 from the axis, one with outward
normal +v and one with outward normal (u, v) = (-0.7071, 0.7071).

**F4. Bottom flat.** Remove everything below the global plane through (0, 0.53511, -7.64494) with unit normal
(0, 0.999970, -0.007746) (material kept on the +Y side). It cuts the underside of the rear of the tube and cap.

**F5. Rod bore:** R0.31496 (dia 0.62992) along the axis from the front face w = 0.5512 to a flat bottom at w = -3.3858.

**F6. Trunnion pins**, axis along u through the origin, each side: cylinder R0.155 from |u| = 1.1614 to 1.5875, 45 degree
chamfer to R0.1411 at the end face |u| = 1.6014. Hex socket in each end: across flats 0.161, corners on the w direction
(flats normal to v), flat bottom at |u| = 1.4414.

**F7. Three socket-head screw heads** on the front face, centres (u, v) = (0, -0.9055), (0.6403, 0.6403), (-0.6403, 0.6403)
(on a circle R0.9055): counterbore R0.1575 from w = 0.5512 down to w = 0.3543; head cylinder R0.1378 from w = 0.3543 to
0.5276 (joined); hex socket across flats 0.1575, flats normal to u and to +/-60 degrees from u (corners on v), from
w = 0.5276 to a flat bottom at w = 0.4528. The lower counterbore breaks through the block underside.

**F8. Front plug port** in the block top, axis along +v at (u, w) = (0, 0.0787). Revolve profile (v, r): 45 degree
countersink from r = 0.2025 at v = 1.04331 to r = 0.1775 at v = 1.0183; plain taper (half angle 1.79 degrees) to r = 0.1684
at v = 0.7283; cylinder r = 0.1684 to v = 0.6575; 120 degree drill point to v = 0.5602.

**F9. Two rear threaded ports** (1/8 NPT), at w = -3.9173, one on each F3 flat: axis along +v (top) and along (u, v) =
(-0.7071, 0.7071) (45 degree flat). Along the port axis (distance h from the cylinder axis):
- 45 degree countersink from r = 0.2207 at h = 0.9843 to the thread;
- internal tapered thread from h = 0.9843 down to h = 0.7204: 60 degree profile, pitch 0.037037 (27 per inch),
  right-hand, flat crest and root each 1/8 pitch wide; root (major) radius 0.2107 and crest (minor) radius 0.1862 at
  h = 0.9843, both decreasing inward at half-angle 1.783 degrees. Phase (top port): a root centre lies on the global +X
  side of the axis at h = 0.0111 + 0.037037 k (approximate, +/-0.002);
- flat shoulder at h = 0.7204, tap drill R0.1308 down to h = 0.5118, 120 degree drill point to h = 0.4363.

### Hardware

Each hardware part is defined in a local frame (origin O, axes U, V, W). Instance poses are in section 5.

**H1 Holding screw** (local W = screw axis, pointing up; O on the head's lower face).
- Hex head, across flats 0.56 (flats normal to U, corners on V), w = 0 to 0.25, no chamfers.
- Shank R0.1875 (dia 0.375) from w = 0.25 to 3.0, 45 degree chamfer at the end (end face R0.1406).
- **Helical thread modelled**, 3/8-16: pitch 0.0625, right-hand, 60 degree profile, flat crest at R0.1875 and flat root at
  R0.1469, each 1/8 pitch (0.0078) wide. The groove starts at the head face (w = 0.25) and runs out through the end chamfer.
  Phase: a root-flat centre lies on the +U side of the axis at w = 0.2618 + 0.0625 k.

**H2 Saddle washer** (O = centre of the face that rests on the arm; V = outward normal of that face; U = global X).
Profile in (u, v), extruded through all w and then intersected with a cylinder R0.5 about the V axis; minus a hole R0.2055
along V. Start (-0.375, 0): line to (0.375, 0), arc R0.0963 c=(0.4713, 0.0013) to (0.4688, -0.095), line to (0.4688, -0.002),
arc R0.1065 c=(0.3628, -0.0128) to (0.375, 0.093), line to (-0.375, 0.093), arc R0.1065 c=(-0.3628, -0.0128) to
(-0.4688, -0.002), line to (-0.4688, -0.095), arc R0.0963 c=(-0.4713, 0.0013) to (-0.375, 0), close.
(A 0.093 plate with two lips bent down 0.095 alongside the arm tines.)

**H3 Hex nut** (O = centre of the lower face, W = axis up). Across flats 0.56 (flats normal to U, corners on V), w = 0 to
0.22. Chamfer on both faces: a cone that meets the face at r = 0.28 and rises at 75 degrees from the axis (cuts the
corners). Plain bore R0.1536 with a 45 degree countersink to R0.1875 at each face.

**H4 Port plug** (O = centre of the top face, W = outward axis). Revolve profile (w, r): (0, 0), (0, 0.2053), (-0.026, 0.2045),
(-0.026, 0.1744), then ring ridges: crests (w, r) = (-0.0445, 0.2039), (-0.0823, 0.2027), (-0.1201, 0.2016),
(-0.1579, 0.2004), (-0.1957, 0.1992), (-0.2335, 0.1980), (-0.2713, 0.1969), each followed by a root (-0.0634, 0.1726),
(-0.1012, 0.1714), (-0.1390, 0.1703), (-0.1768, 0.1691), (-0.2146, 0.1679), (-0.2524, 0.1667), (-0.2901, 0.1656) (straight
lines crest to root to crest), then (-0.2901, 0), close. Hex socket across flats 0.1875 (flats normal to U, corners on V),
from w = 0 to a flat bottom at w = -0.0725.

## 5. Assembly

P01 to P05 are defined directly in global coordinates; P06 and P07 in the cylinder frame C as stated. The supplied pose is
the **clamped** pose (arm horizontal, holding screw vertical); reproduce it exactly.

| Instance | Part | Origin O (x, y, z) | U | V | W |
|---|---|---|---|---|---|
| H1 | H1 | (0, 1.2255, 3.21) | (1, 0, 0) | (0, 0, -1) | (0, 1, 0) |
| H2-a | H2 | (0, 2.5755, 3.21) | (1, 0, 0) | (0, 1, 0) | (0, 0, 1) |
| H2-b | H2 | (0, 1.7885, 3.21) | (1, 0, 0) | (0, -1, 0) | (0, 0, -1) |
| H3-a | H3 | (0, 2.6685, 3.21) | (1, 0, 0) | (0, 0, -1) | (0, 1, 0) |
| H3-b | H3 | (0, 1.4755, 3.21) | (1, 0, 0) | (0, 0, -1) | (0, 1, 0) |
| H4 | H4 | (0, 3.464256, -4.02346) | (1, 0, 0) | (0, -0.277081, -0.960846) | (0, 0.960846, -0.277081) |

Note: for H1, H3-a and H3-b the axis W is global +Y, U = global X and V = (0, 0, -1) (right-handed: U x V = W); the hex
corners therefore point along global Z and the flats face +/-X. H1's head is y = 1.2255..1.4755, thread to the tip at
y = 4.2255; root-flat centres on the +X side at y = 1.4873 + 0.0625 k. A local point p maps to O + [U V W] p; all triads are
right-handed. H4 sits in the P07 front port (F8): O is the cylinder-frame point (0, 1.04331, 0.0787), so the plug top face is flush with the block top.

**Kinematics and relations:**
- Arm P03 pivots about the P02 pin (axis X through y = 2.182, z = -1.62); clearance pin R0.1265 in hole R0.189.
- Link P04 joins the arm (holes at y = 2.182, z = -0.37, no pin modelled) to the upper P05 pin (y = 3.432, z = -0.37),
  shared with the piston-rod clevis hole.
- Side links P05 pivot on their lower pin (y = 0.932, z = -0.37) in the P02 holes R0.125 (zero clearance).
- The cylinder P07 swings about its trunnions (R0.155) in the P01 holes (R0.157). The rod slides along W in the bore.
- Opening: the catalogue states an arm opening angle of 95 degrees; the open pose is not modelled.
- Holding screw: adjustable anywhere along the 2.351 slot; supplied at z = 3.21 (0.003 behind the slot tip-end centre),
  clamped by H3-b / H2-b below and H2-a / H3-a above the arm.

**Interference set as supplied (reproduce as is, overlap volumes):**
- H1 thread with H3-a nut bore: 701.1 mm3; with H3-b: 38.4 mm3 (the nut bores are plain at the minor diameter).
- H4 plug ridges with the P07 front port taper: 67.2 mm3.
- All other contacts are touching or clear (below 8 mm3: P01-P02 0.74 mm3, P04-P05 6.04 mm3).

## 6. Acceptance targets

Measure each body at the supplied pose. Suggested tolerance for a one-to-one rebuild: volume within 0.5 percent per body
(2 percent for hardware), centre of mass within 0.02 in, bounding box within 0.005 in. The "faces" column is for
information only.

| ID | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Base bracket | 3.0572 | 50098.6 | 53.522 | 34530.3 | 0.0000 | 0.6531 | -2.4906 | -1.4320 | 1.4320 | 0.0000 | 2.8500 | -4.2200 | 0.0000 | 58 |
| P02 Arm riser | 1.2612 | 20667.8 | 23.915 | 15429.1 | 0.0007 | 0.8561 | -1.0974 | -1.2675 | 1.2675 | 0.1220 | 2.5220 | -1.9600 | 0.0400 | 61 |
| P03 Clamp arm | 1.3272 | 21748.6 | 18.398 | 11869.8 | -0.0001 | 2.1820 | 0.9406 | -0.3585 | 0.3585 | 1.6820 | 2.6820 | -1.9630 | 3.5662 | 44 |
| P04 Connecting link | 0.3142 | 5148.1 | 6.821 | 4400.5 | 0.0000 | 2.8604 | -0.2483 | -0.2865 | 0.2865 | 1.8720 | 3.7920 | -0.6800 | 0.2520 | 40 |
| P05 Side links + pins | 0.5771 | 9456.3 | 10.306 | 6649.0 | 0.0000 | 2.2739 | -0.3700 | -0.5300 | 0.5300 | 0.6220 | 3.7420 | -0.6800 | -0.0600 | 64 |
| P06 Piston rod | 1.3683 | 22422.3 | 10.315 | 6655.1 | 0.0000 | 2.7430 | -2.7593 | -0.3150 | 0.3150 | 1.8195 | 3.7327 | -5.3852 | -0.0558 | 20 |
| P07 Air cylinder | 15.6145 | 255876.1 | 60.111 | 38781.1 | 0.0111 | 1.9790 | -5.4029 | -1.6014 | 1.6014 | 0.5351 | 3.5952 | -8.1304 | -2.9913 | 167 |
| H1 Holding screw | 0.3114 | 5103.2 | 6.045 | 3900.1 | 0.0288 | 2.5179 | 3.2181 | -0.2800 | 0.2800 | 1.2255 | 4.2255 | 2.8867 | 3.5333 | 104 |
| H2-a Saddle washer, upper | 0.0643 | 1053.0 | 1.832 | 1182.0 | 0.0000 | 2.6119 | 3.2100 | -0.4688 | 0.4688 | 2.4805 | 2.6685 | 2.7100 | 3.7100 | 13 |
| H2-b Saddle washer, lower | 0.0643 | 1053.0 | 1.832 | 1182.0 | 0.0000 | 1.7521 | 3.2100 | -0.4688 | 0.4688 | 1.6955 | 1.8835 | 2.7100 | 3.7100 | 13 |
| H3-a Hex nut, upper | 0.0421 | 689.3 | 0.985 | 635.5 | 0.0000 | 2.7785 | 3.2100 | -0.2800 | 0.2800 | 2.6685 | 2.8885 | 2.8867 | 3.5333 | 26 |
| H3-b Hex nut, lower | 0.0421 | 689.3 | 0.985 | 635.5 | 0.0000 | 1.5855 | 3.2100 | -0.2800 | 0.2800 | 1.4755 | 1.6955 | 2.8867 | 3.5333 | 26 |
| H4 Port plug | 0.0297 | 486.9 | 0.921 | 594.2 | 0.0000 | 3.3216 | -3.9823 | -0.2053 | 0.2053 | 3.1396 | 3.5212 | -4.2207 | -3.7591 | 40 |

The small off-axis CoM of P07 (x = 0.0111) comes from the one-sided slots and ports; that of H1 (x = 0.0288) from the
helical thread run-out.

**Whole assembly:**
- 13 bodies (7 custom + 6 hardware instances).
- Total volume 24.0734 in3 (394 492.6 mm3); total area, sum over bodies, 195.989 in2 (126 444.1 mm2).
- Centre of mass, uniform density: (0.0076, 1.8354, -3.9302) in.
- Bounding box, in: X [-1.6014, 1.6014], Y [0, 4.2255], Z [-8.1304, 3.71]. In mm: X [-40.676, 40.676], Y [0, 107.328],
  Z [-206.512, 94.234].

**Key functional checks:**
- Base bracket 2.864 wide, 4.22 long, sheet 0.122; mounting holes 4 x dia 0.34 at 1.25 along Z and 1.786 across (riser
  flange; the base-plate holes are obround at x = +/-0.890..0.893).
- Arm underside y = 1.7885; arm tip z = 3.5662; slot 0.402 wide, end-arc centres 2.351 apart.
- Holding screw lower end y = 1.2255; top of the linkage (P04) y = 3.792.
- Overall length 11.8404 (z = -8.1304 to 3.71).
- Cylinder axis 16.0861 degrees, through (0, 2.44, -3.81) and (0, 3.432, -0.37).

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs. The catalogue drawing and product data were compared with it.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Mounting hole spacing across | 1.79 | 1.786 (riser flange), 1.783 (base-plate obround centres) | Follow the 3D. |
| Mounting hole dia | 0.34 (11/32 = 0.34375 in the product data) | 0.34 | Follow the 3D. |
| Base width | 2.86 | 2.864 | Same to rounding. |
| Base length, hole pitch | 4.22, 1.25 | 4.22, 1.25 | Agree. |
| Arm tip to base front | 3.57 | 3.5662 | Agree to rounding. |
| Overall length, height | 11.84, 3.79 | 11.8404, 3.792 (top of P04) | Agree. |
| Screw lower end, arm underside | 1.23, 1.79 | 1.2255, 1.7885 | Agree. |
| Adjustable length | 2.35 | slot end-centre distance 2.351 | Agree. |
| Arm opening angle | 95 degrees | not modelled (clamped pose only) | Informational. |
| Product data "arm length 3 5/8", "arm height 1 7/8", "clamping clearance 1 7/32" | as stated | not compared (definitions unknown) | Informational. |
| Holding screw | 3/8-16, rigid tip, steel/rubber | 3/8-16 helical thread, hex head, no rubber tip | Follow the 3D. |
| Ports | 2 x 1/8 NPT | 2 threaded rear ports + 1 plain front port closed by a plug | Follow the 3D. |
| Mounting fasteners | not included | none modelled | Agree. |

**Undetermined, not recoverable from the sources:**
- Thread phase of the second (45 degree) rear cylinder port; the phase of the top port is approximate (+/-0.002).
- Exact thread start/run-out shape of the holding screw at the head and at the end chamfer (the source uses free-form
  surfaces there).
- Arm-to-link pin, piston, seals, bore and internal air passages (not modelled).
- The open pose and the kinematic limits (only the 95 degree opening angle is stated).
- Exact materials and surface finishes.
