# Design specification: ribbed comfort-grip knob with threaded through insert (P10)

A moulded hand knob: a rigid plastic core (lobed head, hollow underside with radial ribs, tapered hub), a soft coating
moulded over the head, and a brass threaded insert in the hub. This document is the only source for the rebuild. Every
value was measured from the master 3D geometry.

## 1. Units and global frame

- **Units: inches.** All coordinates and dimensions are inches unless marked mm (1 in = 25.4 mm exactly). Angles in
  degrees.
- **Global frame (use exactly, no realignment):**
  - The knob axis is the **Z axis**. The domed top of the head faces **+Z**; the hub points to **-Z**.
  - The hub end face is the plane z = -0.68; the insert's lower end is flush with it. The top of the coating is at
    z = 0.68.
  - Angles θ are measured in the XY plane from **+X toward +Y**. The 8 scallops of the head are centred at
    θ = 22.5° + k·45°; the 8 lobes (and the 8 underside ribs) are centred at θ = k·45° (k = 0..7). So a lobe and a rib sit
    on the +X axis.
- "(r, z)" = a profile in a half plane containing the Z axis (r = distance from Z), revolved 360° about Z.
  "Prism of outline L from z1 to z2" = the plane region L extruded parallel to Z between those planes.
- Every body is modelled in place in this frame (identity placement).

## 2. Body list

3 bodies, 3 distinct parts, one of each.

| ID | Qty | Name | Type | Material (product data) |
|---|---|---|---|---|
| P01 | 1 | Knob core (lobed head, ribs, hub) | custom | polypropylene |
| P02 | 1 | Grip coating over the head (0.06 thick skin) | custom | rubber |
| P03 | 1 | Threaded insert, 3/8"-16, 0.5 long | bought-in hardware | brass |

The three bodies touch face to face (no gaps, no overlap): the coating lies on the core, the insert sits in the core's
seat bore. Keep them as three separate solids.

## 3. Plan outlines used below (all made of circular arcs)

Scallop centres: 8 points on the circle of radius **1.39** about Z at θ = 22.5° + k·45°
(the first one is (1.284193, 0.531929)).

| Name | Construction | Resulting corners |
|---|---|---|
| **L0** (core outer) | circle R1.2 about Z minus 8 discs R0.33 about the scallop centres | 16 sharp corners at θ = 22.5° ± 11.992° (r 1.2) |
| **Lci** (core rim inner) | circle R1.11 minus 8 discs R0.39 about the scallop centres | 16 sharp corners at θ = 22.5° ± 12.547° (r 1.11) |
| **Lo** (coating outer) | circle R1.26 minus 8 discs R0.27 about the scallop centres; then every one of the 16 corners rounded R0.1 | round centres at r 1.16, θ = 22.5° ± 13.106°; e.g. centre (1.144445, 0.189335), tangent to R1.26 at θ 9.394° and to the scallop arc at (1.182213, 0.281929) |
| **Li** (coating liner inner) | circle R1.05 minus 8 discs R0.45 about the scallop centres; then every one of the 16 corners rounded R0.1 | round centres at r 0.95, θ = 22.5° ± 16.511°; e.g. centre (0.944815, 0.099122), tangent to R1.05 at θ 5.989° and to the scallop arc at (1.006520, 0.177815) |

Lo is L0 offset outward by 0.06 (with its corners rounded); Li is Lci offset inward by 0.06 (with its corners rounded).
The scallop arc radii: core outer 0.33, core inner 0.39 (wall 0.06 thick around each scallop), coating outer 0.27,
liner inner 0.45.

## 4. P01 Knob core (one solid, 123 faces in the master)

**C1. Main revolve about Z.** Closed (r, z) profile, in this order, last segment closes on the start:
1. start (0, -0.68), line to (0.606021, -0.68)  (hub end face)
2. convex arc R0.02, centre (0.606021, -0.66), to (0.625994, -0.661047)  (hub end round, tangent to both neighbours)
3. line to (0.654348, -0.12)  (hub outer cone: r = 0.625 + tan 3° · (z + 0.68), i.e. 1.25 dia at z = -0.68, 3° draft)
4. line to (1.2, -0.12)  (head underside level)
5. line to (1.2, 0.44)  (head rim, dia 2.4)
6. line to (1.06, 0.44)  (top flat ring)
7. convex arc R2.175763, centre (0.124593, -1.524424), to (0.492553, 0.62)  (domed top)
8. line to (0, 0.62).

