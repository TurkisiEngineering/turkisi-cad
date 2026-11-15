# P27 spec verification (closed-body turnbuckle, clevis to clevis, 5/16-24 LH / RH)

Original: `kaynak.json` (11 solids, no empty shells, identity frame, inch STEP; STEP order P01, P02-a, P03-a, H1-a,
H2-a, P02-b, P03-b, H1-b, H2-b, P04-a, P04-b). Every -X body is the exact mirror image (x -> -x) of its +X partner
(`s03b_ayna.py`: max point distance 0.00000 in for all five pairs). Scripts in `_gizli/is/`: s01 structure, s02 face
dumps (`b/`), kesit / kesit6 sections, s03 interference + mesh volumes, s03b mirror check, s04_halka ring centreline,
s04c_flat thread flats, r_p27 / r_p27b text rebuilds, dbg_bar* T-bar blend analysis, dbg_mesh_tepe crest check,
s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table, s09 thread point classification.

## Target table (spec section 6) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01 | +0.0000 | -0.0000 | 0.0000 | 0.0000 |
| P02-a | -0.0002 | +0.0000 | 0.0003 | 0.0013 |
| P02-b | -0.0002 | +0.0000 | 0.0003 | 0.0013 |
| P03-a | +0.0002 | +0.0003 | 0.0012 | 0.0013 |
| P03-b | +0.0002 | +0.0003 | 0.0012 | 0.0013 |
| P04-a | +0.0000 | +0.0001 | **0.7213** | 0.0013 |
| P04-b | +0.0001 | +0.0001 | **0.7229** | 0.0013 |
| H1-a | +0.0030 | -0.0006 | 0.0011 | 0.0012 |
| H1-b | +0.0030 | -0.0006 | 0.0011 | 0.0012 |
| H2-a | +0.0002 | -0.0003 | 0.0015 | 0.0002 |
| H2-b | +0.0003 | -0.0004 | 0.0015 | 0.0002 |

Largest |dV| 0.003 % (ring, 5-decimal rounding), dbbox 0.0013 mm (4-decimal inch rounding).

**T-bolt CoM (lead to decide, source class K):** OCC GProp gives the T-bolts' CoM 0.0247 in (y) / 0.0141 in (z) off
the shank axis (0.72 mm); a fine-mesh integral gives (2.25773, 0.00001, 0.00003) in, and the bodies are symmetric
except for the helical thread. The spec table gives the mesh (true) CoM, hence the 0.72 mm in this table. GProp vs mesh
volume differs only 0.06 to 0.09 %, so olc.py uses OCC for these bodies: a correct rebuild whose kernel integrates its
own thread correctly may fail the dCoM (0.5 mm) and pose checks for P04-a / P04-b although its geometry is right.
Mesh vs GProp volumes, all bodies: largest 0.20 % (ring), so GProp volumes are the targets.

## Interference set of the original (capped boolean worker, 12 touching pairs)
All common volumes 0 except pin-ring 0.0022 mm3 (both sides): far below 8 mm3. `girisimler` is empty. Bolt shank /
body bore, T-bar / clevis bend and nut / bolt thread are zero-overlap contacts.

## Independent checks from the spec text
| body | check | result |
|---|---|---|
| P01 body | full rebuild (`r_p27.py`) | dV +0.0001 %, dbbox 0, max point distance 0.000000 in |
| P02 clevis | full rebuild | dV +0.0001 %, max 0.000000 in |
| P03 pin | full rebuild | dV -0.0001 %, max 0.000001 in |
| H1 ring | helix sweep R0.46875, pitch 5/96, wire 3/64, 697.5 deg, LH (`r_p27b.py ring`) | dV -0.017 %, max 0.000031 in |
| H2 nut | rebuild without thread | all non-thread faces exact (0.000000); dV -6.9 % = thread ridge |
| P04 T-bolt | rebuild without thread, R0.025 round at the bar ends | non-thread faces exact except the bar-end blends (0.007 in) |
| T-bar blends | analytic test (`dbg_bar6.py`): blend = chord of the R0.025 rolling ball | max 0.000013 in on all four blend faces (a true R0.025 round deviates 0.007, an equal-distance 0.025 chamfer 0.006) |
| threads | point classification (`s09_dis_dogrula.py`, 400 random points each) | nuts 0 / 380 and 0 / 381 mismatches; bolts 6 / 389 and 6 / 383, all near theta 260-270 deg or reported "inside" by the distance query: a classifier artefact on the B-spline crest seams. The mesh shows the crest at r 0.15625 in every 10 deg bin (`dbg_mesh_tepe.py`). |

Thread data from exact half-plane sections (`s04c_flat.py` on the nut, `kesit6.py` on the bolt): crest and root flats
P/8 = 0.00521, minor radius 0.12919, phase shift -P/4 per +90 deg (left-hand on +X), nut root centres = bolt crest
centres.

## Hidden lists
- ozellikler.json: 103 items (body 17, clevis 11 x 2, pin 8 x 2, ring 4 x 2, nut 7 x 2, T-bolt 12 x 2, assembly 2); all
  numbered items reproduce nom on the original (`s07_kontrol.py`, BAD 0); 28 are region-only (threads, rounds,
  chamfers, blends, ring sweep).
- resim_olculeri.json: 9 rows; measured: 8.625 retracted length (pin axis to pin axis), 5.125 body length, 0.313 clevis
  inside width (vertical), 0.313 pin diameter (horizontal), tol 0.0005 (model 0.3125 rounds to 0.313: passes at the
  boundary). Not measured (`modelde_var: false`): 12.375 extended length (pose not modelled), the two thread notes,
  maximum adjustment 3.75, 180 deg pivot. My reading of which 0.313 is which (vertical = clevis inside width,
  horizontal = pin diameter) follows the product data; both are 0.3125 in the model either way.
- parametreler.json: pin centre distance 8.625, body length 5.125, pitch 1/24, thread major diameter 0.3125, clevis
  inside width 0.3125.

## Undetermined (written as such in the spec)
Forging shapes / draft (not modelled), the body's thread (not modelled), thread clearances (model has none).

## Source conflicts (K)
- Drawing calls the end fittings forged; the model is a constant 0.0625 bent strap. Spec follows the 3D.
- Thread hands: drawing labels one end RH and the other LH; the model is LH at +X, RH at -X.
- GProp CoM of the threaded T-bolts (see above).

## Tier
Index: "hard". Found: 11 bodies in 6 kinds, two modelled helical threads (LH and RH) on bolts and nuts in phase, a
two-turn helical split ring, a chordal-blend T-head. "hard" confirmed (at the upper end of it).

## olc self-check result
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00, features 20.00, drawing 5.00; 2106 s). Note: original vs itself, so the T-bolt GProp CoM issue cancels here; it only bites a different rebuild.
