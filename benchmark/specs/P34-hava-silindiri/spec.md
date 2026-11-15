# Design spec: compact single-acting pneumatic clamp cylinder on a rectangular base block

## 1. Units, frame, deliverable

- **Unit: inch.** Every length below is in inch unless marked mm; angles in degrees. All values are round in inch
  (fractions of 1/16, 1/32, 1/64 or three / four decimals). Volumes in in³ (and mm³), areas in in² (and mm²).
- **Global frame (use it exactly, no re-centring, no rotation):**
  - **+Y = cylinder axis, pointing up** from the base towards the rod end. The cylinder axis is the global Y axis
    (X = 0, Z = 0).
  - **Y = 0** is the flat underside (mounting face) of the base block.
  - **X** runs through the two mounting ears (ear holes at X = ±0.8125).
  - **+Z** is the side of the air port: the port boss sticks out of the base towards +Z and its threaded hole
    points along −Z into the block.
- The assembly is delivered as **one STEP file containing 7 separate solids** (no fusing, no booleans between bodies),
  each solid in its final position in the global frame. Bodies are not to be merged even where they overlap (section 7).

## 2. Product and what the source model contains

A compact pneumatic clamping cylinder: an aluminium base block with two mounting ears and a side air port (1/8 pipe
size, tapered thread), a short barrel tube pressed into the base, a head cap on top of the barrel, a threaded stop
sleeve screwed through the head cap and locked by a jam nut (the sleeve sets the stroke, 0 to 1 in), and a steel
piston rod (piston Ø1.0, rod Ø5/16). Air extends the rod, a spring returns it.

Source simplifications, keep them exactly as described:

- **The piston rod appears twice**: once retracted (piston on the base floor) and once fully extended, 1.000 higher
  in +Y. Both are complete, identical solids and both must be delivered. They overlap each other (section 7).
- **The fine thread between stop sleeve, head cap and jam nut is not modelled.** The sleeve is a plain Ø1.000
  cylinder; the cap and the nut have plain Ø0.9459 bores (the thread minor diameter). The sleeve therefore overlaps
  the cap and the nut by the thread depth; keep that overlap.
- The **return spring, seals and O-rings are not modelled.** The barrel's O-ring groove is modelled as a plain
  rectangular groove.
- The **air port is modelled with a real helical taper thread** (27 per inch, right hand). The port's drill does not
  break through into the barrel bore (the source has no air passage; keep it closed).
- The pistons touch the barrel bore and the stop sleeve touches the retracted piston face-to-face (zero overlap).
- No fillets other than the four concave blends of the base outline; all other edges are sharp except the 45°
  chamfers listed per body.

## 3. Part list

| Name | Kind | Count | Description |
|---|---|---|---|
| P01-a | custom | 1 | piston rod, retracted position |
| P01-b | custom | 1 | piston rod, extended position (same part as P01-a, +1.000 in Y) |
| P02 | custom | 1 | stroke stop sleeve (adjusting screw, thread not modelled) |
| P03 | custom | 1 | barrel tube |
| P04 | custom | 1 | head cap |
| P05 | hardware | 1 | jam nut (thread not modelled) |
| P06 | custom | 1 | base block with mounting ears and air port |

Distinct parts: 6 (P01 ×2, P02, P03, P04, P05, P06). Total solids: 7. All bodies are coaxial with the global Y axis
except the features of the base block that are placed off-axis.

## 4. Per-body geometry

Bodies of revolution are given as a **half-section in the (r, Y) plane** (r = radial distance from the Y axis),
listed as a closed polygon of (r, Y) vertices, revolved 360° about the global Y axis. Straight segments join
consecutive vertices; the last vertex joins the first.

### 4.1 P01 piston rod (P01-a retracted, P01-b extended)

One solid of revolution: a piston disc and a rod. Half-section of **P01-a** (r, Y):

(0, 0.2400) → (0.5000, 0.2400) → (0.5000, 0.8105) → (0.15625, 0.8105) → (0.15625, 3.78435) → (0.12500, 3.81560) →
(0, 3.81560)

