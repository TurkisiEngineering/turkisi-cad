<p align="center">
  <img src="docs/img/banner.png" alt="F23 · Agentic CAD Ligi: 4 CAD, 5 yarışmacı, 45 parça" width="100%">
</p>

<h1 align="center">turkisi-cad · Agentic CAD Ligi (F23)</h1>

<p align="center">
  <b>Aynı yapay zekâ modeli, farklı CAD araçları: hangisi gerçekten çiziyor?</b>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=b4b8olf0IgI"><img src="https://img.shields.io/badge/YouTube-yayın_kaydı-e11d48?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube yayın kaydı"></a>
  <img src="https://img.shields.io/badge/parça-45-e6ff2e?style=for-the-badge&labelColor=121a26" alt="45 parça">
  <img src="https://img.shields.io/badge/config-5-22d3ee?style=for-the-badge&labelColor=121a26" alt="5 config">
  <img src="https://img.shields.io/badge/model-Opus_5.5-3461a0?style=for-the-badge&labelColor=121a26" alt="Opus 5.5">
  <a href="LICENSE"><img src="https://img.shields.io/badge/lisans-MIT-94a3b8?style=for-the-badge&labelColor=121a26" alt="MIT"></a>
</p>

<p align="center">
  <a href="#f23-nedir">F23 nedir?</a> ·
  <a href="#45-parça">45 parça</a> ·
  <a href="#i̇lk-sonuçlar">Sonuçlar</a> ·
  <a href="#hızlı-başlangıç-kendi-harnessını-bir-specte-dene">Hızlı başlangıç</a> ·
  <a href="#kanal-ve-yayın">Yayın</a> ·
  <a href="#klasörler">Klasörler</a>
</p>

---

Bu repo, Türkişi Engineering'in **F23 · Agentic CAD Ligi** canlı yayınının açık rehberidir. Yayında gösterilen her şey
burada: spec'ler, ölçüm kodu, koşu düzeneği, kontrol paneli, kurulum rehberleri, bitmiş modeller ve NX dışı CAD
skill'leri. Tek istisna Türkişi'nin özel **NX harness'i** ([aşağıya bakın](#nx-hariç)).

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

## 45 parça

Yapımcı ajan bu parçaların hiçbirini görmez; yalnız yazılı `spec.md`'sini okur. Görsele tıklayınca parçanın spec
klasörü açılır. **9** şekil · **22** zor · **14** çok zor. ⭐ = canlı yayındaki en iyi geçerli koşu (85 üzerinden);
yıldızı olmayan parçalar yayında koşulmadı.

