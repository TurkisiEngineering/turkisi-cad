# Design specification: panel-mount variable-area gas flowmeter (P25)

A vertical variable-area flowmeter for panel mounting: a case with a window, a clear window tube in front of a glass
flow tube that carries a raised scale, a float ball inside the flow tube, a flow-control valve with a knurled knob on the
front of the lower end, and two threaded fittings with panel nuts on the back. The master is **six solids**. This
document is the only source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** Angles in degrees. (1 in = 25.4 mm.)
- **Global frame (use exactly, no realignment):**
  - **+Y is up** (the flow direction). The case end faces are the planes **y = -2.75** (bottom) and **y = +2.75** (top).
  - **+Z is the front** (the viewer, the knob side); **-Z is the back** (panel side, fittings). The flat case back is
    the plane **z = -0.7**.
  - The **flow-tube axis is the Y axis** (x = 0, z = 0). The case, the window tube and the whole layout are symmetric
    about the plane **x = 0**, except the knob emblem, the scale numerals and the thread phases.
  - The case front round and the window tube share the axis **x = 0, z = 0.075** (parallel to Y).
  - The two fittings stand on the back on axes parallel to Z at **(x, y) = (0, -2.25)** and **(0, +2.25)**; the valve and
    knob sit on the front on the axis parallel to Z at **(x, y) = (0, -2.25)**.
- All six solids are modelled in place in this frame.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Case with valve, knob and the two back fittings (one solid) | custom |
| P02 | 1 | Window tube (clear cover) | custom |
| P03 | 1 | Flow tube with raised graduation marks and numerals | custom |
| P04 | 1 | Float ball | custom |
| H1 | 2 | Hex panel nut (H1-a on the lower fitting, H1-b on the upper fitting) | bought-in |

Contacts (no gaps, no overlaps in the master; all pairwise common volumes are 0): P02 lies in the back trough of P01
(same radius 0.625, same axis) and its two ends touch the inner end faces y = -1.75 and y = +1.75 of P01; the two ends of
P03 touch the same faces; P04 floats free inside the bore of P03; each nut's bore touches the thread crests of its
fitting.

## 3. P01 Case (one solid)

**F1. Main prism.** A prism along Y from y = -2.75 to y = +2.75 whose cross-section in the XZ plane is the union of
- the rectangle x from -0.625 to 0.625, z from -0.7 to 0.075, and
- the circle of radius 0.625 centred (x, z) = (0, 0.075).
So the back is flat (z = -0.7), the sides are flat (x = +-0.625, from z = -0.7 to 0.075) and the front is a half round
of diameter 1.25 (front-most line z = 0.7). Case depth 1.4, width 1.25, height 5.5.

**F2. Window opening.** Between y = -1.75 and y = +1.75 remove the whole circular cylinder of radius 0.625 about the axis
x = 0, z = 0.075. What remains there is the **back spine**: the rectangle part minus that circle, i.e. a concave
trough of radius 0.625 (deepest point z = -0.55 at x = 0, so the spine is 0.15 thick there) whose two edges run out
tangent to the side faces at z = 0.075. The two inner end faces y = -1.75 (facing +Y) and y = +1.75 (facing -Y) are
flat and complete (no holes).

**F3. End chamfers.** On both end faces (y = +-2.75): the edges along the front half round and the two straight side
edges are chamfered **0.05 x 45 deg** (equal legs). The round edge becomes a 45 deg cone from radius 0.575 at the end
face to 0.625 at 0.05 inside; each side edge becomes a 45 deg plane from x = +-0.575 on the end face to y = +-2.70 on the
side face. The back edges (along z = -0.7) are sharp. No other edges of the case are rounded or chamfered.

**F4. Top button.** A plain cylinder of **diameter 0.375**, axis on x = 0, z = 0.075, from y = 2.75 to **y = 2.8125**
(height 0.0625), sharp edges.

