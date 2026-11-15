# Design specification: ball joint rod end, male shank, 1/2-20 thread

A spherical-bearing rod end: a housing with an integral externally threaded shank, and a ball with integral spacer collars and a through bore, captured in the housing. This document is the only source for the rebuild. Every dimension below was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. Do not change the origin or the axes.
- **Global frame (use exactly, no realignment):**
  - The shank axis is the **Y axis**. The shank points to **-Y**; its end face is at y = -1.625. The shank meets the housing neck at y = 0.
  - The **ball centre is (0, 1, 0)**. The ball bore axis is parallel to **Z** through (0, 1, 0).
  - The housing's flat side faces are normal to Z (z = +/-0.22656). The part is symmetric about the planes x = 0 and z = 0 except for the helical thread.
- "(r, y)" means a profile in a half plane containing the Y axis, r being the distance from the Y axis; it is revolved 360 deg about Y.
- Every body is modelled in place in this frame (identity placement).

## 2. Product description

The housing (P01) is a sphere-shaped eye, flattened on both sides, with a socket for the ball and a flared neck running into a fully threaded shank. The ball (P02) is a sphere with two cylindrical spacer collars along its bore axis, so the overall thickness at the bore is larger than the housing. There is no liner, no seal and no retaining feature in the model: the ball simply sits in a spherical socket of the same radius.

**Simplifications that exist in the source model and must be reproduced:**
- The housing socket is a plain sphere of the ball radius (face contact, zero clearance). No liner body.
- The shank thread **is modelled** as a real helical thread (section 4, P01 F5). Model it, with the stated phase.
- The ball body carries about 120 zero-area degenerate faces in the master (an export artefact at one point). Ignore them; they have no volume or area.

## 3. Part list

2 custom parts, **2 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Housing with integral threaded shank | custom | alloy steel, zinc plated |
| P02 | 1 | Ball with integral spacer collars | custom | bearing steel, chrome plated |

## 4. Part geometry

### P01 Housing with threaded shank (one solid, 85 faces in the master)

**F1. Eye.** Sphere R0.75 centred (0, 1, 0). (It spans y = 0.25 to 1.75; only the part above the neck matters, see F2.)

**F2. Neck.** Solid of revolution about Y between y = 0 and y = 0.4 with the concave profile r(y) = 0.75 - sqrt(0.25 - y^2), that is an arc R0.5 centred at (r, y) = (0.75, 0), from (0.25, 0) to (0.45, 0.4). At y = 0.4 it meets the sphere F1 tangentially (the sphere radius there is also 0.45). Unite F1 and F2.

**F3. Side flats and neck slopes.** Cut both sides symmetrically about z = 0. The housing keeps only |z| <= min(0.22656, 0.25 - 0.25866 y):
- flat faces z = +/-0.22656 (thickness 0.45312) for y >= 0.09062;
- between y = 0 and y = 0.09062 a sloped plane on each side, through z = +/-0.25 at y = 0 and z = +/-0.22656 at y = 0.09062 (slope 14.50 deg from the flat; plane normal (0, 0.2504, +/-0.9681)). At y = 0 the slope just reaches the shank crest radius 0.25.

**F4. Ball socket.** Cut a sphere R0.5625 centred (0, 1, 0). It opens through both flats (opening radius 0.5149 on each flat).

**F5. Threaded shank,** axis Y, from y = 0 down to y = -1.625.
- Major (crest) radius 0.25 (dia 0.5), minor (root) radius 0.21752 (dia 0.43504), depth 0.03248.
- **Right-hand, pitch 0.05 (20 threads per inch), single start, 60 deg included flank angle.** Axial profile per pitch: root flat 0.00625 (P/8), flank, crest flat 0.00625 (P/8), flank; the flanks are at 30 deg to the radial direction.
- **Phase:** on the +X side of the shank (the half plane x > 0, z = 0) the root flat is centred at y = 0.0031 - 0.05k and the crest flat at y = -0.0219 - 0.05k (k integer). Right-hand: moving round the axis from +X toward -Z, the profile advances in +Y by 0.05 per turn (on the -Z side, the root flat is centred at y = 0.0156 - 0.05k).
- **Lower end:** end face y = -1.625, flat disc radius 0.205; 45 deg chamfer cone from r 0.205 at y = -1.625 to r 0.25 at y = -1.58. The chamfer cuts through the full thread depth.
- **Upper end (thread run-out):** the thread groove ends against a 45 deg cone r = 0.25 + y (between r 0.21752 at y = -0.03248 and r 0.25 at y = 0): material inside that cone is not cut. Above y = 0 is the neck.
- One continuous solid with F1 to F4.

