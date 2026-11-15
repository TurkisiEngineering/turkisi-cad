# Design specification: machine-tool chip shield on a flexible arm (P18)

A square clear shield on an arm: the shield is screwed to a moulded clamp, the clamp holds the near end of a straight
arm (the flexible arm is modelled straight) through a short hex-socket plug, and the far end of the arm butts against a
mounting base that takes two hex bolts with nuts. The master is **11 solids**. This document is the only source for the
rebuild. Every value was measured from the master 3D geometry.

## 1. Units and frames

- **Units: inches.** Angles in degrees. (1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):** the shield lies in the XY plane, centred on the origin, faces
  z = +-0.0625. Its sides are parallel to X and Y. The arm runs from the shield corner at (+X, -Y) diagonally outward.
- **Local frame (u, v, w)** used for everything on the arm line:
  u = (x - y) / sqrt 2, v = (x + y) / sqrt 2, w = z; inversely **x = (u + v) / sqrt 2, y = (v - u) / sqrt 2, z = w**.
  (+u points along the arm, away from the shield, i.e. along global (1, -1, 0)/sqrt 2; +v is global (1, 1, 0)/sqrt 2;
  u, v, w is right-handed.) The local origin is the global origin.
- **The arm axis** is the line v = 0, w = -0.3125.
- All bodies are modelled in place.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Shield (flat plate) | custom |
| P02 | 1 | Clamp (moulded block with arm socket) | custom |
| P03 | 1 | Hex-socket plug (plain pin in the clamp socket) | bought-in |
| P04 | 1 | Arm (straight tube with end collars) | custom |
| P05 | 1 | Mounting base | custom |
| H1-a, H1-b | 2 | Cross-recess screws holding the shield to the clamp (same part) | bought-in |
| H2-a, H2-b | 2 | Hex bolts 1/4-20 in the base (same part) | bought-in |
| H3-a, H3-b | 2 | Hex nuts 1/4-20 in the base (same part) | bought-in |

Instances: H1-a at local (u, v) = (4.44437, 0), H1-b at (3.81937, 0) (axes parallel to Z); H2-a and H3-a on the line
v = 0, w = 0.375, H2-b and H3-b on v = 0, w = -1.0 (axes parallel to u). Each b instance is its a instance translated
(H1: by -0.625 in u; H2, H3: by -1.375 in w), threads included.

## 3. P01 Shield

- Plate 8.0 x 8.0 (x and y from -4 to 4), thickness 0.125 (z from -0.0625 to 0.0625).
- Corners at (-X, -Y), (-X, +Y), (+X, +Y): radius 0.75 (centres at (+-3.25, +-3.25)).
- Corner at (+X, -Y): cut by a straight 45 deg flat on the line **u = 4.94437** (x - y = 6.99239); the flat meets the
  edges y = -4 and x = 4 with two R0.01 rounds centred (2.98823, -3.99) and (3.99, -2.98823).
- Two through holes diameter 0.15625 at global (3.14264, -3.14264) and (2.70071, -2.70071) (local u = 4.44437 and
  3.81937, v = 0); hole edges sharp.
- All outline edges on both faces rounded R0.005.
- Source artefact: the master shield carries 13 empty closed shells (78 faces of zero area) inside the solid; ignore
  them (no volume, no area).

## 4. P02 Clamp

All coordinates local (u, v, w).
- **Main block:** u from 3.12937 to 5.32937 (length 2.2), v from -0.525 to 0.525 (width 1.05), bottom face w = 0.06748
  (it stands 0.005 above the shield top), top = cylinder radius 0.75 about the arm axis (top line w = 0.4375).
  In a section u = const: bottom w = 0.06748, sides v = +-0.525, top arc R0.75 centred (v, w) = (0, -0.3125).
- **Socket:** for u from 4.94937 to 5.32937 the section continues downward: the sides v = +-0.525 run down to
  w = -0.3125 and close with a half cylinder radius 0.525 about the arm axis (lowest point w = -0.8375). Through bore
  diameter 0.3925 (r 0.19625) on the arm axis, from u = 4.94937 to 5.32937. The socket's front face is the plane
  u = 4.94937; the end face u = 5.32937 is shared by block and socket.
- **Two blind holes** diameter 0.15625 from the bottom face up to w = 0.3175 (depth 0.25), flat ends, at
  (u, v) = (3.81937, 0) and (4.44437, 0).
- **Rounds R0.03875** on: both top-arc end edges; the four vertical corner edges (axes at (u, v) = (3.16812 or 5.29062,
  +-0.48625)); the edges between sides and top arc; the bottom edges of the block (sides and the u = 3.12937 end); the
  socket's lower edges at both ends; spherical corners R0.03875 where three rounds meet.
- **Fillet R0.03875 (concave)** between the block bottom face w = 0.06748 and the socket front face u = 4.94937 (axis
  along v at u = 4.91062, w = 0.02874).

## 5. P03 Hex-socket plug

