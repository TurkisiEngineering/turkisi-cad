# Araçlar: kurulum rehberleri

F23 "Agentic CAD Ligi" canlı yayınında kullandığımız her aracı (NX hariç) adım adım kurup Claude Code'a bağlamak ve
bizim düzeneğimizi yeniden kurmak için.

## Harness basamakları

Model her koşuda aynı: **Opus 5.5** (`claude-opus-5-5`, `--effort high`). Değişen yalnız araç × harness.

| Basamak | Yapımcının elinde | Kapalı olan |
|---|---|---|
| **H0** | aracın kendi API'si, kod yazarak (COM / Python / CLI) | her MCP sunucusu, her skill |
| **H1** | H0 + o araç için seçilen topluluk MCP'si | skill'ler |
| **H2** | H1 + uzman skill'ler (harness) | — |

Topluluk MCP'si seçim kuralı: seçim günü (2026-11-11) GitHub'da o araç için en çok yıldızlı MCP; kurulamayan ya da
ligin kurallarına uymayan bir sonrakine bırakılır. Her bileşen bir commit'e sabitlendi ve koşu boyunca güncellenmedi.

## Yayındaki beş config

| Config | Araç | Basamak | Bileşen (sabit sürüm) | Rehber |
|---|---|---|---|---|
| **NX-H2** | Siemens NX 2206 | H2 | kanalın özel NX harness'i (paylaşılmıyor) | [`nx/`](nx/README.md) |
| **SW-H1** | SolidWorks 2024 | H1 | Python + pywin32 COM + [`vespo92/SolidworksMCP-TS`](https://github.com/vespo92/SolidworksMCP-TS/tree/ea5539948b816cd34571a4eda00a3a93f4bd86bb) @ `ea55399` (3.1.3) | [`solidworks/`](solidworks/README.md) |
| **SC-H0** | SolidCraft 0.30.1 | H0 | `solidcraft-cli` ([`tangency-labs/solidcraft`](https://github.com/tangency-labs/solidcraft/releases/tag/v0.30.1) @ `8e2b0cd`) | [`solidcraft/`](solidcraft/README.md) |
| **B3D-H0** | build123d 0.11.1 | H0 | düz Python | [`build123d/`](build123d/README.md) |
| **B3D-H1** | build123d 0.11.1 | H1 | + [`pzfreo/build123d-mcp`](https://github.com/pzfreo/build123d-mcp/tree/49023cd809092daa10dea0e9648a87006591d1f1) @ `49023cd` (0.3.92.dev0) | [`build123d/`](build123d/README.md) |

Bütün config'lerin ortak parçası Claude Code'dur: kurulum, giriş, MCP bağlama ve kilitli kör koşu
[`claude-code/`](claude-code/README.md) rehberinde.

| Ortak bileşen | Sürüm |
|---|---|
| Claude Code | 2.1.322 |
| Yapımcı modeli | Opus 5.5 (`claude-opus-5-5`), `--effort high` |
| Lead (orkestra şefi) modeli | Fable 5.2 (`claude-fable-5-2`) |
| Node.js | v24.15.0 |
| Python | 3.13.13 |

## Bilmeniz gereken iki şey

- **MCP bağlı olması, kullanıldığı anlamına gelmiyor.** SW-H1 koşularının hiçbirinde, B3D-H1 koşularının da biri
  hariç hepsinde Opus 5.5 MCP araçlarını çağırmadı; aracın API'sine doğrudan kod yazdı. Ayrıntı ilgili rehberlerde.
- **H2 yalnız NX'te var.** Öteki araçlar için bir uzman harness yok; karşılaştırma bunu açıkça söyler.

Koşu düzeneğinin kendisi (başlatıcı, guard, istemler) [`../benchmark/kosu/`](../benchmark/kosu/) klasöründe.
