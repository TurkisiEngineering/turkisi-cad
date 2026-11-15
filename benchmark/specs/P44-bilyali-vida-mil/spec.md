# Design specification: hollow ball screw-spline shaft, 10 mm, with flanged ball-screw nut and flanged ball-spline nut

A combined ball screw / ball spline unit as one assembly of **11 separate solids**: a hollow 300 long shaft that
carries both a helical ball groove (lead 15, right-hand) and four straight spline grooves, a flanged ball-screw nut set
(nut body, flange, collar ring, end cap with screws, wiper seal) on the -X side and a flanged ball-spline nut set (nut
body, flange, collar ring, two seals) on the +X side. This document is the only source for the rebuild. Every number
below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: millimetres**, angles in degrees.
- **Global frame (use exactly, no realignment). Every body is modelled in place, each as a separate solid.**
  - **The shaft axis is the X axis**; the shaft runs from x = -150 to x = 150.
  - Angles about the axis ("θ") are measured from **+Y toward +Z**.
  - The ball-screw nut set lies at x -109.5 .. -75, the ball-spline nut set at x 75 .. 108.
- Section notation: "loop" = closed outline; "–" joins points by a straight line; "arc cC RR via M" = circular arc of
  radius R about C through M; "blend curve via M" = free-form transition through M. Axial sections are given in a
  half-plane at angle θ in (x, r) with r the distance from the axis (negative r = the opposite half-plane, θ + 180).
  Face lists: "plane n(a, b, c), n·p = d" is a·x + b·y + c·z = d; cylinders / cones give axis direction, a point on the
  axis and radius; "extent" is the face's bounding box.

## 2. Product description and source simplifications

- The **shaft** (P01) is hollow (bore 4) and carries the ball groove over 270 from its -X end plus four spline grooves
  over its whole length.
- **Ball-screw nut set** (x < 0): nut body P02, flange P03, collar ring P04, end cap P05 (with four cap screws merged
  into it), wiper seal P06 (with four cap screw heads merged into it).
- **Ball-spline nut set** (x > 0): nut body P07 with four tapped holes, flange P08, collar ring P09, seals P10-a, P10-b.
- Simplifications of the source to reproduce: no balls, no ball tracks inside the nuts (the nut bores are plain R5),
  the screws are part of P05 / P06 (not separate bodies), the screw shanks of P05 overlap P02 (section 5). Threads that
  ARE modelled: the shaft ball groove, the M3 threads of P05's screws and P07's tapped holes.
- The original file has 11 solids and 18 empty shells (dropped; do not model them).

## 3. Part list

10 distinct parts, **11 bodies** (P10 twice).

| ID | Name | Count | Faces | Volume (mm³) | Area (mm²) |
|---|---|---|---|---|---|
| P01 | Hollow ball screw-spline shaft | 1 | 230 | 18793.197 | 13857.103 |
| P02 | Ball-screw nut body | 1 | 37 | 10475.776 | 4671.521 |
| P03 | Ball-screw nut flange | 1 | 59 | 5505.290 | 4491.745 |
| P04 | Ball-screw nut collar ring | 1 | 6 | 1548.783 | 1963.370 |
| P05 | Ball-screw nut end cap (with four cap screws) | 1 | 174 | 975.653 | 1503.736 |
| P06 | Ball-screw nut wiper seal (with four cap screw heads) | 1 | 127 | 1225.284 | 1217.856 |
| P07 | Ball-spline nut body | 1 | 137 | 12409.652 | 4787.273 |
| P08 | Ball-spline nut flange | 1 | 57 | 5845.289 | 4535.377 |
| P09 | Ball-spline nut collar ring | 1 | 6 | 1380.039 | 1777.388 |
| P10 | Ball-spline seal (2 identical bodies) | 2 | 13 | 67.567 | 200.205 |

## 4. Part geometry

### P01 Hollow ball screw-spline shaft (230 faces)

A straight hollow shaft on the X axis, x = -150 .. 150 (length 300), outer diameter 10 (cylinder R5), through bore diameter 4 (R2). Both ends are planes x = ±150 with a 0.25 x 45 deg chamfer on the outer edge (cone from R5 at x = ±149.75 to R4.75 at x = ±150) and on the bore edge (R2 at x = ±149.75 to R2.25 at x = ±150).  **Spline grooves (4):** circular grooves R1.24, straight along X over the whole length (open at both ends). Their axes are parallel to X at radius 5.8 from the shaft axis, at the angles 60, 120, 240 and 300 deg measured from +Y toward +Z: (y, z) = (2.9, 5.0229), (-2.9, 5.0229), (-2.9, -5.0231), (2.9, -5.0231). Each groove is the shaft minus a cylinder R1.24 about its axis (groove bottom at radius 4.56, depth 0.44).  **Helical ball groove (1, right-hand, lead 15):** in every axial half-plane the groove is a circular arc R0.7075 whose centre lies at radius 5.0075 (0.0075 outside the shaft surface), so the groove bottom is at radius 4.3 (depth 0.7) and its width at the surface is 1.415. Angle θ is measured from +Y toward +Z (right-hand about +X); the arc centre lies at x = 15·θ/360 + 15·k (k integer), i.e. at x = 0 the groove bottom is on +Y, at θ = 30 deg the centres are at x = 1.25 + 15k. The groove starts at the end x = -150: the sweep begins in the half-plane θ = 0 (y > 0, z = 0) with the profile centre at x = -150 and is cut off flat by that half-plane (a small planar face z = 0, x -150 .. -149.29, y 4.3 .. 5); it continues for about 18 turns and runs out at x = 121.65 (last full-depth crossing at x = 113.75 on θ = 210 deg; the run-out shape near x = 121 is a free-form transition, see section 6). The groove is one continuous helical surface; where it crosses the spline grooves both cuts are simply combined.

Cross-section at x = 0 (coordinates y, z):
  - loop: (0, 2) – arc c(0, 0) R2 via (-2, 0) – (0, -2) – arc c(0, 0) R2 via (2, 0) – (0, 2)
  - loop: (2.9, 3.7829) – arc c(2.9, 5.0229) R1.24 via (3.0615, 3.7935) – (3.2202, 3.825) – arc c(0, 0) R5 via (4.1726, 2.7549) – (4.7825, 1.4586) – blend curve via (4.3, 0) – (4.7825, -1.4586) – arc c(0, 0) R5 via (4.1726, -2.7549) – (3.2201, -3.8251) – arc c(2.9, -5.0231) R1.24 via (2.28, -3.9492) – (1.7025, -4.7012) – arc c(0, 0) R5 via (0.8643, -4.9247) – (0, -5) – arc c(0, 0) R5 via (-0.8643, -4.9247) – (-1.7025, -4.7012) – arc c(-2.9, -5.0231) R1.24 via (-2.28, -3.9492) – (-3.2201, -3.8251) – arc c(0, 0) R5 via (-5, -0.0001) – (-3.2202, 3.825) – arc c(-2.9, 5.0229) R1.24 via (-3.0615, 3.7935) – (-2.9, 3.7829) – arc c(-2.9, 5.0229) R1.24 via (-2.1455, 4.0389) – (-1.7025, 4.7012) – arc c(0, 0) R5 via (0, 5) – (1.7025, 4.7012) – arc c(2.9, 5.0229) R1.24 via (2.1455, 4.0389) – (2.9, 3.7829)
Cross-section at x = 130 (coordinates y, z):
  - loop: (0, 2) – arc c(0, 0) R2 via (-2, 0) – (0, -2) – arc c(0, 0) R2 via (2, 0) – (0, 2)
  - loop: (2.9, 3.7829) – arc c(2.9, 5.0229) R1.24 via (3.0615, 3.7935) – (3.2202, 3.825) – arc c(0, 0) R5 via (5, -0.0001) – (3.2201, -3.8251) – arc c(2.9, -5.0231) R1.24 via (2.28, -3.9492) – (1.7025, -4.7012) – arc c(0, 0) R5 via (0.8643, -4.9247) – (0, -5) – arc c(0, 0) R5 via (-0.8643, -4.9247) – (-1.7025, -4.7012) – arc c(-2.9, -5.0231) R1.24 via (-2.28, -3.9492) – (-3.2201, -3.8251) – arc c(0, 0) R5 via (-5, -0.0001) – (-3.2202, 3.825) – arc c(-2.9, 5.0229) R1.24 via (-3.0615, 3.7935) – (-2.9, 3.7829) – arc c(-2.9, 5.0229) R1.24 via (-2.1455, 4.0389) – (-1.7025, 4.7012) – arc c(0, 0) R5 via (0, 5) – (1.7025, 4.7012) – arc c(2.9, 5.0229) R1.24 via (2.1455, 4.0389) – (2.9, 3.7829)

### P02 Ball-screw nut body (37 faces)

Turned sleeve on the shaft: bore R5 (x -104.5 .. -79.1), outer steps R13 / R12.65 / R11.5 as the half-section shows, with 0.25 / 0.2 / 0.35 chamfers. Four axial blind holes diameter 3 (R1.5) on a circle of radius 9 at 0, 90, 180 and 270 deg (on +Y, +Z, -Y, -Z), from the step face x = -104.5 to a flat bottom at x = -98.4. No ball track is modelled inside the nut.

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (-91, 12.75) – (-91.25, 13) – (-100.9, 13) – (-100.9, 12.65) – (-102.15, 12.65) – (-102.5, 13) – (-109.3, 13) – (-109.5, 12.8) – (-109.5, 11.5) – (-104.5, 11.5) – (-104.5, 5) – (-79.1, 5) – (-79.1, 11.3) – (-79.3, 11.5) – (-91, 11.5) – (-91, 12.75)
  - loop: (-109.5, -11.5) – (-104.5, -11.5) – (-104.5, -5) – (-79.1, -5) – (-79.1, -11.3) – (-79.3, -11.5) – (-91, -11.5) – (-91, -12.75) – (-91.25, -13) – (-100.9, -13) – (-100.9, -12.65) – (-102.15, -12.65) – (-102.5, -13) – (-109.3, -13) – (-109.5, -12.8) – (-109.5, -11.5)
Cross-section at x = -101 (coordinates y, z):
  - loop: (1.5, -9) – arc c(0, -9) R1.5 via (0, -10.5) – (-1.5, -9) – arc c(0, -9) R1.5 via (0, -7.5) – (1.5, -9)
  - loop: (10.5, 0) – arc c(9, 0) R1.5 via (9, -1.5) – (7.5, 0) – arc c(9, 0) R1.5 via (9, 1.5) – (10.5, 0)
  - loop: (1.5, 9) – arc c(0, 9) R1.5 via (0, 7.5) – (-1.5, 9) – arc c(0, 9) R1.5 via (0, 10.5) – (1.5, 9)
  - loop: (-7.5, 0) – arc c(-9, 0) R1.5 via (-9, -1.5) – (-10.5, 0) – arc c(-9, 0) R1.5 via (-9, 1.5) – (-7.5, 0)
  - loop: (12.65, 0) – arc c(0, 0) R12.65 via (0, 12.65) – (-12.65, 0) – arc c(0, 0) R12.65 via (0, -12.65) – (12.65, 0)
  - loop: (-5, 0) – arc c(0, 0) R5 via (0, -5) – (5, 0) – arc c(0, 0) R5 via (0, 5) – (-5, 0)
Faces that are not surfaces of revolution about the X axis (8):
  - cylinder axis dir(-1, 0, 0) through (-101.45, 0, -9) R1.5; extent (-104.5, -1.5, -10.5)..(-98.4, 1.5, -9)
  - cylinder axis dir(-1, 0, 0) through (-101.45, 9, 0) R1.5; extent (-104.5, 7.5, -1.5)..(-98.4, 10.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-101.45, 0, 9) R1.5; extent (-104.5, -1.5, 7.5)..(-98.4, 1.5, 9)
  - cylinder axis dir(-1, 0, 0) through (-101.45, -9, 0) R1.5; extent (-104.5, -10.5, -1.5)..(-98.4, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-101.45, -9, 0) R1.5; extent (-104.5, -10.5, 0)..(-98.4, -7.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-101.45, 0, 9) R1.5; extent (-104.5, -1.5, 9)..(-98.4, 1.5, 10.5)
  - cylinder axis dir(-1, 0, 0) through (-101.45, 9, 0) R1.5; extent (-104.5, 7.5, 0)..(-98.4, 10.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-101.45, 0, -9) R1.5; extent (-104.5, -1.5, -9)..(-98.4, 1.5, -7.5)

### P03 Ball-screw nut flange (59 faces)

Flange ring, diameter 48, 3 thick (x -101.5 .. -98.5) with a hub to x = -91; bore R14.9; a circumferential groove R1 (centre (x, r) = (-95.004, 18.5)) and a step R17.8 on the hub. Four through holes diameter 3.4 (R1.7) on the 42 bolt circle at 0, 90, 180, 270 deg, each with a small 45 deg chamfer at both faces (cones as listed). One radial lubrication hole diameter 0.9 along Z on the +Z side at x = -95.004, from the groove bottom (r 17.5) into the bore, with two free-form blends where it meets the bore.

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (-95.004, 17.5) – arc c(-95.004, 18.5) R1 via (-94.5036, 17.6342) – (-94.1379, 18) – (-91.8, 18) – arc c(-91.8, 17.2) R0.8 via (-91.2345, 17.7658) – (-91, 17.2) – (-91, 15.15) – (-91.25, 14.9) – (-101.25, 14.9) – (-101.5, 15.15) – (-101.5, 23.7) – (-101.2, 24) – (-98.8, 24) – (-98.5, 23.7) – (-98.5, 18) – arc c(-98.3, 18) R0.2 via (-98.4423, 17.8595) – (-98.3, 17.8) – (-97.8925, 17.8) – (-97.5, 18) – (-95.87, 18) – arc c(-95.004, 18.5) R1 via (-95.5042, 17.6341) – (-95.004, 17.5)
  - loop: (-94.1379, -18) – arc c(-95.004, -18.5) R1 via (-94.5039, -17.634) – (-95.004, -17.5) – arc c(-95.004, -18.5) R1 via (-95.5041, -17.634) – (-95.87, -18) – (-97.5, -18) – (-97.8925, -17.8) – (-98.3, -17.8) – arc c(-98.3, -18) R0.2 via (-98.4416, -17.8587) – (-98.5, -18) – (-98.5, -23.7) – (-98.8, -24) – (-101.2, -24) – (-101.5, -23.7) – (-101.5, -15.15) – (-101.25, -14.9) – (-91.25, -14.9) – (-91, -15.15) – (-91, -17.2) – arc c(-91.8, -17.2) R0.8 via (-91.2342, -17.7656) – (-91.8, -18) – (-94.1379, -18)