**C2. Scallops.** Cut 8 cylinders R0.33 parallel to Z, centred on the scallop centres, through the whole head height.
The head's plan outline becomes L0 (min radius 1.06 at a scallop centre, which is exactly where the dome starts, so the
top flat ring is interrupted at each scallop centre). The hub is not touched.

**C3. Underside cavity.** Subtract the region K = (K1 ∪ K2) − hub − ribs, where
- K1 = prism of Lci from z = -0.12 to z = 0.26 (rim inner wall: R1.11 at the lobes, R0.39 arcs around the scallops,
  rim wall 0.09 thick at the lobes and 0.06 thick round the scallops);
- K2 = the revolve of (0, 0.26) → (1.01, 0.26) → (0.92, 0.35) → (0, 0.35) intersected with the prism of Lci (a flat
  ceiling at z = 0.35 inside r 0.92, a 45° conical chamfer down to r 1.01 at z = 0.26, then the flat step z = 0.26 out to
  the rim wall). Because the cone is clipped by Lci, at each scallop the R0.39 wall runs up to z = 0.27 (where the cone
  radius equals 1.0) and the step plane z = 0.26 is interrupted there;
- hub = everything inside the hub cone of C1 step 3 extended upward (r ≤ 0.625 + tan 3° · (z + 0.68)): the hub cone
  continues up to the ceiling z = 0.35 (r 0.678979 there);
- ribs = 4 slabs 0.05 thick (±0.025 about a vertical plane through Z) at θ = 0°, 45°, 90°, 135°, i.e. 8 radial ribs at
  θ = k·45°. The ribs therefore fill the cavity cross-section completely: each rib runs from the hub cone to the rim
  wall, its bottom edge is flush with the rim bottom z = -0.12 and its top follows the ceiling (0.35 flat, 45° cone,
  0.26 step).

**C4. Bore** (cut, revolve about Z). Profile:
- insert seat: r 0.265625 (dia 0.53125) from z = -0.68 up to z = -0.18;
- flat step z = -0.18 from r 0.265625 out to r 0.36;
- tapered bore: line from (0.36, -0.18) to (0.401182, 0.605785) (3° taper, r = 0.36 + tan 3° · (z + 0.18));
- round R0.015, centre (0.416161, 0.605), from (0.401182, 0.605785) to (0.416161, 0.62) on the top face.
So the core's top face z = 0.62 is a flat annulus from r 0.416161 to 0.492553 (where the dome starts).

**C5. Hub end ridge** (add). Annulus r 0.385417 to 0.505208, from z = -0.695 to -0.68 (0.015 proud of the hub end
face). Edges sharp.

All other core edges are sharp (no other rounds or drafts than stated).

## 5. P02 Grip coating (one solid, 292 faces in the master)

A 0.06 thick skin over the head: it covers the rim outside, the dome top (with a central opening), the rim bottom and
the rim inside down to the liner, wrapping every outer edge with R0.06 rounds. Build:

**S1.** B = prism of **Lo** from z = -0.18 to z = 0.5, minus prism of **Li** from below z = -0.18 up to z = 0.26.
(A lobed cup open at the bottom: wall between Li and Lo, closed above z = 0.26.)

