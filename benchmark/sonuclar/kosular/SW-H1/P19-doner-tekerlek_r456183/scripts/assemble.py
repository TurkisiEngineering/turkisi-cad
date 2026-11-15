"""Assemble the 12 part files at identity placement and export final.step (AP214, inches).

usage: python assemble.py
"""
import os
import re
import pythoncom
from win32com.client import VARIANT

import swlib
from swlib import cast, C, IN
from build import TARGETS, ORDER, OUT
from parts import PARAMS


def main():
    app = swlib.sw()
    tmpl = app.GetUserPreferenceStringValue(C.swDefaultTemplateAssembly)
    asm_doc = cast(app.NewDocument(tmpl, 0, 0, 0), 'IModelDoc2')
    ext = cast(asm_doc.Extension, 'IModelDocExtension')
    ext.SetUserPreferenceInteger(C.swUnitSystem, 0, C.swUnitSystem_IPS)
    ext.SetUserPreferenceInteger(C.swUnitsLinear, 0, C.swINCHES)
    asm = cast(asm_doc, 'IAssemblyDoc')
    mu = cast(app.GetMathUtility(), 'IMathUtility')
    ident = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
    opened = []
    for pid in ORDER:
        path = os.path.join(OUT, TARGETS[pid][0] + '.SLDPRT')
        r = app.OpenDoc6(path, C.swDocPART, C.swOpenDocOptions_Silent, "", 0, 0)
        d = r[0] if isinstance(r, tuple) else r
        if d is None:
            raise RuntimeError("cannot open " + path)
        opened.append(cast(d, 'IModelDoc2').GetTitle())
        app.ActivateDoc3(asm_doc.GetTitle(), False, 0, 0)
        comp = asm.AddComponent5(path, 0, "", False, "", 0, 0, 0)
        if comp is None:
            raise RuntimeError("AddComponent failed " + path)
        comp = cast(comp, 'IComponent2')
        comp.Transform2 = cast(mu.CreateTransform(ident), 'IMathTransform')
        t = list(cast(comp.Transform2, 'IMathTransform').ArrayData)
        assert max(abs(a - b) for a, b in zip(t[:13], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1])) < 1e-12, t
        print("added", pid, comp.Name2)
    # global variables (documentation of the key dimensions) in the assembly
    em = cast(asm_doc.GetEquationMgr(), 'IEquationMgr')
    for k, v in PARAMS.items():
        em.Add2(-1, '"%s" = %.6fin' % (k, v), True)
    asm_doc.ForceRebuild3(False)
    asm_path = os.path.join(OUT, 'Caster_Assembly.SLDASM')
    if os.path.exists(asm_path):
        os.remove(asm_path)
    rc = asm_doc.SaveAs3(asm_path, 0, C.swSaveAsOptions_Silent)
    print("saved asm", rc)
    # STEP AP214
    app.SetUserPreferenceIntegerValue(C.swStepAP, 214)
    step = os.path.join(OUT, 'final.step')
    if os.path.exists(step):
        os.remove(step)
    r = ext.SaveAs3(step, 0, C.swSaveAsOptions_Silent | C.swSaveAsOptions_Copy, None, None, 0, 0)
    print("step export", r, os.path.exists(step))
    for t in opened:
        app.CloseDoc(t)
    app.CloseDoc(asm_doc.GetTitle())
    # quick check of the STEP file
    txt = open(step, errors='ignore').read()
    print("schema:", re.findall(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']+)'", txt))
    print("MANIFOLD_SOLID_BREP:", len(re.findall(r'MANIFOLD_SOLID_BREP', txt)))
    print("units:", sorted(set(re.findall(r"CONVERSION_BASED_UNIT\s*\(\s*'([^']+)'", txt))),
          "SI:", sorted(set(re.findall(r"SI_UNIT\s*\(\s*([^)]*)\)", txt)))[:4])


if __name__ == '__main__':
    main()
