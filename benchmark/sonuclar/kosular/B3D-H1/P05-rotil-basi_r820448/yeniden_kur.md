# Yeniden kurulum

Gereksinim: Python 3.10+ ve `build123d==0.11.1` (OCP/OpenCascade ile birlikte gelir).

```
pip install build123d==0.11.1
cd teslim
python rod_end.py      # ~50 s; teslim/final.step dosyasını (AP214, birim INCH) yeniden yazar
python check.py        # isteğe bağlı: hacim / alan / ağırlık merkezi / sınır kutusu, girişim, STEP yeniden okuma
```

- Tek kaynak `rod_end.py`; tüm ölçüler dosyanın başındaki isimli parametrelerdedir (bkz. `parametreler.md`).
- Gövdeler global çerçevede yerinde kurulur (şaft ekseni Y, bilye merkezi (0,1,0), bilye deliği Z'ye paralel); sonradan konumlandırma yoktur.
- STEP içinde 2 katı gövde: `P01_Housing_threaded_shank`, `P02_Ball_with_collars`.
