# Design specification: crossed helical gear with hub, 13 teeth, left hand (P12)

A one-piece steel gear for crossed (screw) helical drives: a helical toothed rim, 10 mm wide, with a plain cylindrical
hub on one side and a plain round bore through both. This document is the only source for the rebuild. Every value was
measured from the master 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** Angles in degrees.
- **Global frame (use exactly, no realignment):**
  - The gear axis is the **X axis**. The toothed rim runs from **X = -10 to X = 0**; the hub runs from **X = 0 to
    X = 10**. Overall length 20.
  - The bore is centred on the X axis.
  - **Polar angle phi** is measured in a plane X = constant, from **+Y towards +Z** (positive rotation about +X):
    a point at radius r and polar angle phi is (x, r cos phi, r sin phi).
- One body, one solid. Name: **P01 Gear**.

## 2. Body list

| ID | Qty | Name | Type |
|---|---|---|---|
| P01 | 1 | Helical gear with hub (teeth, rim and hub one solid) | custom |

## 3. Gear data

| Item | Value |
|---|---|
| Number of teeth z | 13 |
| Nominal normal module | 1 |
| Nominal helix angle | 45, **left hand** |
| Nominal pressure angle | 20 (nominal only, see the note below) |
| Nominal pitch diameter (z m / cos 45) | 18.385 (radius 9.19239) |
| Tip (outside) diameter | **20.380** (radius 10.19) |
| Root diameter | **15.95894** (radius 7.97947) |
| Face width | 10.000 (X = -10 to 0) |
| Angular pitch | 360 / 13 = 27.692308 |
| **Lead** (measured) | **57.600** (twist rate **6.25 per mm**; twist over the face width **62.5**) |
| Helix angle at r = 9.19239 from that lead | 45.08 |

**Hand and twist sense.** Moving toward +X, every tooth turns in the **negative** phi direction (from +Z towards +Y) by
6.25 per mm. This is a left-hand helix about +X.

**Note on the tooth form.** The master's flank is **not** an exact involute of any base circle (the nearest involute
deviates by 0.02 to 0.04 mm). Do not generate the teeth from a gear formula: reproduce the measured transverse profile of
section 4 (table T1). The tooth form is the same in every plane X = constant; only its angular position changes with X.

## 4. Transverse tooth-space profile (table T1)

The profile is given in the plane **X = -10**, for the tooth space whose centre line is the **+Z axis** (phi = 90). The
space is symmetric about the Z axis. Table T1 lists the half with y >= 0, from the space centre on the root circle (row 1)
to the corner on the tip circle (row 32). The other half is the mirror image (y -> -y).

Points are spaced 0.1 mm along the curve. Pass one smooth interpolating curve through all 63 points of the full space
(rows 32 .. 2 mirrored, then rows 1 .. 32); a cubic interpolation through these points reproduces the master within
0.001 mm. Columns r and delta are for checking: r = sqrt(y^2 + z^2), delta = angle from the +Z axis towards +Y.

| Row | y | z | r | delta |
|---|---|---|---|---|
| 1 | 0.00000 | 7.97947 | 7.97947 | 0.0000 |
| 2 | 0.10791 | 7.97874 | 7.97947 | 0.7749 |
| 3 | 0.20597 | 7.97681 | 7.97947 | 1.4791 |
| 4 | 0.30399 | 7.97368 | 7.97947 | 2.1833 |
| 5 | 0.40199 | 7.97011 | 7.98024 | 2.8874 |
| 6 | 0.49950 | 7.97934 | 7.99496 | 3.5820 |
| 7 | 0.59396 | 8.00527 | 8.02728 | 4.2434 |
| 8 | 0.68302 | 8.04610 | 8.07504 | 4.8521 |
| 9 | 0.76478 | 8.10010 | 8.13613 | 5.3936 |
| 10 | 0.83753 | 8.16573 | 8.20857 | 5.8561 |
| 11 | 0.89951 | 8.24161 | 8.29055 | 6.2288 |
| 12 | 0.94876 | 8.32630 | 8.38018 | 6.5007 |
| 13 | 0.98310 | 8.41803 | 8.47524 | 6.6611 |
| 14 | 1.00161 | 8.51426 | 8.57297 | 6.7094 |
| 15 | 1.01895 | 8.61078 | 8.67086 | 6.7486 |
| 16 | 1.04017 | 8.70653 | 8.76844 | 6.8129 |
| 17 | 1.06522 | 8.80134 | 8.86557 | 6.9009 |
| 18 | 1.09402 | 8.89509 | 8.96211 | 7.0117 |
| 19 | 1.12650 | 8.98762 | 9.05794 | 7.1441 |
| 20 | 1.16257 | 9.07881 | 9.15295 | 7.2972 |
| 21 | 1.20218 | 9.16853 | 9.24701 | 7.4700 |
| 22 | 1.24524 | 9.25664 | 9.34002 | 7.6616 |
| 23 | 1.29168 | 9.34301 | 9.43187 | 7.8713 |
| 24 | 1.34145 | 9.42751 | 9.52247 | 8.0983 |
| 25 | 1.39445 | 9.51002 | 9.61171 | 8.3418 |
| 26 | 1.45062 | 9.59041 | 9.69950 | 8.6012 |
| 27 | 1.50989 | 9.66854 | 9.78573 | 8.8759 |
| 28 | 1.57219 | 9.74428 | 9.87030 | 9.1654 |
| 29 | 1.63743 | 9.81750 | 9.95311 | 9.4690 |
| 30 | 1.70554 | 9.88806 | 10.03407 | 9.7863 |
| 31 | 1.77642 | 9.95582 | 10.11307 | 10.1169 |
| 32 | 1.85000 | 10.02066 | 10.19000 | 10.4601 |