Faces that are not surfaces of revolution about the X axis (28):
  - free-form (blend) face; extent (-95.704, 0, 14.8841)..(-94.304, 0.6884, 15.15)
  - cone axis dir(-1, 0, 0) through (-101.375, 21, 0) R1.7, half-angle 45 deg; extent (-101.5, 19.05, -1.95)..(-101.25, 21, 1.95)
  - cone axis dir(1, 0, 0) through (-98.625, 21, 0) R1.95, half-angle 45 deg; extent (-98.75, 19.05, -1.95)..(-98.5, 21, 1.95)
  - cone axis dir(-1, 0, 0) through (-101.375, 0, 21) R1.7, half-angle 45 deg; extent (-101.5, -1.95, 19.05)..(-101.25, 1.95, 21)
  - cone axis dir(1, 0, 0) through (-98.625, 0, 21) R1.95, half-angle 45 deg; extent (-98.75, -1.95, 19.05)..(-98.5, 1.95, 21)
  - cone axis dir(-1, 0, 0) through (-101.375, -21, 0) R1.7, half-angle 45 deg; extent (-101.5, -22.95, -1.95)..(-101.25, -21, 1.95)
  - cone axis dir(1, 0, 0) through (-98.625, -21, 0) R1.95, half-angle 45 deg; extent (-98.75, -22.95, -1.95)..(-98.5, -21, 1.95)
  - cone axis dir(-1, 0, 0) through (-101.375, 0, -21) R1.7, half-angle 45 deg; extent (-101.5, -1.95, -22.95)..(-101.25, 1.95, -21)
  - cone axis dir(1, 0, 0) through (-98.625, 0, -21) R1.95, half-angle 45 deg; extent (-98.75, -1.95, -22.95)..(-98.5, 1.95, -21)
  - cylinder axis dir(-1, 0, 0) through (-100, 21, 0) R1.7; extent (-101.25, 19.3, -1.7)..(-98.75, 22.7, 0)
  - cylinder axis dir(-1, 0, 0) through (-100, 0, 21) R1.7; extent (-101.25, -1.7, 19.3)..(-98.75, 1.7, 21)
  - cylinder axis dir(-1, 0, 0) through (-100, -21, 0) R1.7; extent (-101.25, -22.7, -1.7)..(-98.75, -19.3, 0)
  - cylinder axis dir(-1, 0, 0) through (-100, 0, -21) R1.7; extent (-101.25, -1.7, -22.7)..(-98.75, 1.7, -21)
  - cylinder axis dir(0, 0, -1) through (-95.004, 0, 16.3704) R0.45; extent (-95.454, -0.45, 15.1338)..(-94.554, 0, 17.607)
  - cylinder axis dir(0, 0, -1) through (-95.004, 0, 16.3704) R0.45; extent (-95.454, 0, 15.1338)..(-94.554, 0.45, 17.607)
  - free-form (blend) face; extent (-95.704, -0.6884, 14.8841)..(-94.304, 0.0007, 15.15)
  - cylinder axis dir(-1, 0, 0) through (-100, 0, -21) R1.7; extent (-101.25, -1.7, -21)..(-98.75, 1.7, -19.3)
  - cylinder axis dir(-1, 0, 0) through (-100, -21, 0) R1.7; extent (-101.25, -22.7, 0)..(-98.75, -19.3, 1.7)
  - cylinder axis dir(-1, 0, 0) through (-100, 0, 21) R1.7; extent (-101.25, -1.7, 21)..(-98.75, 1.7, 22.7)
  - cylinder axis dir(-1, 0, 0) through (-100, 21, 0) R1.7; extent (-101.25, 19.3, 0)..(-98.75, 22.7, 1.7)
  - cone axis dir(1, 0, 0) through (-98.625, 0, -21) R1.95, half-angle 45 deg; extent (-98.75, -1.95, -21)..(-98.5, 1.95, -19.05)
  - cone axis dir(-1, 0, 0) through (-101.375, 0, -21) R1.7, half-angle 45 deg; extent (-101.5, -1.95, -21)..(-101.25, 1.95, -19.05)
  - cone axis dir(1, 0, 0) through (-98.625, -21, 0) R1.95, half-angle 45 deg; extent (-98.75, -21, -1.95)..(-98.5, -19.05, 1.95)
  - cone axis dir(-1, 0, 0) through (-101.375, -21, 0) R1.7, half-angle 45 deg; extent (-101.5, -21, -1.95)..(-101.25, -19.05, 1.95)
  - cone axis dir(1, 0, 0) through (-98.625, 0, 21) R1.95, half-angle 45 deg; extent (-98.75, -1.95, 21)..(-98.5, 1.95, 22.95)
  - cone axis dir(-1, 0, 0) through (-101.375, 0, 21) R1.7, half-angle 45 deg; extent (-101.5, -1.95, 21)..(-101.25, 1.95, 22.95)
  - cone axis dir(1, 0, 0) through (-98.625, 21, 0) R1.95, half-angle 45 deg; extent (-98.75, 21, -1.95)..(-98.5, 22.95, 1.95)
  - cone axis dir(-1, 0, 0) through (-101.375, 21, 0) R1.7, half-angle 45 deg; extent (-101.5, 21, -1.95)..(-101.25, 22.95, 1.95)

### P04 Ball-screw nut collar ring (6 faces)

Plain ring: inner R13, outer R14.9, x -100.9 .. -91.6 (no chamfers).

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (-91.6, 14.9) – (-100.9, 14.9) – (-100.9, 13) – (-91.6, 13) – (-91.6, 14.9)
  - loop: (-91.6, -13) – (-100.9, -13) – (-100.9, -14.9) – (-91.6, -14.9) – (-91.6, -13)

### P05 Ball-screw nut end cap (with four cap screws) (174 faces)

End cap of the ball-screw nut, one solid that also contains four cap screws: a ring (x -108 .. -104.5, bore R5, outer R11.25) with four counterbores for the screw heads at radius 9 (0, 90, 180, 270 deg), hexagon sockets 1.5 across flats, and the four screw shanks (thread M3 x 0.5 modelled as a helical V groove: crest R1.5, root R1.1752, x -104.7 .. -100.68) that reach into the holes of P02 (overlap, section 5). Two ball return channels at 45 and 225 deg (radius 9 from the axis: centres (y, z) = (6.364, 6.364) and (-6.364, -6.364)) with R2.25 / R1.9 recesses, spheres and tori as listed. Build it from the sections and the complete face list.

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (-104.75, -5) – (-104.5, -5.25) – (-104.5, -11.25) – (-105.5, -11.25) – (-105.5, -10.9) – (-107.15, -10.9) – arc c(-107.15, -10.65) R0.25 via (-107.3266, -10.827) – (-107.4, -10.65) – (-107.4, -9.866) – (-107.3104, -9.7765) – (-105.9, -9.7765) – (-105.9, -8.2235) – (-107.3104, -8.2235) – (-107.4, -8.134) – (-107.4, -7.35) – arc c(-107.15, -7.35) R0.25 via (-107.327, -7.1734) – (-107.15, -7.1) – (-105.5, -7.1) – (-105.5, -6.75) – (-107.75, -6.75) – arc c(-107.75, -6.5) R0.25 via (-107.9272, -6.6763) – (-108, -6.5) – (-108, -5.25) – (-107.75, -5) – (-104.75, -5)
  - loop: (-107.15, 10.9) – arc c(-107.15, 10.65) R0.25 via (-107.327, 10.8266) – (-107.4, 10.65) – (-107.4, 9.866) – (-107.3104, 9.7765) – (-105.9, 9.7765) – (-105.9, 8.2235) – (-107.3104, 8.2235) – (-107.4, 8.134) – (-107.4, 7.35) – arc c(-107.15, 7.35) R0.25 via (-107.3266, 7.173) – (-107.15, 7.1) – (-105.5, 7.1) – (-105.5, 6.75) – (-107.75, 6.75) – arc c(-107.75, 6.5) R0.25 via (-107.927, 6.6765) – (-108, 6.5) – (-108, 5.25) – (-107.75, 5) – (-104.75, 5) – (-104.5, 5.25) – (-104.5, 11.25) – (-105.5, 11.25) – (-105.5, 10.9) – (-107.15, 10.9)
Axial section in the half-plane at 0 deg (coordinates x, r; negative r = the opposite half-plane at 180 deg):
  - loop: (-107.8, 7.3) – (-108, 7.1) – (-108, 5.25) – (-107.75, 5) – (-104.75, 5) – (-104.5, 5.25) – (-104.5, 7.25) – (-102.5, 7.25) – (-102.5, 7.473) – (-102.4344, 7.4729) – (-102.6375, 7.8248) – (-102.7, 7.8248) – (-102.8875, 7.5) – (-102.95, 7.5) – (-103.1375, 7.8248) – (-103.2, 7.8248) – (-103.3875, 7.5) – (-103.45, 7.5) – (-103.6375, 7.8248) – (-103.7, 7.8248) – (-103.8875, 7.5) – (-103.95, 7.5) – (-104.0781, 7.7219) – (-104.3, 7.5) – (-104.7, 7.5) – (-104.7, 7.3) – (-107.8, 7.3)
  - loop: (-107.8, -10.7) – (-108, -10.9) – (-108, -11) – arc c(-107.75, -11) R0.25 via (-107.9268, -11.1768) – (-107.75, -11.25) – (-104.5, -11.25) – (-104.5, -10.75) – (-102.5, -10.75) – (-102.5, -10.527) – (-102.1844, -10.5271) – (-102.3875, -10.1752) – (-102.45, -10.1752) – (-102.6375, -10.5) – (-102.7, -10.5) – (-102.8875, -10.1752) – (-102.95, -10.1752) – (-103.1375, -10.5) – (-103.2, -10.5) – (-103.3875, -10.1752) – (-103.45, -10.1752) – (-103.6375, -10.5) – (-103.7, -10.5) – (-103.8875, -10.1752) – (-103.95, -10.1752) – (-104.1375, -10.5) – (-104.2, -10.5) – (-104.2366, -10.4366) – (-104.3, -10.5) – (-104.7, -10.5) – (-104.7, -10.7) – (-107.8, -10.7)
  - loop: (-103.7, -7.8248) – (-103.8875, -7.5) – (-103.95, -7.5) – (-104.0781, -7.7219) – (-104.3, -7.5) – (-104.7, -7.5) – (-104.7, -7.3) – (-107.8, -7.3) – (-108, -7.1) – (-108, -5.25) – (-107.75, -5) – (-104.75, -5) – (-104.5, -5.25) – (-104.5, -7.25) – (-102.5, -7.25) – (-102.5, -7.473) – (-102.4344, -7.4729) – (-102.6375, -7.8248) – (-102.7, -7.8248) – (-102.8875, -7.5) – (-102.95, -7.5) – (-103.1375, -7.8248) – (-103.2, -7.8248) – (-103.3875, -7.5) – (-103.45, -7.5) – (-103.6375, -7.8248) – (-103.7, -7.8248)
  - loop: (-102.2, -7.8248) – (-102.4031, -7.4729) – (-101.9344, -7.4729) – (-102.1375, -7.8248) – (-102.2, -7.8248)
  - loop: (-101.95, -10.1752) – (-102.1531, -10.5271) – (-101.6844, -10.5271) – (-101.8875, -10.1752) – (-101.95, -10.1752)
  - loop: (-101.7, -7.8248) – (-101.9031, -7.4729) – (-101.4344, -7.4729) – (-101.6375, -7.8248) – (-101.7, -7.8248)
  - loop: (-101.45, -10.1752) – (-101.6531, -10.5271) – (-101.1844, -10.5271) – (-101.3875, -10.1752) – (-101.45, -10.1752)
  - loop: (-101.2, -7.8248) – (-101.4031, -7.4729) – (-100.9344, -7.4729) – (-101.1375, -7.8248) – (-101.2, -7.8248)
  - loop: (-103.95, 10.1752) – (-104.1375, 10.5) – (-104.2, 10.5) – (-104.2366, 10.4366) – (-104.3, 10.5) – (-104.7, 10.5) – (-104.7, 10.7) – (-107.8, 10.7) – (-108, 10.9) – (-108, 11) – arc c(-107.75, 11) R0.25 via (-107.9268, 11.1768) – (-107.75, 11.25) – (-104.5, 11.25) – (-104.5, 10.75) – (-102.5, 10.75) – (-102.5, 10.527) – (-102.1844, 10.5271) – (-102.3875, 10.1752) – (-102.45, 10.1752) – (-102.6375, 10.5) – (-102.7, 10.5) – (-102.8875, 10.1752) – (-102.95, 10.1752) – (-103.1375, 10.5) – (-103.2, 10.5) – (-103.3875, 10.1752) – (-103.45, 10.1752) – (-103.6375, 10.5) – (-103.7, 10.5) – (-103.8875, 10.1752) – (-103.95, 10.1752)
  - loop: (-102.2, 7.8248) – (-102.4031, 7.4729) – (-101.9344, 7.4729) – (-102.1375, 7.8248) – (-102.2, 7.8248)
  - loop: (-101.95, 10.1752) – (-102.1531, 10.5271) – (-101.6844, 10.5271) – (-101.8875, 10.1752) – (-101.95, 10.1752)
  - loop: (-101.7, 7.8248) – (-101.9031, 7.4729) – (-101.4344, 7.4729) – (-101.6375, 7.8248) – (-101.7, 7.8248)
  - loop: (-101.45, 10.1752) – (-101.6531, 10.5271) – (-101.1844, 10.5271) – (-101.3875, 10.1752) – (-101.45, 10.1752)
  - loop: (-101.2, 7.8248) – (-101.4031, 7.4729) – (-100.9344, 7.4729) – (-101.1375, 7.8248) – (-101.2, 7.8248)
  - loop: (-100.95, -10.1752) – (-101.1531, -10.5271) – (-100.6844, -10.5271) – (-100.8875, -10.1752) – (-100.95, -10.1752)
  - loop: (-100.95, 10.1752) – (-101.1531, 10.5271) – (-100.6844, 10.5271) – (-100.8875, 10.1752) – (-100.95, 10.1752)
Cross-section at x = -107 (coordinates y, z):
  - loop: (-5.9388, -9.5547) – arc c(-5.8069, -9.3424) R0.25 via (-6.0254, -9.4639) – (-6.0569, -9.3424) – arc c(-5.8069, -9.3424) R0.25 via (-6.0378, -9.2467) – (-5.9836, -9.1656) – (-4.773, -7.955) – arc c(-6.364, -6.364) R2.25 via (-4.773, -4.773) – (-7.955, -4.773) – (-9.1656, -5.9836) – arc c(-9.3424, -5.8069) R0.25 via (-9.371, -6.0552) – (-9.5547, -5.9388) – arc c(0, 0) R11.25 via (-10.8179, -3.088) – (-11.25, 0) – arc c(0, 0) R11.25 via (-5.4658, 9.833) – (5.9388, 9.5547) – arc c(5.8069, 9.3424) R0.25 via (6.0552, 9.371) – (5.9836, 9.1656) – (4.773, 7.955) – arc c(6.364, 6.364) R2.25 via (4.2852, 7.225) – (4.114, 6.364) – arc c(6.364, 6.364) R2.25 via (5.5029, 4.2852) – (7.955, 4.773) – (9.1656, 5.9836) – arc c(9.3424, 5.8069) R0.25 via (9.371, 6.0552) – (9.5547, 5.9388) – arc c(0, 0) R11.25 via (10.8179, 3.088) – (11.25, 0) – arc c(0, 0) R11.25 via (5.4658, -9.833) – (-5.9388, -9.5547)
  - loop: (8.264, 6.364) – arc c(6.364, 6.364) R1.9 via (6.364, 8.264) – (4.464, 6.364) – arc c(6.364, 6.364) R1.9 via (6.364, 4.464) – (8.264, 6.364)
  - loop: (-4.464, -6.364) – arc c(-6.364, -6.364) R1.9 via (-6.364, -4.464) – (-8.264, -6.364) – arc c(-6.364, -6.364) R1.9 via (-6.364, -8.264) – (-4.464, -6.364)
  - loop: (-7.3, 0) – arc c(-9, 0) R1.7 via (-9, -1.7) – (-10.7, 0) – arc c(-9, 0) R1.7 via (-9, 1.7) – (-7.3, 0)
  - loop: (1.7, 9) – arc c(0, 9) R1.7 via (0, 7.3) – (-1.7, 9) – arc c(0, 9) R1.7 via (0, 10.7) – (1.7, 9)
  - loop: (10.7, 0) – arc c(9, 0) R1.7 via (9, -1.7) – (7.3, 0) – arc c(9, 0) R1.7 via (9, 1.7) – (10.7, 0)
  - loop: (1.7, -9) – arc c(0, -9) R1.7 via (0, -10.7) – (-1.7, -9) – arc c(0, -9) R1.7 via (0, -7.3) – (1.7, -9)
  - loop: (5, 0) – arc c(0, 0) R5 via (0, -5) – (-5, 0) – arc c(0, 0) R5 via (0, 5) – (5, 0)
  - loop: (-5.9309, -5.614) – (-5.4979, -6.364) – (-5.9309, -7.114) – (-6.797, -7.114) – (-7.23, -6.364) – (-6.797, -5.614) – (-5.9309, -5.614)
  - loop: (5.9309, 7.114) – (6.797, 7.114) – (7.23, 6.364) – (6.797, 5.614) – (5.9309, 5.614) – (5.4979, 6.364) – (5.9309, 7.114)
