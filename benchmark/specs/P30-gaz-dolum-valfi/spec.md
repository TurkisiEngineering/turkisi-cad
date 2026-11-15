# Design specification: threaded-sleeve gas filling valve with hex body and fluted cap

Small fill valve for compressed gas as supplied: a hexagon body with an external metric inlet thread, a thin threaded
sleeve standing on top of it, and a fluted (knurled) protective cap over the sleeve. This document is the only source
for the rebuild. Every dimension below was measured from the original 3D geometry.

## 1. Units and global frame

- **Units: millimetres.** All coordinates and dimensions are mm.
- **Global frame (use exactly, no realignment):**
  - **The valve axis is the Y axis** (x = 0, z = 0). +Y points from the inlet thread up to the cap.
  - The inlet end face is **y = -14**; the cap top is **y = 10.5**.
  - The hexagon has two flats normal to Z (z = +/-6) and corners on the X axis (x = +/-6.9282).
- **Conventions:** rho = distance from the Y axis = sqrt(x^2 + z^2); "(rho, y)" = half-section of a body of revolution
  about Y. Plan angle psi = angle in the XZ plane measured **from +X toward +Z**.
- Every body is modelled in place in this frame (identity placement). Model each body as a separate solid.

## 2. Product description and the source's own simplifications

The **valve body** (P01) is a hexagon nut shape with a collar below it, an external M10 x 1 thread below the collar
and a filleted shoulder on top; it has a plain through bore. The **sleeve** (P02) is a thin tube carrying a fine
external thread (0.305 in, 32 per inch); it stands on the body's top shoulder. The **cap** (P03) is a closed fluted
cap with a plain blind bore; it hangs over the sleeve without touching it.

**Simplifications that exist in the source model and must be reproduced:**
- No valve core, spring, seal or internal thread: the body and the sleeve have a plain bore of diameter 6.5; the cap
  bore is plain (diameter 8.0) and does not touch the sleeve thread.
- Both external threads are modelled as helical grooves (section 4). **The inlet thread groove continues past the end
  of the thread as a closed helical tunnel inside the collar and the hexagon** and ends at a flat face (section 4, B5).
  This is part of the source and must be kept.
- The sleeve wall under its thread root is only 0.108 thick; its top end is a knife edge (the top chamfer reaches the
  bore).

## 3. Part list

3 distinct parts, **3 bodies in total**.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Valve body, hexagon AF 12, M10 x 1 inlet | custom | brass |
| P02 | 1 | Threaded sleeve, 0.305 in - 32 | custom | brass |
| P03 | 1 | Fluted cap | custom | plastic |

## 4. Part geometry

### Threads (common definition)

Both threads are **straight (not tapered), right-hand, 60 deg**, modelled as one helical groove. In any half-plane
that contains the Y axis the groove is a trapezoid: two straight flanks at **30 deg to the plane normal to the axis**,
a flat at the outer radius and a flat at the inner radius, both flats parallel to the axis and **p/8 wide** (axial
widths). Thread depth = 0.6495 p. **Phase:** theta = 0 is the half-plane toward **+X**, theta increases toward **-Z**
(right-hand rotation about +Y); at angle theta every flat position moves **up (+Y) by p x theta / 360 deg**.

**T1. Inlet thread M10 x 1** (P01): p = 1.0; outer radius **5.0**, inner radius **4.35048** (depth 0.64952); flats
0.125 wide. At theta = 0 the outer flats are centred at **y = -12.4375 + n** (n integer: ..., -12.4375, -11.4375,
-10.4375, -9.4375) and the inner flats at **y = -12.9375 + n**. Example: at theta = 90 deg (toward -Z) the outer flats
are centred at -12.1875, -11.1875, ...

