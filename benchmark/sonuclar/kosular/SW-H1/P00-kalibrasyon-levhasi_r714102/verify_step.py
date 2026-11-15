import sys, pythoncom, win32com.client
from win32com.client import VARIANT
sw = win32com.client.Dispatch("SldWorks.Application")
e = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
imp = sw.GetImportFileData(sys.argv[1])
doc = sw.LoadFile4(sys.argv[1], "r", imp, e)
mp = doc.Extension.CreateMassProperty
b = doc.GetBodies2(0, False)
print("bodies", len(b), [x.Name for x in b])
print("V", mp.Volume*1e9, "A", mp.SurfaceArea*1e6, "CoM", [c*1e3 for c in mp.CenterOfMass])
print("box", [v*1e3 for v in b[0].GetBodyBox()], "faces", b[0].GetFaceCount())
sw.CloseDoc(doc.GetTitle)
