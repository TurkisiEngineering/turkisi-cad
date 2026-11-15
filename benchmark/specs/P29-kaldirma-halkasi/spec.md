# Design specification: swivel hoist ring, hand-tightened, 3/4-10 shoulder bolt

A swivel hoist ring as assembled: a star-shaped base that is turned by hand, a shoulder bolt with a 3/4-10 thread
through the base, a hex retainer sleeve on the bolt, a swivel bushing around the sleeve, and a forged lifting bail whose
two trunnions sit in slots of the bushing. This document is the only source for the rebuild. Every dimension below was
measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may
  work in millimetres; the origin and the axes do not change.
- **Global frame (use exactly, no realignment):**
  - **The bolt axis is the Y axis** (x = 0, z = 0); +Y points from the thread end up to the bail.
  - **y = 0 is the top face of the base plate**; the bolt thread end is at y = -1.375, the bail top at y = 5.62.
  - **The bail lies in the XY plane** (its trunnions are on the line y = 0.595, z = 0, parallel to X); it is symmetric
    about the planes x = 0 and z = 0. Its thickness direction is Z.
- **Notation:** "(r, y)" = half-section of a body of revolution about the Y axis (r = distance from the Y axis),
  revolved 360 deg. "Plan view" = the XZ plane seen along Y. "arc R c=(a, b) from P to Q" = circular arc of radius R
  about centre (a, b), the short way.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description

The **base** (P01) is a 0.375 thick six-pointed star plate with a raised ring on top and a matching recess underneath
and a plain bore of diameter 0.75. The **shoulder bolt** (H1) passes up through the base and the **hex retainer
sleeve** (P04); a collar on the bolt sits in the base's lower bore chamfer; the 3/4-10 thread projects 1.0 below the
base. The **swivel bushing** (P03) is a ring around the sleeve, under the sleeve's hex flange, with a slot through both
walls along X. The **lifting bail** (P02) is a round bar of diameter 0.75 bent into an inverted U; its two ends turn
inward as trunnions that sit in the bushing slot; a web plate of the same 0.75 thickness fills the U below a large
hole.

**Simplifications that exist in the source model and must be reproduced:**
- The bolt thread **is modelled** as a real helical thread (section 4, H1).
- No internal threads anywhere; all bores are plain. No markings, no retaining ring, no washer.

## 3. Part list

4 distinct custom parts and 1 hardware item, **5 bodies in total**, one of each.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Base, six-point star plate | custom | steel |
| P02 | 1 | Lifting bail with web | custom | forged steel |
| P03 | 1 | Swivel bushing with trunnion slot | custom | steel |
| P04 | 1 | Hex retainer sleeve with domed top | custom | steel |
| H1 | 1 | Shoulder bolt 3/4-10, thread modelled | hardware | steel |

## 4. Part geometry

### P01 Base (one solid, 67 faces)

**B1. Body of revolution about Y**, closed half-section (r, y):
(0.375, 0.055) -> 45 deg chamfer to (0.44, 0.12) -> raised-ring top **y = 0.12** out to (0.83, 0.12) -> 45 deg cone
down to (0.95, 0) -> **plate top y = 0** outward (to the star outline, B2) -> **plate bottom y = -0.375** back in to
(0.95, -0.375) -> 45 deg cone up to (0.83, -0.255) -> **recess floor y = -0.255** in to (0.44, -0.255) -> 45 deg chamfer
to (0.375, -0.19) -> **bore r = 0.375 (diameter 0.75)** up to (0.375, 0.055).

**B2. Star outline** (plan view; it bounds the plate between y = -0.375 and 0; every edge parallel to Y):
- **root circle R1.25** about the axis;
- **six lobes, 0.5 wide** (sides parallel to the lobe centre line at 0.25 from it), centred on the directions at
  **30, 90, 150, 210, 270 and 330 deg** measured in the XZ plane from +X toward +Z (so one lobe on +Z, one on -Z, and
  the others at +/-30 deg from +X and from -X); lobe tips on the **circle R1.75** (tip-to-tip 3.5);
- **R0.08 rounds** at all twelve tip corners (lobe side to tip arc; round centres e.g. (x, z) =
  (+/-0.17, 1.661325) for the +Z lobe);
- **R0.39 rounds** at all twelve roots (lobe side to root circle; centres e.g. (+/-0.64, 1.509967) for the +Z lobe,
  tangent to the side and to the R1.25 circle).
- The raised ring and the recess (r <= 0.95) are inside the root circle, so the star outline only cuts the plate.

