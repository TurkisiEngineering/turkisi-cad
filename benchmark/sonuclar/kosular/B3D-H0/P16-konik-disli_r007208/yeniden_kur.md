# Yeniden kurulum

Gereksinim: Python 3.10+ ve kurulu build123d 0.11.1 (OCP onunla birlikte gelir).

Temiz bir kopyada `teslim/` klasöründe:

```
python miter_gear.py
```

Betik `miter_gear.py` ile aynı klasöre `final.step` (AP214, mm, spec'in global çerçevesi) yazar ve
kontrol değerlerini (geçerlilik, katı/yüz sayısı, hacim, alan, CoM, bbox) ekrana basar. Süre ≈ 8 s.
Başka girdi dosyası gerekmez; tüm ölçüler betiğin başındaki parametrelerdedir.
