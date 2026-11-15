# Claude Code: kurulum, MCP bağlama, kör koşu

Bu rehber, F23 "Agentic CAD Ligi" yayınında yapımcı ajanları çalıştıran Claude Code kurulumunu adım adım anlatır.
Bütün CAD araçlarının (SolidWorks, SolidCraft, build123d) ajana bağlandığı yer burasıdır.

## 1. Kurulum

Gereken: Node.js (biz v24.15.0 kullandık) ve npm.

Yayında kullandığımız sürüm sabittir:

```bash
npm i -g @anthropic-ai/claude-code@2.1.322
claude --version        # 2.1.322 (Claude Code)
```

Not: Daha eski bir sürüm (2.1.198) Opus 5.5 modelini desteklemiyordu, bu yüzden 2.1.322'ye geçtik. Daha yeni bir sürüm
büyük olasılıkla da çalışır, ama biz yalnız 2.1.322 ile denedik. Claude Code'un başka kurulum yolları (yerel kurucu,
masaüstü uygulaması) için resmi belgelere bakın: https://docs.claude.com/en/docs/claude-code

## 2. Giriş

```bash
claude
```

İlk açılışta tarayıcıda giriş yapmanızı ister (oturum içinden `/login` ile de olur).

- **Abonelik planı yeterli.** Yapımcı oturumları abonelikle girilmiş Claude Code ile koştu (akış kayıtlarının ilk
  satırında `"apiKeySource": "none"`, yani API anahtarı kullanılmadı).
- **API anahtarı isteğe bağlı.** Anahtarla çalışmak isterseniz `ANTHROPIC_API_KEY` ortam değişkenini kendi
  makinenizde tanımlayın. Anahtarı hiçbir dosyaya, repoya ya da ekran görüntüsüne koymayın.

Koşu kayıtlarında görünen `usd` sütunu, Claude Code'un akış çıktısındaki `total_cost_usd` alanıdır (tahmini API
karşılığı). Abonelikle çalışırken bu tutar faturaya yansımaz; yalnız karşılaştırma için tutulur.

## 3. Kullandığımız modeller

| Rol | Model | Model kimliği | Nasıl |
|---|---|---|---|
| Yapımcı (parçayı kör kuran ajan) | Opus 5.5 | `claude-opus-5-5` | `--model claude-opus-5-5 --effort high` |
| Orkestra şefi (lead: koşuları başlatır, puanlatır, yayını yürütür) | Fable 5.2 | `claude-fable-5-2` | etkileşimli oturum, model seçicisinden |

Model sabittir; ligde değişen yalnız **araç × harness** (bkz. [`../README.md`](../README.md)).

## 4. MCP sunucusu eklemek

İki yol var. İkisi de aynı JSON biçimini kullanır.

**a) Proje dosyası `.mcp.json`** (proje kökünde; projeyi açan herkes görür):

```json
{
  "mcpServers": {
    "build123d": {
      "type": "stdio",
      "command": "<KÖK>/mcp/build123d-mcp/.venv/Scripts/build123d-mcp.exe",
      "args": [],
      "env": {}
    }
  }
}
```

**b) Komut satırından `claude mcp add`:**

```bash
claude mcp add build123d -- "<KÖK>/mcp/build123d-mcp/.venv/Scripts/build123d-mcp.exe"
claude mcp add solidworks -- node "<KÖK>/mcp/SolidworksMCP-TS/dist/index.js"
claude mcp add solidcraft -- "<SOLIDCRAFT_KLASÖRÜ>/solidcraft-cli.exe" mcp --headless
claude mcp list
```

`--scope project` verirseniz kayıt `.mcp.json`'a yazılır; vermezseniz yalnız sizin makinenizde kalır. Bağlantıyı
oturum içinde `/mcp` ile kontrol edebilirsiniz.

