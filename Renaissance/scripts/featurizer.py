import os
import glob
import pandas as pd
import numpy as np
import json
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
            # each results will contain data for one row
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

    # any more metrics should go here

    return results
def convfiletojson(loc):
        dict1={}
        fields=["Exp_names" " Iteration" "Metric-name" "timestamp", "value"]
        with open(loc) as fh:
            for line in fh:
                print(line)
                timestamp,value=line.strip().split(";",1)
                dict1['timestamp']=timestamp.strip()
                dict1['value']=value.strip()
                dict1['Metric_name']=os.path.basename(loc)
                head, tail = os.path.split(loc)
                dict1['Iteration']=os.path.basename(head)
                head1,tail1=os.path.split(head)
                head2,tail2=os.path.split(head1)
                dict1['Exp_names']=os.path.basename(head2)

        out_file=open("tests.json","w")
        json.dump(dict1, out_file, indent = 4, sort_keys = False)
def createcsv(loc):
    df = pd.read_csv(loc , skip_blank_lines=False)
    str = ""
    file1 = open(loc)
    Lines = file1.readlines()
    for line in Lines:
        line.strip()
        line.replace("\"", "")
        print(line)
        str = str + line
    str.transpose()
    df.columns = ['Exp_names' ,' Iteration' ,'Metric-name' ,'timestamp', 'value']
    df.to_csv('results.csv', index=None)
