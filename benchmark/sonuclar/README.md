# Sonuçlar (`benchmark/sonuclar/`)

F23 "Agentic CAD Ligi" canlı yayınının (2026-11-11) puanları ve kör yapımcıların teslim ettiği bitmiş dosyalar.
Her koşu taze bir Opus 5.5 oturumudur; parçayı yalnız `benchmark/specs/<paket>/spec.md`'den, internete ve orijinal
modele erişmeden kurdu (bkz. `benchmark/kosu/KOR_KOSU.md`).

## Dosyalar

| Yol | İçerik |
|---|---|
| `puanlar.csv` | her koşu bir satır: puan (§1-§5, 85 üzerinden) ve alt puanlar, süre, token, $ maliyet, araç çağrısı, guard red sayısı, dosyaların yeri |
| `kosular/<config>/<P##-parca>_<run_id>/` | o koşunun teslim klasörü (NX-H2 hariç) |

### `puanlar.csv` sütunları

| Sütun | Anlam |
|---|---|
| `faz` | `yayin` = canlı yayın koşusu; `0 (duman)` = yayından önce her config'in kalibrasyon levhasıyla duman testi (puana girmez) |
| `paket` | parça kodu, `benchmark/specs/` klasörleriyle aynı biçimde (`P00`–`P45`) |
| `durum` | `tamam` / `tavan` (süre tavanında durduruldu) / `cokme` |
| `puan_85` | `olc.py`'nin STEP üzerinden, araçtan habersiz verdiği puan (§1-§5). §6 CAD kalitesi (15) ayrı, burada yok |
| `geometri` | §1: tek gövdeli parçada 50, montajda 40 üzerinden |
| `tamlik_10`, `montaj_10`, `ozellik_20`, `resim_5` | §2-§5 (`montaj` yalnız `montajli = 1` parçalarda puanlanır) |
| `sure_dk` | duvar saati süresi |
| `token_in`, `token_out`, `token_cache` | oturumun girdi / çıktı / önbellek (okuma + yazma) token'ı |
| `usd` | Claude Code'un oturum sonunda bildirdiği $ maliyeti |
| `arac_cagri` | yapımcının araç çağrısı sayısı |
| `guard_red` | guard'ın reddettiği çağrı sayısı (deneme kendisi veridir; hiçbir yasak geçmedi) |
| `dosyalar` | teslim klasörünün yolu; NX-H2 için `özel (NX harness)` |

Rubrik ve ölçüm kodu: `benchmark/degerlendirme/`.

## Liderlik tablosu (canlı yayın, `puan_85` ortalaması)

Yayında config'ler çoğunlukla farklı parçaları çizdi; bu yüzden sıralama seviye başına ortalamayla okunur. Parantez
içi koşu sayısıdır. Yayın, her config'in 9 parçasından yalnız bir kısmı bitmişken kapandı.

| Config | Koşu | Şekil | Zor | Çok zor | Hepsi | Toplam süre (dk) | Toplam $ |
|---|---|---|---|---|---|---|---|
| B3D-H0 · build123d, düz Python | 5 | 84,40 (3) | 84,32 (1) | 84,91 (1) | **84,49** | 37,7 | 6,32 |
| SW-H1 · SolidWorks + SolidworksMCP-TS | 6 | 84,35 (4) | 80,93 (2) | – | **83,21** | 115,5 | 13,48 |
| NX-H2 · NX + özel harness | 6 | 84,50 (4) | 77,72 (2) | – | **82,24** | 73,0 | 16,84 |
| B3D-H1 · build123d + build123d-mcp | 5 | 57,24 (3) | 84,13 (2) | – | **68,00** | 58,5 | 5,93 |
| SC-H0 · SolidCraft CLI | 4 | 46,42 (3) | 77,76 (1) | – | **54,25** | 144,4 | 9,64 |

Okurken:

- B3D-H1'in şekil ortalamasını tek bir koşu düşürüyor: P17 kanca anahtar (r036690) 3,5 puan; yapımcı "TESLIM HAZIR"
  dedi ama geometri orijinalle örtüşmedi (geometri 0). Dosyaları olduğu gibi duruyor.
- SC-H0'ın şekil ortalamasında P10 tırtıllı topuz (r772182) 45 dakikalık tavana takıldı, `final.step` yok, 0 puan.
  Süreç tavanda kapatıldığı için o koşunun token / $ verisi yazılamadı (0 görünüyor).
- NX-H2 Usta'nın özel harness'idir; puanları yayında gösterildiği için tabloda, dosyaları repoda yok.
- **Config adı kurulumu anlatır, davranışı değil:** SW-H1'in 7 koşusunun (6 yayın + 1 duman) hiçbirinde yapımcı
  SolidWorks MCP aracı çağırmadı, hepsi pywin32 ile COM kodu yazdı; B3D-H1 de MCP'yi 6 koşudan yalnız 1'inde kullandı.

### Aynı parçada kafa kafaya (yayında parça birden çok istasyona verildi; iptal ve yardımlı koşular hariç)

| Parça | B3D-H0 | B3D-H1 | SW-H1 | SC-H0 | NX-H2 |
|---|---|---|---|---|---|
| P10 tırtıllı topuz (şekil, montaj) | 84,32 · 9,8 dk | 84,32 · 13,2 dk | 84,72 · 12,9 dk | 0 · tavan | 84,86 · 28,0 dk |
| P16 konik dişli (şekil) | 83,89 · 2,2 dk | 83,89 · 2,3 dk | 85,00 · 7,8 dk | – (yardımlı, r620023) | 83,89 · 5,3 dk |
| P17 kanca anahtar (şekil) | 85,00 · 3,7 dk | 3,50 · 2,7 dk | 82,69 · 13,6 dk | 85,00 · 18,5 dk | 84,23 · 6,1 dk |
| P19 döner tekerlek (zor, montaj) | 84,32 · 13,1 dk | 84,06 · 11,3 dk | 82,12 · 43,3 dk | 77,76 · 53,1 dk | 83,37 · 11,7 dk |

