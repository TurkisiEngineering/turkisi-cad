# Design specification: electromagnetic clutch-brake unit (finned housing, output shaft with key, input hub, coiled lead wires)

Rebuild the assembly below as **27 separate solids** in one STEP file, in the global frame given in §1. Every number is
measured on the reference model. Anything that could not be measured is listed in §7 as *undetermined*; do not invent it.

## 1. Units and global frame

- **Unit: inch.** All coordinates and sizes in this document are inches (the STEP must be written in a consistent unit;
  1 in = 25.4 mm).
- **Z axis = common axis** of the shaft, rings, hub and housing bores. The output shaft sticks out toward **−Z** (front);
  the input hub and the rear clamps are at **+Z** (rear).
- **+Y = top**: the side with the flat land, the wire entry boss and the round plug. The coiled lead wires hang out to −X.
- **Origin** on the axis. Key planes: housing front spigot face z = −1.5095; housing front face z = −1.3095; housing rear
  face z = +3.3505; shaft front end z = −3.3705.
- Assembly bounding box: x −9.3000 … +3.3750, y −3.3750 … +4.2615, z −3.3705 … +4.1158.
- Do not move, re-centre or rotate anything: the result is compared with the reference **without alignment**.
- "Mirror in X" below means mirror about the plane x = 0. Unless a section says otherwise, the housing is symmetric about
  x = 0.
- Notation for outlines (§4.1): a list starts at a point; `L x,y` = straight line to (x, y); `A xm,ym x,y rR` = circular arc
  through the point (xm, ym) to the end point (x, y), radius R (three-point arc). Arcs written with `r3.3750`, `r2.8125`,
  `r3.2001`, `r3.3000`, `r3.2201`, `r2.2338`, `r2.2540` … are centred on the axis (0, 0).

## 2. Product description and source simplifications

An electromagnetic clutch-brake unit that mounts between a motor and the driven machine. A cast aluminium-style
finned housing (one solid, no internal cavity: the reference models it as a full block with recesses only at the front and
rear) carries a front plate, four internal rings at the front, an output shaft with a key, an input hub at the rear with
two set screws and an internal retaining ring, two formed rear clamps held by four socket nuts on four hex standoff studs,
a round plug on the top land and two lead wires that leave the top entry boss, run over the top of the housing and end in a
four-turn coil with bare conductor tips.

Simplifications that are in the reference and must be kept:
- The housing is a solid block (no coil, armature or bearings inside). Its fins, recesses, bores and rounds are modelled.
- The four hex standoff studs carry a **modelled helical internal thread** (20 threads per inch) at their front end; all
  other threads are absent (the socket nuts and set-screw holes are plain).
- The lead wires are plain round rods of diameter 0.100 swept along arcs, straight runs and a helix; the conductor tips are
  rods of diameter 0.080.
- Many edges carry small rounds (R0.01–R0.10). The ones that matter for the shape are given; §4.1.8 lists the rule for the
  rest.

## 3. Part list (27 solids)

| Name | Count | Kind | Description | Equivalence group |
|---|---|---|---|---|
| P01 | 1 | custom | finned housing | P01 |
| P02 | 1 | custom | front plate (sheet 0.03125) | P02 |
| P03 | 1 | custom | output shaft Ø0.625 with keyway and centre hole | P03 |
| P04 | 1 | custom | input hub Ø1.375 / Ø1.000 with Ø0.625 keyed bore | P04 |
| P05 | 1 | custom | shaft key 0.188 × 0.188 × 1.1875 | P05 |
| P06 | 1 | custom | ring A, OD 2.3125 / ID 1.875 | P06 |
| P07 | 1 | custom | ring B, OD 1.855 / ID 1.6675 | P07 |
| P08 | 1 | custom | ring C, OD 0.9675 / ID 0.780 | P08 |
| P09 | 1 | custom | ring D, OD 1.6475 / ID 0.9875 | P09 |
| P10 | 1 | hardware | internal retaining ring (sheet 0.030) | P10 |
| P11-a, P11-b | 2 | custom | formed rear clamp (sheet 0.020); P11-b = P11-a rotated 180° about Z | P11 |
| P12 | 1 | custom | round plug (frustum) on the top land | P12 |
| P13 | 1 | custom | lead wire A (starts at x = −0.051) | P13 |
| P14 | 1 | custom | lead wire B (starts at x = +0.051) | P14 |
| P15-a, P15-b | 2 | custom | bare conductor tip (rod Ø0.080 × 0.250) | P15 |
| H1-a … H1-d | 4 | hardware | round socket nut Ø0.3125 × 0.188 | H1 |
| H2-a … H2-d | 4 | hardware | hex standoff stud (hex 0.4375 with Ø0.250 stud) | H2 |
| H3-a, H3-b | 2 | hardware | set screw Ø0.1876 × 0.1929 | H3 |

Placements of the repeated parts are in §4 (each body is separate; do not unite anything).

## 4. Part geometry

### 4.1 P01 Finned housing (one solid, 1591 faces in the reference)

The housing spans z −1.5095 … +3.3505 and fits inside a Ø6.750 circle. Build it as a stack of prismatic layers along Z
(each layer = one closed XY cross-section extruded between two z values), then cut the recesses and bores, then add the rounds.
The cross-sections are built from two exact master outlines, **B** (main body) and **R** (rear), listed in §4.1.1 and
§4.1.2.

#### 4.1.1 Master outline B (the main finned outline, valid in z −0.3095 … +1.1555)

Half outline for x ≥ 0, clockwise from the top of the y-axis to the bottom of the y-axis; mirror it in X to close the loop.
It consists of: a core circle R2.8125; a flat top land y = 3.2906 for |x| ≤ 0.75; two top fins per side; a diagonal bolt boss
in each corner (tip on R3.375, flanks at 45°); eight side fins per side (width 0.150; the two outermost tip on R3.375, the
six inner ones tip on R3.2001); eleven bottom fins (width 0.150, x pitch 0.3044, tips on R3.375). Fin tips are rounded
R0.06, boss tips R0.05, boss roots R0.0625, inner side-fin roots R0.03.

