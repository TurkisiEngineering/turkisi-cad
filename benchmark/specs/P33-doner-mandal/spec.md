# Design specification: cable-operated rotary latch with T-handle release (remote release kit, left-hand door mount)

A complete remote-release latch kit as one assembly: a stainless steel rotary latch (base plate, cover plate, claw-shaped
rotor, release lever, two pivot spacers, a stop pin, a cable clevis block and a cable end pin), the strike bolt with a
small wire ring, a U-shaped release cable with its end fittings and ferrules, and the release handle unit (plastic
handle housing, pull rod, cable anchor block and a ribbed plastic T-handle). This document is the only source for the
rebuild. Every number below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** All coordinates and dimensions are mm. Some values are round inch values (for example the
  cable diameter 6.35 = 1/4 in, the bend radius 38.1 = 1.5 in); the mm value given is the exact one.
- **Global frame (use exactly, no realignment). Every body is modelled in place in this frame (identity placement),
  each body as a separate solid.**
  - **Y is the "up" direction away from the mounting surface.** The handle housing stands on the plane **y = 0**; the
    latch base plate underside is y = 1.01.
  - **The handle pull axis is the line y = 12, z = -60.4, parallel to X**; the handle is pulled toward +X.
  - The cable lies in the plane **y = 12**; its two straight legs run parallel to X on the lines z = -60.4 (handle
    side) and **z = 15.8** (latch side).
  - The latch plates are parallel to the XZ plane; the latch pivots are parallel to Y.
  - The strike bolt axis is the line **x = -37.857, z = 75.7, parallel to Y**, head toward +Y.
- **Profile conventions:**
  - "(x, z) profile" = closed outline in a plane normal to Y, extruded along Y between the stated y values;
    "(z, y) profile" = outline in a plane normal to X, extruded along X; "(r, x)" / "(r, y)" = half-section of a body
    of revolution (r = radius from the stated axis).
  - "arc c=(a, b) R to (p, q)" = circular arc of radius R about centre (a, b) to (p, q), the short way unless stated.
  - "draft d deg" = the face is tilted by d degrees from the stated nominal plane as described.

## 2. Product description

**Handle unit (around z = -60.4, x from -57.4 to 75.5).** The **handle housing** (P01) is a plastic block on a
rectangular mounting plate (four mounting holes) with a tube along the pull axis. The **pull rod** (P03) slides in the
tube; its +X end carries the **T-handle** (P02), a ribbed plastic grip with twelve finger recesses on its -X side. The
-X end of the pull rod is a flat clevis head with a cross hole. The **cable anchor block** (P04) fills the V-notch under
the housing tube and continues toward -X into an upright tab that holds the cable. The **cable end fitting** (P05) is a
short rod with an inner wire ending in a cross barrel that sits in the clevis cross hole.

**Cable (P08)**: a solid U-shaped round cable diameter 6.35 lying in the plane y = 12, with a ferrule (P06-a, P06-b) at
each end and an end fitting (P05 at the handle, P07 at the latch).

**Latch unit (around z = 9 to 57, x from -59.3 to 9.8).** A **base plate** (P09) with two bent flanges, a **cover
plate** (P10) with a joggled tab and a bent leg that guides the cable end, a claw-shaped **rotor** (P11) and a
**release lever** (P12) between the plates on two **pivot spacers** (P13-a, P13-b), a **stop pin** (P14), a **cable
clevis block** (P15) on the lever pin and an **L-shaped cable end pin** (P16). The **strike bolt** (H1) with a dished
washer flange, an M8 x 1.25 thread and a hex head stands below the latch mouth, with a **wire ring** (H2) under its
flange.

**Simplifications that exist in the source model and must be reproduced:**
- The cable is one solid round bar (no strands, no inner/outer layer); the inner wires are short separate stubs on the
  end fittings.
- No springs (rotor spring, lever spring) are modelled. The mechanism is in one fixed pose (latch open, strike bolt
  outside the mouth).
- The pull rod passes through the T-handle shank without a hole in the handle: the two bodies overlap (section 5).
- The strike bolt thread IS modelled as a helical groove (section 4, H1). No other thread is modelled.
- Several molded parts carry small draft angles (0.5 deg, 1 deg, 1.5 deg, 2 deg); they are stated per part.

## 3. Part list

18 distinct custom parts and 2 distinct hardware items, 20 distinct items, **20 bodies in total** (the original file
has 20 solids and no empty shells).

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Handle housing with mounting plate and tube | custom | black plastic |
| P02 | 1 | T-handle (ribbed grip) | custom | black plastic |
| P03 | 1 | Pull rod with clevis head | custom | plastic (black) |
| P04 | 1 | Cable anchor block | custom | plastic (black) |
| P05 | 1 | Cable end fitting, handle side | custom | steel |
| P06 | 2 | Cable sheath ferrule (P06-a handle side, P06-b latch side; identical) | custom | steel |
| P07 | 1 | Cable end fitting, latch side | custom | steel |
| P08 | 1 | Cable, U-shaped | custom | sheathed cable |
| P09 | 1 | Latch base plate | custom | 300 series stainless steel |
| P10 | 1 | Latch cover plate | custom | 300 series stainless steel |
| P11 | 1 | Rotor (claw) | custom | stainless steel |
| P12 | 1 | Release lever | custom | stainless steel |
| P13 | 2 | Pivot spacer (P13-a lever pivot, P13-b rotor pivot; identical) | custom | stainless steel |
| P14 | 1 | Stop pin | custom | stainless steel |
| P15 | 1 | Cable clevis block | custom | stainless steel |
| P16 | 1 | Cable end L-pin | custom | stainless steel |
| H1 | 1 | Strike bolt, M8 x 1.25, hex head, dished washer flange | hardware | stainless steel |
| H2 | 1 | Wire ring (round wire, toroidal) | hardware | steel |

