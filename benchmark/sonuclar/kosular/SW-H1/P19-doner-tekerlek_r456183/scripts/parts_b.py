"""Builders for P02 top plate, P03 kingpin, P04 washer, P05 hex ring, P06 pedal."""
import math
from swlib import Path, XY, XZ, RY, edge_faces, face_info, edge_mid
from parts import P, YAX


# ------------------------------------------------------------------------------------- P02 top plate
def build_P02(p):
    y0, t = P['plate_top_y'] - P['plate_t'], P['plate_t']
    hx, hz, rc = P['plate_len'] / 2, P['plate_wid'] / 2, P['plate_corner_R']
    cx, cz = hx - rc, hz - rc
    outline = (Path((-cx, -hz)).L((cx, -hz)).A((cx, -cz), (hx, -cz)).L((hx, cz)).A((cx, cz), (cx, hz))
               .L((-cx, hz)).A((-cx, cz), (-hx, cz)).L((-hx, -cz)).A((-cx, -cz), (-cx, -hz)).close())
    slots = []
    rs, dx = P['slot_w'] / 2, P['slot_arc_dx'] / 2
    for sx in (-1, 1):
        for sz in (-1, 1):
            X, Z = sx * P['slot_pitch_x'] / 2, sz * P['slot_pitch_z'] / 2
            slots.append(Path((X - dx, Z - rs)).L((X + dx, Z - rs))
                         .A((X + dx, Z), (X + dx, Z + rs), thru=(X + dx + rs, Z))
                         .L((X - dx, Z + rs)).A((X - dx, Z), (X - dx, Z - rs), thru=(X - dx - rs, Z)))
    # (the section overlaps the flat plate by 0.01 in r so that the merge is volumetric, not face-to-face)
    sec = (Path((0.76, 2.75)).L((0.719, 2.75)).A((0.719, 2.5), (0.57754, 2.70610)).L((0.37560, 2.56750))
           .A((0.319, 2.65), (0.3595, 2.55860)).L((0.3595, 2.502)).L((0.3605, 2.502))
           .A((0.3605, 2.487), (0.3755, 2.487)).L((0.3755, 2.45330)).A((0.35, 2.55), (0.40660, 2.46750))
           .L((0.60855, 2.60610)).A((0.75, 2.4), (0.75, 2.65)).L((0.76, 2.65)).close())
    sk3 = p.sketch(p.front, [sec], RY(), centerline=YAX, name='Sk_pressed_centre')
    p.revolve(sk3, name='Rev_pressed_centre')
    # flat plate with a r=0.75 clearance hole (the pressed centre is revolved first and overlaps it)
    pl = p.plane_y(y0, 'Plane_plate_bottom')
    sk = p.sketch(pl, [outline] + slots, XZ(y0), circles=[((0, y0, 0), 0.75)], name='Sk_plate_outline_slots')
    p.extrude(sk, t, name='Ext_plate')


# ------------------------------------------------------------------------------------- P03 kingpin
def build_P03(p):
    sec = (Path((0, 2.136)).L((0.236, 2.0728)).L((0.236, 1.7767)).L((0.2557, 1.757)).L((0.2732, 1.757))
           .L((0.29285, 1.7767)).L((0.29285, 2.367)).A((0.30785, 2.367), (0.30785, 2.382)).L((0.3605, 2.382))
           .A((0.3605, 2.397), (0.3755, 2.397)).L((0.3755, 2.487)).A((0.3605, 2.487), (0.3605, 2.502))
           .L((0.3115, 2.502)).A((0.3115, 2.517), (0.2965, 2.517)).L((0.2965, 2.7303)).L((0.2768, 2.75))
           .L((0, 2.75)).close())
    sk = p.sketch(p.front, [sec], RY(), centerline=YAX, name='Sk_kingpin_section')
    p.revolve(sk, name='Rev_kingpin')
    y0 = 2.502
    lug = (Path((-0.2832, 0.0878)).A((-0.3208, 0.0995), (-0.3115, 0.0612))
           .A((-0.2965, 0), (-0.3115, -0.0612), thru=(-0.2965 - P['lug_R'], 0))
           .A((-0.3208, -0.0995), (-0.2832, -0.0878)).close())
    pl = p.plane_y(y0, 'Plane_collar_top')
    sk2 = p.sketch(pl, [lug], XZ(y0), name='Sk_lug')
    p.extrude(sk2, P['lug_top_y'] - y0, name='Ext_lug')


# ------------------------------------------------------------------------------------- P04 washer
def build_P04(p):
    ro = P['washer_od'] / 2
    sec = (Path((0.401, 2.464)).L((ro, 2.464)).L((ro, 2.539)).L((0.5107, 2.539)).L((0.4066, 2.4675))
           .A((0.35, 2.55), (0.401, 2.464)))
    sk = p.sketch(p.front, [sec], RY(), centerline=YAX, name='Sk_washer_section')
    p.revolve(sk, name='Rev_washer')