Cross-section at x = -104 (coordinates y, z):
  - loop: (-10.75, 0) – arc c(-9, 0) R1.75 via (-9, 1.75) – (-7.25, 0) – arc c(-9, 0) R1.75 via (-9, -1.75) – (-10.75, 0)
  - loop: (-1.75, -9) – arc c(0, -9) R1.75 via (0, -7.25) – (1.75, -9) – arc c(0, -9) R1.75 via (0, -10.75) – (-1.75, -9)
  - loop: (7.25, 0) – arc c(9, 0) R1.75 via (9, 1.75) – (10.75, 0) – arc c(9, 0) R1.75 via (9, -1.75) – (7.25, 0)
  - loop: (-1.75, 9) – arc c(0, 9) R1.75 via (0, 10.75) – (1.75, 9) – arc c(0, 9) R1.75 via (0, 7.25) – (-1.75, 9)
  - loop: (7.7825, 0.8761) – arc c(9, 0) R1.5 via (8.2175, 1.2797) – (8.775, 1.483) – blend curve via (10.0872, 0.8004) – (10.0795, -0.5241) – arc c(9, 0) R1.2 via (9.6258, -1.0239) – (8.9741, -1.1997) – blend curve via (7.792, -0.6027) – (7.7825, 0.8761)
  - loop: (0.8761, -7.7825) – arc c(0, -9) R1.5 via (1.2797, -8.2175) – (1.483, -8.775) – blend curve via (0.8004, -10.0872) – (-0.5241, -10.0795) – arc c(0, -9) R1.2 via (-1.0239, -9.6258) – (-1.1997, -8.9741) – blend curve via (-0.6027, -7.792) – (0.8761, -7.7825)
  - loop: (-7.7825, -0.8761) – arc c(-9, 0) R1.5 via (-8.2175, -1.2797) – (-8.775, -1.483) – blend curve via (-10.0872, -0.8004) – (-10.0795, 0.5241) – arc c(-9, 0) R1.2 via (-9.6258, 1.0239) – (-8.9741, 1.1997) – blend curve via (-7.792, 0.6027) – (-7.7825, -0.8761)
  - loop: (-0.8761, 7.7825) – arc c(0, 9) R1.5 via (-1.2797, 8.2175) – (-1.483, 8.775) – blend curve via (-0.8004, 10.0872) – (0.5241, 10.0795) – arc c(0, 9) R1.2 via (1.0239, 9.6258) – (1.1997, 8.9741) – blend curve via (0.6027, 7.792) – (-0.8761, 7.7825)
Cross-section at x = -101.5 (coordinates y, z):
  - loop: (0.6865, 9.9539) – blend curve via (-0.8112, 10.0808) – (-1.4375, 8.4846) – arc c(0, 9) R1.5271 via (1.3001, 9.8011) – (-1.1115, 7.9529) – blend curve via (0.5935, 7.7862) – (1.1619, 9.1763) – arc c(0, 9) R1.1752 via (1.0005, 9.6165) – (0.6865, 9.9539)
  - loop: (-9.9539, 0.6865) – blend curve via (-10.0808, -0.8112) – (-8.4846, -1.4375) – arc c(-9, 0) R1.5271 via (-9.8011, 1.3001) – (-7.9529, -1.1115) – blend curve via (-7.7862, 0.5935) – (-9.1763, 1.1619) – arc c(-9, 0) R1.1752 via (-9.6165, 1.0005) – (-9.9539, 0.6865)
  - loop: (-0.6865, -9.9539) – blend curve via (0.8112, -10.0808) – (1.4375, -8.4846) – arc c(0, -9) R1.5271 via (-1.3001, -9.8011) – (1.1115, -7.9529) – blend curve via (-0.5935, -7.7862) – (-1.1619, -9.1763) – arc c(0, -9) R1.1752 via (-1.0005, -9.6165) – (-0.6865, -9.9539)
  - loop: (9.9539, -0.6865) – blend curve via (10.0808, 0.8112) – (8.4846, 1.4375) – arc c(9, 0) R1.5271 via (9.8011, -1.3001) – (7.9529, 1.1115) – blend curve via (7.7862, -0.5935) – (9.1763, -1.1619) – arc c(9, 0) R1.1752 via (9.6165, -1.0005) – (9.9539, -0.6865)
