# Design specification: heavy-duty formed steel shelf bracket, side mount (P22)

A one-piece bracket bent from flat steel sheet: a flat triangular **web** (the gusset) with two flanges bent 90 deg
toward the same side of it. One flange (the **wall flange**) is screwed to the wall, the other (the **top flange**)
carries the shelf. Each flange has four round screw holes. This document is the only source for the rebuild. Every
value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (1 in = 25.4 mm; the master is checked in mm.)
- **Global frame (use exactly, no realignment):**
  - **X** = depth of the bracket, from the wall (X = -6) to the free end of the shelf arm (X = +6).
  - **Y** = height. The top flange is at the top (outer face Y = +4.1196); the wall flange runs down to Y = -3.8804.
  - **Z** = width of the flanges. The web lies at the **-Z** side (Z = -0.75 to -0.6304); both flanges stand up from it
    toward **+Z** and end at Z = +0.75.
  - Outer envelope: X -6 .. +6, Y -3.8804 .. +4.1196, Z -0.75 .. +0.75 (12 x 8 x 1.5).
- One body, one solid. Name: **P01 Bracket**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Formed bracket (web, two bends, two flanges, one solid) | custom |

## 3. Sheet data

| Item | Value |
|---|---|
| Sheet thickness t | **0.1196** (11 gauge; measured 3.0378 mm) |
| Inside bend radius (both bends) | **0.1196** (= t) |
| Outside bend radius (both bends) | **0.2392** (= 2 t) |
| Bend angle (both bends) | 90 |
| Number of bends | 2 (bend axes are parallel to X and to Y; they do not meet, see the corner relief F7) |

The part is described in its **formed** state. The flat blank is not part of the deliverable; the bend allowance /
K-factor of the master cannot be measured from the formed geometry (undetermined), so do not derive positions from an
unfolded layout: use the formed coordinates below.

## 4. Geometry of P01 (build in this order)

All coordinates are global (inch). "Plan view" = looking along Z, coordinates (x, y).

**F1. Web (flat gusset plate).** A plate between the planes **Z = -0.75** (outer face) and **Z = -0.6304** (inner face,
the side the flanges rise from), thickness 0.1196. Its plan profile is the closed loop below (all arcs are tangent to
their neighbouring lines; "cw / ccw" as seen from +Z):

| Seg | From (x, y) | To (x, y) | Type |
|---|---|---|---|
| W1 | (-5.760800, -3.880400) | (-5.250000, -3.523693) | arc R **0.544083**, centre (-5.760800, -3.336317), ccw |
| W2 | (-5.250000, -3.523693) | (-3.812500, 0.395043) | straight line |
| W3 | (-3.812500, 0.395043) | (-2.000000, 1.932100) | arc R **2.408851**, centre (-1.551004, -0.434536), cw (a concave edge: the centre lies outside the web) |
| W4 | (-2.000000, 1.932100) | (5.576997, 3.369600) | straight line |
| W5 | (5.576997, 3.369600) | (6.000000, 3.880400) | arc R **0.519911**, centre (5.480089, 3.880400), ccw |
| W6 | (6.000000, 3.880400) | (-5.760800, 3.880400) | straight line (tangent line of the top bend, Y = 3.8804) |
| W7 | (-5.760800, 3.880400) | (-5.760800, -3.880400) | straight line (tangent line of the wall bend, X = -5.7608) |

Notes: W1 starts at the bottom of the part (Y = -3.8804) on the wall-bend tangent line and leaves it tangentially
(its centre lies on X = -5.7608). W2 rises at **20.144 deg** from the Y axis (its outward normal is (-0.93883, 0.34436)).
W4 rises at **10.742 deg** from the X axis (outward normal (-0.18644, 0.98247)). W5 ends tangent to the end plane X = 6.
W6 and W7 are not free edges: there the web continues into the two bends (F2, F4). The top-left corner of this loop
is later cut by the corner relief F7.

**F2. Top bend (axis parallel to X).** A 90 deg cylindrical bend joining the web to the top flange along the whole
edge W6. Bend axis: the line **Y = 3.8804, Z = -0.5108**, parallel to X. Inside surface radius 0.1196 (from the web
inner face Z = -0.6304 to the flange inner face Y = 4.0), outside surface radius 0.2392 (from Z = -0.75 to
Y = 4.1196). Build it over X = -6 .. +6 (the part at X < -5.25 is removed by F7).

**F3. Top flange.** A plate between **Y = 4.0** (inner face) and **Y = 4.1196** (outer face, the shelf seat), from the
bend tangent Z = -0.5108 up to the free edge **Z = +0.75**, over **X = -6 .. +6** (after F7 it spans X = -5.25 .. +6,
length 11.25). The free end X = +6 is flush with the web end (W5 ends on X = 6 too).
- **Free-end corner round:** the corner at X = +6, Z = +0.75 is rounded with **R 0.25** through the thickness (a
  cylinder parallel to Y, axis X = 5.75, Z = 0.5). The corner at X = 6 next to the bend stays sharp.