## 4. Part geometry

### P01 Handle housing (one solid, 41 faces)

Build it as one prism along X plus cuts:
1. **Envelope prism**, x from -22.5 to 22.5, (z, y) profile: (-88.4, 0) to (-71.8845, 0); line to (-68.5512, 8.8188);
   arc c=(-60.4, 12) R8.75 under the axis to (-52.2488, 8.8188); line to (-48.9155, 0); line to (-32.4, 0); line to
   (-32.4, 6.5); line to (-56.1619, 19.6551); arc c=(-60.4, 12) R8.75 over the top to (-64.6381, 19.6551); line to
   (-88.4, 6.5); close. The two upper lines are tangent to the R8.75 circle; they pass y = 9.8217 at z = -38.4 and
   z = -82.4. The bottom V-notch lines run from y = 0 to the R8.75 circle (they are not tangent).
2. **Plate corners:** round the four edges parallel to Y at the corners of the 45 x 56 outline with **R6** (centres
   (x, z) = (+-16.5, -82.4) and (+-16.5, -38.4)).
3. **Cut-out between the end walls:** above **y = 5** and between the two inner wall faces
   x = +-(20.5 + 0.026186 (y - 5)) (the walls are 2.0 thick at y = 5 and get thinner upward: **draft 1.5 deg**), remove
   all material except the **web-and-tube region**, whose (z, y) outline is: (-72.4, 5); line to (-68.5848, 15.0937);
   arc c=(-60.4, 12) R8.75 over the top to (-52.2152, 15.0937); line to (-48.4, 5). (The two web lines are tangent to
   the R8.75 circle.) The cut-out is open toward +Y and through the plate ends z = -88.4 and z = -32.4 (where the plate
   is only 5 high between x = -16.5 and 16.5). The webs are 2.25 thick (the web top line and the notch line are
   parallel).
4. **Tube extension:** cylinder **diameter 17.5 (R8.75)** about the pull axis from x = 22.5 to the **end face
   x = 50.5**.
5. **Bore:** diameter **12 (R6)** about the pull axis, through from x = -22.5 to **x = 19.5**, then a **counterbore
   diameter 14.7 (R7.35)** from x = 19.5 to the end face x = 50.5 (31 deep, flat shoulder at x = 19.5).
6. **Mounting holes:** four through holes **diameter 4.5** parallel to Y through the plate (y 0 to 5) at
   (x, z) = (+-12.5, -40.4) and (+-12.5, -80.4) (spacing 25 across, 40 along).

### P02 T-handle (one solid; 591 faces in the original, mostly small blends)

A molded grip: shank, hub and a crossbar along Z, all centred on the pull axis (y = 12, z = -60.4). The **parting
plane of the crossbar is x = 68.9**; its drafts are 2 deg away from that plane.

**Shank and hub:**
- **Shank:** frustum about the pull axis from the **free end x = 38.5** (radius 5.2862) to **x = 50.5** (radius
  5.3909): r(x) = 5.57967 - (72.1289 - x) tan 0.5 deg (draft 0.5 deg, narrower toward -X). Flat end face at x = 38.5.
- **Two keys** on the shank, one on the +Z side and one on the -Z side, from **x = 45 to x = 50.5**: each key lies
  between the planes y = 11.8008 - 0.0087269 x and y = 12.1992 + 0.0087269 x (1.19 thick at x = 45, 1.28 at
  x = 50.5) and reaches out radially to r_k(x) = 7.02705 - (66.1 - x) tan 0.5 deg (6.843 at x = 45, 6.891 at
  x = 50.5). The two -X end corners of each key are rounded R0.3; a small R1 round blends the key end into the shank.
- **Hub:** shoulder face **x = 50.5** (annulus from the shank out to radius 10.227), then a frustum r(x) =
  10.22528 + (x - 50.4) tan 1 deg (**draft 1 deg**, growing toward +X) running into the crossbar. The hub meets the
  crossbar -X face with an **R2.5** concave round.

**Crossbar envelope** (60 long in Z, 22 high in Y at the parting plane, x from 63.0 to 75.5):
- **Top surface:** y = -107.3214 + sqrt(Rt(x)^2 - (z + 60.4)^2), **bottom surface** y = 131.3214 - sqrt(Rt(x)^2 -
  (z + 60.4)^2), with Rt(x) = 130.3214 - |x - 68.9| tan 2 deg. So at x = 68.9 the bar is y 1.0 to 23.0 at its centre
  (z = -60.4) and thinner toward its ends (circular arcs R130.32 in each x = constant section).
- **End surfaces:** the -Z end is (y - 12)^2 + (z + 50.4)^2 = Re(x)^2 and the +Z end (y - 12)^2 + (z + 70.4)^2 =
  Re(x)^2 (taking the far side of each circle), Re(x) = 40 - |x - 68.9| tan 2 deg; so at x = 68.9 the ends are
  z = -90.4 and z = -30.4 (arcs R40 in the end view).
- **+X face (crowned):** a surface of revolution about the axis **x = -49.5, y = 12 (parallel to Z)**: its distance
  from that axis is rho(z) = sqrt(226^2 - (z + 60.4)^2) - 101. In the plane y = 12 it is an arc **R226** centred
  (x -150.5, z -60.4) with its apex **x = 75.5** at z = -60.4 (73.75 at z = -90.4); across Y it is curved with radius
  rho (125 at the centre). On each half of the face, for z from -84.85 to -69.16 and from -51.64 to -35.95, y from 3.9 to
  20.1, the face is flattened into a shallow panel (up to about 0.35 below the crowned face, panel edges rounded R1
  to R2); undetermined in detail.