Complete face list (174):
  - cylinder axis dir(-1, 0, 0) through (-103.5, -9, 0) R1.75; extent (-104.5, -10.75, 0)..(-102.5, -7.25, 1.75)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 0, -9) R1.75; extent (-104.5, -1.75, -9)..(-102.5, 1.75, -7.25)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 9, 0) R1.75; extent (-104.5, 7.25, 0)..(-102.5, 10.75, 1.75)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 0, 9) R1.75; extent (-104.5, -1.75, 9)..(-102.5, 1.75, 10.75)
  - cone axis dir(-1, 0, 0) through (-107.9, 0, 9) R1.7, half-angle 45 deg; extent (-108, -1.9, 7.1)..(-107.8, 1.9, 9)
  - cone axis dir(-1, 0, 0) through (-107.9, 9, 0) R1.7, half-angle 45 deg; extent (-108, 7.1, -1.9)..(-107.8, 9, 1.9)
  - cone axis dir(-1, 0, 0) through (-107.9, 0, -9) R1.7, half-angle 45 deg; extent (-108, -1.9, -10.9)..(-107.8, 1.9, -9)
  - cone axis dir(-1, 0, 0) through (-107.9, -9, 0) R1.7, half-angle 45 deg; extent (-108, -10.9, -1.9)..(-107.8, -9, 1.9)
  - cone axis dir(1, 0, 0) through (-104.625, 0, 0) R5.25, half-angle 45 deg; extent (-104.75, -5.25, -5.25)..(-104.5, 5.25, 0)
  - cone axis dir(-1, 0, 0) through (-107.875, 0, 0) R5, half-angle 45 deg; extent (-108, -5.25, -5.25)..(-107.75, 5.25, 0)
  - torus axis dir(1, 0, 0) centre (-107.75, 0, 0) major R11 minor r0.25; extent (-108, -5.9388, -11.25)..(-107.75, 11.25, 0)
  - cylinder axis dir(-1, 0, 0) through (-106.625, -5.8069, -9.3424) R0.25; extent (-107.75, -6.0569, -9.5547)..(-105.5, -5.9388, -9.3424)
  - torus axis dir(1, 0, 0) centre (-107.75, -6.364, -6.364) major R2.5 minor r0.25; extent (-108, -4.773, -8.1317)..(-107.75, -3.864, -6.364)
  - torus axis dir(1, 0, 0) centre (-107.15, 6.364, 6.364) major R1.65 minor r0.25; extent (-107.4, 4.464, 6.364)..(-107.15, 8.264, 8.264)
  - torus axis dir(1, 0, 0) centre (-107.15, -6.364, -6.364) major R1.65 minor r0.25; extent (-107.4, -8.264, -6.364)..(-107.15, -4.464, -4.464)
  - cylinder axis dir(1, 0, 0) through (-106.325, 6.364, 6.364) R1.9; extent (-107.15, 4.464, 6.364)..(-105.5, 8.264, 8.264)
  - cylinder axis dir(1, 0, 0) through (-106.325, -6.364, -6.364) R1.9; extent (-107.15, -8.264, -6.364)..(-105.5, -4.464, -4.464)
  - cylinder axis dir(-1, 0, 0) through (-106.625, 6.364, 6.364) R2.25; extent (-107.75, 4.114, 6.364)..(-105.5, 4.773, 7.955)
  - cylinder axis dir(-1, 0, 0) through (-106.25, -9, 0) R1.7; extent (-107.8, -10.7, -1.7)..(-104.7, -7.3, 0)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, 9) R1.7; extent (-107.8, -1.7, 7.3)..(-104.7, 1.7, 9)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 9, 0) R1.7; extent (-107.8, 7.3, -1.7)..(-104.7, 10.7, 0)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, -9) R1.7; extent (-107.8, -1.7, -10.7)..(-104.7, 1.7, -9)
  - cylinder axis dir(-1, 0, 0) through (-106.125, 0, 0) R11.25; extent (-107.75, -11.25, 0)..(-104.5, 11.25, 11.25)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, 0) R5; extent (-107.75, -5, -5)..(-104.75, 5, 0)
  - cylinder axis dir(-1, 0, 0) through (-102.7937, 9, 0) R1.5; extent (-102.95, 7.5, -1.5)..(-102.6375, 10.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-103.2938, 9, 0) R1.5; extent (-103.45, 7.5, -1.5)..(-103.1375, 10.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-103.7938, 9, 0) R1.5; extent (-103.95, 7.5, -1.5)..(-103.6375, 10.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-104.4188, 9, 0) R1.5; extent (-104.7, 7.5, -1.5)..(-104.1375, 10.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-104.0438, 9, 0) R1.5; extent (-104.2, 7.5, 0)..(-103.8875, 10.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-103.0438, 9, 0) R1.5; extent (-103.2, 7.5, 0)..(-102.8875, 10.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-103.5438, 9, 0) R1.5; extent (-103.7, 7.5, 0)..(-103.3875, 10.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-104.5, 9, 0) R1.5; extent (-104.7, 7.5, 0)..(-104.3, 10.5, 1.5)
  - cone axis dir(-1, 0, 0) through (-104.2683, 9, 0) R1.7, half-angle 45 deg; extent (-104.3, 9.45, -1.4309)..(-104.2366, 10.5, 0)
  - cone axis dir(-1, 0, 0) through (-104.1891, 9, 0) R1.7, half-angle 45 deg; extent (-104.3, 7.5, 0)..(-104.0781, 10.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-102.6688, 0, -9) R1.5; extent (-102.825, -1.5, -10.5)..(-102.5125, 1.5, -9)
  - cylinder axis dir(-1, 0, 0) through (-103.1688, 0, -9) R1.5; extent (-103.325, -1.5, -10.5)..(-103.0125, 1.5, -9)
  - cylinder axis dir(-1, 0, 0) through (-103.6688, 0, -9) R1.5; extent (-103.825, -1.5, -10.5)..(-103.5125, 1.5, -9)
  - cylinder axis dir(-1, 0, 0) through (-104.3563, 0, -9) R1.5; extent (-104.7, -1.5, -10.5)..(-104.0125, 1.5, -9)
  - cylinder axis dir(-1, 0, 0) through (-103.9188, 0, -9) R1.5; extent (-104.075, -1.5, -9)..(-103.7625, 1.5, -7.5)
  - cylinder axis dir(-1, 0, 0) through (-102.9188, 0, -9) R1.5; extent (-103.075, -1.5, -9)..(-102.7625, 1.5, -7.5)
  - cylinder axis dir(-1, 0, 0) through (-103.4188, 0, -9) R1.5; extent (-103.575, -1.5, -9)..(-103.2625, 1.5, -7.5)
  - cylinder axis dir(-1, 0, 0) through (-104.4813, 0, -9) R1.5; extent (-104.7, -1.5, -9)..(-104.2625, 1.5, -7.5)
  - cone axis dir(-1, 0, 0) through (-104.2683, 0, -9) R1.7, half-angle 45 deg; extent (-104.3, -1.4309, -10.5)..(-104.2366, 0, -9.45)
  - cone axis dir(-1, 0, 0) through (-104.1891, 0, -9) R1.7, half-angle 45 deg; extent (-104.3, 0, -10.5)..(-104.0781, 1.5, -7.5)
  - cylinder axis dir(-1, 0, 0) through (-103.0437, -9, 0) R1.5; extent (-103.2, -10.5, -1.5)..(-102.8875, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-103.5437, -9, 0) R1.5; extent (-103.7, -10.5, -1.5)..(-103.3875, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-104.0437, -9, 0) R1.5; extent (-104.2, -10.5, -1.5)..(-103.8875, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-104.5, -9, 0) R1.5; extent (-104.7, -10.5, -1.5)..(-104.3, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-102.7938, -9, 0) R1.5; extent (-102.95, -10.5, 0)..(-102.6375, -7.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-103.2937, -9, 0) R1.5; extent (-103.45, -10.5, 0)..(-103.1375, -7.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-103.7938, -9, 0) R1.5; extent (-103.95, -10.5, 0)..(-103.6375, -7.5, 1.5)
  - cylinder axis dir(-1, 0, 0) through (-104.4188, -9, 0) R1.5; extent (-104.7, -10.5, 0)..(-104.1375, -7.5, 1.5)
  - cone axis dir(-1, 0, 0) through (-104.2683, -9, 0) R1.7, half-angle 45 deg; extent (-104.3, -10.5, 0)..(-104.2366, -9.45, 1.4309)
  - cone axis dir(-1, 0, 0) through (-104.1891, -9, 0) R1.7, half-angle 45 deg; extent (-104.3, -10.5, -1.5)..(-104.0781, -7.5, 0)
  - cylinder axis dir(-1, 0, 0) through (-102.9188, 0, 9) R1.5; extent (-103.075, -1.5, 7.5)..(-102.7625, 1.5, 9)
  - cylinder axis dir(-1, 0, 0) through (-103.4188, 0, 9) R1.5; extent (-103.575, -1.5, 7.5)..(-103.2625, 1.5, 9)
  - cylinder axis dir(-1, 0, 0) through (-103.9188, 0, 9) R1.5; extent (-104.075, -1.5, 7.5)..(-103.7625, 1.5, 9)
  - cylinder axis dir(-1, 0, 0) through (-104.4813, 0, 9) R1.5; extent (-104.7, -1.5, 7.5)..(-104.2625, 1.5, 9)
  - cylinder axis dir(-1, 0, 0) through (-102.6688, 0, 9) R1.5; extent (-102.825, -1.5, 9)..(-102.5125, 1.5, 10.5)
  - cylinder axis dir(-1, 0, 0) through (-103.1688, 0, 9) R1.5; extent (-103.325, -1.5, 9)..(-103.0125, 1.5, 10.5)
  - cylinder axis dir(-1, 0, 0) through (-103.6688, 0, 9) R1.5; extent (-103.825, -1.5, 9)..(-103.5125, 1.5, 10.5)
  - cylinder axis dir(-1, 0, 0) through (-104.3563, 0, 9) R1.5; extent (-104.7, -1.5, 9)..(-104.0125, 1.5, 10.5)
  - cone axis dir(-1, 0, 0) through (-104.2683, 0, 9) R1.7, half-angle 45 deg; extent (-104.3, 0, 9.45)..(-104.2366, 1.4309, 10.5)
  - cone axis dir(-1, 0, 0) through (-104.1891, 0, 9) R1.7, half-angle 45 deg; extent (-104.3, -1.5, 7.5)..(-104.0781, 0, 10.5)
  - cone axis dir(-1, 0, 0) through (-104.1376, 0, 9) R1.7, half-angle 45 deg; extent (-104.3, 0, 7.5)..(-103.9752, 1.4247, 10.1136)
  - plane n(0, 1, 0), n·p = 0; extent (-101.1531, 0, 10.1752)..(-100.6844, 0, 10.5271)
  - free-form (blend) face; extent (-104.3, -1.5271, 7.4729)..(-100.95, 1.5271, 10.5271)
  - free-form (blend) face; extent (-102.5, -1.5271, 7.4729)..(-100.6844, 1.5271, 10.5271)
  - free-form (blend) face; extent (-104.3, -1.5271, 7.4729)..(-100.6844, 1.5271, 10.5271)
  - free-form (blend) face; extent (-103.9752, -1.1752, 7.8248)..(-100.8875, 1.1752, 10.1752)
  - cylinder axis dir(-1, 0, 0) through (-102.5375, 0, 9) R1.5; extent (-102.575, -1.5, 7.7825)..(-102.5, -0.8761, 9)
  - cone axis dir(-1, 0, 0) through (-104.1376, -9, 0) R1.7, half-angle 45 deg; extent (-104.3, -10.1136, 0)..(-103.9752, -7.5, 1.4247)
  - plane n(0, 0, 1), n·p = 0; extent (-101.1531, -10.5271, 0)..(-100.6844, -10.1752, 0)
  - free-form (blend) face; extent (-104.3, -10.5271, -1.5271)..(-100.95, -7.4729, 1.5271)
  - free-form (blend) face; extent (-102.5, -10.5271, -1.5271)..(-100.6844, -7.4729, 1.5271)
  - free-form (blend) face; extent (-104.3, -10.5271, -1.5271)..(-100.6844, -7.4729, 1.5271)
  - free-form (blend) face; extent (-103.9752, -10.1752, -1.1752)..(-100.8875, -7.8248, 1.1752)
  - cylinder axis dir(-1, 0, 0) through (-102.6, -9, 0) R1.5; extent (-102.7, -10.5, -1.5)..(-102.5, -7.7825, 0)
  - cone axis dir(-1, 0, 0) through (-104.1376, 0, -9) R1.7, half-angle 45 deg; extent (-104.3, -1.4247, -10.1136)..(-103.9752, 0, -7.5)
  - plane n(0, -1, 0), n·p = 0; extent (-101.1531, 0, -10.5271)..(-100.6844, 0, -10.1752)
  - free-form (blend) face; extent (-104.3, -1.5271, -10.5271)..(-100.95, 1.5271, -7.4729)
  - free-form (blend) face; extent (-102.5, -1.5271, -10.5271)..(-100.6844, 1.5271, -7.4729)
  - free-form (blend) face; extent (-104.3, -1.5271, -10.5271)..(-100.6844, 1.5271, -7.4729)
  - free-form (blend) face; extent (-103.9752, -1.1752, -10.1752)..(-100.8875, 1.1752, -7.8248)
  - cylinder axis dir(-1, 0, 0) through (-102.5375, 0, -9) R1.5; extent (-102.575, 0.8761, -9)..(-102.5, 1.5, -7.7825)
  - cone axis dir(-1, 0, 0) through (-104.1376, 9, 0) R1.7, half-angle 45 deg; extent (-104.3, 7.5, -1.4247)..(-103.9752, 10.1136, 0)
  - plane n(0, 0, -1), n·p = 0; extent (-101.1531, 10.1752, 0)..(-100.6844, 10.5271, 0)
  - free-form (blend) face; extent (-104.3, 7.4729, -1.5271)..(-100.95, 10.5271, 1.5271)
  - free-form (blend) face; extent (-102.5, 7.4729, -1.5271)..(-100.6844, 10.5271, 1.5271)
  - free-form (blend) face; extent (-104.3, 7.4729, -1.5271)..(-100.6844, 10.5271, 1.5271)
  - free-form (blend) face; extent (-103.9752, 7.8248, -1.1752)..(-100.8875, 10.1752, 1.1752)
  - cylinder axis dir(-1, 0, 0) through (-102.6, 9, 0) R1.5; extent (-102.7, 7.7825, 0)..(-102.5, 10.5, 1.5)
  - plane n(-1, 0, 0), n·p = 104.5; extent (-104.5, -11.25, -11.25)..(-104.5, 11.25, 11.25)
  - plane n(1, 0, 0), n·p = -108; extent (-108, -11, -11)..(-108, 11, 11)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, 0) R5; extent (-107.75, -5, 0)..(-104.75, 5, 5)
  - cylinder axis dir(-1, 0, 0) through (-106.125, 0, 0) R11.25; extent (-107.75, -11.25, -11.25)..(-104.5, 11.25, 0)
  - plane n(-1, 0, 0), n·p = 104.7; extent (-104.7, -1.7, -10.7)..(-104.7, 1.7, -7.3)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, -9) R1.7; extent (-107.8, -1.7, -9)..(-104.7, 1.7, -7.3)
  - plane n(-1, 0, 0), n·p = 104.7; extent (-104.7, 7.3, -1.7)..(-104.7, 10.7, 1.7)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 9, 0) R1.7; extent (-107.8, 7.3, 0)..(-104.7, 10.7, 1.7)
  - plane n(-1, 0, 0), n·p = 104.7; extent (-104.7, -1.7, 7.3)..(-104.7, 1.7, 10.7)
  - cylinder axis dir(-1, 0, 0) through (-106.25, 0, 9) R1.7; extent (-107.8, -1.7, 9)..(-104.7, 1.7, 10.7)
  - plane n(-1, 0, 0), n·p = 104.7; extent (-104.7, -10.7, -1.7)..(-104.7, -7.3, 1.7)
  - cylinder axis dir(-1, 0, 0) through (-106.25, -9, 0) R1.7; extent (-107.8, -10.7, 0)..(-104.7, -7.3, 1.7)
  - cylinder axis dir(-1, 0, 0) through (-106.625, 6.364, 6.364) R2.25; extent (-107.75, 4.114, 4.114)..(-105.5, 7.955, 6.364)
  - plane n(0, 0.7071, -0.7071), n·p = 2.25; extent (-107.75, 7.955, 4.773)..(-105.5, 9.1656, 5.9836)
  - plane n(0, -0.7071, 0.7071), n·p = 2.25; extent (-107.75, 4.773, 7.955)..(-105.5, 5.9836, 9.1656)
  - plane n(-1, 0, 0), n·p = 105.5; extent (-105.5, 4.114, 4.114)..(-105.5, 9.5547, 9.5547)
  - cylinder axis dir(-1, 0, 0) through (-106.625, -6.364, -6.364) R2.25; extent (-107.75, -7.955, -7.955)..(-105.5, -4.114, -4.114)
  - plane n(0, -0.7071, 0.7071), n·p = 2.25; extent (-107.75, -9.1656, -5.9836)..(-105.5, -7.955, -4.773)
  - plane n(0, 0.7071, -0.7071), n·p = 2.25; extent (-107.75, -5.9836, -9.1656)..(-105.5, -4.773, -7.955)
  - plane n(-1, 0, 0), n·p = 105.5; extent (-105.5, -9.5547, -9.5547)..(-105.5, -4.114, -4.114)
  - cylinder axis dir(1, 0, 0) through (-106.325, -6.364, -6.364) R1.9; extent (-107.15, -8.264, -8.264)..(-105.5, -4.464, -6.364)
  - plane n(1, 0, 0), n·p = -107.4; extent (-107.4, -8.014, -8.014)..(-107.4, -4.714, -4.714)
  - cylinder axis dir(1, 0, 0) through (-106.325, 6.364, 6.364) R1.9; extent (-107.15, 4.464, 4.464)..(-105.5, 8.264, 6.364)
  - plane n(1, 0, 0), n·p = -107.4; extent (-107.4, 4.714, 4.714)..(-107.4, 8.014, 8.014)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -5.9309, -6.364)..(-107.284, -5.4979, -5.614)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -5.9309, -7.114)..(-107.284, -5.4979, -6.364)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -6.797, -7.23)..(-107.284, -5.9309, -7.114)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -7.23, -7.114)..(-107.284, -6.797, -6.364)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -7.23, -6.364)..(-107.284, -6.797, -5.614)
  - cone axis dir(-1, 0, 0) through (-107.342, -6.364, -6.364) R0.866, half-angle 45 deg; extent (-107.4, -6.797, -5.614)..(-107.284, -5.9309, -5.4979)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 5.9309, 7.114)..(-107.284, 6.797, 7.23)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 6.797, 6.364)..(-107.284, 7.23, 7.114)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 6.797, 5.614)..(-107.284, 7.23, 6.364)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 5.9309, 5.4979)..(-107.284, 6.797, 5.614)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 5.4979, 5.614)..(-107.284, 5.9309, 6.364)
  - cone axis dir(-1, 0, 0) through (-107.342, 6.364, 6.364) R0.866, half-angle 45 deg; extent (-107.4, 5.4979, 6.364)..(-107.284, 5.9309, 7.114)
  - plane n(-1, 0, 0), n·p = 105.9; extent (-105.9, -7.23, -7.114)..(-105.9, -5.4979, -5.614)
  - plane n(0, 0.866, 0.5), n·p = -7.9433; extent (-107.4, -5.9309, -6.364)..(-105.9, -5.4979, -5.614)
  - plane n(0, 0.866, -0.5), n·p = -1.5794; extent (-107.4, -5.9309, -7.114)..(-105.9, -5.4979, -6.364)
  - plane n(0, 0, -1), n·p = 7.114; extent (-107.4, -6.797, -7.114)..(-105.9, -5.9309, -7.114)
  - plane n(0, -0.866, -0.5), n·p = 9.4433; extent (-107.4, -7.23, -7.114)..(-105.9, -6.797, -6.364)
  - plane n(0, -0.866, 0.5), n·p = 3.0794; extent (-107.4, -7.23, -6.364)..(-105.9, -6.797, -5.614)
  - plane n(0, 0, 1), n·p = -5.614; extent (-107.4, -6.797, -5.614)..(-105.9, -5.9309, -5.614)
  - plane n(-1, 0, 0), n·p = 105.9; extent (-105.9, 5.4979, 5.614)..(-105.9, 7.23, 7.114)
  - plane n(0, 0, 1), n·p = 7.114; extent (-107.4, 5.9309, 7.114)..(-105.9, 6.797, 7.114)
  - plane n(0, 0.866, 0.5), n·p = 9.4433; extent (-107.4, 6.797, 6.364)..(-105.9, 7.23, 7.114)
  - plane n(0, 0.866, -0.5), n·p = 3.0794; extent (-107.4, 6.797, 5.614)..(-105.9, 7.23, 6.364)
  - plane n(0, 0, -1), n·p = -5.614; extent (-107.4, 5.9309, 5.614)..(-105.9, 6.797, 5.614)
  - plane n(0, -0.866, -0.5), n·p = -7.9433; extent (-107.4, 5.4979, 5.614)..(-105.9, 5.9309, 6.364)
  - plane n(0, -0.866, 0.5), n·p = -1.5794; extent (-107.4, 5.4979, 6.364)..(-105.9, 5.9309, 7.114)
  - torus axis dir(1, 0, 0) centre (-107.15, -6.364, -6.364) major R1.65 minor r0.25; extent (-107.4, -8.264, -8.264)..(-107.15, -4.464, -6.364)
  - torus axis dir(1, 0, 0) centre (-107.15, 6.364, 6.364) major R1.65 minor r0.25; extent (-107.4, 4.464, 4.464)..(-107.15, 8.264, 6.364)
  - cylinder axis dir(-1, 0, 0) through (-106.625, -9.3424, -5.8069) R0.25; extent (-107.75, -9.5547, -6.0569)..(-105.5, -9.1656, -5.9388)
  - cylinder axis dir(0, 0.7071, 0.7071) through (-107.75, -8.7371, -5.2015) R0.25; extent (-108, -9.3424, -5.9836)..(-107.75, -7.955, -4.5962)
  - torus axis dir(1, 0, 0) centre (-107.75, -6.364, -6.364) major R2.5 minor r0.25; extent (-108, -8.1317, -6.364)..(-107.75, -3.864, -3.864)
  - sphere centre (-107.75, -9.3424, -5.8069) R0.25; extent (-108, -9.5547, -6.0569)..(-107.75, -9.1656, -5.8069)
  - cylinder axis dir(0, -0.7071, -0.7071) through (-107.75, -5.2015, -8.7371) R0.25; extent (-108, -5.9836, -9.3424)..(-107.75, -4.5962, -7.955)
  - cylinder axis dir(-1, 0, 0) through (-106.625, -5.8069, -9.3424) R0.25; extent (-107.75, -6.0569, -9.3424)..(-105.5, -5.9836, -9.1656)
  - cylinder axis dir(-1, 0, 0) through (-106.625, 5.8069, 9.3424) R0.25; extent (-107.75, 5.9388, 9.1656)..(-105.5, 6.0569, 9.5547)
  - torus axis dir(1, 0, 0) centre (-107.75, 0, 0) major R11 minor r0.25; extent (-108, -11.25, -5.9388)..(-107.75, 5.9388, 11.25)
  - sphere centre (-107.75, -5.8069, -9.3424) R0.25; extent (-108, -6.0569, -9.5547)..(-107.75, -5.8069, -9.1656)
  - sphere centre (-107.75, 5.8069, 9.3424) R0.25; extent (-108, 5.8069, 9.1656)..(-107.75, 6.0569, 9.5547)
  - torus axis dir(1, 0, 0) centre (-107.75, 0, 0) major R11 minor r0.25; extent (-108, 9.3424, 0)..(-107.75, 11.25, 5.9388)
  - cylinder axis dir(-1, 0, 0) through (-106.625, 9.3424, 5.8069) R0.25; extent (-107.75, 9.1656, 5.9388)..(-105.5, 9.5547, 6.0569)
  - cylinder axis dir(0, 0.7071, 0.7071) through (-107.75, 5.2015, 8.7371) R0.25; extent (-108, 4.5962, 7.955)..(-107.75, 5.9836, 9.3424)
  - sphere centre (-107.75, 9.3424, 5.8069) R0.25; extent (-108, 9.1656, 5.8069)..(-107.75, 9.5547, 6.0569)
  - torus axis dir(1, 0, 0) centre (-107.75, 6.364, 6.364) major R2.5 minor r0.25; extent (-108, 3.864, 3.864)..(-107.75, 8.1317, 8.1317)
  - cylinder axis dir(0, -0.7071, -0.7071) through (-107.75, 8.7371, 5.2015) R0.25; extent (-108, 7.955, 4.5962)..(-107.75, 9.3424, 5.9836)
  - cone axis dir(-1, 0, 0) through (-107.875, 0, 0) R5, half-angle 45 deg; extent (-108, -5.25, 0)..(-107.75, 5.25, 5.25)
  - cone axis dir(1, 0, 0) through (-104.625, 0, 0) R5.25, half-angle 45 deg; extent (-104.75, -5.25, 0)..(-104.5, 5.25, 5.25)
  - cone axis dir(-1, 0, 0) through (-107.9, -9, 0) R1.7, half-angle 45 deg; extent (-108, -9, -1.9)..(-107.8, -7.1, 1.9)
  - cone axis dir(-1, 0, 0) through (-107.9, 0, -9) R1.7, half-angle 45 deg; extent (-108, -1.9, -9)..(-107.8, 1.9, -7.1)
  - cone axis dir(-1, 0, 0) through (-107.9, 9, 0) R1.7, half-angle 45 deg; extent (-108, 9, -1.9)..(-107.8, 10.9, 1.9)
  - cone axis dir(-1, 0, 0) through (-107.9, 0, 9) R1.7, half-angle 45 deg; extent (-108, -1.9, 9)..(-107.8, 1.9, 10.9)
  - plane n(1, 0, 0), n·p = -102.5; extent (-102.5, -1.75, 7.25)..(-102.5, 1.75, 10.75)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 0, 9) R1.75; extent (-104.5, -1.75, 7.25)..(-102.5, 1.75, 9)
  - plane n(1, 0, 0), n·p = -102.5; extent (-102.5, 7.25, -1.75)..(-102.5, 10.75, 1.75)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 9, 0) R1.75; extent (-104.5, 7.25, -1.75)..(-102.5, 10.75, 0)
  - plane n(1, 0, 0), n·p = -102.5; extent (-102.5, -1.75, -10.75)..(-102.5, 1.75, -7.25)
  - cylinder axis dir(-1, 0, 0) through (-103.5, 0, -9) R1.75; extent (-104.5, -1.75, -10.75)..(-102.5, 1.75, -9)
  - plane n(1, 0, 0), n·p = -102.5; extent (-102.5, -10.75, -1.75)..(-102.5, -7.25, 1.75)
  - cylinder axis dir(-1, 0, 0) through (-103.5, -9, 0) R1.75; extent (-104.5, -10.75, -1.75)..(-102.5, -7.25, 0)

### P06 Ball-screw nut wiper seal (with four cap screw heads) (127 faces)

Wiper seal ring at the inner end of the ball-screw nut, one solid with four cap screw heads: ring x -79.1 .. -75, outer R11.25, bore R5 with a lip that follows the helical ball groove (one turn, free-form faces, it fills the groove profile R0.7075 at x = -75), four notches R2.125 at radius 9 (0, 90, 180, 270 deg) holding screw heads R1.9 with hexagon sockets 1.5 across flats.

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (-79.1, 11.25) – (-75.3, 11.25) – (-75, 10.95) – (-75, 5.5) – (-75.5, 5) – (-79.1, 5) – (-79.1, 11.25)
  - loop: (-79.1, -5) – (-75.5, -5) – (-75, -5.5) – (-75, -10.95) – (-75.3, -11.25) – (-79.1, -11.25) – (-79.1, -5)
