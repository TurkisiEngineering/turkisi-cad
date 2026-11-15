# P3 spec verification

Independent rebuild of the spec text (`is/s05_rebuild.py`, inches, outer solid + flange + bosses minus inner cavity,
scaled x25.4) compared with the master STEP by `is/cmp.py` (triangulation 0.005 mm, 20 000 samples per direction).

| Body | spec V mm3 | master V (mesh) | rebuild V (B-rep / mesh) | dV % | dCoM mm | dBbox mm | dev P95 / max mm |
|---|---|---|---|---|---|---|---|
| P01 Guard | 136628 | 136627.6 | 136562.9 / 136565.5 | -0.05 | 0.019 | 0.010 (Ymin, mesh) | 0.0012 / 0.51 |

- **Master B-rep volume is wrong:** OCC GProp reads 139956.3 mm3 (+2.4 %) and CoM x = -0.335 mm, because faces 82
  (inner crown) and 11/99 (top recess, cylinder origin 500 m away) integrate badly. Triangulated integration converges
  to 136628-136632 mm3 with CoM x = 0.000. Target table uses the mesh values; the grader must too (RUBRIK §1 note).
- The 0.51 mm maximum deviation is local, under the top boss near x = 0 (|x| < 0.13 in): the master's crown/side-wall
  rounds dip up to 0.02 in there (spec 3.7). Everywhere else max < 0.01 mm.
- Design relations found and written into the spec: all walls 4.000 deg draft; every inner plane = outer - 0.125;
  inner slope tangent to inner crown R1.8125 through (2.8125, -0.40625); hump legs tangent to the arch circles; bosses
  0.0875 high with R0.1 base rounds; recesses 0.125 below the boss tops.
- Feature recipes (33) reproduce on the master. On the rebuild 32/33 pass; F24 (count of R0.1 torus faces) fails
  because the test kernel's rolling-ball round on the low boss is freeform, not a torus; region check passes.
- C recipes: all 6 reproduce on the C rebuild (WT 0.145, inner width +0.25).
- Drawing: 5.625 inside length reproduces exactly (inner end walls at y = -0.40625; no recipe for drafted walls).
  1.5 inside width and 3.063 inside height have no face-pair counterpart (modelde_var false).
- Undetermined: catalogue inside width/height (above); reason for the +Z/-Z flange tab asymmetry; material.

## Hidden-list fix (2026-11-11, after olc.py calibration 2)
Backup of the previous lists: `is/lead_yedek_2026-11-11/`. Original STEP unchanged.
- F13: the 16 read by olc.py = 12 analytic R0.375 cylinders + 4 curved-edge R0.375 rounds written as B-spline (crown/side x2, hump arch x2; already F14 / F15). The item means the 12 planar-edge rounds: `sayi` now has `bolge` y < 14 mm (cylinder face centres y <= 9.6, free-form ones y >= 17.9). Original reads 12.
- F24: the boss base R0.1 round is written half torus, half B-spline on each slope boss (+ R0.1 B-spline corners on the flange and top boss), so any count is kernel-dependent (17 read). Changed to `bolgesel_sapma` on a box around both slope bosses (`kutu` x +/-50, y 20..47, |z| <= 16, minus |x| < 24, which also keeps the faulty top-recess area out). Self-deviation 0.0008 mm dense, 0 in olc.py.
- F18: the old region (0, 44.704, 7.112) sat on the faulty area: recess cylinder faces 11/99 (origin 500 m away) against inner blends 110/117 (radius 6.32 not 6.35), self-deviation 0.18-0.27 mm. Recess-diameter point and region moved to (7.144, 44.704, 0), the middle of face 99 (it used to lie on the 11/99 seam); self-deviation 0.
- Drawing 5.625 in: recipe added: `bbox_boyut` x of the mesh nodes in a 0.16 mm slab at y = -10.31875 mm, |z| < 16, |x| < 72 = the two sharp inner end-wall/inner-slope edges at x = +/-71.4375. Reads 5.62500 in. 1.5 and 3.063 stay `modelde_var: false` (re-checked: the drafted inner side walls are 1.5 apart only at y = -0.187 in, where there is no edge; no inner surface 3.063 in from the flange).
- olc.py original vs itself (`araclar/kalibrasyon/k2c_P3`): S1 47.19, S2 10, S4 20.00 (33/33), S5 5.00 (1/1), total 82.19 / 85. The S1 loss (max 4.69/7.5) is the file's own noise: two samples 0.06 / 0.095 mm at the top recess (x ~ +/-2.3, y 43-44, |z| ~ 7), where the trimming curves of faces 11/99/110/117 do not match their own mesh.