What the table describes (for orientation, the table governs):
- rows 1 to about 4.6: the **root circle**, radius 7.97947, centred on the gear axis (delta 0 to about 2.6);
- rows 5 to 13: a **concave root fillet** whose radius of curvature is about 0.55 to 0.65 (not a constant arc);
- rows 14 to 32: the **flank**, convex, radius of curvature about 2.4 to 2.5, with an inflection at about r = 8.55;
- row 32: the flank meets the tip circle r = 10.19 at y = 1.85 exactly, with a sharp corner.

Measured check values of the transverse section: space angular width at the tip circle 20.920 (tooth tip land 6.772);
at r = 9.19239 the space spans 14.739 and the tooth 12.953 (transverse tooth arc thickness 2.078).

## 5. Geometry of P01 (build in this order)

**F1. Turned blank.** Solid of revolution about X. Profile in (x, r), closed, revolved 360:
(-10, 0) -> (-10, 10.19) -> (0, 10.19) -> (0, 7.5) -> (10, 7.5) -> (10, 0) -> back to (-10, 0).
That is a rim cylinder diameter 20.38 from X = -10 to 0 and a hub cylinder diameter 15 from X = 0 to 10.

**F2. Rim edge rounds.** Round both outer circular edges of the rim (r = 10.19 at X = -10 and at X = 0) with radius
**0.75**. The round surfaces are tori about X: tube-centre circle radius 9.44 at X = -9.25 and X = -0.75, tube radius
0.75. After the teeth are cut these rounds remain only on the tip lands (13 small round patches per face).

**F3. Hub fillet.** The concave edge between the hub cylinder (r = 7.5) and the rim face X = 0 is filleted with radius
**0.4** (torus about X, tube-centre circle radius 7.9 at X = 0.4). The fillet ends on the face X = 0 at r = 7.9, inside
the root circle, so it does not touch the teeth.

**F4. Hub end chamfer.** The outer edge of the hub end face X = 10 has a **0.3 x 45** chamfer: a cone from r = 7.5 at
X = 9.7 to r = 7.2 at X = 10.

**F5. Bore.** Plain through bore, **diameter 6**, on the X axis from X = -10 to X = 10. At the hub end X = 10 a
**0.3 x 45** chamfer: cone from r = 3.3 at X = 10 to r = 3.0 at X = 9.7. The bore edge on the face X = -10 is **sharp**
(no chamfer). No keyway, no set-screw hole, no thread.

**F6. Helical tooth spaces, 13 places.** Cut 13 tooth spaces through the full rim (X = -10 to X = 0), each bounded by
the T1 profile (section 4) swept helically:
- In the plane X = x, the space centres sit at polar angles
  **phi_k(x) = 90 - 6.25 (x + 10) + k 360/13**, k = 0..12.
  At X = -10 one space is centred on +Z (phi 90); at X = -5 the centres are at 58.75 + k 27.6923; at X = 0 at
  27.5 + k 27.6923.
- A point (y, z) of T1 is carried to the plane X = x by rotating it about the X axis by **-6.25 (x + 10)** degrees
  (negative = from +Z towards +Y). The profile shape does not change along X.
- The cutting region of one space is the T1 profile closed outward beyond the tip circle (any closure at r > 10.19).
  Equivalent construction: the full transverse section (13 spaces, the root arcs and the r = 10.19 tip arcs between
  them) swept helically from X = -10 to X = 0 with a twist of -62.5, intersected with the F1-F3 blank.
- Teeth are centred at phi_k(x) + 13.8462. Every tooth and space is identical (no single modified space).

Check points on the master surface (all lie on the flank, within 0.0005):
- X = -5, flank point (-5, -2.65121, 8.76056) and its mirror partner (-5, -4.77311, 7.80985) (both r = 9.153);
- X = -9: (-9, 0.04776, -9.15282); X = -1: (-1, -6.98077, -5.91990) (the same flank, r = 9.153);
- root circle point (-5, -7.82600, 1.55749).

All edges not mentioned are sharp (tooth tip corners, flank-to-face edges, the root at both faces).

## 6. Acceptance targets

| ID | Volume mm3 | Area mm2 | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 Gear | 3771.33 | 2432.03 | -1.0735 | 0.0001 | -0.0001 | -10.000 | 10.000 | -10.190 | 10.190 | -10.190 | 10.190 | 68 |

Volume note: B-rep integration 3771.33, triangulated integration 3770.07 (0.03 %); the target is 3771.33 +/- 0.05 %.
The Y extent reaches 10.1899 at +Y (no tip land lies exactly on +Y); treat as 10.19.
Face census of the master (for orientation only): 13 freeform tooth-space faces (each one face from tip to tip), 15 tip
land cylinder faces (13 lands, seam splits), 27 tip-round torus faces, 2 hub-fillet torus faces, 4 cone faces
(2 chamfers), 4 cylinder faces (bore, hub), 3 planes (X = -10, 0, 10).

Check values: tip diameter 20.38; root diameter 15.959; hub diameter 15; bore 6; face width 10; hub length 10; overall
length 20; 13 teeth; lead 57.6, left hand; twist across the face 62.5.

## 7. Undetermined items

- Nominal pressure angle 20 and module 1 are product data; the master's tooth form does not follow an exact involute
  with those values, so they are not used for the geometry. Table T1 is the governing form.
- No tolerances, surface finish or heat-treat data are in the master. Material (medium-carbon steel) is product data only.