- Piston: Ø1.000, from Y 0.2400 to 0.8105 (thickness 0.5705), sharp edges.
- Rod: Ø0.3125 (5/16), from the piston top Y 0.8105 to Y 3.78435.
- Rod end: 45° chamfer 0.03125 × 0.03125, end face Ø0.2500 at Y 3.8156.
- Overall length 3.5756.

**P01-b** is the identical solid translated by **+1.000 in Y** (piston from Y 1.2400 to 1.8105, rod end face at
Y 4.8156). The offset equals the maximum stroke.

### 4.2 P02 stroke stop sleeve

Solid of revolution with two blind spanner holes in its top face. Half-section (r, Y):

(0.37500, 0.8105) → (0.47025, 0.8105) → (0.50000, 0.84025) → (0.50000, 2.28075) → (0.47025, 2.31050) →
(0.15725, 2.31050) → (0.15725, 1.93550) → (0.37500, 1.93550)

- Outside Ø1.000 from Y 0.8105 to 2.3105 (length 1.500), 45° chamfer 0.02975 at both outer ends.
- Bottom bore Ø0.7500, open at the bottom face (Y 0.8105), flat floor at Y 1.9355 (depth 1.125).
- Rod hole Ø0.3145 through the top, from Y 1.9355 to 2.3105 (clearance on the Ø0.3125 rod).
- **Two spanner holes Ø0.1285**, axes parallel to Y at **(X 0, Z +0.3594)** and **(X 0, Z −0.3594)** (centre distance
  0.7188), drilled from the top face Y 2.3105 down to a **flat bottom at Y 1.8735** (depth 0.437). Their inner sides
  break into the Ø0.75 bore (the hole circles reach to r 0.2951 < 0.375), so the lower 0.062 of each hole opens
  sideways into the bore.

### 4.3 P03 barrel tube

Tube of revolution, bore Ø1.000 through. Half-section (r, Y):

(0.500, 0.24000) → (0.572, 0.24000) → (0.572, 0.33300) → (0.593, 0.33300) → (0.593, 0.61575) → (0.572, 0.61575) →
(0.572, 0.70875) → (0.593, 0.70875) → (0.593, 1.43550) → (0.572, 1.43550) → (0.572, 1.81050) → (0.500, 1.81050)

- Bore Ø1.000 from Y 0.2400 to 1.8105 (length 1.5705). All edges sharp.
- Outside Ø1.186, with three reduced lands of Ø1.144:
  - bottom band Y 0.2400–0.3330 (height 0.093),
  - O-ring groove Y 0.61575–0.70875 (width 0.093),
  - top spigot Y 1.4355–1.8105 (length 0.375), on which the head cap sits.

### 4.4 P04 head cap

Ring of revolution. Half-section (r, Y):

(0.57200, 1.48600) → (0.65200, 1.48600) → (0.68200, 1.51600) → (0.68200, 2.08100) → (0.65200, 2.11100) →
(0.50000, 2.11100) → (0.47295, 2.08395) → (0.47295, 1.83755) → (0.50000, 1.81050) → (0.57200, 1.81050)

- Outside Ø1.364 from Y 1.486 to 2.111 (height 0.625), 45° chamfer 0.030 on both outer edges.
- Counterbore Ø1.144 from the bottom face Y 1.486 up to a flat shoulder at Y 1.8105 (depth 0.3245); it fits over
  the barrel's top spigot (coincident surfaces, no overlap).
- Through bore Ø0.9459 (plain; thread minor diameter) with a 45° entry chamfer of 0.02705 at both ends that opens it
  to Ø1.000 at Y 1.8105 and at Y 2.111.

### 4.5 P05 jam nut

Ring of revolution. Half-section (r, Y):

(0.50000, 2.11100) → (0.65750, 2.11100) → (0.68750, 2.14100) → (0.68750, 2.26800) → (0.65750, 2.29800) →
(0.50000, 2.29800) → (0.47295, 2.27095) → (0.47295, 2.13805)

- Round nut (no flats in the source), outside Ø1.375, from Y 2.111 to 2.298 (thickness 0.187), 45° chamfer 0.030 on
  both outer edges. It sits on the top face of the head cap.
