"""P01 fork builder: F = (OUTER + RIDGE) - GAP - holes, then edge rounds (spec 4/P01)."""
from swlib import Path, XY, XZ, RY, C, edge_faces, face_info, is_tangent, edge_mid
from parts import P, AX, YAX


def back_trim(R):
    """(x,z) region x<0 outside the circle R about the Y axis (Top plane sketch)."""
    B = 1.7
    return (Path((0, R)).L((0, B)).L((-B, B)).L((-B, -B)).L((0, -B)).L((0, -R))
            .A((0, 0), (0, R), thru=(-R, 0)))


def build_P01(p, rounds=True):
    hw, hr, hg = P['fork_half_width'], P['ridge_half_width'], P['fork_inner_half_gap']
    TOPC = (0.13847, -6.14324)
    # F1 outer side profile
    pout = (Path((1.01841, -0.80829)).A(AX, (1.515, -1.25), 'ccw')
            .A((1.515, -0.6992), (2.0658, -0.6992), 'ccw').L((2.06496, 0.58138))
            .A((2.74786, 0.56946), (2.72879, 1.25219), 'cw').L((3.54269, 1.27493))
            .A((3.5385, 1.42487), (3.6885, 1.42487), 'ccw').L((3.6885, 1.61657))
            .A((3.5385, 1.61657), (3.5987, 1.75396), 'ccw').A(TOPC, (1.28005, 2.40286), 'ccw')
            .L((1.221, 2.464)).L((-1.2, 2.464)).L((-1.2, 1.3862))
            .A((-1.46454, -1.09977), (1.01841, -0.80829), 'cw'))
    sk = p.sketch(p.front, [pout], XY(), name='Sk_P_out')
    p.extrude(sk, 2 * hw, mid=True, name='Ext_OUTER')
    sk = p.sketch(p.top, [back_trim(P['crown_R'])], XZ(0), name='Sk_trim_crown')
    p.cut(sk, through_both=True, name='Cut_trim_crown')
    # F2 ridge
    ridge = (Path((-1.2, 2.098)).L((0.21544, 2.098)).A((0.21544, 0.798), (0.42225, 2.08144), 'cw')
             .A((0.18362, 0.60055), (1.656, 0.314), 'cw').A((1.471, 0.314), (1.286, 0.314), 'cw')
             .A((-0.40784, 0.16942), (1.2176, 0.66736), 'ccw').A((-0.21661, 0.228), (-0.21661, 1.728), 'ccw')
             .L((-1.2, 1.728)).close())
    sk = p.sketch(p.front, [ridge], XY(), name='Sk_R_xy')
    p.extrude(sk, 2 * hr, mid=True, name='Ext_RIDGE')
    sk = p.sketch(p.top, [back_trim(P['ridge_R'])], XZ(0), name='Sk_trim_ridge')
    p.cut(sk, through_both=True, name='Cut_trim_ridge')
    # F3 gap between the legs
    cy = P['ceiling_y']
    gap = (Path((0, -1.6)).L((0, cy)).L((1.10215, cy)).L((1.14698, 2.13758))
           .A(TOPC, (P['gap_end_x'], 1.86879), 'cw').L((P['gap_end_x'], 2.8)).L((4.0, 2.8)).L((4.0, -1.6)).close())
    sk = p.sketch(p.front, [gap], XY(), name='Sk_gap_front')
    p.cut(sk, 2 * hg, mid=True, name='Cut_GAP_front')
    # back part of the gap: cylinder R0.83 about Y from below the fork up to the ceiling (revolve cut)
    gb = Path((0, -1.6)).L((P['gap_R'], -1.6)).L((P['gap_R'], cy)).L((0, cy)).close()
    sk = p.sketch(p.front, [gb], RY(), centerline=YAX, name='Sk_gap_back')
    p.revolve(sk, cut=True, name='Cut_GAP_back')
    # F4 kingpin hole, F5 axle bore
    sk = p.sketch(p.top, [], XZ(0), circles=[((0, 0, 0), P['kingpin_hole_d'] / 2)], name='Sk_kingpin_hole')
    p.cut(sk, through_both=True, name='Cut_kingpin_hole')
    sk = p.sketch(p.front, [], XY(), circles=[((AX[0], AX[1], 0), P['axle_bore_d'] / 2)], name='Sk_axle_bore')
    p.cut(sk, through_both=True, name='Cut_axle_bore')
    if rounds:
        fork_rounds(p)


