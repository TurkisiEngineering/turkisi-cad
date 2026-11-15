"""SolidCraft'in AP242 STEP ciktisini AP214 (AUTOMOTIVE_DESIGN) basligina cevirir.
Yalniz FILE_SCHEMA, APPLICATION_CONTEXT, APPLICATION_PROTOCOL_DEFINITION ve PRODUCT adini degistirir;
geometri varliklarina dokunmaz (hepsi AP214'te de gecerli varliklardir).
Kullanim: python step_to_ap214.py girdi_ap242.step cikti_ap214.step ["Urun Adi"]"""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
name = sys.argv[3] if len(sys.argv) > 3 else None
s = open(src, encoding="utf-8").read()
n0 = len(s)
s, a = re.subn(r"FILE_SCHEMA\(\('[^']*'\)\);", "FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));", s)
s, b = re.subn(r"APPLICATION_CONTEXT\('[^']*'\)", "APPLICATION_CONTEXT('core data for automotive mechanical design processes')", s)
s, c = re.subn(r"APPLICATION_PROTOCOL_DEFINITION\('international standard','[^']*',\d+,", "APPLICATION_PROTOCOL_DEFINITION('international standard','automotive_design',2000,", s)
assert (a, b, c) == (1, 1, 1), (a, b, c)
import os
s = re.sub(r"FILE_NAME\('[^']*',", "FILE_NAME('%s'," % os.path.basename(dst), s, count=1)
if name:
    s = re.sub(r"PRODUCT\('[^']*','[^']*',", f"PRODUCT('{name}','{name}',", s, count=1)
    s = re.sub(r"=((?:ADVANCED_BREP_)?SHAPE_REPRESENTATION)\('[^']*',", lambda m: f"={m.group(1)}('{name}',", s)
open(dst, "w", encoding="utf-8", newline="\n").write(s)
print("AP214 yazildi:", dst)
