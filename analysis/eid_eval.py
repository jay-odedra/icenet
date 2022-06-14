# Electron ID [EVALUATION] code
#
# Mikael Mieskolainen, 2022
# m.mieskolainen@imperial.ac.uk


# icenet system paths
import sys
sys.path.append(".")

import numpy as np
import pickle

# icenet
from icenet.tools import io
from icenet.tools import aux
from icenet.tools import process
from icenet.tools import reweight


# iceid
from iceid import common
from iceid import graphio
from configs.eid.mvavars import *


def ele_mva_classifier(data, data_tensor=None, data_kin=None, data_graph=None, weights=None, args=None):
    """
    External classifier directly from the root tree
    """

    varname = 'ele_mva_value_depth15'

    print(f'\nEvaluate <{varname}> classifier ...')
    try:
        y    = np.array(data.tst.y, dtype=float)
        yhat = np.array(data.tst.x[:, data.ids.index(varname)], dtype=float)

        return aux.Metric(y_true=y, y_soft=yhat, weights=weights)
    except:
        print(__name__ + 'Variable not found')


# Main function
#
def main() :

    args, cli = process.read_config(config_path='./configs/eid')

    ### Load data full in memory
    data      = io.IceTriplet(func_loader=common.load_root_file, files=args['root_files'],
                    load_args={'entry_start': 0, 'entry_stop': args['maxevents'], 'args': args},
                    class_id=[0,1], frac=args['frac'], rngseed=args['rngseed'])

    ### Imputation
    imputer   = pickle.load(open(args["modeldir"] + '/imputer.pkl', 'rb')) 
    features  = globals()[args['imputation_param']['var']]
    data, _   = process.impute_datasets(data=data, features=features, args=args['imputation_param'], imputer=imputer)

    ### Compute reweighting weights for the evaluation (before split&factor !)
    if args['eval_reweight']:
        tst_weights,_ = reweight.compute_ND_reweights(x=data.tst.x, y=data.tst.y, ids=data.ids, args=args['reweight_param'])
    else:
        tst_weights = None
    
    ## Parse graph network data
    data_graph = None
    if args['graph_on']:
        data_graph = {}
        data_graph['tst'] = graphio.parse_graph_data(X=data.tst.x, Y=data.tst.y, weights=tst_weights, ids=data.ids,
            features=features, global_on=args['graph_param']['global_on'], coord=args['graph_param']['coord'])
    
    # ----------------------------
    # Evaluate external classifiers
    met_elemva = ele_mva_classifier(data=data, weights=tst_weights)
    
    # Add to the stack
    process.roc_mstats.append(met_elemva)
    process.roc_labels.append('elemva15')
    # ----------------------------
    
    ## Split and factor data
    data, data_tensor, data_kin = common.splitfactor(data=data, args=args)

    ## Evaluate classifiers
    process.evaluate_models(data=data, data_tensor=data_tensor, data_kin=data_kin, weights=tst_weights, data_graph=data_graph, args=args)
    
    print(__name__ + ' [Done]')


if __name__ == '__main__' :
    main()
