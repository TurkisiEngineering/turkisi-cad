# Puanlama rubriği (araçtan bağımsız)

F23 "Agentic CAD Ligi" yayınında kullanılan rubrik. Canlı yayından önce kilitlendi (2026-11-11) ve yayın boyunca
değişmedi. Eğriler ve eşikler `olc/olc.py` dosyasının baştaki sabitler bloğunda; tek kaynak orasıdır, burası onun
okunur hâlidir. İkisi ayrışırsa kod geçerlidir.

Bütün ölçümler yapımcının `final.step` dosyası ile referans STEP arasında, **hizalamasız** (aynı global çerçeve), aynı
betikle (`olc/olc.py`) yapılır. Spec'in istediği çerçevede kurmamak bir hatadır ve puana yansır.

## Görev: spec'ten kör yapım (A görevi)

Yapımcı ajana giden **tek şey** `specs/P##-.../spec.md` dosyasıdır. Spec yazım kuralları:

1. Spec tek kaynaktır: yapımcı başka hiçbir şey görmez. Her ölçü referans modelden **ölçülmüştür**; ölçülemeyen "belirsiz"
   (undetermined) diye yazılır, uydurulmaz.
2. **Araçtan bağımsız dil:** NX, SolidWorks, build123d, SolidCraft, journal, sketch DOF gibi araca özgü terim yoktur.
   Özellikler geometri olarak tarif edilir (düzlem, profil, döndürme, desen, delik).
3. Global çerçeve, birim, gövde listesi ve adetleri, gövde başına hedef tablosu (hacim, alan, ağırlık merkezi, sınır kutusu),
   özellik tarifleri ve kaynağın kendi basitleştirmeleri ("burada diş yok, öyle kalmalı").
4. Marka, parça numarası ve ürün bağlantısı yoktur; ürün adı geneldir ("iç düz dişli").
5. **Doğrulama:** spec'in hedef tablosu referans modele karşı ölçülmüştür. Sonuç her paketin
   `hedefler/P##/spec_dogrulama.md` dosyasındadır; spec'in kendi hatası yapımcının hatası sayılmasın diye.

Değerlendirici tarafı (`hedefler/P##/`): hedef tablosu (`hedef.json`), özellik kontrol listesi (`ozellikler.json`, §4),
teknik resim ölçü listesi (`resim_olculeri.json`, §5), isimli parametre listesi (`parametreler.json`, §6'da beklenen 5
anahtar ölçü).

## Toplam: 100 puan (85'i `olc.py` otomatik, 15'i puanlayıcı)

### 1. Geometrik doğruluk: 40

Gövdeler Macar algoritmasıyla eşleştirilir (ağırlık merkezi + sınır kutusu + hacim). Eşleşmeyen referans gövdesi bu
kalemde 0 alır.

| Alt kalem | Puan | Gövde oranı (doğrusal enterpolasyon) |
|---|---|---|
| A. IoU, gövde başına eşit ağırlık | 12 | ≥ 0,9995 → 1; 0,999 → 0,9; 0,995 → 0,6; 0,98 → 0,3; ≤ 0,95 → 0 |
| B. IoU, hacim ağırlıklı | 4 | aynı eğri |
| C. İki yönlü yüzey sapması P95 (mm) | 10 | ≤ 0,005 → 1; 0,02 → 0,9; 0,05 → 0,7; 0,127 → 0,4; ≥ 0,5 → 0 |
| D. İki yönlü yüzey sapması maks (mm) | 6 | ≤ 0,01 → 1; 0,05 → 0,8; 0,127 → 0,5; 0,5 → 0,2; ≥ 2,5 → 0 |
| E. Tolerans kontrolleri | 8 | gövde başına 4 kontrol: ΔV ≤ %0,5 (donanım %2), ΔA ≤ %0,5 (donanım %2), ΔCoM ≤ 0,5 mm, Δbbox ≤ 0,13 mm; oran = geçen / 4 |

Ölçüm notları (`olc.py` bunları uygular):