```
start 0.0000,3.2906
L 0.7000,3.2906
A 0.7354,3.2760 0.7500,3.2406 r0.0500
L 0.7500,2.7107
A 0.8880,2.6686 1.0236,2.6196 r2.8125
L 1.0236,3.1329
A 1.0488,3.1818 1.1032,3.1896 r0.0600
A 1.1185,3.1843 1.1337,3.1789 r3.3750
A 1.1626,3.1570 1.1736,3.1224 r0.0600
L 1.1736,2.5560
A 1.3123,2.4876 1.4471,2.4116 r2.8125
L 1.4471,2.9526
A 1.4758,3.0038 1.5344,3.0060 r0.0600
A 1.5497,2.9982 1.5649,2.9903 r3.3750
A 1.5884,2.9682 1.5971,2.9371 r0.0600
L 1.5971,2.2341
A 1.6357,2.1764 1.7038,2.1899 r0.0625
L 2.0989,2.5850
A 2.1320,2.5996 2.1663,2.5880 r0.0500
A 2.3865,2.3865 2.5880,2.1663 r3.3750
A 2.5996,2.1320 2.5850,2.0989 r0.0500
L 2.1899,1.7038
A 2.1764,1.6357 2.2341,1.5971 r0.0625
L 2.9371,1.5971
A 2.9682,1.5884 2.9903,1.5649 r0.0600
A 2.9982,1.5497 3.0060,1.5344 r3.3750
A 3.0038,1.4758 2.9526,1.4471 r0.0600
L 2.4116,1.4471
A 2.4752,1.3355 2.5336,1.2211 r2.8125
A 2.5446,1.2087 2.5606,1.2041 r0.0300
L 2.9242,1.2041
A 2.9581,1.1936 2.9801,1.1659 r0.0600
A 2.9861,1.1507 2.9919,1.1354 r3.2001
A 2.9852,1.0800 2.9358,1.0541 r0.0600
L 2.6516,1.0541
A 2.6269,1.0411 2.6236,1.0133 r0.0300
A 2.6566,0.9233 2.6866,0.8322 r2.8125
A 2.6974,0.8169 2.7152,0.8111 r0.0300
L 3.0489,0.8111
A 3.0859,0.7983 3.1072,0.7654 r0.0600
A 3.1109,0.7501 3.1146,0.7348 r3.2001
A 3.1032,0.6838 3.0562,0.6611 r0.0600
L 2.7716,0.6611
A 2.7481,0.6498 2.7423,0.6244 r0.0300
A 2.7613,0.5341 2.7773,0.4433 r2.8125
A 2.7875,0.4252 2.8070,0.4180 r0.0300
L 3.1196,0.4180
A 3.1595,0.4028 3.1792,0.3649 r0.0600
A 3.1809,0.3496 3.1826,0.3343 r3.2001
A 3.1675,0.2879 3.1229,0.2680 r0.0600
L 2.8325,0.2680
A 2.8104,0.2583 2.8026,0.2355 r0.0300
A 2.8125,0.0000 2.8026,-0.2355 r2.8125
A 2.8104,-0.2583 2.8325,-0.2680 r0.0300
L 3.1229,-0.2680
A 3.1675,-0.2879 3.1826,-0.3343 r0.0600
A 3.1809,-0.3496 3.1792,-0.3649 r3.2001
A 3.1595,-0.4028 3.1196,-0.4180 r0.0600
L 2.8070,-0.4180
A 2.7875,-0.4252 2.7773,-0.4433 r0.0300
A 2.7613,-0.5341 2.7423,-0.6244 r2.8125
A 2.7481,-0.6498 2.7716,-0.6611 r0.0300
L 3.0562,-0.6611
A 3.1032,-0.6838 3.1146,-0.7348 r0.0600
A 3.1109,-0.7501 3.1072,-0.7654 r3.2001
A 3.0859,-0.7983 3.0489,-0.8111 r0.0600
L 2.7152,-0.8111
A 2.6974,-0.8169 2.6866,-0.8322 r0.0300
A 2.6566,-0.9233 2.6236,-1.0133 r2.8125
A 2.6269,-1.0411 2.6516,-1.0541 r0.0300
L 2.9358,-1.0541
A 2.9852,-1.0800 2.9919,-1.1354 r0.0600
A 2.9861,-1.1507 2.9801,-1.1659 r3.2001
A 2.9581,-1.1936 2.9242,-1.2041 r0.0600
L 2.5606,-1.2041
A 2.5446,-1.2087 2.5336,-1.2211 r0.0300
A 2.4752,-1.3355 2.4116,-1.4471 r2.8125
L 2.9526,-1.4471
A 3.0038,-1.4758 3.0060,-1.5344 r0.0600
A 2.9982,-1.5497 2.9903,-1.5649 r3.3750
A 2.9682,-1.5884 2.9371,-1.5971 r0.0600
L 2.2341,-1.5971
A 2.1764,-1.6357 2.1899,-1.7038 r0.0625
L 2.5850,-2.0989
A 2.5996,-2.1320 2.5880,-2.1663 r0.0500
A 2.3865,-2.3865 2.1663,-2.5880 r3.3750
A 2.1320,-2.5996 2.0989,-2.5850 r0.0500
L 1.7038,-2.1899
A 1.6357,-2.1764 1.5971,-2.2341 r0.0625
L 1.5971,-2.9371
A 1.5884,-2.9682 1.5649,-2.9903 r0.0600
A 1.5497,-2.9982 1.5344,-3.0060 r3.3750
A 1.4758,-3.0038 1.4471,-2.9526 r0.0600
L 1.4471,-2.4116
A 1.3706,-2.4559 1.2927,-2.4978 r2.8125
L 1.2927,-3.0773
A 1.2824,-3.1109 1.2550,-3.1330 r0.0600
A 1.2398,-3.1391 1.2245,-3.1451 r3.3750
A 1.1688,-3.1386 1.1427,-3.0891 r0.0600
L 1.1427,-2.5699
A 1.0660,-2.6027 0.9883,-2.6332 r2.8125
L 0.9883,-3.1824
A 0.9763,-3.2184 0.9451,-3.2400 r0.0600
A 0.9298,-3.2444 0.9145,-3.2487 r3.3750
A 0.8621,-3.2388 0.8383,-3.1910 r0.0600
L 0.8383,-2.6847
A 0.7614,-2.7075 0.6838,-2.7281 r2.8125
L 0.6838,-3.2558
A 0.6701,-3.2940 0.6351,-3.3147 r0.0600
A 0.6199,-3.3176 0.6046,-3.3204 r3.3750
A 0.5554,-3.3075 0.5338,-3.2614 r0.0600
L 0.5338,-2.7614
A 0.4568,-2.7752 0.3794,-2.7868 r2.8125
L 0.3794,-3.2996
A 0.3638,-3.3399 0.3252,-3.3593 r0.0600
A 0.3100,-3.3607 0.2947,-3.3621 r3.3750
A 0.2489,-3.3466 0.2294,-3.3023 r0.0600
L 0.2294,-2.8031
A 0.1523,-2.8084 0.0750,-2.8115 r2.8125
L 0.0750,-3.3150
A 0.0575,-3.3573 0.0153,-3.3750 r0.0600
A ... to 0.0000,-3.3750  (arc r3.3750 centre 0.0000,0.0000)
```

Holes in B: four Ø0.250 holes centred (±2.0771, ±2.0771) (through the bosses).

#### 4.1.2 Master outline R (rear outline, valid in z +1.6555 … +3.1955)

Same convention (half for x ≥ 0, mirror in X). Differences from B: the six inner side fins per side are longer (tips on
R3.375), and on each side the three gaps between y = −0.268 … +0.268 and between |y| = 0.418 … 0.6611 are filled out to
R3.300.

