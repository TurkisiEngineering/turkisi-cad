# Design specification: hysteresis clutch for torque limiting on a through shaft

## 1. Units, frame, deliverable

- **Units: inch.** Every length below is in inch, every angle in degrees. (The source model is inch-based: the outer
  diameters, the length, the bore and the bolt circle are round in inch; the screw threads are metric M5 × 0.8 and are
  given here in inch too: 5 mm = 0.19685, 0.8 mm = 0.031496.) Your STEP may be written in any unit, at true size.
- **Global frame (use it exactly, do not re-centre or rotate anything):**
  - **Z axis = the common rotation axis** of the whole product (the Ø0.375 shaft bore). Almost every body is a body of
    revolution about Z.
  - The assembly spans **Z = -1.26 … +1.26** (overall length 2.52). The shaft hub collar end is at Z = +1.26, the bottom end
    cap face at Z = -1.26.
  - **Angles θ** are measured in the XY plane from +X towards +Y. The three M5 mounting holes at both ends lie at θ = 0, 120,
    240 on a Ø2.375 bolt circle. The flat of the knurled ring faces +X.
- **Deliverable:** one STEP file with **20 separate solids** (one solid per body in section 3, not fused). Body names are
  for reference; the grader matches bodies by shape and position.
- The source has no empty shells (0 dropped). All bodies are closed solids. Bodies touch face-to-face; no two bodies of the
  source overlap (all pairwise common volumes are 0, see section 7).

## 2. Product

A noncontact magnetic torque limiter (hysteresis type) for a Ø3/8 shaft: a short drum, Ø3.23 body with a knurled
adjusting ring (Ø3.31) at one end and a shaft hub with two M5 set screws sticking out of the other end. Turning the
knurled ring sets the slip torque; the ring is then locked with a set screw. Product data (context only, not modelled):
torque range about 0.5 to 10.6 in·lbf, max 220 rpm, works in both directions, M5 × 0.8 mounting holes.

Source simplifications (keep them):
- No magnets are modelled as separate magnetic parts; the inner rings and the drum are plain solids (which of them carry the
  magnets is not stated in the source).
- The four socket screws on the bottom cap (H3) and the two button screws in the knurled ring (H4) are **heads only**: no
  shank is modelled and there is no hole under them.
- The M5 threads ARE modelled (helical) in the 6 tapped mounting holes (P02, P03) and on the two set screws (H5). The two
  radial holes in the shaft hub (P07) that hold the set screws are plain Ø0.19685 (no thread).
- The set screws do not reach the shaft bore (they end on a Ø0.59 cylinder inside the hub).

## 3. Part list (20 solids)

| Name | Count | Kind | Description |
|---|---|---|---|
| P01 | 1 | custom | Housing ring: thick ring Ø3.23 / Ø2.035, 3 blind pin holes in the bottom face |
| P02 | 1 | custom | Bottom end cap: Ø3.23 plate with 3 integral pins, 3 tapped M5 holes, 4 screw counterbores |
| P03 | 1 | custom | Top end cap: Ø2.71 stepped ring, 3 tapped M5 holes in the top face |
| P04 | 1 | custom | Slotted drum: tube Ø2.035 / Ø1.48, counterbored ends with 9 radial slits each |
| P05 | 1 | custom | Inner ring Ø1.48 / Ø1.12, rounded edges |
| P06 | 1 | custom | Inner sleeve Ø1.12 / Ø0.59, chamfered edges |
| P07 | 1 | custom | Shaft hub: Ø0.375 bore through, Ø1.06 collar with 2 radial Ø5 mm holes |
| P08 | 1 | custom | Outer ring Ø3.01 / Ø2.71 |
| P09 | 1 | custom | Knurled adjusting ring Ø3.31 / Ø3.01: 150 straight knurl grooves, a flat with a V index mark, 2 spot faces |
| H1 | 2 (H1-a, H1-b) | hardware | Internal retaining ring with lugs (for a Ø2.035 bore), identical |
| H2 | 1 | hardware | External retaining ring with lugs |
| H3 | 4 (H3-a … H3-d) | hardware | Socket screw head (head only), identical |
| H4 | 2 (H4-a, H4-b) | hardware | Button screw head (head only), identical |
| H5 | 2 (H5-a, H5-b) | hardware | M5 × 0.8 socket set screw, flat point, 0.235 long, identical |

