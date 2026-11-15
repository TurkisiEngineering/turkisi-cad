# Design specification: two-arm adjustable machine handle with threaded hole (P24)

A machine handle made of a round steel hub with a blind tapped hole in its bottom, a bent two-arm lever that passes
through a cross hole in the hub and ends in two ball knobs, and a socket set screw in the top of the hub that clamps the
lever. The master is three solids. This document is the only source for the rebuild. Every value was measured from the
master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (Millimetre values in brackets are exact conversions, 1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - The **hub axis is the Z axis**. The hub bottom face (where the tapped hole opens) is the plane **z = -0.875**, the
    hub top face (where the set screw sits) is **z = 0.875**. The origin is on the hub axis at mid-height of the hub.
  - The lever lies in the plane **x = 0**. Its straight cross bar runs along **Y** through the hub; the two arms rise
    toward **+Z**, one toward +Y and one toward -Y, and end in the ball knobs centred at (0, +-3.0, 1.875).
  - The assembly is symmetric about the plane x = 0 and the plane y = 0, except for the thread of the tapped hole and
    the orientation of the hex socket.
- "(r, z) profile" = a closed profile in a half plane containing the Z axis, r = distance from the Z axis, revolved
  360 deg about Z.
- All three bodies are modelled in place in this frame.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Hub (round body with cross hole, set-screw bore and tapped hole with modelled 1/2-13 thread) | custom |
| P02 | 1 | Lever: cross bar, two bends, two straight arms and two ball knobs (one solid) | custom |
| H1 | 1 | Socket set screw, flat point, hex socket (thread not modelled) | bought-in |

Fits and contacts in the master:
- The P02 cross bar (diameter 0.375) lies in the P01 cross hole (diameter 0.395) on the same axis: radial clearance
  0.01 all round, no contact.
- H1 fills the P01 set-screw bore exactly (same diameter 0.375, top faces flush at z = 0.875). The flat point of H1
  (z = 0.5625) touches the top line of the cross bar (the bar's top is also z = 0.5625): line contact only.
- No pair of bodies overlaps (common volume 0 for all three pairs).

## 3. P01 Hub

**F1. Revolved body.** (r, z) profile, closed, revolved about Z. Start at the bottom face and go in order:
1. (0.26923, -0.875) to (0.6, -0.875) (bottom face, an annulus)
2. convex arc R0.025, centre (0.6, -0.85), to (0.625, -0.85) (bottom outer edge round)
3. line to (0.625, 0.75) (hub cylinder, **diameter 1.25**)
4. line to (0.5, 0.875) (top outer chamfer 0.125 x 45 deg)
5. line to (0.20625, 0.875) (top face, an annulus)
6. line to (0.1875, 0.85625) (set-screw bore mouth chamfer 0.01875 x 45 deg)
7. line to (0.1875, 0.5625) (set-screw bore, **diameter 0.375**, plain, no thread)
8. line to (0, 0.5625) (flat bore floor, 0.3125 below the top face)
9. along the axis down to (0, -0.08092) (solid core between the two holes)
10. line to (0.25, -0.125) (end cone of the tapped hole: 160 deg included, i.e. 10 deg from the plane z = -0.125;
    apex on the axis at z = -0.08092)
11. line to (0.25, -0.85577) (bore of the tapped hole, **diameter 0.5** = thread major diameter)
12. line to (0.26923, -0.875) (entry countersink, 90 deg included, diameter 0.53846 at the bottom face), close.

The countersink cone of step 12 is extended inward: the cone r = 0.26923 - (z + 0.875) (45 deg to the axis) removes all
material inside it, so it also trims the lower end of the thread ridge of F3, down to the crest radius 0.20004 at
z = -0.80581.

**F2. Cross hole.** A straight through hole **diameter 0.395** along Y, axis the line x = 0, z = 0.375 (1.25 above the
bottom face), through the whole hub (y from -0.625 to +0.625). Its top (z up to 0.5725) breaks through the flat floor of
the set-screw bore: the floor z = 0.5625 remains only as two crescent lands at |x| >= 0.06205.

**F3. Internal thread, modelled, 1/2-13 UNC form, right hand.** A helical ridge is added inside the bore of F1
step 11 (it is united with the hub):
- pitch **P = 1/13 = 0.0769231** (13 threads per inch), single start, right hand; flanks at 30 deg to the radial
  direction (60 deg included);
- profile in any half plane through the Z axis (axial lengths along z): the ridge stands on the bore wall r = 0.25 and
  its crest is at **r = 0.20004** (radial depth 0.04996 = 0.75 x 0.866 P); crest flat P/8 = 0.0096154 long; each flank
  spans 3P/8 = 0.0288462 axially; the gap between neighbouring ridges at r = 0.25 (the root flat, on the bore wall) is
  P/8 = 0.0096154 long. The ridge base on the bore wall is therefore 7P/8 = 0.0673077 long;
- **phase:** in the half plane pointing to **+X** from the axis, the crest flats are centred at
  **z = -0.8125 + k P** (k integer) and the root flats at z = -0.850962 + k P. Moving around the axis from +X toward
  +Y the pattern rises by P/4 per quarter turn (right hand): crest centres at -0.8125 + P/4 + k P toward +Y,
  -0.8125 + P/2 + k P toward -X, -0.8125 + 3P/4 + k P toward -Y;
- **lower end:** the ridge reaches below the bottom face; it is cut by the plane z = -0.875 and trimmed by the extended
  countersink cone of F1;
- **upper end:** the ridge stops abruptly at the half plane pointing to **-X** (the plane y = 0, x < 0), on the turn
  whose crest flat is centred there at z = -0.158654; there its upper flank just meets the bore wall at z = -0.125. The
  ridge ends with a flat radial end face in that half plane (a trapezoid between r = 0.20004 and r = 0.25, z from
  -0.192308 to -0.125). Beyond it the bore is plain (diameter 0.5) up to the end cone, about half a turn long.
- Thread length: 0.75 from the bottom face (z = -0.875 to -0.125).

No other features: the hub has no flats, knurl or marking.

## 4. P02 Lever (one solid)

The lever is a round rod **diameter 0.375** (radius 0.1875) swept along a centreline in the plane x = 0, plus two
balls. Centreline, in (y, z) coordinates of the plane x = 0:
1. **Cross bar:** straight from (-0.625, 0.375) to (0.625, 0.375) (along Y, axis z = 0.375, the cross hole axis).
   The bar's flat-looking ends are not exposed: they join the bends at y = +-0.625 (the hub side faces).
2. **Bends:** at y = +0.625 a circular arc of centreline radius **0.375**, centre (0.625, 0.75), turning upward from
   the bar direction (+Y) by **33.5500 deg**; it ends at the tangent point (0.83225, 0.43747). Mirror image at
   y = -0.625 (centre (-0.625, 0.75), ends at (-0.83225, 0.43747)). The bends are tori: tube radius 0.1875, centre
   circle radius 0.375, axis parallel to X through the arc centre.
3. **Arms:** straight from each tangent point to the ball centre (+-3.0, 1.875), direction (+-0.83340, 0.55266),
   i.e. 33.5500 deg above the horizontal. The angle is not a free choice: it is the angle at which the line from the
   ball centre is tangent to the bend arc. Length tangent point to ball centre 2.60108. The arm rod ends inside the
   ball.
4. **Ball knobs:** two spheres **diameter 1.0**, centres (0, +3.0, 1.875) and (0, -3.0, 1.875), united with the arms.
   The arm cylinder meets each ball along its intersection circle; there is no fillet at the junction.

Resulting extents: x from -0.5 to 0.5 (balls), y from -3.5 to 3.5 (**7.0 over the knobs**), z from 0.1875 (bar
underside) to 2.375 (ball tops). The lever has no other features (no flats, no chamfers, no fillets).

## 5. H1 Socket set screw (bought-in)

**F1. Revolved body,** (r, z) profile about the Z axis:
1. (0, 0.5625) to (0.105, 0.5625) (flat point, diameter 0.21)
2. line to (0.1875, 0.645) (45 deg point cone)
3. line to (0.1875, 0.8375) (plain cylinder, **diameter 0.375**; the thread is not modelled)
4. line to (0.15, 0.875) (top chamfer 0.0375 x 45 deg)
5. line to (0, 0.875) (top face), close.

**F2. Hex socket** in the top face: regular hexagon **0.1875 across flats** (corner circle radius 0.10825), flats
normal to +-Y and to +-30 deg / +-150 deg from +X (corners on +-X), depth **0.09375** with a flat floor at
z = 0.78125, walls parallel to Z.

**F3. Socket mouth countersink:** a 90 deg cone (45 deg to the axis) whose circle in the top face z = 0.875 has radius
0.10825 (it passes through the hex corners) and which narrows downward; it removes the material of the socket walls
inside it. On each flat it cuts a shallow curved notch down to z = 0.86050 at the flat centre; at the corners it is
zero. The top face is the annulus between r = 0.10825 and r = 0.15.

Placement: the set screw axis is the Z axis, its top face is flush with the hub top z = 0.875, its flat point at
z = 0.5625 rests on the lever bar.

## 6. Acceptance targets

| ID | Name | Volume in3 | Volume mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Hub | 1.80698 | 29611.04 | 12.2914 | 7929.90 | 0.0000 | 0.0001 | -0.0238 | -0.6250 | 0.6250 | -0.6250 | 0.6250 | -0.8750 | 0.8750 | 45 |
| P02 | Lever | 1.70185 | 27888.39 | 13.0805 | 8438.99 | 0.0000 | 0.0000 | 1.4762 | -0.5000 | 0.5000 | -3.5000 | 3.5000 | 0.1875 | 2.3750 | 14 |
| H1 | Set screw | 0.02743 | 449.49 | 0.5529 | 356.70 | 0.0000 | 0.0000 | 0.7190 | -0.1875 | 0.1875 | -0.1875 | 0.1875 | 0.5625 | 0.8750 | 21 |

CoM in inches. The hub CoM is off the axis by (0.00002, 0.00006) because of the thread. Face counts are those of the
master and depend on how a kernel splits faces; they are for information only.

Whole assembly: 3.53626 in3 (57948.92 mm3), 25.9247 in2 (16725.59 mm2), CoM (0.0000, 0.0000, 0.7039), bounding box
X [-0.625, 0.625], Y [-3.5, 3.5], Z [-0.875, 2.375].

Check values: handle length over the knobs 7.0; overall height hub bottom to knob top 3.25; hub height 1.75; hub
diameter 1.25; knob diameter 1.0, knob centres 6.0 apart and 2.75 above the hub bottom; lever bar axis 1.25 above the
hub bottom; arm angle 33.55 deg; thread 1/2-13, 0.75 long from the bottom face; set-screw bore 0.375, floor 0.3125
deep; hex socket 0.1875 across flats, 0.09375 deep.

## 7. Source simplifications and undetermined items

- The ball knobs are part of the lever solid in the master (no separate knob bodies, no insert, no bore in the balls).
  Reproduce the lever as one solid.
- The set screw and its bore are plain cylinders of the same diameter 0.375: no thread is modelled on either.
  Leave them plain.
- The tapped hole thread is modelled (section 3, F3) and must be reproduced with the given form and phase.
- There is no clamping or ratchet mechanism inside the hub beyond the set screw; the hub is solid apart from the three
  holes.
- The lever is shown in one position (arms in the plane x = 0); keep that position.
- Nothing else is undetermined.
