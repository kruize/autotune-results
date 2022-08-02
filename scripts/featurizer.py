import os
import glob
import pandas as pd
import numpy as np
import json

'''
NOTE: this is not a working script. it's meant to demo what a script
would look like. you should fill in the details and test everything works.

overall_loop: takes in location 'results/renaissance-202207201850/scale_1'
              and loops over all iterations

featurize_results: loops over metric files in each ITR-X directory and computes
                   features

featurize_metrics: where new metrics/computations can be added

Questions:
Is scale_1 an experiment/workload? Do we need the outer loop to start one level higher?

What are cpu-warmup-0/1/2..., memusage-warmup-0/1/2/3/4 etc.?

Can we collect all data in json format (not just json file extensions)?
'''

def overall_loop(loc):
    '''
    loc: location where all iterations are located
    e.g. loc = results/renaissance-202207201850/scale_1
    '''

    data = []
    exp_names = []
    for f in os.listdir(loc):
        if not os.path.isdir(f):
            continue

        for itr_path in os.listdir(os.path.join(loc, f)):
            #each results will contain data for one row
            results = featurize_results(itr_path)
            
            data.append(results)
            
            exp_names.append('_'.join(itr_path.split(os.path.sep)[-2:])
)

    data = pd.DataFrame(data)
    data['exp_name'] = exp_names
    
    return data


def featurize_results(loc):
    '''
    loc: location of json files for a certain iteration
    e.g. loc = results/renaissance-202207201850/scale_1/ITR-0
    '''

    results = {}
    for f in glob.glob(os.path.join(loc, "*.json")):
        print(f)

        data = json.load(open(f))

        results = featurize_metrics(data, f.split('/')[-1].rstrip('.json'), results=results)

    return results

def featurize_metrics(data, metric_name, results):
    '''
    All particular calculations for the metrics should go here
    '''

    results[f'{metric_name}_max'] = np.max(data[metric_name])
    results[f'{metric_name}_min'] = np.min(data[metric_name])

    for p in [10, 25, 50, 75, 90]:
        results[f'{metric_name}_p'] = np.percentiles(data[metric_name], p)

    #any more metrics should go here

    return results