# Koşu matrisi (planlanan tam deney)

Model sabit: **Opus 5.5** (her yapımcı oturumu). Değişen: araç × harness.

> Bu, F23 için planlanan tam deneyin matrisidir. Yayında koşan bölüm `YAYIN_MATRISI.md`'dir; Faz 1 / Faz 2 henüz
> koşmadı.

## 1. Harness basamakları (bütün araçlarda aynı tanım)

| Basamak | Yapımcının elinde | Kapalı olan |
|---|---|---|
| **H0 · çıplak** | aracın kendi API'si, kod yazarak (journal / COM / Python / CLI); aracın kurulu resmi belgeleri | her MCP sunucusu, her skill |
| **H1 · topluluk MCP'si** | H0 + o aracın seçilen MCP sunucusu (ikisini birlikte kullanabilir) | skill'ler |
| **H2 · uzman harness** | H1 + uzman skill'leri ve yardımcı kütüphaneler | — |

H2 yalnız NX'te var (Usta'nın özel harness'i, paylaşılmıyor); öteki araçlarda bir uzman harness yok, karşılaştırma bunu
açıkça söyler.

## 2. Config'ler

| ID | Araç | Basamak | Bileşen |
|---|---|---|---|
| NX-H0 / H1 / H2 | Siemens NX 2206 | H0 / H1 / H2 | özel harness, paylaşılmıyor |
| SW-H0 | SolidWorks (kurulu) | H0 | pywin32 ile COM API |
| SW-H1 | SolidWorks | H1 | + `vespo92/SolidworksMCP-TS` (2026-11-11: 252★, SolidWorks MCP'lerinin en çok yıldızlısı) |
| B3D-H0 | build123d 0.11.1 | H0 | düz Python |
| B3D-H1 | build123d | H1 | + `pzfreo/build123d-mcp` (147★, yıldızca ikinci build123d MCP'si; birincisi `agentcad` 212★, build123d sürümü ve internete çıkan araçları yüzünden elendi) |
| B3D-H1b | build123d | H1 | + `agentcad` (yalnız Faz 0 dumanında denendi, sonra elendi) |
| SC-H0 | SolidCraft (kurulu) | H0 | `solidcraft-cli` |
| SC-H1 | SolidCraft | H1 | + SolidCraft'ın kendi MCP'si (`tangency-labs/solidcraft`, `docs/mcp.md`) |

Seçim kuralı: her araç için GitHub'da en çok yıldızlı MCP, Faz 0 günü yeniden bakılır; yıldız sayısı, commit hash'i ve
kurulum adımı kayda yazılır. Kurulamayan ya da duman testini geçemeyen bileşen için bir sonraki yıldızlıya geçilir.
Üçüncü taraf MCP kodları bu repoya kopyalanmaz; kurulum `tools/` altında anlatılır.

## 3. Çekirdek-9 parça

| Kod | Parça | Seviye | Neyi ölçer |
|---|---|---|---|
| P1 | İç düz dişli, m0.5, 60 diş | şekil | involüt diş, desen |
| P2 | Döküm krank kolu, ofset kol | şekil | döküm biçimi, yuvarlatmalar |
| P3 | Plastik rulman koruma kapağı | şekil | ince kabuk |
| P4 | Plastik elektronik kutusu | zor | kabuk + kapak, iki parçalı plastik |
| P5 | Döner rot başı | zor | tutsak küre, diş |
| P6 | İki cıvatalı flanşlı rulman yatağı | zor | döküm gövde + rulman montajı |
| P7 | Kollu tezgah presi | çok zor | 25 gövde, kremayer |
| P8 | Havalı mengene (açık kol) | çok zor | mekanizma, 13 gövde |
| P9 | Konumlama kızağı | çok zor | kılavuzlu montaj, 12 gövde |

Kalan 36 parça "genişletilmiş lig"dir (P10–P45). Spec'ler `benchmark/specs/` altında.

## 4. Koşu sayıları (plan)

| Faz | Hesap | Koşu |
|---|---|---|
| 0 · duman testi | config × kalibrasyon parçası P0 (puana girmez) | 9 |
| 1 · A görevi | 9 config × 9 parça × 2 tekrar | 162 |
| 1 · üçüncü tekrar | iki tekrar arasında fark > 10 puan olan hücreler | değişken |
| 2 · B ve C | Faz 1'in ilk 4 config'i × 9 parça × (B + C) | 72 |
| **Toplam (planlı)** | | **243** |

Görevler: **A** spec'ten kör yapım; **B** teknik resim + fotoğraftan yapım; **C** önceki modele değişiklik uygulama.

## 5. Bütçe, sıra, kayıt

- **Süre tavanı (duvar saati):** şekil 45 dk, zor 90 dk, çok zor 180 dk. Tavanda oturum durdurulur; o ana kadarki
  çıktı puanlanır, koşu `tavan` diye işaretlenir.
- **Token:** tavan yok, her koşunun girdi / çıktı / önbellek token'ı ve $ karşılığı kaydedilir (oturum kullanım verisi).
- **İnsan müdahalesi:** sıfır. Yapımcı soru sorarsa cevap verilmez, "spec'teki bilgiyle devam et" denir; bu da kayda girer.
  Biri elle bir şey düzeltirse koşu `yardimli` olur ve liderlik tablosundan çıkar.
- **Sıra:** aynı parçanın config'leri art arda değil, karışık sırayla koşar (saat / makine yükü etkisi dağılsın).
- **Tekrar:** iki tekrar aynı paketle, taze oturumla. Medyan tabloya, ikisi de sonuç dosyasına girer.
- **Kayıt:** her koşu bir satır, `kayit/kosu_listesi.csv`:
  `run_id, faz, config, parca, gorev, tekrar, basla, bitis, sure_dk, token_in, token_out, token_cache, usd, tool_cagri, cokme, durum(tamam|tavan|cokme|yardimli), not`.
- **run_id** rastgele (`r` + 6 hane); config ile eşleme yalnız `kayit/kosu_esleme.csv`'de, puanlayıcı bu dosyayı göremez.

## 6. İş klasörü düzeni (`<IS_KOKU>`, `TCAD_IS_KOKU`)

```
paketler/P1/A/spec.md                 # yapımcının gördüğü tek şey (A)
paketler/P1/B/cizim.pdf, foto_1.png…  # B (dosya adları nötr)
paketler/P1/C/degisiklik.md           # C (değişiklik tablosu, yapımcıya giden kısım)
paketler/P1/_gizli/                   # yalnız lead + puanlayıcı: hedef tablosu, özellik listesi, kaynak.json
kosular/<run_id>/                     # yapımcının çalışma klasörü; dışına yazamaz
oturum/<run_id>/                      # kos.py'nin yazdığı settings.json, mcp.json, brif.md, meta.json
puan/<run_id>/                        # puanlayıcı çıktısı: olcum.json, olcum.md
kayit/                                # kosu_listesi.csv, kosu_esleme.csv, guard.log, akis/*.jsonl
sonuc/                                # yayin_puan.csv
film/ekran/                           # SW / SC koşularının ekran kayıtları
```

## 7. Yapımcının teslim etmesi gereken (her araçta aynı)

`kosular/<run_id>/teslim/` altında:

1. `final.step`: bütün gövdeler, **spec'in global çerçevesinde**, birimi spec'teki gibi (AP214). Montajsa tek dosyada hepsi.
2. Native kaynak: SolidWorks `.SLDPRT` / `.SLDASM` + makro ya da betik; build123d `.py`; SolidCraft native dosya +
   betik / komut dizisi.
3. `yeniden_kur.md`: temiz bir kopyada modeli sıfırdan yeniden üreten tek komut ya da adım listesi.
4. `parametreler.md`: isimli parametrelerin listesi (ad → değer → hangi özellik).
5. `build_log.md`: ne yapıldı, nerede takıldı, neyi bilerek basitleştirdi.

Teslim klasörü eksikse puanlayıcı bulduğunu puanlar; eksik kalemler Tamlık'tan düşer.
