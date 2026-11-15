// Generator for the SolidCraft command script of the swivel plate caster (spec.md).
// All spec values are inches; sketch point coordinates are passed to SolidCraft in mm (x 25.4),
// feature sizes (distances, radii, heights, fillet radii) are expressions over named parameters (design units = in).
// Usage: node gen.js [--no-fillets] > caster_script.json
const IN = 25.4;
const noFillets = process.argv.includes('--no-fillets');
const cmds = [];
const C = (command, params) => cmds.push({ command, params });
const mm = v => +(v * IN).toFixed(9);
const P = (x, y) => [mm(x), mm(y)];
const P3 = (x, y, z) => [mm(x), mm(y), mm(z)];

// ---------------------------------------------------------------- parameters (inches)
const params = [
  ['plate_top_y', 2.75, 'mounting face y (P02 top)'],
  ['plate_t', 0.1, 'top plate thickness (P02)'],
  ['plate_L', 3.625, 'top plate length along X (P02)'],
  ['plate_W', 2.5, 'top plate width along Z (P02)'],
  ['plate_corner_R', 0.25, 'plate corner round (P02)'],
  ['slot_w', 0.3125, 'mounting slot width (P02)'],
  ['fork_top_y', 2.464, 'fork top face y (P01)'],
  ['fork_W', 2.058, 'fork outer width 2 x 1.029 (P01 OUTER extrude)'],
  ['crown_R', 1.029, 'crown round radius behind swivel axis (P01)'],
  ['ridge_W', 2.266, 'width over ridges 2 x 1.133 (P01 RIDGE extrude)'],
  ['ridge_R', 1.133, 'crown ring band radius (P01)'],
  ['gap_W', 1.66, 'gap between fork legs 2 x 0.83 (P01 GAP)'],
  ['gap_R', 0.83, 'inner half-cylinder radius of the U (P01 GAP)'],
  ['kp_hole_D', 1.0, 'kingpin hole diameter in fork deck (P01 F4)'],
  ['axle_x', 1.515, 'swivel offset: wheel axis x'],
  ['axle_y', -0.75, 'wheel axis y'],
  ['axle_D', 0.6, 'axle pin / fork axle bore diameter (H1, P01 F5)'],
  ['axle_L', 2.068, 'axle pin length (H1)'],
  ['fork_R06', 0.06, 'fork edge round R0.06 (P01 F10)'],
  ['fork_R125', 0.125, 'fork leg end vertical edge round (P01 F10)'],
  ['ridge_R04', 0.04, 'ridge top edge round (P01 F10)'],
  ['hex_AF', 1.51, 'hex bearing ring across flats (P05)'],
  ['hex_t', 0.075, 'hex bearing ring thickness (P05)'],
  ['lug_h', 0.098, 'kingpin lug height 2.502..2.6 (P03 K2)'],
  ['pedal_W', 1.65, 'pedal stem width 2 x 0.825 (P06 B1)'],
  ['foot_W', 2.1, 'pedal foot plate width 2 x 1.05 (P06 B2)'],
  ['pedal_R04', 0.04, 'pedal foot plate edge round (P06 B2)'],
  ['rib_R', 0.025, 'grip rib radius (P06 B3)'],
  ['rib_stem_L', 1.35, 'stem rib length (P06 B3)'],
  ['rib_foot_L', 1.75, 'foot plate rib length (P06 B3)'],
  ['wheel_D', 4.0, 'wheel (tread) outer diameter (P07)'],
  ['wheel_W', 1.25, 'wheel / tread / insert width (P07, P08)'],
  ['tread_round_R', 0.2, 'tread outer edge round (P07)'],
  ['tread_bore_R', 1.56375, 'tread bore radius (P07)'],
  ['core_R', 1.51375, 'core / insert inner radius (P08, P09, P10)'],
  ['trim_eps', 0.0005, 'crown / ring trim cylinders are this much larger than the flat faces (avoids an exact tangency the kernel cannot cut)'],
  ['core_W', 0.625, 'core centre disc width (P09)'],
];
C('document.units', { units: 'in' });
for (const [name, v, comment] of params) C('parameters.add', { name, expression: `${v} in`, comment });