- **-X face (toward the housing):** on each half of the bar a surface of revolution about the axis **x = 93, y = 12
  (parallel to Z)**: rho = 53.5 - sqrt(25^2 - (z - zc)^2), zc = -78.4 for the -Z half and zc = -42.4 for the +Z half;
  in the plane y = 12 this is x = 39.5 + sqrt(625 - (z - zc)^2) (x = 64.5 at z = zc, 63.67 at zc +- 6.4). This face
  exists only as the -X ends of the ribs between the recesses and the rim around them.
- **Edge rounds** (measured median radii, the rounds are free-form in the source): +X face to top / bottom **R2.2**;
  crossbar end corners **R2.2** (+X side) and **R3.0** (ends to top / bottom); -X face to top / bottom / ends **R1.9**.

**Grip recesses:** twelve recesses open toward -X, in two rows (y > 12 and y < 12) of six (three on each side of the
hub), symmetric about the planes y = 12 and z = -60.4. Their walls are drafted **2 deg** so that each recess widens
toward -X. Outlines **in the section x = 69** for the quadrant y > 12, z < -60.4 (points (y, z), in order, closed;
mirror about y = 12 and/or z = -60.4 for the other three quadrants):
- Recess 1 (next to the hub): (13.188, -70.883), (13.998, -70.759), (15.190, -70.456), (15.961, -70.178),
  (16.709, -69.841), (17.428, -69.447), (18.114, -68.998), (19.073, -68.228), (19.659, -67.655), (19.992, -67.446),
  (20.284, -67.763), (20.067, -70.871), (19.797, -73.755), (19.628, -74.079), (19.293, -74.227), (18.479, -74.456),
  (16.867, -74.826), (15.283, -75.083), (13.397, -75.255), (13.001, -75.025), (12.922, -74.655), (12.922, -71.433),
  (12.946, -71.063). (The side toward the hub is the hub frustum, radius 10.55 at x = 69.)
- Recess 2: (13.324, -81.569), (12.958, -81.431), (12.803, -81.070), (12.803, -77.223), (12.887, -76.896),
  (13.211, -76.681), (14.632, -76.574), (16.048, -76.396), (17.417, -76.151), (19.040, -75.792), (19.417, -76.012),
  (19.497, -76.353), (18.905, -80.510), (18.710, -80.831), (18.453, -80.933), (18.238, -80.977), (16.448, -81.283),
  (15.194, -81.435), (13.555, -81.558).
- Recess 3 (at the end): (17.669, -87.137), (17.499, -87.417), (17.250, -87.527), (15.717, -87.712), (14.510, -87.812),
  (13.321, -87.873), (13.052, -87.806), (12.830, -87.534), (12.803, -87.273), (12.818, -83.359), (13.010, -83.073),
  (13.284, -82.979), (15.438, -82.825), (18.058, -82.473), (18.377, -82.662), (18.479, -83.003), (17.679, -87.088).
- **Recess floors** follow the +X face at a wall thickness of about 3.5: measured along X the floor lies 3.54 in front
  of the +X face at mid-length (floor x = 71.53 at (y 7, z -72), 70.74 at (y 7, z -79), 69.58 at (y 7, z -85)). Floor
  and rim edges carry small rounds (R0.5 floor edges, R0.3 to R0.4 rim and corner rounds); the exact floor shape is
  undetermined.
- The central rib between the two rows is 1.84 thick at x = 69 (y 11.08 to 12.92) beside recesses 1 and 1.61 to 1.71
  thick beside recesses 2 and 3.

**Internal closed voids** (no opening to the outside; reproduce them):
- **Void A** in the shank: frustum about the pull axis from x = 48.5 (radius 3.1484) to x = 50.5 (radius 3.1309),
  flat ends.
- **Voids behind the hub** (in the crossbar, from the plane **x = 70.5** to the surface 3.5 inside the +X face, i.e.
  the surface of revolution about x = -49.5, y = 12 with rho = sqrt(222.5^2 - (z + 60.4)^2) - 101, which is x = 72.0
  on the pull axis): a central round void r(x) = 3.23563 - (x - 38.5) tan 0.5 deg (2.956 at x = 70.5), and four
  quarter-ring voids between r = 5.57967 - (72.1289 - x) tan 0.5 deg (5.565 at x = 70.5) and r = 9.03265 -
  (x - 50.3) tan 0.5 deg (8.856 at x = 70.5), separated by two cross ribs: one between the planes
  y = 11.8008 - 0.0087269 x and y = 12.1992 + 0.0087269 x, the other between z = -60.199 + 0.0087269 x and
  z = -60.601 - 0.0087269 x (1.63 thick at x = 70.5). The outer corners of the quarter voids are rounded R0.5.

### P03 Pull rod (one solid, 37 faces)

Plastic rod on the pull axis (y = 12, z = -60.4). **Parting plane z = -60.4**; the faces normal to X are drafted away
from it as stated.
- **Body of revolution** about the pull axis, (r, x): **collar R5.9 (diameter 11.8)** from the head to the shoulder
  **x = -14.714**; **shaft R4.4 (diameter 8.8)** from x = -14.714 to the shoulder **x = 20.286**; **tapered tip** from
  radius 2.9 at x = 20.286 to radius 2.6382 at the **end x = 50.286** (half-angle 0.5 deg). The shoulder at x = 20.286
  and the end face at x = 50.286 are each split along the parting plane into two halves tilted back by 1 deg
  (shoulder) and 0.5 deg (end face), so they lie at x = 20.286 / 50.286 only on the parting plane.
- **Clevis head** (x from -35.597 to -23.714): the R5.9 collar is cut by **two flats z = -64.4 and z = -56.4** (8
  apart) from the end to **x = -23.714** (the flat shoulders are drafted 1 deg). The **end is rounded about the pin
  axis** (the line x = -29.714, y = 12, parallel to Z) with **R5.9** at the parting plane, decreasing 1 deg toward each
  flat (R5.830 at the flats); the rod material is the intersection of the R5.9 collar and this rounded end. On the
  upper -Z quarter of the end (z from -64.4 to -61.4, y above 12) the end surface is free-form in the source
  (undetermined; it follows the R5.9 rounding within 0.1).