```
start 0.0000,3.2906
L 0.7000,3.2906
A 0.7354,3.2760 0.7500,3.2406 r0.0500
L 0.7500,2.7107
A 0.8880,2.6686 1.0236,2.6196 r2.8125
L 1.0236,3.1329
A 1.0488,3.1818 1.1032,3.1896 r0.0600
A 1.1185,3.1843 1.1337,3.1789 r3.3750
A 1.1626,3.1570 1.1736,3.1224 r0.0600
L 1.1736,2.5560
A 1.3123,2.4876 1.4471,2.4116 r2.8125
L 1.4471,2.9526
A 1.4758,3.0038 1.5344,3.0060 r0.0600
A 1.5497,2.9982 1.5649,2.9903 r3.3750
A 1.5884,2.9682 1.5971,2.9371 r0.0600
L 1.5971,2.2341
A 1.6357,2.1764 1.7038,2.1899 r0.0625
L 2.0989,2.5850
A 2.1320,2.5996 2.1663,2.5880 r0.0500
A 2.3865,2.3865 2.5880,2.1663 r3.3750
A 2.5996,2.1320 2.5850,2.0989 r0.0500
L 2.1899,1.7038
A 2.1764,1.6357 2.2341,1.5971 r0.0625
L 2.9371,1.5971
A 2.9682,1.5884 2.9903,1.5649 r0.0600
A 2.9982,1.5497 3.0060,1.5344 r3.3750
A 3.0038,1.4758 2.9526,1.4471 r0.0600
L 2.4116,1.4471
A 2.4752,1.3355 2.5336,1.2211 r2.8125
A 2.5446,1.2087 2.5606,1.2041 r0.0300
L 3.1113,1.2041
A 3.1456,1.1933 3.1676,1.1648 r0.0600
A 3.1732,1.1495 3.1787,1.1342 r3.3750
A 3.1712,1.0795 3.1222,1.0541 r0.0600
L 2.6075,1.0541
A 2.6494,0.9440 2.6866,0.8322 r2.8125
A 2.6974,0.8169 2.7152,0.8111 r0.0300
L 3.2288,0.8111
A 3.2661,0.7981 3.2872,0.7646 r0.0600
A 3.2908,0.7494 3.2942,0.7341 r3.3750
A 3.2824,0.6835 3.2356,0.6611 r0.0600
L 3.2331,0.6611
A 3.2555,0.5399 3.2734,0.4180 r3.3000
L 3.2956,0.4180
A 3.3357,0.4027 3.3553,0.3645 r0.0600
A 3.3569,0.3493 3.3584,0.3340 r3.3750
A 3.3432,0.2878 3.2987,0.2680 r0.0600
L 3.2891,0.2680
A 3.3000,0.0000 3.2891,-0.2680 r3.3000
L 3.2987,-0.2680
A 3.3432,-0.2878 3.3584,-0.3340 r0.0600
A 3.3569,-0.3493 3.3553,-0.3645 r3.3750
A 3.3357,-0.4027 3.2956,-0.4180 r0.0600
L 3.2734,-0.4180
A 3.2555,-0.5399 3.2331,-0.6611 r3.3000
L 3.2356,-0.6611
A 3.2824,-0.6835 3.2942,-0.7341 r0.0600
A 3.2908,-0.7494 3.2872,-0.7646 r3.3750
A 3.2661,-0.7981 3.2288,-0.8111 r0.0600
L 2.6930,-0.8111
A 2.6602,-0.9129 2.6236,-1.0133 r2.8125
A 2.6269,-1.0411 2.6516,-1.0541 r0.0300
L 3.1222,-1.0541
A 3.1712,-1.0795 3.1787,-1.1342 r0.0600
A 3.1732,-1.1495 3.1676,-1.1648 r3.3750
A 3.1456,-1.1933 3.1113,-1.2041 r0.0600
L 2.5417,-1.2041
A 2.4919,-1.3041 2.4381,-1.4021 r2.8125
A 2.4351,-1.4093 2.4341,-1.4171 r0.0300
A 2.4429,-1.4383 2.4641,-1.4471 r0.0300
L 2.9526,-1.4471
A 3.0038,-1.4758 3.0060,-1.5344 r0.0600
A 2.9982,-1.5497 2.9903,-1.5649 r3.3750
A 2.9682,-1.5884 2.9371,-1.5971 r0.0600
L 2.2341,-1.5971
A 2.1764,-1.6357 2.1899,-1.7038 r0.0625
L 2.5850,-2.0989
A 2.5996,-2.1320 2.5880,-2.1663 r0.0500
A 2.3865,-2.3865 2.1663,-2.5880 r3.3750
A 2.1320,-2.5996 2.0989,-2.5850 r0.0500
L 1.7038,-2.1899
A 1.6357,-2.1764 1.5971,-2.2341 r0.0625
L 1.5971,-2.9371
A 1.5884,-2.9682 1.5649,-2.9903 r0.0600
A 1.5497,-2.9982 1.5344,-3.0060 r3.3750
A 1.4758,-3.0038 1.4471,-2.9526 r0.0600
L 1.4471,-2.4116
A 1.3706,-2.4559 1.2927,-2.4978 r2.8125
L 1.2927,-3.0773
A 1.2824,-3.1109 1.2550,-3.1330 r0.0600
A 1.2398,-3.1391 1.2245,-3.1451 r3.3750
A 1.1688,-3.1386 1.1427,-3.0891 r0.0600
L 1.1427,-2.5699
A 1.0660,-2.6027 0.9883,-2.6332 r2.8125
L 0.9883,-3.1824
A 0.9763,-3.2184 0.9451,-3.2400 r0.0600
A 0.9298,-3.2444 0.9145,-3.2487 r3.3750
A 0.8621,-3.2388 0.8383,-3.1910 r0.0600
L 0.8383,-2.6847
A 0.7614,-2.7075 0.6838,-2.7281 r2.8125
L 0.6838,-3.2558
A 0.6701,-3.2940 0.6351,-3.3147 r0.0600
A 0.6199,-3.3176 0.6046,-3.3204 r3.3750
A 0.5554,-3.3075 0.5338,-3.2614 r0.0600
L 0.5338,-2.7614
A 0.4568,-2.7752 0.3794,-2.7868 r2.8125
L 0.3794,-3.2996
A 0.3638,-3.3399 0.3252,-3.3593 r0.0600
A 0.3100,-3.3607 0.2947,-3.3621 r3.3750
A 0.2489,-3.3466 0.2294,-3.3023 r0.0600
L 0.2294,-2.8031
A 0.1523,-2.8084 0.0750,-2.8115 r2.8125
L 0.0750,-3.3150
A 0.0575,-3.3573 0.0153,-3.3750 r0.0600
A ... to 0.0000,-3.3750  (arc r3.3750 centre 0.0000,0.0000)
```

#### 4.1.3 Layers (front to rear)

