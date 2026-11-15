# Design specification: small plastic electronics enclosure (base, lid, closure screw)

Two-piece moulded box with a lift-off lid held by one central screw. This document is the only source for the rebuild. Every dimension below was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. Do not change the origin or the axes.
- **Global frame (use exactly, no realignment):**
  - Z is the opening direction. The **parting plane** is z = 0: the top of the base wall rim. The base lies below (z < 0 down to z = -0.45), the lid above (up to z = 0.48).
  - The box is centred on the Z axis and symmetric about the planes x = 0 and y = 0 (except where stated). Overall outline 1.85 along X, 2.40 along Y.
  - The screw axis is the Z axis.
- Coordinates written (x, y) are in a plane normal to Z; (x, z) or (y, z) are in vertical planes.
- "Drafted d deg" means the face leans d degrees from the Z direction; the direction in which the outline shrinks is always stated.
- Every body is modelled in place in this frame (identity placement).

## 2. Product description

A black ABS box: an open **base** (P01) and a shallow **lid** (P02) of the same plan outline meet at z = 0 to 0.03 with a tongue-and-groove joint. One **flat countersunk screw** (H1) passes up from the underside through a boss in the base into a boss in the lid. Both outer faces (base bottom, lid top) carry a shallow rectangular label recess.

**Simplifications that exist in the source model and must be reproduced:**
- No threads anywhere. The screw shank is a plain cylinder, the lid boss hole a plain hole slightly smaller than the shank (they overlap, see section 5).
- No ejector marks, text or logos.

## 3. Part list

2 custom parts and 1 hardware item, **3 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Base (open shell) | custom moulding | ABS, black |
| P02 | 1 | Lid | custom moulding | ABS, black |
| H1 | 1 | Flat countersunk cross-recess screw, dia 0.072 x 0.5 | hardware | steel |

## 4. Part geometry

### Common shell outline (P01 and P02)

**Outline S** (at the parting side of each part): rectangle x = -0.925 to 0.925, y = -1.2 to 1.2, four vertical-edge corners R0.1 centred at (+/-0.825, +/-1.1).

**Cavity outline C** (open side of each cavity): rectangle x = -0.845 to 0.845, y = -1.12 to 1.12, with each corner cut by a straight 45 deg chamfer from (+/-0.845, +/-1.02562) to (+/-0.75062, +/-1.12), that is the line |x| + |y| = 1.87062. No corner radius.

**Label recess:** a 0.01-deep rectangular ring groove on the outer flat face: between the rectangles |x| <= 0.755, |y| <= 1.035 (inner) and |x| <= 0.775, |y| <= 1.055 (outer). Sharp corners, walls normal to the face, flat floor.

### P01 Base (one solid, 211 faces in the master)

**B1. Outer shell.** Solid from z = 0 down to the bottom face z = -0.45. At z = 0 the plan is outline S. All side faces (flats and corners) drafted 3 deg so the outline shrinks going down: half-width x = 0.925 - tan(3 deg)(-z), half-length y = 1.2 - tan(3 deg)(-z), the corner centres move in diagonally with the flats (by tan(3 deg)(-z) in both x and y) and the **corner radius stays R0.1 at every height**. This is not a uniform inward offset of the outline (an offset would shrink the corner radius and leave about 2.8 mm3 too much material per corner). In the master the corner faces are R0.1 cylinders whose axis is tilted along the corner diagonal; a constant-radius corner moved this way is equivalent to within 0.0003.

**B2. Bottom edge round.** Convex R0.1 on the whole bottom perimeter edge (bottom face z = -0.45 to the drafted sides). In the section y = 0.6 the round centre is (+/-0.80652, -0.35); it meets the bottom face at |x| = 0.80652 and the wall at (+/-0.90638, -0.35523). Along the four straight edges the round is a cylinder R0.1 with a horizontal axis at z = -0.35 through |x| = 0.80652 (Y sides: |y| = 1.08152). **At each corner the round is a sphere octant R0.1 centred at (+/-0.80652, +/-1.08152, -0.35)**, which meets the bottom face only at the point (+/-0.80652, +/-1.08152, -0.45); the bottom flat face is therefore the sharp-cornered rectangle |x| <= 0.80652, |y| <= 1.08152. (A rolling-ball round of R0.1 on an R0.1 corner is degenerate in many kernels; build the round from these cylinders and spheres if needed.)