**F5. Valve seat cut.** On the front of the lower end block the material above **z = 0.65** is removed for y from -2.5
to -2.0 (a flat seat 0.05 below the front-most line). Beyond y = -2.0 and y = -2.5 the cut boundary rises along two
planes with slope **8 : 15** (dz : dy, 28.07 deg to the seat), outward: the plane through the line (y = -2.0, z = 0.65)
reaches z = 0.7 at y = -1.90625, the plane through (y = -2.5, z = 0.65) reaches z = 0.7 at y = -2.59375. The cut runs
across the whole width; on the round front it is visible only where the round is above z = 0.65 (|x| < 0.24495).

**F6. Valve hex.** A regular hexagonal prism along Z, **0.5 across flats**, centred on (x, y) = (0, -2.25): two flats are
the planes y = -2.0 and y = -2.5, the other four are at +-60 deg to them, the corners lie on the line y = -2.25 at
x = +-0.288675. It runs from **z = 0.65 to z = 0.8375** (height 0.1875), sharp edges. Its bottom is the seat plane;
where the hex corners overhang the falling round (|x| > 0.24495) the underside at z = 0.65 stays open (no fill below).

**F7. Valve stem.** On the same axis (x = 0, y = -2.25): a cylinder **diameter 0.375** from z = 0.8375 to z = 0.9, then
a spindle **diameter 0.125** from z = 0.9 to z = 0.9625 (where the knob starts).

**F8. Knob.** On the same axis: a cylinder **diameter 0.8125** from **z = 0.9625 to z = 1.64** (length 0.6775).
- Front edge chamfer **0.05 x 45 deg**: cone from radius 0.40625 at z = 1.59 to radius 0.35625 at z = 1.64.
- Flat front face z = 1.64 (annulus from radius 0.325 to 0.35625).
- **Front recess:** diameter **0.65**, depth **0.03125**, flat floor at z = 1.60875.
- Back face of the knob (z = 0.9625) flat; all other knob edges sharp.

**F9. Knob knurl: 64 straight V grooves**, parallel to Z, equally spaced at **5.625 deg**: groove centre lines at the
angles k x 5.625 deg (k = 0 ... 63) about the knob axis measured from +X (so grooves point to +X, +Y, -X and -Y).
Each groove is a sharp V: bottom line at radius **0.39125** (depth 0.015), the two flanks are planes at **15 deg** on
either side of the radial plane through the groove centre (30 deg included), width at the surface 0.00804. The grooves
run the full length of the knob from z = 0.9625 and pass out through the front chamfer (they end on the chamfer cone at
z = 1.605). The 64 lands between the grooves are the remaining parts of the diameter 0.8125 cylinder.

**F10. Raised emblem in the recess** (height 0.01: top face z = 1.61875 on the floor z = 1.60875, vertical walls). Its
outline in the XY plane: the half disc of radius **0.2625** centred (0, -2.25) on the side y <= -2.25, minus the disc of
radius **0.169046** centred **(x, y) = (-0.09375, -2.24)**. Result: a crescent; its straight edge on y = -2.25 runs from
x = 0.075 to 0.2625, its two horns meet the y = -2.25 line at x = 0.075 and x = -0.2625.

**F11. Two back fittings** (identical, threads included: the lower one is the upper one translated by -4.5 in Y), on the axes x = 0, y = +-2.25,
parallel to Z, standing on the back face from **z = -0.7 to z = -1.275** (length 0.575):
- end face z = -1.275: flat annulus from radius 0.2025 to 0.23958;
- outer end chamfer 45 deg from radius 0.23958 at z = -1.275 outward until it meets the thread (about radius 0.263 to
  0.272 depending on the thread phase);
- inner countersink 45 deg (90 deg included) from radius 0.2025 at z = -1.275 inward until it meets the inner thread;
- through the fitting a bore with a **flat floor at z = -0.7** (in the plane of the case back; no drill point);
- an **external thread** (F12) on the outside and a **tapered internal pipe thread** (F13) in the bore, both modelled.

**F12. External thread, modelled, 9/16-18 UN form** (right hand, **18 threads per inch**, pitch P = 0.0555556, 60 deg
included flank angle, flanks at 30 deg to the radial direction):
- crest (major) radius **0.28125** (diameter 0.5625), root (minor) radius **0.24517** (diameter 0.49034), thread depth
  0.03608;