### P02 Lifting bail (one solid, 54 faces)

**L1. Round bar, diameter 0.75 (R0.375)**, swept along this centre line (symmetric about x = 0; right half given):
- **trunnion:** straight on the line y = 0.595, z = 0 from **x = 0.545** (end) to **x = 1.648858**;
- **corner ball:** a sphere R0.375 centred at **(1.648858, 0.595, 0)** joins trunnion and leg (sharp path corner);
- **leg:** straight from (1.648858, 0.595, 0) in the direction **(-0.024258, 0.999706, 0)** (leaning inward by
  1.390 deg) for 3.115343, to the tangent point **(1.573286, 3.709426, 0)**;
- **top arc:** circle **R1.57375 about (0, 3.67125, 0)** in the XY plane, tangent to both legs, over the top (the bar
  top is y = 5.62; outer arc radius 1.94875, inner 1.19875).
- **Trunnion ends:** flat end face x = +/-0.545 (radius 0.325) with a 45 deg chamfer cone to the bar radius 0.375 at
  x = +/-0.595.

**L2. Web plate**, thickness 0.75 (z from -0.375 to 0.375, flush with the bar sides), united with the bar:
- outline in the XY plane: below by the **arc R2.25 about (0, -0.1525)** (lowest at x = 0, y = 2.0975), on the sides
  by the two **leg centre lines** (the arc meets them at (+/-1.629344, 1.399189)), at the top by the **top-arc centre
  line R1.57375**;
- **D-shaped hole:** the half circle **R1.19875 about (0, 3.67125)** below y = 3.67125, continued straight up by the
  lines **x = +/-1.19875** (through the top of the web). Above y = 3.67125 the hole is closed by the bar itself; the
  hole width 2.3975 equals the inner width of the top arc.
- **Full rounds R0.2** on both faces along the lower arc and along the whole D-hole edge: the edge is a band
  |z| <= 0.175 on the cylinder R2.25 (lower arc), R1.19875 (hole) or plane x = +/-1.19875 (hole sides), joined to the
  faces z = +/-0.375 by quarter-round tori / cylinders R0.2 (round centres at |z| = 0.175 and 0.2 inside the edge:
  ring radius 2.45 about (0, -0.1525), 1.39875 about (0, 3.67125), lines x = +/-1.39875). Below the hole (x = 0) the
  web is only 0.375 tall (y 2.0975 to 2.4725): there the lower and upper rounds of each face overlap; keep the material
  that both rounded shapes keep (intersection), which leaves a ridge at y = 2.285, |z| = 0.374609.

**L3. Fillets (source blends):**
- **R0.125** concave, at the inner corner between each trunnion and its leg (between the two cylinders).
- **R0.375** concave, along the line where the web's lower edge (its R2.25 band and the R0.2 rounds) meets each leg
  (in the plane z = 0 it runs from (1.251447, 1.514085) on the leg to (1.051869, 1.836488) on the R2.25 arc).
- At the top of the D-hole sides, where the R0.2-rounded hole sides (x = +/-1.19875) run into the top bar, the source
  has a concave blend of about R0.375 (bar radius) between y = 3.68 and 4.39 (|x| 1.16 to 1.40). Its exact form is
  undetermined; it affects at most 0.007 in.

### P03 Swivel bushing (one solid, 26 faces)

**S1. Body of revolution about Y**, closed half-section (r, y): (0.555, 0.165) -> bottom face out to (1.015, 0.165) ->
45 deg chamfer to (1.115, 0.265) -> **outer cylinder r = 1.115 (diameter 2.23)** up to (1.115, 1.34) -> 45 deg chamfer
to (1.015, 1.44) -> **top face y = 1.44** in to (0.655, 1.44) -> 45 deg chamfer to (0.555, 1.34) -> **bore r = 0.555
(diameter 1.11)** down to (0.555, 0.165).

**S2. Trunnion slot**, cut along X through both walls, open at the bottom face. Outline in the YZ plane: **half circle
R0.4 about (y 0.57, z 0)** at the top (slot top y = 0.97), continued downward by two straight sides tangent to it at
(y 0.590934, z +/-0.399452) that **open outward by 3 deg** (plane normals (0, 0.052336, +/-0.99863)), reaching
|z| = 0.421774 at the bottom face y = 0.165.

