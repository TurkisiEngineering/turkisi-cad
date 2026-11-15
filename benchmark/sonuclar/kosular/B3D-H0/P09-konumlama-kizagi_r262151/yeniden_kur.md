# Yeniden kurulum

Gereken: Python 3.10+ (denendi: 3.13.13) ve `build123d==0.11.1` (OCP/OCCT ile birlikte gelir).

```
pip install build123d==0.11.1
cd teslim
python model.py            # final.step'i sıfırdan üretir (~25 s)
python model.py --check    # + bellek içindeki gövdeleri spec §6 hedefleriyle karşılaştırır
python measure.py          # üretilen final.step'i geri okuyup aynı tabloyu basar
```

- `model.py`: tüm geometri (P01–P08, 4 × H1), parametreler dosyanın başında.
- `measure.py`: spec §6 hedef tablosu ve karşılaştırma (hacim, alan, ağırlık merkezi, sınır kutusu).
- Çıktı: `final.step`, AP214 (AUTOMOTIVE_DESIGN), uzunluk birimi **inç**, spec'in global çerçevesi;
  12 ayrı katı gövde, her biri isimli (P01_Base … H1_d). Taşıma/dönüşüm gerekmez.