- axial lengths per pitch: crest flat **0.00694** (P/8), root flat **0.00694** (P/8), each flank 0.02083;
- runs over the whole fitting length: at the free end it is cut by the 45 deg end chamfer, at the case end it simply
  meets the back face z = -0.7 (no run-out, no undercut);
- **phase:** see the table in F13.

**F13. Internal tapered pipe thread, modelled, 1/8-27 taper-pipe form** (right hand, **27 threads per inch**, pitch
p = 0.0370370, 60 deg, flanks at 30 deg to the radial direction). With d = z + 1.275 = depth below the fitting end face:
- root (major) radius **r = 0.2025 - 0.031135 d** (taper 1.7833 deg on the radius, 1 : 16 on the diameter; Ø0.405 at the
  end face, Ø0.3692 at the floor);
- crest (minor) radius = root radius - **0.02357**;
- axial lengths per pitch: root flat **0.0052**, crest flat **0.00463**, the rest is the two flanks;
- the thread runs from the countersink to the flat floor z = -0.7, which cuts it off.

**Thread phases** (z of the centre of the flat named, plus any integer multiple of the pitch; each value measured in the
half plane that leaves the fitting axis in the stated direction):

| Half plane from the fitting axis | external thread: crest-flat centre at z = | internal thread: root-flat centre at z = |
|---|---|---|
| toward +X | -1.21042 + k x 0.0555556 | -1.24982 + k x 0.0370370 |
| toward +Y | -1.19653 + k x 0.0555556 | -1.24057 + k x 0.0370370 |
| toward -X | -1.18264 + k x 0.0555556 | -1.23130 + k x 0.0370370 |
| toward -Y | -1.16875 + k x 0.0555556 | -1.22205 + k x 0.0370370 |

(k integer; each quarter turn from +X toward +Y adds a quarter pitch: right hand.) The external root flats are centred
half a pitch from the crest flats (for example -1.23819 + k P toward +X). **Both fittings have exactly these phases**:
the lower fitting is the upper one translated by -4.5 in Y.

## 4. P02 Window tube

A plain tube on the axis x = 0, z = 0.075 (parallel to Y): **outer diameter 1.25, inner diameter 1.05**, from
**y = -1.75 to y = 1.75** (length 3.5), flat square ends, no chamfers. Front-most line z = 0.7, back-most z = -0.55.

## 5. P03 Flow tube with scale

**F1. Tube** on the Y axis: **outer diameter 0.25, bore diameter 0.1875**, from **y = -1.75 to y = 1.75** (length 3.5),
flat square ends.

**F2. 20 raised graduation marks.** Each mark is a ring sector standing on the outside of the tube: radius 0.125 to
**0.135** (raised 0.01), **0.01** wide in Y, spanning the angle from -1 rad to +1 rad (+-57.296 deg) about the Y axis
measured from +Z (i.e. centred on the front); its two ends are flat radial planes through the Y axis. The lower faces of
the marks are at **y = -1.5 + k x 0.1584375** (k = 0 ... 19; first -1.5, last 1.5103125), the upper faces 0.01 higher.

**F3. Raised numerals** "0", "10", "20", "30", "40", "50" on the outside of the tube, raised 0.01 (their top surfaces lie
on the radius 0.135, the same as the marks), upright when the tube is viewed from +Z with +Y up. Each numeral sits just
above a mark, left of the front centre line:

| Numeral | above mark k | numeral extent y | extent x |
|---|---|---|---|
| 0 | 0 | -1.4816 to -1.4159 | -0.1058 to -0.0665 |
| 10 | 3 | -1.0063 to -0.9410 | -0.0991 to -0.0225 |
| 20 | 7 | -0.3725 to -0.3073 | -0.1058 to -0.0225 |
| 30 | 11 | 0.2612 to 0.3265 | -0.1058 to -0.0225 |
| 40 | 15 | 0.8950 to 0.9602 | -0.1058 to -0.0225 |
| 50 | 19 | 1.5287 to 1.5940 | -0.1053 to -0.0225 |

