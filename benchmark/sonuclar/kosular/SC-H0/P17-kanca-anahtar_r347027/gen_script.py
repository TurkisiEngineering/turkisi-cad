# Generates spanner_build.json (SolidCraft command script) for P01 Spanner.
# Frame: plate between Y=-T/2..+T/2, outline in XZ, units inch.
# SolidCraft XZ sketch: sketch x = +X, sketch y = -Z.  Bare numbers are mm,
# so every coordinate is written as an expression (parameter or "<v> in").
import json, math, sys

P = [  # name, expression, comment
    ("T", "0.12 in", "F1 plate thickness (symmetric extrude along Y)"),
    ("H_handle", "0.389790 in", "F1 handle width (Z=0 .. -H_handle)"),
    ("R_end", "H_handle / 2", "F1 semicircular handle end radius"),
    ("X_end", "1.970605 in", "F1 x of handle-end arc centre"),
    ("X_top0", "-1.354007 in", "F1 start x of handle top edge"),
    ("X_neck", "-0.703984 in", "F1 end x of handle bottom edge / neck arc centre x"),
    ("R_neck", "15/32 * 1 in", "F1 concave neck arc radius"),
    ("Xc_back", "-1.507307 in", "F1 head back arc centre x (z=0)"),
    ("R_back", "0.707013 in", "F1 head back arc radius (head height)"),
    ("R_tip", "5/64 * 1 in", "F1 hook tip arc radius"),
    ("Xc_jaw", "-1.696750 in", "F1 jaw arc centre x (z=0)"),
    ("R_jaw", "5/16 * 1 in", "F1 jaw arc radius (0.625 nut)"),
    ("Slot_X1", "1.918717 in", "F2 slot first centre x"),
    ("Slot_C", "0.025985 in", "F2 slot centre distance"),
    ("Slot_W", "0.129930 in", "F2 slot width"),
    ("R_round", "1/64 * 1 in", "F3 handle edge round radius"),
    ("X_round0", "-0.441484 in", "F3/F4 x where full round ends"),
    ("A_runout", "10 deg", "F4 run-out cone half angle"),
    ("L_runout", "(sqrt(2) - 1) * R_round / tan(A_runout)", "F4 run-out length (0.036705)"),
    ("Cut_big", "0.05 in", "F3/F4 helper: radial extent of round cutters (outside part)"),
    ("Cut_ext", "0.002 in", "F4 helper: cutter extension past sharp end (removes nothing)"),
]

def I(v):
    return f"{v:.6f} in"

def pt(x, z):
    """XZ point -> sketch point (sketch y = -Z). Numeric z is world Z; a string is the depth -Z."""
    return [x if isinstance(x, str) else I(x), negz(z)]

def negz(z):
    if isinstance(z, str):
        return z  # string = depth expression (-Z), already the sketch y
    return I(-z)

cmds = []
def c(command, **params):
    cmds.append({"command": command, "params": params})

c("document.units", units="in")
for n, e, cm in P:
    c("parameters.add", name=n, expression=e, comment=cm)

# ---------- numeric copy for arc direction decisions ----------
V = dict(H=0.389790, Xe=1.970605, Xt=-1.354007, Xn=-0.703984, Rn=0.46875,
         Xb=-1.507307, Rb=0.707013, Rt=0.078125, Xj=-1.696750, Rj=0.3125)

def cw_flag(center, start, end, through):
    """center/start/end/through in XZ numbers -> True if arc start->end via through is clockwise in sketch coords."""
    def ang(p):
        return math.atan2(-(p[1]) - (-(center[1])), p[0] - center[0]) % (2 * math.pi)
    a0, a1, at = ang(start), ang(end), ang(through)
    ccw_sweep = (a1 - a0) % (2 * math.pi)
    ccw_t = (at - a0) % (2 * math.pi)
    return not (ccw_t < ccw_sweep)

def arc(center_e, start_e, end_e, center_n, start_n, end_n, through_n):
    c("sketch.arc.center_point", center=center_e, start=start_e, end=end_e,
      clockwise=cw_flag(center_n, start_n, end_n, through_n))

