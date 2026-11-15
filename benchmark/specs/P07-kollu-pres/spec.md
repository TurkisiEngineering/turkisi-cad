# Design specification: bench-mount rack-and-pinion arbor press

Hand-operated rack-and-pinion arbor press, rated 2000 lb. This document is the only source for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm. 1 in = 25.4 mm exactly. A rebuild may work in inches, or in millimetres by multiplying every value by 25.4. The origin and the axes do not change either way.
- **Global frame (use exactly, no realignment):**
  - +Y is up. Y = 0 is the bench surface (the underside of the base).
  - X is across the press. +X is the lever and knob side, -X is the handwheel side.
  - +Z is toward the operator (front, the open throat side). -Z is the rear of the frame.
  - The ram axis is the line x = 0, z = 0, parallel to Y.
  - The pinion shaft axis is the line y = 9.775, z = -1.15, parallel to X.
- **Profile coordinate conventions used in this document:**
  - "(z, y)" = profile in a plane normal to X.
  - "(x, z)" = profile in a plane normal to Y.
  - "(x, y)" = profile in a plane normal to Z.
  - "(x, r)" = revolve profile, r being the radius from the stated axis.
- All geometry is located directly in the global frame. Each main part (P01 to P10) sits in place, so its feature coordinates are global. The rebuilt bodies must coincide with the original without any transform.
- Arc notation: "arc R c=(a,b) to (p,q)" is a circular arc of radius R centred at (a,b) from the current point to (p,q), taking the minor arc unless a sweep is stated.

## 2. Product description and operation

A cast-iron C-frame stands on a bench, held by two vertical mounting holes in its rear base. A 1 in square steel ram slides vertically in a square channel in the head of the frame. A front cover plate closes the channel. Rack teeth are cut in the rear face of the ram (the -Z face) and mesh with a pinion on the X-axis shaft that passes through the frame head.

The operator turns the shaft with either of two inputs:
1. A long lever bar passing through a cross-hole in the +X end of the shaft, retained at the shaft end by a sleeve and a lobed knob.
2. A three-spoke handwheel with a crank handle on the -X end of the shaft.

Rotating the shaft drives the ram down onto the work. A slotted circular plate sits on a raised seat on the base under the ram. The plate rotates by hand to present slots of different widths (0.5, 0.7875, 1.125, 1.575 in) under the ram, for shafts and arbors of different diameters.

There is no return spring. The ram returns by reversing the lever or handwheel. A circular cap with a small upstanding stud sits on top of the ram and limits downward travel against the frame head.

**Simplifications that exist in the source geometry and must be reproduced:**
- No pinion teeth exist anywhere. The pinion and shaft are plain cylinders fused into the frame body. The frame is one solid that includes the shaft.
- The frame has no internal cavity for the pinion. The rack teeth simply face the solid channel back wall.
- The cover plate fasteners are heads and short studs only. No shanks, and no holes in the cover plate or frame head for them.
- The base plate has no pivot pin or hole.

## 3. Part list

10 distinct custom parts and 8 distinct hardware items, 18 distinct, **25 bodies in total**.

| ID | Qty | Name | Type | Material / finish (where known) |
|---|---|---|---|---|
| P01 | 1 | Frame, with integral pinion shaft | custom casting | Cast iron, painted dark blue, machined faces bare |
| P02 | 1 | Ram with rack | custom | Steel, black oxide look |
| P03 | 1 | Ram cap (stop collar) | custom | Steel, black |
| P04 | 1 | Rotary base plate | custom | Steel, bare ground |
| P05 | 1 | Front cover plate | custom | Cast or steel, painted dark blue |
| P06 | 1 | Lever bar | custom | Steel, bright plated |
| P07 | 1 | Lever retainer sleeve | custom | Steel, bright |
| P08 | 1 | Lobed end knob | custom | Plastic, red |
| P09 | 1 | Handwheel, three spokes | custom | Cast iron; rim bright, spokes black |
| P10 | 1 | Crank handle grip | custom | Plastic, red |
| H1 | 4 | Hex head, no shank (cover corners) | hardware | Steel |
| H2 | 3 | Socket set screw, 0.25 dia x 0.33 (cap, lever end, boss) | hardware | Steel |
| H3 | 2 | Hex nut, 0.375 across flats (cover centre) | hardware | Steel |
| H4 | 2 | Threaded stud, 0.25 dia x 0.35 (cover centre) | hardware | Steel |
| H5 | 1 | Threaded stud, 0.1875 dia x 0.5 (on cap) | hardware | Steel |
| H6 | 1 | Hex nut, 0.25 across flats (on cap stud) | hardware | Steel |
| H7 | 1 | Hex nut, 0.5 across flats (crank handle) | hardware | Steel |
| H8 | 1 | Socket plug screw, 0.375 dia x 0.27 (end of handle) | hardware | Steel |

Finishes come from product photographs. The original 3D geometry carries no colour. Cast iron for the frame and steel for the ram are stated by the product data. All other materials are inferred from appearance.

## 4. Part geometry

All coordinates are global. The features are listed in an order that constructs each part.

### P01 Frame (one solid, 287 faces in the original)

