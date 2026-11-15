# P34 spec verification

Source: `kaynak.json` (original STEP, declared INCH; geometry round in inch, spec unit = inch). Loaded with
`olc_cekirdek.load_step`: **7 solids, 0 empty shells dropped**, 0 free shells ignored. Frame unchanged.
`step_govde_sirasi` = P03, P04, P05, P01-a, P02, P01-b, P06.

## Bodies (what the source contains)
- Solid 0 = P03 barrel tube, 1 = P04 head cap, 2 = P05 jam nut (round, no flats), 4 = P02 stop sleeve
  (adjusting screw; thread not modelled), 6 = P06 base block (only body with free-form faces: the helical 1/8 pipe
  thread of the air port).
- **Solids 3 and 5 are the same piston rod twice** (identical V 11112.24 mm³, A 4060.69 mm², 9 faces), 3 retracted
  (Y 0.24–3.8156 in) and 5 extended (Y 1.24–4.8156 in): a pure +1.000 in Y translation = the maximum stroke. The
  drawing's 3.81 retracted / 4.81 extended lengths are exactly these two positions. Both are kept as P01-a / P01-b
  (equivalence group P01); the spec says so explicitly.

## s08 back-check: spec section 6 table vs original

| body | dV % | dA % | dCoM mm | dbbox max mm |
|---|---|---|---|---|
| P01-a | -0.0000 | -0.0000 | 0.0011 | 0.0000 |
| P01-b | -0.0000 | -0.0000 | 0.0011 | 0.0000 |
| P02 | +0.0000 | -0.0000 | 0.0007 | 0.0000 |
| P03 | -0.0001 | -0.0000 | 0.0012 | 0.0000 |
| P04 | -0.0001 | +0.0001 | 0.0010 | 0.0000 |
| P05 | -0.0002 | +0.0001 | 0.0000 | 0.0000 |
| P06 | -0.0000 | -0.0000 | 0.0002 | 0.0000 |

(dCoM ≤ 0.0012 mm is the 4-decimal inch rounding of the table.)

## Rebuild from the spec text (`is\r_govde.py`, all 7 bodies)

Compared with the original: V, A, CoM, bbox, and symmetric-difference volume via the capped BoolWorker.

| body | dV % | dA % | dCoM mm | dbbox mm | sym. diff mm³ |
|---|---|---|---|---|---|
| P03 | +0.0017 | +0.0001 | 0.0001 | 0 | 0.126 |
| P04 | 0 | 0 | 0 | 0 | 0 |
| P05 | 0 | 0 | 0 | 0 | 0 |
| P01-a | 0 | 0 | 0 | 0 | 0 |
| P02 | +0.0014 | +0.0023 | 0.00004 | 0 | 0.216 |
| P01-b | 0 | 0 | 0 | 0 | 0 |
| P06 (port thread omitted) | -0.402 | -1.62 | 0.083 | 0 | 54.73 |

- P03 / P02 residuals came from 4-decimal values in the rebuild script (groove 0.6158/0.7087, chamfer 0.0298);
  the spec now gives the exact values 0.61575 / 0.70875 / 0.02975 measured on the original.
- P06 was rebuilt with a plain crest-cone port (no helical thread): the 54.7 mm³ (0.40 %) residual is exactly the
  thread teeth; everything else of the block (outline, ears, blends, boss, holes, recess, bore, drill, step) matches
  (dbbox 0). The thread itself is specified (pitch, taper, depth, crest / root flats, phase, hand) from sections of
  the original; its run-in shape is undetermined.

## Mesh vs GProp volume
All bodies within 0.016 % (P01 0.0159 %, P02 0.0088 %, P06 -0.0019 %): GProp values are the targets.

## Interference set (capped BoolWorker after bbox pre-filter, `is\girisim.json`)
| pair | common mm³ |
|---|---|
| P01-a / P01-b | 3229.868 |
| P02 / P01-b | 3212.364 |
| P04 / P02 | 370.838 |
| P05 / P02 | 213.249 |

All other pairs 0 (touching: P03/P06, P03/P04, P01-a/P03, P01-a/P06, P01-a/P02, P04/P05, P01 rods in the P02 hole
with 0.001 radial clearance). All four pairs > 8 mm³ are in `hedef.json` `girisimler`. Causes: duplicate rod
position (2 pairs) and the unmodelled sleeve thread (2 pairs).

## Hidden lists
- `ozellikler.json`: 60 items (51 numeric, 9 region-only: chamfers, port thread box, drill bottom). `sayi` items:
  2 spanner holes, 3 separate Ø1.144 lands (`ayri_yuzler`), 2 mounting holes, 4 R0.25 blends.
- `resim_olculeri.json`: 10 rows = every printed dimension (1" bore, 0.2", 1 5/8", 5/16", 2", 11/16", 3.81", 4.81",
  0"–1" stroke, 1/8 NPT port; the last `modelde_var: false`, like P20's NPT notes).
- `parametreler.json`: bore Ø1.0, rod Ø0.3125, stroke 1.0, hole spacing 1.625, port pitch 1/27.
- **s07 self-check (tarifler.olc on the original): BAD 0** (all numeric items and drawing rows reproduce `nom`).

## Source conflicts (K)
- Drawing 11/16" base height vs model 0.705: fractions on this drawing are to the nearest 1/16 (0.705 → 11/16), tol
  set to 1/32; with 0.005 the original itself fails.
- Drawing 3.81" / 4.81" vs model 3.8156 / 4.8156: two-decimal truncation, tol 0.01 (as P20).
- The air port's drill ends at z 0.700 and never reaches the barrel bore (wall at r 0.593): the source has no air
  passage. Spec follows the 3D.
- The rod body appears twice (retracted + extended); kept, not an error of the spec.

## Undetermined
- Run-in / run-out shape of the port thread groove (starts near z 0.759 in; free-form faces in the source).

## Tier
"zor / hard" confirmed: 7 solids (6 distinct parts) of mostly simple turned geometry, but a helical tapered pipe
thread with free-form faces, a non-trivial base outline with tangent blends, a cross-axis port boss, a duplicated rod
and four source overlaps that a rebuild must reproduce on purpose.

## olc self-check result
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40, completeness 10, assembly 10, features 20.00, drawing 5.00; 102 s, 2026-11-12). Interference set reproduced (4 pairs).
