# Yeniden kurulum

Gereksinim: Python 3.13 + build123d 0.11.1.

```
cd teslim
python spanner.py
```

Betik `final.step` dosyasını (AP214, birim inch, spec'in global çerçevesi) betiğin yanına yazar ve
katı sayısı, yüz sayısı, hacim, alan, kütle merkezi ve sınır kutusunu ekrana basar.
Beklenen çıktı: `solids 1 faces 27 valid True`, `volume 0.208501`, `area 4.612037`.