Equivalence groups: H1-a = H1-b, H3-a…d, H4-a = H4-b, H5-a = H5-b (same shape, different placement). Everything else is
unique.

## 4. Body geometry

"Half-section" = a closed profile in the (r, Z) plane (r = distance from the Z axis) that is revolved 360° about Z.
Vertices are listed in order; "R" after a corner = that corner is rounded with the given radius (tangent arc), "C" = a 45°
chamfer with the given leg length. Unless stated, edges are sharp.

### 4.1 P01 housing ring

Half-section (r, Z): (1.0175, -1.0121) → (1.6150, -1.0121) R0.02479 → (1.6150, 0.2390) → (1.0175, 0.2390) → close.
So: bore Ø2.035, outside Ø3.23, from Z -1.0121 (bottom face) to Z 0.239 (top face); only the outer bottom edge is rounded
R0.02479; all other edges sharp.

Pin holes: 3 blind holes **Ø0.22834**, axes parallel to Z on the Ø2.375 bolt circle (r = 1.1875) at θ = 0, 120, 240
(centres (1.1875, 0), (-0.59375, 1.02846), (-0.59375, -1.02846)); from the bottom face Z -1.0121 up to a flat bottom at
Z -0.6221 (depth 0.39). The pins of P02 fill them exactly.

### 4.2 P02 bottom end cap

Half-section of the plate (r, Z): (0.9250, -1.2600) → (1.6150, -1.2600) R0.02479 → (1.6150, -1.0121) R0.02479 →
(1.0175, -1.0121) → (1.0175, -1.1800) → (0.9250, -1.1800) → close.
So: Ø1.85 through bore, a Ø2.035 recess 0.1679 deep from the top face (floor at Z -1.18), outside Ø3.23, bottom face
Z -1.26, top face Z -1.0121, both outer edges R0.02479.

Pins (part of the same solid): 3 cylinders **Ø0.22834** standing on the top face Z -1.0121 up to Z -0.6221 (0.39 tall,
flat ends, sharp edges), axes at r 1.1875, θ = 0, 120, 240 (the same positions as the P01 holes).

Tapped holes: 3 × **M5 × 0.8** blind tapped holes on the same three axes, from the bottom face Z -1.26 up to a flat
bottom at **Z -0.87** (depth 0.39; they run through the plate into the pins). Mouth: 90° countersink, Ø0.20366 at the
bottom face. Thread: see 4.15 (internal). Thread phase: on the radially outer side of each hole (the side facing away from
the Z axis) the flats at the major diameter are centred at Z = -0.88795 - k·0.031496 (k = 0, 1, …). The holes at 120 and
240 are copies of the hole at 0 rotated about Z (the phase turns with them).

Screw-head counterbores: 4 × **Ø0.17442**, depth 0.09895 (from Z -1.26 to a flat floor at Z -1.16105), axes parallel to Z
at r 1.4535, θ = 0, 90, 180, 270; mouth chamfer 0.0174 × 45° (cone from Ø0.20932 at Z -1.26 to Ø0.17442 at Z -1.2426).
The heads H3 fill them.

### 4.3 P03 top end cap

Half-section (r, Z): (1.0175, 0.2390) → (1.3550, 0.2390) → (1.3550, 0.9145) C0.0255 → (1.3295, 0.9400) → (0.9250, 0.9400)
→ (0.9250, 0.8151) → (1.0175, 0.8151) → close.
So: outside Ø2.71 from Z 0.239 to the top face Z 0.94 with a 0.0255 × 45° top outer chamfer; bore Ø2.035 from the bottom
face up to a step at Z 0.8151, then Ø1.85 to the top.

