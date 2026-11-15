# P23 spec verification (forged dual-connect lifting shackle with flush pins)

Original: `kaynak.json` (6 solids, flat, no assembly tree, identity frame; STEP written in inch, geometry dimensioned in
round millimetres, so the spec is in **mm**; STEP order P02, P01, H2, H1-a, H1-b, P03). 17 empty micro shells (each
about 0.0001 mm, 102 zero-area faces) inside P03 are an artefact of the file; `olc_cekirdek.load_step` drops them
(`bos_kabuk_atilan 17`), the target face count of P03 is therefore 8. Scripts: `_gizli/is/` (s00 discovery, s01 face
dump, `dump_b1.txt`, s03 interference, r_govde.py text rebuild of P01, fkontrol.py per-face check, kesit.py /
blend_kesit.py sections, s05 hedef, s06 hidden lists, s07 recipe self-check, s08 this table).

## Target table (spec section 7) measured back against the original
| body | dV % | dA % | dCoM mm | dbbox max mm | faces spec / master |
|---|---|---|---|---|---|
| P01 | -0.0000 | -0.0000 | 0.0001 | 0.0000 | 182 / 182 |
| P02 | +0.0000 | -0.0000 | 0.0000 | 0.0000 | 24 / 24 |
| P03 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 8 / 8 |
| H1-a | +0.0001 | +0.0000 | 0.0001 | 0.0000 | 26 / 26 |
| H1-b | +0.0001 | +0.0000 | 0.0001 | 0.0000 | 26 / 26 |
| H2 | +0.0000 | -0.0000 | 0.0000 | 0.0000 | 26 / 26 |

Largest: dV 0.0001 % (3-decimal rounding of the spring pins), dCoM 0.0001 mm, dbbox 0.0000 mm. Bodies 6 / 6.
GProp volume vs fine-mesh integral: largest difference 0.026 % (spring pins), so all targets are GProp values.

## Interference set of the original (capped boolean worker, bbox pre-filter, all 7 touching pairs)
All 0 mm³ (pins in clearance holes: upper bore Ø20.0508 / pin Ø20, lower bore Ø16.127 / pin Ø16, spring-pin holes
Ø4.833784 / pins Ø4.782984; upper spring pins clear the P02 grooves, groove bottom r 7.1875 vs pin inner reach
r 7.2764). `girisimler` is empty.

## Independent rebuild check from the spec text (`r_govde.py`, build123d)
P01 rebuilt as written: side prism ∩ front prism, R3 on every edge, bores and holes (the R0.127 / R0.0254 hole-edge
rounds omitted). Volume 140659.25 vs 140650.84 (+0.006 %, = the omitted small rounds). Per-face check (`fkontrol.py`,
both directions, 36 samples per face): every analytic face of the original lies on the rebuild within 0.026 (0.026 =
the omitted R0.127 rounds); the R3 free-form blends follow a plain rolling ball within 0.01 except the blend at the top
of the lower slot (faces 125 / 127 / 129 / 132 / 134 / 136 of the original): 0.16 (whole face) and up to 0.24 in
sections at x = 7. The spec gives that blend as measured (y, z) sections at x = 0, 2, 4, 6, 7, 8 (`blend_kesit.py`).
P02 / P03 / spring pins checked by closed-form volume: P02 18035.5 (groove rectangle + half disc by Pappus, chamfer
frusta) vs 18035.30; P03 7651.6 vs 7651.46; spring pin 392.40 before the R0.0254 end rounds vs 392.375.

## olc self-check (original vs itself)
`is/olc_kendi/olcum.md`: **85.00 / 85** (geometry 40.00, completeness 10.00, assembly 10.00 (pose 4.00, assembly
3.00, interference 3.00), features 20.00 (66 / 66), drawing 5.00 (9 / 9)); 104 s, peak 1.13 GB, first run. Every body
IoU 1.000000, all deviations 0, orientation 0.0000 deg. The axisymmetric pins (P02, P03) lose no pose points: two of
their principal moments are equal, but the pin axis moment is distinct, so olc scores orientation on that axis alone
(unlike the P25 sphere, where all three moments are equal).

## Hidden lists
- ozellikler.json: 66 items over all 6 bodies + assembly; every recipe reproduces nom on the original (`s07_kontrol.py`,
  BAD 0). Five items are region-only (`olcum: null`): the R3 torus round at the upper clevis end, the R3 torus where the
  S-curve meets the inner lug face, and three free-form R3 blends (upper outer waist, top of the lower slot, lower slot
  corner). Free-form shape is scored only by `bolgesel_sapma` regions, never by face counts.
- resim_olculeri.json: 9 rows (every dimension printed on the catalogue drawing), all modelled and reproduced within
  0.005 in: 5.47 (139.0 mm = 5.4724), 1.57 (40.0 = 1.5748), 1.46 (37.0 = 1.4567), 1.09 (27.686 = 1.0900), 0.79 (Ø20 =
  0.7874), 1.93 (slot bottom z = -8.75 to pin bottom z = 40.25, 49.0 = 1.9291), 0.58 (lower slot top z = -27.4164 to
  lower pin top z = -42.25, 14.8336 = 0.5840), 0.63 (Ø16 = 0.6299), 0.61 (15.5448 = 0.6120).
- parametreler.json: overall length 139, upper jaw opening 27.686, lower jaw opening 15.5448, upper pin Ø20, lower pin
  Ø16 (mm).

## Source conflicts (K)
The product data lists inch values that differ from the 3D: top opening 1 1/16 (3D 1.090), top pin 25/32 (3D 0.787),
top inside length 1 15/16 (3D 1.929), bottom opening 9/16 (3D 0.612), bottom pin 5/8 (3D 0.630), bottom inside length
19/32 (3D 0.584). The drawing agrees with the 3D; the spec follows the 3D. Product data says "hammer-set dowel" pins;
the 3D has slotted spring pins (5 deg slot), described as modelled. The lower pin is enclosed by blind bores with no
outside access, as modelled.

## Undetermined (written as such in the spec)
Exact shape of the free-form R3 blend at the top of the lower slot (only sections given); exact form of the tiny blend
(about 0.025) where the upper spring-pin holes break into the upper bores. Nothing else.

## Tier
Index: "zor" (hard). Found: 6 bodies; the body is two intersecting tangent-arc prisms with R3 on every edge, 28
free-form blend faces (one of them not a plain rolling ball), a blind-bore / spring-pin retention scheme, grooved pin,
slotted spring pins with a 5 deg wedge. No threads, no gears. "zor" confirmed: the geometry is analytic and fully
measurable, but the many interacting R3 blends and the one non-standard blend make an exact rebuild demanding.