Axial section in the half-plane at 0 deg (coordinates x, r; negative r = the opposite half-plane at 180 deg):
  - loop: (-75.7075, 5.0075) – arc c(-75, 5.0075) R0.7075 via (-75.566, 5.432) – (-75, 5.715) – (-75, 6.675) – arc c(-75.2, 6.675) R0.2 via (-75.0586, 6.8164) – (-75.2, 6.875) – (-77.25, 6.875) – (-77.25, 7.1) – (-75.5, 7.1) – arc c(-75.5, 7.35) R0.25 via (-75.3232, 7.1732) – (-75.25, 7.35) – (-75.25, 8.134) – (-76.75, 8.134) – (-76.75, 9.866) – (-75.25, 9.866) – (-75.25, 10.65) – arc c(-75.5, 10.65) R0.25 via (-75.3232, 10.8268) – (-75.5, 10.9) – (-77.25, 10.9) – (-77.25, 11.25) – (-79.1, 11.25) – (-79.1, 5) – (-75.7075, 5) – arc c(-75, 5.0075) R0.7075 via (-75.7075, 5.0038) – (-75.7075, 5.0075)
  - loop: (-79.1, -5) – (-79.1, -11.25) – (-77.25, -11.25) – (-77.25, -10.9) – (-75.5, -10.9) – arc c(-75.5, -10.65) R0.25 via (-75.3232, -10.8268) – (-75.25, -10.65) – (-75.25, -9.866) – (-76.75, -9.866) – (-76.75, -8.134) – (-75.25, -8.134) – (-75.25, -7.35) – arc c(-75.5, -7.35) R0.25 via (-75.3232, -7.1732) – (-75.5, -7.1) – (-77.25, -7.1) – (-77.25, -6.875) – (-75.2, -6.875) – arc c(-75.2, -6.675) R0.2 via (-75.0586, -6.8164) – (-75, -6.675) – (-75, -5.5) – (-75.5, -5) – (-79.1, -5)
Cross-section at x = -77 (coordinates y, z):
  - loop: (4.2916, -2.5802) – blend curve via (3.8227, -4.2483) – (2.1163, -4.5383) – arc c(2.4232, -4.3952) R0.3385 via (2.1148, -4.5349) – (2.1132, -4.5315) – arc c(0, 0) R5 via (-2.6864, -4.217) – (-5, 0) – arc c(0, 0) R5 via (0, 5) – (5, 0) – arc c(0, 0) R5 via (4.818, -1.3369) – (4.2851, -2.5764) – arc c(4.1165, -2.8714) R0.3398 via (4.2884, -2.5783) – (4.2916, -2.5802)
  - loop: (10.8026, 2.125) – arc c(10.8026, 2.325) R0.2 via (10.9441, 2.1836) – (11.0026, 2.325) – arc c(10.8026, 2.325) R0.2 via (11.0015, 2.3462) – (10.9982, 2.3671) – arc c(0, 0) R11.25 via (7.955, 7.955) – (2.3671, 10.9982) – arc c(2.325, 10.8026) R0.2 via (2.1993, 10.9582) – (2.125, 10.8026) – (2.125, 9) – arc c(0, 9) R2.125 via (0, 6.875) – (-2.125, 9) – (-2.125, 10.8026) – arc c(-2.325, 10.8026) R0.2 via (-2.1993, 10.9582) – (-2.3671, 10.9982) – arc c(0, 0) R11.25 via (-7.955, 7.955) – (-10.9982, 2.3671) – arc c(-10.8026, 2.325) R0.2 via (-10.9582, 2.1993) – (-10.8026, 2.125) – (-9, 2.125) – arc c(-9, 0) R2.125 via (-7.4974, 1.5026) – (-6.875, 0) – arc c(-9, 0) R2.125 via (-7.4974, -1.5026) – (-9, -2.125) – (-10.8026, -2.125) – arc c(-10.8026, -2.325) R0.2 via (-10.9582, -2.1993) – (-10.9982, -2.3671) – arc c(0, 0) R11.25 via (-7.955, -7.955) – (-2.3671, -10.9982) – arc c(-2.325, -10.8026) R0.2 via (-2.1993, -10.9582) – (-2.125, -10.8026) – (-2.125, -9) – arc c(0, -9) R2.125 via (0, -6.875) – (2.125, -9) – (2.125, -10.8026) – arc c(2.325, -10.8026) R0.2 via (2.1993, -10.9582) – (2.3671, -10.9982) – arc c(0, 0) R11.25 via (7.955, -7.955) – (10.9982, -2.3671) – arc c(10.8026, -2.325) R0.2 via (11.0015, -2.3462) – (11.0026, -2.325) – arc c(10.8026, -2.325) R0.2 via (10.9441, -2.1836) – (10.8026, -2.125) – (9, -2.125) – arc c(9, 0) R2.125 via (6.875, 0) – (9, 2.125) – (10.8026, 2.125)
  - loop: (7.1, 0) – arc c(9, 0) R1.9 via (9, 1.9) – (10.9, 0) – arc c(9, 0) R1.9 via (9, -1.9) – (7.1, 0)
  - loop: (-1.9, -9) – arc c(0, -9) R1.9 via (0, -7.1) – (1.9, -9) – arc c(0, -9) R1.9 via (0, -10.9) – (-1.9, -9)
  - loop: (-10.9, 0) – arc c(-9, 0) R1.9 via (-9, 1.9) – (-7.1, 0) – arc c(-9, 0) R1.9 via (-9, -1.9) – (-10.9, 0)
  - loop: (-1.9, 9) – arc c(0, 9) R1.9 via (0, 10.9) – (1.9, 9) – arc c(0, 9) R1.9 via (0, 7.1) – (-1.9, 9)
Cross-section at x = -75.5 (coordinates y, z):
  - loop: (4.9885, 0.4364) – blend curve via (5.5901, -1.1881) – (4.3803, -2.4265) – arc c(4.5449, -2.1293) R0.3398 via (4.377, -2.4247) – (4.3738, -2.4228) – arc c(0, 0) R5 via (-1.2512, -4.8409) – (-5, 0) – arc c(0, 0) R5 via (-0.218, 4.9952) – (4.981, 0.4356) – arc c(5.018, 0.0991) R0.3385 via (4.9847, 0.436) – (4.9885, 0.4364)
  - loop: (10.8026, 2.125) – arc c(10.8026, 2.325) R0.2 via (10.9441, 2.1836) – (11.0026, 2.325) – arc c(10.8026, 2.325) R0.2 via (11.0015, 2.3462) – (10.9982, 2.3671) – arc c(0, 0) R11.25 via (7.955, 7.955) – (2.3671, 10.9982) – arc c(2.325, 10.8026) R0.2 via (2.1993, 10.9582) – (2.125, 10.8026) – (2.125, 9) – arc c(0, 9) R2.125 via (0, 6.875) – (-2.125, 9) – (-2.125, 10.8026) – arc c(-2.325, 10.8026) R0.2 via (-2.1993, 10.9582) – (-2.3671, 10.9982) – arc c(0, 0) R11.25 via (-7.955, 7.955) – (-10.9982, 2.3671) – arc c(-10.8026, 2.325) R0.2 via (-10.9582, 2.1993) – (-10.8026, 2.125) – (-9, 2.125) – arc c(-9, 0) R2.125 via (-7.4974, 1.5026) – (-6.875, 0) – arc c(-9, 0) R2.125 via (-7.4974, -1.5026) – (-9, -2.125) – (-10.8026, -2.125) – arc c(-10.8026, -2.325) R0.2 via (-10.9582, -2.1993) – (-10.9982, -2.3671) – arc c(0, 0) R11.25 via (-7.955, -7.955) – (-2.3671, -10.9982) – arc c(-2.325, -10.8026) R0.2 via (-2.1993, -10.9582) – (-2.125, -10.8026) – (-2.125, -9) – arc c(0, -9) R2.125 via (0, -6.875) – (2.125, -9) – (2.125, -10.8026) – arc c(2.325, -10.8026) R0.2 via (2.1993, -10.9582) – (2.3671, -10.9982) – arc c(0, 0) R11.25 via (7.955, -7.955) – (10.9982, -2.3671) – arc c(10.8026, -2.325) R0.2 via (11.0015, -2.3462) – (11.0026, -2.325) – arc c(10.8026, -2.325) R0.2 via (10.9441, -2.1836) – (10.8026, -2.125) – (9, -2.125) – arc c(9, 0) R2.125 via (6.875, 0) – (9, 2.125) – (10.8026, 2.125)
  - loop: (-0.433, 8.25) – (-0.866, 9) – (-0.433, 9.75) – (0.433, 9.75) – (0.866, 9) – (0.433, 8.25) – (-0.433, 8.25)
  - loop: (-9.433, -0.75) – (-9.866, 0) – (-9.433, 0.75) – (-8.567, 0.75) – (-8.134, 0) – (-8.567, -0.75) – (-9.433, -0.75)
  - loop: (0.866, -9) – (0.433, -9.75) – (-0.433, -9.75) – (-0.866, -9) – (-0.433, -8.25) – (0.433, -8.25) – (0.866, -9)
  - loop: (8.567, -0.75) – (8.134, 0) – (8.567, 0.75) – (9.433, 0.75) – (9.866, 0) – (9.433, -0.75) – (8.567, -0.75)
  - loop: (-1.9, 9) – arc c(0, 9) R1.9 via (0, 10.9) – (1.9, 9) – arc c(0, 9) R1.9 via (0, 7.1) – (-1.9, 9)
  - loop: (-10.9, 0) – arc c(-9, 0) R1.9 via (-9, 1.9) – (-7.1, 0) – arc c(-9, 0) R1.9 via (-9, -1.9) – (-10.9, 0)
  - loop: (-1.9, -9) – arc c(0, -9) R1.9 via (0, -7.1) – (1.9, -9) – arc c(0, -9) R1.9 via (0, -10.9) – (-1.9, -9)
  - loop: (7.1, 0) – arc c(9, 0) R1.9 via (9, 1.9) – (10.9, 0) – arc c(9, 0) R1.9 via (9, -1.9) – (7.1, 0)