Her aracın kendi sunucu tanımı ilgili klasörde: [`../solidworks/`](../solidworks/), [`../solidcraft/`](../solidcraft/),
[`../build123d/`](../build123d/). Yayında kullandığımız tanımların hepsi bir arada:
[`ornek/mcp_tanimlari.json`](ornek/mcp_tanimlari.json).

## 5. Kör headless koşu

Ligde her parça, taze bir Claude Code oturumunda, insan müdahalesi olmadan kurulur. Oturum `claude -p` ile
(etkileşimsiz) açılır ve kilitlenir: yalnız o config'in MCP'sini görür, kullanıcı ayarlarını / eklentilerini /
kancalarını yüklemez, her araç çağrısı bir guard kancasından geçer.

Yayında kullanılan komut (koşu başlatıcımızdan aynen; yollar `<KÖK>` yapıldı):

```bash
cd "<KÖK>/kosular/<run_id>"          # yapımcının tek çalışma klasörü
claude -p \
  --model claude-opus-5-5 --effort high \
  --permission-mode bypassPermissions \
  --setting-sources project \
  --settings "<OTURUM>/settings.json" \
  --mcp-config "<OTURUM>/mcp.json" --strict-mcp-config \
  --output-format stream-json --verbose \
  --disallowedTools WebSearch WebFetch Workflow Artifact DesignSync RemoteTrigger \
      CronCreate CronDelete CronList PushNotification SendMessage ListAgents ScheduleWakeup \
      EnterWorktree ExitWorktree ReportFindings \
      Skill Agent Task \
  --disable-slash-commands \
  < brif.md > akis.jsonl
```

Bayrakların ne işe yaradığı:

| Bayrak | Neden |
|---|---|
| `-p` | etkileşimsiz: istem stdin'den gelir, oturum bitince çıkar |
| `--model claude-opus-5-5 --effort high` | her koşuda aynı model ve aynı düşünme bütçesi |
| `--permission-mode bypassPermissions` | soru sormadan çalışsın (cevap verecek kimse yok); güvenliği izin ekranı değil guard sağlar |
| `--setting-sources project` | kullanıcı ayarları (`~/.claude`), eklentiler ve kancalar yüklenmez; yalnız proje ayarı |
| `--settings <dosya>` | guard kancasını ve `deny` kurallarını bu oturuma verir ([`ornek/settings.json`](ornek/settings.json)) |
| `--mcp-config <dosya>` + `--strict-mcp-config` | yalnız bu dosyadaki MCP sunucuları; makinedeki başka MCP'ler görünmez |
| `--output-format stream-json --verbose` | bütün akış JSON satırları olarak kaydedilir (araç çağrıları, token, süre) |
| `--disallowedTools ...` | web, zamanlayıcı, başka oturumlara mesaj gibi araçlar kapalı |
| `Skill Agent Task` + `--disable-slash-commands` | yalnız H0 ve H1'de: skill ve alt ajan yok (H2'de açık) |

Ek ayrıntılar:

- `settings.json` ve `mcp.json` koşu klasörünün **dışında** durur; yapımcı onları göremez.
- Akış kaydı (`akis.jsonl`) da koşu klasörünün dışına yazılır.
- Süre tavanı koşu başlatıcıda tutulur (şekil 45 dk, zor 90 dk, çok zor 180 dk). Tavan dolunca süreç ağacı durdurulur,
  o ana kadarki teslim puanlanır.
- Koşu başlatıcı Claude Code'un içinden çağrılıyorsa, alt sürecin ortamından `CLAUDECODE` ve `CLAUDE_CODE_SSE*` ile
  başlayan değişkenler çıkarılır; böylece yeni oturum bağımsız açılır.
- PowerShell ile aynı komut: [`ornek/kor_kosu.ps1`](ornek/kor_kosu.ps1).

## 6. PreToolUse guard kancası

Kanca, her araç çağrısından **önce** çalışan bir komuttur. Claude Code çağrının JSON'unu (`tool_name`, `tool_input`,
`session_id`) kancanın stdin'ine verir. Kanca hiçbir şey yazmazsa çağrı geçer; aşağıdaki JSON'u yazarsa reddedilir:

