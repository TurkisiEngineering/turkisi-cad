# Yayında ne gösterildi

**F23 · Agentic CAD Ligi** canlı yayını Türkişi Engineering YouTube kanalında, **11 Kasım 2026**'da yapıldı
([yayın kaydı](https://www.youtube.com/watch?v=b4b8olf0IgI)).
Başlık: *4 CAD, 5 yarışmacı, 45 parça.* Aynı yapay zekâ modeli, farklı CAD araçları ve farklı harness'lar; her yarışmacı
parçayı yalnız yazılı bir spec'ten, kör çizdi.

Bu repo, yayında ekranda görünen her şeyin (NX hariç) paylaşılabilir hâlidir.

## 1. Yarışmacılar (5 config)

Beşinde de tasarımı aynı model yaptı: **Opus 5.5**. Değişen yalnız araç ve harness basamağı.

| Config | Araç | Basamak | Yapımcının elinde |
|---|---|---|---|
| **NX-H2** | Siemens NX 2206 | H2 · uzman harness | NX + kanalın özel harness'i (özel, bu repoda yok) |
| **SW-H1** | SolidWorks | H1 · topluluk MCP'si | COM arayüzü (Python) + SolidWorks için en çok yıldızlı topluluk MCP sunucusu (SolidworksMCP-TS) |
| **SC-H0** | SolidCraft | H0 · çıplak | yalnız aracın komut satırı arayüzü, kod yazarak; aracın kendi MCP'si bu config'te kapalı |
| **B3D-H0** | build123d 0.11.1 | H0 · çıplak | düz Python; MCP yok, skill yok |
| **B3D-H1** | build123d | H1 · topluluk MCP'si | düz Python + en çok yıldızlı build123d MCP'si (build123d-mcp) |

H1 = H0 + topluluk MCP'si (en çok yıldızlı uygun olan; build123d'de ikinci sıradaki build123d-mcp, çünkü birinci olan
agentcad sürüm ve internet bağımlılığı yüzünden çıkarıldı). Yıldız sayıları yayın günü GitHub'dan okundu. Kurulum rehberleri ve linkler: [tools/](../tools/).

## 2. Parçalar

- **45 katalog tarzı parça planlandı**, üç seviyede: 9 şekil, 22 zor, 14 çok zor. Zorluk beş config'e dengeli
  dağıtıldı; plana göre her config 9 farklı parça alacak, her parça yalnız bir config'te, tek tekrarla koşulacaktı
  (yayında kullanım hakkı dolmasın, çeşitlilik olsun diye).
- Yayın bittiğinde **11 parça** koşulmuştu. P10, P16, P17 ve P19 birden çok istasyonda **kafa kafaya** koşuldu (aynı
  parça birkaç config'e birden verildi).
- Bir parça (çok uzun, tek yüzeyli helisel vida dişi olan bir bilyalı vida) yayından çıkarıldı: bir koşusunun
  puanlanması 2,5–4 saat sürüyordu.
- Spec'ler: [benchmark/specs/](../benchmark/specs/). Orijinal katalog modelleri (STEP / PDF) paylaşılmaz.

## 3. Ekranda görünenler

| Ekran | Ne gösterdi | Repodaki yeri |
|---|---|---|
| **Yayın sayfası** | yarışmacı kartları (araç, basamak, linkler, yıldızlar), 45 parçalık matris ve her hücrenin durumu (bekliyor / koşuyor / bitti + puan) | [panel/](../panel/) |
| **Kontrol paneli** | beş istasyon, her birinin o an çizdiği parça ve sıradaki parçası, makinenin CPU / RAM durumu, "aynı parçada yarış" düğmesi | [panel/](../panel/) |
| **Skor tablosu** | config başına puan, parça başına sonuçlar | [panel/](../panel/), puanlar [benchmark/sonuclar/](../benchmark/sonuclar/) |
| **Araç pencereleri** | SolidWorks ve SolidCraft'ta model kurulurken ekran (yalnız aracın ana penceresi kaydedildi) | — (video yayında) |
| **NX harness** | NX-H2'nin skill'leri ekranda gösterildi | **paylaşılmıyor** (özel) |
| **Bitmiş modeller** | koşuların `final.step`'leri ve native kaynakları | [benchmark/sonuclar/](../benchmark/sonuclar/) (NX-H2 çıktıları hariç) |

## 4. Kurallar (yayında anlatılan)

- **Kör koşu:** yapımcı yalnız `spec.md`'yi görür. Web kapalı, cevap anahtarı kilitli, başka koşular görünmez; her
  araç çağrısı bir guard kancasından geçer. Ayrıntı: [mimari.md](mimari.md) §2.
- **Rubrik ölçümden önce kilitlendi:** her parça aynı betikle, 100 üzerinden ölçülür. Canlı tabloda betiğin ölçtüğü
  85 puan görünür (geometri, tamlık, montaj, özellik, teknik resim); CAD kalitesinin 15 puanı ayrı bir kontrol listesidir.
- **Hizalama yok:** model spec'in istediği global çerçevede kurulmalı; kurulmazsa puan düşer. Neden: [sss.md](sss.md).
- **Aynı anda en çok 5 tasarım** açık. Planlanan kural aynı anda tek `olc.py` idi; canlı yayında `yayin_puanla.py`
  yeterli boş bellek varken (≥ 4 GB) en çok 3 `olc.py`'yi paralel koştu.

## 5. Sonuçlar

Puanların özeti kök [README](../README.md#ilk-sonuçlar)'de, ham puan tablosu ve bitmiş çıktılar
[benchmark/sonuclar/](../benchmark/sonuclar/) altında.
