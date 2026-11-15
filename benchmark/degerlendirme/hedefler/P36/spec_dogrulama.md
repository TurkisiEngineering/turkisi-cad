# P36 spec verification (lifting jack with power screw, swivel saddle and carry handle)

Original: `kaynak.json` (6 solids, inch STEP, identity frame; STEP order P02 screw, P01 base, P03 saddle, H1-a, H1-b,
H1-c). `olc_cekirdek.load_step` drops **0** empty bodies / shells. Scripts in `_gizli/is/`: s01 structure, s02 face
dumps (`b/dump_*.txt`), kesit.py sections (`b/k*.txt`), s04_dis.py (crest flats per azimuth), s04b_setscrew.py (set
screw / hole frames), s03 interference (`girisim.json`), r_govde.py + r_dis.py text rebuilds (`rb_*.step`), s05 hedef,
s06 hidden lists, s07 recipe self-check (`b/s07.log`), s08 this table, s09 thread point classification.

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | -0.0000 | -0.0000 | 0.0006 | 0.0007 |
| P02 | -0.0000 | +0.0000 | 0.0011 | 0.0000 |
| P03 | -0.0000 | -0.0000 | 0.0010 | 0.0000 |
| H1-a | -0.0010 | +0.0021 | 0.0016 | 0.0010 |
| H1-b | -0.0010 | +0.0021 | 0.0012 | 0.0012 |
| H1-c | -0.0010 | +0.0021 | 0.0012 | 0.0012 |

Largest: |dV| 0.001 % (5-decimal in3 rounding of the set screws), dCoM 0.0016 mm, dbbox 0.0012 mm (4-decimal inch
rounding; exact extremes are printed in the spec). Bodies 6 / 6.

**GProp vs fine mesh volume:** screw -0.197 % (GProp 406304.77, mesh 407107.48 mm3; B-spline thread flanks), base
-0.0007 %, saddle +0.002 %, set screws +0.005 %. All below 0.5 %: GProp values are the targets.

## Interference set of the original (capped boolean worker, bbox pre-filter, 8 touching pairs)
- **P02 screw / P03 saddle: 1482.79 mm3** (0.09048 in3) -> `girisimler`. Cause: the saddle bottom opening (r 0.414578 at
  y 14.3) is smaller than the screw neck (r 0.65); the overlap is the ring between the neck cylinder and the socket
  sphere for y 14.3 to 14.550834 (analytic pi * 0.028802 = 0.090484 in3, agrees). Written into the spec as is.
- All other pairs 0: screw / base (crests on the plain bore, head on the top face), screw / set screws (tips on the
  ball sphere), saddle / set screws (equal hole and screw diameter). Base / saddle and base / set screws: bboxes apart.

## Independent checks from the spec text
| body | check | result |
|---|---|---|
| P03 saddle | full rebuild from the spec (revolve, 36 studs, 3 holes; `r_govde.py`) | dV +0.0000 %, dA +0.0000 %, bbox equal, every rebuilt face on the original (max 0.0000 in) |
| P01 base | rebuild without the R0.06 handle junction blends and the R0.05625 window edge rounds | dV +0.002 %, dA +0.08 %, bbox equal; 60 of 63 faces exact; residuals only where the omitted rounds sit (window wall 0.016 in, bead ends at the junctions 0.011 in) |
| P02 screw | rebuild without the thread groove and the hole-mouth edge breaks | every non-thread face exact; cross-hole walls 0.02 in near the mouths (edge breaks omitted); rebuild - original = 60393.6 mm3, of which the groove computed from the spec profile is 59368 mm3 and the edge breaks about 107 mm3; the remaining 0.25 % equals the GProp-vs-mesh shortfall of the original (against the mesh volume the residual is 116 mm3, 0.03 %) |
| P02 thread | 400 random points between root and crest radius (all azimuths, y 0.6..11.25), classified against the original and predicted by the spec phase / profile formula (`s09_dis_dogrula.py`, 2 thou margin) | **0 / 400 mismatches** |
| P02 thread (solid) | helical sweep of the groove + boolean cut (`r_dis.py`) | the sweep is valid (6.84 in3) but the boolean with the 33-turn helix fails silently (removes 0.36 in3 only). **A full-helix boolean is slow / fragile here**; the point classification above is the proof used |
| H1 | from the dumps (`s04b_setscrew.py`): all three identical, axes through (0, 14.855184, 0), 10.000 deg down, az 90 / 210 / 330, hex flats at 49.702 deg + k 60 deg in the hole frame | recipes F52-F59 reproduce |