- Bore Ø0.9459 (plain) with a 45° chamfer of 0.02705 at both ends to Ø1.000.

### 4.6 P06 base block

A prismatic block between the planes **Y 0 and Y 0.705**, plus a port boss towards +Z, with the bores and holes
below. Build it as the union of (a) and (b), then remove (c)–(f).

**(a) Main outline**, in the XZ plane, extruded along +Y from Y 0 to Y 0.705. The outline is the union of:
- a circle Ø1.500 (R 0.75) centred on the origin;
- two ear circles R 0.1875 centred at (X ±0.8125, Z 0) (outer ear ends at X ±1.000, total width 2.000);
- four concave blends R 0.25 that join each ear circle tangentially to the R 0.75 circle. Their centres are at
  (X ±0.903846, Z ±0.427850) (centre distance 1.000 from the origin and 0.4375 from the ear centre). The tangent points
  are (±0.67788, ±0.32089) on the R 0.75 circle and (±0.85165, ±0.18336) on the ear circle.

**(b) Port boss**, a profile in the XY plane extruded along +Z from Z 0 to **Z 1.000** (it merges with the outline):
- rectangle X −0.3125 … +0.3125, Y 0 … 0.3925, plus a half-disc R 0.3125 centred at (X 0, Y 0.3925) on top of it;
  the half-disc is cut off by the top plane Y 0.705 (its apex would be at Y 0.705 exactly, so it just touches).
- The boss ends in a flat face at Z 1.000; its sides are the planes X ±0.3125 and the R 0.3125 half-cylinder (axis
  parallel to Z through X 0, Y 0.3925). Above the half-cylinder the R 0.75 circular wall of (a) continues.

**(c) Two mounting holes** Ø0.200, through (Y 0 to 0.705), axes parallel to Y at (X ±0.8125, Z 0) — concentric with
the ears.

**(d) Underside recess** Ø1.09375 (R 0.546875) centred on the Y axis, from Y 0 to a flat floor at Y 0.0625.

**(e) Barrel bore** Ø1.186 (R 0.593) on the Y axis, from the top face Y 0.705 down to a flat floor at Y 0.240
(depth 0.465). The barrel tube P03 sits in it on its Ø1.186 lands with its bottom face on the floor (coincident,
no overlap). Between the recess floor (Y 0.0625) and the bore floor (Y 0.240) the block is solid.

**(f) Air port**, axis parallel to Z through **(X 0, Y 0.3925)**, entering from the boss face Z 1.000 towards −Z.
Radii below are measured from the port axis; "z" is the global Z coordinate.
- Drill: cone of half-angle 1.788°, radius 0.18117 at z 0.700 growing to 0.18241 at z 0.740; flat bottom (disc) at
  **z 0.700** (port depth 0.300 from the boss face).
- Step: flat annulus at **z 0.740** from r 0.18241 out to r 0.19442.
- Thread major (crest) cone: half-angle **1.780°** (taper 1:16 on diameter), radius **0.20250 at z 1.000**
  (Ø0.405 at the face), radius 0.19442 at z 0.740. From z 0.740 up to the start of the thread the hole wall is this
  plain cone.
- **Tapered pipe thread, 27 per inch (pitch 0.037037), right hand**, cut into the crest cone from about z 0.759 out
  through the boss face:
  - profile symmetric 60° V (flanks at 30° to the radial direction), flat crest 0.0040 wide (axial) lying on the
    crest cone, flat root 0.0047 wide lying on the root cone;
  - root cone: same half-angle 1.780°, radius **0.17790 at z 1.000** (thread depth 0.0246 radially);
  - phase: the centre of a crest flat lies at (X 0, Y 0.3925 − r, z 0.7943) on the −Y side of the port axis, at
    z 0.8035 on the +X side, at z 0.8128 on the +Y side and at z 0.8221 on the −X side (the thread advances towards
    +Z when turned counter-clockwise seen from +Z, i.e. right hand);
  - the groove starts with a short run-in at about z 0.759 (−Y side); the exact run-in shape is undetermined.