# ------------------------------------------------------------------------------------- P05 hex ring
def build_P05(p):
    y0, t = 2.539, P['hex_t']
    rc = P['hex_af'] / 2 / math.cos(math.radians(30))   # corner radius (0.87180)
    pts = [(rc * math.cos(math.radians(a)), rc * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    hexp = Path(pts[0])
    for q in pts[1:]:
        hexp.L(q)
    hexp.close()
    pl = p.plane_y(y0, 'Plane_hex_bottom')
    sk = p.sketch(pl, [hexp], XZ(y0), name='Sk_hex')
    p.extrude(sk, t, name='Ext_hex')
    bore = (Path((0, 2.52)).L((0.5107, 2.52)).L((0.5107, 2.539)).L((0.60855, 2.6061))
            .A((0.75, 2.4), (0.6208, 2.614)).L((0.6208, 2.63)).L((0, 2.63)).close())
    sk2 = p.sketch(p.front, [bore], RY(), centerline=YAX, name='Sk_hex_bore')
    p.revolve(sk2, cut=True, name='Cut_hex_bore')


# ------------------------------------------------------------------------------------- P06 pedal
def foot_plan_complement():
    """(x,z) region x >= 3.6885 outside the foot-plate plan outline (intersection done as a cut)."""
    xb = P['leg_end_x']
    return (Path((xb, 1.01)).A((3.7285, 1.01), (3.7285, 1.05)).L((3.8139, 1.05))
            .A((3.8139, 0.8), (3.94710, 1.01157)).A((3.4144, 0.1653), (4.25988, 0.69922))
            .A((4.0485, 0.5657), (4.2985, 0.5657)).L((4.2985, -0.5657))
            .A((4.0485, -0.5657), (4.25988, -0.69922)).A((3.4144, -0.1653), (3.94710, -1.01157))
            .A((3.8139, -0.8), (3.8139, -1.05)).L((3.7285, -1.05)).A((3.7285, -1.01), (xb, -1.01))
            .L((xb, -1.6)).L((4.7, -1.6)).L((4.7, 1.6)).L((xb, 1.6)).close())


def build_P06(p, with_rounds=True):
    stem = (Path((2.4615, 1.18953)).L((2.4615, 2.15992)).A((0.13847, -6.14324), (3.5987, 1.75396), 'cw')
            .A((3.5385, 1.6166), (3.60992, 1.74847), 'cw').A((0.03345, -6.51039), (3.6885, 1.714), 'cw')
            .L((3.6885, 1.42487)).A((3.5385, 1.42487), (3.54269, 1.27493), 'cw').L((2.72879, 1.25219))
            .A((2.74786, 0.56946), (2.4615, 1.18953), 'ccw'))
    sk = p.sketch(p.front, [stem], XY(), name='Sk_pedal_stem')
    p.extrude(sk, 2 * P['pedal_stem_half_w'], mid=True, name='Ext_pedal_stem')
    foot = (Path((3.6885, 1.38078)).L((3.6885, 1.65822)).A((3.7385, 1.65822), (3.74187, 1.70811), 'cw')
            .A((3.7857, 2.3496), (4.08040, 1.77815), 'ccw').A((4.1485, 1.6445), (4.2985, 1.6445), 'cw')
            .L((4.2985, 1.3945)).A((4.1485, 1.3945), (4.0804, 1.26085), 'cw')
            .A((3.7857, 0.6894), (3.74187, 1.33089), 'ccw').A((3.7385, 1.38078), (3.6885, 1.38078), 'cw'))
    sk2 = p.sketch(p.front, [foot], XY(), name='Sk_foot_side')
    p.extrude(sk2, 2 * P['pedal_foot_half_w'], mid=True, name='Ext_foot_side')
    sk3 = p.sketch(p.top, [foot_plan_complement()], XZ(0), name='Sk_foot_plan_trim')
    p.cut(sk3, through_both=True, name='Cut_foot_plan')
    if with_rounds:
        try:
            p.fillet(pedal_round_edges(p), P['pedal_round'], name='Fillet_foot_R0_04')
        except Exception as e:
            print("  pedal rounds failed:", e)
            p.LOG.append('P06 R0.04 foot-plate rounds failed: %s' % e)
    ribs_stem = [(2.5865, 2.1107), (2.7115, 2.0682), (2.8365, 2.0334)]
    ribs_foot = [(3.7885, 1.7045), (3.8885, 1.7140), (3.9885, 1.7376)]
    sk4 = p.sketch(p.front, [], XY(), circles=[((x, y, 0), P['rib_R']) for x, y in ribs_stem], name='Sk_ribs_stem')
    p.extrude(sk4, 1.35, mid=True, name='Ext_ribs_stem')
    sk5 = p.sketch(p.front, [], XY(), circles=[((x, y, 0), P['rib_R']) for x, y in ribs_foot], name='Sk_ribs_foot')
    p.extrude(sk5, 1.75, mid=True, name='Ext_ribs_foot')


def pedal_round_edges(p):
    """Edges between foot-plate plan side faces (planes z=+/-1.05 or cylinders with axis // Y)
    and side-profile top/bottom faces (cylinders with axis // Z), for x > 3.69."""
    def plan_side(fi):
        if fi['type'] == 'plane':
            return abs(abs(fi['n'][2]) - 1) < 1e-6 and abs(fi['box'][2]) > 1.04 and abs(fi['box'][5]) > 1.04 \
                and fi['box'][2] * fi['box'][5] > 0
        if fi['type'] == 'cyl':
            return abs(abs(fi['a'][1]) - 1) < 1e-6 and fi['r'] > 0.045
        return False

    def prof(fi):
        return fi['type'] == 'cyl' and abs(abs(fi['a'][2]) - 1) < 1e-6

    sel = []
    for e in p.edges():
        m = edge_mid(e)
        if m[0] < 3.69:
            continue
        f1, f2 = [face_info(f) for f in edge_faces(e)]
        if (plan_side(f1) and prof(f2)) or (plan_side(f2) and prof(f1)):
            sel.append(e)
    print("  pedal round edges:", len(sel))
    return sel
