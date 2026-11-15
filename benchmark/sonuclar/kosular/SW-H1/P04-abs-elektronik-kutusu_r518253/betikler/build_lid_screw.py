"""P02 Lid and H1 closure screw - built in place in the global frame (inch)."""
import math
from params import *
from common import outer_shell, cavity, label, cross


def build_lid(P, verbose=True):
    rep = (lambda t: P.report(t)) if verbose else (lambda t: None)
    tag = "P02"
    z0 = LID_Z_BOT
    outer_shell(P, z0, +1, tag)                 # L1 + L2
    rep("shell")
    cavity(P, z0, +1, tag, LID_CEIL)            # L3 + L4
    rep("cavity")

    # L5 groove, 10 deg walls, narrowing toward the floor z=0.065
    P.begin(P.pz(z0), "P02_SK_groove")
    P.rrect(GROOVE_OUT[0], GROOVE_OUT[1], GROOVE_OUT[2], z0)
    P.rrect(GROOVE_IN[0], GROOVE_IN[1], GROOVE_IN[2], z0)
    P.end()
    P.extrude(GROOVE_DEPTH, up=True, cut=True, draft=GROOVE_DRAFT, outward=False, name="P02_Groove_10deg")
    P.param("GROOVE_IN", "%.4f x %.4f half, R%.4f" % GROOVE_IN, "P02_SK_groove", "groove inner boundary at mouth")
    P.param("GROOVE_OUT", "%.4f x %.4f half, R%.4f" % GROOVE_OUT, "P02_SK_groove", "groove outer boundary at mouth")
    P.param("GROOVE_DEPTH", GROOVE_DEPTH, "P02_Groove_10deg", "groove depth")
    P.param("GROOVE_DRAFT", GROOVE_DRAFT, "P02_Groove_10deg", "groove wall draft deg")
    rep("groove")

    # L6 keys: groove left solid for |y| < 0.146 on the X sides, end faces 3 deg
    P.begin(P.pz(z0), "P02_SK_key")
    P.rect(0.85, -KEY_HALF, 0.915, KEY_HALF, z0)
    P.rect(-0.915, -KEY_HALF, -0.85, KEY_HALF, z0)
    P.end()
    P.extrude(GROOVE_DEPTH, up=True, draft=KEY_DRAFT, outward=False, name="P02_Key_3deg")
    P.param("KEY_HALF", KEY_HALF, "P02_SK_key", "key half length |y| at the mouth")
    P.param("KEY_DRAFT", KEY_DRAFT, "P02_Key_3deg", "key end-face draft deg")
    rep("key")

    # L7 boss (bottom z=0.035, r=0.0925, grows 1 deg toward the ceiling)
    zb = LID_BOSS_Z
    P.begin(P.pz(zb), "P02_SK_boss")
    P.circle((0, 0, zb), BOSS_R)
    P.end()
    P.extrude(LID_CEIL - zb, up=True, draft=DRAFT_IN, outward=True, name="P02_Boss_1deg")
    P.param("BOSS_R", BOSS_R, "P02_SK_boss", "boss radius at z=0.035")
    P.param("LID_BOSS_Z", zb, "P02_SK_boss", "boss / rib bottom z")
    # L8 ribs
    P.begin(P.pz(zb), "P02_SK_ribs")
    P.poly(cross(LID_RIB_END, RIB_HALF_T), zb)
    P.end()
    P.extrude(LID_CEIL - zb, up=True, draft=DRAFT_IN, outward=True, name="P02_Ribs_1deg")
    P.param("LID_RIB_END", LID_RIB_END, "P02_SK_ribs", "rib end |x| at z=0.035")
    P.param("RIB_HALF_T", RIB_HALF_T, "P02_SK_ribs", "rib half thickness at z=0.035")
    rep("boss+ribs")
    # L9 hole r0.035 up to z=0.42
    P.begin(P.pz(zb), "P02_SK_hole")
    P.circle((0, 0, zb), LID_HOLE_R)
    P.end()
    P.extrude(LID_CEIL - zb, up=True, cut=True, name="P02_ScrewHole")
    P.param("LID_HOLE_R", LID_HOLE_R, "P02_SK_hole", "lid hole radius (plain)")
    rep("hole")
    # L10 label
    label(P, LID_Z_TOP, -1, tag)
    rep("label")
    return P


def build_screw(P, verbose=True):
    rep = (lambda t: P.report(t)) if verbose else (lambda t: None)
    P.begin(P.right, "H1_SK_profile")
    pr = [(0, SCR_Z_HEAD), (SCR_HEAD_R, SCR_Z_HEAD), (SCR_R, SCR_Z_CONE), (SCR_R, SCR_Z_END), (0, SCR_Z_END)]
    for i in range(len(pr)):
        a, b = pr[i], pr[(i + 1) % len(pr)]
        P.line((0, a[0], a[1]), (0, b[0], b[1]))
    P.cline((0, 0, -0.6), (0, 0, 0.2))
    P.end()
    P.revolve(name="H1_Body")
    rep("revolve")
    q = [(SCR_ARM_REACH, -SCR_ARM_HALF), (SCR_ARM_REACH, SCR_ARM_HALF), (SCR_FILL, SCR_ARM_HALF),
         (SCR_ARM_HALF, SCR_FILL)]
    pts = []
    for k in range(4):
        c, s = [(1, 0), (0, 1), (-1, 0), (0, -1)][k]
        pts += [(x * c - y * s, x * s + y * c) for x, y in q]
    P.begin(P.pz(SCR_Z_HEAD), "H1_SK_crossRecess")
    P.poly(pts, SCR_Z_HEAD)
    P.end()
    P.extrude(SCR_RECESS_D, up=True, cut=True, draft=SCR_RECESS_DRAFT, outward=False, name="H1_CrossRecess_4deg")
    rep("recess")
    for n, v, f, d in (("SCR_HEAD_R", SCR_HEAD_R, "H1_SK_profile", "head radius"),
                       ("SCR_Z_HEAD", SCR_Z_HEAD, "H1_SK_profile", "head face z"),
                       ("SCR_Z_CONE", SCR_Z_CONE, "H1_SK_profile", "end of 84 deg head cone"),
                       ("SCR_R", SCR_R, "H1_SK_profile", "shank radius"),
                       ("SCR_Z_END", SCR_Z_END, "H1_SK_profile", "shank end z"),
                       ("SCR_RECESS_D", SCR_RECESS_D, "H1_CrossRecess_4deg", "cross recess depth"),
                       ("SCR_RECESS_DRAFT", SCR_RECESS_DRAFT, "H1_CrossRecess_4deg", "recess wall draft deg"),
                       ("SCR_ARM_REACH", SCR_ARM_REACH, "H1_SK_crossRecess", "arm reach at mouth"),
                       ("SCR_ARM_HALF", SCR_ARM_HALF, "H1_SK_crossRecess", "arm half width at mouth"),
                       ("SCR_FILL", SCR_FILL, "H1_SK_crossRecess", "45 deg fill-flat vertex")):
        P.param(n, v, f, d)
    return P


if __name__ == "__main__":
    import sys, win32com.client, swlib
    sw = win32com.client.Dispatch("SldWorks.Application")
    if "lid" in sys.argv:
        build_lid(swlib.Part(sw))
    if "screw" in sys.argv:
        build_screw(swlib.Part(sw))
