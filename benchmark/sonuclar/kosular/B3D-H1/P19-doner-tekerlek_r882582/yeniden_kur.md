# Yeniden kurma

Gereksinim: Python 3.13 + build123d 0.11.1 (OCP dahil).

```
cd teslim
python caster.py          # 12 gövdeyi kurar, final.step yazar (AP214, birim INCH)
python olcum.py           # (isteğe bağlı) bellekteki modeli spec §6 tablosuyla karşılaştırır
python olcum.py final.step  # (isteğe bağlı) STEP'i geri okuyup aynı karşılaştırmayı yapar
```

- Tek kaynak `caster.py`; dış dosya, STEP/mesh içe aktarma yok. Çalışma süresi ~7 s.
- Tüm gövdeler spec'in global çerçevesinde (inç, +Y yukarı, döner eksen = Y) yerinde kurulur; sonradan taşıma yok.
- STEP'te uzunluk birimi `CONVERSION_BASED_UNIT('INCH')`; koordinat değerleri spec'teki inç değerleriyle birebir aynıdır
  (ör. plaka üstü y = 2.75). mm'ye çeviren bir okuyucu 25.4 ile çarpar.