| Layer | z from | z to | Cross-section |
|---|---|---|---|
| L1 spigot | −1.5095 | −1.4095 | ring: outer circle R1.375, inner circle R1.250 |
| L2 spokes | −1.4095 | −1.3095 | ring R1.250 … R1.375 plus four diagonal spokes (see below) |
| L3 front web | −1.3095 | −1.0595 | outline F (see below) with the front recesses |
| L4 | −1.0595 | −0.3095 | outline B with the four bosses replaced by corner chamfers (see below); no holes |
| L5 | −0.3095 | +1.1555 | outline B, four Ø0.250 holes |
| L6 | +1.1555 | +1.4055 | outline B with the side fins removed (see below), four Ø0.250 holes |
| L7 band | +1.4055 | +1.6555 | full disc R3.375 with the top land: arc R3.375 from (−0.7612, 3.2880) around the bottom to (0.7612, 3.2880), R0.10 round to (0.7387, 3.2906), line y = 3.2906 to (−0.7387, 3.2906), R0.10 round back; four Ø0.250 holes |
| L8 rear | +1.6555 | +3.2555 | outline R, with the fill blocks ending as described below; holes and bores of §4.1.5 |
| L9 rear | +3.2555 | +3.3505 | outline R without the fill blocks and with the slot |y| < 0.268 cut through (see §4.1.6) |

**L2 spokes.** Four spokes along the diagonals (directions 45°, 135°, 225°, 315°), each bounded by two lines parallel to its
diagonal at perpendicular distance 0.250 (spoke width 0.500), running from the ring (R1.375) out to an arc R2.2338 centred
on the axis. Spoke-to-ring corners are rounded R0.03. The ring's outer face meets the spoke front faces (z = −1.4095) with a
concave round R0.03.

**L3 outline F and front recesses.** Outer outline F = B with three changes: (a) on each side the side fins between
y = −1.4471 and +1.4471 are absent: the outline runs from (±2.4116, +1.4471) along the core arc R2.8125 to (±2.4116,
−1.4471) (the outermost side fins y = ±1.4471 … ±1.5971 stay); (b) the bosses are replaced by the corner chamfer described
under L4; (c) no Ø0.250 holes. Inside F, recesses 0.250 deep are open to the front face z = −1.3095 with their floor at
z = −1.0595 (floor edges R0.03):
- Central bore R1.250 (inside the ring R1.250…R1.375; this bore is open from the spigot face z = −1.5095 to the floor
  z = −1.0595, floor edge R0.02).
- Four windows between the spokes, centred at 0°, 90°, 180°, 270°: bounded by the ring R1.375 (inside), an arc R2.2338
  (outside) and two lines parallel to the neighbouring diagonals at distance 0.375 from them; corners R0.03. Example
  (window at +X): (1.2113, 0.6507) – R1.375 – (1.2113, −0.6507), line to (1.8223, −1.2919), arc R2.2338 to (1.8223, 1.2919),
  line back.
- Four diagonal recesses, one on each diagonal: bounded by the ring R1.375, two lines parallel to the diagonal at distance
  0.250 and an outer arc R2.375; inner corners R0.03, outer corners R0.04. Example (recess at 315°): ring arc from
  (0.8080, −1.1125) to (1.1125, −0.8080), line to (1.8212, −1.4676), R0.04, arc R2.375 to (1.4676, −1.8212) via R0.04,
  line back to (0.8045, −1.1580).
  So between a window and a diagonal recess stands a wall 0.125 thick; L2's spokes cover the diagonal recesses at the front.
- In each diagonal recess a hollow boss stands on the floor: centred (±1.4866, ±1.4866), outer Ø0.3125, bore Ø0.188, front
  face at z = −1.2595, outer foot round R0.03 into the floor (z = −1.0595); the Ø0.188 bore runs from z = −1.2595 to the
  floor.

**L4 corner chamfers.** In each quadrant the boss of B (from the R0.0625 root on the top/bottom line x = ±1.5971 to the
R0.0625 root on the side line y = ±1.5971) is replaced by: line x = 1.5971 down to (1.5971, 1.9092), arc R0.15 through
(1.6085, 1.8518) to (1.6410, 1.8032), straight 45° line to (1.8032, 1.6410), arc R0.15 through (1.8518, 1.6085) to
(1.9092, 1.5971), then the line y = 1.5971 outward (mirror for the other quadrants). The same chamfer bounds outline F (L3).
In L4 the inner six side fins on each side start at z = −1.0595 (their front ends are rounded R0.03); the two outermost side
fins, the top fins and the bottom fins run from z = −1.3095.

**L6.** On each side, between y = +1.4471 and −1.4471 the side fins are absent and the outline is an arc R3.2201 centred on
the axis, from (±2.8928, ±1.4471) (small R0.01 corners at the ends: the arc meets the lines y = ±1.4471 at x = ±2.8838 …
±2.8928). The inner side fins of L5 end at z = +1.1555 (end edges R0.01). The R3.2201 face meets the band face z = 1.4055
with a concave R0.03.

**L8 fill blocks.** The R3.300 fills of outline R (|y| ≤ 0.268 and 0.418 ≤ |y| ≤ 0.6611 on both sides) run from z = +1.6555
up to z = +3.2555; their outer top edge is rounded R0.06 (the R3.300 face rolls over into the face z = 3.2555).

#### 4.1.4 Top features

- The top land y = 3.2906 runs the full length; its front edge (at z = −1.3095) is rounded R0.10.
- **Wire entry boss**: a Ø0.785 cylinder with axis parallel to Y through (x = 0, z = 2.3705), standing 0.080 proud of the top
  land (top face y = 3.3706). A Ø0.625 blind hole on the same axis goes from y = 3.3706 down to a flat bottom at y = 2.7906.

#### 4.1.5 Bores and holes (revolved about Z unless stated)

Half profile of the central cavities in the plane y = 0 (radius, z), from the bottom upward:
(0, 1.7855) – (0.6875, 1.7855) – (0.6875, 2.7855) – (0.8531, 2.7855) – (0.8549, 2.8055) – (0.8831, 2.8055) –
(0.8831, 2.8455) – (0.8584, 2.8455) – (0.8750, 3.0355) – (1.0000, 3.0355) – (1.0000, 3.1605) – (2.2540, 3.1605) –
(2.2540, 3.3205) – R0.03 – (2.2840, 3.3505) (rear face).
Meaning: Ø1.375 blind bore 1.000 deep (bottom z = 1.7855); a 5° tapered bore (R0.8531 at z 2.7855 → R0.8750 at z 3.0355)
interrupted by a retaining-ring groove R0.8831 between z 2.8055 and 2.8455; a Ø2.000 counterbore from z 3.0355 to 3.1605; a
Ø4.508 rear recess from z 3.1605 to the rear face, mouth edge rounded R0.03.

