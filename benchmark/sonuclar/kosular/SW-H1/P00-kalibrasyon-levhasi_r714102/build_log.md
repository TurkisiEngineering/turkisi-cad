# Build log — P01 Plate (calibration plate P0)

## Ne yaptım
- Araç: SolidWorks 2024, Python 3.13 + pywin32 COM (`build_p01.py`). MCP sunucusu kullanılmadı.
- Çerçeve: SolidWorks "Front Plane" = model XY düzlemi, normal +Z. Tüm çizimler Front Plane'de ya da ondan +Z yönünde
  `T` ofsetli `PL_TopZ10` düzleminde → çizim x,y = global X,Y; parça yerinde kuruldu, taşıma yok. Birim MMGS.
- Özellik ağacı (spec sırası):
  - `SK_PlateOutline` + `F1_PlateBlock`: merkez dikdörtgen 100×60, Z=0→10 ekstrüzyon.
  - `F2_CornerRounds`: 4 dikey köşe kenarına R3 fillet özelliği (kenarlar gövde topolojisinden |X|=50, |Y|=30, Z'ye paralel olarak seçildi).
  - `SK_CornerHoles` + `F3_CornerHoles`: 4 × Ø6 daire (±42, ±22), Through All Both kesim.
  - `PL_TopZ10`, `SK_Pocket` + `F4_CentralPocket`: Ø20 daire, Z=10'dan aşağı 4 mm kör kesim; düz taban, keskin kenarlar.
- Gövde adı `P01 Plate`; STEP'te `MANIFOLD_SOLID_BREP('P01 Plate')`, şema AUTOMOTIVE_DESIGN (AP214), birim mm.

## Nerede takıldım
- pywin32 geç bağlamada argümansız SW metodları (GetEquationMgr, GetBodyBox…) özellik gibi görünüyor → `g()` yardımcısı ile hem erken hem geç bağlamada çalışır hale getirildi.
- `SelectByID2("EDGE", ...)` köşe kenarını tam kenar koordinatında seçemedi → kenarlar gövde topolojisinden seçildi.
- F4 ilk denemede `FeatureCut4`'ün 2. argümanı (flip side to cut) yüzünden profilin dışını kesti → yalnız yön bayrağı deneniyor, kesimin malzeme kaldırdığı hacim farkıyla doğrulanıyor.
- Çizimler yeniden adlandırılınca boyut adları değişti → denklem bağları en sonda güncel adlarla kuruluyor.

## Bilerek basitleştirdiğim
- Delik konumları (`E_hole`) çizimde koordinatla konumlandı; konum boyutları/denklem bağı eklenmedi (çizim tam tanımlı değil). Çap boyutu tek dairede sürücü; değeri değiştirmek için betikteki `P` sözlüğü esas alınmalı.
- Bilgi eksikliği yok (spec §5: "None"); yorum gerektiren kalem olmadı.

## Ölçüm vs. hedef (SolidWorks kütle özellikleri; SLDPRT içinde ve `final.step` geri okunarak aynı)

| Büyüklük | Hedef | Ölçülen | Fark |
|---|---|---|---|
| Hacim mm³ | 57535.133 | 57535.133 | 0.000 % |
| Alan mm² | 15912.159 | 15912.159 | 0.000 % |
| CoM X / Y / Z | 0 / 0 / 4.9345 | 0.0000 / 0.0000 / 4.9345 | < 1e-4 mm |
| Xmin / Xmax | −50 / 50 | −50.000 / 50.000 | 0 |
| Ymin / Ymax | −30 / 30 | −30.000 / 30.000 | 0 |
| Zmin / Zmax | 0 / 10 | 0.000 / 10.000 | 0 |
| Yüz sayısı | 16 | 16 | — |

Ara adımlar: F1 V=60000.000; F2 V=59922.743 (−4·(9−9π/4)·10); F3 V=58791.770 (−4·π·9·10); F4 V=57535.133 (−π·100·4) — analitik değerlerle birebir.

Teslim: `final.step`, `P01_Plate.SLDPRT`, `build_p01.py`, `verify_step.py`, `yeniden_kur.md`, `parametreler.md`, `build_log.md`.
