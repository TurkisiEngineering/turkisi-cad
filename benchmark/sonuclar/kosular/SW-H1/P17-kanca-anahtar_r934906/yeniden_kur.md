# Yeniden kurma

Gereken: Windows, SolidWorks (2024 ile denendi), Python 3 + pywin32.

```powershell
cd <temiz kopya>\teslim
python build_spanner.py      # SolidWorks'e COM ile bağlanır (gerekirse başlatır), parçayı sıfırdan kurar
python verify.py             # isteğe bağlı: kaydedilen SLDPRT'yi açar, hacim/alan/CoM/bbox/yüz/denklem yazdırır
```

`build_spanner.py`:
1. Varsayılan parça şablonuyla yeni parça açar, birimi IPS (inch) yapar.
2. Global değişkenleri Equation Manager'a yazar (`"T"` F1 derinliğini sürer).
3. F1 → F2 → F3a → F3b → F4 özelliklerini spec'in global çerçevesinde, yerinde kurar (taşıma yok).
4. `P01_Spanner.SLDPRT` ve `final.step` (AP214, inch, periyodik yüz bölme kapalı) dosyalarını betiğin yanına yazar.
5. Yalnız kendi açtığı belgeyi kapatır (`--keep-open` verilirse açık bırakır).

Çıktılar: `P01_Spanner.SLDPRT`, `final.step`, konsol günlüğü (`build_output.txt` olarak saklandı).