- **Cross hole diameter 6.35** along Z through both flats, axis x = -29.714, y = 12.
- **Wire slot** 2 wide between **z = -61.4 and z = -59.4**, from the end to **x = -28.683**, from y = 11 upward
  (open on top), crossing the cross hole; its floor y = 11 runs from the end to the cross hole.
- **Entry channel** 2 wide between **x = -30.683 and x = -28.683**, from the slot (z = -61.4) to the flat z = -56.4,
  above the cross hole (from y = 15.0 upward, open on top).
- **Two bottom grooves** 1.5 wide between z = -62.9 and -61.4 and between z = -59.4 and -57.9 (walls drafted 1 deg),
  from the end to x = -30.714: the groove floor is the plane y = 9.0 from the end to x = -32.360, then an arc R4 about
  the pin axis down to (x -30.714, y 8.127), then the plane x = -30.714 down to the outer surface.

### P04 Cable anchor block (one solid, 27 faces)

- **Main section** (z, y), from x = -42.42 to x = 20.0: bottom **y = 0** from **z = -71.8 to -49.0** (22.8 wide);
  sides inclined **21 deg from vertical** (each side goes 0.38386 inward per unit of height); a **cradle R8.9** about
  the pull axis (centre y 12, z -60.4), concave, whose lowest point is y = 3.1. The sides meet the cradle at
  y = 8.444 (z = -68.559 and -52.241). (The cradle clears the housing tube R8.75 by 0.15.)
- **End segment** x 20.0 to 22.5: the same section, but its bottom and cradle are rotated by 0.5 deg about the line
  (x 20.0, y 0, parallel to Z) so that the end lifts by 0.02; end face at x = 22.5 (drafted 0.5 deg).
- **End tab** x from **-44.5** to the inner face x = -42.3938 - 0.0087269 y (2.08 thick at the bottom, draft 0.5 deg).
  (z, y) outline: the two side lines continue up to the **two lobes R1.8** centred (z -64.1606, y 14.8785) and
  (-56.6394, 14.8785), each tangent to its side line (tangent points (-65.8411, 15.5236) and (-54.9589, 15.5236));
  from the top of each lobe a straight **V-flank** runs down at 30 deg from vertical, from (-62.6018, 15.7787) to
  (-61.8042, 14.3973) and from (-58.1982, 15.7787) to (-58.9958, 14.3973); the flanks open into the **cable bore**
  (diameter 5.588 at y = 12, lowest point y = 9.188), which goes through the tab along X.
- **Two side windows**, x from -4.5 to 4.5 (side walls drafted 0.5 deg so the window widens upward), one in each
  inclined side: for the +Z side, the cut (z, y) outline is (-52.3601, 1.5), (-50.3601, 1.5), then a steep line
  leaning outward (direction (dz, dy) = (0.0976, 0.9952)) up through the side face, and the line parallel to the side
  face through (-52.3601, 1.5) up into the cradle (it meets the cradle at y = 5.803); everything outward of that
  parallel line and above y = 1.5 is removed, except the thin lip outside the steep line. The -Z window is the mirror
  image about z = -60.4.

### P05 Cable end fitting, handle side (one solid, 13 faces)

- Body of revolution about the pull axis (y = 12, z = -60.4), (r, x): rod **R2.794 (diameter 5.588)** from x = -57.4
  to x = -42.414; flat shoulder at x = -42.414 out to R3.556; **cone** from R3.556 at x = -42.414 to R1.778 at
  x = -40.8265; flat step at x = -40.8265 down to the **inner wire R1.016 (diameter 2.032)**, which runs into the
  barrel.
- **Cross barrel:** cylinder **diameter 6.35** along Z, axis x = -29.714, y = 12, from z = -64.36875 to z = -56.43125
  (7.9375 long), flat ends.

### P06 Sheath ferrule (2 identical bodies, 6 faces each)

Tube along X, **outside diameter 7.112, bore 5.588**, from x = -57.4 to x = -44.7 (12.7 long), flat ends.
**P06-a** on the axis y = 12, z = -60.4; **P06-b** on the axis y = 12, z = 15.8.

### P07 Cable end fitting, latch side (one solid, 12 faces)

Body of revolution about the line y = 12, z = 15.8 (parallel to X), (r, x): rod R2.794 from x = -57.4 to x = -42.414;
shoulder out to **R3.556**; cylinder R3.556 to x = -39.366; 45 deg cone down to R2.794 at x = -38.604; flat step down to
the **wire R1.016**; wire to its **flat end x = -28.952**.

### P08 Cable (one solid, 8 faces)

Solid round bar **diameter 6.35 (R3.175)** swept along a planar path in the plane y = 12, made of exactly three
segments (straight / circular, tangent):
1. straight leg on the line z = -60.4 from **x = -57.4** (flat end face) to x = -454.7527;
2. a **180 deg arc, centre-line radius 38.1**, centre (x -454.7527, y 12, z -22.3), bulging toward -X (outermost
   centre-line point x = -492.8527);
3. straight leg on the line z = 15.8 from x = -454.7527 back to **x = -57.4** (flat end face).
Each leg is 397.3527 long; the centre-line length is 914.40 (36.0 in). The legs are 76.2 apart.

### P09 Latch base plate (one solid, 58 faces)