- **Bar slot** across the counterbore: |y| ≤ 0.268, from x = −2.625 to +2.625 (ends are arcs R2.625 centred on the axis),
  floor z = 3.0355 (near its floor the slot walls are drafted in to |y| = 0.2345 at z 3.0355 … 3.0755).
- **Bolt holes**: four Ø0.250 holes at (±2.0771, ±2.0771) from z = −0.3095 to z = 1.8305, continuing as Ø0.330 from
  z = 1.8305 to the floor of the diagonal rear recess (z = 3.0805).
- **Diagonal rear recesses** (4, one per quadrant): obround, width 0.400 (end radius 0.200), axis along the diagonal from the
  end centre (±1.5938, ±1.5938) to the end centre (±2.0771, ±2.0771), floor z = 3.0805, open to the rear (they merge with the
  rear recess). In the (−X, −Y) recess only, the floor edge is rounded R0.08 and the inner end radius is 0.1526 (reference
  asymmetry; the other three recesses have sharp floor edges).

#### 4.1.6 Rear slot (L9)

From z = 3.2555 to the rear face the housing is cut through by a slot |y| < 0.268 that runs across the whole width: from the
recess (x = ±2.2380) out through all side fins. Its floor z = 3.2555 between R2.625 and R3.300 has R0.06 rounds at both ends
(R2.685 inner, R3.240 outer). The slot divides the rear rim into a top half and a bottom half.

#### 4.1.7 Front plate seat

