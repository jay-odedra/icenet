
KINEMATIC_GEN_VARS = [
]
KINEMATIC_VARS = [
  'e1_reco_eta',
  'e1_reco_pt',
  'e2_reco_eta',
  'e2_reco_pt',
]

# Use here only variables available in real data.
MVA_SCALAR_VARS = [
  'e1_reco_eta',
  'e1_reco_pt',
  'e2_reco_eta',
  'e2_reco_pt',
  
  'b_l1_pt_over_b_mass',
  'b_l2_pt_over_b_mass',
  'b_k_pt_over_b_mass',
  'b_pt_over_b_mass',
  'L_xySig',
  'cos2d',
  'e12_reco_dr',
  'e1_reco_loose',
  'e1_reco_medium',
  'e1_reco_tight',
  'e2_reco_loose',
  'e2_reco_medium',
  'e2_reco_tight',
  'b_svprob' 


]

# Mutual information regularization targets
MI_VARS = [
]

# Variables we use with name replacement, need to be found in both MC and DATA
NEW_VARS = [
  'e1_reco_eta',
  'e1_reco_pt',
  'e2_reco_eta',
  'e2_reco_pt',
  
  'b_l1_pt_over_b_mass',
  'b_l2_pt_over_b_mass',
  'b_k_pt_over_b_mass',
  'b_pt_over_b_mass',
  'L_xySig',
  'cos2d',
  'e12_reco_dr',
  'e1_reco_loose',
  'e1_reco_medium',
  'e1_reco_tight',
  'e2_reco_loose',
  'e2_reco_medium',
  'e2_reco_tight',
  'b_svprob'



]

PLOT_VARS = [
  'e1_reco_eta',
  'e1_reco_pt',

]

# Variables we read out from the root files (regular expressions supported here)
#LOAD_VARS = ['.+hlt.?', '.?gen.?']
LOAD_VARS = ['.*'] # all