Cylinder diameter 0.375 on the arm axis from u = 4.94937 to 5.32937 (inside the clamp bore, clearance 0.00875 on the
radius). In its front end face u = 4.94937: a hex socket 0.1875 across flats (flats normal to w and +-60 deg from w;
corners on +-v), corners rounded R0.025, flat bottom at u = 5.07437 (depth 0.125), with a 60 deg (to the axis)
countersink from r 0.10439 at the face; outer edge of the front face rounded R0.01. Rear end u = 5.32937 sharp.

## 6. P04 Arm

Revolved about the arm axis; (u, r) profile, r = distance from the axis:
1. end face u = 5.32937, r 0 to 0.415, rounded R0.01 into
2. collar r 0.425 from u = 5.33937 to 6.2937
3. convex arc R0.05 centred (6.2937, 0.375) from (6.2937, 0.425) to (6.3389, 0.39644)
4. concave arc R0.125 centred (6.45181, 0.45) from (6.3389, 0.39644) to (6.45181, 0.325)
5. tube r 0.325 (diameter 0.65) to u = 16.02189
6. the far end mirrors steps 1-4 about u = 11.13687: concave R0.125 centred (16.02189, 0.45), convex R0.05 centred
   (16.18, 0.375), collar r 0.425 to u = 16.93437, R0.01 round, end face u = 16.94437.
Overall length 11.615. The arm is solid. Its near end face touches the clamp end face u = 5.32937; its far end face
touches the base front face u = 16.94437.

## 7. P05 Mounting base

A plate between the planes **u = 16.94437 (front) and u = 17.44437 (back)** (thickness 0.5). Outline in (v, w), closed:
- arc R0.2875 centred (0, 0.4) from (-0.28087, 0.46138) over the top to (0.28087, 0.46138);
- line to (0.415, -0.15236); arc R0.75 centred (-0.31772, -0.3125) through (0.43228, -0.3125) to (0.415, -0.47264);
- line to (0.28087, -1.08638); arc R0.2875 centred (0, -1.025) round the bottom to (-0.28087, -1.08638);
- line to (-0.415, -0.47264); arc R0.75 centred (0.31772, -0.3125) through (-0.43228, -0.3125) to (-0.415, -0.15236);
- line back to the start.

Cut-outs:
- **Mounting holes:** two through holes diameter 0.255 at (v, w) = (0, 0.375) and (0, -1.0) (1.375 apart), each with a
  round recess diameter 0.4325 from the front face to u = 17.13185 (depth 0.1875) and one from the back face to
  u = 17.31937 (depth 0.125); recess floors flat.
- **Four blind holes** diameter 0.2375 from the back face to u = 17.06937 (flat bottom) at (v, w) = (+-0.21, 0.08748)
  and (+-0.21, -0.71252).
- **Slot** on the -v side: width 0.3925 (w from -0.50874 to -0.11626), from the -v edge to a round end radius 0.19625
  centred (v, w) = (0, -0.3125), through the full thickness in u, except:
  - **front lip:** for u from 16.94437 to 16.99811 the slot does not break through the -v edge: material remains between
    the inner arc R0.715 and the outer arc R0.75, both centred (0.31772, -0.3125) (lip 0.035 thick in v); the lip's
    inner edge at u = 16.99811 is rounded R0.01;
  - **notch through the lip zone:** the region outside the R0.715 arc (v below about -0.371) is cut, from the back face
    forward, by a half cylinder radius 0.19625 with its axis along v at (u, w) = (17.19437, -0.3125), extended to the
    back face; it reaches the lip at u = 16.99811 (its front-most point). So, seen from -v, the slot mouth is a U opening
    toward the back face. Check section u = 17.0475: the lip remains at w outside -0.18260 .. -0.44240.
- **Rounds R0.01** on all edges of the outline, slot, notch and recesses on the front and back faces. The edges of the
  through holes and blind holes are sharp.

## 8. Hardware

**H1 screws (2):** axis parallel to Z at the shield holes. Head under the shield: cylinder r 0.15626 from z = -0.1475 to
-0.0625 (underside of head on the shield bottom face), bottom face z = -0.1875 (r up to 0.11625) joined to the cylinder
by a R0.04 round. Cross recess in the bottom face: four arms along global +-X and +-Y; at the face each arm is 0.0401
wide and reaches 0.0958 from the axis; arm walls and ends are inclined 5 deg toward the axis; a central 5 deg cone
from r 0.05 at the face to r 0.04126 at the flat recess floor z = -0.0875. Shank: **modelled thread, 48 threads per
inch** (pitch 0.020833), right hand, 60 deg, major diameter 0.156 (r 0.078), minor r 0.06673, crest flat 0.0026 on the
major radius, root flat 0.00521 on the minor radius; thread from the head up to z = 0.2925, then a 45 deg chamfer to a
flat end r 0.053 at **z = 0.3175**. **Phase:** in the half plane from the screw axis toward local +u, crest flats are
centred at z = 0.00023 + k (0.020833); toward local +v at z = 0.00023 + P/4 + k P.

