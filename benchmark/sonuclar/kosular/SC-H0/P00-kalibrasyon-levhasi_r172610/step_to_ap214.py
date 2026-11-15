"""Rewrite the schema header of a SolidCraft STEP export from AP242 to AP214 (AUTOMOTIVE_DESIGN).

The SolidCraft CLI (file.export_step) has no parameter to choose the STEP schema and always writes
AP242. Every entity it writes for this part (MANIFOLD_SOLID_BREP, ADVANCED_FACE, PLANE,
CYLINDRICAL_SURFACE, B_SPLINE_CURVE_WITH_KNOTS, PRODUCT..., SI_UNIT...) is also in the AP214
AUTOMOTIVE_DESIGN schema, so only the header and the application context are changed. Geometry is
not touched.

usage: python step_to_ap214.py IN.step OUT.step
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
reps = [
    (r"FILE_SCHEMA\(\('[^']*'\)\);", "FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));"),
    (r"APPLICATION_CONTEXT\('[^']*'\)", "APPLICATION_CONTEXT('core data for automotive mechanical design processes')"),
    (r"PRODUCT\('[^']*','[^']*',", "PRODUCT('P01 Plate','P01 Plate',"),
    (r"APPLICATION_PROTOCOL_DEFINITION\('[^']*','[^']*',\d+,", "APPLICATION_PROTOCOL_DEFINITION('international standard','automotive_design',2001,"),
]
for pat, new in reps:
    text, n = re.subn(pat, new, text, count=1)
    if n != 1:
        sys.exit(f"pattern not found: {pat}")
open(dst, "w", encoding="utf-8", newline="").write(text)
print(f"wrote {dst} (AP214 AUTOMOTIVE_DESIGN)")