**F1. Base block**, extrude y = 0 to 2.0. Closed outline in (x, z), start at (-0.9769, 1.5), going in the order listed; the last arc closes on the start point:
1. line to (-2.5250, 1.5)
2. arc R0.6313 c=(-2.5250, 0.8688) to (-3.1562, 0.8688)
3. line to (-3.1562, -2.0932)
4. arc R0.6312 c=(-2.5250, -2.0932) to (-2.9461, -2.5635)
5. arc R1.9281 c=(-4.2322, -4.0) to (-2.3041, -4.0) (concave waist)
6. line to (-2.3041, -8.6187)
7. arc R0.6313 c=(-1.6728, -8.6187) to (-1.6728, -9.25)
8. line to (1.6728, -9.25)
9. arc R0.6313 c=(1.6728, -8.6187) to (2.3041, -8.6187)
10. line to (2.3041, -4.0)
11. arc R1.9281 c=(4.2322, -4.0) to (2.9461, -2.5635)
12. arc R0.6312 c=(2.5250, -2.0932) to (3.1562, -2.0932)
13. line to (3.1562, 0.8688)
14. arc R0.6312 c=(2.5250, 0.8688) to (2.5250, 1.5)
15. line to (0.9769, 1.5)
16. arc R0.1894 c=(0.9769, 1.3106) to (0.7875, 1.3106) (rounded slot mouth corner)
17. line to (0.7875, -0.8375)
18. line to (-0.7875, -0.8375)
19. line to (-0.7875, 1.3106)
20. arc R0.1894 c=(-0.9769, 1.3106) to (-0.9769, 1.5)

This creates a front-opening U-slot, 1.575 wide, in the base.

**F2. Underside relief**, cut through full X width, between z = -7.09 and z = -0.66, from y = 0 up to y = 0.4. Profile in (z, y): vertical walls at z = -7.09 and z = -0.66 from y = 0 to y = 0.2106, then arcs R0.1894 to the flat ceiling y = 0.4 (arc centres (-6.9006, 0.2106) and (-0.8494, 0.2106)). The ceiling spans z = -6.9006 to z = -0.8494. The base slot back wall at z = -0.8375 trims the front arc locally. The result is two bench feet: a rear foot z = -9.25 to -7.09 and a front foot z = -0.66 to 1.5.

**F3. Mounting holes**, 2x dia 0.375 through, centres (x, z) = (-1.15, -6.5) and (1.15, -6.5), vertical, from relief ceiling y = 0.4 to base top y = 2.0.

**F4. Raised plate seat**, extrude y = 2.0 to 2.15. Closed outline in (x, z):
1. start (-2.5, -1.15)
2. arc R2.5 c=(0, -1.15) through (0, -3.65) to (2.5, -1.15) (a 180 degree half circle at the rear)
3. line to (2.5, 1.0)
4. arc R0.5 c=(2.0, 1.0) to (2.0, 1.5)
5. line to (0.9769, 1.5)
6. arc R0.1894 c=(0.9769, 1.3106) to (0.7875, 1.3106)
7. line to (0.7875, -0.8375)
8. line to (-0.7875, -0.8375)
9. line to (-0.7875, 1.3106)
10. arc R0.1894 c=(-0.9769, 1.3106) to (-0.9769, 1.5)
11. line to (-2.0, 1.5)
12. arc R0.5 c=(-2.0, 1.0) to (-2.5, 1.0)
13. line to start

The seat centre (0, -1.15) is deliberately different from the plate centre (0, -1.4) in P04.

**F5. Web**, symmetric extrude x = -0.175 to 0.175. Closed outline in (z, y):
1. start (-4.0, 2.0)
2. line to (-4.0, 6.055)
3. arc R2.22 c=(-1.78, 6.055) to (-1.78, 8.275)
4. line to (-0.5, 8.275)
5. line to (-0.5, 11.125)
6. line to (-5.1093, 11.125)
7. arc R3.4488 c=(-5.1093, 7.6762) to (-8.5581, 7.6762)
8. line to (-8.5581, 4.4475)
9. arc R0.8566 c=(-9.4147, 4.4475) to (-8.5938, 4.2029) (16.59 degree concave blend into the raked rear)
10. line to (-9.25, 2.0) (raked rear edge, 16.59 degrees from vertical)
11. line to start

**F6. Rear rim band**, symmetric extrude x = -0.30 to 0.30. Closed outline in (z, y), 0.35 wide band along the rear and top:
1. start (-9.25, 2.0)
2. line to (-8.5938, 4.2029)
3. arc R0.8566 c=(-9.4147, 4.4475) to (-8.5581, 4.4475)
4. line to (-8.5581, 7.6762)
5. arc R3.4488 c=(-5.1093, 7.6762) to (-5.1093, 11.125)
6. line to (-1.15, 11.125)
7. line to (-1.15, 10.775)
8. line to (-5.1093, 10.775)
9. arc R3.0988 c=(-5.1093, 7.6762) to (-8.2081, 7.6762)
10. line to (-8.2081, 4.4475)
11. arc R1.2066 c=(-9.4147, 4.4475) to (-8.2583, 4.1030)
12. line to (-8.8082, 2.2571)
13. arc R0.2 c=(-8.6165, 2.2) through (-8.8165, 2.2) to (-8.6165, 2.0) (106.59 degree sweep)
14. line to start

**F7. Throat flange**, symmetric extrude x = -2.3041 to 2.3041. Closed outline in (z, y), 0.35 thick:
1. start (-4.0, 2.0)
2. line to (-4.0, 6.055)
3. arc R2.22 c=(-1.78, 6.055) to (-1.78, 8.275)
4. line to (-1.15, 8.275)
5. line to (-1.15, 8.625)
6. line to (-1.78, 8.625)
7. arc R2.57 c=(-1.78, 6.055) to (-4.35, 6.055)
8. line to (-4.35, 2.0)
9. line to start

Then blend R0.2 on the two vertical edges where x = +/-2.3041 meets z = -1.15 (edge direction along Y, length y = 8.275 to 8.625). The R0.2 centres are at (x, z) = (+/-2.1041, -1.35).

**F8. Head block**, extrude z = -1.15 to 0.5, outline in (x, y): rectangle x = -1.1875 to 1.1875, y = 8.275 to 11.125, four corners R0.2 (centres at (+/-0.9875, 8.475) and (+/-0.9875, 10.925)).