<table>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P01-ic-disli-60-dis/"><img src="docs/img/parcalar/P01.webp" alt="P01 iç dişli, 60 diş" width="170"></a><br><sub><b>P01</b> · iç dişli, 60 diş<br>🟢 şekil<br>⭐ 85,00 · NX-H2</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P02-krank-kolu/"><img src="docs/img/parcalar/P02.webp" alt="P02 krank kolu" width="170"></a><br><sub><b>P02</b> · krank kolu<br>🟢 şekil<br>⭐ 85,00 · SW-H1</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P03-rulman-koruma-kapagi/"><img src="docs/img/parcalar/P03.webp" alt="P03 rulman koruma kapağı" width="170"></a><br><sub><b>P03</b> · rulman koruma kapağı<br>🟢 şekil<br>⭐ 54,25 · SC-H0</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P04-abs-elektronik-kutusu/"><img src="docs/img/parcalar/P04.webp" alt="P04 ABS elektronik kutusu" width="170"></a><br><sub><b>P04</b> · ABS elektronik kutusu<br>🟠 zor<br>⭐ 79,74 · SW-H1</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P05-rotil-basi/"><img src="docs/img/parcalar/P05.webp" alt="P05 rotil başı" width="170"></a><br><sub><b>P05</b> · rotil başı<br>🟠 zor<br>⭐ 84,21 · B3D-H1</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P06-flansli-rulman-yatagi/"><img src="docs/img/parcalar/P06.webp" alt="P06 flanşlı rulman yatağı" width="170"></a><br><sub><b>P06</b> · flanşlı rulman yatağı<br>🟠 zor<br>⭐ 72,07 · NX-H2</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P07-kollu-pres/"><img src="docs/img/parcalar/P07.webp" alt="P07 kollu pres" width="170"></a><br><sub><b>P07</b> · kollu pres<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P08-havali-mengene/"><img src="docs/img/parcalar/P08.webp" alt="P08 havalı mengene" width="170"></a><br><sub><b>P08</b> · havalı mengene<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P09-konumlama-kizagi/"><img src="docs/img/parcalar/P09.webp" alt="P09 konumlama kızağı" width="170"></a><br><sub><b>P09</b> · konumlama kızağı<br>🔴 çok zor<br>⭐ 84,91 · B3D-H0</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P10-tirtilli-topuz/"><img src="docs/img/parcalar/P10.webp" alt="P10 tırtıllı topuz" width="170"></a><br><sub><b>P10</b> · tırtıllı topuz<br>🟢 şekil<br>⭐ 84,86 · NX-H2</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P11-sonsuz-vida/"><img src="docs/img/parcalar/P11.webp" alt="P11 sonsuz vida" width="170"></a><br><sub><b>P11</b> · sonsuz vida<br>🟢 şekil</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P12-capraz-helis-disli/"><img src="docs/img/parcalar/P12.webp" alt="P12 çapraz helis dişli" width="170"></a><br><sub><b>P12</b> · çapraz helis dişli<br>🟢 şekil</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P13-sogutma-plakasi/"><img src="docs/img/parcalar/P13.webp" alt="P13 soğutma plakası" width="170"></a><br><sub><b>P13</b> · soğutma plakası<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P14-bilyali-vida/"><img src="docs/img/parcalar/P14.webp" alt="P14 bilyalı vida" width="170"></a><br><sub><b>P14</b> · bilyalı vida<br>🟢 şekil</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P15-havali-reduktor-motor/"><img src="docs/img/parcalar/P15.webp" alt="P15 havalı redüktör motor" width="170"></a><br><sub><b>P15</b> · havalı redüktör motor<br>🟠 zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P16-konik-disli/"><img src="docs/img/parcalar/P16.webp" alt="P16 konik dişli" width="170"></a><br><sub><b>P16</b> · konik dişli<br>🟢 şekil<br>⭐ 85,00 · SW-H1</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P17-kanca-anahtar/"><img src="docs/img/parcalar/P17.webp" alt="P17 kanca anahtar" width="170"></a><br><sub><b>P17</b> · kanca anahtar<br>🟢 şekil<br>⭐ 85,00 · B3D-H0 / SC-H0</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P18-talas-siperi/"><img src="docs/img/parcalar/P18.webp" alt="P18 talaş siperi" width="170"></a><br><sub><b>P18</b> · talaş siperi<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P19-doner-tekerlek/"><img src="docs/img/parcalar/P19.webp" alt="P19 döner tekerlek" width="170"></a><br><sub><b>P19</b> · döner tekerlek<br>🟠 zor<br>⭐ 84,32 · B3D-H0</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P20-darbe-valfi/"><img src="docs/img/parcalar/P20.webp" alt="P20 darbe valfi" width="170"></a><br><sub><b>P20</b> · darbe valfi<br>🟠 zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P21-acili-kardan/"><img src="docs/img/parcalar/P21.webp" alt="P21 açılı kardan" width="170"></a><br><sub><b>P21</b> · açılı kardan<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P22-raf-konsolu/"><img src="docs/img/parcalar/P22.webp" alt="P22 raf konsolu" width="170"></a><br><sub><b>P22</b> · raf konsolu<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P23-kilit-cift-baglantili/"><img src="docs/img/parcalar/P23.webp" alt="P23 kilit (çift bağlantılı)" width="170"></a><br><sub><b>P23</b> · kilit (çift bağlantılı)<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P24-ayarli-kol/"><img src="docs/img/parcalar/P24.webp" alt="P24 ayarlı kol" width="170"></a><br><sub><b>P24</b> · ayarlı kol<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P25-gaz-debimetresi/"><img src="docs/img/parcalar/P25.webp" alt="P25 gaz debimetresi" width="170"></a><br><sub><b>P25</b> · gaz debimetresi<br>🟠 zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P26-igne-valf/"><img src="docs/img/parcalar/P26.webp" alt="P26 iğne valf" width="170"></a><br><sub><b>P26</b> · iğne valf<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P27-gergi/"><img src="docs/img/parcalar/P27.webp" alt="P27 gergi" width="170"></a><br><sub><b>P27</b> · gergi<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P28-filtre-govdesi/"><img src="docs/img/parcalar/P28.webp" alt="P28 filtre gövdesi" width="170"></a><br><sub><b>P28</b> · filtre gövdesi<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P29-kaldirma-halkasi/"><img src="docs/img/parcalar/P29.webp" alt="P29 kaldırma halkası" width="170"></a><br><sub><b>P29</b> · kaldırma halkası<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P30-gaz-dolum-valfi/"><img src="docs/img/parcalar/P30.webp" alt="P30 gaz dolum valfi" width="170"></a><br><sub><b>P30</b> · gaz dolum valfi<br>🟠 zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P31-manometre/"><img src="docs/img/parcalar/P31.webp" alt="P31 manometre" width="170"></a><br><sub><b>P31</b> · manometre<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P32-sogutma-fani/"><img src="docs/img/parcalar/P32.webp" alt="P32 soğutma fanı" width="170"></a><br><sub><b>P32</b> · soğutma fanı<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P33-doner-mandal/"><img src="docs/img/parcalar/P33.webp" alt="P33 döner mandal" width="170"></a><br><sub><b>P33</b> · döner mandal<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P34-hava-silindiri/"><img src="docs/img/parcalar/P34.webp" alt="P34 hava silindiri" width="170"></a><br><sub><b>P34</b> · hava silindiri<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P35-disli-pompa/"><img src="docs/img/parcalar/P35.webp" alt="P35 dişli pompa" width="170"></a><br><sub><b>P35</b> · dişli pompa<br>🔴 çok zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P36-vidali-kriko/"><img src="docs/img/parcalar/P36.webp" alt="P36 vidalı kriko" width="170"></a><br><sub><b>P36</b> · vidalı kriko<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P37-elektronik-kabin-rafi/"><img src="docs/img/parcalar/P37.webp" alt="P37 elektronik kabin rafı" width="170"></a><br><sub><b>P37</b> · elektronik kabin rafı<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P38-ac-reduktor-motor/"><img src="docs/img/parcalar/P38.webp" alt="P38 AC redüktör motor" width="170"></a><br><sub><b>P38</b> · AC redüktör motor<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P39-termometre/"><img src="docs/img/parcalar/P39.webp" alt="P39 termometre" width="170"></a><br><sub><b>P39</b> · termometre<br>🟠 zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P40-manyetik-tork-sinirlayici/"><img src="docs/img/parcalar/P40.webp" alt="P40 manyetik tork sınırlayıcı" width="170"></a><br><sub><b>P40</b> · manyetik tork sınırlayıcı<br>🔴 çok zor</sub></td>
</tr>
<tr>
<td align="center" width="20%"><a href="benchmark/specs/P41-kavrama-fren/"><img src="docs/img/parcalar/P41.webp" alt="P41 kavrama-fren" width="170"></a><br><sub><b>P41</b> · kavrama-fren<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P42-kiris-arabasi/"><img src="docs/img/parcalar/P42.webp" alt="P42 kiriş arabası" width="170"></a><br><sub><b>P42</b> · kiriş arabası<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P43-platform-merdiven/"><img src="docs/img/parcalar/P43.webp" alt="P43 platform merdiven" width="170"></a><br><sub><b>P43</b> · platform merdiven<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P44-bilyali-vida-mil/"><img src="docs/img/parcalar/P44.webp" alt="P44 bilyalı vida-mil" width="170"></a><br><sub><b>P44</b> · bilyalı vida-mil<br>🔴 çok zor</sub></td>
<td align="center" width="20%"><a href="benchmark/specs/P45-su-sogutmali-isi-emici/"><img src="docs/img/parcalar/P45.webp" alt="P45 su soğutmalı ısı emici" width="170"></a><br><sub><b>P45</b> · su soğutmalı ısı emici<br>🔴 çok zor</sub></td>
</tr>
</table>

