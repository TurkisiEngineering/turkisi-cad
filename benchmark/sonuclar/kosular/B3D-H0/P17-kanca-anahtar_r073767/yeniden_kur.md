# Yeniden kurma

Gereksinim: Python 3.10+ ve build123d 0.11.1 kurulu ortam.

```
cd teslim
python spanner.py
```

Betik `spanner.py` geometriyi sıfırdan kurar (F1 dış hat + ekstrüzyon, F2 kanal, F3 kenar yuvarlatmaları,
F4 konik bitişler), aynı klasöre `final.step` (AP214, birim inç, spec'in global çerçevesi) yazar,
dosyayı geri okuyup hacim/yüz sayısını, kütle merkezini ve sınır kutusunu ekrana basar. Süre ~6 s.
Başka girdi dosyası gerekmez; taşıma/yeniden hizalama adımı yoktur.
