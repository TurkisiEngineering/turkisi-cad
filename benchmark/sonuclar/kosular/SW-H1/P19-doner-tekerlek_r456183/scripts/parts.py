"""Part builders for the swivel caster (spec.md). Units: inches, global frame of the spec.

Each builder takes a swlib.Part and builds exactly one solid in place.
Named parameters live in PARAMS (also written to each part as global variables).
"""
import math
from swlib import Path, mirror_v, XY, XZ, RY, WHEEL, C, edge_faces, face_info, is_tangent, edge_mid

PARAMS = {
    # global layout
    'mount_height': 5.5, 'plate_top_y': 2.75, 'swivel_offset': 1.515, 'axle_y': -0.75,
    # wheel
    'wheel_od': 4.0, 'wheel_width': 1.25, 'tread_bore_r': 1.56375, 'tread_edge_round': 0.2,
    'insert_ri': 1.51375, 'insert_ro': 1.56375, 'core_r': 1.51375, 'core_half_width': 0.3125,
    'flange_hub_r': 0.305, 'flange_dish_R': 3.75269, 'flange_dish_cz': 2.9277, 'flange_round': 0.02,
    'axle_d': 0.6, 'axle_half_len': 1.034,
    # fork
    'fork_half_width': 1.029, 'fork_inner_half_gap': 0.83, 'ridge_half_width': 1.133,
    'crown_R': 1.029, 'ridge_R': 1.133, 'gap_R': 0.83, 'deck_top_y': 2.464, 'ceiling_y': 2.184,
    'kingpin_hole_d': 1.0, 'axle_bore_d': 0.6, 'top_arc_R': 8.622, 'ceiling_arc_R': 8.342,
    'gap_end_x': 2.4615, 'leg_end_x': 3.6885, 'fork_round': 0.06, 'leg_end_round': 0.125,
    'ridge_round': 0.04,
    # top plate
    'plate_len': 3.625, 'plate_wid': 2.5, 'plate_t': 0.1, 'plate_corner_R': 0.25,
    'slot_w': 0.3125, 'slot_pitch_x': 2.9375, 'slot_pitch_z': 1.75, 'slot_arc_dx': 0.125,
    # kingpin / bearings
    'kp_shank_d': 0.5857, 'kp_collar_d': 0.751, 'kp_upper_d': 0.593, 'kp_bottom_y': 1.757,
    'lug_top_y': 2.6, 'lug_R': 0.063, 'washer_od': 1.744, 'washer_t': 0.075,
    'hex_af': 1.51, 'hex_t': 0.075,
    # pedal
    'pedal_stem_half_w': 0.825, 'pedal_foot_half_w': 1.05, 'pedal_front_x': 4.2985,
    'pedal_round': 0.04, 'rib_R': 0.025,
}
P = PARAMS
AX = (P['swivel_offset'], P['axle_y'])        # wheel axis (x, y)
YAX = ((0, -1, 0), (0, 3, 0))                 # swivel axis centerline (model coords)
WAX = ((1.515, -0.75, -2), (1.515, -0.75, 2))  # wheel axis centerline


def wheel_plane(p):
    return p.plane_y(P['axle_y'], 'Plane_axle_y')


# ------------------------------------------------------------------------------------- wheel
def build_P07(p):
    ri, ro, hw, r = P['tread_bore_r'], P['wheel_od'] / 2, P['wheel_width'] / 2, P['tread_edge_round']
    pl = wheel_plane(p)
    path = (Path((ri, -hw)).L((ro - r, -hw)).A((ro - r, -hw + r), (ro, -hw + r))
            .L((ro, hw - r)).A((ro - r, hw - r), (ro - r, hw)).L((ri, hw)).close())
    sk = p.sketch(pl, [path], WHEEL(), centerline=WAX, name='Sk_tread_section')
    p.revolve(sk, name='Rev_tread')


def build_P08(p):
    hw = P['wheel_width'] / 2
    pl = wheel_plane(p)
    path = Path((P['insert_ri'], -hw)).L((P['insert_ro'], -hw)).L((P['insert_ro'], hw)).L((P['insert_ri'], hw)).close()
    sk = p.sketch(pl, [path], WHEEL(), centerline=WAX, name='Sk_insert_section')
    p.revolve(sk, name='Rev_insert')


def build_P09(p):
    sk = p.sketch(p.front, [], XY(), circles=[((AX[0], AX[1], 0), P['core_r'])], name='Sk_core')
    p.extrude(sk, 2 * P['core_half_width'], mid=True, name='Ext_core')


def build_H1(p):
    sk = p.sketch(p.front, [], XY(), circles=[((AX[0], AX[1], 0), P['axle_d'] / 2)], name='Sk_axle')
    p.extrude(sk, 2 * P['axle_half_len'], mid=True, name='Ext_axle')


def flange_path(sign):
    """P10 half section (rho, z) for sign=-1 (P10-a) or +1 (P10-b)."""
    hub, rim, zi = P['flange_hub_r'], P['core_r'], P['core_half_width']
    rr = P['flange_round']
    Rd, cz = P['flange_dish_R'], P['flange_dish_cz']
    # P10-a geometry (z<0), mirrored for P10-b
    dc = (hub, cz)                                  # dish circle centre (rho, z)
    c_rim = (rim - rr, -0.6106)                     # rim round centre
    c_hub = (hub + rr, -0.8049)                     # hub round centre

    def tang(c):
        dx, dz = c[0] - dc[0], c[1] - dc[1]
        L = math.hypot(dx, dz)
        return (dc[0] + Rd * dx / L, dc[1] + Rd * dz / L)
    t_rim, t_hub = tang(c_rim), tang(c_hub)
    path = (Path((hub, -zi)).L((rim, -zi)).L((rim, c_rim[1])).A(c_rim, t_rim)
            .A(dc, t_hub).A(c_hub, (hub, c_hub[1])).close())
    return path if sign < 0 else mirror_v(path)


def build_P10(p, sign):
    pl = wheel_plane(p)
    sk = p.sketch(pl, [flange_path(sign)], WHEEL(), centerline=WAX, name='Sk_flange_section')
    p.revolve(sk, name='Rev_flange')


def build_P10a(p):
    build_P10(p, -1)


def build_P10b(p):
    build_P10(p, +1)


from parts_b import *  # noqa: E402,F401,F403
from parts_fork import *  # noqa: E402,F401,F403