- Mouth: a 45° cone, radius 0.2025 at z 1.000 narrowing inward (radius 0.1905 at z 0.988), trims the first thread
  turn at the face.

## 5. Assembly placement and fits (all in the global frame, all coaxial on Y unless stated)

| Body | Y range | Relation |
|---|---|---|
| P06 | 0 … 0.705 | base, underside on Y 0 |
| P03 | 0.240 … 1.8105 | in the base bore, on the bore floor |
| P01-a | 0.240 … 3.8156 | piston on the base bore floor inside the barrel |
| P01-b | 1.240 … 4.8156 | P01-a + 1.000 in Y |
| P02 | 0.8105 … 2.3105 | bottom face touches the top of the P01-a piston; passes through P04 and P05 |
| P04 | 1.486 … 2.111 | on the barrel top spigot, shoulder on the barrel top face Y 1.8105 |
| P05 | 2.111 … 2.298 | on the head cap top face |

## 6. Target table (original, per body; inch, with mm³ / mm² copies)

Columns: name | description | V in³ | V mm³ | A in² | A mm² | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces

| P01-a | Piston rod, retracted | 0.67811 | 11112.24 | 6.2941 | 4060.69 | 0.0000 | 1.1308 | -0.0000 | -0.5000 | 0.5000 | 0.2400 | 3.8156 | -0.5000 | 0.5000 | 9 |
| P01-b | Piston rod, extended | 0.67811 | 11112.24 | 6.2941 | 4060.69 | 0.0000 | 2.1308 | -0.0000 | -0.5000 | 0.5000 | 1.2400 | 4.8156 | -0.5000 | 0.5000 | 9 |
| P02 | Stop sleeve | 0.63892 | 10470.01 | 9.3137 | 6008.82 | -0.0000 | 1.6718 | -0.0000 | -0.5000 | 0.5000 | 0.8105 | 2.3105 | -0.5000 | 0.5000 | 19 |
| P03 | Barrel tube | 0.45841 | 7511.91 | 11.5038 | 7421.80 | 0.0000 | 1.0048 | -0.0000 | -0.5930 | 0.5930 | 0.2400 | 1.8105 | -0.5930 | 0.5930 | 18 |
| P04 | Head cap | 0.36254 | 5940.96 | 6.0092 | 3876.92 | -0.0000 | 1.8412 | -0.0000 | -0.6820 | 0.6820 | 1.4860 | 2.1110 | -0.6820 | 0.6820 | 17 |
| P05 | Jam nut | 0.14022 | 2297.79 | 2.6814 | 1729.93 | -0.0000 | 2.2045 | 0.0000 | -0.6875 | 0.6875 | 2.1110 | 2.2980 | -0.6875 | 0.6875 | 14 |
| P06 | Base block | 0.82984 | 13598.66 | 11.5868 | 7475.32 | 0.0000 | 0.2952 | 0.0783 | -1.0000 | 1.0000 | -0.0000 | 0.7050 | -0.7500 | 1.0000 | 50 |

Face counts are the source's (many faces are split in halves); they are for information only.

**Assembly totals** (7 solids, overlaps counted twice): V 3.78615 in³ (62043.82 mm³), A 53.6831 in²
(34634.18 mm²), CoM (0.0000, 1.3106, 0.0172), bbox X −1.000 … 1.000, Y 0 … 4.8156, Z −0.750 … 1.000
(2.000 × 4.8156 × 1.750).

## 7. Overlaps that are part of the source (keep them)

| Pair | Common volume mm³ | Why |
|---|---|---|
| P01-a / P01-b | 3229.87 | the same rod in two positions |
| P02 / P01-b | 3212.36 | extended piston occupies the sleeve's lower wall region |
| P04 / P02 | 370.84 | unmodelled thread (Ø1.000 sleeve in Ø0.9459 bore) |
| P05 / P02 | 213.25 | unmodelled thread |

All other pairs touch or are apart (zero common volume).

## 8. Undetermined

- Exact run-in / run-out shape of the port thread groove (start near z 0.759); the source's thread faces are free-form
  approximations of the helix.
- Materials (product data: aluminium body, steel rod) are not geometry and are not checked.