### P02 Ball with integral spacer collars (one solid; 14 real faces)

All about the bore axis (parallel to Z through (0, 1, 0)), symmetric about z = 0.
- **Ball:** sphere R0.5625 (dia 1.125) centred (0, 1, 0), between z = -0.44035 and 0.44035.
- **Spacer collars:** cylinder R0.35 (dia 0.70) from z = -0.625 to 0.625 (overall 1.25), united with the ball. The ball/collar intersection lies at |z| = 0.44035.
- **Bore:** dia 0.5 (R0.25) through, along the full length.
- **Bore chamfers:** 45 deg x 0.025 at both ends (cone from r 0.275 at z = +/-0.625 to r 0.25 at z = +/-0.6).
- Collar end faces z = +/-0.625 are flat annuli from r 0.275 to 0.35. Outer collar edges sharp.

## 5. Assembly

Both bodies are built in place, identity placement, as supplied (ball axis along Z, not swivelled).
- The ball sphere and the housing socket are the same sphere (R0.5625 about (0, 1, 0)): face contact, **no volumetric interference** (measured overlap 0.0000 mm3).
- Kinematics: the ball can swivel about its centre (0, 1, 0). The collars (R0.35, reaching |z| = 0.625) stand clear of the housing flats (|z| = 0.22656). No stops are modelled.

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body, centre of mass within 0.02 in, bounding box within 0.005 in. Faces column is information only (P02's count includes the degenerate faces).

| ID | Name | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Housing with threaded shank | 0.69442 | 11379.47 | 9.8350 | 6345.18 | 0.0000 | 0.1926 | 0.0000 | -0.7500 | 0.7500 | -1.6250 | 1.7500 | -0.2500 | 0.2500 | 85 |
| P02 | Ball with spacer collars | 0.59227 | 9705.56 | 6.2209 | 4013.47 | 0.0000 | 1.0000 | 0.0000 | -0.5625 | 0.5625 | 0.4375 | 1.5625 | -0.6250 | 0.6250 | 140 |

**Whole assembly:** 2 bodies; total volume 1.28669 in3 (21085.04 mm3); total area 16.0559 in2 (10358.64 mm2); centre of mass (0.0000, 0.5642, 0.0000) in; bounding box X [-0.75, 0.75], Y [-1.625, 1.75], Z [-0.625, 0.625] in (mm: X [-19.05, 19.05], Y [-41.275, 44.45], Z [-15.875, 15.875]).

**Key functional checks:** overall length 3.375 (y -1.625 to 1.75); ball centre to shank end 2.625; thread length 1.625 (1/2-20, right hand); eye diameter 1.5; housing thickness 0.4531; ball diameter 1.125; bore 0.500; overall thickness at the collars 1.25.

## 7. Source conflicts and undetermined items

**Authority:** the master 3D geometry governs.

| Item | Drawing / product data | Master 3D | Decision |
|---|---|---|---|
| Overall length, centre length, thread length | 3.375, 2.625, 1.625 | same | Agree |
| Eye diameter, thickness | 1.500, 0.4531 | 1.5, 0.45312 | Agree |
| Ball diameter, collar length, bore | 1.125, 1.250, 0.5000 (+0.0015 / -0.0005) | 1.125, 1.25, 0.5 | Agree (model at nominal) |
| Thread | 1/2-20, right hand, fully threaded | 1/2-20 modelled helix, right hand, 1.625 long | Agree |
| Maximum swivel | 65 deg | not a stored quantity | Informational, do not model |
| PTFE liner | in product data | not modelled | Follow the 3D |

**Undetermined:** liner thickness and the real ball-to-socket clearance; material and plating thickness; any wrench flats (none in the 3D).
