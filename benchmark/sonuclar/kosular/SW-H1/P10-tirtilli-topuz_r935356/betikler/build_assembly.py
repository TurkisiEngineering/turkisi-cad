"""3 parcayi kimlik yerlesimiyle montaja koyar, final.step (AP214) yazar."""
import os, pythoncom
import win32com.client as wc
from swcom import *


def build(sw):
    tpl = sw.GetUserPreferenceStringValue(C.swDefaultTemplateAssembly)
    doc = sw.NewDocument(tpl, 0, 0, 0)
    m = swmod.IModelDoc2(doc._oleobj_)
    asm = cast(doc, swmod.IAssemblyDoc)
    m.Extension.SetUserPreferenceInteger(C.swUnitSystem, 0, C.swUnitSystem_IPS)  # STEP birimi = inc
    for fn in ("P01_core.SLDPRT", "P02_coating.SLDPRT", "P03_insert.SLDPRT"):
        p = os.path.join(OUT, fn)
        c = asm.AddComponent5(p, 0, "", False, "", 0, 0, 0)
        assert c is not None, fn
        c = cast(c, swmod.IComponent2)
        mu = cast(sw.GetMathUtility(), swmod.IMathUtility)
        I = mu.CreateTransform(wc.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,
                                          [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]))
        c.Transform2 = I
        print(fn, list(c.Transform2.ArrayData)[:13])
    # fix all components (identity placement, no mates)
    m.ClearSelection2(True)
    comps = asm.GetComponents(True)
    for c in comps:
        cast(c, swmod.IComponent2).Select4(True, None, False)
    asm.FixComponent()
    m.ForceRebuild3(False)
    p = os.path.join(OUT, "knob_assembly.SLDASM")
    print("save asm", m.Extension.SaveAs3(p, 0, 1, None, None, 0, 0))
    sw.SetUserPreferenceIntegerValue(C.swStepAP, 214)
    ps = os.path.join(OUT, "final.step")
    print("save step", m.Extension.SaveAs3(ps, 0, 1, None, None, 0, 0))
    return m


if __name__ == "__main__":
    build(app())
