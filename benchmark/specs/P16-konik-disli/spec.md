# Design specification: straight-tooth miter (bevel) gear with plain round bore (P16)

A one-piece steel bevel gear for a 45° shaft angle, 1:1 ratio: a cylindrical hub at the back, a conical toothed rim with
20 straight teeth, and a plain round through bore with small chamfers. No keyway, no set-screw hole. This document is
the only source for the rebuild. Every value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - The gear / bore axis is the **Y axis**. The flat back face of the hub is the plane **y = 0**; the teeth point toward
    **+Y**. The top (toe) of the teeth reaches y = 19.33.
  - A tooth **space** (gap) is centred on the **+Z** axis (θ = 90°); with 20 teeth the spaces are centred at
    θ = 90° + k·18° (so also on +X, -X and -Z), and the teeth are centred at θ = 9° + k·18°. θ is measured in the XZ
    plane from +X toward +Z.
- "(r, y)" = a profile in a half plane containing the Y axis (r = distance from Y), revolved 360° about Y.
- One body, one solid: **P01 Miter gear**.

## 2. Design data (for orientation; the geometry below governs)

Module 1.5, 20 teeth, pressure angle 20°, shaft angle 45° (pitch cone angle 22.5°), pitch diameter 30 at the heel,
pitch cone apex on the axis at y = 45 (mounting distance 45 from the back face), cone distance 39.197, face width 11
along the pitch cone (heel pitch point (r, y) = (15, 8.787), toe pitch point (10.79, 18.94)). Outside diameter at the
heel 32.77. Root cone apex at y = 42.50, tip cone apex at y = 44.51 (the cones do not share one apex).

## 3. Geometry of P01

The body is (A) a revolved blank minus (B) 20 identical tooth-space cuts, circularly patterned about Y.

**A. Blank: revolve about Y.** Closed (r, y) polygon, in this order (all straight segments):
1. (4.4, 0) → (12.5, 0)  (back face, annulus)
2. → (12.5, 7.75)  (hub, dia 25, length 7.75)
3. → (16.385, 9.36)  (back cone: 67.4902° from the axis, i.e. normal to the pitch cone within 0.01°)
4. → (11.73752, 19.33)  (tip cone: 24.9924° from the axis; this is the heel outside dia 32.77 at y = 9.36)
5. → (8.5, 18)  (toe cone: 67.6667° from the axis, rising outward to the toe tip edge at y = 19.33)
6. → (4.4, 18)  (front face, annulus)
7. → (4.0, 17.6)  (bore chamfer 45° x 0.4)
8. → (4.0, 0.4)  (bore, dia 8)
9. → back to (4.4, 0)  (bore chamfer 45° x 0.4).

**B. Tooth-space cutter** (one, for the space centred on +Z; then pattern 20 times about Y, 18° apart).

The cutter is a **ruled solid between two closed section curves S_A and S_B**: each point of S_A is joined to the
corresponding point of S_B by a straight line (same curve parameter on corresponding segments). S_A lies near the heel
(y ≈ 7.1 to 8.6), S_B beyond the toe (y ≈ 20.6 to 22.1); only the part of the cutter inside the blank matters (the
blank trims it at the back cone, tip cone and toe cone). The space is symmetric about the plane x = 0.

Each section is a closed chain of 6 segments, in this order:
1. **left flank** — cubic B-spline: the right-flank poles with x negated, run from pole 6 (outer end) to pole 1,
2. **left root fillet** — cubic B-spline: the right-fillet poles with x negated, run from pole 1 (flank junction) to
   pole 6 (root),
3. **root** — cubic Bezier (4 poles, given in full),
4. **right root fillet** — cubic B-spline, from the root end to the flank,
5. **right flank** — cubic B-spline, from the fillet junction out to the tip side,
6. straight closing line from the outer end of segment 5 to the outer end of segment 1 (it lies outside the gear).

The 6-pole cubic B-splines have the knot vector **(0, 0, 0, 0, 0.5, 0.5, 1, 1, 1, 1)** (interior knot 0.5 with
multiplicity 2, non-rational); the root is a Bezier (knots (0,0,0,0,1,1,1,1)). The left half is the mirror image
x → -x of the right half. The poles (x, y, z) in mm, global frame, right half (x ≥ 0):

**Section S_A (heel side)**

