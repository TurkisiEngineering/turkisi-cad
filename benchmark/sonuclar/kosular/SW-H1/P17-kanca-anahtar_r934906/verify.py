# Verifies the saved SLDPRT: mass props, tight bbox (extreme points), faces, equations.
import os, pythoncom, win32com.client
from win32com.client import VARIANT
IN = 0.0254
HERE = os.path.dirname(os.path.abspath(__file__))
sw = win32com.client.dynamic.Dispatch("SldWorks.Application")
path = os.path.join(HERE, "P01_Spanner.SLDPRT")
e = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0); w = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
already = sw.GetOpenDocumentByName(path) is not None
doc = sw.OpenDoc6(path, 1, 1, "", e, w)
ext = doc.Extension; ext._FlagAsMethod("CreateMassProperty")
mp = ext.CreateMassProperty()
print("volume in3", mp.Volume / IN**3, "area in2", mp.SurfaceArea / IN**2)
print("CoM in", [c / IN for c in mp.CenterOfMass])
body = doc.GetBodies2(0, True)[0]
print("body", body.Name, "faces", body.GetFaceCount())
ext_pts = []
for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
    r = body.GetExtremePoint(d[0], d[1], d[2], 0.0, 0.0, 0.0)
    p = [v / IN for v in r[1:4]]
    ext_pts.append(sum(p[i]*d[i] for i in range(3)))
print("Xmax %.6f Xmin %.6f Ymax %.6f Ymin %.6f Zmax %.6f Zmin %.6f" % (ext_pts[0], -ext_pts[1], ext_pts[2], -ext_pts[3], ext_pts[4], -ext_pts[5]))
eq = doc.GetEquationMgr
for i in range(eq.GetCount):
    print("eq", eq.Equation(i), eq.Value(i))
if not already:
    sw.CloseDoc(doc.GetTitle)