Tapped holes: 3 × **M5 × 0.8** blind tapped holes, axes parallel to Z at r 1.1875, θ = 0, 120, 240, from the top face
Z 0.94 down to a flat bottom at **Z 0.55** (depth 0.39). Mouth: 90° countersink Ø0.20366 at the top face. Thread as 4.15;
phase: on the radially outer side of each hole the major-diameter flats are centred at Z = 0.93015 - k·0.031496; holes at
120 and 240 are rotated copies of the hole at 0.

### 4.4 P04 slotted drum

Outside Ø2.035 (r 1.0175), bore Ø1.48 (r 0.74), ends Z -1.095 and Z +0.7301. Both ends have the same counterbore; the
part is symmetric about the plane Z = -0.18245.

Half-section, top end (r, Z), from the bore up: (0.7400, 0.6616) → arc R0.01958 (centre (0.75958, 0.6616)) to
(0.75958, 0.68115) → floor (0.85917, 0.68115) → concave arc R0.01958 (centre (0.85917, 0.7007)) to (0.87875, 0.7007) →
wall (0.87875, 0.7105) → arc R0.01958 (centre (0.89833, 0.7105)) to (0.89833, 0.7301) → end face to (1.0175, 0.7301) →
outside (1.0175, -1.0950) → bottom end (mirror image about Z -0.18245: end face Z -1.095 from r 1.0175 to 0.89833, arc to
the counterbore wall r 0.87875 between Z -1.0754 and -1.0656, concave arc to the floor Z -1.04605 from r 0.85917 to 0.75958,
arc to the bore at Z -1.0265) → bore r 0.74 back to Z 0.6616.
So each end has a counterbore Ø1.7575 × 0.04895 deep with all three of its edges R0.01958; the outer edges are sharp.

Radial slits: at each end **9 slits, width 0.010**, through the whole wall (r 0.74 → 1.0175), from the end face
(top: Z 0.7301 down to a flat floor at Z 0.63115; bottom: Z -1.095 up to Z -0.99605; depth 0.09895). The slit mid-planes contain the Z axis
at θ = 10 + 40·k (10, 50, 90, 130, 170, 210, 250, 290, 330); the slit faces are the two planes parallel to that mid-plane
at ±0.005. Top and bottom slits are at the same angles.

### 4.5 P05 inner ring

Half-section: rectangle r 0.56 … 0.74, Z -1.0821 … 0.7172, all four corners **R0.0148**.

### 4.6 P06 inner sleeve

Half-section: rectangle r 0.295 … 0.56, Z -1.0821 … 0.7172, all four corners chamfered **0.01 × 45°**.

### 4.7 P07 shaft hub

Half-section (r, Z): (0.1875, -1.1000) → (0.2655, -1.1000) → (0.2950, -1.0705) → (0.2950, 0.8100) → (0.5300, 0.8100) →
(0.5300, 1.2388) → (0.5088, 1.2600) → (0.2087, 1.2600) → (0.1875, 1.2388) → close.
So: through bore **Ø0.375**; spigot Ø0.59 from Z -1.1 to the collar shoulder at Z 0.81 with a 0.0295 × 45° chamfer at the
bottom; collar Ø1.06 from Z 0.81 to the end face Z 1.26 with a 0.0212 × 45° chamfer on the outer edge and on the bore edge
of the end face. Bottom bore edge sharp.

Radial holes: 2 × plain **Ø0.19685** (5 mm), axis at Z 1.035, one along +X (axis = the line Y 0, Z 1.035), one along +Y
(X 0, Z 1.035); each runs from the collar surface (r 0.53) inwards and ends on the **Ø0.59 cylinder** (r 0.295, coaxial
with Z) — the hole bottom is that curved surface, not a flat. Each mouth has a small flare to Ø0.2228 at the collar
surface (freeform in the source).