| Segment | Pole 1 | Pole 2 | Pole 3 | Pole 4 | Pole 5 | Pole 6 |
|---|---|---|---|---|---|---|
| 5 right flank | (0.87084, 7.27758, 14.26998) | (0.96531, 7.52986, 14.87873) | (1.16091, 7.77651, 15.47392) | (1.73652, 8.23609, 16.58289) | (2.11640, 8.44891, 17.09644) | (2.57105, 8.63507, 17.54565) |
| 4 right fillet (run from pole 6 to pole 1 in the chain) | (0.87084, 7.27758, 14.26998) | (0.84943, 7.22045, 14.13202) | (0.77207, 7.16685, 14.00268) | (0.54276, 7.09215, 13.82243) | (0.39217, 7.07150, 13.77260) | (0.24135, 7.07257, 13.77517) |
| 3 root (Bezier) | (-0.24135, 7.07257, 13.77517) | (-0.08047, 7.07371, 13.77791) | (0.08047, 7.07371, 13.77791) | (0.24135, 7.07257, 13.77517) | | |

**Section S_B (beyond the toe)**

| Segment | Pole 1 | Pole 2 | Pole 3 | Pole 4 | Pole 5 | Pole 6 |
|---|---|---|---|---|---|---|
| 5 right flank | (0.55803, 20.67480, 8.76922) | (0.65705, 20.93923, 9.40732) | (0.86209, 21.19778, 10.03121) | (1.46545, 21.67950, 11.19366) | (1.86365, 21.90259, 11.73198) | (2.34023, 22.09772, 12.20284) |
| 4 right fillet (run from pole 6 to pole 1 in the chain) | (0.55803, 20.67480, 8.76922) | (0.54746, 20.64621, 8.70124) | (0.50926, 20.61973, 8.63737) | (0.39602, 20.58283, 8.54836) | (0.32165, 20.57262, 8.52376) | (0.24717, 20.57315, 8.52502) |
| 3 root (Bezier) | (-0.24717, 20.57315, 8.52502) | (-0.08241, 20.57425, 8.52785) | (0.08241, 20.57425, 8.52785) | (0.24717, 20.57315, 8.52502) | | |

Segments 1 and 2 = segments 5 and 4 with x negated. Closing line 6: S_A from (2.57105, 8.63507, 17.54565) to
(-2.57105, 8.63507, 17.54565); S_B from (2.34023, 22.09772, 12.20284) to (-2.34023, 22.09772, 12.20284).

Notes on the cutter:
- The flank segments are the involute-like working flanks (20° pressure angle), the fillets blend them into the root;
  segment 5 meets segment 4 and segment 4 meets segment 3 with tangent continuity in both sections.
- The straight rulings of the flanks do not pass exactly through one apex (they cross the axis region at y ≈ 46.2,
  0.38 from the axis); the root rulings meet the axis at y = 42.50 (root cone, 21.25° from the axis). Use the poles as
  given; do not "correct" the rulings to a common apex.
- S_A and S_B are not planar sections of the gear; they are two positions along the same ruled surfaces. Extending the
  rulings further (beyond S_A or S_B) changes nothing inside the blank.

**Pattern:** subtract the cutter and its 19 copies rotated about the Y axis by k·18° (k = 1..19).

**Result checks:** tooth tips are 20 separate lands on the tip cone, each running from the back cone (heel, y ≈ 9.36)
to the toe edge (y = 19.33); root depth at the heel: the root meets the back cone at r ≈ 13.37 (y 8.11). The hub, back
face, bore and front face are untouched by the cutters. All edges not mentioned are sharp (no tip chamfers, no edge
rounds other than the root fillets).

## 4. Acceptance targets

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Miter gear | 8494.85 | 3858.30 | 0.000 | 9.030 | 0.000 | -16.281 | 16.281 | 0.000 | 19.330 | -16.281 | 16.281 | 134 |

Volume note: B-rep 8494.85, triangulated 8493.86 (0.012 %). The bounding box in X and Z is 32.562, not the outside
diameter 32.77, because a tooth space (not a tooth) lies on each of ±X and ±Z.

Check values: overall width 19.33 (y 0 to 19.33); hub dia 25, hub length 7.75; bore 8 through, 0.4 x 45° chamfers both
ends; front face at y = 18 (annulus r 4.4 to 8.5); outside dia at the heel 32.77; 20 teeth.

## 5. Undetermined items

- The exact generating method of the tooth flanks (e.g. Tredgold back-cone involute or an octoidal form) is not
  recoverable from the master; the spline poles above are the master's own flank definition and are authoritative.
- Material 1045 carbon steel (product data only). Nothing else is undetermined.
