# Design specification: external gear pump with flange mount, keyed shaft and threaded ports

A small fixed-displacement hydraulic gear pump as a simplified catalogue model: a front cover with the two-hole mounting
flange and pilot, a thin middle plate, a rear housing carrying the two threaded side ports, a keyed drive shaft with a
Woodruff key, and four hex heads with washers on the rear face. This document is the only source for the rebuild. Every
dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **Z is the pump axis direction.** The shaft points to **+Z**; the hex heads are at the rear (**-Z**).
  - The **mounting face** of the flange (the face the pilot stands on) is the plane **z = 0.495**. The pilot face is
    z = 0.75, the shaft end z = 2.0, the rear ends of the hex heads and of the rear pads z = -1.928 / -2.0.
  - **Shaft axis: the line x = 0, y = 0.5315**, parallel to Z (the pilot and the flange holes are centred on y = 0.5315).
  - **X** runs across the flange (the two mounting holes lie on the line y = 0.5315 at x = +/-1.625) and along the two
    port axes. **Y** is the long direction of the housing (the drive-shaft side is +Y).
  - The two **ports** share the axis **y = 0.0142, z = -1.367**, parallel to X: the larger port opens toward -X, the
    smaller toward +X.
  - Joint planes: front cover / middle plate **z = -0.537**; middle plate / rear housing **z = -0.7385**; rear housing
    bosses / washers **z = -1.648**.
  - Every custom body is mirror-symmetric about the plane x = 0, except the two port threads of the rear housing.