**F9. Pinion bosses and shaft**, revolve about the pinion axis (y = 9.775, z = -1.15). Profiles in (x, r), each a closed region with r = 0 as the axis.
- +X side:
  (0.175, 0), (0.175, 1.175), (1.1875, 1.175), (1.1875, 1.07),
  concave arc R0.07 c=(1.2575, 1.07) to (1.2575, 1.0),
  (2.2341, 1.0), convex arc R0.07 c=(2.2341, 0.93) to (2.3041, 0.93),
  (2.3041, 0.65), (3.935, 0.65), chamfer line to (3.985, 0.60), (3.985, 0).
- -X side:
  (-0.175, 0), (-0.175, 0.8), (-1.468, 0.8), (-1.468, 0.6), (-1.7486, 0.6), (-1.7486, 0.25), (-1.8486, 0.25), (-1.8486, 0).

The R0.25 x 0.1 tip on the -X side deliberately penetrates the handwheel hub (see section 5). Join both revolved solids to the frame (boolean union).

**F10. Ram channel**, cut through all Y, rectangle x = -0.5 to 0.5, z = -0.5 to 0.5, open at +Z. The back wall of the channel is the plane z = -0.5. Corners are sharp.

**F11. Lever cross-hole**, dia 0.455 through the +X shaft, axis passing through (3.4925, 9.775, -1.15) with direction (0, 0.70711, 0.70711), through all.

**F12. Boss set-screw hole**, dia 0.27, axis parallel to Y through (x, z) = (1.7458, -1.15), blind from the top of the R1.0 boss down to a flat bottom at y = 10.475.

**F13. Web lightening window with raised bead.** The window is a stadium with straight runs along Z at y = 9.5625, end-arc centres at z = -5.2581 and z = -3.2581, height 2 x R.
- Bead (add, both sides): stadium R0.7875, spanning x = -0.275 to 0.275.
- Window (cut through): stadium R0.5875, all through X.
- Bead edges: convex R0.07 blend on the outer edge (between the R0.7875 wall and the x = +/-0.275 land) and on the inner edge (between the R0.5875 wall and the land). Land width remaining 0.06 (at R0.6575 to R0.7175).

The bead cross-section on the +X side in (R, x) is: (0.5875, 0), (0.5875, 0.205), convex arc R0.07 c=(0.6575, 0.205) to (0.6575, 0.275), (0.7175, 0.275), convex arc R0.07 c=(0.7175, 0.205) to (0.7875, 0.205), (0.7875, 0.175).

**F14. Small blends:**
1. Convex R0.03 on the exposed outer top edge of the base block (at y = 2.0) along its outer outline wherever it is not covered by the seat, the flange or the rim: rear edge, rear corners, sides, waists, front corners x = 2.0 to 3.1562.
2. Convex R0.03 on the entire top edge of the seat (at y = 2.15), including the slot edges and slot back wall.
3. Convex R0.03 on the two outer long edges of the rear rim band (x = +/-0.30 with the outer rim surface), along the whole outer path from the base to the head.
4. Concave R0.03 at the junction of web faces x = +/-0.175 with the rear face of the throat flange (z = -4.35, then R2.57 and y = 8.625). Centres at x = +/-0.205.
5. Concave R0.03 at the base top y = 2.0 with the throat flange front face z = -4.0 (x = -2.2741 to 2.2741) and with the flange rear face z = -4.35 (x = 0.175 to 2.2741 each side).
6. Concave R0.04 at the rim sides x = +/-0.30 with base top y = 2.0, from z = -9.2068 to z = -8.6165. The R0.2 concave arc of F6 step 13 extends sideways to x = +/-0.34 to meet it.

All other edges of the frame are sharp in the original.

**F15. Raised lettering "NO. 1"** on both web faces. Each glyph is extruded 0.05 from the web face outward: on the +X face from x = 0.175 to 0.225, on the -X face from x = -0.175 to -0.225. Cap height 0.875, baseline y = 6.775. Letters read correctly from outside on each face, so the +X and -X faces have different Z positions. The two faces use different glyph widths. Coordinates in (z, y):

*-X face:*
- N, closed polygon: (-7.8207,6.7750) (-7.6973,6.7750) (-7.6973,7.4279) (-7.2780,6.7750) (-7.1476,6.7750) (-7.1476,7.6500) (-7.2710,7.6500) (-7.2710,6.9971) (-7.6903,7.6500) (-7.8207,7.6500).
- O outer, closed smooth spline through: (-6.9906,7.2009) (-6.9621,7.0351) (-6.8774,6.8909) (-6.7404,6.7953) (-6.5755,6.7638) (-6.4080,6.7966) (-6.2688,6.8936) (-6.1859,7.0419) (-6.1604,7.2111) (-6.1857,7.3808) (-6.2684,7.5297) (-6.4070,7.6286) (-6.5750,7.6612) (-6.7459,7.6290) (-6.8855,7.5269) (-6.9675,7.3746).
- O inner, closed smooth spline (subtract): (-6.8672,7.1995) (-6.8546,7.3319) (-6.8035,7.4516) (-6.7018,7.5326) (-6.5743,7.5603) (-6.4505,7.5329) (-6.3528,7.4531) (-6.2991,7.3385) (-6.2838,7.2120) (-6.2986,7.0842) (-6.3535,6.9702) (-6.4519,6.8910) (-6.5760,6.8647) (-6.6972,6.8901) (-6.7944,6.9660) (-6.8512,7.0756).
- Period, square: z = -5.9922 to -5.8800, y = 6.7750 to 6.8872.
- 1, closed outline: (-4.9825,6.7750) (-4.9825,7.6500) (-5.0548,7.6500), spline (-5.1004,7.5811) (-5.1572,7.5234) (-5.2216,7.4741) to (-5.2966,7.4313), line to (-5.2966,7.3278), spline (-5.2401,7.3542) (-5.1896,7.3836) (-5.1414,7.4165) to (-5.0947,7.4568), line to (-5.0947,6.7750), close.