# ---------- F1 outline ----------
c("sketch.create", plane="XZ", name="F1_Outline")
p1 = pt("X_top0", "0 in");            p1n = (-1.354007, 0)
p2 = pt("X_end", "0 in");             p2n = (1.970605, 0)
p3 = pt("X_end", "H_handle");         p3n = (1.970605, -0.389790)
p4 = pt("X_neck", "H_handle");        p4n = (-0.703984, -0.389790)
p5 = pt(-1.024250, -0.516259);        p5n = (-1.024250, -0.516259)
# p6: exact internal tangency point of back arc and tip arc (spec value -2.159435,-0.273121 is rounded)
_cb, _ct, _rb = (-1.507307, 0.0), (-2.087375, -0.242941), 0.707013
_d = math.hypot(_ct[0] - _cb[0], _ct[1] - _cb[1])
p6n = (_cb[0] + _rb * (_ct[0] - _cb[0]) / _d, _cb[1] + _rb * (_ct[1] - _cb[1]) / _d)
p6 = [f"{p6n[0]:.9f} in", f"{-p6n[1]:.9f} in"]
p7 = pt(-2.104284, -0.166668);        p7n = (-2.104284, -0.166668)
p8 = pt(-1.931443, -0.128350);        p8n = (-1.931443, -0.128350)
p9 = pt(-1.864243, -0.193720);        p9n = (-1.864243, -0.193720)
p10 = pt(-1.922674, -0.215905);       p10n = (-1.922674, -0.215905)
p11 = pt(-1.411824, -0.128350);       p11n = (-1.411824, -0.128350)

# Junction points that sit on arcs are snapped onto their circle (spec values are rounded to 1e-6;
# SolidCraft puts an arc's end exactly on its circle, so an off-circle point would leave the loop open).
def proj(cen, R, p):
    d = math.hypot(p[0] - cen[0], p[1] - cen[1])
    return (cen[0] + R * (p[0] - cen[0]) / d, cen[1] + R * (p[1] - cen[1]) / d)
def npt(pn):
    return [f"{pn[0]:.9f} in", f"{-pn[1]:.9f} in"]
_cn = (-0.703984, -0.858540)
p5n = proj(_cn, 0.46875, (-1.507307, 0.0)); p5 = npt(p5n)        # neck/back tangency
# an arc's radius is set by its start point, so the following junction uses that same radius
_r3 = math.hypot(p5n[0] - _cb[0], p5n[1] - _cb[1])
p6n = proj(_cb, _r3, p6n); p6 = npt(p6n)                          # back/tip tangency
_r4 = math.hypot(p6n[0] - _ct[0], p6n[1] - _ct[1])
p7n = proj(_ct, _r4, p7n); p7 = npt(p7n)                          # tip/top-of-hook
p10n = proj((-1.696750, 0.0), 0.3125, p10n); p10 = npt(p10n)      # pin underside/jaw
p11n = proj((-1.696750, 0.0), 0.3125, p11n); p11 = npt(p11n)      # jaw/closing line

# 1 top edge
c("sketch.line", points=[p1, p2])
# 2 semicircular end (centre X_end, -R_end)
arc(pt("X_end", "R_end"), p2, p3, (1.970605, -0.194895), p2n, p3n, (2.1655, -0.194895))
# 3 bottom edge
c("sketch.line", points=[p3, p4])
# 4 concave neck arc, centre (X_neck, -(H_handle+R_neck))
cn = (-0.703984, -0.858540)
arc(pt("X_neck", "H_handle + R_neck"), p4, p5, cn, p4n, p5n,
    (cn[0] + 0.46875 * math.cos(math.radians(110)), cn[1] + 0.46875 * math.sin(math.radians(110))))
# 5 back of head, centre (Xc_back, 0)
arc(pt("Xc_back", "0 in"), p5, p6, (-1.507307, 0), p5n, p6n, (-1.507307, -0.707013))
# 6 hook tip, centre (-2.087375, -0.242941)
arc(pt(-2.087375, -0.242941), p6, p7, (-2.087375, -0.242941), p6n, p7n, (-2.165500, -0.242941))
# 7,8,9 pin lines
c("sketch.line", points=[p7, p8, p9, p10])
# 10 jaw arc, centre (Xc_jaw, 0)
arc(pt("Xc_jaw", "0 in"), p10, p11, (-1.696750, 0), p10n, p11n, (-1.696750, -0.3125))
# 11 closing line
c("sketch.line", points=[p11, p1])
c("sketch.finish")
c("solid.extrude", sketch="F1_Outline", distance="T", direction="symmetric",
  operation="new", body_name="P01 Spanner", name="F1_Extrude")

# ---------- F3 handle with edge rounds ----------
# F3a: keep only the head part of the F1 plate (x <= X_round0); the handle is rebuilt as its own body.
c("sketch.create", plane="XZ", name="F3a_HandleZone")
c("sketch.rectangle.two_point", p0=["X_round0", "-0.1 in"], p1=["X_end + R_end + 0.1 in", "H_handle + 0.1 in"])
c("sketch.finish")
c("solid.extrude", sketch="F3a_HandleZone", through_all=True, direction="symmetric",
  operation="cut", targets=["P01 Spanner"], name="F3a_TrimHandle")

