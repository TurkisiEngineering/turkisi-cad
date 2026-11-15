# Yeniden kurulum: döner tablalı tekerlek (swivel plate caster), 4 in

Gereken: SolidCraft (`C:\Program Files\SolidCraft\solidcraft-cli.exe`) ve Node.js. Modelin kaynağı `gen.js` dosyası;
bu dosya SolidCraft komut dizisini (`caster_script.json`) üretiyor. Teslim klasörünün temiz bir kopyasında, o klasörün
içinden şu adımları çalıştırın (Git Bash):

```sh
CLI="/c/Program Files/SolidCraft/solidcraft-cli.exe"

# 1) Komut dizisini üret (teslimdeki caster_script.json ile birebir aynı çıkar)
node gen.js > caster_script.json

# 2) Modeli sıfırdan kur ve SolidCraft belgesi olarak kaydet (12 gövde, yaklaşık 15 s sürer)
"$CLI" run caster_script.json --save caster.sc

# 3) STEP AP242 olarak dışa aktar (aracın kendi STEP yazıcısı)
cat > export_step.json <<'EOF'
{"commands":[{"command":"file.export_step","params":{"path":"final.step"}}]}
EOF
"$CLI" run export_step.json --in caster.sc

# 4) (isteğe bağlı) Ölçüm ve girişim kontrolü
"$CLI" eval caster.sc --json-out eval.json
```

Notlar
- Teslimdeki `export_step.json` dosyası mutlak yol kullanıyor. Başka bir klasörde çalışırken yukarıdaki göreli yollu
  sürümü kullanın.
- 1. adımı atlayıp teslimdeki `caster_script.json` dosyasını doğrudan `run` ile de çalıştırabilirsiniz.
- `node gen.js --no-fillets` komutu, kenar yuvarlamaları olmayan bir varyant üretir (hata ayıklama için).
- Belge birimi inç (`document.units in`); ölçüler `parametreler.md`'deki isimli parametrelerle tanımlı. Bir
  parametreyi değiştirmek için: `"$CLI" exec parameters.change '{"name":"axle_D","expression":"0.6 in"}'` ya da
  `caster.sc` üzerinde `parameters.change` komutunu içeren bir betiği `run --in caster.sc --save ...` ile
  çalıştırın.
- SolidCraft'ın STEP çıktısı her zaman mm birimiyle yazılıyor (`SI_UNIT(.MILLI.,.METRE.)`). Geometri spec'in global
  çerçevesinde ve 1 in = 25.4 mm ile birebir aynı; eksen ve orijin değişmiyor.
