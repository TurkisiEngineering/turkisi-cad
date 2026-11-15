#!/bin/sh
# P01 Plate'i sifirdan kurar: P0_plate_script.json -> P0_plate.sc + final.step (AP214)
# Kullanim (bu klasorde): sh yeniden_kur.sh
set -e
CLI="${SOLIDCRAFT_CLI:-/c/Program Files/SolidCraft/solidcraft-cli.exe}"
cd "$(dirname "$0")"
rm -f P0_plate.sc final.step _ap242_raw.step
"$CLI" run P0_plate_script.json --save P0_plate.sc --out _ap242_raw.step --quiet
python step_to_ap214.py _ap242_raw.step final.step "P01 Plate"
rm -f _ap242_raw.step
"$CLI" eval final.step --json-out olcum_final_step.json
python -c "import json;b=json.load(open('olcum_final_step.json'))['bodies'][0];print(b['name'],round(b['volume_mm3'],3),round(b['area_mm2'],3),[round(c,4) for c in b['center_of_mass']],b['bbox'],b['faces'])"