// ---------------------------------------------------------------- sketch helpers
let sk = 0;
function sketch(plane, name) { C('sketch.create', { plane, name }); return name; }
function finish() { C('sketch.finish', {}); }
const XY = 'XY';
// top-view plane at height y: sketch (x, y) = world (X, Z), normal -Y
const topPlane = y => ({ origin: P3(0, y, 0), x_dir: [1, 0, 0], y_dir: [0, 0, 1] });
// wheel plane: sketch (x, y) = (rho, z) about the wheel axis
const wheelPlane = () => ({ origin: P3(1.515, -0.75, 0), x_dir: [1, 0, 0], y_dir: [0, 0, 1] });

// contour: start point (inches) + segments ['L', [x,y]] | ['A', [cx,cy], [x,y], 'cw'|'ccw']
// Arc ends are projected onto the circle through the arc start (spec values are rounded to 1e-5).
// The last segment should be a line so the loop closes exactly on the start point.
function contour(start, segs) {
  let cur = start.slice();
  const s0 = start.slice();
  segs.forEach((s, i) => {
    const last = i === segs.length - 1;
    if (s[0] === 'L') {
      const to = last ? s0 : s[1];
      C('sketch.line', { points: [P(...cur), P(...to)] });
      cur = to.slice();
    } else {
      const [, c, end, dir] = s;
      const R = Math.hypot(cur[0] - c[0], cur[1] - c[1]);
      let to;
      if (last) to = s0; else {
        const a = Math.atan2(end[1] - c[1], end[0] - c[0]);
        to = [c[0] + R * Math.cos(a), c[1] + R * Math.sin(a)];
      }
      const p = { center: P(...c), start: P(...cur), end: P(...to) };
      if (dir === 'cw') p.clockwise = true;
      C('sketch.arc.center_point', p);
      cur = to;
    }
  });
}
function arcMid(c, a, b, dir) { // midpoint of arc from a to b about c (inches)
  let t0 = Math.atan2(a[1] - c[1], a[0] - c[0]), t1 = Math.atan2(b[1] - c[1], b[0] - c[0]);
  const R = Math.hypot(a[0] - c[0], a[1] - c[1]);
  if (dir === 'ccw') { while (t1 < t0) t1 += 2 * Math.PI; } else { while (t1 > t0) t1 -= 2 * Math.PI; }
  const t = (t0 + t1) / 2; return [c[0] + R * Math.cos(t), c[1] + R * Math.sin(t)];
}
const extrude = (sketchName, distance, body_name, extra = {}) =>
  C('solid.extrude', Object.assign({ sketch: sketchName, distance, direction: 'symmetric', operation: 'new', body_name, name: body_name + '_extrude' }, extra));
const revolveY = (sketchName, body_name, extra = {}) =>
  C('solid.revolve', Object.assign({ sketch: sketchName, axis: 'Y', operation: 'new', body_name, name: body_name + '_revolve' }, extra));
const revolveWheel = (sketchName, body_name, extra = {}) =>
  C('solid.revolve', Object.assign({ sketch: sketchName, axis: 'y', operation: 'new', body_name, name: body_name + '_revolve' }, extra));
const cut = (target, tool) => C('solid.combine', { target, tools: [tool], operation: 'cut', keep_tools: false });
const join = (target, tool) => C('solid.combine', { target, tools: [tool], operation: 'join', keep_tools: false });
const intersect = (target, tool) => C('solid.combine', { target, tools: [tool], operation: 'intersect', keep_tools: false });