- Sapma **kesin B-rep** mesafesiyle ölçülür (yüz başına örnek → karşı kabuğa `BRepExtrema`); helisel / spline yüzeyde
  `min(kesin, ince mesh)`. Mesh-mesh mesafesi tek başına kullanılmaz (0,07 mm'ye varan yapay sapma verir).
- OCC `GProp` hacmi helisel gövdelerde yanlış okuyabilir; hacim, OCC ile ince mesh integrali %0,5'ten fazla ayrışırsa mesh
  değeri alınır ve rapora yazılır.
- IoU: OCC boolean geçerliyse boolean, değilse ince kabuk tahmini; hangisi kullanıldıysa tabloda yazar.

### 2. Tamlık: 10

- 6: eşleşen gövde / referans gövde. Her fazla gövde −0,5.
- 2: farklı parça çeşitleri ve adetleri; her yanlış kalem −0,5.
- 2: teslimatlar (5 kalem: `final.step`, native kaynak, `yeniden_kur.md`, `parametreler.md`, `build_log.md`); eksik kalem
  başına −0,5. `olc.py`'ye `--teslim <klasör>` verilmezse bu kalem kontrol edilmez.

### 3. Montaj ve poz: 10

Tek gövdeli parçalarda bu 10 puan §1'e oranla dağıtılır (§1 = 50, §3 = 0; toplam yine 85).

- 4: gövde başına poz. ΔCoM ≤ 0,025 mm ve yönelim ≤ 0,01° tam; > 0,5 mm ya da > 0,5° → 0; arası doğrusal.
- 3: bütün montaj hacim (%0,1), alan (%0,1), CoM (0,13 mm), bbox (0,13 mm); her biri 0,75.
- 3: girişim kümesi. Birinde olup ötekinde olmayan her girişim çifti (> 8 mm³) −1; ortak girişimde hacim farkı > %5 → −0,5.

### 4. Özellik sadakati: 20

Parça başına kontrol listesi (`ozellikler.json`): delik, kanal, diş, pah, yuvarlatma, lob / tırtıl, vida dişi, yazı.
Kalem başına: tam 1, yakın (sayı doğru, ölçü toleransı aşıyor) 0,5, kayıp 0. Spec dışı uydurulan her özellik −0,5 kalem.
Puan = 20 × toplanan / toplam. Ölçü toleransı 0,05 mm, açı 0,2°. Yöntem: analitik yüzey sayımı (düzlem / silindir / koni /
tor parametreleri), kesit ve bölgesel sapma.

Çekirdeğe bağlı sayım kalemlerinde (dişli ya da serbest-form yüzlerde `sayi`) `olc.py` `hakem` önerirse son kararı
puanlayıcı verir ve gerekçesini yazar (geçici puan 0).

### 5. Teknik resim ölçüleri: 5

Kaynak resimdeki her ölçü yeniden yapımda ölçülür (`resim_olculeri.json`); tolerans resmin yazılı hassasiyetidir.
Puan = 5 × geçen / toplam. Modellenmiş geometriye karşılık gelmeyen ölçüler ayrı yazılır, ölçülebiliyorsa sayılır.

### 6. CAD kalitesi: 15 (puanlayıcı elinde, `olc.py` hesaplamaz)

| Kalem | Puan | Nasıl |
|---|---|---|
| Yeniden kurulabilirlik | 4 | `yeniden_kur.md` temiz bir kopyada koşulur; aynı `final.step` (gövde başına ΔV ≤ %0,01, Δbbox ≤ 0,01 mm) → 4; kısmi → 2; çalışmıyor → 0 |
| Gerçek modelleme | 4 | gövdelerin kaçı özelliklerle / kodla kurulmuş: içe aktarılmış STEP, mesh, dumb body = 0. Oran × 4 |
| İsimli parametreler | 4 | `parametreler.json`'daki 5 anahtar ölçü native kaynakta isimli parametre / ifade / değişken olarak var mı; oran × 4 |
| Sağlık | 3 | native dosya hatasız açılıyor / betik uyarısız koşuyor, bastırılmış ya da başarısız özellik yok; sorunlu parça başına −0,5 |

Eskiz kısıt derecesi (DOF) puanlanmaz; build123d ve CLI tabanlı yolların eşdeğeri yok.

F23 canlı yayınının skor tablosu yalnız §1–§5'i (85 puan) gösterdi.

## Özel durumlar

- `tavan`: süre tavanı doldu; o ana kadar teslim edilen puanlanır. `final.step` yoksa §1–§5 sıfırdır, §6 kaynaktan
  puanlanır.
- `cokme`: araç çöktü ve yapımcı toparlayamadı: aynı kural.
- **Neden sınıfı:** her önemli sapma için S (spec eksik / yanlış), B (yapımcı saptı), K (kaynak çelişkisi), A (aracın
  sınırı: araç bu geometriyi kuramıyor ya da STEP'e yanlış yazıyor). S sınıfı sapmalar da puandan düşer (spec her config için
  aynı olduğundan sıralamayı bozmaz).

## Kararlar

- **STEP biçimi:** kural AP214. Yalnız AP242 yazabilen bir aracın kendi AP242 çıktısı kabul edilir; başlık elle
  değiştirilmez.
- **Referansın kendi tavanı:** bazı katalog orijinalleri kendileriyle karşılaştırıldığında bile 85'in altında kalır (kusurlu
  kaynak dosyası, simetrik gövdede belirsiz yönelim, resmi olmayan parça). Bu tavanlar düzeltilmeden, her config'e aynı
  biçimde uygulanır. Liste ve açıklama: [`README.md`](README.md#bilinen-öz-kontrol-istisnaları).
- **Kalibrasyon (P00):** referans kendisiyle 85,00 alır; bozulmuş kopyası (`(42, 22)` deliği dolu, +0,1 mm X) 51,26 alır.
