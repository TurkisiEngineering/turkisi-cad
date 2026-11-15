# Değerlendirme: ölçüm kodu, rubrik, hedef listeleri

> **Bu klasör yapımcı ajana asla gösterilmez.** Burası değerlendirici (puanlayıcı) ajanlar ve insanlar içindir.
> Kör koşu kuralı: [`../README.md`](../README.md#kör-koşu-kuralı).

| Yol | İçerik |
|---|---|
| [`RUBRIK.md`](RUBRIK.md) | 100 puanlık rubrik (85'i otomatik, 15'i puanlayıcı) |
| `olc/olc.py` | ölçüm ve §1–§5 alt puanları; eğriler ve eşikler dosyanın başındaki sabitler bloğunda |
| `olc/olc_cekirdek.py` | STEP okuma, ince mesh, kesin B-rep mesafe, boolean işçisi (bellek sınırlı alt süreç) |
| `olc/tarifler.py` | `ozellikler.json` ve `resim_olculeri.json` kalemlerinin ölçüm tarifleri |
| `olc/paket_denetle.py` | bir referans STEP'in hedef listesine ait olduğunu doğrular (gövde sayısı, hacim, bbox) |
| `olc/requirements.txt` | F23 puanlamasında kurulu olan sürümler |
| `hedefler/P##/` | paket başına gizli listeler (aşağıda) |
| [`referanslar.csv`](referanslar.csv) | hangi pakette referans STEP var, hangi koşudan geldiği |

Kod, F23 canlı yayınında puan veren kodun aynısıdır; puanlama mantığına dokunulmadı. Yalnız `paket_denetle.py`'deki sabit
yollar argümana çevrildi. Kod yorumları ve ekran çıktısı F23'teki gibi İngilizce / ASCII Türkçedir.

## Kurulum

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r olc/requirements.txt    # Linux / macOS: .venv/bin/python
```

Python 3.13 ile denendi (Windows 11). Boş bellek 4 GB'ın altındaysa `olc.py` bekler (30 dk sonra vazgeçer); bellek
ölçümü Windows API'siyledir, başka sistemde bu kapı atlanır. Aynı anda tek `olc.py` çalıştırın: boolean işçisi büyük
montajlarda birkaç GB tutabilir.

## Çalıştırma

```bash
cd benchmark/degerlendirme
python -I olc/olc.py hedefler/P02/referans.step <teslim>/final.step --gizli hedefler/P02 --out ../../_work/puan/P02 --teslim <teslim>
```

Çıktıyı repo dışına ya da `_work/` altına yazın (`_work/` git'e girmez).

| Argüman | Anlamı |
|---|---|
| `<referans.step>` | doğru kabul edilen model. **Yalnız 6 pakette var**; aşağıya bakın |
| `<teslim>/final.step` | yapımcının teslim ettiği STEP |
| `--gizli hedefler/P##` | o paketin hedef listeleri |
| `--out <klasör>` | çıktı: `olcum.json` (ham sayılar, alt puanlar, kaynaklar), `olcum.md` (tablolar), `sapma_ornekleri.npz` |
| `--teslim <klasör>` | isteğe bağlı: §2'deki 5 teslim kalemini kontrol eder |

Çıkış kodu 0 = bitti, 2 = hata (sebebi `olcum_hata.txt`'de). OCC bir adımda çökerse denetçi süreç o adımı atlayıp yeniden
dener ve atlananı `olcum.json`'a yazar. Toplam puan ekrandaki son satırda ve `olcum.json` → `alt_puanlar.toplam_1_5`.

İlk deneme olarak kalibrasyon parçasını koşun (2 saniye):

```bash
python -I olc/olc.py hedefler/P00/referans.step hedefler/P00/referans.step --gizli hedefler/P00 --out ../../_work/puan/P00
# beklenen son satır: TOPLAM §1-§5 85.00 / 85
```

### Referans: en iyi koşumuz, katalog orijinali değil

`olc.py` §1'i (IoU, yüzey sapması, ΔV / ΔA / ΔCoM / Δbbox) ve §4'ün bölge sapmalarını teslim ile **referans model**
arasında ölçer. F23'ün resmî puanları ticari katalog modellerine karşı ölçüldü; o modellerin lisansı bize ait olmadığı
için yayımlanmaz. Onların yerine:

- **P00** (kalibrasyon levhası): bizim tasarımımız, referans tam doğru.
- **P02, P09, P10, P16, P17:** referans, o pakette F23'te en yüksek puanı alan NX dışı yapımcı koşusunun `final.step`'i
  (yalnız resmî puanı en az 84,5 / 85 olanlar). Liste: [`referanslar.csv`](referanslar.csv). Burada aldığınız puan
  "**en iyi koşumuza karşı**" puandır; referansın kendisi kusursuz olmadığından F23'ün resmî puanlarından biraz
  ayrışabilir.
- **Öteki paketler (39):** referans yok. `olc.py` referans olmadan koşmaz; `hedefler/` listeleri tamdır, ama geometri
  (§1) ve özelliklerin bölge sapmaları ancak spec'ten kendi kurduğunuz bir referansa karşı ölçülebilir. Puan o zaman
  sizin referansınıza göredir. Referansınızı önce `paket_denetle.py` ile hedef tablosuna karşı doğrulayın:

```bash
python -I olc/paket_denetle.py --hedefler hedefler --referans P05=benim_referansim.step
# hacim_fark_yuzde_occ ve montaj_bbox_fark_mm sıfıra yakın olmalı
```

## 85 puan ne demek

`olc.py` RUBRIK §1–§5'i otomatik puanlar:

| Bölüm | Puan | Ne ölçer |
|---|---|---|
| §1 Geometri | 40 (tek gövdede 50) | IoU, iki yönlü yüzey sapması P95 / maks, gövde başına hacim / alan / CoM / bbox toleransı |
| §2 Tamlık | 10 | eşleşen gövde, parça çeşidi ve adedi, 5 teslim kalemi |
| §3 Montaj | 10 (tek gövdede 0) | gövde pozları, bütün montaj hacim / alan / CoM / bbox, girişim kümesi |
| §4 Özellik | 20 | `ozellikler.json` kalemleri: delik, kanal, diş, pah, yuvarlatma, yazı... |
| §5 Resim | 5 | `resim_olculeri.json`: kaynak resimdeki ölçüler |

Kalan 15 puan (§6 CAD kalitesi: yeniden kurulabilirlik, gerçek modelleme, isimli parametreler, sağlık) puanlayıcının
elindedir. F23 skor tablosu yalnız 85'lik kısmı gösterdi.

## Hedef listeleri (`hedefler/P##/`)

| Dosya | İçerik |
|---|---|
| `hedef.json` | gövde başına hacim, alan, ağırlık merkezi, sınır kutusu, yüz sayısı, eşdeğer grup; montaj toplamı; girişimler. Her şey mm |
| `ozellikler.json` | §4 kontrol listesi: kalem, gövde, ölçüm tarifi, nominal, tolerans, bölge noktaları |
| `resim_olculeri.json` | §5: kaynak resmin ölçüleri, birim, tolerans, ölçüm tarifi |
| `parametreler.json` | §6: native kaynakta isimli parametre olarak beklenen 5 anahtar ölçü ve kabul edilen adlar |
| `spec_dogrulama.md` | spec yazarının doğrulama notu: hedef tablosu katalog orijinaline karşı, liste öz-kontrolleri, kararlar. Notlar özgün İngilizce çalışma hâlinde bırakıldı |
| `referans.step` | yalnız P00, P02, P09, P10, P16, P17 |

Temizlik: liste dosyalarından katalog numaraları, satıcı adları, katalog başlıkları ve yerel yollar çıkarıldı.
`spec_dogrulama.md` notları F23 çalışma klasörüne atıf yapar (`kaynak.json`, `is/...`, `olc_kendi/`): o dosyalar
yayımlanmadı, atıflar yalnız kayıt içindir.

## Bilinen öz-kontrol istisnaları

Her paketin listeleri, katalog orijinali kendisiyle `olc.py`'den geçirilerek denendi. Çoğu 85,00 / 85 verir. Aşağıdakiler
listelerden değil, kaynak dosyanın kendisinden ya da ölçüm yolundan dolayı tam puanın altında kalır. Bu tavanlar
düzeltilmedi; F23'te her config'e aynı uygulandı. Ayrıntı ilgili `spec_dogrulama.md` dosyasında.

| Paket | Orijinal kendisiyle | Eksik | Sebep |
|---|---|---|---|
| [P03](hedefler/P03/spec_dogrulama.md) | 82,19 | §1 maks sapma | kaynak dosyada kırpma eğrileri kendi mesh'iyle uyuşmuyor (0,095 mm gürültü) |
| [P11](hedefler/P11/spec_dogrulama.md) | 83,00 | §3 poz | eksenel simetrik gövdelerde asal eksenler belirsiz; ICP yönelimi 0,69° okur |
| [P25](hedefler/P25/spec_dogrulama.md) | 84,33 | §3 poz (P04) | P04 tam küre: yönelim tanımsız, sayısal gürültü 7,88° verir |
| [P28](hedefler/P28/spec_dogrulama.md) | 80,00 | §5 tamamı | parçanın teknik resmi yok, `resim_olculeri.json` boş; §5 "ölçülmedi" |
| [P31](hedefler/P31/spec_dogrulama.md) | 84,50 | §2 çeşit (H2) | kaynakta bir rakam gravürü pimlerden birine 0,001 in kesik açıyor; iki pim eş sayılmıyor |
| [P32](hedefler/P32/spec_dogrulama.md) | 84,96 | §1 maks sapma (P01) | serbest-form kanatlı gövdede boolean zaman aşımı; ince kabuk tahmini 0,0144 mm okur |

Puanlarken bu paketlerde referansın kendi puanını tavan olarak not edin.

## Bu klasördeki kodun doğrulanması

Taşındıktan sonra kod F23 ölçümlerini birebir verdi (`alt_puanlar` JSON'u bit bit aynı):

| Deneme | Referans | Teslim | Yeni konum | F23 kaydı |
|---|---|---|---|---|
| P00 kendisiyle | `hedefler/P00/referans.step` | aynı dosya | 85,00 | 85,00 |
| P00 bozuk kopya | `hedefler/P00/referans.step` | delik dolu, +0,1 mm X | 51,26 | 51,26 |
| P16, en iyi koşuya karşı | `hedefler/P16/referans.step` (SW-H1 r571844) | B3D-H0 r007208 | 83,89 | 83,89 (katalog orijinaline karşı) |