**B3. Cavity.** Cut from z = 0 down to the floor z = -0.39. Outline at z = 0 is outline C; all cavity walls (flats and corner chamfers) drafted 1 deg so the cavity narrows going down: wall |x| = 0.845 - tan(1 deg)(-z), |y| = 1.12 - tan(1 deg)(-z); chamfer plane |x| + |y| = 1.87062 - 0.024680(-z).

**B4. Floor fillets.** Concave R0.03 between the floor and the four straight cavity walls only (centres at (+/-0.80871, -0.36) in the section y = 0.6). The fillets run along the straight walls and stop where they meet the corner chamfer planes; the chamfer-to-floor edges are sharp.

**B5. Rim and lip on top of the wall** (profile in the section y = const, valid on all four sides, x side shown):
- top ring of the wall at z = 0 from |x| = 0.845 (cavity wall) to 0.865;
- **lip** z = 0 to 0.03: inner face from (0.865, 0) to (0.86657, 0.03), lip top z = 0.03 from 0.86657 to 0.91343, outer face from (0.91343, 0.03) to (0.915, 0) (both lip faces drafted 3 deg, lip narrower at the top);
- outer step ring z = 0 from |x| = 0.915 to 0.925 (top of the outer shell).
- In plan, the lip's inner boundary at z = 0 is the sharp-cornered rectangle |x| <= 0.865, |y| <= 1.14; its outer boundary at z = 0 is |x| <= 0.915, |y| <= 1.19 with corners R0.09 centred at (+/-0.825, +/-1.1).

**B6. Tongue** on the lip top (z = 0.03), height 0.03 (to z = 0.06). Cross-section: base width 0.0385 at z = 0.03, both flanks drafted 10 deg (tongue narrower at top), convex R0.005 round on both top edges. X-side cross-section: (0.86657, 0.03) up the flank to (0.87113, 0.05587), round R0.005 c=(0.87606, 0.055) to (0.87606, 0.06), top to (0.89559, 0.06), round R0.005 c=(0.89559, 0.055) to (0.90051, 0.05587), flank down to (0.90507, 0.03). The tongue is **six separate segments**:
- On each X side (centreline |x| = 0.88582): two segments, one for y > 0 and one for y < 0. Each runs from a **flat vertical end** at |y| = 0.156 to a **round end**: a half circle of radius 0.01925 (at z = 0.03) centred at (+/-0.88582, +/-1.07085), drafted 10 deg like the flanks, so the segment reaches |y| = 1.09 at its base.
- On each Y side (centreline |y| = 1.16082, base from |y| = 1.14157 to 1.18007): one segment from x = -0.79585 to 0.79585 between centres of half-circle round ends of radius 0.01925 (reaches |x| = 0.8151 at its base).
- The tongue top-edge rounds R0.005 continue around the round ends. The gap |y| < 0.156 on the X sides receives the key of the lid.

**B7. Corner recesses** (4x, one per corner, shown for +x +y). Between z = -0.035 and z = 0 the corner is recessed outward beyond the cavity. Outline at z = 0: start on the cavity wall x = 0.845 at y = 1.05; convex arc R0.02 centred (0.865, 1.05) to (0.865, 1.07); line to (0.865, 1.14); line to (0.795, 1.14); convex arc R0.02 centred (0.775, 1.14) to (0.775, 1.12) on the cavity wall y = 1.12; then along the cavity outline back to the start: line to (0.75062, 1.12), the 45 deg chamfer to (0.845, 1.02562), line to (0.845, 1.05). (At z = 0 the recess thus covers the corner chamfer zone plus the region out to x = 0.865, y = 1.14.) The recess walls are drafted 1 deg (recess narrower going down). Recess floor z = -0.035, flat. Below z = -0.035 the corner is closed by the B3 chamfer. The recess breaks the z = 0 ring and meets the sharp inner corner of the lip at (0.865, 1.14).

**B8. Central screw boss.** Circular boss on the Z axis from the floor up to its flat top at z = 0.03: radius 0.0925 at z = 0.03, drafted 1 deg (radius grows going down: r = 0.0925 + tan(1 deg)(0.03 - z)).

**B9. Four ribs** (cross pattern, arms along +X, -X, +Y, -Y, from the boss to r = 0.15221), described for the +X arm:
- thickness 0.03 at z = 0 (|y| <= 0.015), both sides drafted 1 deg (thicker going down);
- top z = 0 from the boss out to x = 0.123; a step face at x = 0.123 (at z = 0), drafted 1 deg (x = 0.12361 at z = -0.035); lower top z = -0.035 from there to the end face; end face x = 0.15221 at z = -0.035, drafted 1 deg (x grows going down, 0.15833 at z = -0.385).
- The other arms are the same rotated by 90 deg steps about Z.

