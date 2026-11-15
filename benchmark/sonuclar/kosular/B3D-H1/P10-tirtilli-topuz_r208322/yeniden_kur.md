# Yeniden kurulum

Gereken: Python 3.10+ ve `build123d==0.11.1` (OCP / OpenCascade 7.9 ile).

```
cd teslim
python knob.py
```

- `params.py`: bütün isimli ölçüler (inç). `knob.py` bunları içe aktarır.
- `knob.py` üç gövdeyi kurar (P01 çekirdek, P02 kaplama, P03 dişli insert), her birinin hacim/alan/CoM/bbox/yüz
  sayısını ekrana yazar ve aynı klasöre `final.step` dosyasını yazar (AP214 = AUTOMOTIVE_DESIGN, uzunluk birimi INCH,
  koordinatlar spec çerçevesinde, taşıma yok). Çalışma süresi yaklaşık 10 s.
- Fonksiyonlar tek tek de çağrılabilir: `from knob import build_core, build_coating, build_insert, build_all`.