// ================================================================ P01 FORK
const A = [1.01841, -0.80829];
const R25c = [-1.46454, -1.09977], R8622c = [0.13847, -6.14324];
const Pout = [
  ['L', [-1.2, 1.3862]],
  ['A', R25c, A, 'cw'],
  ['A', [1.515, -0.75], [1.515, -1.25], 'ccw'],
  ['A', [1.515, -0.6992], [2.0658, -0.6992], 'ccw'],
  ['L', [2.06496, 0.58138]],
  ['A', [2.74786, 0.56946], [2.72879, 1.25219], 'cw'],
  ['L', [3.54269, 1.27493]],
  ['A', [3.5385, 1.42487], [3.6885, 1.42487], 'ccw'],
  ['L', [3.6885, 1.61657]],
  ['A', [3.5385, 1.61657], [3.5987, 1.75396], 'ccw'],
  ['A', R8622c, [1.28005, 2.40286], 'ccw'],
  ['L', [1.221, 2.464]],
  ['L', [-1.2, 2.464]],
];
sketch(XY, 'S_P01_outer'); contour([-1.2, 2.464], Pout); finish();
extrude('S_P01_outer', 'fork_W', 'P01_Fork');
// trim behind the swivel axis: keep x >= 0 plus the inside of cylinder R crown_R about Y
C('solid.box', { length: '4 in', width: '8 in', height: '4 in', center: P3(-2, 0, 0), operation: 'new', body_name: 'T_back1', name: 'T_back1' });
C('solid.cylinder', { radius: 'crown_R + trim_eps', height: '8 in', base: P3(0, -4, 0), axis: 'Y', operation: 'new', body_name: 'T_cyl1', name: 'T_cyl1' });
cut('T_back1', 'T_cyl1');
cut('P01_Fork', 'T_back1');

// RIDGE
const Rxy = [
  ['L', [0.21544, 2.098]],
  ['A', [0.21544, 0.798], [0.42225, 2.08144], 'cw'],
  ['A', [0.18362, 0.60055], [1.656, 0.314], 'cw'],
  ['A', [1.471, 0.314], [1.286, 0.314], 'cw'],
  ['A', [-0.40784, 0.16942], [1.2176, 0.66736], 'ccw'],
  ['A', [-0.21661, 0.228], [-0.21661, 1.728], 'ccw'],
  ['L', [-1.2, 1.728]],
  ['L', [-1.2, 2.098]],
];
sketch(XY, 'S_P01_ridge'); contour([-1.2, 2.098], Rxy); finish();
extrude('S_P01_ridge', 'ridge_W', 'P01_Ridge');
C('solid.box', { length: '4 in', width: '8 in', height: '4 in', center: P3(-2, 0, 0), operation: 'new', body_name: 'T_back2', name: 'T_back2' });
C('solid.cylinder', { radius: 'ridge_R + trim_eps', height: '8 in', base: P3(0, -4, 0), axis: 'Y', operation: 'new', body_name: 'T_cyl2', name: 'T_cyl2' });
cut('T_back2', 'T_cyl2');
cut('P01_Ridge', 'T_back2');
join('P01_Fork', 'P01_Ridge');

// GAP (|z| < 0.83)
const R8342c = R8622c;
sketch(XY, 'S_P01_gap');
contour([-1.0, -2], [
  ['L', [-1.0, 2.184]],
  ['L', [1.10215, 2.184]],
  ['L', [1.14698, 2.13758]],
  ['A', R8342c, [2.4615, 1.86879], 'cw'],
  ['L', [2.4615, 3.0]],
  ['L', [5.0, 3.0]],
  ['L', [5.0, -2]],
  ['L', [-1.0, -2]],
]);
finish();
extrude('S_P01_gap', 'gap_W', 'T_gap');
// plan of the gap: half disc R gap_R behind the swivel axis + band |z| < 0.83 in front (one tangent-continuous loop)
sketch(topPlane(0.5), 'S_P01_gap_plan');
contour([5.0, -0.83], [
  ['L', [5.0, 0.83]],
  ['L', [0, 0.83]],
  ['A', [0, 0], [0, -0.83], 'ccw'],
  ['L', [5.0, -0.83]],
]);
finish();
extrude('S_P01_gap_plan', '7 in', 'T_gap_plan');
intersect('T_gap', 'T_gap_plan');
cut('P01_Fork', 'T_gap');
// F4 kingpin hole, F5 axle bore
C('solid.cylinder', { diameter: 'kp_hole_D', height: '1 in', base: P3(0, 2.0, 0), axis: 'Y', operation: 'new', body_name: 'T_kphole', name: 'T_kphole' });
cut('P01_Fork', 'T_kphole');
C('solid.cylinder', { diameter: 'axle_D', height: '3 in', base: P3(1.515, -0.75, -1.5), axis: 'Z', operation: 'new', body_name: 'T_axlebore', name: 'T_axlebore' });
cut('P01_Fork', 'T_axlebore');