Complete face list (127):
  - free-form (blend) face; extent (-79.1, -2.1774, -5.715)..(-75, 5.715, 1.1604)
  - free-form (blend) face; extent (-79.1, -2.1448, -5.0075)..(-75.4925, 4.3879, -2.4128)
  - torus axis dir(1, 0, 0) centre (-75.2, -9, 0) major R2.325 minor r0.2; extent (-75.2, -9, -2.325)..(-75, -6.675, 0)
  - cylinder axis dir(1, 0, 0) through (-76.1902, 10.8026, 2.325) R0.2; extent (-77.25, 10.8026, 2.125)..(-75.1304, 11.0026, 2.325)
  - cylinder axis dir(1, 0, 0) through (-76.2728, 10.8026, -2.325) R0.2; extent (-77.25, 10.9982, -2.3671)..(-75.2956, 11.0026, -2.325)
  - torus axis dir(1, 0, 0) centre (-75.5, 0, 9) major R1.65 minor r0.25; extent (-75.5, -1.9, 9)..(-75.25, 1.9, 10.9)
  - torus axis dir(1, 0, 0) centre (-75.5, -9, 0) major R1.65 minor r0.25; extent (-75.5, -10.9, 0)..(-75.25, -7.1, 1.9)
  - torus axis dir(1, 0, 0) centre (-75.5, 0, -9) major R1.65 minor r0.25; extent (-75.5, -1.9, -9)..(-75.25, 1.9, -7.1)
  - torus axis dir(1, 0, 0) centre (-75.5, 9, 0) major R1.65 minor r0.25; extent (-75.5, 7.1, 0)..(-75.25, 10.9, 1.9)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 9, 0) R1.9; extent (-77.25, 7.1, 0)..(-75.5, 10.9, 1.9)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 0, -9) R1.9; extent (-77.25, -1.9, -9)..(-75.5, 1.9, -7.1)
  - cylinder axis dir(-1, 0, 0) through (-76.375, -9, 0) R1.9; extent (-77.25, -10.9, 0)..(-75.5, -7.1, 1.9)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 0, 9) R1.9; extent (-77.25, -1.9, 9)..(-75.5, 1.9, 10.9)
  - cylinder axis dir(1, 0, 0) through (-76.225, -9, 0) R2.125; extent (-77.25, -9, 0)..(-75.2, -6.875, 2.125)
  - cylinder axis dir(1, 0, 0) through (-77.2, 0, 0) R11.25; extent (-79.1, -11.25, 0)..(-75.3, 11.25, 11.25)
  - cylinder axis dir(1, 0, 0) through (-77.3, 0, 0) R5; extent (-79.1, -5, -5)..(-75.5, 4.3738, 0)
  - cylinder axis dir(1, 0, 0) through (-77.3, 0, 0) R5; extent (-79.1, -5, 0)..(-75.5, 5, 5)
  - plane n(1, 0, 0), n·p = -79.1; extent (-79.1, -11.25, -11.25)..(-79.1, 11.25, 11.25)
  - plane n(1, 0, 0), n·p = -75; extent (-75, -10.7003, -10.7003)..(-75, 10.7003, 10.7003)
  - cylinder axis dir(1, 0, 0) through (-77.4037, 0, 0) R5; extent (-79.1, 0.7449, -4.9442)..(-75.7075, 5, 0)
  - cone axis dir(1, 0, 0) through (-75.25, 0, 0) R5, half-angle 45 deg; extent (-75.5, -5.5, -5.5)..(-75, 5.3762, 5.5)
  - cone axis dir(-1, 0, 0) through (-75.15, 0, 0) R10.95, half-angle 45 deg; extent (-75.3, 2.1375, 2.1375)..(-75, 11.0026, 11.0025)
  - cone axis dir(-1, 0, 0) through (-75.15, 0, 0) R10.95, half-angle 45 deg; extent (-75.3, 2.1375, -11.0025)..(-75, 11.0026, -2.1375)
  - cone axis dir(-1, 0, 0) through (-75.15, 0, 0) R10.95, half-angle 45 deg; extent (-75.3, -11.0025, -11.0025)..(-75, -2.1375, -2.1375)
  - cylinder axis dir(1, 0, 0) through (-77.2, 0, 0) R11.25; extent (-79.1, -11.25, -11.25)..(-75.3, 11.25, 0)
  - cone axis dir(-1, 0, 0) through (-75.15, 0, 0) R10.95, half-angle 45 deg; extent (-75.3, -11.0025, 2.1375)..(-75, -2.1375, 11.0025)
  - cylinder axis dir(1, 0, 0) through (-76.225, 0, -9) R2.125; extent (-77.25, -2.125, -9)..(-75.2, 2.125, -6.875)
  - plane n(0, 1, 0), n·p = 2.125; extent (-77.25, 2.125, -10.8026)..(-75.2, 2.125, -9)
  - plane n(0, -1, 0), n·p = 2.125; extent (-77.25, -2.125, -10.8026)..(-75.2, -2.125, -9)
  - plane n(1, 0, 0), n·p = -77.25; extent (-77.25, -2.3671, -11.25)..(-77.25, 2.3671, -6.875)
  - cylinder axis dir(1, 0, 0) through (-76.225, -9, 0) R2.125; extent (-77.25, -9, -2.125)..(-75.2, -6.875, 0)
  - plane n(0, 0, -1), n·p = 2.125; extent (-77.25, -10.8026, -2.125)..(-75.2, -9, -2.125)
  - plane n(0, 0, 1), n·p = 2.125; extent (-77.25, -10.8026, 2.125)..(-75.2, -9, 2.125)
  - plane n(1, 0, 0), n·p = -77.25; extent (-77.25, -11.25, -2.3671)..(-77.25, -6.875, 2.3671)
  - plane n(0, 0, -1), n·p = 2.125; extent (-77.25, 9, -2.125)..(-75.2, 10.8026, -2.125)
  - cylinder axis dir(1, 0, 0) through (-76.225, 9, 0) R2.125; extent (-77.25, 6.875, -2.125)..(-75.2, 9, 2.125)
  - plane n(0, 0, 1), n·p = 2.125; extent (-77.25, 9, 2.125)..(-75.2, 10.8026, 2.125)
  - plane n(1, 0, 0), n·p = -77.25; extent (-77.25, 6.875, -2.3671)..(-77.25, 11.25, 2.3671)
  - plane n(0, 1, 0), n·p = 2.125; extent (-77.25, 2.125, 9)..(-75.2, 2.125, 10.8026)
  - cylinder axis dir(1, 0, 0) through (-76.225, 0, 9) R2.125; extent (-77.25, -2.125, 6.875)..(-75.2, 2.125, 9)
  - plane n(0, -1, 0), n·p = 2.125; extent (-77.25, -2.125, 9)..(-75.2, -2.125, 10.8026)
  - plane n(1, 0, 0), n·p = -77.25; extent (-77.25, -2.3671, 6.875)..(-77.25, 2.3671, 11.25)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 0, 9) R1.9; extent (-77.25, -1.9, 7.1)..(-75.5, 1.9, 9)
  - plane n(1, 0, 0), n·p = -75.25; extent (-75.25, -1.65, 7.35)..(-75.25, 1.65, 10.65)
  - cylinder axis dir(-1, 0, 0) through (-76.375, -9, 0) R1.9; extent (-77.25, -10.9, -1.9)..(-75.5, -7.1, 0)
  - plane n(1, 0, 0), n·p = -75.25; extent (-75.25, -10.65, -1.65)..(-75.25, -7.35, 1.65)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 0, -9) R1.9; extent (-77.25, -1.9, -10.9)..(-75.5, 1.9, -9)
  - plane n(1, 0, 0), n·p = -75.25; extent (-75.25, -1.65, -10.65)..(-75.25, 1.65, -7.35)
  - cylinder axis dir(-1, 0, 0) through (-76.375, 9, 0) R1.9; extent (-77.25, 7.1, -1.9)..(-75.5, 10.9, 0)
  - plane n(1, 0, 0), n·p = -75.25; extent (-75.25, 7.35, -1.65)..(-75.25, 10.65, 1.65)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, -0.866, 8.25)..(-75.25, -0.433, 9)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, -0.433, 8.134)..(-75.25, 0.433, 8.25)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, 0.433, 8.25)..(-75.25, 0.866, 9)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, 0.433, 9)..(-75.25, 0.866, 9.75)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, -0.433, 9.75)..(-75.25, 0.433, 9.866)
  - cone axis dir(1, 0, 0) through (-75.308, 0, 9) R0.866, half-angle 45 deg; extent (-75.366, -0.866, 9)..(-75.25, -0.433, 9.75)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -9.866, -0.75)..(-75.25, -9.433, 0)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -9.433, -0.866)..(-75.25, -8.567, -0.75)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -8.567, -0.75)..(-75.25, -8.134, 0)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -8.567, 0)..(-75.25, -8.134, 0.75)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -9.433, 0.75)..(-75.25, -8.567, 0.866)
  - cone axis dir(1, 0, 0) through (-75.308, -9, 0) R0.866, half-angle 45 deg; extent (-75.366, -9.866, 0)..(-75.25, -9.433, 0.75)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, 0.433, -9.75)..(-75.25, 0.866, -9)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, 0.433, -9)..(-75.25, 0.866, -8.25)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, -0.433, -8.25)..(-75.25, 0.433, -8.134)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, -0.866, -9)..(-75.25, -0.433, -8.25)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, -0.866, -9.75)..(-75.25, -0.433, -9)
  - cone axis dir(1, 0, 0) through (-75.308, 0, -9) R0.866, half-angle 45 deg; extent (-75.366, -0.433, -9.866)..(-75.25, 0.433, -9.75)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 8.134, -0.75)..(-75.25, 8.567, 0)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 8.567, -0.866)..(-75.25, 9.433, -0.75)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 9.433, -0.75)..(-75.25, 9.866, 0)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 9.433, 0)..(-75.25, 9.866, 0.75)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 8.567, 0.75)..(-75.25, 9.433, 0.866)
  - cone axis dir(1, 0, 0) through (-75.308, 9, 0) R0.866, half-angle 45 deg; extent (-75.366, 8.134, 0)..(-75.25, 8.567, 0.75)
  - plane n(1, 0, 0), n·p = -76.75; extent (-76.75, -0.866, 8.25)..(-76.75, 0.866, 9.75)
  - plane n(0, -0.866, -0.5), n·p = -3.75; extent (-76.75, -0.866, 8.25)..(-75.25, -0.433, 9)
  - plane n(0, 0, -1), n·p = -8.25; extent (-76.75, -0.433, 8.25)..(-75.25, 0.433, 8.25)
  - plane n(0, 0.866, -0.5), n·p = -3.75; extent (-76.75, 0.433, 8.25)..(-75.25, 0.866, 9)
  - plane n(0, 0.866, 0.5), n·p = 5.25; extent (-76.75, 0.433, 9)..(-75.25, 0.866, 9.75)
  - plane n(0, 0, 1), n·p = 9.75; extent (-76.75, -0.433, 9.75)..(-75.25, 0.433, 9.75)
  - plane n(0, -0.866, 0.5), n·p = 5.25; extent (-76.75, -0.866, 9)..(-75.25, -0.433, 9.75)
  - plane n(1, 0, 0), n·p = -76.75; extent (-76.75, -9.866, -0.75)..(-76.75, -8.134, 0.75)
  - plane n(0, -0.866, -0.5), n·p = 8.5442; extent (-76.75, -9.866, -0.75)..(-75.25, -9.433, 0)
  - plane n(0, 0, -1), n·p = 0.75; extent (-76.75, -9.433, -0.75)..(-75.25, -8.567, -0.75)
  - plane n(0, 0.866, -0.5), n·p = -7.0442; extent (-76.75, -8.567, -0.75)..(-75.25, -8.134, 0)
  - plane n(0, 0.866, 0.5), n·p = -7.0442; extent (-76.75, -8.567, 0)..(-75.25, -8.134, 0.75)
  - plane n(0, 0, 1), n·p = 0.75; extent (-76.75, -9.433, 0.75)..(-75.25, -8.567, 0.75)
  - plane n(0, -0.866, 0.5), n·p = 8.5442; extent (-76.75, -9.866, 0)..(-75.25, -9.433, 0.75)
  - plane n(1, 0, 0), n·p = -76.75; extent (-76.75, -0.866, -9.75)..(-76.75, 0.866, -8.25)
  - plane n(0, 0.866, -0.5), n·p = 5.25; extent (-76.75, 0.433, -9.75)..(-75.25, 0.866, -9)
  - plane n(0, 0.866, 0.5), n·p = -3.75; extent (-76.75, 0.433, -9)..(-75.25, 0.866, -8.25)
  - plane n(0, 0, 1), n·p = -8.25; extent (-76.75, -0.433, -8.25)..(-75.25, 0.433, -8.25)
  - plane n(0, -0.866, 0.5), n·p = -3.75; extent (-76.75, -0.866, -9)..(-75.25, -0.433, -8.25)
  - plane n(0, -0.866, -0.5), n·p = 5.25; extent (-76.75, -0.866, -9.75)..(-75.25, -0.433, -9)
  - plane n(0, 0, -1), n·p = 9.75; extent (-76.75, -0.433, -9.75)..(-75.25, 0.433, -9.75)
  - plane n(1, 0, 0), n·p = -76.75; extent (-76.75, 8.134, -0.75)..(-76.75, 9.866, 0.75)
  - plane n(0, -0.866, -0.5), n·p = -7.0442; extent (-76.75, 8.134, -0.75)..(-75.25, 8.567, 0)
  - plane n(0, 0, -1), n·p = 0.75; extent (-76.75, 8.567, -0.75)..(-75.25, 9.433, -0.75)
  - plane n(0, 0.866, -0.5), n·p = 8.5442; extent (-76.75, 9.433, -0.75)..(-75.25, 9.866, 0)
  - plane n(0, 0.866, 0.5), n·p = 8.5442; extent (-76.75, 9.433, 0)..(-75.25, 9.866, 0.75)
  - plane n(0, 0, 1), n·p = 0.75; extent (-76.75, 8.567, 0.75)..(-75.25, 9.433, 0.75)
  - plane n(0, -0.866, 0.5), n·p = -7.0442; extent (-76.75, 8.134, 0)..(-75.25, 8.567, 0.75)
  - torus axis dir(1, 0, 0) centre (-75.5, 9, 0) major R1.65 minor r0.25; extent (-75.5, 7.1, -1.9)..(-75.25, 10.9, 0)
  - torus axis dir(1, 0, 0) centre (-75.5, 0, -9) major R1.65 minor r0.25; extent (-75.5, -1.9, -10.9)..(-75.25, 1.9, -9)
  - torus axis dir(1, 0, 0) centre (-75.5, -9, 0) major R1.65 minor r0.25; extent (-75.5, -10.9, -1.9)..(-75.25, -7.1, 0)
  - torus axis dir(1, 0, 0) centre (-75.5, 0, 9) major R1.65 minor r0.25; extent (-75.5, -1.9, 7.1)..(-75.25, 1.9, 9)
  - cylinder axis dir(1, 0, 0) through (-76.1902, 10.8026, -2.325) R0.2; extent (-77.25, 10.8026, -2.325)..(-75.1304, 11.0026, -2.125)
  - cylinder axis dir(0, -1, 0) through (-75.2, 9.9361, -2.325) R0.2; extent (-75.2, 9, -2.325)..(-75, 10.8723, -2.125)
  - cylinder axis dir(1, 0, 0) through (-76.2728, 10.8026, 2.325) R0.2; extent (-77.25, 10.9982, 2.325)..(-75.2956, 11.0026, 2.3671)
  - torus axis dir(1, 0, 0) centre (-75.2, 9, 0) major R2.325 minor r0.2; extent (-75.2, 6.675, -2.325)..(-75, 9, 2.325)
  - cylinder axis dir(0, 1, 0) through (-75.2, 9.9361, 2.325) R0.2; extent (-75.2, 9, 2.125)..(-75, 10.8723, 2.325)
  - cylinder axis dir(1, 0, 0) through (-76.1902, -2.325, -10.8026) R0.2; extent (-77.25, -2.3671, -11.0026)..(-75.1304, -2.125, -10.8026)
  - cylinder axis dir(0, 0, 1) through (-75.2, -2.325, -9.9361) R0.2; extent (-75.2, -2.325, -10.8723)..(-75, -2.125, -9)
  - cylinder axis dir(1, 0, 0) through (-76.1902, 2.325, -10.8026) R0.2; extent (-77.25, 2.125, -11.0026)..(-75.1304, 2.3671, -10.8026)
  - torus axis dir(1, 0, 0) centre (-75.2, 0, -9) major R2.325 minor r0.2; extent (-75.2, -2.325, -9)..(-75, 2.325, -6.675)
  - cylinder axis dir(0, 0, -1) through (-75.2, 2.325, -9.9361) R0.2; extent (-75.2, 2.125, -10.8723)..(-75, 2.325, -9)
  - cylinder axis dir(1, 0, 0) through (-76.1902, -10.8026, -2.325) R0.2; extent (-77.25, -11.0026, -2.3671)..(-75.1304, -10.8026, -2.125)
  - cylinder axis dir(0, -1, 0) through (-75.2, -9.9361, -2.325) R0.2; extent (-75.2, -10.8723, -2.325)..(-75, -9, -2.125)
  - torus axis dir(1, 0, 0) centre (-75.2, -9, 0) major R2.325 minor r0.2; extent (-75.2, -9, 0)..(-75, -6.675, 2.325)
  - cylinder axis dir(1, 0, 0) through (-76.1902, -10.8026, 2.325) R0.2; extent (-77.25, -11.0026, 2.125)..(-75.1304, -10.8026, 2.3671)
  - cylinder axis dir(0, 1, 0) through (-75.2, -9.9361, 2.325) R0.2; extent (-75.2, -10.8723, 2.125)..(-75, -9, 2.325)
  - cylinder axis dir(1, 0, 0) through (-76.1902, 2.325, 10.8026) R0.2; extent (-77.25, 2.125, 10.8026)..(-75.1304, 2.3671, 11.0026)
  - cylinder axis dir(0, 0, -1) through (-75.2, 2.325, 9.9361) R0.2; extent (-75.2, 2.125, 9)..(-75, 2.325, 10.8723)
  - cylinder axis dir(1, 0, 0) through (-76.1902, -2.325, 10.8026) R0.2; extent (-77.25, -2.3671, 10.8026)..(-75.1304, -2.125, 11.0026)
  - torus axis dir(1, 0, 0) centre (-75.2, 0, 9) major R2.325 minor r0.2; extent (-75.2, -2.325, 6.675)..(-75, 2.325, 9)
  - cylinder axis dir(0, 0, 1) through (-75.2, -2.325, 9.9361) R0.2; extent (-75.2, -2.325, 9)..(-75, -2.125, 10.8723)
  - free-form (blend) face; extent (-79.1, 0.7449, -4.9516)..(-75.4925, 5.0075, 0.452)

### P07 Ball-spline nut body (137 faces)

Turned sleeve on the shaft: bore R5 (x 76.5 .. 106.5) with counterbores R6.5 at both ends (x 75 .. 76.5 and 106.5 .. 108), outer R10.5 (x 75 .. 88.5), R12.65 (to x 100.15), a 45 deg cone to R14 and R14 to x = 108, chamfers as listed. Four tapped holes M3 x 0.5 in the end face x = 108 on a circle of radius 11.5 at 0, 90, 180, 270 deg: thread modelled as a helical 60 deg V groove (crest flats 0.0625 at R1.5, root flats at R1.1752, pitch 0.5) from x = 103.25 to a 45 deg countersink at the mouth (cone to R1.5541 at x = 107.9459). The hand and phase of the thread were not measured (undetermined).

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (75.25, -6.5) – (75, -6.75) – (75, -10) – (75.5, -10.5) – (88.5, -10.5) – (88.5, -12.4) – (88.75, -12.65) – (100.15, -12.65) – (101.5, -14) – (107.7, -14) – (108, -13.7) – (108, -6.75) – (107.75, -6.5) – (106.5, -6.5) – (106.5, -5) – (76.5, -5) – (76.5, -6.5) – (75.25, -6.5)
  - loop: (88.5, 12.4) – (88.75, 12.65) – (100.15, 12.65) – (101.5, 14) – (107.7, 14) – (108, 13.7) – (108, 6.75) – (107.75, 6.5) – (106.5, 6.5) – (106.5, 5) – (76.5, 5) – (76.5, 6.5) – (75.25, 6.5) – (75, 6.75) – (75, 10) – (75.5, 10.5) – (88.5, 10.5) – (88.5, 12.4)