*+X face:*
- N, closed polygon: (-5.1922,6.7750) (-5.1013,6.7750) (-5.1013,7.6500) (-5.1980,7.6500) (-5.5672,6.9526) (-5.5672,7.6500) (-5.6581,7.6500) (-5.6581,6.7750) (-5.5608,6.7750) (-5.1922,7.4716).
- O outer, closed smooth spline: (-5.8058,7.2010) (-5.8111,7.1183) (-5.8267,7.0425) (-5.8539,6.9701) (-5.8944,6.9009) (-5.9455,6.8424) (-6.0061,6.7988) (-6.0758,6.7723) (-6.1524,6.7636) (-6.2285,6.7720) (-6.2977,6.7977) (-6.3582,6.8400) (-6.4099,6.8973) (-6.4520,6.9690) (-6.4791,7.0451) (-6.4941,7.1246) (-6.4990,7.2116) (-6.4813,7.3700) (-6.4191,7.5148) (-6.3047,7.6223) (-6.1529,7.6614) (-5.9980,7.6216) (-5.8824,7.5113) (-5.8220,7.3629).
- O inner, closed smooth spline (subtract): (-5.8967,7.1995) (-5.9070,7.3249) (-5.9481,7.4412) (-6.0346,7.5282) (-6.1537,7.5591) (-6.2228,7.5484) (-6.2836,7.5179) (-6.3338,7.4719) (-6.3701,7.4121) (-6.3882,7.3622) (-6.3993,7.3159) (-6.4057,7.2687) (-6.4081,7.2143) (-6.3968,7.0923) (-6.3532,6.9802) (-6.2676,6.8965) (-6.1517,6.8659) (-6.0394,6.8952) (-5.9548,6.9747) (-5.9092,7.0816).
- Period, rectangle: z = -6.7149 to -6.6240, y = 6.7750 to 6.9000.
- 1, closed outline: (-7.4763,7.6614) (-7.4763,6.7750) (-7.3854,6.7750) (-7.3854,7.4682), spline (-7.3444,7.4264) (-7.3012,7.3914) (-7.2554,7.3600) to (-7.2036,7.3318), line to (-7.2036,7.4341), spline (-7.2714,7.4798) (-7.3291,7.5320) (-7.3788,7.5918) to (-7.4173,7.6614), close.

### P02 Ram with rack

Square bar x = -0.5 to 0.5, z = -0.5 to 0.5, y = 4.825 to 14.575. All long edges sharp, ends square.

- **Top blind hole:** dia 0.5, axis x = z = 0, from y = 14.575 down to a flat bottom at y = 14.075.
- **Rack teeth:** on the -Z face only, 27 identical notches cut straight across the full X width, pitch 0.26 along Y. Notch centre k is at y = 6.325 + 0.26 x k, for k = 0 to 26 (first 6.325, last 13.085). Notch profile in (z, y) relative to the notch centre yc:
  (-0.5, yc - 0.0882), (-0.32, yc - 0.04), (-0.32, yc + 0.04), (-0.5, yc + 0.0882), close at the -Z face. Depth 0.18, root flat 0.08, flanks 15 degrees from the plane normal to Y. Tooth tip land 0.0836 between notches on the z = -0.5 plane.

The toothed zone spans y = 6.2368 to 13.1732. No fillets anywhere on the ram.

### P03 Ram cap (stop collar)

Disc outer radius 1.1875, y = 14.075 to 14.575, axis x = z = 0.
- Chamfer 0.02 x 45 degrees on both outer circular edges.
- Square through-hole x = -0.5 to 0.5, z = -0.5 to 0.5, through all Y.
- Four corner relief circles, R0.1, centred exactly on the corners of the square at (x, z) = (+/-0.5, +/-0.5), through all Y. Each cuts a 270 degree relief around the square corner.
- Radial set-screw hole: dia 0.25, axis along Z at x = 0, y = 14.325, from the +Z outer surface inward to a flat bottom at z = 0.85. It does not reach the square hole.

### P04 Rotary base plate

Disc centre (x, z) = (0, -1.4), radius 2.25, y = 2.15 to 2.90 (thickness 0.75).
- Chamfer 0.1 x 45 degrees on both outer circular edges (top and bottom).
- Four open-ended U-slots cut through all Y, each running from an arc centre out through the disc edge. Sides are parallel to the slot direction.

| Slot | Direction from plate centre | Width | End-arc centre (x, z) | End-arc R | Top-edge chamfer (45 degrees) |
|---|---|---|---|---|---|
| A | +Z | 0.5 | (0, -0.05) | 0.25 | 0.03 |
| B | -Z | 1.125 | (0, -2.75) | 0.5625 | 0.08 |
| C | +X | 1.575 | (1.35, -1.4) | 0.7875 | 0.08 |
| D | -X | 0.7875 | (-1.35, -1.4) | 0.39375 | 0.03 |

The top-edge chamfer applies at y = 2.90 around the whole slot outline (end arc and both straight sides). The bottom slot edges are sharp. Where a slot chamfer meets the outer disc chamfer, the small resulting blend is unimportant.

### P05 Front cover plate

Plate x = -1.1875 to 1.1875, y = 8.275 to 11.125, z = 0.501 to 1.10.
- Corners R0.2 on the four edges parallel to Z (centres at (+/-0.9875, 8.475), (+/-0.9875, 10.925)).
- Convex R0.08 on the front perimeter edge at z = 1.10 (all four sides and corners).
- **Recessed front panel**, floor z = 1.05, rounded-rectangle outline. At the recess mid-wall (z = 1.075) the outline is x = -0.65 to 0.65, y = 8.7625 to 10.6375, with corner radii R0.2 centred at (+/-0.45, 8.9625) and (+/-0.45, 10.4375).
- The wall is an S-shaped transition of two R0.025 arcs. In profile (wall distance from the mid-wall centre line, z): top edge 0.025 outside mid-wall at z = 1.10, convex arc centre at (0.025 outside, 1.075) to the mid-wall at z = 1.075, concave arc centre at (0.025 inside, 1.075) to the floor edge 0.025 inside mid-wall at z = 1.05.
- **Two circular islands** inside the recess, centres (x, y) = (0, 9.2) and (0, 10.2), flat top z = 1.10 with top radius R0.2875, base radius R0.3375 at the floor z = 1.05, with the same two-arc R0.025 S-transition (arc centres R = 0.2875 and 0.3375, z = 1.075).
- The rear face is flat at z = 0.501. No holes. The 0.001 gap from the frame front face z = 0.5 is intentional.