**S3. Slot-mouth flares (source blend surfaces, different on the two sides):** where the slot meets the outer cylinder
its edge is relieved by a smooth flared surface. Boundary points (x, y, z), mirror in z:
- **+X mouth:** on the slot side face from (0.92805, 0.1693, 0.42155) to (0.93879, 0.59093, 0.39945), then along the
  slot top from (0.93879, 0.59093, 0.39945) via (0.96744, 0.78191, 0.33926) to (1.03794, 0.97, 0); on the outer
  cylinder from (0.99957, 0.265, 0.49406) via (1.00849, 0.5932, 0.47558), (1.03949, 0.80569, 0.40335) to
  (1.115, 1.01332, 0). (Width at the top about 0.077 radially x 0.043 in Y.)
- **-X mouth (larger, about 0.1 x 45 deg at the top):** on the slot side face from (-0.8707, 0.165, 0.42177) to
  (-0.88369, 0.59093, 0.39945), along the slot top via (-0.9222, 0.782, 0.3392) to (-1.015, 0.97, 0); on the outer
  cylinder from (-0.95973, 0.265, 0.56757) via (-0.97075, 0.59617, 0.54851), (-1.01338, 0.83602, 0.46507) to
  (-1.115, 1.07, 0); on the bottom face from (-0.8707, 0.165, 0.42177) to (-0.89882, 0.165, 0.47154).
- Sections: at y = 0.3 the flare is a nearly straight line from (0.931448, z 0.414699) to (1.000538, 0.492085) on +X
  and from (-0.874901, 0.414699) to (-0.96092, 0.565559) on -X; at y = 0.8 from (0.972505, 0.327261) to
  (1.038015, 0.407124) and from (-0.928914, 0.327261) to (-1.002684, 0.487699).
- The exact surfaces are undetermined (free-form in the source); a smooth surface through these curves is expected.

### P04 Hex retainer sleeve (one solid, 32 faces)

- **Body of revolution about Y**, half-section (r, y): (0.425, 1.945) -> 45 deg chamfer to (0.375, 1.895) -> **bore
  r = 0.375 (diameter 0.75)** down to (0.375, 0.185) -> 45 deg chamfer to (0.44, 0.12) -> bottom face y = 0.12 out to
  (0.525, 0.12) -> **cylinder r = 0.525 (diameter 1.05)** up to (0.525, 1.44) -> flange underside **y = 1.44** out to the
  hex -> hex up to y = 1.755 -> **dome: arc R1.82 c=(-0.060821, 0.191039)** from (0.87, 1.755) to (0.425, 1.945).
- **Hex flange:** prism along Y from y = 1.44, **1.74 across flats**, flats normal to **+/-X** and to the directions at
  +/-60 deg from X in the XZ plane (corners on +/-Z); corners turned to **diameter 1.985 (R0.9925)**; corner chamfer
  **cone r = 0.87 + (1.755 - y)** (45 deg about Y), so the corners are cut from y = 1.6325 upward and the dome starts on
  the flats at y = 1.755.

### H1 Shoulder bolt 3/4-10 (one solid, 46 real faces)

**H1. Body of revolution about Y**, half-section (r, y), bottom to top:
(0, -1.375) -> **end face** to (0.3, -1.375) -> 45 deg chamfer to (0.375, -1.3) -> thread zone (major radius 0.375) up
to y = -0.375 -> **run-out cone r = -y** (45 deg) to (0.310048, -0.310048) -> **relief cylinder r = 0.310048** up to
(0.310048, -0.278967) -> **concave R0.1 fillet c=(0.375, -0.355)** to (0.375, -0.255) -> **collar underside y = -0.255**
out to (0.44, -0.255) -> 45 deg cone to (0.375, -0.19) -> **shank r = 0.375 (diameter 0.75)** up to (0.375, 1.867218)
-> 45 deg chamfer to (0.297218, 1.945) -> **top face y = 1.945** to the axis.

**H2. Centre holes:** at both end faces a **60 deg included cone, diameter 0.11 at the face**, depth 0.095263 (apex at
y = -1.279737 and y = 1.849737).

**H3. Thread 3/4-10, right-hand, single start, pitch P = 0.1, 60 deg**:
- major radius 0.375, minor radius 0.310048 (depth 0.064952 = 0.75 x 0.866025 P); symmetric trapezoid profile in
  every half-plane through the Y axis: **flat crest 0.0125 (P/8) on r = 0.375, flat root 0.0125 (P/8) on r = 0.310048**,
  straight flanks at 30 deg to the radial direction (each 0.0375 long axially).
