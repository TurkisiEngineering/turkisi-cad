# Yeniden kurulum

Gereksinim: Python 3 + build123d 0.11.1 (OCP dahil). Başka girdi/dosya gerekmez.

```
cd teslim
python knob.py
```

Betik üç gövdeyi (P01 çekirdek, P02 kaplama, P03 dişli insert) spec'in global çerçevesinde
(Z ekseni, inç) kurar ve aynı klasöre `final.step` (AP214, uzunluk birimi INCH, 3 ayrı solid,
etiketli) yazar; konsola her gövdenin hacim/alan/ağırlık merkezi/bbox/yüz sayısını basar.
Süre ~20 s.