## Teslim klasörleri

Her klasör yapımcının `teslim/` klasörünün kopyasıdır. Metin dosyalarında yerel yollar `<KOSU_KOKU>` gibi yer
tutuculara çevrildi (yalnız 1 dosyada 1 yol vardı); geometri ve kod değiştirilmedi.

| Dosya | Ne | Nasıl açılır |
|---|---|---|
| `final.step` | puanlanan geometri, bütün gövdeler tek dosyada, spec'in çerçevesinde (AP214; SolidCraft yayın koşularında aracın kendi AP242 çıktısı, iki SolidCraft duman koşusunda başlık elle AP214'e çevrildi) | herhangi bir CAD (FreeCAD, SolidWorks, Fusion, Onshape, NX), ya da `build123d`: `import_step("final.step")` |
| `*.py` (build123d) | modeli sıfırdan üreten betik | `pip install build123d==0.11.1`, sonra `yeniden_kur.md`'deki komut (çoğunda `python <betik>.py`) `final.step`'i yeniden yazar |
| `*.SLDPRT` / `*.SLDASM` | SolidWorks native parça / montaj (özellik ağacıyla) | SolidWorks (kayıttaki sürüm ya da daha yenisi); montajı açmadan önce bütün klasörü birlikte kopyalayın, SolidWorks aynı klasördeki parçaları bulur. Ayrıntı: klasördeki `SOLIDWORKS_NATIVE_NOTU.md` |
| `*.py` (SolidWorks, `betikler/`, `scripts/`) | SolidWorks COM (pywin32) betikleri | Windows + SolidWorks + `pip install pywin32`; `yeniden_kur.md`'deki sırayla |
| `*.sc` | SolidCraft belgesi (zip kapsayıcı) | SolidCraft ile aç; komut dizisi `*_build.json` / `*_script.json` ile `solidcraft-cli` yeniden kurar |
| `*.json` | SolidCraft komut dizileri, yapımcının kendi ölçüm çıktıları | metin düzenleyici |
| `*.png` | yapımcının kendi kontrol görüntüleri (yalnız bazı koşularda) | resim görüntüleyici |
| `yeniden_kur.md` | temiz kopyada modeli yeniden üretme adımları | — |
| `parametreler.md` | isimli parametreler: ad → değer → özellik | — |
| `build_log.md` | yapımcının günlüğü: ne yaptı, nerede takıldı, neyi basitleştirdi, kendi ölçümü | — |
| `SOLIDWORKS_NATIVE_NOTU.md` | SolidWorks koşularında native dosyaların nasıl açılacağı | — |

**SolidWorks native dosyaları:** 6 yayın koşusunun 24 `.SLDPRT` / `.SLDASM` dosyası değiştirilmeden kondu. SolidWorks
her kayıtta dosyanın içine kayıt yolunu ve kaydeden kullanıcıyı yazar; bunlar geometriyi etkilemez. İki Faz 0 duman
koşusunun (SW-H0 r106866, SW-H1 r714102) `.SLDPRT`'si konmadı: SolidWorks'ün dosyaya yazdığı geçmişte bilgisayardaki
ilgisiz bir proje klasörünün adı geçiyor. O klasörlerde `final.step` ve modeli sıfırdan kuran betik var.

## Dahil edilen koşular

| Config | Parça | run_id | Puan |
|---|---|---|---|
| B3D-H0 | P09 konumlama kızağı (çok zor) | r262151 | 84,91 |
| B3D-H0 | P10 tırtıllı topuz | r018668 | 84,32 |
| B3D-H0 | P16 konik dişli | r007208 | 83,89 |
| B3D-H0 | P17 kanca anahtar | r073767 | 85,00 |
| B3D-H0 | P19 döner tekerlek | r024679 | 84,32 |
| B3D-H1 | P05 rotil başı | r820448 | 84,21 |
| B3D-H1 | P10 tırtıllı topuz | r208322 | 84,32 |
| B3D-H1 | P16 konik dişli | r851117 | 83,89 |
| B3D-H1 | P17 kanca anahtar | r036690 | 3,50 |
| B3D-H1 | P19 döner tekerlek | r882582 | 84,06 |
| SW-H1 | P02 krank kolu | r652075 | 85,00 |
| SW-H1 | P04 ABS elektronik kutusu | r518253 | 79,74 |
| SW-H1 | P10 tırtıllı topuz | r935356 | 84,72 |
| SW-H1 | P16 konik dişli | r571844 | 85,00 |
| SW-H1 | P17 kanca anahtar | r934906 | 82,69 |
| SW-H1 | P19 döner tekerlek | r456183 | 82,12 |
| SC-H0 | P03 rulman koruma kapağı | r935818 | 54,25 |
| SC-H0 | P17 kanca anahtar | r347027 | 85,00 |
| SC-H0 | P19 döner tekerlek | r102032 | 77,76 |

Kalibrasyon örneği olarak Faz 0 duman koşuları da var (P00 kalibrasyon levhası, puansız): B3D-H0 r719476, B3D-H1
r835129, B3D-H1b r315784, SC-H0 r172610, SC-H1 r333376, SW-H0 r106866, SW-H1 r714102.

Dahil edilmeyenler: bütün NX-H2 koşuları (özel harness; puanlar `puanlar.csv`'de), SC-H0 P10 r772182 (tavan, teslim
boş), SC-H0 P16 r620023 (yardımlı: yayında elle durduruldu, `final.step` yok, puanlanmadı), sızıntı (guard) testleri
(model yok).