**F4. Wall bend (axis parallel to Y).** A 90 deg cylindrical bend joining the web to the wall flange along the whole
edge W7. Bend axis: the line **X = -5.7608, Z = -0.5108**, parallel to Y. Inside radius 0.1196 (from Z = -0.6304 to the
flange inner face X = -5.8804), outside radius 0.2392 (from Z = -0.75 to X = -6.0). Build it over
Y = -3.8804 .. +4.1196 (the part at Y > 3.3696 is removed by F7).

**F5. Wall flange.** A plate between **X = -6.0** (outer face, against the wall) and **X = -5.8804** (inner face),
from the bend tangent Z = -0.5108 up to the free edge **Z = +0.75**, over **Y = -3.8804 .. +4.1196** (after F7 it spans
Y = -3.8804 .. +3.3696, length 7.25). Its bottom end Y = -3.8804 is flush with the bottom of the bend and the web.
- **Free-end corner round:** the corner at Y = -3.8804, Z = +0.75 is rounded with **R 0.25** through the thickness (a
  cylinder parallel to X, axis Y = -3.6304, Z = 0.5). The corner at the top end (Y = 3.3696) stays sharp.

**F6. Union.** F1 to F5 form one solid. In the top-left corner the two bends and flanges overlap; that region is
removed completely in F7.

**F7. Corner relief (through cut along Z).** Remove everything inside the following plan-view region, through the full
Z range (it cuts the web, both bends and both flanges):

| Seg | From (x, y) | To (x, y) | Type |
|---|---|---|---|
| R1 | (-6.5, 3.369600) | (-5.812577, 3.369600) | straight line on Y = 3.3696 |
| R2 | (-5.812577, 3.369600) | (-5.724188, 3.406212) | arc R **0.125**, centre (-5.812577, 3.494600), ccw, from -90 deg to -45 deg about its centre |
| R3 | (-5.724188, 3.406212) | (-5.286612, 3.843788) | straight line at **45 deg** |
| R4 | (-5.286612, 3.843788) | (-5.250000, 3.932177) | arc R **0.125**, centre (-5.375000, 3.932177), ccw, from -45 deg to 0 deg |
| R5 | (-5.250000, 3.932177) | (-5.25, 4.5) | straight line on X = -5.25 |
| R6 | (-5.25, 4.5) -> (-6.5, 4.5) -> (-6.5, 3.3696) | | closing lines outside the part |

So the wall flange (and its bend) ends at **Y = 3.3696**, the top flange (and its bend) ends at **X = -5.25**, and the
web corner between them is a 45 deg edge with two R 0.125 rounds, each tangent to the end line it meets (R2 tangent to
Y = 3.3696 at x = -5.812577; R4 tangent to X = -5.25 at y = 3.932177). The arcs cut slightly into the bend zones: the
R4 cylinder crosses the top bend between Y = 3.8804 and 3.9322, the R2 cylinder crosses the wall bend between
X = -5.8126 and -5.7608. All other corner edges are sharp.

**F8. Wall-flange holes, 4x.** Round through holes **diameter 0.25** along X through the wall flange (X = -6 to
-5.8804), at (y, z):

| Hole | y | z |
|---|---|---|
| W-1 | -3.1304 | +0.25 |
| W-2 | -1.1304 | -0.25 |
| W-3 | +0.8696 | +0.25 |
| W-4 | +2.8696 | -0.25 |

Pitch 2.0 in Y, staggered +-0.25 about the flange mid-line Z = 0. W-1 is 0.75 above the flange bottom end; W-4 is 0.5
below the flange top end.

**F9. Top-flange holes, 4x.** Round through holes **diameter 0.25** along Y through the top flange (Y = 4.0 to 4.1196),
at (x, z):

| Hole | x | z |
|---|---|---|
| T-1 | +4.5 | +0.25 |
| T-2 | +1.5 | -0.25 |
| T-3 | -1.5 | +0.25 |
| T-4 | -4.5 | -0.25 |

Pitch 3.0 in X, staggered +-0.25 about Z = 0, symmetric about X = 0. T-1 is 1.5 from the free end X = 6.

No embossed ribs, darts, gussets, countersinks, slots or other cut-outs exist. All edges not mentioned are sharp. No
paint layer is modelled.

## 5. Check points and values

- Web inner face Z = -0.6304 and outer face Z = -0.75: point (0, 3.1496) lies on the web in plan.
- Top bend inside surface point (0, 3.96497, -0.59537); outside (0, 4.04954, -0.67994).
- Wall bend inside surface point (-5.84537, 0, -0.59537); outside (-5.92994, 0, -0.67994).
- Flange free edges Z = 0.75 are 1.3804 from the web inner face.
- Wall flange: Y -3.8804 .. 3.3696 (7.25). Top flange: X -5.25 .. 6 (11.25).

## 6. Acceptance targets

| ID | Name | Volume in3 | Volume mm3 | Area in2 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Formed bracket | 6.41409 | 105108.06 | 112.9047 | 72841.57 | -2.2025 | 2.1714 | -0.3378 | -6.0000 | 6.0000 | -3.8804 | 4.1196 | -0.7500 | 0.7500 | 42 |

CoM and bounding box in inches. Volume tolerance +-0.05 %. The face count is for orientation only (the master splits
each hole into two half-cylinder faces); it is not a target.
