"""Temiz kopyada tam yeniden kurulum: python build_all.py  (SolidWorks 2024 + pywin32)."""
from swcom import *
import build_core, build_coating, build_insert, build_assembly

sw = app()
c, _ = build_core.build(sw)
k, _ = build_coating.build(sw)
i, _ = build_insert.build(sw, clockwise=False, start_deg=0.0)   # cw=False -> sag el (RH) dis
build_assembly.build(sw)