- **Phase:** in the half-plane z = 0, x > 0 (theta = 0) the crest-flat centres are at **y = -1.21875 + 0.1 k** and the
  root-flat centres at y = -1.26875 + 0.1 k. Theta increases from +X toward -Z (right-hand rotation about +Y) and every
  position moves by **+0.1 x theta / 360 deg** (at theta = 90 deg, the half-plane x = 0, z < 0, crests at
  y = -1.19375 + 0.1 k).
- **Extent:** from the end chamfer (the thread runs out through it) to y = -0.375; above it the run-out cone r = -y
  removes the groove's remaining material down to the relief cylinder (material kept only where r <= -y between
  y = -0.375 and -0.310048).

## 5. Assembly

All five bodies are built in place with identity placement:
- Base on y = -0.375 .. 0.12; sleeve bottom face y = 0.12 on the base raised ring; bolt through base and sleeve bores
  (diameter 0.75 in 0.75, face contact), its collar in the base's lower bore chamfer (face contact), its top face flush
  with the sleeve top y = 1.945; thread below the base from y = -1.375 to -0.375 (**thread length 1.0**).
- Bushing y = 0.165 .. 1.44 around the sleeve (bore 1.11 on 1.05: clearance), its top face against the hex flange
  underside y = 1.44.
- Bail trunnions (diameter 0.75, axis y = 0.595) in the bushing slot (top R0.4 about y = 0.57: the trunnion top
  y = 0.97 touches the slot top); trunnion end faces x = +/-0.545 clear the sleeve (r 0.525) by 0.02.
- **No body pair overlaps** (all common volumes 0).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body
(hardware 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Base with six strike points | 2.28779 | 37490.14 | 18.2850 | 11796.78 | -0.0000 | -0.1477 | 0.0000 | -1.6037 | 1.6037 | -0.3750 | 0.1200 | -1.7500 | 1.7500 | 67 |
| P02 | Lifting bail | 7.40878 | 121408.11 | 37.7183 | 24334.32 | -0.0000 | 2.7542 | -0.0000 | -2.0239 | 2.0239 | 0.2200 | 5.6200 | -0.3750 | 0.3750 | 54 |
| P03 | Swivel bushing | 2.95713 | 48458.69 | 17.0476 | 10998.45 | 0.0045 | 0.8629 | -0.0000 | -1.1150 | 1.1150 | 0.1650 | 1.4400 | -1.1150 | 1.1150 | 26 |
| P04 | Hex retainer sleeve | 1.42552 | 23360.09 | 14.7535 | 9518.38 | 0.0000 | 1.3114 | 0.0000 | -0.8700 | 0.8700 | 0.1200 | 1.9450 | -0.9925 | 0.9925 | 32 |
| H1 | Shoulder bolt 3/4-10 | 1.37752 | 22573.43 | 10.2141 | 6589.70 | -0.0000 | 0.3441 | -0.0001 | -0.4400 | 0.4400 | -1.3750 | 1.9450 | -0.4400 | 0.4400 | 46 |

Exact extremes: base x +/-1.603749, z +/-1.75; bail x +/-2.023858, y 0.22 to 5.62, z +/-0.375; bushing +/-1.115,
y 0.165 to 1.44; sleeve x +/-0.87, z +/-0.9925, y 0.12 to 1.945; bolt y -1.375 to 1.945, r 0.44.
**Whole assembly:** 5 bodies; total volume 15.45673 in3 (253290.46 mm3); total area 98.0185 in2 (63237.63 mm2);
centre of mass (0.0000, 1.6150, 0.0000) in; bounding box X [-2.023858, 2.023858], Y [-1.375, 5.62], Z [-1.75, 1.75] in
(mm: X [-51.406, 51.406], Y [-34.925, 142.748], Z [-44.45, 44.45]).

**Key functional checks:** overall height 6.995; base star diameter 3.5 (tip to tip, along Z); bail bar diameter 0.75;
bail hole width 2.3975; thread 3/4-10 right-hand, 1.0 long below the base.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Overall height | 6.995 (drawing), 7 (product data) | 6.995 | Agree |
| Inside width | 2.4 (drawing), 2 3/8 (product data) | 2.3975 | Agree within rounding |
| Base diameter | 3.5 | 3.5 tip to tip | Agree |
| Bail thickness | 0.75 | 0.75 | Agree |
| Thread | 3/4-10, 1 long | 3/4-10 modelled, 1.0 below the base | Agree |
| Pivot 180 deg, swivel 360 deg | movement note | not a modelled quantity | Informational |

**Undetermined:** the exact free-form surfaces of the two bushing slot-mouth flares (S3) and of the blends at the top of
the bail hole sides (L3, third item); forging draft and parting lines (none modelled).