- **Plate** y from **1.01 to 2.6** (1.59 thick), (x, z) outline: start (-20.257, 54.3); arc c=(-22.757, 54.3) R2.5 to
  (-22.757, 56.8); line to (-30.757, 56.8); arc c=(-30.757, 54.3) R2.5 to (-33.257, 54.3); line to (-33.257, 39.8); arc
  c=(-38.257, 39.8) R5 to (-38.257, 34.8); line to (-41.257, 34.8); arc c=(-41.257, 39.8) R5 to (-46.257, 39.8)
  [this is the **mouth slot**, 13 wide, open toward +Z]; line to (-46.257, 54.3); arc c=(-48.757, 54.3) R2.5 to
  (-48.757, 56.8); line to (-56.757, 56.8); arc c=(-56.757, 54.3) R2.5 to (-59.257, 54.3); line to (-59.257, 31.3);
  line to (-11.757, 31.3); semicircular notch arc c=(-10.257, 31.3) R1.5 (toward +Z) to (-8.757, 31.3); arc
  c=(-6.257, 31.3) R2.5 to (-6.257, 28.8); line to (6.743, 28.8); arc c=(6.743, 31.3) R2.5 to (9.243, 31.3); line to
  (9.243, 50.3); arc c=(6.743, 50.3) R2.5 to (6.743, 52.8); line to (-6.757, 52.8); line to (-6.757, 54.3) [on the top
  face 54.8, see flange 2]; line to (-16.257, 54.3); semicircular notch arc c=(-18.257, 54.3) R2 (toward -Z) to
  (-20.257, 54.3).
- **Bent flange 1** (along the edge z = 31.3, x from -59.257 to -11.757): 2.0 thick (z 28.8 to 30.8), up to
  **y = 12.1**. (z, y) section: outer bend arc c=(31.3, 3.51) R2.5 from (31.3, 1.01) to (28.8, 3.51); outer face
  z = 28.8 to y = 12.1; top y = 12.1; inner face z = 30.8 down to y = 3.1; inner bend arc c=(31.3, 3.1) R0.5 to
  (31.3, 2.6).
- **Bent flange 2** (x from -16.257 to -6.757): 2.0 thick (z 54.8 to 56.8), up to **y = 10.6**. Section: outer bend
  arc c=(54.3, 3.51) R2.5 from (54.3, 1.01) to (56.8, 3.51); outer face z = 56.8 up to y = 10.6; inner face z = 54.8
  down to the plate top y = 2.6 (sharp inner corner).
- **Curved lip** on top of flange 2: y from **8.6 to 10.6**, between the arcs **R35.5 and R37.5 about
  (x -16.257, z 19.3)** (continuing the flange faces z = 54.8 / 56.8 at x = -16.257), running toward -X to the straight
  end line from (-27.6208, 52.932) to (-28.3144, 54.8087); the end is a full round **R1** across the 2 thickness
  (half cylinder about the line through (-27.6257, 9.6, 52.9453) with direction (-0.3467, 0, 0.9380)).
- **Embossed pad** y from 2.6 to **4.0**: stadium outline R7.5 about the two pivot axes (x, z) = (0.243, 39.8) and
  (-22.257, 43.3) (two semicircles joined by tangent lines), vertical walls. Under it, a **recess** in the underside:
  stadium R6.5 about the same centres at the underside y = 1.01, floor **y = 2.0**; its wall is a convex quarter round
  R1 whose centre line lies 6.5 from the centre line of the stadium at y = 2.01 (the recess is 5.5 wide from the centre
  line at the floor).
- **Holes:** two holes **diameter 9.1 (R4.55)** on the pivot axes (through pad and recess floor); **stop pin hole
  diameter 4.0** at (x -55.757, z 42.55) with a 45 deg countersink on the top face (diameter 5.2 at y = 2.6).

### P10 Latch cover plate (one solid, 47 faces)

- **Plate** y from **12.9 to 14.9** (2 thick), (x, z) outline: start (9.243, 53.3); line to (9.243, 31.3); arc
  c=(6.743, 31.3) R2.5 to (6.743, 28.8); line to (-59.257, 28.8); line to (-59.257, 54.3); arc c=(-56.757, 54.3) R2.5
  to (-56.757, 56.8); line to (-48.257, 56.8); line to (-48.257, 43.3); arc c=(-43.257, 43.3) R5 to (-43.257, 38.3);
  line to (-36.257, 38.3); arc c=(-36.257, 43.3) R5 to (-31.257, 43.3) [**mouth slot** 17 wide, open toward +Z]; line
  to (-31.257, 54.3); arc c=(-28.757, 54.3) R2.5 to (-28.757, 56.8); line to (-10.557, 56.8); line to (-10.557, 51.8);
  semicircular notch arc c=(-8.557, 51.8) R2 (toward -Z) to (-6.557, 51.8); line to (-6.557, 53.3); close.
- **Holes:** two holes **diameter 9.1 (R4.55)** on the pivot axes (0.243, 39.8) and (-22.257, 43.3); the **stop pin
  hole** at (-55.757, 42.55) is conical: radius 2.6 at y = 12.9 to radius 2.0641 at y = 14.9 (half-angle 15 deg).
- **Joggle** (x from -59.257 to -44.557) from the edge z = 28.8 to an **offset tab y 17.41 to 19.41**. (z, y)
  section: top face y = 14.9 to z = 28.8; arc c=(28.8, 16.3166) R1.4166 to (27.3909, 16.171); arc c=(23.8, 15.8) R3.61
  to (23.8, 19.41); tab top y = 19.41 to the tab end z = 8.8; tab underside y = 17.41 back to z = 23.8; arc
  c=(23.8, 15.8) R1.61 to (25.4015, 15.9655); arc c=(28.8, 16.3166) R3.4166 to (28.8, 12.9). The tab (x, z) outline is
  x from -59.257 to -44.557, z from 8.8 to 23.8, with the corner (-59.257, 8.8) rounded **R2.5** (centre
  (-56.757, 11.3)).
