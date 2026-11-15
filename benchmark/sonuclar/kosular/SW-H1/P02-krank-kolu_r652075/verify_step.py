# -*- coding: utf-8 -*-
"""Re-import final.step into SolidWorks and measure it (independent check of the deliverable).
Usage: python verify_step.py [path/to/final.step]"""
import json, os, sys, types
import pythoncom, win32com.client
from win32com.client import VARIANT

V = lambda x: x() if isinstance(x, types.MethodType) else x
stp = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "final.step")
sw = win32com.client.Dispatch("SldWorks.Application")
err = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
imp = sw.GetImportFileData(stp)
m = sw.LoadFile4(stp, "r", imp, err)
assert m is not None, "import failed %s" % err.value
try:
    bodies = m.GetBodies2(0, False)
    mp = V(m.Extension.CreateMassProperty)
    box = [0.0] * 6
    for i, b in enumerate(bodies):
        bb = V(b.GetBodyBox)
        if i == 0:
            box = list(bb)
        else:
            box = [min(box[k], bb[k]) for k in range(3)] + [max(box[k + 3], bb[k + 3]) for k in range(3)]
    out = {
        "bodies": len(bodies),
        "names": [V(b.Name) for b in bodies],
        "volume_mm3": V(mp.Volume) * 1e9,
        "area_mm2": V(mp.SurfaceArea) * 1e6,
        "com_mm": [c * 1000 for c in V(mp.CenterOfMass)],
        "bbox_mm": [c * 1000 for c in box],
        "faces": sum(V(b.GetFaceCount) for b in bodies),
    }
    print(json.dumps(out, indent=1))
finally:
    sw.CloseDoc(V(m.GetTitle))
