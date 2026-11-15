"""Close only the documents created by build_gear.py (P01_Miter_gear*)."""
import win32com.client as w


def G(o, n):
    a = getattr(o, n)
    return a() if callable(a) and not hasattr(a, "_oleobj_") else a


sw = w.GetActiveObject('SldWorks.Application')
for d in (G(sw, "GetDocuments") or []):
    t = G(d, "GetTitle")
    if t.upper().startswith("P01_MITER_GEAR"):
        print("closing", t)
        sw.CloseDoc(t)
