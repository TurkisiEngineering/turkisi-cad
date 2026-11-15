# SolidWorks native dosyaları nasıl açılır

Bu klasörde yapımcının SolidWorks'te kurduğu native dosyalar var:

- `H1_Screw.SLDPRT`
- `Kutu_Hepsi.SLDPRT`
- `P01_Base.SLDPRT`
- `P02_Lid.SLDPRT`

- SolidWorks ile açın (koşular SolidWorks'ün kurulu sürümüyle kaydedildi; daha eski bir sürüm açamaz). Özellik ağacı ve isimli ölçüler (`parametreler.md`) olduğu gibi durur.
- SolidWorks yoksa `final.step` aynı geometridir (FreeCAD, Fusion, Onshape vb. açar).
- Dosyaların içinde SolidWorks'ün kendi yazdığı kayıt yolu ve kullanıcı adı gibi kayıt bilgileri bulunur; geometriyi etkilemez.
- Yeniden üretmek için: `yeniden_kur.md` ve klasördeki pywin32 betikleri.