### 4.8 P08 outer ring

Half-section: rectangle r 1.355 … 1.505, Z 0.239 … 0.889; the two top corners rounded **R0.015**; bottom corners sharp.

### 4.9 P09 knurled adjusting ring

Base half-section (r, Z): (1.5050, 0.2390) → (1.6175, 0.2390) → (1.6550, 0.2765) → (1.6550, 0.8515) → (1.6175, 0.8890) →
(1.5200, 0.8890) → arc R0.015 (centre (1.52, 0.874)) to (1.5050, 0.8740) → close.
So: bore Ø3.01, knurl crest Ø3.31, Z 0.239 … 0.889, 0.0375 × 45° chamfers on both outer edges, inner top edge R0.015.

Then, in this order:
1. **Straight knurl: 150 grooves** parallel to Z over the full length (they run out through the end chamfers). Groove
   mid-planes contain the Z axis at θ = 1.2 + 2.4·k (k = 0 … 149). Groove cross-section (in any Z plane, symmetric about
   its mid-line): root = arc **R0.01488** whose centre lies on the mid-line at r 1.6558 (root bottom at r 1.64092); two
   straight flanks tangent to the root arc, each at **37.5°** to the mid-line (75° included), running out to the crest
   circle r 1.655. Crest lands between grooves are 1.152° wide.
2. **Flat** on the +X side: plane X = 1.615 (cuts the knurl between about θ = ±12.6). In its middle a **90° V-groove**
   (index mark) parallel to Z: its two faces are the planes through the line (X 1.5963, Y 0) at ±45° to the flat, i.e. the
   mark is 0.0374 wide and 0.0187 deep. Flat and mark run the full ring length.
3. **2 spot faces** at θ = 90 and 270: Ø0.455 cylindrical pockets, axis along Y at X 0, Z 0.564, open to the outside, flat
   floor at |Y| = 1.5425. The heads H4 sit on these floors.

### 4.10 H1 internal retaining ring (H1-a, H1-b)

Flat ring, thickness 0.085, outline in the XY plane (closed, symmetric about X = 0), lugs towards -Y:
- outer arc R0.99715, centre (0, 0.0204), from (0.2758, -0.9379) the long way round through +Y to (-0.2758, -0.9379);
- lug end (-X side): arc R0.04736, centre (-0.2627, -0.8924), from (-0.2758, -0.9379) through (-0.2627, -0.9398) to
  (-0.2166, -0.9034); line to (-0.1934, -0.8065); arc R0.09473, centre (-0.2855, -0.7844), to (-0.3307, -0.7012); arc
  R0.09473, centre (-0.3760, -0.6179), to (-0.4252, -0.6989);
- inner arc R0.81807, centre (0, 0), from (-0.4252, -0.6989) the long way round through +Y to (0.4252, -0.6989);
- the +X lug is the mirror image (X → -X) of the -X lug.
- 2 lug holes Ø0.09972 (R0.04986) at (±0.2855, -0.7844).

Placement: H1-a between Z -1.18 and -1.095 (in the P02 recess, against the bottom end of P04); H1-b between Z 0.7301 and
0.8151 (in the P03 bore, on the top end of P04). Same XY outline for both.

### 4.11 H2 external retaining ring

Flat ring, Z 0.7172 … 0.81 (thickness 0.0928), outline symmetric about X = 0, lugs towards -Y:
- outer arc R0.55281, centre (0, 0.0272), from (0.3018, -0.4360) the long way round through +Y to (-0.3018, -0.4360);
- -X lug: concave arc R0.1475, centre (-0.3823, -0.5596), to (-0.2444, -0.5072); line to (-0.2163, -0.5812); arc
  R0.04917, centre (-0.1703, -0.5637), to (-0.1703, -0.6129); line to (-0.0753, -0.6129); line to (-0.0587, -0.4781); arc
  R0.0295, centre (-0.0880, -0.4745), through (-0.0585, -0.4745) to (-0.0826, -0.4455);
