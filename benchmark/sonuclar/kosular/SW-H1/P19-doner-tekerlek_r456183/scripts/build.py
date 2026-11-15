"""Build caster parts in SolidWorks, measure against spec targets, save .SLDPRT.

usage: python build.py [ID ...]      (no IDs = all parts)
"""
import json
import os
import sys
import traceback

import swlib
import parts

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..'))

# ID: (file name, builder, target vol, com, bbox[xmin,xmax,ymin,ymax,zmin,zmax], area)
TARGETS = {
    'P01': ('P01_Fork', 'build_P01', 5.06749, (0.9987, 1.5153, 0), (-1.1330, 3.6885, -1.25, 2.464, -1.133, 1.133), 50.1952),
    'P02': ('P02_TopPlate', 'build_P02', 0.83205, (0, 2.6876, 0), (-1.8125, 1.8125, 2.4533, 2.75, -1.25, 1.25), 18.5321),
    'P03': ('P03_Kingpin', 'build_P03', 0.23072, (-0.0009, 2.3584, 0), (-0.3755, 0.3755, 1.757, 2.75, -0.3755, 0.3755), 3.1492),
    'P04': ('P04_BearingWasher', 'build_P04', 0.12992, (0, 2.5004, 0), (-0.872, 0.872, 2.464, 2.539, -0.872, 0.872), 4.2445),
    'P05': ('P05_HexBearingRing', 'build_P05', 0.07254, (0, 2.5740, 0), (-0.8718, 0.8718, 2.539, 2.614, -0.755, 0.755), 2.7849),
    'P06': ('P06_BrakePedal', 'build_P06', 1.90479, (3.2588, 1.5941, 0), (2.4615, 4.2985, 1.1895, 2.1599, -1.05, 1.05), 11.7309),
    'P07': ('P07_WheelTread', 'build_P07', 5.89220, (1.515, -0.75, 0), (-0.485, 3.515, -2.75, 1.25, -0.625, 0.625), 35.5529),
    'P08': ('P08_WheelInsertRing', 'build_P08', 0.60427, (1.515, -0.75, 0), (-0.0487, 3.0787, -2.3138, 0.8137, -0.625, 0.625), 25.1375),
    'P09': ('P09_WheelCoreDisc', 'build_P09', 4.49923, (1.515, -0.75, 0), (0.0013, 3.0288, -2.2638, 0.7638, -0.3125, 0.3125), 20.3420),
    'P10a': ('P10a_CoreFlange_negZ', 'build_P10a', 2.93150, (1.515, -0.75, -0.529), (0.0013, 3.0288, -2.2638, 0.7638, -0.8249, -0.3125), 17.8824),
    'P10b': ('P10b_CoreFlange_posZ', 'build_P10b', 2.93150, (1.515, -0.75, 0.529), (0.0013, 3.0288, -2.2638, 0.7638, 0.3125, 0.8249), 17.8824),
    'H1': ('H1_AxlePin', 'build_H1', 0.58471, (1.515, -0.75, 0), (1.215, 1.815, -1.05, -0.45, -1.034, 1.034), 4.4636),
}
ORDER = ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10a', 'P10b', 'H1']


def build_one(pid, keep_open=False):
    fname, fn, tv, tcom, tbox, tarea = TARGETS[pid]
    p = swlib.Part(fname)
    res = {'id': pid, 'file': fname + '.SLDPRT'}
    try:
        getattr(parts, fn)(p)
        p.rebuild()
        m = swlib.measure(p)
        res.update(m)
        res['dvol_pct'] = 100 * (m['vol'] - tv) / tv
        res['darea_pct'] = 100 * (m['area'] - tarea) / tarea
        res['dcom'] = max(abs(a - b) for a, b in zip(m['com'], tcom))
        res['dbox'] = max(abs(a - b) for a, b in zip(m['box'], tbox))
        res['target'] = dict(vol=tv, area=tarea, com=tcom, box=tbox)
        p.save(os.path.join(OUT, fname + '.SLDPRT'))
        res['ok'] = True
        res['log'] = p.LOG
    except Exception as e:
        traceback.print_exc()
        res['ok'] = False
        res['error'] = str(e)
    print("%-5s ok=%s vol=%.5f (%+.3f%%) area=%+.2f%% dCoM=%.4f dBox=%.4f faces=%s" % (
        pid, res['ok'], res.get('vol', 0), res.get('dvol_pct', 0), res.get('darea_pct', 0),
        res.get('dcom', -1), res.get('dbox', -1), res.get('faces')))
    if res['ok']:
        print("      box", ["%.4f" % v for v in res['box']], "com", ["%.4f" % v for v in res['com']])
    if not keep_open:
        p.close()
    return res


if __name__ == '__main__':
    ids = sys.argv[1:] or ORDER
    keep = '--keep' in ids
    ids = [i for i in ids if not i.startswith('--')]
    allres = {}
    rp = os.path.join(HERE, 'measure_results.json')
    if os.path.exists(rp):
        allres = json.load(open(rp))
    for pid in ids:
        allres[pid] = build_one(pid, keep_open=keep)
    json.dump(allres, open(rp, 'w'), indent=1, default=str)
