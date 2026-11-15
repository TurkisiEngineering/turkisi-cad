# Design specification: forged dual-connect lifting shackle with flush pins (P23)

A forged steel link with a clevis at each end: a wide upper clevis (jaw opening 27.686) closed by a Ø20 pin and a
narrow lower clevis (jaw opening 15.545) closed by a Ø16 pin. The pins sit flush with the outside of the lugs and are
held by slotted spring pins driven across the lugs. The master is **six solids**. This document is the only source
for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees. (The product is catalogued in inches, but its geometry is dimensioned in
  millimetres; use the millimetre values below. 1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - **Z is the long axis of the shackle.** The upper (wide) clevis is at +Z, the lower (narrow) clevis at -Z. The
    body runs from z = -69.5 to z = +69.5.
  - **X is the pin direction.** Both pin axes are parallel to X: the upper pin axis is the line (y = 0, z = 50.25),
    the lower pin axis is the line (y = 0, z = -50.25).
  - **Y is the width of the lugs** (the direction in which the spring pins are driven).
  - The origin is the centre of the body: the body is symmetric about the plane y = 0, and about the plane x = 0
    except for the single lower spring pin hole (on the -X lug only).
- "Side profile" = a closed profile in the (y, z) plane; "front profile" = a closed profile in the (x, z) plane.
- All six solids are modelled in place in this frame. There are no overlaps between solids (pins sit in clearance
  holes, see the contacts below).

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Shackle body (one forged solid with both clevises) | custom |
| P02 | 1 | Upper pin, Ø20, with two spring-pin grooves | custom |
| P03 | 1 | Lower pin, Ø16, plain | custom |
| H1 | 2 | Slotted spring pin Ø4.783 x 40 (H1-a in the -X upper lug, H1-b in the +X upper lug) | bought-in |
| H2 | 1 | Slotted spring pin Ø4.783 x 37 (in the -X lower lug) | bought-in |

Contacts and clearances (all from the master):
- P02 lies in the two upper bores of P01 (bore Ø20.0508, pin Ø20: radial clearance 0.0254); its end faces are flush
  with the outer lug faces x = ±30.843.
- P03 lies in the two blind lower bores of P01 (bore Ø16.127, pin Ø16: radial clearance 0.0635); its end faces touch
  the flat bore bottoms x = ±19.1474.
- H1-a, H1-b, H2 lie in their holes (hole Ø4.833784, pin Ø4.782984: radial clearance 0.0254); their end faces are
  flush with the lug faces (y = ±20 upper, y = ±18.5 lower).
- Each upper spring pin passes through the groove of P02 without touching it; H2 passes just outside the end face of
  P03 (it is not grooved into the pin).

## 3. P01 Shackle body

The body is the **intersection of two prisms** (F1, F2), with **every edge of that intersection rounded R3** (F3),
then pin bores and spring-pin holes (F4 to F6).

**F1. Side profile prism.** Closed (y, z) profile, symmetric about y = 0, extruded along X through the whole body
(at least x = -31 to x = +31). Half profile for y >= 0, from the top, in order (mirror it for y <= 0):
1. arc R20, centre (y, z) = (0, 49.5), from (0, 69.5) to (20, 49.5) (round end of the upper clevis);
2. line to (20, 33.531) (upper lug side, width 40 over both sides);
3. convex arc R25.049692, centre (-5.049692, 33.531), from (20, 33.531) to (14.25, 17.562);
4. concave arc R25.049692, centre (33.549692, 1.593), from (14.25, 17.562) to (8.5, 1.593) (arcs 3 and 4 form a
   tangent S-curve with its inflection at (14.25, 17.562));
5. line to (8.5, -20.907652) (neck, width 17);
6. concave arc R7.733975, centre (16.233976, -20.907652), from (8.5, -20.907652) to (12.05659, -27.4164);
7. convex arc R14.011527, centre (4.488473, -39.2082), from (12.05659, -27.4164) to (18.5, -39.2082);
8. line to (18.5, -51.0) (lower lug side, width 37);
9. arc R18.5, centre (0, -51.0), from (18.5, -51.0) to (0, -69.5) (round end of the lower clevis).
All joints are tangent.

**F2. Front profile prism.** Closed (x, z) profile, symmetric about x = 0, extruded along Y through the whole body
(at least y = -20 to y = +20). Its top and bottom are open: run its outer and slot lines past the body ends (for
example to z = ±75) and close them there; only F1 shapes the two ends.
- Outer contour, x >= 0 side, from the top down (mirror for x <= 0):
  1. line x = 30.843 from the top down to z = 6.052974 (outer face of the upper lugs, 61.686 over both);
  2. convex arc R30.843, centre (x, z) = (0, 6.052974), from (30.843, 6.052974) to (27.0585, -8.75);
  3. concave arc R12.826737, centre (38.311375, -14.906141), from (27.0585, -8.75) to (26.97528, -20.90765)
     (deepest point x = 25.484638 at z = -14.906141);
  4. convex arc R30.5224, centre (0, -35.1888), from (26.97528, -20.90765) to (30.5224, -35.1888);
  5. line x = 30.5224 down past the bottom (outer face of the lower lugs, 61.0448 over both).
- Upper slot (open at the top): the lines x = ±13.843 (jaw opening 27.686) from the top down to z = 1.593, then
  two quarter arcs R10.343, centres (±3.5, 1.593), from (±13.843, 1.593) to (±3.5, -8.75), joined by the flat
  bottom line z = -8.75 between x = -3.5 and x = 3.5. The upper lugs are 17.0 thick (13.843 to 30.843).
- Lower slot (open at the bottom): the lines x = ±7.7724 (jaw opening 15.5448) from the bottom up to z = -35.1888,
  closed by a half circle R7.7724, centre (0, -35.1888), top point (0, -27.4164). The lower lugs are 22.75 thick
  (7.7724 to 30.5224).
All joints are tangent.

The intersection F1 ∩ F2 is one solid, 61.686 x 40 x 139 overall.

**F3. R3 rounds.** Round **every edge** of the intersection solid with a constant radius **R3** (rolling ball).
These are the edges where a face of F1 meets a face of F2: the outline of both clevis ends, the four vertical lug
corners of each clevis, the edges of both slots (inner lug faces, upper slot bottom, lower slot half circle) and the
edges along the neck. Tangent joints inside one profile are not edges and get nothing. Where an R3 round meets two
curved faces it is a free-form blend; most of these follow a plain R3 rolling ball within 0.01. The exception is the
blend at the top of the lower slot (where the half circle R7.7724 meets the side faces near (y, z) = (±9, -27)): in
the master it is set back differently. Its sections with planes x = constant, measured on the master, y > 0 side
(mirror to y < 0 and to x < 0), listed as (y, z) points from the slot ceiling up to the side face:

| x | points (y, z) along the blend |
|---|---|
| 0 | (6.090, -27.416) (6.843, -27.320) (7.582, -27.019) (8.250, -26.498) (8.722, -25.856) (9.019, -25.062) (9.086, -24.267) (8.925, -23.436) |
| 2 | (6.223, -27.678) (7.008, -27.570) (7.781, -27.224) (8.388, -26.707) (8.858, -26.002) (9.108, -25.245) (9.154, -24.399) (8.973, -23.571) |
| 4 | (6.759, -28.525) (7.566, -28.402) (8.315, -28.010) (8.920, -27.349) (9.279, -26.582) (9.441, -25.699) (9.395, -24.852) (9.141, -23.991) |
| 6 | (8.490, -30.248) (9.395, -30.097) (10.146, -29.467) (10.388, -28.556) (10.363, -27.557) (10.213, -26.620) (9.939, -25.659) (9.523, -24.751) |
| 7 | (11.237, -31.811) (12.309, -31.485) (12.547, -30.404) (12.130, -29.285) (11.585, -28.402) (11.011, -27.348) (10.484, -26.326) (9.867, -25.298) |
| 8 | (15.807, -34.770) (15.346, -33.344) (14.880, -31.918) (14.255, -30.556) (13.407, -29.261) (12.401, -28.150) (11.422, -27.176) (10.413, -25.999) |

At x = 0 the blend leaves the slot ceiling (z = -27.4164) at y = 6.090 and runs into the concave side arc (F1 step 6)
at (8.925, -23.436). A plain R3 rolling ball there differs from the master by up to about 0.25; match the sections if
your tool allows.

**F4. Upper pin bores.** One straight bore **Ø20.0508** (radius 10.0254) on the upper pin axis (y = 0, z = 50.25),
through both upper lugs (x = 13.843 to 30.843 and x = -30.843 to -13.843). Both ends of each bore have an edge round
**R0.127**.

**F5. Lower pin bores (blind from the slot).** One bore **Ø16.127** (radius 8.0635) on the lower pin axis
(y = 0, z = -50.25) in each lower lug, entering from the slot face x = ±7.7724 and ending in a **flat bottom at
x = ±19.1474** (depth 11.375, no drill point, sharp bottom edge). The entry edge has an edge round **R0.127**. The
lower lugs are solid between x = ±19.1474 and the outer faces x = ±30.5224 (the pin cannot be seen from outside; the
master is drawn that way).

**F6. Spring-pin holes**, all parallel to Y, **Ø4.833784** (radius 2.416892), straight through the lug from face to
face:
- two upper holes, axes (x, z) = (-25.217954, 40.582108) and (25.217954, 40.582108), from y = -20 to y = 20. Each
  axis is 9.667892 below the upper pin axis, so each hole cuts through the lower part of its upper bore;
- one lower hole, **only in the -X lower lug**, axis (x, z) = (-21.691292, -50.25), from y = -18.5 to y = 18.5. It
  passes 0.127 outside the bore bottom x = -19.1474 and does not break into the bore. The +X lower lug has no hole.
Every hole edge on the outer faces has an edge round **R0.0254**; where the upper holes break into the upper bores the
edges carry a tiny blend of about the same size (free-form in the master).

## 4. P02 Upper pin

Axis: the line (y = 0, z = 50.25). "(r, x)" = profile about that axis, r = distance from it.

**F1. Revolved body.** Cylinder **Ø20.0** from x = -30.843 to x = 30.843 (length 61.686), with a **45 deg end
chamfer 1.25 x 1.25** at each end: cone from r 10.0 at x = ±29.593 to r 8.75 at x = ±30.843; flat end faces
Ø17.5 at x = ±30.843 (flush with the lug faces).

**F2. Two spring-pin grooves** (identical, mirrored about x = 0), centred at **x = ±25.217954** (the spring-pin hole
axes). Groove profile in (r, x), revolved 360 deg: a half circle of radius **2.480392** centred at
(r, x) = (9.667892, ±25.217954), concave toward the axis (groove bottom radius 7.1875), continued by two straight
radial walls from r 9.667892 out to the pin surface r 10.0 at x = ±25.217954 ± 2.480392 (x = ±22.737562 and
±27.698346). Groove width 4.960784; the walls are sharp at the pin surface.

## 5. P03 Lower pin

Axis: the line (y = 0, z = -50.25). Plain cylinder **Ø16.0** from x = -19.1474 to x = 19.1474 (length 38.2948), with a
**45 deg end chamfer 1.0 x 1.0** at each end: cone from r 8.0 at x = ±18.1474 to r 7.0 at x = ±19.1474; flat end
faces Ø14 at x = ±19.1474. No groove, no hole.

(The master file holds 17 microscopic empty shells, each about 0.0001 in size, inside this pin near
(-4.103, 0.572, -50.821). They are an artefact of the file: do not model them.)

## 6. H1, H2 Slotted spring pins

A straight tube along Y, cut by one narrow longitudinal slot. Same cross-section for all three:
- outside **Ø4.782984** (r 2.391492), inside **Ø3.195484** (r 1.597742), wall 0.79375;
- the **slot** is a **5.0 deg wedge** whose edge is the pin axis: material is removed between two half-planes that
  both contain the pin axis, one horizontal (z = axis z) and one turned 5 deg below it (toward -Z), on the side of
  the pin given below;
- every edge of both end faces (outer circle, inner circle and the four short slot edges) is rounded **R0.0254**; the
  long slot edges are sharp.

Placement:
| ID | axis (x, z) | from y to y | length | slot side (horizontal half-plane direction / 5 deg half-plane direction) |
|---|---|---|---|---|
| H1-a | (-25.217954, 40.582108) | -20 to 20 | 40.0 | toward +X: (1, 0, 0) and (0.99619, 0, -0.08716) |
| H1-b | (25.217954, 40.582108) | -20 to 20 | 40.0 | toward -X: (-1, 0, 0) and (-0.99619, 0, -0.08716) |
| H2 | (-21.691292, -50.25) | -18.5 to 18.5 | 37.0 | toward +X: (1, 0, 0) and (0.99619, 0, -0.08716) |

All three slots face the centre plane x = 0 and open slightly downward. H1-b is H1-a turned 180 deg about the Z
direction.

## 7. Target table (master, millimetres)

V = volume (mm³), A = surface area (mm²), CoM = centre of mass, bbox = exact bounding box, faces = face count of
the master solid (the P03 count excludes the 17 empty artefact shells).

| ID | name | V | A | CoM x | CoM y | CoM z | xmin | xmax | ymin | ymax | zmin | zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | shackle body | 140650.837 | 31194.900 | 0.1047 | 0.0000 | -6.1002 | -30.8430 | 30.8430 | -20.0000 | 20.0000 | -69.5000 | 69.5000 | 182 |
| P02 | upper pin | 18035.301 | 4658.847 | 0.0000 | 0.0000 | 50.2500 | -30.8430 | 30.8430 | -10.0000 | 10.0000 | 40.2500 | 60.2500 | 24 |
| P03 | lower pin | 7651.455 | 2265.538 | 0.0000 | 0.0000 | -50.2500 | -19.1474 | 19.1474 | -8.0000 | 8.0000 | -58.2500 | -42.2500 | 8 |
| H1-a | upper spring pin -X | 392.375 | 1071.224 | -25.2464 | 0.0000 | 40.5833 | -27.6094 | -22.8265 | -20.0000 | 20.0000 | 38.1906 | 42.9736 | 26 |
| H1-b | upper spring pin +X | 392.375 | 1071.224 | 25.2464 | 0.0000 | 40.5833 | 22.8265 | 27.6094 | -20.0000 | 20.0000 | 38.1906 | 42.9736 | 26 |
| H2 | lower spring pin | 362.946 | 992.310 | -21.7197 | 0.0000 | -50.2488 | -24.0828 | -19.2998 | -18.5000 | 18.5000 | -52.6415 | -47.8585 | 26 |

Assembly: V 167485.288, A 41254.043, CoM (0.0408, 0.0000, -1.9261), bbox x ±30.843, y ±20.0, z ±69.5.

## 8. Notes and simplifications of the source

- The body is shown as clean machined geometry: no forging draft, no parting line, no flash, no markings, no coating
  thickness. Keep it that way.
- The lower pin is completely enclosed (blind bores, no access from outside) and the lower spring pin is outside the
  pin end, not through it. This is how the master is drawn; reproduce it as described.
- The pins are not threaded and have no heads; the spring pins are plain slotted tubes (no chamfers other than the
  R0.0254 edge rounds).
- Undetermined: the exact shape of the free-form R3 blend at the top of the lower slot (sections given in F3 only);
  the exact form of the tiny blend where the upper spring-pin holes break into the upper bores (size about 0.025).