<sub>Kartlar <a href="panel/varlik.js"><code>panel/varlik.js</code></a>'teki render'lardan
<a href="docs/img/galeri_uret.py"><code>docs/img/galeri_uret.py</code></a> ile üretilir.</sub>

## Kanal ve yayın

**Türkişi Engineering**, agentic CAD ve mühendislik üzerine bir YouTube kanalı. F23 canlı yayını **11 Kasım 2026**'da
yapıldı: beş istasyon aynı anda parça çizdi, puanlar canlı tabloya düştü. Yayın kaydı:
**[YouTube'da izle](https://www.youtube.com/watch?v=b4b8olf0IgI)**. Yayında ne gösterildiği:
[docs/yayin.md](docs/yayin.md).

<table>
<tr>
<td width="50%"><img src="panel/ekran/yayin_sayfasi.png" alt="Yayın sayfası"><br><sub>Yayın sayfası</sub></td>
<td width="50%"><img src="panel/ekran/skor.png" alt="Canlı skor tablosu"><br><sub>Canlı skor tablosu</sub></td>
</tr>
<tr>
<td width="50%"><img src="panel/ekran/panel_kosuyor.png" alt="Kontrol paneli, koşu sırasında"><br><sub>Kontrol paneli, koşu sırasında</sub></td>
<td width="50%"><img src="panel/ekran/parca_secici.png" alt="Parça seçici"><br><sub>Parça seçici</sub></td>
</tr>
</table>

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
