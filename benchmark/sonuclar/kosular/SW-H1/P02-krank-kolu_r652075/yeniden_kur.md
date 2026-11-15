# Yeniden kurulum — P01 Crank handle

Gereksinim: Windows, SolidWorks 2024 (kurulu, lisanslı), Python 3 + `pywin32`.

```
cd <teslim klasörü>
python build_crank.py            # çıktı: bu klasöre "P01 Crank handle.SLDPRT", final.step (AP214), measure.json
python verify_step.py            # isteğe bağlı: final.step'i SolidWorks'e geri alıp hacim/alan/CoM/kutu ölçer
```

- `python build_crank.py <çıkış_klasörü>` ile başka klasöre üretilebilir.
- SolidWorks açık değilse COM ile başlatılır. Betik yalnız kendi oluşturduğu belgeyi kapatır
  (`KEEP=1` ortam değişkeniyle belge açık bırakılır).
- Varsayılan parça şablonu kullanılır (`swDefaultTemplatePart`); API metre ile çalıştığından şablon birimi sonucu etkilemez.
- Ölçüleri değiştirmek için `build_crank.py` başındaki `PARAM` sözlüğünü düzenleyip yeniden çalıştırın.

Özellik sırası (Front Plane = XY, Right Plane = YZ; global çerçeve spec ile birebir, taşıma yok):
1. `SK_A1` (Front) → `A1_HubArmRevolve`: X ekseni etrafında 360° revolve (spec A1, 12 adım).
2. `SK_A2` (Right) → `A2_PlanTrim`: plan konturu, +X yönünde Through All extrude-cut, "flip side to cut"
   (konturun içi kalır = A1 ∩ prizma).
3. `SK_B` (Front) → `B_GripRevolve`: Y=-100, Z=0 eksenli 360° revolve, birleştir (spec B).
4. `SK_C` (Front) → `C_Bore`: Ø10 delik + 120° havşa, X ekseni etrafında revolve-cut (spec C).