### P06 Lever bar

Straight bar, axis passing through (3.4925, 9.775, -1.15), direction (0, 0.70711, 0.70711). Define t = (y + z) / sqrt(2), so the axis point at t = 6.0988 is the shaft centre. Revolve about the axis. Profile in (t, r):

(0.5363, 0), (0.5363, 0.2625), chamfer to (0.5663, 0.2925), (1.1213, 0.2925), (1.1213, 0.2275), (11.0763, 0.2275), (11.0763, 0.2925), (11.6313, 0.2925), chamfer to (11.6613, 0.2625), (11.6613, 0).

- Overall length 11.125, centred on the shaft. Rod dia 0.455, end collars dia 0.585 by 0.555 long plus chamfer 0.03 x 45 degrees.
- At the upper end (t = 11.6613): blind hole dia 0.25 along the axis from the end face to flat bottom t = 11.2613 (0.4 deep), with a 0.01 x 45 degree chamfer at the mouth.

### P07 Lever retainer sleeve

Stepped solid revolve about the pinion axis. Profile (x, r): (3.985, 0), (3.985, 0.25), (4.41, 0.25), (4.41, 0.5), (4.61, 0.5), (4.61, 0).

### P08 Lobed end knob

About the pinion axis.
1. Revolve profile (x, r), solid: (4.41, 0), (4.41, 0.65), (4.785, 0.65), convex arc R0.125 c=(4.785, 0.525) to (4.91, 0.525), (4.91, 0).
2. Rear counterbore: dia 1.0, from x = 4.41 to flat bottom x = 4.61, centred on the axis.
3. Front recess: dia 0.6, from x = 4.91 to flat bottom x = 4.8725.
4. Six scallops, circles R0.25 parallel to X through the full length. Centres in (z, y): (-0.375, 9.775), (-0.7625, 10.4462), (-1.5375, 10.4462), (-1.925, 9.775), (-1.5375, 9.1038), (-0.7625, 9.1038). These lie on a circle of radius 0.775 about the axis, 60 degrees apart, two of them on the Z direction through the axis. Scallops cut the R0.125 end blend too.

### P09 Handwheel

Axis is the pinion axis. Hub has no bore (solid).

1. **Dished disc, revolve, profile in (x, r), closed:**
   (-1.7486, 0), (-1.7486, 0.625), (-2.3486, 0.625), (-2.3486, 0.925),
   line (front cone) to (-3.1240, 2.2033),
   arc R0.15 c=(-2.9958, 2.2811) to (-3.1458, 2.2811),
   line to (-3.1458, 2.60),
   line to (-3.6687, 2.60),
   line to (-3.6687, 2.4392),
   line (rear cone) to (-2.7138, 0.8650),
   line to (-2.7138, 0), close along the axis.
   Both cone generators make 58.759 degrees with the axis. The (-3.1458, 2.60) and (-3.6687, 2.60) corners are hidden inside the rim added in step 3.