// F10 edge rounds (points on edges, mm)
function forkFillets() {
  const zf = 1.029, zr = 1.133;
  const e06 = [];
  // P_out boundary edges for x >= 0 (on both outer faces)
  const outSegs = [
    arcMid(R25c, [0.0, 0.92634], A, 'cw'),
    arcMid([1.515, -0.75], A, [1.515, -1.25], 'ccw'),
    arcMid([1.515, -0.6992], [1.515, -1.25], [2.0658, -0.6992], 'ccw'),
    [2.06538, 0.0],
    arcMid([2.74786, 0.56946], [2.06496, 0.58138], [2.72879, 1.25219], 'cw'),
    [3.1357, 1.26356],
    arcMid([3.5385, 1.42487], [3.54269, 1.27493], [3.6885, 1.42487], 'ccw'),
    arcMid([3.5385, 1.61657], [3.6885, 1.61657], [3.5987, 1.75396], 'ccw'),
    arcMid(R8622c, [3.5987, 1.75396], [1.28005, 2.40286], 'ccw'),
    [1.2505, 2.43343],
    [0.6, 2.464],
  ];
  for (const s of [1, -1]) for (const p of outSegs) e06.push(P3(p[0], p[1], s * zf));
  // top face with the crown round, R2.5 wall with the crown round (behind x = 0)
  e06.push(P3(-1.029, 2.464, 0));
  e06.push(P3(-1.029, -1.09977 + Math.sqrt(6.25 - Math.pow(-1.029 + 1.46454, 2)), 0));
  return e06;
}
function ridgeFillets() {
  const zr = 1.133, e = [];
  const segs = [
    [0.1, 2.098],
    arcMid([0.21544, 0.798], [0.21544, 2.098], [0.42225, 2.08144], 'cw'),
    arcMid([0.18362, 0.60055], [0.42225, 2.08144], [1.656, 0.314], 'cw'),
    [1.471, 0.129],
    arcMid([-0.40784, 0.16942], [1.286, 0.314], [1.2176, 0.66736], 'ccw'),
    arcMid([-0.21661, 0.228], [1.2176, 0.66736], [0.0, 1.71227], 'ccw'),
  ];
  for (const s of [1, -1]) for (const p of segs) e.push(P3(p[0], p[1], s * zr));
  e.push(P3(-1.133, 2.098, 0));
  e.push(P3(-1.133, 1.728, 0));
  return e;
}
// SIMPLIFIED F10: this SolidCraft fillet kernel only blends these edges (tested edge by edge, see build_log.md):
// R0.06 on the R8.622 top edges and on the flat top (y 2.464) edges of the two outer faces.
// All other F10 rounds (R0.06 side walls / crown, R0.125 leg end, R0.04 ridge) fail in the kernel and are left sharp.
if (!noFillets) {
  const e = forkFillets();
  C('solid.fillet', { body: 'P01_Fork', edges: [e[8], e[19]], radius: 'fork_R06', name: 'P01_round_R006_topR8622' });
  C('solid.fillet', { body: 'P01_Fork', edges: [e[10], e[21]], radius: 'fork_R06', name: 'P01_round_R006_topflat' });
}

// ================================================================ P02 TOP PLATE
sketch({ origin: P3(0, 2.7, 0), x_dir: [1, 0, 0], y_dir: [0, 0, 1] }, 'S_P02_plate');
C('sketch.rectangle.rounded', { p0: P(-1.8125, -1.25), p1: P(1.8125, 1.25), radius: 'plate_corner_R' });
for (const sx of [1, -1]) for (const sz of [1, -1])
  C('sketch.slot.center_to_center', { p0: P(sx * 1.40625, sz * 0.875), p1: P(sx * 1.53125, sz * 0.875), width: mm(0.3125) });
C('sketch.circle.center', { center: P(0, 0), radius: mm(0.75) });
finish();
extrude('S_P02_plate', 'plate_t', 'P02_TopPlate');
sketch(XY, 'S_P02_press');
contour([0.8, 2.75], [
  ['L', [0.719, 2.75]],
  ['A', [0.719, 2.5], [0.57754, 2.70610], 'ccw'],
  ['L', [0.37560, 2.56750]],
  ['A', [0.319, 2.65], [0.3595, 2.55860], 'cw'],
  ['L', [0.3595, 2.502]],
  ['L', [0.3605, 2.502]],
  ['A', [0.3605, 2.487], [0.3755, 2.487], 'cw'],
  ['L', [0.3755, 2.45330]],
  ['A', [0.35, 2.55], [0.40660, 2.46750], 'ccw'],
  ['L', [0.60855, 2.60610]],
  ['A', [0.75, 2.4], [0.75, 2.65], 'cw'],
  ['L', [0.8, 2.65]],  // overlap 0.05 into the flat plate (avoids coincident cylinder faces in the union)
  ['L', [0.8, 2.75]],
]);
finish();
revolveY('S_P02_press', 'T_press');
join('P02_TopPlate', 'T_press');