Axial section in the half-plane at 0 deg (coordinates x, r; negative r = the opposite half-plane at 180 deg):
  - loop: (103.25, -10) – (103.25, -12.6752) – (103.4375, -13) – (103.5, -13) – (103.6875, -12.6752) – (103.75, -12.6752) – (103.9375, -13) – (104, -13) – (104.1875, -12.6752) – (104.25, -12.6752) – (104.4375, -13) – (104.5, -13) – (104.6875, -12.6752) – (104.75, -12.6752) – (104.9375, -13) – (105, -13) – (105.1875, -12.6752) – (105.25, -12.6752) – (105.4375, -13) – (105.5, -13) – (105.6875, -12.6752) – (105.75, -12.6752) – (105.9375, -13) – (106, -13) – (106.1875, -12.6752) – (106.25, -12.6752) – (106.4375, -13) – (106.5, -13) – (106.6875, -12.6752) – (106.75, -12.6752) – (106.9375, -13) – (107, -13) – (107.1875, -12.6752) – (107.25, -12.6752) – (107.4375, -13) – (107.5, -13) – (107.6632, -12.7173) – (107.9261, -12.9802) – (107.9375, -13) – (108, -13) – (108, -13.7) – (107.7, -14) – (101.5, -14) – (100.15, -12.65) – (88.75, -12.65) – (88.5, -12.4) – (88.5, -10.5) – (75.5, -10.5) – (75, -10) – (75, -6.75) – (75.25, -6.5) – (76.5, -6.5) – (76.5, -5) – (106.5, -5) – (106.5, -6.5) – (107.75, -6.5) – (108, -6.75) – (108, -10) – (107.9459, -10) – (107.8217, -10.1242) – (107.75, -10) – (107.6875, -10) – (107.5, -10.3248) – (107.4375, -10.3248) – (107.25, -10) – (107.1875, -10) – (107, -10.3248) – (106.9375, -10.3248) – (106.75, -10) – (106.6875, -10) – (106.5, -10.3248) – (106.4375, -10.3248) – (106.25, -10) – (106.1875, -10) – (106, -10.3248) – (105.9375, -10.3248) – (105.75, -10) – (105.6875, -10) – (105.5, -10.3248) – (105.4375, -10.3248) – (105.25, -10) – (105.1875, -10) – (105, -10.3248) – (104.9375, -10.3248) – (104.75, -10) – (104.6875, -10) – (104.5, -10.3248) – (104.4375, -10.3248) – (104.25, -10) – (104.1875, -10) – (104, -10.3248) – (103.9375, -10.3248) – (103.75, -10) – (103.6875, -10) – (103.5, -10.3248) – (103.4375, -10.3248) – (103.25, -10)
  - loop: (103.25, 12.6752) – (103.25, 10) – (103.4375, 10.3248) – (103.5, 10.3248) – (103.6875, 10) – (103.75, 10) – (103.9375, 10.3248) – (104, 10.3248) – (104.1875, 10) – (104.25, 10) – (104.4375, 10.3248) – (104.5, 10.3248) – (104.6875, 10) – (104.75, 10) – (104.9375, 10.3248) – (105, 10.3248) – (105.1875, 10) – (105.25, 10) – (105.4375, 10.3248) – (105.5, 10.3248) – (105.6875, 10) – (105.75, 10) – (105.9375, 10.3248) – (106, 10.3248) – (106.1875, 10) – (106.25, 10) – (106.4375, 10.3248) – (106.5, 10.3248) – (106.6875, 10) – (106.75, 10) – (106.9375, 10.3248) – (107, 10.3248) – (107.1875, 10) – (107.25, 10) – (107.4375, 10.3248) – (107.5, 10.3248) – (107.6875, 10) – (107.75, 10) – (107.8217, 10.1242) – (107.9459, 10) – (108, 10) – (108, 6.75) – (107.75, 6.5) – (106.5, 6.5) – (106.5, 5) – (76.5, 5) – (76.5, 6.5) – (75.25, 6.5) – (75, 6.75) – (75, 10) – (75.5, 10.5) – (88.5, 10.5) – (88.5, 12.4) – (88.75, 12.65) – (100.15, 12.65) – (101.5, 14) – (107.7, 14) – (108, 13.7) – (108, 13) – (107.9375, 13) – (107.9261, 12.9802) – (107.6632, 12.7173) – (107.5, 13) – (107.4375, 13) – (107.25, 12.6752) – (107.1875, 12.6752) – (107, 13) – (106.9375, 13) – (106.75, 12.6752) – (106.6875, 12.6752) – (106.5, 13) – (106.4375, 13) – (106.25, 12.6752) – (106.1875, 12.6752) – (106, 13) – (105.9375, 13) – (105.75, 12.6752) – (105.6875, 12.6752) – (105.5, 13) – (105.4375, 13) – (105.25, 12.6752) – (105.1875, 12.6752) – (105, 13) – (104.9375, 13) – (104.75, 12.6752) – (104.6875, 12.6752) – (104.5, 13) – (104.4375, 13) – (104.25, 12.6752) – (104.1875, 12.6752) – (104, 13) – (103.9375, 13) – (103.75, 12.6752) – (103.6875, 12.6752) – (103.5, 13) – (103.4375, 13) – (103.25, 12.6752)
Cross-section at x = 105 (coordinates y, z):
  - loop: (-14, 0) – arc c(0, 0) R14 via (0, 14) – (14, 0) – arc c(0, 0) R14 via (0, -14) – (-14, 0)
  - loop: (5, 0) – arc c(0, 0) R5 via (0, -5) – (-5, 0) – arc c(0, 0) R5 via (0, 5) – (5, 0)
  - loop: (13, 0) – arc c(11.5, 0) R1.5 via (12.8884, 0.5677) – (12.5703, 1.0509) – blend curve via (10.9984, 1.24) – (10.3248, 0) – arc c(11.5, 0) R1.1752 via (10.4167, -0.4558) – (10.6614, -0.8234) – blend curve via (12.0016, -1.24) – (13, 0)
  - loop: (0, -13) – arc c(0, -11.5) R1.5 via (0.5677, -12.8884) – (1.0509, -12.5703) – blend curve via (1.24, -10.9984) – (0, -10.3248) – arc c(0, -11.5) R1.1752 via (-0.4558, -10.4167) – (-0.8234, -10.6614) – blend curve via (-1.24, -12.0016) – (0, -13)
  - loop: (-13, 0) – arc c(-11.5, 0) R1.5 via (-12.8884, -0.5677) – (-12.5703, -1.0509) – blend curve via (-10.9984, -1.24) – (-10.3248, 0) – arc c(-11.5, 0) R1.1752 via (-10.4167, 0.4558) – (-10.6614, 0.8234) – blend curve via (-12.0016, 1.24) – (-13, 0)
  - loop: (0, 13) – arc c(0, 11.5) R1.5 via (-0.5677, 12.8884) – (-1.0509, 12.5703) – blend curve via (-1.24, 10.9984) – (0, 10.3248) – arc c(0, 11.5) R1.1752 via (0.4558, 10.4167) – (0.8234, 10.6614) – blend curve via (1.24, 12.0016) – (0, 13)