Character height about 0.065 (digit cap height), sans-serif upright digits; the exact typeface is undetermined. The
numerals are a region to reproduce in position and size; their glyph outlines need not match exactly.

## 6. P04 Float ball

A sphere of **diameter 0.125** centred at **(0, -1.625, 0)** (inside the flow-tube bore, touching nothing).

## 7. H1 Hex panel nuts (2, identical)

A regular hexagonal nut, **1.0 across flats**, **thickness 0.1875**, plain bore **diameter 0.5625** (no thread modelled).
Orientation like the valve hex: two flats normal to Y (at y = yc +- 0.5), corners on the line y = yc at x = +-0.57735.
Both faces chamfered at the corners: a cone at **30 deg to the face** (60 deg half angle to the nut axis) starting on
the circle of radius 0.5 in each face, so each corner loses 0.0447 of height.
- **H1-a:** axis (x, y) = (0, -2.25), faces z = -0.825 (toward the case) and z = -1.0125.
- **H1-b:** axis (x, y) = (0, +2.25), same z.
The nut faces are 0.125 off the case back (panel gap).

## 8. Acceptance targets

| ID | Name | Volume in3 | Volume mm3 | Area in2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Case | 4.90932 | 80449.41 | 41.2095 | 26586.70 | -0.0001 | -0.1681 | -0.1021 | -0.6250 | 0.6250 | -2.7500 | 2.8125 | -1.2750 | 1.6400 | 379 |
| P02 | Window tube | 1.26449 | 20721.30 | 26.0124 | 16782.15 | 0.0000 | 0.0000 | 0.0750 | -0.6250 | 0.6250 | -1.7500 | 1.7500 | -0.5500 | 0.7000 | 6 |
| P03 | Flow tube with scale | 0.07578 | 1241.83 | 4.9985 | 3224.80 | -0.0001 | 0.0003 | 0.0009 | -0.1250 | 0.1250 | -1.7500 | 1.7500 | -0.1250 | 0.1350 | 240 |
| P04 | Float ball | 0.00102 | 16.76 | 0.0491 | 31.67 | 0.0000 | -1.6250 | 0.0000 | -0.0625 | 0.0625 | -1.6875 | -1.5625 | -0.0625 | 0.0625 | 2 |
| H1-a | Panel nut, lower | 0.11361 | 1861.78 | 2.1347 | 1377.23 | 0.0000 | -2.2500 | -0.9188 | -0.5774 | 0.5774 | -2.7500 | -1.7500 | -1.0125 | -0.8250 | 24 |
| H1-b | Panel nut, upper | 0.11361 | 1861.78 | 2.1347 | 1377.23 | 0.0000 | 2.2500 | -0.9188 | -0.5774 | 0.5774 | 1.7500 | 2.7500 | -1.0125 | -0.8250 | 24 |

Whole assembly: 6.47784 in3 (106152.84 mm3), 76.5388 in2 (49379.79 mm2), CoM (-0.0001, -0.1276, -0.0950), bounding box
X [-0.625, 0.625], Y [-2.75, 2.8125], Z [-1.275, 1.64]. Face counts are those of the master (for information).

Check values: case 1.25 wide, 5.5 high (5.5625 over the top button), 1.4 deep; fittings 4.5 apart, 0.575 long behind
the back; case back to knob front 2.34; knob diameter 0.8125; window tube 1.25 / 1.05; flow tube 0.25 / 0.1875; scale
pitch 0.1584375; nuts 1.0 across flats.

## 9. Source simplifications and undetermined items

- The case is solid: no flow passages between the fittings, the valve and the flow tube, no tube seals, no internal valve
  parts. The fitting bores end flat at the case back. Reproduce exactly that.
- The window tube and the flow tube are separate solid bodies; the float is a plain sphere.
- The nut bores are plain (no thread); the fitting threads are modelled with the phases given.
- The numeral typeface (glyph outlines) is undetermined; position, height and the raised height 0.01 are given.
- Materials (glass flow tube, metal case and fittings, clear window) are product data only and are not modelled.
- Nothing else is undetermined.