```json
{"hookSpecificOutput": {"hookEventName": "PreToolUse",
  "permissionDecision": "deny",
  "permissionDecisionReason": "Bu işlem bu görevde kapalı (izinli alan dışı)."}}
```

Kancayı `settings.json` bağlar:

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "*", "hooks": [{"type": "command",
        "command": "python -I \"<GUARD_KLASÖRÜ>/guard.py\" --run <run_id> --config SW-H1 --kok \"<KÖK>/kosular/<run_id>\" --log \"<KÖK>/kayit/guard.log\"",
        "timeout": 30}]}
    ]
  },
  "permissions": {"deny": ["WebSearch", "WebFetch"]}
}
```

Guard'ın argümanları (yayındaki koşu başlatıcının yazdığı gibi):

| Argüman | Ne |
|---|---|
| `--run <run_id>` | koşu kimliği (log satırına yazılır) |
| `--config <CONFIG>` | ör. `SW-H1`; hangi MCP'nin açık, skill'in kapalı olduğunu belirler |
| `--kok "<KÖK>/kosular/<run_id>"` | **zorunlu**: yapımcının tek yazma yeri |
| `--log "<KÖK>/kayit/guard.log"` | kararların yazıldığı log (koşu klasörünün dışında) |

`--kok` verilmezse betik her çağrıda argüman hatasıyla (çıkış kodu 2) kapanır ve Claude Code bunu ret sayar: ajan hiçbir
araç kullanamaz. **Guard dosyası (`guard.py`, `kurallar.json`) ve log yapımcının klasörünün dışında durmalı**; içeride
olursa ajan kuralları okuyabilir ya da değiştirebilir.

Bizim guard'ımızın kuralları kısaca:

- web araçları, tarayıcı / ekran araçları, zamanlayıcılar ve başka oturumlarla konuşan araçlar kapalı;
- yalnız o config'in MCP sunucusu açık (ör. SW-H1'de yalnız `mcp__solidworks__*`); H0'da hiç MCP yok;
- H0 ve H1'de `Skill`, `Agent`, `Task` kapalı;
- komut metninde ağ erişimi (`curl`, `wget`, `Invoke-WebRequest`, `pip install`, `npm install`, `npx`, `git clone`,
  `urllib`, `requests.get` ...), üst klasöre çıkma (`..\..`), cevap anahtarının bulunduğu sürücü ve klasör adları,
  parça numaraları reddedilir;
- `Write` / `Edit` yalnız koşunun kendi klasörüne;
- her karar `zaman, oturum, run_id, araç, karar` olarak bir log dosyasına yazılır; kanca hata verirse güvenli tarafta
  kalıp reddeder.

Kanca protokolünü gösteren kısa bir iskelet: [`ornek/guard_iskelet.py`](ornek/guard_iskelet.py). Yayında kullanılan
tam guard ve koşu başlatıcı [`../../benchmark/kosu/`](../../benchmark/kosu/) klasöründe.

Guard'ı her koşudan önce bir **sızıntı testiyle** denedik: yapımcı oturumuna bilerek cevap anahtarını okumayı, web'e
çıkmayı, skill çağırmayı denetiyoruz; hepsi reddedilmeli.

## 7. Dosyalar

| Dosya | Ne |
|---|---|
| [`ornek/settings.json`](ornek/settings.json) | guard kancası + deny kuralları |
| [`ornek/mcp_tanimlari.json`](ornek/mcp_tanimlari.json) | yayındaki üç topluluk / araç MCP'sinin tanımı |
| [`ornek/kor_kosu.ps1`](ornek/kor_kosu.ps1) | Windows PowerShell'de tek kör koşu |
| [`ornek/guard_iskelet.py`](ornek/guard_iskelet.py) | PreToolUse kanca protokolünün en kısa hali |