**B10. Rib and boss fillets.** Concave R0.005 where ribs and boss meet the floor z = -0.39 (rib sides and end faces, boss between the ribs). No other fillets on the ribs.

**B11. Screw hole** on the Z axis, from the bottom face: counterbore dia 0.17 (r 0.085) from z = -0.45 up to z = -0.429; countersink cone 82 deg included (half angle 41 deg) from r 0.085 at z = -0.429 to r 0.0475 at z = -0.38586; through hole dia 0.095 (r 0.0475) up to the boss top z = 0.03.

**B12. Label recess** on the bottom face z = -0.45 (floor at z = -0.44).

### P02 Lid (one solid, 89 faces in the master)

**L1. Outer shell.** Solid from the bottom face z = 0.03 up to the top face z = 0.48. At z = 0.03 the plan is outline S. All side faces drafted 3 deg so the outline shrinks going up: |x| = 0.925 - tan(3 deg)(z - 0.03), same rule for |y|; as in B1 the corner centres move diagonally inward with the flats and the corner radius stays R0.1 at every height (not a uniform offset).

**L2. Top edge round.** Convex R0.1 on the whole top perimeter edge. In the section y = 0.6 the centre is (+/-0.80652, 0.38); it meets the top at |x| = 0.80652 and the wall at (+/-0.90638, 0.38523). As for the base: straight runs are R0.1 cylinders with horizontal axes at z = 0.38, and **each corner is a sphere octant R0.1 centred at (+/-0.80652, +/-1.08152, 0.38)**; the top flat face is the sharp-cornered rectangle |x| <= 0.80652, |y| <= 1.08152.

**L3. Cavity.** Cut from z = 0.03 up to the ceiling z = 0.42. Outline at z = 0.03 is outline C; walls and corner chamfers drafted 1 deg so the cavity narrows going up: |x| = 0.845 - tan(1 deg)(z - 0.03), |y| = 1.12 - tan(1 deg)(z - 0.03), chamfer plane |x| + |y| = 1.87062 - 0.024680(z - 0.03).

**L4. Ceiling fillets.** Concave R0.03 between the ceiling and the four straight walls only (centres (+/-0.80871, 0.39) in the section y = 0.6), stopping at the chamfer planes. Chamfer-to-ceiling edges sharp.

**L5. Groove** in the bottom face (z = 0.03), receiving the base tongue. Mouth at z = 0.03: between an inner rounded rectangle |x| <= 0.865, |y| <= 1.14, corners R0.05 centred at (+/-0.815, +/-1.09), and an outer rounded rectangle |x| <= 0.9035, |y| <= 1.1785, corners R0.0885 on the same centres. Groove floor z = 0.065. Both walls drafted 10 deg so the groove narrows toward the floor (at the floor: |x| from 0.87117 to 0.89733). X-side cross-section: (0.865, 0.03), (0.87117, 0.065), (0.89733, 0.065), (0.9035, 0.03). The groove runs continuously around the corners.
- The bottom face z = 0.03 remains as two rings: |x| from 0.845 to 0.865 (inside the groove) and from 0.9035 to the outer outline (outside the groove), likewise in Y.

**L6. Key.** On each X side the groove is interrupted (left solid) for |y| < 0.146 at the mouth. The two key end faces are drafted 3 deg (|y| = 0.146 at z = 0.03, 0.14417 at z = 0.065).

**L7. Central boss.** On the Z axis, hanging from the ceiling down to its flat bottom z = 0.035: radius 0.0925 at z = 0.035, drafted 1 deg (radius grows going up toward the ceiling).

**L8. Four ribs** (arms along +/-X and +/-Y) from the boss to the end faces, full height from the ceiling down to the common flat bottom z = 0.035. Thickness 0.03 at z = 0.035 (|y| <= 0.015 for the X arms), sides drafted 1 deg (thicker toward the ceiling). End face |x| = 0.153 at z = 0.035, drafted 1 deg (end moves outward toward the ceiling). No fillets on lid ribs or boss.

**L9. Screw hole** dia 0.07 (r 0.035) on the Z axis, from the boss bottom z = 0.035 up to a flat bottom at z = 0.42. Not threaded.

**L10. Label recess** on the top face z = 0.48 (floor at z = 0.47).

### H1 Closure screw (one solid, 23 faces)

