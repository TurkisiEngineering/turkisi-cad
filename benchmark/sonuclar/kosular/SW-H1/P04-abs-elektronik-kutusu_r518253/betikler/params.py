"""Named parameters (inch / degree) shared by all build scripts. Values from girdi/spec.md."""
import math

T3 = math.tan(math.radians(3.0))
T1 = math.tan(math.radians(1.0))
T10 = math.tan(math.radians(10.0))

# --- common shell outline S / cavity outline C ---
W_HALF = 0.925           # outline S half width (X)
L_HALF = 1.2             # outline S half length (Y)
R_CORNER = 0.1           # vertical corner radius, constant at every height
DRAFT_OUT = 3.0          # outer wall draft
DRAFT_IN = 1.0           # cavity / rib / boss draft
CAV_HX = 0.845           # cavity outline C half width at the open side
CAV_HY = 1.12            # cavity outline C half length
CAV_CHAMF = 1.87062      # chamfer line |x|+|y| at the open side
R_EDGE = 0.1             # bottom / top perimeter round
EDGE_C_HX = 0.80652      # centre of the perimeter round (X sides)
EDGE_C_HY = 1.08152      # centre of the perimeter round (Y sides)
R_CAV_FILLET = 0.03      # floor / ceiling fillet
LABEL_IN = (0.755, 1.035)
LABEL_OUT = (0.775, 1.055)
LABEL_DEPTH = 0.01

# --- base P01 ---
BASE_Z_BOT = -0.45
BASE_FLOOR = -0.39
LIP_H = 0.03
LIP_IN = (0.865, 1.14)
LIP_OUT = (0.915, 1.19)
LIP_OUT_R = 0.09
TONGUE_H = 0.03
TONGUE_HALF_W = 0.01925
TONGUE_DRAFT = 10.0
TONGUE_X_C = 0.88582
TONGUE_Y_C = 1.16082
TONGUE_X_END = 1.07085   # round-end centre of X-side segments
TONGUE_Y_END = 0.79585   # round-end centre of Y-side segment
TONGUE_GAP = 0.156       # flat ends |y| of X-side segments
TONGUE_R = 0.005
RECESS_DEPTH = 0.035
RECESS_R = 0.02
BOSS_R = 0.0925
BOSS_TOP_BASE = 0.03
RIB_HALF_T = 0.015
RIB_STEP_X = 0.123
RIB_END_X = 0.15221
RIB_LOW_Z = -0.035
HOLE_CB_R = 0.085
HOLE_CB_Z = -0.429
HOLE_CS_Z = -0.38586
HOLE_R = 0.0475

# --- lid P02 ---
LID_Z_BOT = 0.03
LID_Z_TOP = 0.48
LID_CEIL = 0.42
GROOVE_IN = (0.865, 1.14, 0.05)
GROOVE_OUT = (0.9035, 1.1785, 0.0885)
GROOVE_DEPTH = 0.035
GROOVE_DRAFT = 10.0
KEY_HALF = 0.146
KEY_DRAFT = 3.0
LID_BOSS_Z = 0.035
LID_RIB_END = 0.153
LID_HOLE_R = 0.035

# --- screw H1 ---
SCR_HEAD_R = 0.081
SCR_Z_HEAD = -0.45
SCR_Z_CONE = -0.40
SCR_R = 0.036
SCR_Z_END = 0.05
SCR_RECESS_D = 0.03
SCR_RECESS_DRAFT = 4.0
SCR_ARM_REACH = 0.053
SCR_ARM_HALF = 0.0085
SCR_FILL = 0.0235
