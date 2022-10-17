
KINEMATIC_GEN_VARS = [
]
KINEMATIC_VARS = [
  'x_reco_eta',
  'x_reco_pt',
  'x_reco_loose',
  'x_reco_medium',
  'x_reco_tight',
  'ip3d',
  'cos2d',
  'b_pt',
  'b_l1_pt',
  'b_k_pt',
  'b_cos2D',
  'b_lxy',
  'b_lxyerr',
  'b_svprob'
]

# Use here only variables available in real data.
MVA_SCALAR_VARS = [
  'x_reco_eta',
  'x_reco_pt',
]

# Mutual information regularization targets
MI_VARS = [
]

# Variables we use with name replacement, need to be found in both MC and DATA
NEW_VARS = [
  'x_reco_eta',
  'x_reco_pt',
]

PLOT_VARS = [
  'x_reco_eta',
  'x_reco_pt',

]

# Variables we read out from the root files (regular expressions supported here)
#LOAD_VARS = ['.+hlt.?', '.?gen.?']
LOAD_VARS = ['.*'] # all