# ---------- F4 conical run-out (4 places) ----------
# Cut into the head part before the handle is joined: the cutters end flush with the head's
# end face at X_round0, where their section equals the handle's rounded section.
# Profile in the plane through the round's centre line (parallel X), revolved 90 deg into the
# corner quadrant: the slanted edge (10 deg to X) becomes the cone r(x) = R_round + tan(A_runout)*(X_round0 - x).
# Centre lines: Y = +/-(T/2 - R_round), Z = -R_round (top) / -(H_handle - R_round) (bottom).
xa = "X_round0 - L_runout - Cut_ext"
ra = "R_round + tan(A_runout) * (L_runout + Cut_ext)"
corners = [  # name, y sign, z of centre line (world Z), quadrant direction in Z (+1 up / -1 down)
    ("TopPos", +1, "-R_round", +1),
    ("TopNeg", -1, "-R_round", +1),
    ("BotPos", +1, "-(H_handle - R_round)", -1),
    ("BotNeg", -1, "-(H_handle - R_round)", -1),
]
cutters = []
for nm, ys, zc, zd in corners:
    sk = f"F4_{nm}_Profile"
    c("sketch.create", plane="XY", offset=zc, name=sk)
    cy = "(T/2 - R_round)"
    def yy(d):
        e = f"{cy} + {d}"
        return e if ys > 0 else f"-({e})"
    c("sketch.line", closed=True, points=[
        [xa, yy(ra)], ["X_round0", yy("R_round")], ["X_round0", yy("Cut_big")], [xa, yy("Cut_big")]])
    c("sketch.line", points=[[xa, yy("0 in")], ["X_round0", yy("0 in")]], construction=True, ids=["ax"])
    c("sketch.finish")
    # SolidCraft measures the revolve angle from the profile side (checked on the cutter bboxes):
    # +90 sweeps the profile up into +Z, -90 down into -Z, for either Y side.
    body = f"Cut_{nm}"
    c("solid.revolve", sketch=sk, axis="ax", angle=f"{90 * zd} deg", operation="new",
      body_name=body, name=f"F4_{nm}_Revolve")
    cutters.append(body)
c("solid.combine", target="P01 Spanner", tools=cutters, operation="cut", keep_tools=False)

# F3b: handle (straight part + semicircular end) from X_round0, same thickness
c("sketch.create", plane="XZ", name="F3b_Handle")
c("sketch.line", points=[["X_round0", "H_handle"], ["X_round0", "0 in"], ["X_end", "0 in"]])
c("sketch.arc.center_point", center=["X_end", "R_end"], start=["X_end", "0 in"], end=["X_end", "H_handle"], clockwise=False)
c("sketch.line", points=[["X_end", "H_handle"], ["X_round0", "H_handle"]])
c("sketch.finish")
c("solid.extrude", sketch="F3b_Handle", distance="T", direction="symmetric",
  operation="new", body_name="Handle", name="F3b_HandleExtrude")

# F3c: R_round on top edge, semicircular end and bottom edge, both faces (edge picks in mm, world)
MM = 25.4
xm = 0.5 * MM; yf = 0.06 * MM; H = 0.389790 * MM; Re = 0.194895 * MM; Xe = 1.970605 * MM
edges = []
for s_ in (+1, -1):
    edges += [[xm, s_ * yf, 0.0], [Xe + Re, s_ * yf, -Re], [xm, s_ * yf, -H]]
c("solid.fillet", body="Handle", edges=edges, radius="R_round", name="F3c_EdgeRounds")

# F3d: join handle back to the head
c("solid.combine", target="P01 Spanner", tools=["Handle"], operation="join", keep_tools=False)

# ---------- F2 slot ----------
c("sketch.create", plane="XZ", name="F2_Slot")
# obround: tangent lines at depth R_end -/+ Slot_W/2, semicircles about the two centres
_X1, _X2 = "Slot_X1", "Slot_X1 + Slot_C"
_up, _dn = "R_end - Slot_W/2", "R_end + Slot_W/2"
c("sketch.line", points=[[_X1, _up], [_X2, _up]])
c("sketch.arc.center_point", center=[_X2, "R_end"], start=[_X2, _up], end=[_X2, _dn], clockwise=False)
c("sketch.line", points=[[_X2, _dn], [_X1, _dn]])
c("sketch.arc.center_point", center=[_X1, "R_end"], start=[_X1, _dn], end=[_X1, _up], clockwise=False)
c("sketch.finish")
c("solid.extrude", sketch="F2_Slot", through_all=True, direction="symmetric",
  operation="cut", targets=["P01 Spanner"], name="F2_SlotCut")


out = sys.argv[1] if len(sys.argv) > 1 else "spanner_build.json"
json.dump({"commands": cmds}, open(out, "w"), indent=1)
print("wrote", out, len(cmds), "commands")