// ================================================================ P03 KINGPIN
sketch(XY, 'S_P03_pin');
contour([0, 2.75], [
  ['L', [0, 2.136]],
  ['L', [0.236, 2.0728]],
  ['L', [0.236, 1.7767]],
  ['L', [0.2557, 1.757]],
  ['L', [0.2732, 1.757]],
  ['L', [0.29285, 1.7767]],
  ['L', [0.29285, 2.367]],
  ['A', [0.30785, 2.367], [0.30785, 2.382], 'cw'],
  ['L', [0.3605, 2.382]],
  ['A', [0.3605, 2.397], [0.3755, 2.397], 'ccw'],
  ['L', [0.3755, 2.487]],
  ['A', [0.3605, 2.487], [0.3605, 2.502], 'ccw'],
  ['L', [0.3115, 2.502]],
  ['A', [0.3115, 2.517], [0.2965, 2.517], 'cw'],
  ['L', [0.2965, 2.7303]],
  ['L', [0.2768, 2.75]],
  ['L', [0, 2.75]],
]);
finish();
revolveY('S_P03_pin', 'P03_Kingpin');
// K2 lug, plan (x, z), closed through the inside of the upper shank
sketch(topPlane(2.525), 'S_P03_lug'); // lug y 2.45..2.6: the part below 2.502 lies inside the collar (avoids a coplanar union)
// SIMPLIFIED: boss circle R0.063 only; the two concave R0.0394 junction rounds (tangent to the shank) are left out,
// because the kernel cannot union the tangent junction (volume effect ~1e-4 in3)
C('sketch.circle.center', { center: P(-0.2965, 0), radius: mm(0.063) });
finish();
extrude('S_P03_lug', 'lug_h + 0.052 in', 'T_lug');
join('P03_Kingpin', 'T_lug');

// ================================================================ P04 BEARING WASHER
sketch(XY, 'S_P04');
contour([0.401, 2.464], [
  ['L', [0.872, 2.464]],
  ['L', [0.872, 2.539]],
  ['L', [0.5107, 2.539]],
  ['L', [0.4066, 2.4675]],
  ['A', [0.35, 2.55], [0.401, 2.464], 'cw'],
]);
finish();
revolveY('S_P04', 'P04_BearingWasher');

// ================================================================ P05 HEX BEARING RING
sketch(topPlane(2.5765), 'S_P05_hex');
C('sketch.polygon.circumscribed', { center: P(0, 0), radius: mm(0.755), sides: 6, angle: 30 });
finish();
extrude('S_P05_hex', 'hex_t', 'P05_HexRing');
sketch(XY, 'S_P05_bore');
contour([0, 2.539], [
  ['L', [0.5107, 2.539]],
  ['L', [0.60855, 2.6061]],
  ['A', [0.75, 2.4], [0.75 + 0.25 * Math.cos(110 * Math.PI / 180), 2.4 + 0.25 * Math.sin(110 * Math.PI / 180)], 'cw'], // runs on past the top face y 2.614
  ['L', [0, 2.4 + 0.25 * Math.sin(110 * Math.PI / 180)]],
  ['L', [0, 2.539]],
]);
finish();
revolveY('S_P05_bore', 'T_hexbore');
cut('P05_HexRing', 'T_hexbore');