- inner arc R0.45313, centre (0, 0), from (-0.0826, -0.4455) the long way round through +Y to (0.0826, -0.4455);
- +X lug = mirror image of the -X lug.
- 2 lug holes Ø0.0734 (R0.0367) at (±0.1561, -0.5445).

### 4.12 H3 socket screw head (head only; 4 copies)

Described for H3-a (axis parallel to Z through (0, 1.4535)): cylinder **Ø0.17442** from Z -1.2600 to Z -1.16105 (0.09895
long), flat top; the lower (exposed) edge chamfered 0.0174 × 45° (Ø0.13954 at Z -1.26). Hex socket in the lower face:
across flats **0.1046**, the six corners rounded R0.01047, depth 0.05442 (flat floor at Z -1.20558); two flats are
perpendicular to X (i.e. parallel to the radial direction of the head).

| Name | Axis (X, Y) | Socket |
|---|---|---|
| H3-a | (0, 1.4535) | flats at X = ±0.0523 |
| H3-b | (-1.4535, 0) | H3-a rotated 90° about Z |
| H3-c | (0, -1.4535) | H3-a rotated 180° about Z |
| H3-d | (1.4535, 0) | H3-a rotated 270° about Z |

### 4.13 H4 button screw head (head only; 2 copies)

Described for H4-a: axis along Y at (X 0, Z 0.564); let h = Y - 1.5425 (height above the spot-face floor) and ρ = radial
distance from the axis. Half-section (ρ, h): (0, 0) → (0.20827, 0) → arc R0.01273 (centre (0.20827, 0.01273)) to
(0.221, 0.01273) → (0.221, 0.01463) → arc R0.01273 (centre (0.20827, 0.01463)) to the dome → dome = arc R0.18785 with
centre (0.06797, -0.0902) → arc R0.01273 (centre (0.10475, 0.081)) to the top flat (0.10475, 0.0938) → (0, 0.0938).
So: Ø0.442 button head, 0.0938 tall, flat top Ø0.2095.
Hex socket in the top: across flats **0.1592** (two flats perpendicular to X, at X = ±0.0796), corners R0.01273, depth
0.0625 (floor at h 0.0313); the socket mouth edge and the floor edge are rounded R0.00509.
H4-b = H4-a rotated 180° about Z (axis at Y -1.5425 … -1.6363, X 0, Z 0.564).

### 4.14 H5 set screw M5 × 0.8 × 0.235 (2 copies)

Described for H5-a: axis along Y at (X 0, Z 1.035), from Y 0.295 (inner end, flat point) to Y 0.53 (outer end).
- Body: external thread M5 × 0.8 (4.15) over the length.
- Inner end: flat point Ø0.1496 at Y 0.295, 45° chamfer up to the thread.
- Outer end: face Ø0.1496 at Y 0.53 with a 45° chamfer to the thread; hex socket across flats **0.0984**, depth 0.0705
  (floor at Y 0.4595), two flats perpendicular to X (X = ±0.0492), socket mouth with a 120° countersink Ø0.1137 at the end
  face.
- Thread phase: on the +X side of H5-a the crest flats (major diameter) are centred at Y = 0.3206 + k·0.031496.
- H5-b = H5-a rotated -90° about Z (axis along X at Y 0, Z 1.035, from X 0.295 to 0.53).
Both screws sit in the plain radial holes of P07.

### 4.15 Thread form (all M5 × 0.8, right hand, modelled helically)

ISO-like 60° profile, pitch 0.031496: major diameter **0.19685**, minor diameter **0.1560**, flats 0.0039 wide at both the
major and the minor diameter, straight flanks at 30° to the radial direction. Internal threads (P02, P03): the major
diameter is the root in the material, the minor diameter is the crest. External thread (H5): crest at the major diameter,
root at the minor diameter.