**H2 bolts (2):** axis parallel to u. Hex head 0.375 across flats (flats normal to w and +-60 deg from w; corners on
+-v), corners rounded R0.05 (corner-round axes 0.15878 from the bolt axis), from u = 17.31937 to 17.44437 (head height
0.125, outer face flush with the base back face), with a 30 deg chamfer at the outer face (cone at 60 deg to the axis
through r 0.1875 at u = 17.44437). Shank **1/4-20 thread modelled**, right hand, pitch 0.05: major r 0.125, minor
r 0.09794, crest flat 0.00625, root flat 0.0125; from the tip u = 16.61937 (45 deg chamfer from r 0.09 at the tip) to
the head; under the head the groove runs out against a 15 deg cone (half angle) of radius 0.125 at u = 17.31937
(radius 0.11484 at u = 17.28146). **Phase:** in the half plane toward +w from the bolt axis, crest flats centred at
u = 16.97248 + 0.05k; toward +v at u = 16.97248 - 0.0125 + 0.05k.

**H3 nuts (2):** 1/4-20, 0.375 across flats (same hex orientation as the bolt heads), corners rounded R0.05, from
u = 17.00685 to 17.13185 (thickness 0.125, seated on the floor of the front recess); 30 deg chamfers on both faces
(cone through r 0.1875 at each face); 45 deg countersinks on both faces from r 0.1275. Internal thread modelled,
matching the bolt: root (major) flats r 0.125 centred at u = 17.02248 + 0.05k in the half plane toward +w (they
coincide with the bolt crest flats), minor r 0.09794.

## 9. Acceptance targets (inches)

| ID | Volume in3 | Area in2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 7.88615 | 129.9811 | -0.0239 | 0.0239 | 0.0000 | -4.0 | 4.0 | -4.0 | 4.0 | -0.0625 | 0.0625 | 114 (36 real + 78 in 13 empty shells) |
| P02 | 0.95718 | 8.6098 | 3.1725 | -3.1725 | 0.0670 | 1.8576 | 4.1236 | -4.1236 | -1.8576 | -0.8375 | 0.4375 | 44 |
| P03 | 0.03815 | 0.7410 | 3.6431 | -3.6431 | -0.3125 | 3.3713 | 3.9010 | -3.9010 | -3.3713 | -0.5 | -0.125 | 26 |
| P04 | 4.29068 | 26.1846 | 7.8370 | -7.8370 | -0.3125 | 3.4720 | 12.2778 | -12.2778 | -3.4720 | -0.7375 | 0.1125 | 20 |
| P05 | 0.36861 | 7.1322 | 12.1799 | -12.1240 | -0.3125 | 11.6799 | 12.6366 | -12.6170 | -11.6799 | -1.3125 | 0.6875 | 91 |
| H1-a | 0.01410 | 0.5887 | 3.1427 | -3.1427 | -0.0147 | 2.9864 | 3.2989 | -3.2989 | -2.9864 | -0.1875 | 0.3175 | 65 |
| H1-b | 0.01410 | 0.5887 | 2.7007 | -2.7007 | -0.0147 | 2.5444 | 2.8569 | -2.8569 | -2.5444 | -0.1875 | 0.3175 | 65 |
| H2-a | 0.04208 | 1.1399 | 12.1069 | -12.1068 | 0.3750 | 11.6880 | 12.4740 | -12.4740 | -11.6880 | 0.1875 | 0.5625 | 62 |
| H2-b | 0.04208 | 1.1399 | 12.1069 | -12.1068 | -1.0000 | 11.6880 | 12.4740 | -12.4740 | -11.6880 | -1.1875 | -0.8125 | 62 |
| H3-a | 0.01016 | 0.4471 | 12.0707 | -12.0705 | 0.3746 | 11.8867 | 12.2617 | -12.2617 | -11.8867 | 0.1875 | 0.5625 | 34 |
| H3-b | 0.01016 | 0.4471 | 12.0707 | -12.0705 | -1.0004 | 11.8867 | 12.2617 | -12.2617 | -11.8867 | -1.1875 | -0.8125 | 34 |

Whole assembly: 13.6734 in3, 177.000 in2, CoM (3.1045, -3.1030, -0.1051), bounding box X [-4.0, 12.6366],
Y [-12.617, 4.0], Z [-1.3125, 0.6875]. No interferences (the clamp socket overlaps the shield's cut corner by 1.36 mm3 only).

Check values: shield 8 x 8 x 0.125; arm length 11.615, tube 0.65, collars 0.85; mounting holes 0.255, 1.375 apart;
base thickness 0.5; clamp 2.2 x 1.05.

## 10. Source simplifications and undetermined items

- The flexible arm is modelled as a straight solid tube; keep it straight and solid.
- No washers; the screws H1 sit with their heads on the shield bottom, the clamp floats 0.005 above the shield.
- The catalogue's 12 in arm length has no exact counterpart in the master (arm 11.615; clamp socket face to base back
  face 12.115); follow this document.
- The catalogue's 0.25 in mounting hole is 0.255 in the master; follow the master.
- Nothing else is undetermined.