- **Bent leg** under the tab, x from **-44.557 to -42.557** (2 thick), from the tab down to **y = 5.41**, z from 8.8 to
  22.8. Its outer bend is a quarter cylinder **R2** about the line (x -44.557, y 17.41, parallel to Z) joining the tab
  top y = 19.41 to the leg face x = -42.557 (sharp inner corner). (z, y) outline of the leg: (8.8, 17.41); down to
  (8.8, 6.41); arc c=(9.8, 6.41) R1 to (9.8, 5.41); line to (13.0345, 5.41); line to (13.7, 10.467); arc
  c=(15.8, 12) R2.6 through (15.8, 14.6) to (17.9, 10.467) [the **cable guide hole R2.6** about the line y = 12,
  z = 15.8, open downward through a tapered slot]; line to (18.5655, 5.41); line to (21.8, 5.41); arc c=(21.8, 6.41) R1
  to (22.8, 6.41); line to (22.8, 17.41).

### P11 Rotor (one solid, 23 faces)

Flat plate **y from 4.4 to 8.4** (4 thick), (x, z) outline: start (-16.257, 33.3); line to (-42.609, 33.3); arc
c=(-42.609, 34.8) R1.5 to (-44.0981, 34.98); arc c=(-40.127, 34.5) R4 to (-40.127, 38.5); line to (-37.857, 38.5);
arc c=(-37.857, 43.3) **R4.8** (toward +X, the **jaw** for the strike bolt) to (-37.857, 48.1); line to (-43.077, 48.1);
arc c=(-43.077, 51.1) R3 to (-45.1984, 53.2213); line to (-42.059, 56.3607); arc c=(-40.9984, 55.3) R1.5 to
(-40.9984, 56.8); line to (-32.9761, 56.8); arc c=(-32.9761, 55.8) R1 to (-32.4026, 56.6192); line to
(-27.9206, 53.4808); arc c=(-27.347, 54.3) R1 (concave) to (-27.347, 53.3); line to (-17.7849, 53.3); arc
c=(-17.7849, 47.3) R6 to (-13.3128, 51.3); arc c=(-22.257, 43.3) R12 to (-15.057, 33.7); arc c=(-16.257, 35.3) R2 to
(-16.257, 33.3). **Pivot hole diameter 10.8** at (-22.257, 43.3).

### P12 Release lever (one solid, 15 faces)

Flat plate **y from 4.3937 to 8.3937** (4 thick), (x, z) outline: start (2.143, 30.2151); line to (-8.934, 13.5341);
arc c=(-13.0993, 16.3) R5 around the -Z side to (-17.5309, 18.6154); line to (-8.6721, 35.5708); arc c=(-9.5584,
36.0339) R1 (concave) to (-8.6249, 36.3926); arc c=(0.243, 39.8) **R9.5** around the +Z side to (2.7158, 30.6275);
arc c=(2.976, 29.6619) R1 (concave) to (2.143, 30.2151). Holes: **diameter 10.8** at (0.243, 39.8) and **diameter
6.4** at (-13.0993, 16.3) (27.023 apart).

### P13 Pivot spacer (2 identical bodies, 30 faces each)

Body of revolution about a Y-parallel axis, bore **diameter 7.2 (R3.6)** through, (r, y) outline: R5.45 from y = 1.1
to 2.1; R4.45 to 4.1; R5.25 to 8.4; **R6.35 (diameter 12.7)** to 12.9; R4.45 to 14.9; R5.45 to the top y = 15.9. The
top collar (y 14.9 to 15.9) is cut by a **slot 2.2 wide** across its full diameter, slot walls parallel to the YZ
plane (x = axis +- 1.1), slot floor y = 14.9. **P13-a** axis (x 0.243, z 39.8) (lever pivot); **P13-b** axis
(x -22.257, z 43.3) (rotor pivot); same orientation.

### P14 Stop pin (one solid, 10 faces)

Body of revolution about the line x = -55.757, z = 42.55 (parallel to Y): R1.85 from y = 0.1 to 2.65; **R2.5** from
2.65 to 12.75; R1.85 from 12.75 to 15.3. Flat ends.

### P15 Cable clevis block (one solid, 13 faces)

- **Base** y from **8.9 to 10.0** (1.1 thick), (x, z) outline: (-22.7993, 11.3); line to (-15.3906, 11.3); arc
  c=(-13.0993, 16.3) **R5.5** around the +X side to (-16.2616, 20.8); line to (-22.7993, 20.8); close. Hole
  **diameter 5.2705** at (-13.0993, 16.3).
- **Upright block** x from -22.7993 to -17.2993 (5.5 long), (z, y) outline: (11.3, 8.9); (15.8, 8.9); (15.8, 10.0);
  (19.8311, 10.0); arc c=(15.8, 12) **R4.5** over the top to (11.3, 12); close. **Cross hole diameter 4.0** along X
  about the line y = 12, z = 15.8.

### P16 Cable end L-pin (one solid, 15 faces)

- **Pin**, body of revolution about the line x = -13.0993, z = 16.3 (parallel to Y), (r, y): R3.0 at the bottom
  y = 0.11 widening (half-angle 5 deg) to **R3.375 at y = 4.4**; shoulder; **R2.95** from 4.4 to 8.9; shoulder;
  **R2.63525** from 8.9 to the top y = 10.0.
- **Rod diameter 3.81 (R1.905)** in the plane z = 15.8 (offset 0.5 from the pin axis): starts vertical on the line
  x = -13.0993 inside the pin, bends **90 deg with centre-line radius 3.175** about the centre (x -16.2743, y 8.825)
  to horizontal at y = 12, then runs straight along -X on the line y = 12, z = 15.8 to its **flat end x = -28.952**.

### H1 Strike bolt (one solid, 58 faces)