Faces that are not surfaces of revolution about the X axis (104):
  - cone axis dir(1, 0, 0) through (107.8838, 0, 11.5) R1.5541, half-angle 45 deg; extent (107.8217, 0, 10)..(107.9459, 1.5, 12.6723)
  - cone axis dir(1, 0, 0) through (107.8045, 0, 11.5) R1.5541, half-angle 45 deg; extent (107.6632, -1.5, 10)..(107.9459, 0, 12.9905)
  - cone axis dir(1, 0, 0) through (107.8838, -11.5, 0) R1.5541, half-angle 45 deg; extent (107.8217, -12.6723, 0)..(107.9459, -10, 1.5)
  - cone axis dir(1, 0, 0) through (107.8045, -11.5, 0) R1.5541, half-angle 45 deg; extent (107.6632, -12.9905, -1.5)..(107.9459, -10, 0)
  - cone axis dir(1, 0, 0) through (107.8838, 0, -11.5) R1.5541, half-angle 45 deg; extent (107.8217, -1.5, -12.6723)..(107.9459, 0, -10)
  - cone axis dir(1, 0, 0) through (107.8045, 0, -11.5) R1.5541, half-angle 45 deg; extent (107.6632, 0, -12.9905)..(107.9459, 1.5, -10)
  - cone axis dir(1, 0, 0) through (107.8838, 11.5, 0) R1.5541, half-angle 45 deg; extent (107.8217, 10, -1.5)..(107.9459, 12.6723, 0)
  - cone axis dir(1, 0, 0) through (107.8045, 11.5, 0) R1.5541, half-angle 45 deg; extent (107.6632, 10, 0)..(107.9459, 12.9905, 1.5)
  - cylinder axis dir(1, 0, 0) through (103.8437, 11.5, 0) R1.5; extent (103.6875, 10, -1.5)..(104, 13, 0)
  - cylinder axis dir(1, 0, 0) through (104.3438, 11.5, 0) R1.5; extent (104.1875, 10, -1.5)..(104.5, 13, 0)
  - cylinder axis dir(1, 0, 0) through (104.8437, 11.5, 0) R1.5; extent (104.6875, 10, -1.5)..(105, 13, 0)
  - cylinder axis dir(1, 0, 0) through (105.3437, 11.5, 0) R1.5; extent (105.1875, 10, -1.5)..(105.5, 13, 0)
  - cylinder axis dir(1, 0, 0) through (105.8438, 11.5, 0) R1.5; extent (105.6875, 10, -1.5)..(106, 13, 0)
  - cylinder axis dir(1, 0, 0) through (106.3437, 11.5, 0) R1.5; extent (106.1875, 10, -1.5)..(106.5, 13, 0)
  - cylinder axis dir(1, 0, 0) through (106.8437, 11.5, 0) R1.5; extent (106.6875, 10, -1.5)..(107, 13, 0)
  - cylinder axis dir(1, 0, 0) through (107.3437, 11.5, 0) R1.5; extent (107.1875, 10, -1.5)..(107.5, 13, 0)
  - cylinder axis dir(1, 0, 0) through (107.8437, 11.5, 0) R1.5; extent (107.6875, 10, -1.5)..(108, 13, 0)
  - cylinder axis dir(1, 0, 0) through (107.5938, 11.5, 0) R1.5; extent (107.4375, 10, 0)..(107.75, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (103.5937, 11.5, 0) R1.5; extent (103.4375, 10, 0)..(103.75, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (104.0938, 11.5, 0) R1.5; extent (103.9375, 10, 0)..(104.25, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (104.5937, 11.5, 0) R1.5; extent (104.4375, 10, 0)..(104.75, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (105.0938, 11.5, 0) R1.5; extent (104.9375, 10, 0)..(105.25, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (105.5937, 11.5, 0) R1.5; extent (105.4375, 10, 0)..(105.75, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (106.0937, 11.5, 0) R1.5; extent (105.9375, 10, 0)..(106.25, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (106.5938, 11.5, 0) R1.5; extent (106.4375, 10, 0)..(106.75, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (107.0937, 11.5, 0) R1.5; extent (106.9375, 10, 0)..(107.25, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (107.9687, 11.5, 0) R1.5; extent (107.9375, 10, 0)..(108, 13, 1.5)
  - cylinder axis dir(1, 0, 0) through (103.8437, 0, -11.5) R1.5; extent (103.6875, -1.5, -13)..(104, 0, -10)
  - cylinder axis dir(1, 0, 0) through (104.3438, 0, -11.5) R1.5; extent (104.1875, -1.5, -13)..(104.5, 0, -10)
  - cylinder axis dir(1, 0, 0) through (104.8437, 0, -11.5) R1.5; extent (104.6875, -1.5, -13)..(105, 0, -10)
  - cylinder axis dir(1, 0, 0) through (105.3437, 0, -11.5) R1.5; extent (105.1875, -1.5, -13)..(105.5, 0, -10)
  - cylinder axis dir(1, 0, 0) through (105.8438, 0, -11.5) R1.5; extent (105.6875, -1.5, -13)..(106, 0, -10)
  - cylinder axis dir(1, 0, 0) through (106.3437, 0, -11.5) R1.5; extent (106.1875, -1.5, -13)..(106.5, 0, -10)
  - cylinder axis dir(1, 0, 0) through (106.8437, 0, -11.5) R1.5; extent (106.6875, -1.5, -13)..(107, 0, -10)
  - cylinder axis dir(1, 0, 0) through (107.3437, 0, -11.5) R1.5; extent (107.1875, -1.5, -13)..(107.5, 0, -10)
  - cylinder axis dir(1, 0, 0) through (107.8437, 0, -11.5) R1.5; extent (107.6875, -1.5, -13)..(108, 0, -10)
  - cylinder axis dir(1, 0, 0) through (107.5938, 0, -11.5) R1.5; extent (107.4375, 0, -13)..(107.75, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (103.5937, 0, -11.5) R1.5; extent (103.4375, 0, -13)..(103.75, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (104.0938, 0, -11.5) R1.5; extent (103.9375, 0, -13)..(104.25, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (104.5937, 0, -11.5) R1.5; extent (104.4375, 0, -13)..(104.75, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (105.0938, 0, -11.5) R1.5; extent (104.9375, 0, -13)..(105.25, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (105.5937, 0, -11.5) R1.5; extent (105.4375, 0, -13)..(105.75, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (106.0937, 0, -11.5) R1.5; extent (105.9375, 0, -13)..(106.25, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (106.5938, 0, -11.5) R1.5; extent (106.4375, 0, -13)..(106.75, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (107.0937, 0, -11.5) R1.5; extent (106.9375, 0, -13)..(107.25, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (107.9687, 0, -11.5) R1.5; extent (107.9375, 0, -13)..(108, 1.5, -10)
  - cylinder axis dir(1, 0, 0) through (103.8437, -11.5, 0) R1.5; extent (103.6875, -13, 0)..(104, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (104.3438, -11.5, 0) R1.5; extent (104.1875, -13, 0)..(104.5, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (104.8437, -11.5, 0) R1.5; extent (104.6875, -13, 0)..(105, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (105.3437, -11.5, 0) R1.5; extent (105.1875, -13, 0)..(105.5, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (105.8438, -11.5, 0) R1.5; extent (105.6875, -13, 0)..(106, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (106.3437, -11.5, 0) R1.5; extent (106.1875, -13, 0)..(106.5, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (106.8437, -11.5, 0) R1.5; extent (106.6875, -13, 0)..(107, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (107.3437, -11.5, 0) R1.5; extent (107.1875, -13, 0)..(107.5, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (107.8437, -11.5, 0) R1.5; extent (107.6875, -13, 0)..(108, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (107.5938, -11.5, 0) R1.5; extent (107.4375, -13, -1.5)..(107.75, -10, 0)
  - cylinder axis dir(1, 0, 0) through (103.5937, -11.5, 0) R1.5; extent (103.4375, -13, -1.5)..(103.75, -10, 0)
  - cylinder axis dir(1, 0, 0) through (104.0938, -11.5, 0) R1.5; extent (103.9375, -13, -1.5)..(104.25, -10, 0)
  - cylinder axis dir(1, 0, 0) through (104.5937, -11.5, 0) R1.5; extent (104.4375, -13, -1.5)..(104.75, -10, 0)
  - cylinder axis dir(1, 0, 0) through (105.0938, -11.5, 0) R1.5; extent (104.9375, -13, -1.5)..(105.25, -10, 0)
  - cylinder axis dir(1, 0, 0) through (105.5937, -11.5, 0) R1.5; extent (105.4375, -13, -1.5)..(105.75, -10, 0)
  - cylinder axis dir(1, 0, 0) through (106.0937, -11.5, 0) R1.5; extent (105.9375, -13, -1.5)..(106.25, -10, 0)
  - cylinder axis dir(1, 0, 0) through (106.5938, -11.5, 0) R1.5; extent (106.4375, -13, -1.5)..(106.75, -10, 0)
  - cylinder axis dir(1, 0, 0) through (107.0937, -11.5, 0) R1.5; extent (106.9375, -13, -1.5)..(107.25, -10, 0)
  - cylinder axis dir(1, 0, 0) through (107.9687, -11.5, 0) R1.5; extent (107.9375, -13, -1.5)..(108, -10, 0)
  - cylinder axis dir(1, 0, 0) through (103.8437, 0, 11.5) R1.5; extent (103.6875, 0, 10)..(104, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (104.3438, 0, 11.5) R1.5; extent (104.1875, 0, 10)..(104.5, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (104.8437, 0, 11.5) R1.5; extent (104.6875, 0, 10)..(105, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (105.3437, 0, 11.5) R1.5; extent (105.1875, 0, 10)..(105.5, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (105.8438, 0, 11.5) R1.5; extent (105.6875, 0, 10)..(106, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (106.3437, 0, 11.5) R1.5; extent (106.1875, 0, 10)..(106.5, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (106.8437, 0, 11.5) R1.5; extent (106.6875, 0, 10)..(107, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (107.3437, 0, 11.5) R1.5; extent (107.1875, 0, 10)..(107.5, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (107.8437, 0, 11.5) R1.5; extent (107.6875, 0, 10)..(108, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (107.5938, 0, 11.5) R1.5; extent (107.4375, -1.5, 10)..(107.75, 0, 13)
  - cylinder axis dir(1, 0, 0) through (103.5937, 0, 11.5) R1.5; extent (103.4375, -1.5, 10)..(103.75, 0, 13)
  - cylinder axis dir(1, 0, 0) through (104.0938, 0, 11.5) R1.5; extent (103.9375, -1.5, 10)..(104.25, 0, 13)
  - cylinder axis dir(1, 0, 0) through (104.5937, 0, 11.5) R1.5; extent (104.4375, -1.5, 10)..(104.75, 0, 13)
  - cylinder axis dir(1, 0, 0) through (105.0938, 0, 11.5) R1.5; extent (104.9375, -1.5, 10)..(105.25, 0, 13)
  - cylinder axis dir(1, 0, 0) through (105.5937, 0, 11.5) R1.5; extent (105.4375, -1.5, 10)..(105.75, 0, 13)
  - cylinder axis dir(1, 0, 0) through (106.0937, 0, 11.5) R1.5; extent (105.9375, -1.5, 10)..(106.25, 0, 13)
  - cylinder axis dir(1, 0, 0) through (106.5938, 0, 11.5) R1.5; extent (106.4375, -1.5, 10)..(106.75, 0, 13)
  - cylinder axis dir(1, 0, 0) through (107.0937, 0, 11.5) R1.5; extent (106.9375, -1.5, 10)..(107.25, 0, 13)
  - cylinder axis dir(1, 0, 0) through (107.9687, 0, 11.5) R1.5; extent (107.9375, -1.5, 10)..(108, 0, 13)
  - cylinder axis dir(1, 0, 0) through (103.375, 0, 11.5) R1.5; extent (103.25, 0, 10)..(103.5, 1.5, 13)
  - cylinder axis dir(1, 0, 0) through (103.375, -11.5, 0) R1.5; extent (103.25, -13, 0)..(103.5, -10, 1.5)
  - cylinder axis dir(1, 0, 0) through (103.375, 0, -11.5) R1.5; extent (103.25, -1.5, -13)..(103.5, 0, -10)
  - cylinder axis dir(1, 0, 0) through (103.375, 11.5, 0) R1.5; extent (103.25, 10, -1.5)..(103.5, 13, 0)
  - free-form (blend) face; extent (103.25, 10, -1.5)..(107.9459, 13, 1.5)
  - free-form (blend) face; extent (103.25, 10, -1.5)..(107.9459, 13, 1.5)
  - cone axis dir(1, 0, 0) through (107.7736, 11.5, 0) R1.5541, half-angle 45 deg; extent (107.6211, 11.4452, -1.2003)..(107.9261, 12.9802, 0)
  - free-form (blend) face; extent (103.25, 10.3248, -1.1752)..(107.6211, 12.6752, 1.1752)
  - free-form (blend) face; extent (103.25, -1.5, -13)..(107.9459, 1.5, -10)
  - free-form (blend) face; extent (103.25, -1.5, -13)..(107.9459, 1.5, -10)
  - cone axis dir(1, 0, 0) through (107.7736, 0, -11.5) R1.5541, half-angle 45 deg; extent (107.6211, -1.2003, -12.9802)..(107.9261, 0, -11.4452)
  - free-form (blend) face; extent (103.25, -1.1752, -12.6752)..(107.6211, 1.1752, -10.3248)
  - free-form (blend) face; extent (103.25, -13, -1.5)..(107.9459, -10, 1.5)
  - free-form (blend) face; extent (103.25, -13, -1.5)..(107.9459, -10, 1.5)
  - cone axis dir(1, 0, 0) through (107.7736, -11.5, 0) R1.5541, half-angle 45 deg; extent (107.6211, -12.9802, 0)..(107.9261, -11.4452, 1.2003)
  - free-form (blend) face; extent (103.25, -12.6752, -1.1752)..(107.6211, -10.3248, 1.1752)
  - free-form (blend) face; extent (103.25, -1.5, 10)..(107.9459, 1.5, 13)
  - free-form (blend) face; extent (103.25, -1.5, 10)..(107.9459, 1.5, 13)
  - cone axis dir(1, 0, 0) through (107.7736, 0, 11.5) R1.5541, half-angle 45 deg; extent (107.6211, 0, 11.4452)..(107.9261, 1.2003, 12.9802)
  - free-form (blend) face; extent (103.25, -1.1752, 10.3248)..(107.6211, 1.1752, 12.6752)

### P08 Ball-spline nut flange (57 faces)

Flange ring, diameter 48, 3 thick (x 96 .. 99) with a hub to x = 88.5; bore R14.55; a circumferential groove R1 (centre (x, r) = (92.5, 18.5)) and a step R17.8. Four through holes diameter 3.4 on the 42 bolt circle at 0, 90, 180, 270 deg with 0.25 x 45 deg chamfers on both faces. One radial lubrication hole diameter 0.9 along Z on the +Z side at x = 92.5, from the groove bottom into the bore.

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (91.634, 18) – arc c(92.5, 18.5) R1 via (92, 17.634) – (92.5, 17.5) – arc c(92.5, 18.5) R1 via (93, 17.634) – (93.366, 18) – (95, 18) – (95.3925, 17.8) – (95.8, 17.8) – arc c(95.8, 18) R0.2 via (95.9414, 17.8586) – (96, 18) – (96, 23.7) – (96.3, 24) – (98.7, 24) – (99, 23.7) – (99, 14.8) – (98.75, 14.55) – (88.75, 14.55) – (88.5, 14.8) – (88.5, 17.2) – arc c(89.3, 17.2) R0.8 via (88.7343, 17.7657) – (89.3, 18) – (91.634, 18)
  - loop: (92.5, -17.5) – arc c(92.5, -18.5) R1 via (92, -17.634) – (91.634, -18) – (89.3, -18) – arc c(89.3, -17.2) R0.8 via (88.7343, -17.7657) – (88.5, -17.2) – (88.5, -14.8) – (88.75, -14.55) – (98.75, -14.55) – (99, -14.8) – (99, -23.7) – (98.7, -24) – (96.3, -24) – (96, -23.7) – (96, -18) – arc c(95.8, -18) R0.2 via (95.9414, -17.8586) – (95.8, -17.8) – (95.3925, -17.8) – (95, -18) – (93.366, -18) – arc c(92.5, -18.5) R1 via (93, -17.634) – (92.5, -17.5)
Faces that are not surfaces of revolution about the X axis (26):
  - cone axis dir(-1, 0, 0) through (96.125, -21, 0) R1.7, half-angle 45 deg; extent (96, -22.95, -1.95)..(96.25, -21, 1.95)
  - cone axis dir(1, 0, 0) through (98.875, -21, 0) R1.7, half-angle 45 deg; extent (98.75, -22.95, -1.95)..(99, -21, 1.95)
  - cone axis dir(-1, 0, 0) through (96.125, 21, 0) R1.7, half-angle 45 deg; extent (96, 19.05, -1.95)..(96.25, 21, 1.95)
  - cone axis dir(1, 0, 0) through (98.875, 21, 0) R1.7, half-angle 45 deg; extent (98.75, 19.05, -1.95)..(99, 21, 1.95)
  - cone axis dir(-1, 0, 0) through (96.125, 0, -21) R1.7, half-angle 45 deg; extent (96, -1.95, -22.95)..(96.25, 0, -19.05)
  - cone axis dir(1, 0, 0) through (98.875, 0, -21) R1.7, half-angle 45 deg; extent (98.75, -1.95, -22.95)..(99, 0, -19.05)
  - cone axis dir(-1, 0, 0) through (96.125, 0, 21) R1.7, half-angle 45 deg; extent (96, -1.95, 19.05)..(96.25, 0, 22.95)
  - cone axis dir(1, 0, 0) through (98.875, 0, 21) R1.7, half-angle 45 deg; extent (98.75, -1.95, 19.05)..(99, 0, 22.95)
  - cylinder axis dir(0, 0, -1) through (92.5, 0, 16.075) R0.45; extent (92.05, -0.45, 14.543)..(92.95, 0, 17.607)
  - cylinder axis dir(1, 0, 0) through (97.5, 0, 21) R1.7; extent (96.25, 0, 19.3)..(98.75, 1.7, 22.7)
  - cylinder axis dir(1, 0, 0) through (97.5, -21, 0) R1.7; extent (96.25, -22.7, 0)..(98.75, -19.3, 1.7)
  - cylinder axis dir(1, 0, 0) through (97.5, 0, -21) R1.7; extent (96.25, -1.7, -22.7)..(98.75, 0, -19.3)
  - cylinder axis dir(1, 0, 0) through (97.5, 21, 0) R1.7; extent (96.25, 19.3, -1.7)..(98.75, 22.7, 0)
  - cylinder axis dir(1, 0, 0) through (97.5, 21, 0) R1.7; extent (96.25, 19.3, 0)..(98.75, 22.7, 1.7)
  - cylinder axis dir(1, 0, 0) through (97.5, 0, -21) R1.7; extent (96.25, 0, -22.7)..(98.75, 1.7, -19.3)
  - cylinder axis dir(1, 0, 0) through (97.5, -21, 0) R1.7; extent (96.25, -22.7, -1.7)..(98.75, -19.3, 0)
  - cylinder axis dir(1, 0, 0) through (97.5, 0, 21) R1.7; extent (96.25, -1.7, 19.3)..(98.75, 0, 22.7)
  - cylinder axis dir(0, 0, -1) through (92.5, 0, 16.075) R0.45; extent (92.05, 0, 14.543)..(92.95, 0.45, 17.607)
  - cone axis dir(1, 0, 0) through (98.875, 0, 21) R1.7, half-angle 45 deg; extent (98.75, 0, 19.05)..(99, 1.95, 22.95)
  - cone axis dir(-1, 0, 0) through (96.125, 0, 21) R1.7, half-angle 45 deg; extent (96, 0, 19.05)..(96.25, 1.95, 22.95)
  - cone axis dir(1, 0, 0) through (98.875, 0, -21) R1.7, half-angle 45 deg; extent (98.75, 0, -22.95)..(99, 1.95, -19.05)
  - cone axis dir(-1, 0, 0) through (96.125, 0, -21) R1.7, half-angle 45 deg; extent (96, 0, -22.95)..(96.25, 1.95, -19.05)
  - cone axis dir(1, 0, 0) through (98.875, 21, 0) R1.7, half-angle 45 deg; extent (98.75, 21, -1.95)..(99, 22.95, 1.95)
  - cone axis dir(-1, 0, 0) through (96.125, 21, 0) R1.7, half-angle 45 deg; extent (96, 21, -1.95)..(96.25, 22.95, 1.95)
  - cone axis dir(1, 0, 0) through (98.875, -21, 0) R1.7, half-angle 45 deg; extent (98.75, -21, -1.95)..(99, -19.05, 1.95)
  - cone axis dir(-1, 0, 0) through (96.125, -21, 0) R1.7, half-angle 45 deg; extent (96, -21, -1.95)..(96.25, -19.05, 1.95)

### P09 Ball-spline nut collar ring (6 faces)

Plain ring: inner R12.65, outer R14.55, x 89.5 .. 98 (no chamfers).

Axial section in the half-plane at 45 deg (coordinates x, r; negative r = the opposite half-plane at 225 deg):
  - loop: (98, -12.65) – (89.5, -12.65) – (89.5, -14.55) – (98, -14.55) – (98, -12.65)
  - loop: (98, 14.55) – (89.5, 14.55) – (89.5, 12.65) – (98, 12.65) – (98, 14.55)

### P10 Ball-spline seal (2 identical bodies) (13 faces)

Thin seal ring 1.2 thick, outer R6.5, whose bore is the shaft section without the ball groove: circle R5 plus four lobes R1.24 about the spline groove axes (60, 120, 240, 300 deg at radius 5.8), so the lobes fill the spline grooves. P10-a at x 75.3 .. 76.5, P10-b at x 106.5 .. 107.7 (same orientation, translation only).

Axial section in the half-plane at 0 deg (coordinates x, r; negative r = the opposite half-plane at 180 deg):
  - loop: (76.5, 5) – (75.3, 5) – (75.3, 6.5) – (76.5, 6.5) – (76.5, 5)
  - loop: (76.5, -6.5) – (76.5, -5) – (75.3, -5) – (75.3, -6.5) – (76.5, -6.5)
Cross-section at x = 75.9 (coordinates y, z):
  - loop: (-6.5, 0) – arc c(0, 0) R6.5 via (0, 6.5) – (6.5, 0) – arc c(0, 0) R6.5 via (0, -6.5) – (-6.5, 0)
  - loop: (-5, 0) – arc c(0, 0) R5 via (-4.5333, 2.1094) – (-3.2202, 3.825) – arc c(-2.9, 5.0229) R1.24 via (-2.28, 3.9491) – (-1.7025, 4.7012) – arc c(0, 0) R5 via (0, 5) – (1.7025, 4.7012) – arc c(2.9, 5.0229) R1.24 via (2.28, 3.9491) – (3.2202, 3.825) – arc c(0, 0) R5 via (5, -0.0001) – (3.2201, -3.8251) – arc c(2.9, -5.0231) R1.24 via (2.28, -3.9492) – (1.7025, -4.7012) – arc c(0, 0) R5 via (0, -5) – (-1.7025, -4.7012) – arc c(-2.9, -5.0231) R1.24 via (-2.28, -3.9492) – (-3.2201, -3.8251) – arc c(0, 0) R5 via (-4.5332, -2.1095) – (-5, 0)
Faces that are not surfaces of revolution about the X axis (4):
  - cylinder axis dir(1, 0, 0) through (75.9, -2.9, -5.0231) R1.24; extent (75.3, -3.2201, -4.7012)..(76.5, -1.7025, -3.7831)
  - cylinder axis dir(1, 0, 0) through (75.9, 2.9, -5.0231) R1.24; extent (75.3, 1.7025, -4.7012)..(76.5, 3.2201, -3.7831)
  - cylinder axis dir(1, 0, 0) through (75.9, -2.9, 5.0229) R1.24; extent (75.3, -3.2202, 3.7829)..(76.5, -1.7025, 4.7012)
  - cylinder axis dir(1, 0, 0) through (75.9, 2.9, 5.0229) R1.24; extent (75.3, 1.7025, 3.7829)..(76.5, 3.2202, 4.7012)

## 5. Assembly

All bodies are coaxial with the X axis and placed as the coordinates above state. Contacts: nut bores R5 on the shaft surface, collar rings on the nut bodies, seals in the counterbores of P07. One overlap exists in the original: P02 / P05 40.389 mm³ (the cap screw shanks of P05 inside the plain holes of P02). Keep it.

## 6. Acceptance targets

| Body | Volume (mm³) | Area (mm²) | CoM x | CoM y | CoM z | x min | x max | y min | y max | z min | z max | Faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 18793.197 | 13857.103 | 0.2783 | -0.0002 | -0.0001 | -150.0000 | 150.0000 | -5.0000 | 5.0000 | -5.0000 | 5.0000 | 230 |
| P02 | 10475.776 | 4671.521 | -93.3255 | 0.0000 | 0.0000 | -109.5000 | -79.1000 | -13.0000 | 13.0000 | -13.0000 | 13.0000 | 37 |
| P03 | 5505.290 | 4491.745 | -97.8069 | 0.0000 | -0.0051 | -101.5000 | -91.0000 | -24.0000 | 24.0000 | -24.0000 | 24.0000 | 59 |
| P04 | 1548.783 | 1963.370 | -96.2500 | 0.0000 | 0.0000 | -100.9000 | -91.6000 | -14.9000 | 14.9000 | -14.9000 | 14.9000 | 6 |
| P05 | 975.653 | 1503.736 | -106.0694 | 0.0000 | 0.0000 | -108.0000 | -100.6844 | -11.2500 | 11.2500 | -11.2500 | 11.2500 | 174 |
| P06 | 1225.284 | 1217.856 | -77.1232 | -0.0164 | 0.0207 | -79.1000 | -75.0000 | -11.2500 | 11.2500 | -11.2500 | 11.2500 | 127 |
| P07 | 12409.652 | 4787.273 | 93.8841 | 0.0000 | 0.0000 | 75.0000 | 108.0000 | -14.0000 | 14.0000 | -14.0000 | 14.0000 | 137 |
| P08 | 5845.289 | 4535.377 | 95.2164 | 0.0000 | -0.0052 | 88.5000 | 99.0000 | -24.0000 | 24.0000 | -24.0000 | 24.0000 | 57 |
| P09 | 1380.039 | 1777.388 | 93.7500 | 0.0000 | 0.0000 | 89.5000 | 98.0000 | -14.5500 | 14.5500 | -14.5500 | 14.5500 | 6 |
| P10-a | 67.567 | 200.205 | 75.9000 | 0.0000 | 0.0000 | 75.3000 | 76.5000 | -6.5000 | 6.5000 | -6.5000 | 6.5000 | 13 |
| P10-b | 67.567 | 200.205 | 107.1000 | 0.0000 | 0.0000 | 106.5000 | 107.7000 | -6.5000 | 6.5000 | -6.5000 | 6.5000 | 13 |

Assembly: volume 58294.096 mm³, area 39205.779 mm², centre of mass (0.0934, -0.0004, -0.0006), box x -150 .. 150, y -24 .. 24, z -24 .. 24.

## 7. Undetermined items and source notes

- Exact shape of the free-form faces: the ball groove run-out at x ≈ 121 on P01, the helical lip of P06, the blends at
  the radial lubrication holes of P03, and the thread flanks of P05's screws and P07's tapped holes (given by their
  extents, pitch 0.5, 60 deg profile). Hand and phase of these M3 threads: undetermined.
- The shaft ball groove's bottom is at diameter 8.6 in the model; the catalogue drawing prints "Root Diameter 9.27".
  Follow the model.
- Materials (not geometry): carbon steel shaft, alloy steel nuts.
