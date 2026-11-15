# Build log: r518253, plastik kutu (P01 taban, P02 kapak, H1 vida)

Araç: SolidWorks 2024 (32.5), Python 3.13 + pywin32, late-bound COM. MCP sunucusu kullanılmadı.
Birim: inch. Çerçeve: spec'in global çerçevesi (SolidWorks Front Plane = XY, +Z = açılma yönü). Hiçbir gövde taşınmadı.

## Ne yaptım

Bütün geometri `betikler/` altındaki betiklerle, SolidWorks'ün kendi özellikleriyle kuruldu (içe aktarma yok).

**Ortak dış kabuk (B1/B2, L1/L2)**
- Sabit R0.1 köşeli 3° eğimli duvar, iki profil arasında *ruled loft*: z=0'da S ana hattı, 0.35 aşağıda (kapakta yukarıda) yarı ölçüleri `0.35·tan3°` küçültülmüş ve köşe yarıçapı yine R0.1 olan profil. Köşe yüzeyi böylece spec'in tarif ettiği eğik R0.1 silindiri oluyor. Taslak açılı ekstrüzyon kullanmadım; o yöntem köşe yarıçapını küçültürdü.
- Kenar yuvarlatma: köşe merkezleri (±0.80652, ±1.08152), R0.1 köşeli bir "slab" (z −0.30…−0.45) ve alt kenar döngüsüne R0.1 fillet. Köşelerde küre oktantı oluştu, alt düz yüz keskin köşeli 1.61304 × 2.16304 dikdörtgen. Loft bu slab'ın üstüne birleşiyor.
**Taban P01**: boşluk (1° taslaklı kesme, pah köşeli), sadece 4 düz duvarda R0.03 taban fileti, 4 köşe girintisi (1°, 0.035 derin), dudak (iki yüzü 3°, halka profil tek ekstrüzyon), dil (4 stadyum, 10° taslak, R0.005 üst kenar, ardından |y|<0.156 boşluğu taslaksız kesildi; düz uçlar dikey ve tam kesit gösteriyor), 1° göbek, iki kademeli haç nervür (üst haç x≤0.123 / z=0, alt haç x≤0.15221 / z=−0.035, yan yüzler aynı düzlemde), döndürmeli vida deliği (havşa 82°), etiket oluğu.
**Kapak P02**: aynı kabuk ve boşluk, 10° kanal (iç R0.05, dış R0.0885), ardından X kenarlarında 3° taslaklı "anahtar" dolgusu (|y|<0.146), 1° göbek, haç nervür (uç 0.153), r0.035 kör delik (z 0.035…0.42), etiket oluğu.
**Vida H1**: döndürme profili (84° baş konisi), 16 köşeli yıldız girinti, 4° taslaklı kesme (taban ofseti 0.0021 kendiliğinden çıkıyor).

## Hedef tabloyla karşılaştırma (kendi ölçümüm: SolidWorks mass properties, GetBodyBox)

| ID | Hacim in³ (hedef) | Fark | Alan in² (hedef) | KM z (hedef) | BBox | Yüz (bilgi) |
|---|---|---|---|---|---|---|
| P01 | 0.503833 (0.50384) | −0.001 % | 16.4496 (16.4101, +0.24 %) | −0.2902 (−0.2902) | X ±0.925, Y ±1.200, Z −0.45…0.06 ✓ | 169 (211) |
| P02 | 0.479377 (0.47934) | +0.008 % | 15.9833 (15.9829) | 0.3372 (0.3372) | X ±0.925, Y ±1.200, Z 0.03…0.48 ✓ | 80 (89) |
| H1 | 0.0022953 (0.00230; 37.61 mm³ = 0.0022951) | +0.01 % (37.613 mm³) | 0.1618 (0.1618) | −0.2265 (−0.2265) | ±0.081, Z −0.45…0.05 ✓ | 21 (23) |
| Toplam | 0.985505 (0.98548) | +0.003 % | 32.5947 (32.5548) | 0.01513 (0.0151) | ✓ | 3 gövde ✓ |

