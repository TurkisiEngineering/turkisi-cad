"""Named parameters for the P10 comfort-grip knob (units: inch, frame per spec.md)."""
import math

TAN3 = math.tan(math.radians(3.0))

# --- global / plan -----------------------------------------------------------
N_LOBES = 8
SCALLOP_PCR = 1.39          # scallop centre circle radius
SCALLOP_THETA0 = 22.5       # deg, first scallop centre angle

# --- P01 core ----------------------------------------------------------------
HUB_END_Z = -0.68
HUB_R_END = 0.625           # hub radius at z=-0.68 (dia 1.25), 3 deg draft
HUB_END_ROUND = 0.02
HEAD_UNDER_Z = -0.12
CORE_RIM_R = 1.20           # head rim (dia 2.4)
RIM_TOP_Z = 0.44
TOP_FLAT_R_IN = 1.06        # top flat ring inner radius = dome start
DOME_R = 2.175763
DOME_C = (0.124593, -1.524424)
CORE_TOP_Z = 0.62
DOME_END_R = 0.492553
SCALLOP_R_CORE = 0.33
LCI_R = 1.11                # core rim inner circle
LCI_SCALLOP_R = 0.39
CAV_STEP_Z = 0.26
CAV_CEIL_Z = 0.35
CAV_CONE_R_LO = 1.01
CAV_CONE_R_HI = 0.92
RIB_T = 0.05
BORE_SEAT_R = 0.265625
BORE_STEP_Z = -0.18
BORE_R0 = 0.36              # tapered bore radius at z=-0.18
BORE_TOP_ROUND = 0.015
BORE_ROUND_C = (0.416161, 0.605)
BORE_TAN_PT = (0.401182, 0.605785)
RIDGE_RI = 0.385417
RIDGE_RO = 0.505208
RIDGE_H = 0.015

# --- P02 coating -------------------------------------------------------------
COAT_T = 0.06
LO_R = 1.26
LO_SCALLOP_R = 0.27
LI_R = 1.05
LI_SCALLOP_R = 0.45
PLAN_CORNER_R = 0.10
COAT_BOT_Z = -0.18
COAT_FLAT_TOP_Z = 0.50
COAT_EDGE_R = 0.06
COAT_DOME_R = 2.230085
COAT_TOP_Z = 0.68
COAT_DOME_END_R = 0.461925
TOP_OPEN_R = 0.421954
TOP_OPEN_CONE_Z = 0.674670

# --- P03 insert --------------------------------------------------------------
INS_R = 0.265625
INS_Z0 = -0.68
INS_Z1 = -0.18
PITCH = 1.0 / 16.0
TH_MAJOR_R = 0.1875
TH_MINOR_R = 0.146906
TH_FLAT = PITCH / 8.0
TH_PHASE_Z = -0.379218      # root flat centre in half-plane theta=0
CSK_R = 0.21875
CSK_DEPTH = 0.03125
