"""P01 Knob core -> teslim/P01_core.SLDPRT  (spec bolum 4). Birim inc, global cerceve: eksen Z."""
import math
from swcom import *

# ---- isimli parametreler (inc) ----
P = dict(
    Z_hub_end=-0.68, R_hub_end=0.625, hub_draft_deg=3.0, R_hub_end_round=0.02,
    Z_underside=-0.12, R_head=1.2, Z_rim_top=0.44, R_top_flat_in=1.06,
    R_dome=2.175763, Dome_cx=0.124593, Dome_cz=-1.524424, R_top_face_out=0.492553, Z_top=0.62,
    R_scallop_pcd=1.39, R_scallop=0.33, N_lobes=8,
    R_rim_in=1.11, R_scallop_in=0.39, Z_step=0.26, Z_ceiling=0.35, R_step=1.01, R_ceiling=0.92,
    T_rib=0.05,
    R_seat=0.265625, Z_seat_top=-0.18, R_bore_bot=0.36, bore_taper_deg=3.0, R_bore_round=0.015,
    R_ridge_in=0.385417, R_ridge_out=0.505208, H_ridge=0.015,
)
t3 = math.tan(P["hub_draft_deg"] * DEG)
hub_r = lambda z: P["R_hub_end"] + t3 * (z - P["Z_hub_end"])
bore_r = lambda z: P["R_bore_bot"] + math.tan(P["bore_taper_deg"] * DEG) * (z - P["Z_seat_top"])


def arc_mid(c, R, p1, p2):
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0]); a2 = math.atan2(p2[1] - c[1], p2[0] - c[0])
    am = (a1 + a2) / 2
    return (c[0] + R * math.cos(am), c[1] + R * math.sin(am))


def build(sw):
    pt = Part(sw, "P01_core")
    pt.equations(P)
    Zh, Zu, Rh = P["Z_hub_end"], P["Z_underside"], P["R_head"]
    # ---- C1 main revolve ----
    pt.sketch("Top Plane")
    rr = P["R_hub_end_round"]
    c_r = (P["R_hub_end"] - rr * (1 / math.cos(t3 and math.atan(t3)) - t3) if False else None)
    # hub end round: centre (0.606021,-0.66), tangent to z=-0.68 and to cone
    cx = 0.606021; cz = Zh + rr
    # tangent point on cone: cone direction (t3,1)/|.|, outward normal (1,-t3)/|.|
    nrm = math.hypot(1, t3)
    tp = (cx + rr * 1 / nrm, cz - rr * t3 / nrm)
    dome_c = (P["Dome_cx"], P["Dome_cz"])
    pt.rz_profile([(0, Zh), ('L', (cx, Zh)), ('A', arc_mid((cx, cz), rr, (cx, Zh), tp), tp),
                   ('L', (hub_r(Zu), Zu)), ('L', (Rh, Zu)), ('L', (Rh, P["Z_rim_top"])),
                   ('L', (P["R_top_flat_in"], P["Z_rim_top"])),
                   ('A', arc_mid(dome_c, P["R_dome"], (P["R_top_flat_in"], P["Z_rim_top"]), (P["R_top_face_out"], P["Z_top"])),
                    (P["R_top_face_out"], P["Z_top"])),
                   ('L', (0, P["Z_top"])), ('L', (0, Zh))])
    pt.end_sketch("SK_C1_profile"); pt.revolve("C1_MainRevolve")
    pt.report("C1")
    # ---- C3 underside cavity ----
    # (a) cut prism Lci from z_underside to z_ceiling
    pl = pt.plane_z(Zu)
    pt.sketch(pl); pt.plan(outline(P["R_rim_in"], P["R_scallop_in"], 0, P["R_scallop_pcd"]), Zu)
    pt.end_sketch("SK_C3_Lci"); pt.extrude("C3a_CavityPrism", P["Z_ceiling"] - Zu, cut=True)
    pt.report("C3a")
    # (b) add back ring outside the 45deg ceiling cone / above step (K2 clipped by Lci)
    pt.sketch("Top Plane")
    pt.rz_profile([(P["R_step"], P["Z_step"]), ('L', (P["R_ceiling"], P["Z_ceiling"])), ('L', (Rh, P["Z_ceiling"])),
                   ('L', (Rh, P["Z_step"])), ('L', (P["R_step"], P["Z_step"]))])
    pt.end_sketch("SK_C3_ceiling"); pt.revolve("C3b_CeilingRing")
    # (c) hub cone continued up to the ceiling
    pt.sketch("Top Plane")
    zc = P["Z_ceiling"]
    pt.rz_profile([(0, Zu), ('L', (hub_r(Zu), Zu)), ('L', (hub_r(zc), zc)), ('L', (0, zc)), ('L', (0, Zu))])
    pt.end_sketch("SK_C3_hub"); pt.revolve("C3c_HubUp")
    # (d) 8 radial ribs (4 slabs through Z), bottom flush z_underside, up to ceiling
    pt.sketch(pl)
    L = 1.15  # inside rim wall (R1.11 at lobes) -> rib merges into wall
    L0 = 0.40  # inside hub material (bore r<=0.388 below ceiling) -> rib merges into hub
    h = P["T_rib"] / 2
    for k in range(8):
        a = k * 45 * DEG
        ca, sa = math.cos(a), math.sin(a)
        corners = [(L0, -h), (L, -h), (L, h), (L0, h)]
        pts = [(x * ca - y * sa, x * sa + y * ca, Zu) for x, y in corners]
        for i in range(4):
            pt.line(pts[i], pts[(i + 1) % 4])
    pt.end_sketch("SK_C3_ribs"); pt.extrude("C3d_Ribs", P["Z_ceiling"] - Zu)
    pt.report("C3")
    # ---- C2 scallops ----
    pt.sketch("Front Plane")
    for k in range(int(P["N_lobes"])):
        c = pol(P["R_scallop_pcd"], 22.5 + 45 * k)
        pt.circle((c[0], c[1], 0), P["R_scallop"])
    pt.end_sketch("SK_C2_scallops"); pt.extrude("C2_Scallops", 1, cut=True, both=True)
    pt.report("C2")
    # ---- C4 bore ----
    pt.sketch("Top Plane")
    zt = P["Z_top"]; rb = P["R_bore_round"]
    rc = (0.416161, 0.605)
    tb = (0.401182, 0.605785)
    pt.rz_profile([(0, Zh - 0.05), ('L', (P["R_seat"], Zh - 0.05)), ('L', (P["R_seat"], P["Z_seat_top"])),
                   ('L', (P["R_bore_bot"], P["Z_seat_top"])), ('L', tb),
                   ('A', arc_mid(rc, rb, tb, (rc[0], zt)), (rc[0], zt)),
                   ('L', (rc[0], zt + 0.1)), ('L', (0, zt + 0.1)), ('L', (0, Zh - 0.05))])
    pt.end_sketch("SK_C4_bore"); pt.revolve("C4_Bore", cut=True)
    # ---- C5 hub end ridge ----
    pt.sketch("Top Plane")
    zr = Zh - P["H_ridge"]
    pt.rz_profile([(P["R_ridge_in"], zr), ('L', (P["R_ridge_out"], zr)), ('L', (P["R_ridge_out"], Zh)),
                   ('L', (P["R_ridge_in"], Zh)), ('L', (P["R_ridge_in"], zr))])
    pt.end_sketch("SK_C5_ridge"); pt.revolve("C5_Ridge")
    r = pt.report("P01 final")
    pt.save("P01_core.SLDPRT")
    return pt, r


if __name__ == "__main__":
    build(app())
