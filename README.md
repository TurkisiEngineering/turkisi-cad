# turkisi-cad · Agentic CAD Ligi (F23)

**Aynı yapay zekâ modeli, farklı CAD araçları: hangisi gerçekten çiziyor?**

Bu repo, Türkişi Engineering'in **F23 · Agentic CAD Ligi** canlı yayınının açık rehberidir. Yayında gösterilen her şey
burada: spec'ler, ölçüm kodu, koşu düzeneği, kontrol paneli, kurulum rehberleri, bitmiş modeller ve NX dışı CAD
skill'leri. Tek istisna Türkişi'nin özel **NX harness'i** (aşağıya bakın).

## F23 nedir?

Kör bir benchmark. Bir **Opus 5.5** yapımcı ajanı, **45 herkese açık katalog tarzı parçayı** yalnız yazılı bir
`spec.md`'den yeniden çizer. Orijinal modeli görmez, web'e çıkamaz; her araç çağrısı bir guard kancasından geçer.
Çıkan `final.step`, kilitli bir rubrikle ve aynı betikle (`olc.py`) orijinaline karşı ölçülür.

Model sabittir. Değişen yalnız **araç** ve elindeki **harness**:

| Config | Araç | Harness basamağı |
|---|---|---|
| **NX-H2** | Siemens NX 2206 | H2 · uzman harness (özel, paylaşılmıyor) |
| **SW-H1** | SolidWorks | H1 · topluluk MCP'si |
| **SC-H0** | SolidCraft | H0 · çıplak (yalnız CLI) |
| **B3D-H0** | build123d | H0 · çıplak (düz Python) |
| **B3D-H1** | build123d | H1 · topluluk MCP'si |

H0 = aracın kendi API'si, kod yazarak · H1 = H0 + topluluk MCP'si (en çok yıldızlı uygun olan; build123d'de ikinci
sıradaki build123d-mcp, çünkü birinci olan agentcad sürüm ve internet bağımlılığı yüzünden çıkarıldı) · H2 = H1 + uzman
skill'ler.

## Kanal ve yayın

**Türkişi Engineering**, agentic CAD ve mühendislik üzerine bir YouTube kanalı. F23 canlı yayını **11 Kasım 2026**'da
yapıldı: beş istasyon aynı anda parça çizdi, puanlar canlı tabloya düştü. Yayında ne gösterildiği:
[docs/yayin.md](docs/yayin.md).

## Klasörler

| Klasör | İçerik |
|---|---|
| [`tools/`](tools/) | araç kurulum rehberleri: Claude Code, SolidWorks, SolidCraft, build123d (NX yalnız "özel" notu) |
| [`benchmark/specs/`](benchmark/specs/) | parça spec'leri: **yapımcı ajanın gördüğü tek yer** |
| [`benchmark/degerlendirme/`](benchmark/degerlendirme/) | ölçüm kodu (`olc.py` …), rubrik, hedef listeleri; yalnız değerlendirici için, yapımcıya gösterilmez |
| [`benchmark/kosu/`](benchmark/kosu/) | koşu düzeneği: koşucu, guard kancası, istemler, matris |
| [`benchmark/sonuclar/`](benchmark/sonuclar/) | puanlar ve bitmiş çıktılar (SolidWorks native, build123d, SolidCraft) |
| [`panel/`](panel/) | kontrol paneli, skor tablosu, yayın sayfası |
| [`skills/`](skills/) | NX dışı CAD skill'leri ve ajanları (QA kapısı, kesit, girişim, baskı, STEP kaydı) |
| [`docs/`](docs/) | [mimari](docs/mimari.md), [yayın](docs/yayin.md), [SSS](docs/sss.md) |

Kör koşu kuralı ve klasörlerin rolü: [benchmark/README.md](benchmark/README.md).

## Hızlı başlangıç: kendi harness'ını bir spec'te dene

1. **Bir spec seç.** [`benchmark/specs/`](benchmark/specs/) altından bir parça klasörü al (ilk deneme için bir "şekil"
   seviyesi parça). Ajanına **yalnız** o `spec.md`'yi ver; web'i ve bu reponun geri kalanını kapat (guard örneği:
   [`benchmark/kosu/`](benchmark/kosu/)).
