# Tek kör koşu (Windows PowerShell). Yayındaki koşu başlatıcının yaptığının elle hali.
# Not: bu betik yayındaki Python başlatıcının (subprocess) birebir karşılığıdır; PowerShell hali ayrıca denenmedi.
# Önce <KÖK>, <run_id> ve <OTURUM> yerlerini kendi yollarınızla değiştirin.
#   <KÖK>\kosular\<run_id>\girdi\spec.md   yapımcının gördüğü tek dosya
#   <OTURUM>\settings.json, mcp.json, brif.md  koşu klasörünün DIŞINDA

$Kosu   = "<KÖK>\kosular\<run_id>"
$Oturum = "<OTURUM>"

# Claude Code içinden çağrılıyorsa üst oturumun değişkenlerini temizle
Get-ChildItem Env: | Where-Object { $_.Name -like "CLAUDECODE*" -or $_.Name -like "CLAUDE_CODE_SSE*" } |
    ForEach-Object { Remove-Item "Env:$($_.Name)" }

Set-Location $Kosu
Get-Content "$Oturum\brif.md" -Raw -Encoding UTF8 | claude -p `
    --model claude-opus-5-5 --effort high `
    --permission-mode bypassPermissions `
    --setting-sources project `
    --settings "$Oturum\settings.json" `
    --mcp-config "$Oturum\mcp.json" --strict-mcp-config `
    --output-format stream-json --verbose `
    --disallowedTools WebSearch WebFetch Workflow Artifact DesignSync RemoteTrigger `
        CronCreate CronDelete CronList PushNotification SendMessage ListAgents ScheduleWakeup `
        EnterWorktree ExitWorktree ReportFindings Skill Agent Task `
    --disable-slash-commands |
    Out-File -Encoding utf8 "$Oturum\akis.jsonl"

# Guard kancası settings.json'dan gelir; orada --run, --config, --kok ve --log dolu olmalı (README §6).
# H2 basamağında (skill'ler açık) "Skill Agent Task" ve "--disable-slash-commands" çıkarılır.
# Süre tavanı bu betikte yok; yayında koşu başlatıcı süreç ağacını tavanda durdurur.