**T2. Sleeve thread** (P02): **p = 0.79375 (32 per inch)**; outer radius **3.8735** (diameter 7.747), inner radius
**3.35794** (depth 0.51556); flats 0.09922 wide. At theta = 0 the outer flats are centred at **y = 0.0965 + n p**
(..., -1.4910, -0.6973, 0.0965, 0.8903, 1.6840, 2.4778, 3.2715, 4.0652, 4.8590) and the inner flats at
**y = 0.49336 + n p**. At theta = 90 deg the outer flats are at 0.2949 + n p.

### P01 Valve body (one solid, 47 faces in the original)

**B1. Body of revolution (before the hexagon and the thread)**, half-section (rho, y) from the bottom:
- **inlet end face y = -14**, ring from the bore rho 3.25 out to rho 4.22;
- **45 deg chamfer** rho = 4.22 + (y + 14) up to (5.0, -13.22);
- **thread cylinder rho 5.0** (thread T1) up to the collar underside **y = -8.525**;
- collar underside ring y = -8.525 out to **rho 6.0**; **collar cylinder rho 6.0** up to **y = -7.525**.

**B2. Hexagon AF 12.0** (flats at 6.0 from the axis, flats normal to Z, corners at rho 6.9282 at psi 0, 60, ...
300 deg), from **y = -7.525** (flat underside outside the collar) up to **y = -3.525**. The top is chamfered by the cone
**rho = 6.0 + (-3.525 - y)** (45 deg, through the AF circle at the top face, reaching the corners at y = -4.4532).

**B3. Top:** hexagon top face **y = -3.525** inside rho 6.0; a concave **fillet R1.5** (centre rho 5.3735, y -2.025),
tangent to the top face at rho 5.3735, rising to the **shoulder y = -2.025** at rho 3.8735 (where its tangent is
vertical); the shoulder is the ring y = -2.025 from rho 3.8735 in to the bore.

**B4. Bore:** plain through bore **rho 3.25 (diameter 6.5)** from y = -14 to y = -2.025.

**B5. Thread T1** cut into the thread cylinder from the chamfer to the collar (the groove runs out through the chamfer
at the bottom). **Above the collar underside (y > -8.525) the same helical groove continues inside the material as a
closed tunnel** whose cross-section is the groove profile closed by the cylinder rho 5.0 (the region between rho
4.35048 and rho 5.0 that the groove would remove). The tunnel ends at a **flat end face in the half-plane theta = 180
deg** (plane z = 0, x < 0), where the inner flat is centred at y = -4.4375; the end face spans y from -4.875 to -4.0
at rho 5.0 and from -4.5 to -4.375 at rho 4.35048.

### P02 Threaded sleeve (one solid, 28 faces)

- Tube **bore rho 3.25** from **y = -2.025** (flat bottom face, ring rho 3.25 to 3.8735, standing on the body shoulder)
  up to **y = 5.6735**.
- Outside: **thread T2** on the cylinder **rho 3.8735** from the bottom face (the groove runs out through it) up to the
  top chamfer **rho = 3.8735 - (y - 5.05)** (45 deg) from y = 5.05, which reaches the bore at **y = 5.6735**: the top is
  a knife edge (no top face).

### P03 Fluted cap (one solid, 82 faces)

**C1. Blank, body of revolution**, half-section (rho, y):
- **bottom face**: the cone from **(4.0, 0.1109)** to **(5.5, 0.6)** (rho = 3.66 + 3.06667 y; it rises outward,
  18.06 deg to the plane normal to Y);
- **cylinder rho 5.5** from y = 0.6 up to **y = 4.32474**;
- **barrel arc R8.8**, centre (rho -3.3, y 4.32474) (i.e. on the far side of the axis), tangent to the cylinder at
  (5.5, 4.32474), up to (3.7185, 9.6332);
- **round R1.0**, centre (2.920974, 9.03), tangent to the barrel arc and to the **top face y = 10.03**;
- top face y = 10.03 from rho 2.920974 in to rho 1.83;
- **button**: arc R0.7, centre (1.168865, 9.8), from (1.83, 10.03) up to (1.168865, 10.5) (its top point), then the
  **flat button top y = 10.5** in to the axis.