2. **Kur ve teslim et.** Ajanın modeli spec'in global çerçevesinde ve biriminde kursun, bir `teslim/` klasörüne
   `final.step`, native kaynak, `yeniden_kur.md`, `parametreler.md` ve `build_log.md` yazsın. Aracın kurulumu:
   [`tools/`](tools/).
3. **Ölç.** Teslim klasörünü [`benchmark/degerlendirme/`](benchmark/degerlendirme/)'deki `olc.py` ile puanla.
   `olc.py` her zaman bir **referans STEP** ister: varsa `benchmark/degerlendirme/hedefler/P##/referans.step` kullan.
   Bu dosya bizim en iyi koşumuzdan (≥ 84,5 / 85) üretildi; yani puanın katalog orijinaline karşı değil, **bizim en
   iyi koşumuza karşı**dır. Referansı olmayan pakette kendi referansını hazırlaman gerekir. Sonra
   [`benchmark/sonuclar/`](benchmark/sonuclar/)'daki koşularla karşılaştır.

Yeni bir araç ya da harness eklemek için: [docs/sss.md](docs/sss.md#kendi-aracımı--harnessımı-nasıl-eklerim).

## İlk sonuçlar

Canlı yayın puan dosyasındaki ([`benchmark/sonuclar/puanlar.csv`](benchmark/sonuclar/puanlar.csv), `faz = yayin`)
**26 geçerli koşunun** özeti; iptal ve yardımlı koşular hariç. 45 parça planlanmıştı; yayın bittiğinde 11 parça koşulmuştu.
Puanlar `olc.py`'nin ölçtüğü **85 üzerinden**dir (geometri, tamlık, montaj, özellik, teknik resim); CAD kalitesinin
15 puanı bu tabloda yok.

| Config | Koşu | Ortalama / 85 | Medyan / 85 |
|---|---|---|---|
| B3D-H0 | 5 | 84,49 | 84,32 |
| SW-H1 | 6 | 83,21 | 83,70 |
| NX-H2 | 6 | 82,24 | 84,06 |
| B3D-H1 | 5 | 68,00 | 84,06 |
| SC-H0 | 4 | 54,25 | 66,00 |

Okurken dikkat:

- Config'ler çoğunlukla **farklı parçalar** çizdi; bu tablo bir sıralama değil, ilk görünümdür. Dört parçada kafa kafaya
  koşu yapıldı (aynı parça dört ya da beş istasyonda).
- Ortalamayı tek bir koşu çok etkileyebilir: B3D-H1'in bir koşusu 3,5 aldı, SC-H0'ın bir koşusu süre tavanına takılıp
  `final.step` teslim edemedi (0). Medyan bu yüzden yanında.
- **MCP gerçekte ne kadar kullanıldı:** 7 koşunun hiçbirinde SW-H1 yapımcısı bir SolidWorks MCP aracı çağırmadı
  (pywin32 ile COM kodu yazdılar); B3D-H1 MCP'yi 6 koşunun yalnız 1'inde kullandı.
- Ham tablo: [`benchmark/sonuclar/puanlar.csv`](benchmark/sonuclar/puanlar.csv); bitmiş çıktılar:
  [`benchmark/sonuclar/`](benchmark/sonuclar/). Puanlama kuralları:
  [`benchmark/degerlendirme/`](benchmark/degerlendirme/).

## NX hariç

NX-H2'nin uzman harness'i (NX skill'leri, journal yardımcıları) Türkişi Engineering'in **özel** çalışmasıdır ve bu
repoda yoktur. NX-H2 koşularının native dosyaları ve akışları da paylaşılmaz; NX-H2'nin puanları sonuç tablosunda yer
alır. Orijinal katalog modelleri (STEP / PDF) de paylaşılmaz. Üçüncü taraf araçlar (MCP sunucuları, SolidCraft,
build123d) kopyalanmadı; [`tools/`](tools/) kendi repolarına link ve bizim ayarlarımızı verir.

## Lisans

[MIT](LICENSE) · © 2026 Türkişi Engineering. Üçüncü taraf araçlar kendi lisanslarına tabidir.
