# Yeniden kurulum

Gereken: Windows, SOLIDWORKS 2024 (kurulu, `C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS`), Python 3 + pywin32.

```
cd teslim\betikler
python build_all.py
```

`build_all.py` SolidWorks'e COM ile bağlanır (çalışmıyorsa başlatır) ve sırayla şunları yapar:
1. `build_core.py` → `teslim\P01_core.SLDPRT` (C1 revolve, C3 boşluk + kaburgalar, C2 oyuklar, C4 delik, C5 halka)
2. `build_coating.py` → `teslim\P02_coating.SLDPRT` (S1 lobed kap, S2 R0.06 yuvarlatmalar, S3 kubbe, S4 kesimler,
   P01 parça olarak eklenip Combine-Subtract ile çıkarılır; bu yüzden önce 1. adım gerekir)
3. `build_insert.py` → `teslim\P03_insert.SLDPRT` (tüp, helis + süpürme kesim ile sağ el 3/8"-16 diş, 90° havşalar)
4. `build_assembly.py` → `teslim\knob_assembly.SLDASM` (3 bileşen birim dönüşüm + sabit) ve `teslim\final.step`
   (AP214, birim inç)

Her betik sonunda gövdenin hacim / alan / CoM / bbox / yüz sayısını yazdırır. Parametreler her betiğin başındaki
`P = dict(...)` sözlüğündedir; ayrıca her parçanın Equation Manager'ına global değişken olarak yazılır.
Not: Betikler yeni belgeler açar; tekrar çalıştırmadan önce aynı adlı açık belgeleri kapatın.