The front plate P02 lies on the housing front face z = −1.3095 (the housing face is exactly at the plate's top face).

#### 4.1.8 Rounds

- All fin ends at the front face (z = −1.3095) and the rear face (z = 3.3505) are rounded R0.03 on every edge
  (fin flanks, tips, roots); the outer front edge of the outline and the outer rear edge are rounded R0.03.
- Inner side-fin front ends at z = −1.0595: R0.03.
- Boss bottom faces (z = −0.3095) meet the outline with R0.03 rounds; the L4 chamfer meets the L3 front zone with R0.03.
- Recess floor edges at z = −1.0595: R0.03 (window corners use R0.03 spherical corners).
- Spigot ring front edges: R0.02 (both).
- These rounds are worth less than 0.1 % of the housing volume; model them if you can, otherwise leave sharp.

### 4.2 P02 Front plate (sheet 0.03125)

Flat portion: z = −1.3408 … −1.3095 (lies against the housing front face). Outer outline, half for x ≥ 0 (mirror in X):

```
start 0.0000,2.8125
A -0.0000,2.8125 1.5796,2.3270 r2.8125
A 1.5925,2.3126 1.5971,2.2939 r0.0400
L 1.5971,1.9092
A 1.6085,1.8518 1.6410,1.8032 r0.1500
L 1.8032,1.6410
A 1.8518,1.6085 1.9092,1.5971 r0.1500
L 2.5650,1.5971
A 2.6400,1.5221 2.5650,1.4471 r0.0750
L 2.4813,1.4471
A 2.4467,1.4272 2.4465,1.3874 r0.0400
A 2.8125,0.0000 2.4465,-1.3874 r2.8125
A 2.4467,-1.4272 2.4813,-1.4471 r0.0400
L 2.5650,-1.4471
A 2.6400,-1.5221 2.5650,-1.5971 r0.0750
L 1.9092,-1.5971
A 1.8518,-1.6085 1.8032,-1.6410 r0.1500
L 1.6410,-1.8032
A 1.6085,-1.8518 1.5971,-1.9092 r0.1500
L 1.5971,-2.2939
A 1.5925,-2.3126 1.5796,-2.3270 r0.0400
A ... to 0.0000,-2.8125  (arc r2.8125 centre 0.0000,0.0000)
```

(The two ears reach x = ±2.640 with R0.075 tips centred (±2.565, ±1.5221); the corner chamfers are the same as the housing's.)

Inner opening of the flat portion: circle R2.2721 interrupted on each diagonal by a notch 0.500 wide (lines parallel to the
diagonal at distance 0.250) that reaches out to an arc R2.375, corners R0.04.

Four **joggled tabs** (one at 0°, 90°, 180°, 270°) are formed down out of the plate between the diagonal notches: radial half
profile (r, z) of one tab, revolved about Z and trimmed by the lines parallel to the diagonals at distance 0.250:
outer surface (2.8125, −1.3095) → (2.3083, −1.3095) → R0.05 → (2.2585, −1.3551) → straight (5° from axial) →
(2.2537, −1.4100) → R0.02 → (2.2338, −1.4283) → (2.0307, −1.4283); inner surface (2.8125, −1.3408) → (2.3095, −1.3408) →
R0.02 → (2.2895, −1.3590) → straight → (2.2847, −1.4139) → R0.05 → (2.2349, −1.4595) → (2.0307, −1.4595).
So each tab bottom is an annular sector R2.0307 … R2.2746 at z −1.4595 … −1.4283, angular width set by the lines at distance
0.250 from the two neighbouring diagonals (at the bottom the sector ends at e.g. (1.2483, 1.6018) and (1.4218, 1.7754)).

### 4.3 P03 Output shaft

Revolved about Z; half profile (r, z): (0, −2.3705) → (0.125, −2.3705) → (0.125, −3.3305) → 45° to (0.165, −3.3705) →
(0.2525, −3.3705) → 45° to (0.3125, −3.3105) → (0.3125, −1.4595) → concave R0.06 (centre r 0.3725, z −1.4595) up to
z −1.3995 → convex R0.02 (centre r 0.370, z −1.3795) out to (0.390, −1.3795) → (0.390, −1.0595) → (0, −1.0595).
So: Ø0.625 shaft, front end chamfer 0.06 × 45°, centre hole Ø0.250 × 1.000 deep (flat bottom) with 0.04 × 45° entry
chamfer, shoulder to Ø0.780 with R0.06 fillet, rear face z = −1.0595.
**Keyway**: 0.188 wide (x = ±0.094), floor at y = +0.2185, from the front end z = −3.3705 to a square end at z = −2.1205;
the two floor-to-end corners are rounded R0.02 (axes parallel to Y at x = ±0.074, z = −2.1405).

### 4.4 P04 Input hub

Revolved about Z: Ø1.375 from z 1.7855 to 2.8055; Ø1.000 from 2.8055 to 3.1405; 0.02 × 45° chamfer to the rear face
z = 3.1605 (face Ø0.960); front face z = 1.7855. Bore Ø0.625 through, with a 0.02 × 45° chamfer at the rear end (Ø0.665 at
z = 3.1605). Keyway in the bore: 0.188 wide (x = ±0.094), floor (outer face) at y = +0.4065, from the rear face down to a flat
end at z = 2.1605. Two plain radial holes Ø0.1876 through the Ø1.000 wall at z = 2.9830: one on the −Y axis (x = 0), one on
the +X axis (y = 0).

### 4.5 P05 Shaft key

Block x −0.094 … +0.094, y 0.2185 … 0.4065, z −3.3080 … −2.1205. All edges rounded R0.02 (corner spheres R0.02) except the
two long bottom edges (y = 0.2185) and the rear bottom edge (z = −2.1205, y = 0.2185), which are sharp.

### 4.6 Rings P06 – P09 (revolved about Z)

| Body | OD | ID | z front | z rear | front edges |
|---|---|---|---|---|---|
| P06 | 2.3125 | 1.8750 | −1.4095 | −1.0595 | 0.020 × 45° chamfer on OD and ID |
| P07 | 1.8550 | 1.6675 | −1.4095 | −1.0595 | 0.020 × 45° chamfer on OD and ID |
| P08 | 0.9675 | 0.7800 | −1.4095 | −1.0595 | 0.010 × 45° chamfer on OD and ID |
| P09 | 1.6475 | 0.9875 | −1.3795 | −1.0595 | R0.02 round on OD and ID |

Rear edges are sharp.

### 4.7 P10 Internal retaining ring

Flat, z = 2.8055 … 2.8355 (sits in the housing groove). Outline (full, clockwise):

```
from -0.3310,-0.7098 L -0.3732,-0.8004
from -0.3732,-0.8004 A -0.7448,-0.4745 -0.8831,-0.0000 r0.8831
from -0.8831,0.0000 A c=0.0000,0.0000 r=0.8831 to 0.8831,0.0000 (half circle)
from 0.8831,0.0000 A 0.7448,-0.4745 0.3732,-0.8004 r0.8831
from 0.3732,-0.8004 L 0.3310,-0.7098
from 0.3310,-0.7098 A 0.3099,-0.6388 0.3107,-0.5648 r0.2500
from 0.3107,-0.5648 L 0.4618,-0.4943
from 0.4618,-0.4943 A 0.5753,-0.4890 0.6630,-0.4168 r0.1800
from 0.6630,-0.4168 A 0.7525,-0.2169 0.7831,0.0000 r0.7831
from 0.7831,0.0000 A c=0.0000,0.0000 r=0.7831 to -0.7831,0.0000 (half circle)
from -0.7831,-0.0000 A -0.7525,-0.2169 -0.6630,-0.4168 r0.7831
from -0.6630,-0.4168 A -0.5753,-0.4890 -0.4618,-0.4943 r0.1800
from -0.4618,-0.4943 L -0.3107,-0.5648
from -0.3107,-0.5648 A -0.3083,-0.5844 -0.3075,-0.6041 r0.2500
from -0.3075,-0.6041 A -0.3134,-0.6582 -0.3310,-0.7098 r0.2500
```

Two Ø0.125 lug holes centred (±0.4403, −0.6367).

### 4.8 P11 Rear clamps (sheet 0.020)

**P11-a** (+Y half). Flange z = 3.3505 … 3.3705 with this outline (full loop):

```
from -2.5850,2.0989 A -2.5958,2.1151 -2.5996,2.1342 r0.0500
from -2.5996,2.1342 A -2.5966,2.1513 -2.5880,2.1663 r0.0500
from -2.5880,2.1663 A -2.3865,2.3865 -2.1663,2.5880 r3.3750
from -2.1663,2.5880 A -2.1320,2.5996 -2.0989,2.5850 r0.0500
from -2.0989,2.5850 L -1.7308,2.2169
from -1.7308,2.2169 A 0.0000,2.8125 1.7308,2.2169 r2.8125
from 1.7308,2.2169 L 2.0989,2.5850
from 2.0989,2.5850 A 2.1320,2.5996 2.1663,2.5880 r0.0500
from 2.1663,2.5880 A 2.3865,2.3865 2.5880,2.1663 r3.3750
from 2.5880,2.1663 A 2.5996,2.1320 2.5850,2.0989 r0.0500
from 2.5850,2.0989 L 2.2169,1.7308
from 2.2169,1.7308 A 2.6127,1.0410 2.7997,0.2680 r2.8125
from 2.7997,0.2680 L 2.1981,0.2680
from 2.1981,0.2680 A 2.0325,0.8789 1.7008,1.4180 r2.2144
from 1.7008,1.4180 L 2.2185,1.9357
from 2.2185,1.9357 A c=2.0771,2.0771 r=0.2000 to 1.9357,2.2185 (half circle)
from 1.9357,2.2185 L 1.4180,1.7008
from 1.4180,1.7008 A -0.0000,2.2144 -1.4180,1.7008 r2.2144
from -1.4180,1.7008 L -1.9357,2.2185
from -1.9357,2.2185 A -2.1536,2.2619 -2.2771,2.0771 r0.2000
from -2.2771,2.0771 A -2.2619,2.0006 -2.2185,1.9357 r0.2000
from -2.2185,1.9357 L -1.7008,1.4180
from -1.7008,1.4180 A -2.0325,0.8789 -2.1981,0.2680 r2.2144
from -2.1981,0.2680 L -2.7997,0.2680
from -2.7997,0.2680 A -2.6127,1.0410 -2.2169,1.7308 r2.8125
from -2.2169,1.7308 L -2.5850,2.0989
```

Formed lip, revolved about Z, radial profile (r, z) closed loop: (2.2540, 3.3705) → (2.8125, 3.3705) [flange top] …
flange … (2.2140, 3.3505) → (2.2140, 3.1605) → (2.0740, 3.1605) → (2.0740, 3.1805) → (2.1340, 3.1805) → R0.04 (centre
2.1340, 3.2205) → (2.1740, 3.2205) → (2.1740, 3.2905) → R0.08 (centre 2.2540, 3.2905) → (2.2540, 3.3705).
The lip exists in three angular segments: from the line y = 0.268 up to the radial plane at 39.82° from +X; from 50.18° to
129.82°; from 140.18° to the line y = 0.268 on the −X side (radial end faces).
**P11-b** = P11-a rotated 180° about the Z axis.

### 4.9 P12 Round plug

Frustum with axis parallel to Y through (x = 0, z = −0.3345): base Ø1.000 at y = 3.2906 (on the top land), top Ø0.7229 at
y = 3.3706, side cone 60° half-angle.

### 4.10 Lead wires P13 / P14 and tips P15

Round rods Ø0.100 swept along the centre lines below (P14 differs from P13 in the listed numbers).

| Segment | P13 (wire A) | P14 (wire B) |
|---|---|---|
| start face | plane y = 2.7906 (bottom of the entry hole), centre (−0.051, 2.7906, 2.3705), direction +Y | centre (+0.051, 2.7906, 2.3705) |
| arc 1 in the plane x = const | R2.000, centre (y 2.7906, z 4.3705), bending up | same |
| arc 2 in the same plane | R0.750, centre (y 3.4615, z 3.3158), tangent to arc 1, over the top to (y 3.4615, z 4.0658), heading −Y | same |
| arc 3 in the plane z = 4.0658 | R0.949, centre (−1.000, 3.4615), to (−1.000, 2.5125) heading −X | R1.051, centre (−1.000, 3.4615), to (−1.000, 2.4105) |
| straight | to (−3.500, 2.5125) | to (−3.500, 2.4105) |
| arc 4 (z = 4.0658) | R1.051, centre (−3.500, 1.4615), to (−4.551, 1.4615) heading −Y | R0.949, centre (−3.500, 1.4615), to (−4.449, 1.4615) |
| straight | to (−4.551, −1.585) | to (−4.449, −1.585) |
| arc 5 (z = 4.0658) | R0.949, centre (−5.500, −1.585), to (−5.500, −2.534) heading −X | R1.051, centre (−5.500, −1.585), to (−5.500, −2.636) |
| straight | to (−7.500, −2.534, 4.0658) | to (−7.500, −2.636, 4.0658) |
| helix | 4 turns, axis parallel to Y through (x −7.500, z 2.3158), radius 1.750, pitch 0.250 advancing +Y; centre line (−7.5 − 1.75 sin 2πt, y0 + 0.25 t, 2.3158 + 1.75 cos 2πt), t = 0 … 4, y0 = −2.534 | y0 = −2.636 |
| end face | flat, normal to the helix tangent at t = 4, centre (−7.500, −1.534, 4.0658) | (−7.500, −1.636, 4.0658) |

The arcs are tangent to their neighbours (arc 1 starts horizontal along +Y; arc 2 ends horizontal along −Y).

**P15-a / P15-b**: rod Ø0.080, length 0.250, continuing each wire from its end face along the helix tangent at t = 4
(direction (−0.99974, +0.02273, 0)): P15-a axis from (−7.4989, −1.5340, 4.0658) to (−7.7488, −1.5283, 4.0658); P15-b
axis from (−7.5012, −1.6360, 4.0658) to (−7.7511, −1.6303, 4.0658). Flat ends normal to the axis; the start face of each
tip coincides with the end face of its wire (the wire end faces lie on the plane through the tip start point with normal
(−0.99974, 0.02273, 0); the measured wire ends are 0.001 off the ideal helix end).

### 4.11 H1 Socket nuts (4)

Cylinder Ø0.3125, z 3.0805 … 3.2685, top outer edge R0.02. Hex socket from the top: 0.125 across flats, 0.150 deep (flat
bottom z = 3.1185), 45° entry countersink to Ø0.1443 at the top face. Centres (x, y): H1-a (−1.7106, +1.7106), H1-b
(+1.7106, +1.7106), H1-c (+1.7106, −1.7106), H1-d (−1.7106, −1.7106). Each socket is turned so that one hex corner points
along the radial (diagonal) direction.

### 4.12 H2 Hex standoff studs (4)

Along Z through the centre (xc, yc): H2-a (+2.0771, +2.0771), H2-b (+2.0771, −2.0771), H2-c (−2.0771, −2.0771), H2-d
(−2.0771, +2.0771).
- Hex 0.4375 across flats from z = −1.2095 to −0.4990, turned so that one corner points along the radial (diagonal)
  direction (flat normals at 15°, 75°, 135° … for the +X+Y instance). Bottom corners chamfered by a 45° cone starting at
  Ø0.4375 on the bottom face.
- Domed collar: the hex is intersected/united with a body of revolution whose outline is an arc R0.300 centred at (r 0.020,
  z −0.3095), so the collar grows from the hex to Ø0.640 at its top face z = −0.3095.
- Plain stud Ø0.250 from z = −0.3095 to 1.6405, then 45° chamfer to the top face z = 1.6905 (Ø0.150).
- Internal thread from the bottom face: 20 threads per inch, major Ø0.250, modelled helical, from z = −1.2095 to about
  z = −0.59, 45° entry countersink to Ø0.260 at the bottom face.

### 4.13 H3 Set screws (2)

Cylinder Ø0.1876, length 0.1929 along a radial axis at z = 2.9830, from radius 0.3071 to 0.5000; both ends chamfered
0.0357 × 45° (end faces Ø0.1162). H3-a on the −Y axis (x = 0, y −0.5000 … −0.3071); H3-b on the +X axis (y = 0,
x 0.3071 … 0.5000).

## 5. Assembly

All parts are in place in the global frame as given; nothing has to be moved. Contacts: P02 on the housing front face;
rings P06–P09 and the shaft rear face on the housing floor z = −1.0595; P04 on the Ø1.375 bore bottom; P10 in its groove;
P11 flanges on the rear face z = 3.3505; H1 in the diagonal rear recesses; H2 studs in the Ø0.250 bolt holes (coincident
surfaces); the wires start on the bottom of the entry hole.
No two bodies overlap by more than 8 mm³ (largest overlap: H1-d with P01, 0.32 mm³; all others 0).

## 6. Acceptance targets

Per body (inch; V in in³ and mm³, A in in² and mm², CoM in inch, bbox in inch, F = reference face count):

| Body | Description | V in³ | V mm³ | A in² | A mm² | CoM x | CoM y | CoM z | xmin | xmax | ymin | ymax | zmin | zmax | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-a | Socket nut at (-1.7106, +1.7106) | 0.01230 | 201.51 | 0.3927 | 253.38 | -1.7106 | 1.7106 | 3.1707 | -1.8668 | -1.5543 | 1.5543 | 1.8668 | 3.0805 | 3.2685 | 20 |
| H1-b | Socket nut at (+1.7106, +1.7106) | 0.01230 | 201.51 | 0.3927 | 253.38 | 1.7106 | 1.7106 | 3.1707 | 1.5543 | 1.8668 | 1.5543 | 1.8668 | 3.0805 | 3.2685 | 20 |
| H1-c | Socket nut at (+1.7106, -1.7106) | 0.01230 | 201.51 | 0.3927 | 253.38 | 1.7106 | -1.7106 | 3.1707 | 1.5543 | 1.8668 | -1.8668 | -1.5543 | 3.0805 | 3.2685 | 20 |
| H1-d | Socket nut at (-1.7106, -1.7106) | 0.01230 | 201.51 | 0.3927 | 253.38 | -1.7106 | -1.7106 | 3.1707 | -1.8668 | -1.5543 | -1.8668 | -1.5543 | 3.0805 | 3.2685 | 20 |
| H2-a | Hex standoff stud at (+2.0771, +2.0771) | 0.24421 | 4001.83 | 4.1750 | 2693.53 | 2.0772 | 2.0771 | -0.1374 | 1.7571 | 2.3971 | 1.7571 | 2.3971 | -1.2095 | 1.6905 | 51 |
| H2-b | Hex standoff stud at (+2.0771, -2.0771) | 0.24421 | 4001.83 | 4.1750 | 2693.53 | 2.0771 | -2.0772 | -0.1374 | 1.7571 | 2.3971 | -2.3971 | -1.7571 | -1.2095 | 1.6905 | 51 |
| H2-c | Hex standoff stud at (-2.0771, -2.0771) | 0.24421 | 4001.83 | 4.1750 | 2693.53 | -2.0772 | -2.0771 | -0.1374 | -2.3971 | -1.7571 | -2.3971 | -1.7571 | -1.2095 | 1.6905 | 51 |
| H2-d | Hex standoff stud at (-2.0771, +2.0771) | 0.24421 | 4001.83 | 4.1750 | 2693.53 | -2.0771 | 2.0772 | -0.1374 | -2.3971 | -1.7571 | 1.7571 | 2.3971 | -1.2095 | 1.6905 | 51 |
| H3-a | Set screw on -Y radial | 0.00468 | 76.64 | 0.1410 | 90.98 | 0.0000 | -0.4035 | 2.9830 | -0.0938 | 0.0938 | -0.5000 | -0.3071 | 2.8892 | 3.0768 | 8 |
| H3-b | Set screw on +X radial | 0.00468 | 76.64 | 0.1410 | 90.98 | 0.4035 | 0.0000 | 2.9830 | 0.3071 | 0.5000 | -0.0938 | 0.0938 | 2.8892 | 3.0768 | 8 |
| P01 | Finned housing | 128.53972 | 2106388.63 | 344.7394 | 222412.05 | -0.0000 | 0.0145 | 1.0449 | -3.3750 | 3.3750 | -3.3750 | 3.3706 | -1.5095 | 3.3505 | 1591 |
| P02 | Front plate | 0.35583 | 5831.05 | 23.8871 | 15411.00 | 0.0000 | 0.0000 | -1.3595 | -2.8125 | 2.8125 | -2.8125 | 2.8125 | -1.4595 | -1.3095 | 110 |
| P03 | Output shaft | 0.69483 | 11386.21 | 6.4808 | 4181.17 | 0.0000 | -0.0078 | -2.0626 | -0.3900 | 0.3900 | -0.3900 | 0.3900 | -3.3705 | -1.0595 | 23 |
| P04 | Input hub | 1.34157 | 21984.35 | 10.8461 | 6997.48 | -0.0016 | -0.0034 | 2.3715 | -0.6875 | 0.6875 | -0.6875 | 0.6875 | 1.7855 | 3.1605 | 22 |
| P05 | Shaft key | 0.04166 | 682.70 | 0.9315 | 600.96 | 0.0000 | 0.3120 | -2.7140 | -0.0940 | 0.0940 | 0.2185 | 0.4065 | -3.3080 | -2.1205 | 19 |
| P06 | Ring A (OD 2.3125) | 0.50097 | 8209.51 | 7.3280 | 4727.74 | -0.0000 | 0.0000 | -1.2336 | -1.1563 | 1.1563 | -1.1562 | 1.1562 | -1.4095 | -1.0595 | 10 |
| P07 | Ring B (OD 1.855) | 0.17934 | 2938.90 | 4.7810 | 3084.51 | -0.0000 | 0.0000 | -1.2324 | -0.9275 | 0.9275 | -0.9275 | 0.9275 | -1.4095 | -1.0595 | 10 |
| P08 | Ring C (OD 0.9675) | 0.08979 | 1471.47 | 2.4040 | 1550.96 | -0.0000 | 0.0000 | -1.2340 | -0.4838 | 0.4838 | -0.4838 | 0.4838 | -1.4095 | -1.0595 | 10 |
| P09 | Ring D (OD 1.6475) | 0.43637 | 7150.87 | 5.3097 | 3425.61 | -0.0000 | 0.0000 | -1.2192 | -0.8237 | 0.8237 | -0.8238 | 0.8238 | -1.3795 | -1.0595 | 10 |
| P10 | Internal retaining ring | 0.01480 | 242.54 | 1.2926 | 833.91 | 0.0000 | 0.0717 | 2.8205 | -0.8831 | 0.8831 | -0.8004 | 0.8831 | 2.8055 | 2.8355 | 21 |
| P11-a | Rear clamp, +Y half | 0.14111 | 2312.39 | 12.7686 | 8237.81 | -0.0000 | 1.6668 | 3.3127 | -2.7997 | 2.7997 | 0.2680 | 2.8125 | 3.1605 | 3.3705 | 50 |
| P11-b | Rear clamp, -Y half | 0.14111 | 2312.39 | 12.7686 | 8237.81 | -0.0000 | -1.6668 | 3.3127 | -2.7997 | 2.7997 | -2.8125 | -0.2680 | 3.1605 | 3.3705 | 50 |
| P12 | Round plug on top flat | 0.04703 | 770.65 | 1.6288 | 1050.84 | 0.0000 | 3.3264 | -0.3345 | -0.5000 | 0.5000 | 3.2906 | 3.3706 | -0.8345 | 0.1655 | 4 |
| P13 | Lead wire A (x=-0.051) | 0.46510 | 7621.59 | 18.6249 | 12016.03 | -6.3702 | -1.2227 | 2.7163 | -9.3000 | -0.0010 | -2.5840 | 4.2615 | 0.5158 | 4.1158 | 20 |
| P14 | Lead wire B (x=+0.051) | 0.46637 | 7642.50 | 18.6760 | 12048.98 | -6.3403 | -1.3119 | 2.7200 | -9.3000 | 0.1010 | -2.6860 | 4.2615 | 0.5158 | 4.1158 | 20 |
| P15-a | Bare conductor tip of wire A | 0.00126 | 20.59 | 0.0729 | 47.02 | -7.6238 | -1.5312 | 4.0658 | -7.7497 | -7.4979 | -1.5740 | -1.4883 | 4.0258 | 4.1058 | 4 |
| P15-b | Bare conductor tip of wire B | 0.00126 | 20.59 | 0.0729 | 47.02 | -7.6261 | -1.6332 | 4.0658 | -7.7520 | -7.5003 | -1.6760 | -1.5903 | 4.0258 | 4.1058 | 4 |

Assembly: V = 134.4935 in³ (2 203 953.58 mm³), A = 491.1658 in² (316 880.50 mm²), CoM (−0.0442, 0.0062, 1.0226), bbox x −9.3000 … 3.3750, y −3.3750 … 4.2615, z −3.3705 … 4.1158.

## 7. Source conflicts and undetermined items

- The reference has small asymmetries in the R0.03 fin-root rounds (some roots are rounded on one side of the housing and
  sharp on the other) and the single R0.08-floored rear recess (§4.1.5). Follow the outlines as listed.
- Exact profile of the helical internal thread in H2 and the bottom of its tapped hole (near z −0.59 … −0.61): undetermined
  beyond 20 TPI, major Ø0.250, length.
- The catalogue drawing gives a 36 in lead-wire length; the modelled wires are much shorter (coil + run). Follow the model.
- The catalogue keyway note "0.188 wide × 0.188 deep" refers to the shaft; the modelled shaft keyway floor is at y = 0.2185
  (depth 0.094 from the Ø0.625 surface at the keyway edge) and the key is 0.188 × 0.188.