Thread data: crest flats from exact vertices (crest start at az 0 = 0.583333, az 90 = 0.5, az 270 = 0.666667, crest
0.13434 wide, flanks 0.166667 x 0.043103 = 14.5 deg, root 0.583333 wide 0.112787), phase advance -p/4 per +90 deg az
(right-hand about +Y).

## olc-style recipe self-check (s07_kontrol.py, tarifler.olc on the original)
**BAD 0.** 60 ozellikler items: 37 numbered items all reproduce nom (lengths within 1e-4 mm, counts exact); 23 are
region-only (`bolgesel_sapma`: flares, window, handle bead / rounds / junction blends, thread body and both run-outs,
cross-hole edge breaks, chamfers, ball, saddle profile, socket, set screw tip). Thread faces are counted nowhere
(B-spline in the source): thread items are boxes only. Stud count uses cone faces (36, sphere tips not counted).

## Hidden lists
- ozellikler.json: 60 items (base 23, screw 18, saddle 10, set screws 8, assembly 1).
- resim_olculeri.json: 6 rows. **2.88 saddle diameter** (2.88000) and **15.75 minimum height** (base floor to saddle top
  face, 15.75000) are measured. 25.5 max height, 9.75 max lift and 9 deg swivel are `modelde_var: false` (motion /
  extended pose). **6.25 base diameter: SOURCE CONFLICT** - the model is 6.1747 across the foot round (6.0497 across the
  flat underside); no feature of the model is 6.25, so the row is `modelde_var: false`, `olcum: null` with a note.
  **Lead to confirm** (alternative: a recipe on the base X extent with nom 6.25 would fail on the original itself).
- parametreler.json: thread pitch 1/3, thread major diameter 1.5, saddle diameter 2.88, base height 12.0, ball
  diameter 1.5.

## Undetermined (written as such in the spec)
Materials of screw, saddle and set screws (product data names only the iron body); exact form of the free-form edge
breaks at the turning-bar hole mouths and at the set screw tips; exact shape of the R0.06 handle junction blends; the
buried ends of the handle sweep (any end inside the wall gives the same solid).

## Source conflicts (K)
- Base diameter: drawing 6.25 and product data 6 1/4 vs model 6.1747 (spec follows the 3D).
- Minimum height 15.75 agrees with the saddle top face; the stud tops reach 15.8375 (assembly Y extent).
- The saddle overlaps the screw neck in the original (1482.79 mm3), kept.
- No nut thread in the base (plain bore r 0.75 on the crests).

## Tier
Index: "very-hard" (cok_zor). Found: 6 bodies (3 identical set screws), a modelled 33-turn 29 deg trapezoidal thread
with run-outs at both ends, a swept C-handle with a beaded cross-section and free-form junction blends, an elliptical
window, 36 studs, tilted socket set screws. **Very hard confirmed.**

## olc self-check result

Run 2026-11-12 18:49-19:26 (2228 s, peak 3.69 GB), original vs itself:
**§1-§5 = 84.03 / 85** (geometry 39.20/40, completeness 10, assembly 10, features 19.83/20, drawing 5/5).

Shortfall 0.97, all from **one sample on the original's helical thread B-spline of P02 (screw)**, not from the lists:
- The P02 boolean timed out (the 33-turn helix), so olc used the thin-shell IoU estimate (0.999998). Its mesh-boundary
  sampling put one point 0.5075 mm off the same surface ("mesh boundary won 1 sample, helix / spline: P02 1"). The P95
  for every body is 0.00000, and dV, dCoM and dbbox are all zero. This max costs 0.80 on "maks".
- F28 (thread upper run-out region, `bolgesel_sapma`) picks up that same 0.5075 mm sample, giving `yakin` instead of
  `tam` (-0.17). The region is right. The original measured against itself cannot reach ≤ 0.05 there with olc's
  helix sampling.
- Interference: original P02-P03 1482.79 mm³ is reproduced exactly. 59.5 / 60 feature items, 2 / 2 drawing rows.
Lists were left unchanged. The grader can treat F28 as `tam` for a rebuild that matches the thread definition.