**S2. Edge rounds R0.06** on B, three closed edge loops:
- the outer bottom loop (Lo at z = -0.18),
- the outer top loop (Lo at z = 0.5),
- the inner bottom loop (Li at z = -0.18).
Along the R0.1 plan corners these rounds become toroidal (outer loops: tube radius 0.06 about a centre line of radius
0.04; inner loop: about a centre line of radius 0.16). The centre lines of the outer rounds lie on L0 with its corners
rounded R0.04, at z = -0.12 and z = 0.44; the centre line of the inner round lies on Lci with its corners rounded R0.16,
at z = -0.12 (i.e. the rounds are concentric with the core's edges).

**S3. Dome cap** (add). Revolve (0, 0.5) → (1.06, 0.5) → convex arc R2.230085, centre (0.124593, -1.524424) (same
centre as the core dome) → (0.461925, 0.68) → (0, 0.68). It lies inside the flat top of B, so it only adds the dome.

**S4. Cuts:**
- prism of **Lci** from z = 0.26 to z = 0.35 (frees the core's ceiling region; the liner top is the flat plane z = 0.26);
- top opening, revolve: r ≤ 0.421954 for z ≤ 0.62; a cone from (0.421954, 0.62) to (0.461925, 0.674670); then a
  cylinder r 0.461925 (dia 0.92385) from z = 0.674670 up through the top (the dome reaches z = 0.68 exactly at
  r 0.461925, so the coating has no flat top face);
- the core P01 (subtract the finished core): this leaves the coating's inside faces congruent with the core (rim
  outside R1.2 / R0.33, rim bottom z = -0.12, rim inside R1.11 / R0.39, core dome, core top annulus z = 0.62 from r
  0.421954 to 0.492553) and cuts the liner by the 8 ribs (8 slots 0.05 wide from z = -0.12 to 0.26).

Result checks: coating thickness 0.06 everywhere on the outer faces; below the rim bottom (z = -0.18 to -0.12) the
coating is a continuous lobed ring, also under the rib ends; the liner (between Li and Lci, z -0.18 to 0.26) is split into
8 segments above z = -0.12 by the rib slots. Outer dia 2.52 (at the lobes); min outer radius 1.12 (scallop centres).

## 6. P03 Threaded insert (one solid, 27 faces in the master)

- Plain tube outside: cylinder R0.265625 (dia 0.53125) from z = -0.68 to z = -0.18 (length 0.5). End faces flat.
- **Internal thread, modelled:** 3/8"-16, **right-hand**, single start, pitch **0.0625**, 60° included flank angle.
  - Major (root) radius 0.1875 (dia 0.375) with an axial flat 0.0078125 (P/8);
  - minor (crest) radius 0.146906 (dia 0.293811) with an axial flat 0.0078125 (P/8);
  - flanks at 30° to the radial direction (radial depth 0.040594, axial run 0.0234375 each).
  - **Phase:** in the half plane θ = 0 (+X side) the root flat is centred at z = -0.379218 + 0.0625·k (k integer).
    Right-hand: moving round the axis from +X toward +Y the profile rises in +Z by 0.0625 per turn (at θ = 90° the root
    flat is centred at z = -0.363593 + 0.0625·k).
  - The thread runs the full length; it is interrupted only by the two countersinks.
- **Countersinks**, both ends, 90° included (45° cones): from r 0.21875 (dia 0.4375) at the end face to r 0.1875 at
  0.03125 from the face (z = -0.68 → -0.64875 and z = -0.18 → -0.21125); the cones cut through the thread.
- In the master the minor (crest) surface and the flanks are free-form helical surfaces; that is a property of the
  source, any exact helical representation is fine.

## 7. Acceptance targets (from the master)

| ID | Volume in3 (mm3) | Area in2 (mm2) | CoM x, y, z (in) | Bbox X | Bbox Y | Bbox Z | faces |
|---|---|---|---|---|---|---|---|
| P01 core | 2.07189 (33952.27) | 24.9600 (16103.22) | 0, 0, 0.07567 | ±1.2 | ±1.2 | -0.695 .. 0.62 | 123 |
| P02 coating | 0.72941 (11952.84) | 25.8622 (16685.26) | 0, 0, 0.22687 | ±1.26 | ±1.26 | -0.18 .. 0.68 | 292 |
| P03 insert | 0.06340 (1038.98) | 1.8851 (1216.21) | -0.00012, -0.00032, -0.43003 | ±0.265625 | ±0.265625 | -0.68 .. -0.18 | 27 |

**Whole assembly:** 3 bodies; volume 2.86470 in3 (46944.09 mm3); area 52.7074 in2 (34004.70 mm2); centre of mass
(0, 0, 0.10298) in; bounding box X, Y ±1.26, Z -0.695 .. 0.68 (mm: ±32.004; -17.653 .. 17.272). No overlaps between
the bodies (contact only).

Check values: head dia 2.52 (coating), core rim dia 2.4; head height 0.68 (coating bottom z -0.18 to its top flat
z 0.5), 0.86 to the top of the dome; hub dia 1.25 at the hub end (3° draft); hub length 0.5 (z -0.18 to -0.68) plus
the 0.015 ridge; insert 0.5 long, thread 3/8"-16; coating thickness 0.06; 8 lobes, 8 ribs 0.05 thick.

## 8. Undetermined items and source notes

- The insert's small CoM offset from the axis comes from the helical thread; reproduce the stated phase and it follows.
- No knurl or retention grooves are modelled on the insert outside; the core has no other drafts than the 3° hub and
  bore cones. Keep it so.
- Nothing else is undetermined.