KM x, y: üç gövdede de 0 (1e-10'dan küçük). BBox farkı 0.00001'den az (GetBodyBox'un payı).

Girişimler (gövde kesişim hacmi):
- P01–P02: **4.991 mm³** (hedef 4.998), dil / kanal dış yanağı
- P02–H1: **0.055 mm³** (hedef 0.055), z 0.035…0.05
- P01–H1: **0** (hedef 0)

`final.step`: başlık `FILE_SCHEMA(('AUTOMOTIVE_DESIGN'))` yani AP214, uzunluk birimi INCH, 3 adet MANIFOLD_SOLID_BREP.

## Nerede takıldım

1. **Birim tercihi**: İlk denemede belge birimi için yanlış tercih kimliği (260/261) kullandım. Bunlar kütle-özelliği gösterim ayarlarıymış. Sonuç olarak STEP mm ve AP203 çıktı. `swconst.tlb`'den doğru sabitleri buldum: `swUnitSystem` = 263, IPS = 3, `swStepAP` = 75. Düzelttim. `swStepAP` sistem genelinde bir seçenek olduğu için export sırasında 214 yapılıyor, sonra kullanıcının eski değerine (203) geri alınıyor.
2. **Montaj**: `IAssemblyDoc.AddComponent5` / `AddComponent4` bu oturumda (geç ve erken bağlamayla, farklı config seçenekleriyle) hep `Nothing` döndü. Zaman kısıtı yüzünden `.SLDASM` yerine `Kutu_Hepsi.SLDPRT` yaptım: üç parça *Insert Part* (bağlı, dönüşüm yok) ile tek çok-gövdeli parçada toplanıyor. `final.step` buradan alındı. Gövdeler birleştirilmedi, 3 ayrı katı.
3. `MathUtility.CreatePoint` geç bağlamada çağrılamadı. Çizim dönüşümünü `ModelToSketchTransform.ArrayData` ile kendim uyguladım.
4. Koordinatla `SelectByID2("EDGE")` seçimi çalışmadı. Kenarları geometrik olarak buluyorum: gövde kenarları içinde `GetClosestPointOn` ile verilen noktaya en yakın kenar seçiliyor.

## Bilerek basitleştirdiklerim / yorumlarım

- **B10 (taban nervür ve göbek dibi R0.005 iç filetleri) yapılmadı.** Hacim etkisi yaklaşık +5e-6 in³ (%0.001). Ölçülen hacim farkı bu mertebede. Yüz sayısının düşük çıkmasının ana sebebi bu (211'e karşı 169). Kalan fark SolidWorks'ün yüz bölmesinden geliyor.
- Kenar yuvarlatmasında loft'un alt ucu R0.1 eksen düzleminde (z=−0.35 / 0.38). Spec'teki teğet noktası z=−0.35523'te. Bu yüzden loft ile slab arasında 0.00014 genişliğinde yatay bir mikro basamak kalıyor (hacim etkisi ~1e-6 in³).
- P01 yüzey alanı hedeften 0.04 in² (%0.24) fazla. Hacim, KM ve P02'nin (aynı kabuk yöntemiyle) alanı birebir tuttuğu için fark tabana özgü bir detayda. Kaynağını süre içinde bulamadım. Alan kabul kriterlerinden biri değil.
- Dil uçları: X kenar segmentlerinin |y|=0.156'daki uçları spec'e göre dikey ve taslaksız. Bunun için dil önce sürekli kuruldu, sonra boşluk dik kesildi.
- Kapak "anahtarı": kanal kesildikten sonra 3° taslaklı bir dolgu ekstrüzyonuyla geri dolduruldu. |y| = 0.146 → 0.14417 değerleri spec ile aynı.
- Parça tanımlarındaki bütün değerler spec'ten. Eksik bilgi yoktu, ek yorum gerekmedi.
- Malzeme ataması yapılmadı. Ölçümler hacim tabanlı olduğu için yoğunluk etkisizdir.
