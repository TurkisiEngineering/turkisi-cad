# SolidCraft: SC-H0 (`solidcraft-cli`)

| Config | Yapımcının elinde |
|---|---|
| **SC-H0** | SolidCraft'ın komut satırı aracı `solidcraft-cli.exe` (ajan JSON komut dizisi yazıp oynatır) |
| SC-H1 | SC-H0 + SolidCraft'ın kendi MCP sunucusu (`solidcraft-cli mcp --headless`); yalnız duman testinde koştu |

Yayında **SC-H0** koştu. Kaynak: [`tangency-labs/solidcraft`](https://github.com/tangency-labs/solidcraft/tree/8e2b0cd60d14b4152b12b8f1fdb2bcfdcd8c52f4).

## 1. Kurulum

Kullandığımız sürüm: **0.30.1** (o günün son kararlı sürümü), etiket `v0.30.1` =
commit [`8e2b0cd60d14b4152b12b8f1fdb2bcfdcd8c52f4`](https://github.com/tangency-labs/solidcraft/commit/8e2b0cd60d14b4152b12b8f1fdb2bcfdcd8c52f4).

1. Sürüm sayfasını açın: https://github.com/tangency-labs/solidcraft/releases/tag/v0.30.1
2. Windows için `solidcraft-0.30.1-windows-x64.msi` (kurucu) ya da `solidcraft-0.30.1-windows-x64-portable.zip`
   (taşınabilir) paketini indirin. Sayfada başka işletim sistemleri için paketler de var.
3. Kurun. Kurulum klasöründe üç program olur: `solidcraft.exe` (arayüz), `solidcraft-cli.exe` (komut satırı),
   `solvecraft-cli.exe`.
4. Deneyin:

```bash
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" --version     # solidcraft-cli 0.30.1
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" --help
```

Not: Bizim makinemizde SolidCraft hazır kuruluydu; hangi paketle (msi / exe / zip) kurulduğunu kayıtlarımızdan
**doğrulayamadık**. Yukarıdaki dosya adları sürüm sayfasından okundu. Koşu boyunca sürüm hiç güncellenmedi. Biz
`solidcraft-cli.exe` dosyasının SHA-256'sını da kaydettik:
`abc39aed92a18ea540bf12ea17552cd974f63313208a0ad1d4468062ae3a6a88`.

## 2. Kurulumu deneyin: örnek komut dizisi

[`ornek/plaka.json`](ornek/plaka.json): 80 × 50 × 8 mm, ortasında Ø12 delik olan bir plaka (isimli parametrelerle).

```bash
cd tools/solidcraft/ornek
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" run plaka.json --save plaka.sc --out plaka.step
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" eval plaka.sc
```

`eval` hacim, alan, ağırlık merkezi, sınır kutusu ve yüz sayısını JSON olarak yazar. Bu örnekte: tek kapalı gövde,
sınır kutusu (−40, −25, 0) – (40, 25, 8), 7 yüz (6 düzlem + 1 silindir). Bunu 0.30.1 ile denedik.

## 3. Yapımcının kullandığı komutlar

Yapımcıya verilen araç cümlesi (koşu brifinden): "SolidCraft (kurulu), `solidcraft-cli.exe` komut satırı aracıyla
modelle. Native: SolidCraft belgesi + komut dizisi / betik."

SC-H0'ın 6 koşusunun (yayında 5 + duman testinde 1) akış kayıtlarında sayılan `solidcraft-cli` alt komutları:

| Alt komut | Kaç kez | Ne için |
|---|---|---|
| `eval` | 74 | betiği, `.sc` belgesini ya da STEP'i ölçmek (hacim, alan, ağırlık merkezi, kutu, yüz) |
| `run` | 62 | JSON komut dizisini oynatıp `.sc` belgesini kaydetmek ve STEP yazmak |
| `commands` | 24 | komut listesini ve parametrelerini öğrenmek (ajanın "belgesi") |
| `--help` | 6 | kullanım |
| `bench-agent` | 5 | aracın kendi örnek ajan betiğini görmek |
| `snapshot` | 4 | modelin PNG görüntüsü (seçenekler: `--view iso`, `--section z=...` vb.) |

Tipik akış (yapımcıların `yeniden_kur.md` dosyalarından):

```bash
# 1) Ajanın yazdığı üretici betik komut dizisini üretir (Python, Node.js, bash + awk: hepsi görüldü)
python gen_script.py parca_build.json

# 2) Modeli sıfırdan kur, belgeyi kaydet, STEP yaz
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" run parca_build.json --save parca.sc --out final.step

# 3) Kontrol
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" eval final.step --json-out olcum.json

# Parametre değiştirmek (belge üzerinde)
"<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" exec parameters.change '{"name":"wall","expression":"0.125"}'
```

Komut dizisi biçimi: `{"commands": [{"command": "...", "params": {...}}, ...]}`. Yapımcıların teslim ettiği beş komut
dizisinde en çok kullanılan komutlar:

| Komut | Kullanım |
|---|---|
| `sketch.line`, `sketch.arc.center_point`, `sketch.arc.three_point`, `sketch.circle.center` | eskiz geometrisi |
| `sketch.create`, `sketch.finish` | eskiz aç / kapat (`plane`, `offset`) |
| `parameters.add` | isimli parametre (`expression`, `comment`) |
| `solid.extrude`, `solid.revolve`, `solid.combine`, `solid.cylinder`, `solid.box` | katı özellikler ve boolean |
| `solid.fillet` | yuvarlatma (kenar, kenar üzerindeki bir noktayla seçilir) |
| `surface.boundary`, `surface.stitch` | yüzeyden katıya |
| `solid.pattern.circular`, `sketch.slot.center_to_center`, `sketch.polygon.circumscribed`, `document.units` | diğer |

## 4. STEP çıktısı

SolidCraft 0.30.1 yalnız **AP242** yazar (`AP242_MANAGED_MODEL_BASED_3D_ENGINEERING_MIM_LF`); `run --out`,
`file.export_step` ve `file.export` için şema seçme parametresi yok (yapımcı `--param-check strict` ile denedi: `schema`,
`protocol`, `ap` anahtarlarının hepsi "unknown key"). Duman testinde iki yapımcı başlığı elle AP214'e çevirdi; geometri
aynı kaldı. Yayın kuralı: **SolidCraft'ın kendi AP242 çıktısı kabul edilir, başlık elle değiştirilmez.**

## 5. Sorun giderme (yapımcıların `build_log.md`'lerinden)

- **Eskiz koordinatları mm'dir.** Belge birimi inç olsa da çıplak sayılar mm okunur. Sayıları parametre ya da
  `"<değer> in"` biçiminde ifade olarak yazın.
- **XZ düzlemindeki eskizde eskiz-y = −Z** (deneme ile bulundu).
- **Boolean çekirdeği tam teğet / çakışık yüzlerde "no result" verir.** Çözüm: kesiciyi çok az büyütmek (ör. 0,0005 in),
  gövdeye az gömmek ya da teğet-sürekli tek bir profil kullanmak. Bir koşuda teğet kırpma, sınır kutusunu bozan sıfır
  alanlı bir yüz parçası bıraktı.
- **Yuvarlatma sınırları:** "the blend is larger than the neighbouring faces", "only straight edges can be blended",
  "the ball doesn't fit". Çok kenarlı yuvarlatmayı taraf taraf ayrı özelliklere bölmek bazen çözdü; eğri kenardaki
  içbükey yuvarlatmalar bazı koşularda hiç kurulamadı ve modelden çıkarıldı.
- `sketch.slot.center_to_center` ve `solid.revolve`'un `{origin, dir}` ekseni ifade kabul etmedi; yuva çizgi + iki
  yayla, eksen eskizde yardımcı çizgiyle çizildi.
- Özellik sırası önemli: bir koni kesimi birleştirmeden sonra yapılınca bozuldu, önce yapılınca temiz çıktı.
- Büyük modellerde `run` dakikalar sürebilir (bir koşuda yaklaşık 5 dk; yuvarlatma ve birleştirmeler yavaş).
- Bir özellik başarısız olursa `run` hiçbir şey yazmaz; `--allow-errors` yine de yazar.

## 6. SC-H1: SolidCraft MCP (yalnız duman testinde)

SolidCraft'ın MCP sunucusu kendi programının içinde. Biz şu tanımla bağladık (21 araç):

```json
{
  "mcpServers": {
    "solidcraft": {
      "type": "stdio",
      "command": "<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe",
      "args": ["mcp", "--headless"],
      "env": {}
    }
  }
}
```

`solidcraft-cli mcp setup --client claude-code` komutu bu kaydı kendisi ekler (aracın `--help` çıktısından; biz
kullanmadık). Duman testindeki tek SC-H1 koşusunda ajan `list_commands`, `describe_command`, `skill_reference`,
`batch`, `open`, `body_topology`, `check_parameters` araçlarını çağırdı. Yayın matrisinde SC-H1 yok.

Aynı tanım dosya olarak: [`ornek/mcp.json`](ornek/mcp.json).

## 7. Ekran kaydı

SolidCraft'ın penceresi görünebildiği için yayında her SC koşusunun ekranı kaydedildi (koşu başlatıcı yapar; kurulumun
parçası değil).