On the axis x = -37.857, z = 75.7 (parallel to Y):
- **Hex head** y from **20.6612 to 23.4512** (2.79 high), **12.7 across flats**, two flats normal to Z
  (z = 69.35 and 82.05), corners on the X direction. Both head ends are chamfered by a cone of half-angle 75 deg whose
  radius is 6.35 on the end face (the chamfer only cuts the corners).
- **Shank diameter 9.45 (R4.725)** from the head down to the flange dome (y = -1.9488 at the shank).
- **Dished washer flange diameter 25.4 (R12.7)**, 0.762 thick: top surface a sphere **R79.883** centred on the axis
  at y = -81.705, underside a sphere R79.883 centred at y = -82.467 (both convex upward), rim cylinder R12.7 from
  y = -3.6 to -2.838.
- **Thread M8 x 1.25, right-hand, modelled**: crest cylinder **R4.0**, root **R3.1881**, depth 0.8119 (3/4 of the
  fundamental triangle height), **60 deg profile** (flanks 30 deg to the radial plane), crest flat and root flat each
  0.15625 (P/8) wide. Phase: in the half-plane toward +X (z = 75.7, x > axis) the crest flat centres are at
  **y = -11.759 + 1.25 n** and the root flat centres at y = -11.133 + 1.25 n; turning from +X toward -Z the thread
  rises by P/4 per 90 deg (right-hand). Extent: from the end chamfer up to the flange underside, where the groove runs
  out into a cone of half-angle 35 deg (radius 4.0 at y = -2.6842, narrowing downward).
- **End:** 45 deg chamfer from R4.0 at y = -13.7113 to R3.0625 on the **flat end y = -14.6488**.

### H2 Wire ring (one solid, 4 faces)

Torus, axis parallel to Y, centre **(x -39.757, y -3.2116, z 75.7)** (1.9 off the bolt axis toward -X), **ring radius
4.5, wire radius 0.5** (outside diameter 10, inside diameter 8).

## 5. Assembly

All twenty bodies are built in place with identity placement.
- **Handle unit:** the housing (P01) stands on y = 0; the anchor block (P04) sits in the V-notch under the housing tube
  (bottom on y = 0, cradle 0.15 below the tube); the pull rod (P03) collar is in the R6 bore; the rod tip enters the
  T-handle shank. **The pull rod overlaps the T-handle shank by 228.6 mm3** (the handle has no hole for it except the
  short void A at the tip); keep this overlap. The end fitting P05 barrel sits in the clevis cross hole (same diameter
  6.35, face contact); its rod passes the anchor tab bore and fills the ferrule P06-a bore; the cable P08 end face
  meets the ferrule end face x = -57.4.
- **Latch unit:** base plate (y 1.01 to 2.6), rotor (y 4.4 to 8.4) on spacer P13-b, lever (y 4.3937 to 8.3937) on
  spacer P13-a, clevis block on top of the lever pin (P16), cover plate (y 12.9 to 14.9). The spacers pass through the
  R4.55 holes of both plates (their flanges R5.45 overlap the plates by 2.83 mm3 each: the original rivet heads are
  pressed into the plates). The latch-side fitting P07 wire end touches the L-pin rod end at x = -28.952; P07 overlaps
  the cover joggle by 4.7 mm3. The strike bolt H1 overlaps the wire ring H2 by 7.1 mm3.
- **Body pairs overlapping by more than 8 mm3: only P03 / P02 (228.6 mm3).** All other contacts are face contacts or
  overlaps below 8 mm3 (listed above).

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body
(P02 T-handle 3 percent, H1 thread 1 percent), centre of mass within 0.1, bounding box within 0.05 (P02 0.2). The
faces column is information only. Volumes in cm3 = mm3 / 1000, areas in cm2 = mm2 / 100.

