# P8 spec verification (pneumatic toggle clamp with forked arm, hold-down type)

Measured with OCP (GProp volume/area/CoM, optimal bbox) on the original STEP, in its own frame, no alignment.
Spec values are as printed in `A/spec.md` (inch to 4 decimals, mm3 / mm2 to 0.1).

| Body | ΔV % (mm3 col) | ΔA % (mm2 col) | ΔCoM mm | Δbbox mm (max of 6) |
|---|---|---|---|---|
| P01 | -0.000 | -0.000 | 0.0014 | 0.0000 |
| P02 | -0.000 | -0.000 | 0.0018 | 0.0005 |
| P03 | -0.000 | +0.000 | 0.0005 | 0.0011 |
| P04 | +0.001 | -0.001 | 0.0011 | 0.0000 |
| P05 | -0.000 | -0.000 | 0.0010 | 0.0000 |
| P06 | -0.000 | +0.001 | 0.0005 | 0.0010 |
| P07 | -0.000 | -0.000 | 0.0008 | 0.0006 |
| H1 | -0.001 | -0.001 | 0.0015 | 0.0004 |
| H2-a | +0.003 | +0.003 | 0.0009 | 0.0013 |
| H2-b | +0.003 | +0.003 | 0.0009 | 0.0013 |
| H3-a | +0.002 | +0.004 | 0.0000 | 0.0004 |
| H3-b | +0.002 | +0.004 | 0.0000 | 0.0004 |
| H4 | +0.009 | +0.003 | 0.0005 | 0.0009 |

Largest: |ΔV| 0.0095 (H4) %, |ΔA| 0.0037 (H3-a) %, ΔCoM 0.0018 (P02) mm, Δbbox 0.0013 (H2-a) mm.

## Rebuild from the spec numbers (independent check)

Every body was rebuilt in build123d from the numbers written in `A/spec.md` (script `_gizli/is/yap_govdeler.py`,
run by `s07_yeniden.py`) and compared with the original body (no alignment).

| Body | ΔV % | ΔCoM mm | Δbbox mm | IoU (OCC common) |
|---|---|---|---|---|
| P01 | -0.000 | 0.0001 | 0.0000 | boolean failed (coincident faces); ΔV 0 |
| P02 | +0.000 | 0.0001 | 0.0005 | 1.0000 |
| P03 | +0.006 | 0.0011 | 0.0011 | 0.99989 |
| P04 | -0.001 | 0.0002 | 0.0000 | 0.99999 |
| P05 | +0.001 | 0.0005 | 0.0000 | 0.99995 |
| P06 | +0.001 | 0.0022 | 0.0013 | 0.99996 |
| P07 | +0.008 | 0.0036 | 0.0004 | boolean failed; ΔV 0.008 % (rear-port threads replaced by their mean cone in the check) |
| H1 | +18.95 | 1.55 | 0.0000 | 0.840 (thread NOT modelled in the check; the missing groove volume 0.059 in3 equals the analytic groove volume of the specified 3/8-16 profile, 0.060 in3) |
| H2-a / H2-b | +0.003 | 0.0001 | 0.0013 | boolean failed; ΔV 0.003 % |
| H3-a / H3-b | +0.029 | 0.0000 | 0.0000 | 0.99971 |
| H4 | -0.026 | 0.0010 | 0.0006 | 0.99912 |

## Undetermined items (as listed in spec §7)

- Thread phase of the 45-degree rear port of P07; phase of the top rear port approximate (+/-0.002 in).
- Thread start / run-out shape of H1 at the head and at the end chamfer (free-form in the source).
- Arm-to-link pin, piston, seals, bore, air passages: not in the source.
- Open pose and kinematic limits (only "arm opening angle 95 deg" is stated).
- Materials and finishes.
- Not verified by rebuild: the helical threads themselves (H1, P07 rear ports); their parameters come from point sampling
  of the source surfaces (pitch fit 0.0625 / 0.03695 in, profile from radius-vs-phase bins).