// ================================================================ P06 BRAKE PEDAL
sketch(XY, 'S_P06_stem');
contour([2.4615, 2.15992], [
  ['A', R8622c, [3.5987, 1.75396], 'cw'],
  ['A', [3.5385, 1.6166], [3.60992, 1.74847], 'cw'],
  ['A', [0.03345, -6.51039], [3.6885, 1.714], 'cw'],
  ['L', [3.6885, 1.42487]],
  ['A', [3.5385, 1.42487], [3.54269, 1.27493], 'cw'],
  ['L', [2.72879, 1.25219]],
  ['A', [2.74786, 0.56946], [2.4615, 1.18953], 'ccw'],
  ['L', [2.4615, 2.15992]],
]);
finish();
extrude('S_P06_stem', 'pedal_W', 'P06_BrakePedal');
sketch(XY, 'S_P06_foot_side');
contour([3.6885, 1.65822], [
  ['A', [3.7385, 1.65822], [3.74187, 1.70811], 'cw'],
  ['A', [3.7857, 2.3496], [4.08040, 1.77815], 'ccw'],
  ['A', [4.1485, 1.6445], [4.2985, 1.6445], 'cw'],
  ['L', [4.2985, 1.3945]],
  ['A', [4.1485, 1.3945], [4.0804, 1.26085], 'cw'],
  ['A', [3.7857, 0.6894], [3.74187, 1.33089], 'ccw'],
  ['A', [3.7385, 1.38078], [3.6885, 1.38078], 'cw'],
  ['L', [3.6885, 1.65822]],
]);
finish();
extrude('S_P06_foot_side', 'foot_W + 0.2 in', 'T_foot'); // wider than the plan: the flats z = +/-1.05 come from the plan (no coplanar faces)
sketch(topPlane(1.5195), 'S_P06_foot_plan');
// back line (x 3.6885) and front line (x 4.2985) are taken from the side profile; the plan loop is pushed
// out there (to x 3.6 / 4.4) so the intersect has no coplanar faces
// SIMPLIFICATION: the back R0.04 corner centres are moved 0.001 to -X and the front R0.25 corner centres 0.004
// to +X, so these arcs cross the side profile's back/front planes instead of touching them tangentially
// (the kernel's intersect fails on the exact tangency). Shape change <= 0.001 in.
const fc = 4.0485 + 0.004, bc = 3.7285 - 0.001;
contour([4.4, -0.5657], [
  ['L', [4.4, 0.5657]],
  ['L', [fc + Math.hypot(4.25988 - fc, 0.69922 - 0.5657), 0.5657]],
  ['A', [fc, 0.5657], [4.25988, 0.69922], 'ccw'],
  ['A', [3.4144, 0.1653], [3.94710, 1.01157], 'ccw'],
  ['A', [3.8139, 0.8], [3.8139, 1.05], 'ccw'],
  ['L', [bc, 1.05]],
  ['A', [bc, 1.01], [bc - 0.04, 1.01], 'ccw'],
  ['L', [3.6, 1.01]],
  ['L', [3.6, -1.01]],
  ['L', [bc - 0.04, -1.01]],
  ['A', [bc, -1.01], [bc, -1.05], 'ccw'],
  ['L', [3.8139, -1.05]],
  ['A', [3.8139, -0.8], [3.94710, -1.01157], 'ccw'],
  ['A', [3.4144, -0.1653], [4.25988, -0.69922], 'ccw'],
  ['A', [fc, -0.5657], [4.2985, -0.5657], 'ccw'],
  ['L', [4.4, -0.5657]],
]);
finish();
extrude('S_P06_foot_plan', '1 in', 'T_footplan');
intersect('T_foot', 'T_footplan');
// SIMPLIFIED B2: the R0.04 foot plate rounds fail in this fillet kernel ("only straight edges can be blended"),
// so they are not built; the edge list is kept here, switched off (set tryPedalRounds = true to retry).
const tryPedalRounds = false;
if (!noFillets && tryPedalRounds) {
  // R0.04 where the plan side faces meet the top / bottom of the side profile
  const e = [];
  const topY = x => 2.3496 - Math.sqrt(0.643 * 0.643 - (x - 3.7857) ** 2);
  const botY = x => 0.6894 + Math.sqrt(0.643 * 0.643 - (x - 3.7857) ** 2);
  for (const s of [1, -1]) {
    // flats z = +/-1.05 (x 3.7285..3.8139)
    e.push(P3(3.78, topY(3.78), s * 1.05), P3(3.78, botY(3.78), s * 1.05));
    // R0.25 c=(3.8139, 0.8)
    let m = arcMid([3.8139, 0.8], [3.8139, 1.05], [3.9471, 1.01157], 'cw');
    e.push(P3(m[0], topY(m[0]), s * m[1]), P3(m[0], botY(m[0]), s * m[1]));
    // R1.0
    m = arcMid([3.4144, 0.1653], [3.9471, 1.01157], [4.25988, 0.69922], 'cw');
    e.push(P3(m[0], topY(m[0]), s * m[1]), P3(m[0], botY(m[0]), s * m[1]));
  }
  C('solid.fillet', { body: 'T_foot', edges: e, radius: 'pedal_R04', name: 'P06_round_R004', fit: 'exact' });
}
join('P06_BrakePedal', 'T_foot');
const ribs = [[2.5865, 2.1107, 'rib_stem_L', 0.675], [2.7115, 2.0682, 'rib_stem_L', 0.675], [2.8365, 2.0334, 'rib_stem_L', 0.675],
  [3.7885, 1.7045, 'rib_foot_L', 0.875], [3.8885, 1.7140, 'rib_foot_L', 0.875], [3.9885, 1.7376, 'rib_foot_L', 0.875]];