## 5. Assembly relations (all already given by the coordinates above)
- Stack along Z: P02 (Z -1.26 … -1.0121) under P01 (-1.0121 … 0.239); P08 and P09 and P03 start at Z 0.239.
- P01 bore Ø2.035 = P04 outside; P04 bore Ø1.48 = P05 outside; P05 bore Ø1.12 = P06 outside; P06 bore Ø0.59 = P07 spigot.
- P08 fits on P03 (Ø2.71); P09 fits on P08 (Ø3.01).
- P02 pins fill the P01 pin holes; H3 heads fill the P02 counterbores; H4 heads sit on the P09 spot faces; H5 screws sit
  in the P07 radial holes.

## 6. Target table (original STEP, per body)

V = volume, A = surface area, CoM = centre of mass, bbox in inch; faces = source face count (information only).

| Body | Description | V in³ | V mm³ | A in² | A mm² | CoM X | CoM Y | CoM Z | Xmin | Xmax | Ymin | Ymax | Zmin | Zmax | faces |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | Housing ring | 6.13303 | 100502.28 | 31.3078 | 20198.56 | -0.0000 | 0.0000 | -0.3831 | -1.6150 | 1.6150 | -1.6150 | 1.6150 | -1.0121 | 0.2390 | 17 |
| P02 | Bottom end cap | 1.27654 | 20918.67 | 16.9918 | 10962.41 | 0.0000 | 0.0000 | -1.1280 | -1.6150 | 1.6150 | -1.6150 | 1.6150 | -1.2600 | -0.6221 | 141 |
| P03 | Top end cap | 1.80224 | 29533.38 | 17.5162 | 11300.74 | 0.0000 | -0.0000 | 0.5977 | -1.3550 | 1.3550 | -1.3550 | 1.3550 | 0.2390 | 0.9400 | 109 |
| P04 | Slotted drum | 2.72281 | 44618.84 | 23.7503 | 15322.73 | -0.0000 | -0.0000 | -0.1824 | -1.0175 | 1.0175 | -1.0175 | 1.0175 | -1.0950 | 0.7301 | 171 |
| P05 | Inner ring | 1.32196 | 21662.98 | 16.0634 | 10363.48 | 0.0000 | 0.0000 | -0.1825 | -0.7400 | 0.7400 | -0.7400 | 0.7400 | -1.0821 | 0.7172 | 14 |
| P06 | Inner sleeve | 1.28022 | 20978.98 | 11.0267 | 7114.01 | 0.0000 | 0.0000 | -0.1825 | -0.5600 | 0.5600 | -0.5600 | 0.5600 | -1.0821 | 0.7172 | 14 |
| P07 | Shaft hub | 0.64233 | 10525.90 | 9.5596 | 6167.46 | -0.0046 | -0.0046 | 0.4655 | -0.5300 | 0.5300 | -0.5300 | 0.5300 | -1.1000 | 1.2600 | 25 |
| P08 | Outer ring | 0.87517 | 14341.39 | 14.2602 | 9200.13 | 0.0000 | 0.0000 | 0.5637 | -1.5050 | 1.5050 | -1.5050 | 1.5050 | 0.2390 | 0.8890 | 10 |
| P09 | Knurled adjusting ring | 0.87926 | 14408.56 | 16.5018 | 10646.28 | -0.0186 | 0.0000 | 0.5638 | -1.6550 | 1.6150 | -1.6549 | 1.6549 | 0.2390 | 0.8890 | 661 |
| H1-a | Internal retaining ring, bottom | 0.08160 | 1337.20 | 2.9031 | 1872.97 | 0.0000 | 0.1250 | -1.1375 | -0.9972 | 0.9972 | -0.9398 | 1.0175 | -1.1800 | -1.0950 | 20 |
| H1-b | Internal retaining ring, top | 0.08160 | 1337.20 | 2.9031 | 1872.97 | 0.0000 | 0.1250 | 0.7726 | -0.9972 | 0.9972 | -0.9398 | 1.0175 | 0.7301 | 0.8151 | 20 |
| H2 | External retaining ring | 0.03095 | 507.17 | 1.3158 | 848.88 | 0.0000 | 0.0461 | 0.7636 | -0.5528 | 0.5528 | -0.6129 | 0.5800 | 0.7172 | 0.8100 | 26 |
| H3-a | Socket screw head, +Y | 0.00177 | 29.04 | 0.1154 | 74.44 | -0.0000 | 1.4535 | -1.2022 | -0.0872 | 0.0872 | 1.3663 | 1.5407 | -1.2600 | -1.1610 | 20 |
| H3-b | Socket screw head, -X | 0.00177 | 29.04 | 0.1154 | 74.44 | -1.4535 | -0.0000 | -1.2022 | -1.5407 | -1.3663 | -0.0872 | 0.0872 | -1.2600 | -1.1611 | 20 |
| H3-c | Socket screw head, -Y | 0.00177 | 29.04 | 0.1154 | 74.44 | 0.0000 | -1.4535 | -1.2022 | -0.0872 | 0.0872 | -1.5407 | -1.3663 | -1.2600 | -1.1611 | 20 |
| H3-d | Socket screw head, +X | 0.00177 | 29.04 | 0.1154 | 74.44 | 1.4535 | 0.0000 | -1.2022 | 1.3663 | 1.5407 | -0.0872 | 0.0872 | -1.2600 | -1.1611 | 20 |
| H4-a | Button screw head, +Y | 0.00927 | 151.92 | 0.3868 | 249.58 | 0.0000 | 1.5778 | 0.5640 | -0.2210 | 0.2210 | 1.5425 | 1.6363 | 0.3430 | 0.7850 | 52 |
| H4-b | Button screw head, -Y | 0.00927 | 151.92 | 0.3868 | 249.58 | -0.0000 | -1.5778 | 0.5640 | -0.2210 | 0.2210 | -1.6363 | -1.5425 | 0.3430 | 0.7850 | 52 |
| H5-a | Set screw M5, +Y | 0.00506 | 82.89 | 0.2793 | 180.21 | 0.0002 | 0.4028 | 1.0352 | -0.0984 | 0.0984 | 0.2950 | 0.5300 | 0.9366 | 1.1334 | 36 |
| H5-b | Set screw M5, +X | 0.00506 | 82.89 | 0.2793 | 180.21 | 0.4028 | -0.0002 | 1.0352 | 0.2950 | 0.5300 | -0.0984 | 0.0984 | 0.9366 | 1.1334 | 36 |

**Assembly** (20 solids): V = 17.16344 in³ (281258.36 mm³), A = 165.8936 in² (107027.93 mm²), CoM = (-0.0010, 0.0012,
-0.1392), bbox X -1.655 … 1.615, Y -1.6549 … 1.6549, Z -1.26 … 1.26 (3.27 × 3.3098 × 2.52).

## 7. Checks you can make
- Overall length 2.52 (Z); knurl crest Ø3.31; body Ø3.23 (P01, P02); bore Ø0.375; mounting bolt circle Ø2.375 at both ends.
- No two bodies overlap (the source has zero common volume for every pair; the set screws only touch the hub hole walls).
- P04, P05, P06 are symmetric about Z = -0.18245; P04 has 18 slits in total.

## 8. Undetermined / not in the source
- Which rings are permanent magnets, their pole count and magnetisation: not modelled.
- Screw shanks under the H3 and H4 heads, and any holes for them: not in the source; do not add.
- Thread run-out at the ends of the helical threads: the source simply cuts the helix at the hole bottom / screw ends; only
  the phase given in 4.2, 4.3 and 4.14 is defined.
- The exact shape of the small flare at the mouths of the P07 radial holes (freeform in the source).
- Materials and finishes: not part of the geometry.
