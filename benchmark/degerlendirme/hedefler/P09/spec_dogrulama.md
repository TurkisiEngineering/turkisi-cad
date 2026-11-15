# P9 · spec target table vs original STEP

Measured with OCP (GProp volume/area/CoM, optimal bbox) on the original STEP, in its own frame, no alignment.
Spec values are as printed in `A/spec.md` (inch to 4 decimals, mm3 / mm2 to 0.1).

| Body | ΔV % (mm3 col) | ΔA % (mm2 col) | ΔCoM mm | Δbbox mm (max of 6) |
|---|---|---|---|---|
| P01 | -0.000 | +0.000 | 0.0006 | 0.0011 |
| P02 | +0.000 | +0.001 | 0.0002 | 0.0011 |
| P03 | -0.000 | -0.001 | 0.0011 | 0.0011 |
| P04 | -0.000 | -0.000 | 0.0009 | 0.0011 |
| P05 | +0.001 | -0.001 | 0.0002 | 0.0011 |
| P06 | +0.002 | -0.001 | 0.0011 | 0.0011 |
| P07 | -0.000 | +0.001 | 0.0015 | 0.0011 |
| P08 | -0.006 | +0.006 | 0.0017 | 0.0011 |
| H1-a | +0.006 | -0.003 | 0.0015 | 0.0011 |
| H1-b | +0.006 | -0.003 | 0.0015 | 0.0011 |
| H1-c | +0.006 | -0.003 | 0.0015 | 0.0011 |
| H1-d | +0.006 | -0.003 | 0.0015 | 0.0011 |

Largest: |ΔV| 0.0064 (H1-a) %, |ΔA| 0.0065 (P08) %, ΔCoM 0.0017 (P08) mm, Δbbox 0.0011 (P02) mm.


## Undetermined items in the spec (section 7)

- Thread data of the carriage holes and base end holes beyond the 0.164 major diameter (no thread modelled).
- Lead screw thread standard beyond the modelled profile (pitch 0.05, major 0.25, root 0.18504).
- Bearing bush / thrust collar / retention of the lead screw in the end block (none modelled).
- Fixing of the nut in the carriage and its engagement with the screw (solid nut, overlaps the screw).
- Materials beyond aluminium base/carriage and stainless lead screw; pads are not separate bodies.
- Angular position of handwheel/handle in use (the supplied one is to be reproduced).

## Notes

- OCC volume vs fine-mesh volume: all bodies within 0.27 % (lead screw -0.17 %, handle -0.26 %, screws -0.22 %); OCC values used.
- Interference set (> 8 mm3): P03-P06 608.708 mm3, P06-P07 191.447 mm3. Below threshold: P01-P02 4.973 (pads), P01-H1-c/d 0.035 each, P07-P08 0.0001.
- Source artefact P02 F5 (+X wedge, max 0.0064 mm) is stated as optional in the spec.

## Spec text rebuilt independently (is/s07_spec_yeniden.py, build123d, from the spec.md profiles only)

| Body | ΔV % vs original | Δbbox mm |
|---|---|---|
| P01 base | +0.000 | 0.0001 |
| P02 carriage (with pads) | +0.001 | 0.0001 |
| P03 nut | +0.000 | 0.0001 |
| P04 end block | +0.000 | 0.0001 |
| P05 end plate | -0.000 | 0.0001 |
| P07 handwheel | -0.000 | 0.0001 |
| P08 handle | +0.005 | 0.0002 |
| H1-a, H1-c (via pose table) | +0.001 | 0.0001 |
| P06 lead screw, blank only | +23.58 (blank 3412.7 vs 2761.5 mm3) | 0.0001 |

P06: the 651 mm3 difference is the helical groove; analytic groove volume (trapezoid 0.000812 in2 x 2 pi x r_centroid
0.112 x 70 turns) is about 655 mm3, consistent. The helical groove itself was not rebuilt; its hand, phase, root/crest
radii and lands come from the original's root-land helix edges (is/s02_dis2.py) and are checked by recipes F47, F48,
F51 (region deviation 0 on the original).

Hidden lists verified on the original: ozellikler 63 / 63 pass (all region deviations 0.0, none NaN);
resim_olculeri 11 / 11 measurable rows pass, 7 rows modelde_var = false.