2. **Cut between spokes.** Three spokes on the disc, centre lines through the axis, in (y, z) directions from the axis: S1 (-1, 0), S2 (0.5, 0.86603), S3 (0.5, -0.86603). Each spoke is 1.0 wide (flat sides 0.5 from its centre line). Remove all disc material outside the three spoke strips and outside radius 0.925. The hub cylinder R0.925 then remains between spokes, from x = -2.3486 to x = -2.7502.
3. **Rim**, torus, centre circle in plane x = -3.4072, major R2.6586, section circle r0.3414. Rim extreme x values are -3.7486 and -3.0658, overall dia 6.0. Join to the wheel (boolean union).
4. **Spoke edge blends.** Convex R0.15 on all 12 longitudinal edges of the three spokes (each spoke's two side planes against the front cone and the rear cone), running from the hub cylinder to the rim. On the front side the blend continues along the flat ring face x = -3.1458 to the rim.
5. **Crank boss on spoke S2**, axis parallel to X through (y, z) = (11.0259, 1.0166), 2.5018 from the wheel axis along the S2 direction. Profile in (z, y): circle R0.35 around the boss axis, plus two tangent lines extending to the rim:
   - tangent point (0.7723, 11.2765), going outward through (0.8318, 11.3345), and
   - tangent point (1.1114, 10.6890), going outward through (1.1915, 10.7116).
   Both lines run outward until they meet the rim. The boss end faces at x = -3.7486 and x = -3.0659 lie tangent to the rim's rear and front extremes. Extrude x = -3.7486 to -3.0659, keep only the portion inside the rim, and join it to the wheel. Convex R0.03 on the rear edge of the boss cylinder at x = -3.7486.
6. **Recess on the front of the boss:** blind dia 0.375, centre (y, z) = (10.9776, 0.9330), from x = -3.0659 to flat bottom x = -3.1659.

### P10 Crank handle grip

Axis parallel to X through (y, z) = (11.0259, 1.0166), +X end at x = -3.9486 (flat, R0.25 end). Revolve profile in (x, r), solid:

(-3.9486, 0), (-3.9486, 0.25), line (taper 2.603 degrees) to (-6.6463, 0.3727), convex arc R0.05 c=(-6.6486, 0.3227) to (-6.6986, 0.3227), (-6.6986, 0.2375), then recess: convex arc R0.05 c=(-6.6486, 0.2375) to (-6.6486, 0.1875), (-6.3986, 0.1875), (-6.3986, 0).

The end recess dia 0.375 is therefore blind, floor at x = -6.3986, with mouth radius R0.05.

### Hardware

Each hardware part is defined in a local frame (origin O, axes U, V, W). The pose of every instance is in section 5.

**H1 Hex head, no shank (0.1696 tall).**
- Base plane w = 0. Flats normal to U at u = +/-0.20185 (across flats 0.4037), corners on V.
- 30 degree chamfer: cone cut at the top, circle R0.20185 at w = 0.1696, radius increasing downward at 60 degrees from the axis (reaching corner radius 0.2331 at w = 0.1515). Bottom face is not chamfered.

**H2 Socket set screw.**
- Cylinder R0.125, w = 0 (flat tip, no chamfer) to w = 0.33, with 0.01 x 45 degree chamfer at w = 0.33.
- Hex socket from w = 0.33 down to flat bottom w = 0.23, across flats 0.1575 (flats normal to U, corners on V).
- A lead-in countersink at the mouth, 120 degrees included, circle R0.0909 at w = 0.33 reducing to R0.0787 at depth 0.007. It removes material only where it exceeds the hex.

**H3 Hex nut, cover centre.**
- w = 0 to 0.20. Flats normal to V at v = +/-0.1875 (across flats 0.375), corners on U.
- 30 degree chamfers on both faces (circle R0.1875 at each face, radius increasing inward at 60 degrees from the axis).
- Through-bore R0.125, plain, no thread modelled in the nut.

**H4 Threaded stud, cover centre.**
- Length w = 0 to 0.35, major R0.125, flat at w = 0. Tip chamfer at w = 0.35 from R0.105 at the tip, 45 degrees, to the thread.
- **Real helical thread is modelled, right-handed**, pitch 0.04, 60 degree included flanks, root R0.099, depth 0.026, crest land 0.005, root land 0.005. Groove runs the full length and overruns both ends. Phase: root centre on the +U direction at w = -0.0025 + 0.04k.

**H5 Threaded stud, on cap.**
- Length w = 0 to 0.5, major R0.09375, flat at w = 0. Tip chamfer at w = 0.5 from R0.08125, 45 degrees.
- **Real helical thread, right-handed**, pitch 0.03, 60 degree flanks, root R0.0743, depth 0.01945, crest land 0.0037, root land 0.0038, full length with overruns. Phase: root centre on the +U direction at w = 0.0181 + 0.03k.

**H6 Hex nut on cap stud.**
- w = 0 to 0.10, across flats 0.25 (flats normal to V, corners on U), through-bore R0.09375, 30 degree chamfers both faces (circle R0.125).

**H7 Hex nut, crank handle (no bore).**
- w = 0 to 0.20, across flats 0.5 (flats normal to V, corners on U). 30 degree chamfer at w = 0.20 only (circle R0.25). Solid, no bore. The w = 0 face has no chamfer.

**H8 Socket plug screw.**
- Cylinder R0.1875, w = 0 to 0.27, chamfer 0.03 x 45 degrees at w = 0.27 (R0.1575 at the end).
- Hex socket from w = 0.27 to flat bottom w = 0.17, across flats 0.1968 (flats normal to V, corners on U).
- Lead-in countersink at the mouth, circle R0.1137 at w = 0.27, 120 degrees included, down to the flats at depth 0.0088.

## 5. Assembly

P01 to P10 are defined directly in global coordinates (no rotation, origin at (0, 0, 0)). The pose below is the pose as supplied, and the supplied pose is to be reproduced exactly.

Hardware instance pose, local origin O, local axes U, V, W expressed in global coordinates.

| Instance | Part | Origin O (x, y, z) | U | V | W |
|---|---|---|---|---|---|
| H1-a | H1 | (-0.83125, 10.76875, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H1-b | H1 | (0.83125, 10.76875, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H1-c | H1 | (0.83125, 8.63125, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H1-d | H1 | (-0.83125, 8.63125, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H2-a | H2 (in P03) | (0, 14.325, 0.85) | (1,0,0) | (0,1,0) | (0,0,1) |
| H2-b | H2 (in P06) | (3.4925, 13.4608, 2.5358) | (1,0,0) | (0,0.70711,-0.70711) | (0,0.70711,0.70711) |
| H2-c | H2 (in P01) | (1.7458, 10.475, -1.15) | (1,0,0) | (0,0,-1) | (0,1,0) |
| H3-a | H3 | (0, 10.2, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H3-b | H3 | (0, 9.2, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H4-a | H4 | (0, 10.2, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H4-b | H4 | (0, 9.2, 1.10) | (1,0,0) | (0,1,0) | (0,0,1) |
| H5 | H5 | (0.84375, 14.575, 0) | (1,0,0) | (0,0,-1) | (0,1,0) |
| H6 | H6 | (0.84375, 14.575, 0) | (1,0,0) | (0,0,-1) | (0,1,0) |
| H7 | H7 | (-3.7486, 11.0259, 1.0166) | (0,0,1) | (0,1,0) | (-1,0,0) |
| H8 | H8 | (-6.3986, 11.0259, 1.0166) | (0,0,1) | (0,1,0) | (-1,0,0) |

Each hardware instance is a rigid copy: R = [U V W] maps local to global, and a local point p maps to O + R p. All U, V, W triads above are right-handed (U x V = W).

Note on H3 and H4: the nut and stud of each pair share the same origin and axes, and the nut bore equals the thread crest diameter. There is no interference by volume.

**Kinematics and relations:**
- **Ram:** translates along global Y only, sliding in the frame channel and against the cover plate. Supplied at y = 4.825 (bottom end). Bottom end to plate top (y = 2.90) is 1.925 in the supplied pose.
- **Cap and stud:** ride with the ram. The cap is a collar around the top 0.5 of the ram, its square hole on the ram section, its top face flush with the ram top at y = 14.575, retained by set screw H2-a. The cap underside at y = 14.075 is 2.95 above the frame head top y = 11.125 as supplied, so it stops downward travel 2.95 from the supplied pose. Before that, the ram reaches the plate after 1.925.
- **Pinion shaft:** rotates about the pinion axis (x direction, through y = 9.775, z = -1.15). In the source it is fused to the frame, so no separate moving body exists.
- **Lever and handwheel:** both rotate with the shaft. The lever bar lies at +45 degrees in the Y-Z plane (upper end toward +Z). The retainer sleeve seats against the shaft end x = 3.985. The knob seats on the sleeve head.
- **Rotary plate:** sits flat on the seat at y = 2.15, free to rotate about (x, z) = (0, -1.4). As supplied, slot A is toward +Z. No geometry that fixes its rotation exists.
- **Handwheel to frame:** the frame tip R0.25, x = -1.7486 to -1.8486, passes 0.10 into the solid handwheel hub (hub face at x = -1.7486). Overlap volume 0.0196 in3. Reproduce as is.
- All other adjacent bodies touch with zero or positive clearance, no volumetric overlap by measurement.

## 6. Acceptance targets

Measure each body at the supplied pose. Bounding box, volume, area, centre of mass, instance count should all match. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body, centre of mass within 0.02 in, bounding box within 0.005 in. For hardware with tiny features, accept volume within 2 percent.

Coordinates in inches (centre of mass and bounding box extents). The same origin and axes apply in mm by multiplying by 25.4. The "faces" column is for information only: it is the face count in the original and a correct rebuild may differ, for example where a CAD system splits or merges faces.

| ID | Vol in3 | Vol mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Frame | 143.2973 | 2348222.3 | 414.462 | 267394.0 | 0.0828 | 3.3324 | -3.5496 | -3.1563 | 3.9850 | 0.0000 | 11.1250 | -9.2500 | 1.5000 | 287 |
| P02 Ram | 9.0286 | 147952.6 | 47.997 | 30966.0 | 0.0000 | 9.6494 | 0.0291 | -0.5000 | 0.5000 | 4.8250 | 14.5750 | -0.5000 | 0.5000 | 117 |
| P03 Ram cap | 1.6485 | 27013.9 | 13.031 | 8407.4 | 0.0000 | 14.3250 | -0.0102 | -1.1875 | 1.1875 | 14.0750 | 14.5750 | -1.1875 | 1.1875 | 21 |
| P04 Rotary base plate | 7.8363 | 128413.3 | 36.778 | 23727.8 | -0.1749 | 2.5239 | -1.2673 | -2.2153 | 2.1077 | 2.1500 | 2.9000 | -3.5786 | 0.8361 | 44 |
| P05 Front cover plate | 3.9307 | 64412.9 | 19.456 | 12552.4 | 0.0000 | 9.7000 | 0.7933 | -1.1875 | 1.1875 | 8.2750 | 11.1250 | 0.5010 | 1.1000 | 45 |
| P06 Lever bar | 1.9119 | 31329.7 | 17.373 | 11208.3 | 3.4925 | 9.7360 | -1.1890 | 3.2000 | 3.7850 | 5.6561 | 13.8939 | -5.2689 | 2.9689 | 19 |
| P07 Lever retainer sleeve | 0.2405 | 3941.6 | 2.867 | 1849.5 | 4.4016 | 9.7750 | -1.1500 | 3.9850 | 4.6100 | 9.2750 | 10.2750 | -1.6500 | -0.6500 | 7 |
| P08 Lobed end knob | 0.3885 | 6366.2 | 5.012 | 3233.7 | 4.7109 | 9.7750 | -1.1500 | 4.4100 | 4.9100 | 9.1250 | 10.4250 | -1.7698 | -0.5302 | 26 |
| P09 Handwheel | 9.5249 | 156084.8 | 56.274 | 36305.7 | -3.1371 | 9.7785 | -1.1439 | -3.7486 | -1.7486 | 6.7750 | 12.7750 | -4.1500 | 1.8500 | 71 |
| P10 Crank handle | 0.8198 | 13433.7 | 6.315 | 4074.4 | -5.4594 | 11.0259 | 1.0166 | -6.6986 | -3.9486 | 10.6532 | 11.3986 | 0.6440 | 1.3893 | 11 |
| H1-a Hex head | 0.0239 | 391.1 | 0.513 | 330.9 | -0.8312 | 10.7688 | 1.1845 | -1.0331 | -0.6294 | 10.5356 | 11.0019 | 1.1000 | 1.2696 | 14 |
| H1-b Hex head | 0.0239 | 391.1 | 0.513 | 330.9 | 0.8312 | 10.7688 | 1.1845 | 0.6294 | 1.0331 | 10.5356 | 11.0019 | 1.1000 | 1.2696 | 14 |
| H1-c Hex head | 0.0239 | 391.1 | 0.513 | 330.9 | 0.8312 | 8.6312 | 1.1845 | 0.6294 | 1.0331 | 8.3981 | 8.8644 | 1.1000 | 1.2696 | 14 |
| H1-d Hex head | 0.0239 | 391.1 | 0.513 | 330.9 | -0.8312 | 8.6312 | 1.1845 | -1.0331 | -0.6294 | 8.3981 | 8.8644 | 1.1000 | 1.2696 | 14 |
| H2-a Set screw (cap) | 0.0140 | 229.4 | 0.405 | 261.5 | 0.0000 | 14.3250 | 0.9968 | -0.1250 | 0.1250 | 14.2000 | 14.4500 | 0.8500 | 1.1800 | 20 |
| H2-b Set screw (lever) | 0.0140 | 229.4 | 0.405 | 261.5 | 3.4925 | 13.5646 | 2.6396 | 3.3675 | 3.6175 | 13.3724 | 13.7755 | 2.4474 | 2.8505 | 20 |
| H2-c Set screw (boss) | 0.0140 | 229.4 | 0.405 | 261.5 | 1.7458 | 10.6218 | -1.1500 | 1.6208 | 1.8708 | 10.4750 | 10.8050 | -1.2750 | -1.0250 | 20 |
| H3-a Cover nut upper | 0.0144 | 236.4 | 0.551 | 355.4 | 0.0000 | 10.2000 | 1.2000 | -0.2165 | 0.2165 | 10.0125 | 10.3875 | 1.1000 | 1.3000 | 24 |
| H3-b Cover nut lower | 0.0144 | 236.4 | 0.551 | 355.4 | 0.0000 | 9.2000 | 1.2000 | -0.2165 | 0.2165 | 9.0125 | 9.3875 | 1.1000 | 1.3000 | 24 |
| H4-a Cover stud upper | 0.0138 | 226.8 | 0.503 | 324.4 | 0.0003 | 10.1997 | 1.2744 | -0.1250 | 0.1250 | 10.0750 | 10.3250 | 1.1000 | 1.4500 | 25 |
| H4-b Cover stud lower | 0.0138 | 226.8 | 0.503 | 324.4 | 0.0003 | 9.1997 | 1.2744 | -0.1250 | 0.1250 | 9.0750 | 9.3250 | 1.1000 | 1.4500 | 25 |
| H5 Cap stud | 0.0111 | 182.5 | 0.504 | 324.9 | 0.8438 | 14.8247 | -0.0002 | 0.7500 | 0.9375 | 14.5750 | 15.0750 | -0.0938 | 0.0938 | 41 |
| H6 Cap stud nut | 0.0026 | 42.9 | 0.193 | 124.8 | 0.8438 | 14.6250 | 0.0000 | 0.6994 | 0.9881 | 14.5750 | 14.6750 | -0.1250 | 0.1250 | 22 |
| H7 Handle nut | 0.0432 | 707.4 | 0.769 | 496.3 | -3.8483 | 11.0259 | 1.0166 | -3.9486 | -3.7486 | 10.7759 | 11.2759 | 0.7280 | 1.3053 | 15 |
| H8 Handle plug screw | 0.0259 | 425.1 | 0.582 | 375.8 | -6.5201 | 11.0259 | 1.0166 | -6.6686 | -6.3986 | 10.8384 | 11.2134 | 0.8291 | 1.2041 | 20 |

**Whole assembly:**
- Instance count: 25 bodies (10 custom + 15 hardware).
- Total volume: 178.904 in3 (2 931 708 mm3).
- Total surface area, sum over bodies: 626.99 in2 (404 509 mm2).
- Centre of mass, uniform density: (-0.0813, 4.3380, -2.9512) in.
- Bounding box, in: X [-6.6986, 4.9100], Y [0, 15.0750], Z [-9.2500, 2.9689]. In mm: X [-170.144, 124.714], Y [0, 382.905], Z [-234.950, 75.410].

**Key functional checks:**
- Base width 6.3125, base length 10.75 (z from -9.25 to 1.5), height to head top 11.125.
- Throat depth from ram axis to flange front face: 4.0.
- Head underside y = 8.275. Clearance over the seat 6.125. Clearance over the plate 5.375.
- Base height 2.0, seat height 2.15.
- Mounting holes 2 x dia 0.375 at x = +/-1.15, z = -6.5.
- Ram section 1.0 x 1.0, length 9.75, top bore dia 0.5.
- Plate slot A width 0.5.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs all dimensions. The supplied dimensioned drawing and product data were compared with it.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| Base width | 6.313 | 6.3125 (x = +/-3.15625) | Same to rounding. Use the 3D value. |
| Base length | 10.75 | 10.75 | Agree |
| Overall frame height | 11.125 (stated as 11 1/8) | 11.125 | Agree |
| Base thickness, seat height | 2, 2.15 | 2.0, 2.15 | Agree |
| Throat depth | 4 | 4.0 | Agree |
| Head clearance over seat, plate | 6.125, 5.375 | 6.125, 5.375 | Agree |
| Mounting holes | 2 x 0.375 | 2 x 0.375 | Agree |
| Ram section, length, top bore | 1, 9.75, 0.5 | 1.0, 9.75, 0.5 | Agree |
| Plate slot width listed | 0.5 | Slot A = 0.5; three other slots exist | The 3D is the full definition. |
| Maximum stroke | 6.875 | Not a stored quantity. The toothed zone along the ram is 6.9364 long. | Treated as informational. It is not a geometric feature. |
| Colours and finishes | Photos show a blue frame, red knob and handle, bright lever and rim | 3D carries no colour | Section 3 finish column is from the photos. |
| "NO. 1" lettering | Photos show it on the +X side only | Present on both web faces | Follow the 3D: lettering on both faces. |
| Cover plate fasteners | Photos show ordinary fasteners | 3D has heads and short studs only, no holes or shanks | Follow the 3D. |
| Pinion | Photos and function imply a gear | 3D has no teeth, plain cylinders fused to the frame | Follow the 3D. |

**Undetermined, not recoverable from the sources:**
- Pinion tooth geometry, pitch circle and the ram-to-shaft motion ratio. No pinion teeth exist. Rack pitch is 0.26 and rack tip plane is 0.65 from the shaft axis, that is all that is known.
- Rotary plate pivot or retention detail. None exists in the geometry.
- Thread standards of the studs and screws. Only the modelled pitch and profile are known.
- Exact part materials other than cast iron for the frame and steel for the ram.
- How the upper end of the ram travel is limited in use, beyond the cap and head geometry as modelled.
- Internal structure of the handwheel hub connection. Hub and shaft simply overlap as stated.