**C2. Blind bore** rho 4.0 (diameter 8.0) from the bottom (y = 0.1109) up to a **flat end at y = 6.0**.

**C3. Sixteen flutes**, straight grooves parallel to Y, centred at **psi = 0, 22.5, 45, ... 337.5 deg**. In any plane
normal to Y each flute is a V of **75 deg included angle**, symmetric about the radial line at psi_k, with a round
bottom **R0.2** whose centre lies on that radial line at rho 5.0 (flute bottom at rho 4.8); the flanks are tangent to
the R0.2 arc (each flank lies 2.843807 from the Y axis, at 37.5 deg to the radial line). The flutes cut through the
bottom cone, the cylinder and the barrel and run out where the barrel radius falls below rho 4.8 (y = 7.7642). Between
the flutes the cylinder rho 5.5 / barrel surface remains (ridges about 9.7 deg wide on rho 5.5).

## 5. Assembly

All three bodies in place, identity placement.
- The sleeve's bottom face y = -2.025 sits on the body shoulder y = -2.025 (face contact; same bore).
- The cap is clear of the sleeve (cap bore rho 4.0 > sleeve thread rho 3.8735; bore end y = 6.0 above the sleeve top
  y = 5.6735) and of the body (cap bottom y >= 0.1109).
- **No overlapping pair.**

## 6. Acceptance targets

Measured at the supplied pose. Suggested tolerance for a one to one rebuild: volume within 0.5 percent per body,
centre of mass within 0.5 mm, bounding box within 0.13 mm. The faces column is information only.

| ID | Name | Vol mm3 | Vol mm3 | Area mm2 | Area mm2 | CoM x | CoM y | CoM z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Valve body | 628.300 | 628.30 | 1205.2523 | 1205.25 | 0.0007 | -7.3855 | 0.0100 | -6.9282 | 6.9282 | -14.0000 | -2.0250 | -6.0000 | 6.0000 | 47 |
| P02 | Threaded sleeve | 59.382 | 59.38 | 467.6636 | 467.66 | -0.0301 | 1.7046 | -0.0090 | -3.8736 | 3.8735 | -2.0250 | 5.6735 | -3.8735 | 3.8735 | 28 |
| P03 | Fluted cap | 476.400 | 476.40 | 652.4869 | 652.49 | -0.0000 | 5.7756 | 0.0000 | -5.4661 | 5.4661 | 0.1109 | 10.5000 | -5.4661 | 5.4661 | 82 |

**Whole assembly:** 3 bodies; total volume 1164.083 mm3; total area 2325.403 mm2; centre of mass (-0.0012, -1.5356,
0.0049) mm; bounding box X [-6.9282, 6.9282], Y [-14, 10.5], Z [-6, 6] mm.

**Key functional checks:** inlet end face to cap bore end 20.0; hexagon top face to cap bore end 9.525 (3/8 in);
hexagon 12 across flats; inlet thread outer diameter 10.0, pitch 1.0; sleeve thread outer diameter 7.747 (0.305 in),
32 per inch.

## 7. Source conflicts and undetermined items

**Authority:** the original 3D geometry governs.

| Item | Drawing / product data | Original 3D | Decision |
|---|---|---|---|
| 20 mm | overall dimension, inlet end to the upper reference line | inlet end face y = -14 to the cap bore end y = 6.0: 20.0 | Agree. |
| 3/8 in | hexagon top to the same upper reference line | hexagon top y = -3.525 to y = 6.0: 9.525 | Agree. |
| 12 mm hex | across flats | 12.0 | Agree. |
| M10 x 1 | inlet thread | outer diameter 10.0, pitch 1.0 | Agree. |
| 0.305 in - 32 | sleeve thread | outer diameter 7.747, pitch 0.79375 | Agree. |

**Undetermined:** valve core, seal and any internal thread (none modelled); the exact shape of the thread run-outs (the
grooves simply run out through the chamfer and the sleeve bottom face; the inlet groove ends as described in B5).