# ---------------------------------------------------------------------------------------------
def _cls(fi):
    t, b = fi['type'], fi['box']
    if t == 'plane':
        n = fi['n']
        if abs(abs(n[2]) - 1) < 1e-6:
            z = fi['p'][2]
            if abs(abs(z) - P['fork_half_width']) < 1e-4:
                return 'outer'
            if abs(abs(z) - P['ridge_half_width']) < 1e-4:
                return 'bandtop'
            if abs(abs(z) - P['fork_inner_half_gap']) < 1e-4:
                return 'inner'
        if abs(abs(n[1]) - 1) < 1e-6:
            y = fi['p'][1]
            if abs(y - P['deck_top_y']) < 1e-4:
                return 'top'
            if abs(y - 1.728) < 1e-4 or abs(y - 2.098) < 1e-4:
                return 'ridgewall'
            if abs(y - P['ceiling_y']) < 1e-4:
                return 'ceiling'
        if abs(abs(n[0]) - 1) < 1e-6 and abs(fi['p'][0] - P['leg_end_x']) < 1e-4:
            return 'legend'
        if abs(n[0] - 0.7193) < 2e-3 and abs(n[1] - 0.6947) < 2e-3:
            return 'bevel'
    if t == 'cyl':
        a, r = fi['a'], fi['r']
        if abs(abs(a[1]) - 1) < 1e-6 and abs(fi['o'][0]) < 1e-6 and abs(fi['o'][2]) < 1e-6:
            if abs(r - P['crown_R']) < 1e-4:
                return 'crown'
            if abs(r - P['ridge_R']) < 1e-4:
                return 'ring'
            if abs(r - 0.5) < 1e-4:
                return 'kphole'
            if abs(r - P['gap_R']) < 1e-4:
                return 'gapcyl'
        if abs(abs(a[2]) - 1) < 1e-6 and abs(r - 0.3) < 1e-4:
            return 'bore'
    # remaining faces: is it a ridge band wall? (spans only 1.029 <= |z| <= 1.133)
    zlo, zhi = min(abs(b[2]), abs(b[5])), max(abs(b[2]), abs(b[5]))
    if b[2] * b[5] > 0 and zlo > P['fork_half_width'] - 1e-3 and zhi < P['ridge_half_width'] + 1e-3:
        return 'ridgewall'
    return 'wall'


def _edges_with_classes(p):
    out = []
    for e in p.edges():
        fs = edge_faces(e)
        fis = [face_info(f) for f in fs]
        out.append((e, fis, [_cls(fi) for fi in fis]))
    return out


def sel_leg_end(p):
    return [e for e, fis, c in _edges_with_classes(p) if sorted(c) == ['legend', 'outer']]


def sel_r006(p):
    sel = []
    for e, fis, c in _edges_with_classes(p):
        a, b = c
        s = set(c)
        skin = {'outer', 'crown', 'top'}
        if not (s & skin):
            continue
        if s & {'ridgewall', 'bore', 'kphole', 'legend', 'bandtop', 'ring', 'inner', 'gapcyl', 'ceiling'}:
            continue
        if s == {'top', 'bevel'}:
            continue
        if a in skin and b in skin and not ({a, b} in ({'top', 'outer'}, {'top', 'crown'})):
            continue
        if is_tangent(e, fis[0], fis[1]):
            continue
        sel.append(e)
    return sel


def sel_r004(p):
    sel = []
    for e, fis, c in _edges_with_classes(p):
        s = set(c)
        if 'bandtop' in s and len(s) == 2 and not (s & {'outer', 'ring'}):
            if not is_tangent(e, fis[0], fis[1]):
                sel.append(e)
        elif s == {'ring', 'ridgewall'}:
            sel.append(e)
    return sel


def fork_rounds(p):
    import time
    steps = [('Fillet_leg_end_R0_125', sel_leg_end, P['leg_end_round']),
             ('Fillet_ridge_R0_04', sel_r004, P['ridge_round']),
             ('Fillet_outer_R0_06', sel_r006, P['fork_round'])]
    for name, fsel, r in steps:
        t0 = time.time()
        edges = fsel(p)
        print("  %s: %d edges (select %.1fs)" % (name, len(edges), time.time() - t0), flush=True)
        mids0 = [edge_mid(e) for e in edges]
        try:
            p.fillet(edges, r, name=name)
            p.LOG.append('%s OK (%d edges)' % (name, len(edges)))
            print("   ok %.1fs" % (time.time() - t0), flush=True)
        except Exception as ex:
            print("   failed:", ex, flush=True)
            p.LOG.append('%s FAILED with all %d edges: %s' % (name, len(edges), ex))
        if not name.startswith('Fillet_outer') or ('OK' in p.LOG[-1]):
            continue
        # fallback: one fillet feature per edge, edges re-selected by their mid points
        mids = mids0
        nok = 0
        for k, m in enumerate(mids):
            if p.fillet_at(m, r, name='%s_e%02d' % (name, k)):
                nok += 1
        p.LOG.append('%s fallback per edge: %d of %d edges rounded' % (name, nok, len(mids)))
        print("   fallback per edge: %d/%d ok (%.1fs)" % (nok, len(mids), time.time() - t0), flush=True)