ribs.forEach(([x, y, L, hz], i) => {
  C('solid.cylinder', { radius: 'rib_R', height: L, base: P3(x, y, -hz), axis: 'Z', operation: 'new', body_name: `T_rib${i + 1}`, name: `P06_rib${i + 1}` });
  join('P06_BrakePedal', `T_rib${i + 1}`);
});

// ================================================================ WHEEL (about x = 1.515, y = -0.75, along Z)
sketch(wheelPlane(), 'S_P07_tread');
contour([1.56375, 0.625], [
  ['L', [1.56375, -0.625]],
  ['L', [1.8, -0.625]],
  ['A', [1.8, -0.425], [2.0, -0.425], 'ccw'],
  ['L', [2.0, 0.425]],
  ['A', [1.8, 0.425], [1.8, 0.625], 'ccw'],
  ['L', [1.56375, 0.625]],
]);
finish();
revolveWheel('S_P07_tread', 'P07_WheelTread');

sketch(wheelPlane(), 'S_P08_insert');
C('sketch.rectangle.two_point', { p0: P(1.51375, -0.625), p1: P(1.56375, 0.625) });
finish();
revolveWheel('S_P08_insert', 'P08_WheelInsertRing');

C('solid.cylinder', { radius: 'core_R', height: 'core_W', base: P3(1.515, -0.75, -0.3125), axis: 'Z', operation: 'new', body_name: 'P09_WheelCoreDisc', name: 'P09_WheelCoreDisc' });

// P10 flanges: dish torus arc R3.75269 about (0.305, +/-2.9277), R0.02 rounds tangent to it
function flange(sz, name) {
  const Cd = [0.305, sz * 2.9277], Rd = 3.75269;
  const tp = rc => { const dx = rc[0] - Cd[0], dy = rc[1] - Cd[1], d = Math.hypot(dx, dy); return [Cd[0] + dx * Rd / d, Cd[1] + dy * Rd / d]; };
  const rcRim = [1.49375, sz * -0.6106], rcHub = [0.325, sz * -0.8049];
  const tRim = tp(rcRim), tHub = tp(rcHub);
  const cw = sz > 0 ? 'cw' : 'ccw', ccw = sz > 0 ? 'ccw' : 'cw';
  sketch(wheelPlane(), 'S_' + name);
  contour([0.305, sz * -0.3125], [
    ['L', [1.51375, sz * -0.3125]],
    ['L', [1.51375, sz * -0.6106]],
    ['A', rcRim, tRim, cw],
    ['A', Cd, tHub, cw],
    ['A', rcHub, [0.305, sz * -0.8049], cw],
    ['L', [0.305, sz * -0.3125]],
  ]);
  finish();
  revolveWheel('S_' + name, name);
}
flange(1, 'P10a_CoreFlange_negZ');
flange(-1, 'P10b_CoreFlange_posZ');

// ================================================================ H1 AXLE PIN
C('solid.cylinder', { diameter: 'axle_D', height: 'axle_L', base: P3(1.515, -0.75, -1.034), axis: 'Z', operation: 'new', body_name: 'H1_AxlePin', name: 'H1_AxlePin' });

process.stdout.write(JSON.stringify({ commands: cmds }, null, 1));