| ID | Name | Vol cm3 | Vol mm3 | Area cm2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Handle housing | 17.07753 | 17077.53 | 132.4785 | 13247.85 | 4.0288 | 7.5013 | -60.4000 | -22.5000 | 50.5000 | -0.0000 | 20.7500 | -88.4000 | -32.4000 | 41 |
| P02 | T-handle | 14.71066 | 14710.66 | 70.2557 | 7025.57 | 64.2490 | 12.0000 | -60.4000 | 38.5000 | 75.5000 | 1.0000 | 23.0000 | -90.4000 | -30.4000 | 591 |
| P03 | Pull rod | 4.43528 | 4435.28 | 25.4190 | 2541.90 | -1.1213 | 11.9757 | -60.4069 | -35.5966 | 50.2860 | 6.1000 | 17.9000 | -66.3000 | -54.5000 | 37 |
| P04 | Cable anchor block | 6.86351 | 6863.51 | 46.8647 | 4686.47 | -12.7406 | 2.8028 | -60.4000 | -44.5001 | 22.4998 | -0.0000 | 16.6993 | -71.8043 | -48.9956 | 27 |
| P05 | Cable end fitting, handle side | 0.68156 | 681.56 | 6.1904 | 619.04 | -41.5252 | 12.0000 | -60.4000 | -57.4000 | -26.5390 | 8.4440 | 15.5560 | -64.3688 | -56.4312 | 13 |
| P06-a | Sheath ferrule, handle side | 0.19306 | 193.06 | 5.3711 | 537.11 | -51.0500 | 12.0000 | -60.4000 | -57.4000 | -44.7000 | 8.4440 | 15.5560 | -63.9560 | -56.8440 | 6 |
| P06-b | Sheath ferrule, latch side | 0.19306 | 193.06 | 5.3711 | 537.11 | -51.0500 | 12.0000 | 15.8000 | -57.4000 | -44.7000 | 8.4440 | 15.5560 | 12.2440 | 19.3560 | 6 |
| P07 | Cable end fitting, latch side | 0.54416 | 544.16 | 4.7855 | 478.55 | -46.4875 | 12.0000 | 15.8000 | -57.4000 | -28.9520 | 8.4440 | 15.5560 | 12.2440 | 19.3560 | 12 |
| P08 | Cable, U-shaped | 28.95833 | 28958.33 | 183.0481 | 18304.81 | -285.2635 | 12.0000 | -22.3000 | -496.0277 | -57.4000 | 8.8250 | 15.1750 | -63.5750 | 18.9750 | 8 |
| P09 | Latch base plate | 3.56669 | 3566.69 | 46.3324 | 4633.24 | -25.3877 | 3.7774 | 39.5809 | -59.2570 | 9.2430 | 1.0100 | 12.1000 | 28.8000 | 56.8000 | 58 |
| P10 | Latch cover plate | 3.71172 | 3711.72 | 44.8383 | 4483.83 | -30.5172 | 14.4904 | 35.3152 | -59.2570 | 9.2430 | 5.4100 | 19.4100 | 8.8000 | 56.8000 | 47 |
| P11 | Rotor (claw) | 2.02684 | 2026.84 | 16.3091 | 1630.91 | -27.8199 | 6.4000 | 44.5056 | -46.0770 | -10.2570 | 4.4000 | 8.4000 | 33.3000 | 56.8000 | 23 |
| P12 | Release lever | 1.59525 | 1595.25 | 14.2040 | 1420.40 | -4.3744 | 6.3937 | 31.4659 | -18.0993 | 9.7430 | 4.3937 | 8.3937 | 11.3000 | 49.3000 | 15 |
| P13-a | Pivot spacer, lever | 0.76705 | 767.05 | 11.2267 | 1122.67 | 0.2430 | 8.9316 | 39.8000 | -6.1070 | 6.5930 | 1.1000 | 15.9000 | 33.4500 | 46.1500 | 30 |
| P13-b | Pivot spacer, rotor | 0.76705 | 767.05 | 11.2267 | 1122.67 | -22.2570 | 8.9316 | 43.3000 | -28.6070 | -15.9070 | 1.1000 | 15.9000 | 36.9500 | 49.6500 | 30 |
| P14 | Stop pin | 0.25315 | 253.15 | 2.5720 | 257.20 | -55.7570 | 7.7000 | 42.5500 | -58.2570 | -53.2570 | 0.1000 | 15.3000 | 40.0500 | 45.0500 | 10 |
| P15 | Cable clevis block | 0.33600 | 336.00 | 5.0708 | 507.08 | -18.4121 | 11.6991 | 15.9218 | -22.7993 | -7.5993 | 8.9000 | 16.5000 | 10.8000 | 21.8000 | 13 |
| P16 | Cable end L-pin | 0.47160 | 471.60 | 4.4704 | 447.04 | -16.1289 | 7.6253 | 16.1012 | -28.9520 | -9.7243 | 0.1100 | 13.9050 | 12.9250 | 19.6750 | 15 |
| H1 | Strike bolt M8x1.25 | 2.84702 | 2847.02 | 24.4815 | 2448.15 | -37.8578 | 6.3750 | 75.6999 | -50.5570 | -25.1570 | -14.6488 | 23.4512 | 63.0000 | 88.4000 | 58 |
| H2 | Wire ring | 0.02221 | 22.21 | 0.8883 | 88.83 | -39.7570 | -3.2116 | 75.7000 | -44.7570 | -34.7570 | -3.7116 | -2.7116 | 70.7000 | 80.7000 | 4 |

**Whole assembly:** 20 bodies; total volume 90021.71 mm3; total area 66140.42 mm2; centre of mass (-87.0144, 9.7256,
-28.5722); bounding box X [-496.0277, 75.5], Y [-14.6488, 23.4512], Z [-90.4, 88.4].

**Key functional checks:** cable diameter 6.35 (1/4 in), bend radius 38.1 (1.5 in), legs 76.2 apart, centre-line
length 914.4 (3 ft); T-handle 60 long and 22 thick; handle plate 45 x 56 with four diameter 4.5 holes 25 x 40 apart;
latch width 68.5, latch height (cover) 48.0, latch depth (L-pin bottom to cover tab top) 19.30; strike bolt 38.1 long,
M8 x 1.25, 25.40 from the flange dome to the head top; rotor pivot 15.6 from the strike bolt axis along X; pivot
spacing 22.5 along X.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| T-handle thickness | 0.86 in (drawing); handle width 7/8 in (product data) | 22.0 (0.866 in) | Follow the 3D. |
| Handle plate | 2 3/16 x 1 3/4 in, holes 3/16 in at 1 in and 1 9/16 in (product data) | 56 x 45, holes 4.5 at 25 and 40 | Follow the 3D. |
| Latch size | 2 11/16 x 1 7/8 x 3/4 in (product data) | 68.5 x 48.0 x 19.30 | Agree within rounding. |
| Strike bolt | diameter 3/8 in, length 1 1/2 in, projection 1 in, M8 x 1.25 | shank 9.45, length 38.1, 25.40, M8 x 1.25 modelled | Follow the 3D. |
| Latching distance | 0.61 in (drawing), 5/8 in (product data) | 15.6 (0.614 in) | Follow the 3D. |
| Mounting hole of the latch | 9/32 in at 7/8 in (product data) | pivot holes 9.1 at 22.77 (centre distance) | Not the same feature; follow the 3D. |

**Undetermined:** the T-handle's free-form blends (edge rounds R0.3 to R3, given as measured median radii), the exact
recess floor and recess wall surfaces (given as the x = 69 section, 2 deg draft and floor offset), the two flattened
panels on its +X face; the free-form upper -Z quarter of the pull rod clevis end; the exact run-out of the strike bolt
thread groove under the flange; springs and any internal detail of the cable (not modelled in the source).