- **Profile conventions:** "(x, y)" = outline in a plane normal to Z, extruded along Z between the stated z values.
  "disc (cx, cy) R r" = full circle of radius r about (cx, cy). "Concave fillet R f at (cx, cy)" = a circular arc of
  radius f about (cx, cy) that bridges two outline elements tangentially; the region between the two elements and the
  arc is filled (the arc's centre lies outside the material). Tangent points are given where useful.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description and source simplifications

The **front cover** (P01) is a cast housing block whose outline is two overlapping R1.25 circles with four bolt bosses
and two side bulges; on its +Z end it carries the two-hole mounting flange (0.406 thick), the 2.0 diameter pilot with a
shallow central recess and four arc-shaped slots in the pilot face. Below the flange (toward -Y) the block is cut back
into a domed "skirt" with two bolt bosses, a centre lobe and a drain boss. The **middle plate** (P02) is a 0.2015 thick
slab with the housing outline grown by 0.0205. The **rear housing** (P03) repeats the housing outline, carries the
port block (a half-round barrel across X with a threaded port at each end), four bolt bosses whose rear faces seat the
washers, a 58 deg chamfered rear part, a rear centre boss, two round rear pads and a rib on -Y with a blind hole. The
**shaft** (P04) is a plain 0.5 cylinder with a Woodruff keyseat holding the **key** (P05). **Washers** (H1) and **hex
heads** (H2) sit on the four rear bosses.

**Simplifications that exist in the source model and must be reproduced:**
- **No pump internals.** No gears, no gear bores, no bearing bores, no seals: the front cover, the middle plate and the
  rear housing are solid apart from the features listed. The shaft does not enter the housing: it starts at the floor
  of the pilot recess (z = 0.6225) and stands on it.
- **No bolts.** The four hex heads and washers have no shanks and no holes, and no bolt holes exist in any housing part.
  Each hex head is a plain hex prism with a chamfered outer end; each washer is a plain solid disc.
- The two ports in the rear housing **are modelled with helical straight threads** (section 4, "Port threads"); the
  ports are connected by a plain 0.375 bore. The blind hole in the rib is plain (no thread).
- The mounting holes are plain through holes with sharp edges.

## 3. Part list

5 distinct custom parts / bodies (one of them the key, counted as hardware) and 2 distinct hardware items repeated four
times: **13 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Front cover with mounting flange and pilot | custom | aluminium |
| P02 | 1 | Middle plate | custom | not stated |
| P03 | 1 | Rear housing with ports | custom | aluminium |
| P04 | 1 | Drive shaft, 0.5 dia, keyed | custom | not stated |
| P05 | 1 | Woodruff key, 0.125 wide | hardware | not stated |
| H1 | 4 | Flat washer, 0.5729 dia x 0.03 (H1-a, H1-b, H1-c, H1-d) | hardware | not stated |
| H2 | 4 | Hex head, 0.5317 across flats x 0.25 (H2-a, H2-b, H2-c, H2-d) | hardware | not stated |

Equivalence groups: H1-a..d are identical (translated copies); H2-a..d are identical (translated copies, same
orientation). The four bolt positions (used by H1, H2 and the bosses of P01 / P03) are:
**a (-0.95, 0.9365), b (-0.95, -0.9375), c (0.95, -0.9375), d (0.95, 0.9365)**. Note the 0.001 asymmetry in y
(+0.9365 / -0.9375); keep it.

## 4. Part geometry

### 4.0 The housing outline O1 (used by P01 and P03; P02 uses it grown by 0.0205)

O1 is a closed outline in the XY plane made of these elements (all centres and radii exact):
- **Upper cap:** circle **R1.25 about (0, 0.5315)**, used only for its part above the line y = 0.9365 (between the two
  upper bosses); it reaches y = 1.7815 at x = 0.
- **Lower cap:** circle **R1.25 about (0, -0.5315)**, used only for its part below the line y = -0.9375; it reaches
  y = -1.7815.
- **Four bolt bosses:** discs **R0.307** about the four bolt positions a, b, c, d (section 3).
- **Two side bulges:** discs **R0.704 about (+/-0.548, -0.0005)** (outermost x = +/-1.252).
- **Four concave fillets R0.307** joining each bulge to the boss above and below it, centred **(+/-1.4093, 0.5290)**
  (upper) and **(+/-1.4093, -0.5300)** (lower). Tangent points, right side: upper fillet on the bulge (1.1477, 0.3682),
  on boss d (1.17965, 0.73275); lower fillet on the bulge (1.1477, -0.3692), on boss c (1.17965, -0.73375).
- **Upper cap-to-boss fillets:** concave **R0.04 at (+/-1.0610, 1.2653)**, tangent to the cap at (+/-1.0281, 1.2425) and
  to the boss at (+/-1.0482, 1.2274).
- **Lower cap-to-boss fillets** (present only where stated per part): concave **R0.04 at (+/-1.0601, -1.2666)**,
  tangent to the cap at (+/-1.0272, -1.2438) and to the boss at (+/-1.0474, -1.2287). Where a part has no lower fillet,
  the lower cap and the boss meet in a sharp corner at (+/-1.0349, -1.2325).
- The inside is completely filled (the polygon through the four boss centres and the two bulge centres is solid).

### P01 Front cover with mounting flange (one solid, 236 faces in the original)

Build it as a housing block, a flange plate and a pilot, then cut the -Y pocket and the cone, then add the details and
the rounds.

**A1. Housing block:** O1 **with both upper and lower R0.04 fillets**, extruded from the rear face **z = -0.537** up to
**z = 0.404**. Its top edges (z = 0.404) along the four bosses, the two bulges and the four R0.307 concave fillets are
rounded **R0.3** (convex). On the R0.307 bosses this leaves only a 0.007 radius flat at the top, so each visible boss top
is a dome: in any half-section through the boss axis the profile is a vertical line to z = 0.104 and an arc R0.3 about
(s = 0.007, z = 0.104) up to z = 0.404 (s = distance from the boss axis). On the bulges the round is a torus R0.3 about the
circle of radius 0.404 at z = 0.104; on the concave fillets a torus R0.3 about the circle of radius 0.607 at z = 0.104.
Only the parts of this round that lie outside the flange outline O2 (A2) and outside the pocket (A4) remain visible.

**A2. Flange plate:** outline **O2** = the convex hull of the circle **R1.25 about (0, 0.5315)** and four circles
**R0.375 about (+/-1.6, 0.2496) and (+/-1.6, 0.8134)**, extruded from **z = 0.089 to the mounting face z = 0.495**
(thickness **0.406**). O2 vertices, going round from the top: arc R1.25 about (0, 0.5315) from (-0.4803, 1.6855) over
(0, 1.7815) to (0.4803, 1.6855); straight line to (1.7441, 1.1596) (line with unit normal (0.3842, 0.9232), distance
1.7407 from the origin); arc R0.375 about (1.6, 0.8134) to (1.975, 0.8134); straight line x = 1.975 down to
(1.975, 0.2496); arc R0.375 about (1.6, 0.2496) to (1.7441, -0.0966); straight line to (0.4803, -0.6225) (normal
(0.3842, -0.9232), distance 0.7593); arc R1.25 about (0, 0.5315) through (0, -0.7185) to (-0.4803, -0.6225); then the
mirror image. Width 3.95 (x = +/-1.975), height 2.5 (y = -0.7185 to 1.7815).
- **Two mounting holes:** through holes **diameter 0.39 (R0.195)** on the axes **(+/-1.625, 0.5315)** (3.25 apart),
  from z = 0.089 to 0.495, sharp edges.
- The upper cap of O1 (R1.25 about (0, 0.5315)) coincides with the top arc of O2, so on +Y the housing wall runs straight
  up to the mounting face.

**A3. Pilot:** cylinder **diameter 2.0 (R1.0) about the shaft axis** from z = 0.495 to **z = 0.71**, then a **45 deg
chamfer** to **R0.96 at the pilot face z = 0.75**. No round where the pilot meets the mounting face.
- **Central recess:** cylinder **diameter 1.0 (R0.5)** about the shaft axis from the pilot face down to a flat floor at
  **z = 0.6225** (0.1275 deep); its mouth is chamfered 45 deg from R0.54 at z = 0.75 to R0.5 at z = 0.71.
- **Four arc slots** in the pilot face, one per quadrant about the shaft axis, each centred on the 45 deg diagonal:
  inner wall **R0.6405**, outer wall **R0.8595** (centre radius 0.75, width 0.219) about the shaft axis, from **18.75 deg
  to 71.25 deg** (and +90, +180, +270 deg) measured from +X about (0, 0.5315); both ends are half circles **R0.1095**
  about the points at radius 0.75 and 18.75 / 71.25 deg (slot end centres in the first quadrant (0.7102, 0.7726) and
  (0.2411, 1.2417); others by 90 deg steps about the shaft axis: (-0.2411, 1.2417), (-0.7102, 0.7726), (-0.7102,
  0.2904), (-0.2411, -0.1787), (0.2411, -0.1787), (0.7102, 0.2904)). Depth from the pilot face **0.255**: the walls are
  vertical down to z = 0.595, then the bottom edges are rounded **R0.1** (concave) all round, leaving a flat floor
  0.019 wide at **z = 0.495** (the floor lies on the mounting-face level).

**A4. Pocket on -Y (between the two lower bosses):** define the **V region** = all points (x, y) with
**y < (0.1251 - 0.766 |x|) / 0.6428** (two straight "web lines" with unit normals (+/-0.766, -0.6428), meeting at
(0, 0.19462), 40 deg below the X axis on each side). Remove the material that lies inside the V region, outside O2,
outside the two lower boss discs R0.307 (b and c) and outside the centre lobe A5, **above z = 0.089** (up to the top).
The pocket floor is the plane **z = 0.089** (same level as the flange underside). The web walls are the parts of the two
web lines between the lower boss and the R0.079 fillets of A5.

**A5. Centre lobe:** disc **R0.563 about (0, -0.4865)** from the pocket floor z = 0.089 up to a flat top **z = 0.404**
(0.091 below the mounting face; its -Y edge at y = -1.0495). The lobe is joined to each web line by a **concave fillet
R0.079 centred (+/-0.6171, -0.6637)**, tangent to the lobe at (+/-0.5411, -0.6419) and to the web line at (+/-0.6776,
-0.6129). The region between the web walls, the lower bosses and the flange (outside the V region) stays solid up to the
top z = 0.404.

**A6. Cone chamfer on the lower cap (below the pocket floor):** inside the V region (but not inside the two lower boss
discs and not inside the drain boss A7), the block below z = 0.089 is bounded by a **cone about the axis x = 0,
y = -0.5315: radius 1.25 at z = -0.3305, half-angle 50 deg, narrowing upward** (radius 0.75006 at z = 0.089). Material
outside this cone and above z = -0.3305 is removed; below z = -0.3305 the R1.25 lower cap is unchanged. The cone meets
the pocket floor in the circle R0.75 about (0, -0.5315).

**A7. Drain boss:** cylinder **R0.25 about (0, -1.5315)** (touching the lower cap circle at y = -1.7815) from the rear
face up to a flat top at **z = 0.089**; it is not cut by A6.

**A8. Rounds of P01** (radius; location):
- R0.3 convex: A1 (domes).
- R0.1 concave: slot bottoms (A3).
- **R0.04 concave** where the housing walls (upper cap, upper bosses a / d, bulges, upper and lower R0.307 fillets) meet
  the flange underside z = 0.089; where the pocket floor z = 0.089 meets the lobe, the web walls and the lower bosses;
  vertical R0.04 fillets of O1 (A4.0); where the drain boss meets the cone.
- **R0.04 convex:** top edge of the lobe (z = 0.404); top edges of the web walls (z = 0.404); where the cone meets the
  pocket floor; the top edge of the drain boss.
- **R0.02:** convex where the R1.25 lower cap turns into the 50 deg cone (round about the circle R1.23 at z = -0.3399);
  concave where the skirt top z = 0.404 meets the flange side walls (the two lower straight lines of O2 and the lower
  R1.25 arc; round centred z = 0.424); small vertical concave R0.02 where the bulges meet the lower straight lines of O2.
- **R0.01 convex:** all edges of the mounting face z = 0.495 along the O2 outline, and the free edges of the flange
  underside z = 0.089 along O2 (the ends, the two upper lines, and the lower lines from x = +/-1.1728 outward).
- Sharp: the rear face z = -0.537, the mounting holes, the pilot / mounting face junction, the pilot face edges (they
  are the chamfers), the recess.

### P02 Middle plate (one solid, 21 faces)

Slab from **z = -0.7385 to z = -0.537 (0.2015 thick)** with the outline **O1 grown outward by 0.0205**: caps R1.2705
about (0, +/-0.5315); boss discs R0.3275 about a, b, c, d; bulges R0.7245 about (+/-0.548, -0.0005); concave fillets
R0.2865 at the same centres (+/-1.4093, 0.5290) and (+/-1.4093, -0.5300); **lower cap-to-boss concave fillets R0.0195
at (+/-1.0601, -1.2666)**; **no fillet at the upper cap / boss junction** (sharp corner at (+/-1.04865, 1.24879)).
Extent x = +/-1.2775, y = +/-1.802. No holes, sharp edges.

### P03 Rear housing with ports (one solid, 281 faces)

**B1. Top lip:** O1 **with the upper R0.04 fillets and without the lower ones** (lower caps meet the lower bosses in
sharp corners), extruded from the joint face **z = -0.7385 down to z = -0.774**.

**B2. Main block:** from z = -0.774 down to the **rear face z = -1.648**, outline = O1 (as B1) united with the
**port-block rectangle x = -1.4215..1.4215, y = -0.5788..0.6072** (the bulges are swallowed by the rectangle; the
rectangle's long sides cut the four R0.307 concave fillets, and each re-entrant corner there gets a vertical concave
**R0.04 fillet centred (+/-1.1699, 0.6472) / (+/-1.1575, -0.6188)**).

**B3. Port block barrel:** below the port axis the port block is a **half cylinder R0.593 about the axis y = 0.0142,
z = -1.367** (lowest line z = -1.96), running from each port face x = +/-1.4215 inward to x = +/-0.6895 (inside the rear
pads B8). Above the axis the block is the rectangle of B2 up to its top face **z = -0.774** (the top face lies
0.0355 below the joint face; outside the lip it is exposed between the bulge lip and the port face). The block width
1.186 (y = -0.5788 to 0.6072) equals the barrel diameter. **Port faces: planes x = -1.4215 and x = +1.4215.**

**B4. 58 deg chamfered rear part:** on each cap side (+Y and -Y) the main block below **z = -1.0485** is bounded by a
**cone about the axis x = 0, y = +/-0.5315: radius 1.25 at z = -1.0485, half-angle 58 deg, narrowing toward -Z**, and
by the **flat planes y = +1.0835 / y = -1.0835**: in the region |y| > 1.0835, outside the bosses, material outside the
cone is removed and everything below the cone's meeting with the flat is removed, so below about z = -1.48 the block
side is the flat y = +/-1.0835 down to the rear face. Each flat is joined to the neighbouring bolt boss by a vertical
**concave fillet R0.25** centred **(+/-0.5593, 1.3335)** (+Y) / **(+/-0.5583, -1.3335)** (-Y), tangent to the flat at
x = +/-0.5593 / +/-0.5583 and to the boss at (+/-0.7347, 1.1553) / (+/-0.7341, -1.1558). The bolt bosses (R0.307,
full height from -0.7385 to the rear face -1.648) are not cut. Above z = -1.0485 the cap walls are the plain R1.25
cylinders. (B5 and B6 are added after this cut and are not affected by it.)

**B5. +Y boss:** a stadium-shaped boss: half disc **R0.25 about (0, 1.5315)** on its +Y side and straight sides
x = +/-0.25 running toward -Y into the chamfered part; from the lip down to a flat bottom **z = -1.367**.

**B6. Rib on -Y:** box **x = -0.375..0.375**, from its front face **y = -1.7815** (flat, 0.75 wide, standing slightly
proud of the R1.25 lower cap at its corners) back to the rear centre boss, from the joint face **z = -0.7385** down to
**z = -1.929**. **Blind hole diameter 0.375** (R0.1875) on the axis **x = 0, z = -1.541**, parallel to Y, from the
front face y = -1.7815 to a flat bottom at **y = -1.3815** (0.4 deep), plain, mouth rounded R0.04.

**B7. Rear centre boss:** cylinder **R0.55 about the shaft axis (0, 0.5315)** from the rear face z = -1.648 down to
**z = -1.929** (flush with the rib bottom; the two form one flat face z = -1.929).

**B8. Two rear pads:** cylinders **R0.593 about (+/-0.6895, 0.0142)** from the rear face z = -1.648 down to
**z = -2.0** (1.379 apart).

**B9. Bore and ports** (all on the port axis y = 0.0142, z = -1.367):
- **Large port (-X):** from the port face x = -1.4215: 45 deg mouth chamfer (cone from **R0.44523 at the face**,
  narrowing inward), then the **7/8-14 thread** (T1 below) to a **flat bottom at x = -0.7072** (0.71429 = 10 pitches
  deep).
- **Small port (+X):** from x = +1.4215: 45 deg mouth chamfer from **R0.38177 at the face**, then the **3/4-16 thread**
  (T2) to a flat bottom at **x = 0.7965** (0.625 = 10 pitches deep).
- **Connecting bore diameter 0.375** (R0.1875) from x = -0.7072 to x = 0.7965.

**Port threads (helical, as modelled).** Both are straight 60 deg threads, right-hand, cut as one helical groove into a
bore at the minor (crest) diameter. In every half-plane containing the port axis the profile is: crest flat on the minor
diameter, axial width p/8; flank at 30 deg to the plane normal to the axis; root flat on the major diameter, axial width
p/8; flank back. Depth a is measured along the port axis from the port face into the port; theta is measured about the
port axis from the half-plane toward +Z.
- **T1, large port:** p = 1/14 = 0.071429. Major (root) diameter **0.875** (R0.4375), minor (crest) diameter
  **0.78222** (R0.39111), thread depth 0.04639; flats 0.00893 wide. **a = x + 1.4215**; theta
  increases from +Z toward -Y. Root-flat centres in the half-plane theta = 0 at **a = 0.02232 + n p** (0.02232, 0.09375,
  0.16518, ...); at angle theta every position is **a + p theta / 360 deg** (right-hand). Crest flats are centred half
  a pitch away (a = 0.05804 + n p at theta = 0). The groove runs out through the mouth chamfer and ends abruptly at the
  flat bottom a = 0.71429.
- **T2, small port:** p = 1/16 = 0.0625. Major (root) diameter **0.75** (R0.375), minor (crest) diameter **0.66882**
  (R0.33441), depth 0.04059; flats 0.0078 wide. **a = 1.4215 - x**; theta increases from +Z toward +Y. Root-flat centres
  at theta = 0 at **a = 0.05078 + n p**, shifting by **+p theta / 360 deg**. Ends at the flat bottom a = 0.625.

**B10. Rounds of P03** (the source rounds almost every free edge of this casting):
- **R0.04 convex:** the top edges of the port block (z = -0.774) and the perimeter of both port faces (end of the
  barrel, the top edge and the two vertical edges); the edge where each R1.25 cap wall turns into the 58 deg cone (round
  about R1.21 at z = -1.0263); the rear-face (z = -1.648) perimeter edges of the bolt bosses, the R0.307 fillets, the
  R0.25 fillets and the flats y = +/-1.0835; the bottom edges of the +Y boss (z = -1.367); the front face edges of the rib
  (vertical edges at x = +/-0.375, top edge at z = -0.7385, bottom edge at z = -1.929) and the rib's lower side edges
  along Y; the bottom edge of the rear centre boss (z = -1.929); the bottom edges of the two rear pads (z = -2.0); the
  blind-hole mouth; where the flats meet the cones.
- **R0.04 concave:** vertical fillets of B2 and of O1 (upper cap to boss); where the rib sides meet the rear face
  z = -1.648, the flat y = -1.0835 (vertical, centred (+/-0.415, -1.1235)) and the cone; where the rear centre boss and
  the rear pads meet the rear face z = -1.648; between the rear centre boss and each rear pad (vertical, centred
  (+/-0.5804, 0.6377)); where the barrel meets the rear face and the pads; where the +Y boss bottom meets the cone.
- **R0.1 concave** (vertical, centred (+/-0.475, -0.6386), from z = -1.648 to -1.929): rib side to rear pad, finished
  with an R0.01 blend onto the pad.
- **R0.01 concave:** where the rib / centre-boss bottom face z = -1.929 meets the rear pads.
- Sharp: the joint face z = -0.7385 along O1, the top lip side walls, the thread and bore edges (except the chamfers).

### P04 Drive shaft (one solid, 7 faces)

Cylinder **diameter 0.5 (R0.25) about the shaft axis (0, 0.5315)** from **z = 0.6225** (standing on the recess floor of
P01) to the end **z = 2.0** (1.3775 long; **1.25 beyond the pilot face**). Plain flat ends, no chamfers.
**Woodruff keyseat:** remove the part of the shaft inside the slab **x = -0.0625..0.0625** (0.125 wide) that lies inside
the circle **R0.3115 about (y = 0.905, z = 1.562)** in the YZ plane (axis parallel to X). Keyseat bottom at y = 0.5935,
**0.188 below the shaft top line y = 0.7815**; it breaks out of the shaft surface between z = 1.2796 and 1.8444.

### P05 Woodruff key (one solid, 4 faces)

The part of the same circle **R0.3115 about (y = 0.905, z = 1.562)**, between **x = -0.0625 and 0.0625**, that lies
**below the flat top y = 0.8745**: a circular segment 0.125 thick, **0.62 long** (z = 1.252 to 1.872), 0.281 high
(y = 0.5935 to 0.8745). It fills the keyseat exactly and stands 0.093 proud of the shaft.

### H1 Washer (4 identical bodies, 4 faces each)

Plain solid disc **diameter 0.57286 (R0.28643), 0.03 thick, from z = -1.678 to z = -1.648**, axis parallel to Z through
the bolt position: H1-a (-0.95, 0.9365), H1-b (-0.95, -0.9375), H1-c (0.95, -0.9375), H1-d (0.95, 0.9365). No hole.

### H2 Hex head (4 identical bodies, 14 faces each)

Solid regular hexagonal prism, **0.53174 across flats** (flats normal to X at x = x0 +/- 0.26587; corners on +/-Y at
y = y0 +/- 0.30700), from **z = -1.678** (on the washer) to **z = -1.928** (0.25 high), axis through the bolt position
(x0, y0). The rear end (z = -1.928) is **chamfered 45 deg**: the head is intersected with a cone about its axis of
**radius 0.26587 at z = -1.928**, growing 1:1 toward +Z (radius 0.307 at z = -1.8868), so the chamfer cuts only the six
corners. No socket, no shank. H2-a (-0.95, 0.9365), H2-b (-0.95, -0.9375), H2-c (0.95, -0.9375), H2-d (0.95, 0.9365).

## 5. Assembly

All 13 bodies are built in place with identity placement.
- Axial stack: front cover rear face z = -0.537 = middle plate front face; middle plate rear face z = -0.7385 = rear
  housing joint face; washers on the rear faces of the rear bosses (z = -1.648); hex heads on the washers (z = -1.678).
- Shaft end face on the recess floor (z = 0.6225); key in the keyseat (same circle and width, face contact).
- **No body pair overlaps** (all contacts are face contacts with zero overlap volume; checked pairwise).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (small
hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-a | Washer at (-0.95, 0.9365) | 0.00773 | 126.71 | 0.5695 | 367.42 | -0.9500 | 0.9365 | -1.6630 | -1.2364 | -0.6636 | 0.6501 | 1.2229 | -1.6780 | -1.6480 | 4 |
| H1-b | Washer at (-0.95, -0.9375) | 0.00773 | 126.71 | 0.5695 | 367.42 | -0.9500 | -0.9375 | -1.6630 | -1.2364 | -0.6636 | -1.2239 | -0.6511 | -1.6780 | -1.6480 | 4 |
| H1-c | Washer at (0.95, -0.9375) | 0.00773 | 126.71 | 0.5695 | 367.42 | 0.9500 | -0.9375 | -1.6630 | 0.6636 | 1.2364 | -1.2239 | -0.6511 | -1.6780 | -1.6480 | 4 |
| H1-d | Washer at (0.95, 0.9365) | 0.00773 | 126.71 | 0.5695 | 367.42 | 0.9500 | 0.9365 | -1.6630 | 0.6636 | 1.2364 | 0.6501 | 1.2229 | -1.6780 | -1.6480 | 4 |
| H2-a | Hex head at (-0.95, 0.9365) | 0.06093 | 998.52 | 0.9337 | 602.38 | -0.9500 | 0.9365 | -1.8025 | -1.2159 | -0.6841 | 0.6295 | 1.2435 | -1.9280 | -1.6780 | 14 |
| H2-b | Hex head at (-0.95, -0.9375) | 0.06093 | 998.52 | 0.9337 | 602.38 | -0.9500 | -0.9375 | -1.8025 | -1.2159 | -0.6841 | -1.2445 | -0.6305 | -1.9280 | -1.6780 | 14 |
| H2-c | Hex head at (0.95, -0.9375) | 0.06093 | 998.52 | 0.9337 | 602.38 | 0.9500 | -0.9375 | -1.8025 | 0.6841 | 1.2159 | -1.2445 | -0.6305 | -1.9280 | -1.6780 | 14 |
| H2-d | Hex head at (0.95, 0.9365) | 0.06093 | 998.52 | 0.9337 | 602.38 | 0.9500 | 0.9365 | -1.8025 | 0.6841 | 1.2159 | 0.6295 | 1.2435 | -1.9280 | -1.6780 | 14 |
| P01 | Front cover with mounting flange | 8.17817 | 134016.18 | 34.2521 | 22098.05 | -0.0000 | 0.2223 | 0.0223 | -1.9750 | 1.9750 | -1.7816 | 1.7815 | -0.5370 | 0.7500 | 236 |
| P02 | Middle plate | 1.54506 | 25318.96 | 17.4715 | 11271.93 | -0.0000 | -0.0001 | -0.6377 | -1.2775 | 1.2775 | -1.8020 | 1.8020 | -0.7385 | -0.5370 | 21 |
| P03 | Rear housing with ports | 7.17087 | 117509.47 | 36.3821 | 23472.27 | 0.0180 | -0.0543 | -1.2696 | -1.4215 | 1.4215 | -1.7815 | 1.7815 | -2.0000 | -0.7385 | 281 |
| P04 | Drive shaft | 0.26097 | 4276.46 | 2.7204 | 1755.11 | -0.0000 | 0.5253 | 1.3021 | -0.2500 | 0.2500 | 0.2815 | 0.7815 | 0.6225 | 2.0000 | 7 |
| P05 | Woodruff key | 0.01668 | 273.31 | 0.4590 | 296.15 | 0.0000 | 0.7561 | 1.5620 | -0.0625 | 0.0625 | 0.5935 | 0.8745 | 1.2520 | 1.8720 | 4 |

**Whole assembly:** 13 bodies; total volume 17.44640 in3 (285895.33 mm3); total area 97.2979 in2 (62772.69 mm2); centre
of mass (0.0074, 0.0904, -0.5750) in; bounding box X [-1.975, 1.975], Y [-1.802, 1.802], Z [-2.0, 2.0] in
(mm: X [-50.165, 50.165], Y [-45.7708, 45.7708], Z [-50.8, 50.8]).

**Key functional checks:** overall length 4.0 (hex heads / rear pads to shaft end); overall height 3.604 (middle
plate); flange width 3.95, height 2.5, thickness 0.406; mounting holes 0.39 on 3.25 centres; pilot 2.0; shaft 0.5
extending 1.25 beyond the pilot face; key 0.125 x 0.62, seat depth 0.188; ports 7/8-14 (-X) and 3/4-16 (+X) on the axis
y = 0.0142, z = -1.367.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs. The catalogue drawing agrees with the model on every printed
dimension (4, 3.604, 3.95, 3.25, 0.39, 2.5, 2, 0.125, 0.188, 0.62, 0.406, 0.5, 1.25, 7/8-14, 3/4-16).

**Undetermined (not in the source model):** gears, gear chambers, shaft bearings and seals, the internal passages from
the ports to the gears, bolt shanks and tapped holes, the thread of the blind hole, the inside of the hex heads.
Which port is the inlet is not marked in the model (the larger, -X port is the usual suction side; not verified).