Axis = Z axis, head down.
- **Head:** flat face z = -0.45, radius 0.081; conical underside 84 deg included (half angle 42 deg) from r 0.081 at z = -0.45 to r 0.036 at z = -0.40.
- **Shank:** plain cylinder r 0.036 from z = -0.40 to a flat end at z = 0.05. No thread, no chamfer, all edges sharp.
- **Cross recess** in the head face, depth 0.03 (floor z = -0.42). Mouth outline at z = -0.45 (16 vertices, first quadrant shown, mirror to the others): (0.053, -0.0085), (0.053, 0.0085), (0.0235, 0.0085), (0.0085, 0.0235), (0.0085, 0.053), (-0.0085, 0.053) and so on: four arms of width 0.017 reaching 0.053 from the axis, with 45 deg fill flats between the arms. All recess walls drafted 4 deg (recess narrows going up into the head); the floor outline at z = -0.42 is the mouth outline offset inward by 0.0021 (arm half-width 0.0064, arm reach 0.0509). Flat floor.

## 5. Assembly

All three bodies are built in place with identity placement, in the closed position as supplied.

- The lid bottom face z = 0.03 rests on the base lip top z = 0.03 (face contact). The outer step ring of the base (z = 0, |x| 0.915 to 0.925) and the lid bottom leave a 0.03 x 0.01 reveal groove around the outside.
- The tongue (centreline |x| = 0.88582, |y| = 1.16082) is offset 0.00157 outward from the groove centreline (|x| = 0.88425, |y| = 1.15925). Its outer flank therefore overlaps the groove's outer wall slightly: **interference P01-P02 = 4.998 mm3 (0.000305 in3). Reproduce as is.**
- The screw head lies in the base counterbore, head face flush with the base bottom (z = -0.45); there is clearance between the screw and the base hole and countersink.
- The screw shank (r 0.036) enters the lid hole (r 0.035) from z = 0.035 to 0.05: **interference P02-H1 = 0.055 mm3. Reproduce as is.**
- Base and screw do not overlap.

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body (screw 2 percent), centre of mass within 0.02 in, bounding box within 0.005 in. The faces column is information only.

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Base (shell) | 0.50384 | 8256.45 | 16.4101 | 10587.14 | 0.0000 | 0.0000 | -0.2902 | -0.9250 | 0.9250 | -1.2000 | 1.2000 | -0.4500 | 0.0600 | 211 |
| P02 | Lid | 0.47934 | 7854.99 | 15.9829 | 10311.50 | 0.0000 | 0.0000 | 0.3372 | -0.9250 | 0.9250 | -1.2000 | 1.2000 | 0.0300 | 0.4800 | 89 |
| H1 | Closure screw | 0.00230 | 37.61 | 0.1618 | 104.39 | 0.0000 | 0.0000 | -0.2265 | -0.0810 | 0.0810 | -0.0810 | 0.0810 | -0.4500 | 0.0500 | 23 |

**Whole assembly:** 3 bodies; total volume 0.98548 in3 (16149.05 mm3); total area 32.5548 in2 (21003.04 mm2); centre of mass (0, 0, 0.0151) in; bounding box X [-0.925, 0.925], Y [-1.2, 1.2], Z [-0.45, 0.48] in (mm: X [-23.495, 23.495], Y [-30.48, 30.48], Z [-11.43, 12.192]).

**Key functional checks:** outline 1.85 x 2.40, overall height 0.93; base 0.45 below the parting plane (+0.06 lip and tongue above), lid 0.45 high (0.03 to 0.48); cavity depth 0.39 in each part; wall draft outside 3 deg, inside 1 deg; tongue height 0.03, groove depth 0.035; label recess outer 1.55 x 2.11.

## 7. Source conflicts and undetermined items

**Authority:** the master 3D geometry governs.

| Item | Drawing / product data | Master 3D | Decision |
|---|---|---|---|
| Outline | 1.85 x 2.40 x 0.93 | 1.85 x 2.40 x 0.93 | Agree |
| "Inside width / height" | 1.55 / 2.11 (drawing); 1 5/8 / 2 1/8 (product data) | Cavity at the rim 1.69 x 2.24; the label recess outer outline is exactly 1.55 x 2.11 | Follow the 3D. |
| "Inside depth" | 0.75 (drawing), 3/4 (product data) | Base cavity 0.39 + lid cavity 0.39; floor to ceiling 0.81 when closed | Follow the 3D. |
| Screw | steel closure screw | plain unthreaded shank, cross-recess flat head | Follow the 3D. |

**Undetermined:** screw thread size and pitch; wall thicknesses not stated as such (they follow from the drafts above); the moulding's real gate and ejector features (none modelled).
