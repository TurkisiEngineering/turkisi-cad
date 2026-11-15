# Modeli sıfırdan yeniden kurma

Gereken: Python 3.10+ ve `build123d==0.11.1` (OCP / OpenCascade dahil). Başka bir bağımlılık yok, girdi dosyası okunmaz,
bütün ölçüler `caster.py` içinde.

```sh
pip install build123d==0.11.1      # henüz kurulu değilse
cd teslim
python caster.py                   # -> teslim/final.step (12 gövde, AP214, birim INCH)
```

Süre yaklaşık 10 s. Çıktı olarak her iki yuvarlatma adımının durumu yazdırılır, örneğin:

```
P01: R0.06 x24 + R0.125 x2 ok; R0.04 x16 ok
P06: foot plate R0.04 x14 (-z half, mirrored) ok
written .../teslim/final.step
```

İsteğe bağlı kontroller:

```sh
python olcum.py               # modeli bellekte kurar, spec bölüm 6'daki tabloyla karşılaştırır
python olcum.py final.step    # yazılmış STEP'i geri okur, aynı karşılaştırmayı yapar
python caster.py --no-rounds  # çatal ve pedal yuvarlatmaları olmadan kurar (hata ayıklama için)
```

Notlar
- Model, spec'in global çerçevesinde ve inç cinsinden kurulur: +Y yukarı, dönme ekseni Y ekseni, tekerlek ekseni
  x=1.515, y=-0.75 ve Z'ye paralel. Hiçbir gövdeye sonradan taşıma uygulanmaz.
- STEP AP214 (AUTOMOTIVE_DESIGN) şemasında yazılır. Uzunluk birimi `CONVERSION_BASED_UNIT('INCH')` olduğu için
  koordinatlar dosyada inç değeriyle 1:1 yer alır.
- build123d'nin `import_step` fonksiyonu STEP'i mm'ye çevirerek okur. `olcum.py` bunu hesaba katar.
