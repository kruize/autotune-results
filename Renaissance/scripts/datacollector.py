import os
import glob
import pandas as pd
import numpy as np


def overall_loop(loc):
    '''
    loc: location where all iterations are located
    e.g. loc = results/renaissance-202207201850/scale_1
    '''

    data = []
    exp_names = []
    for f in os.listdir(loc):
        if not os.path.isdir(loc + "/" + f):
            continue

        for itr_path in os.listdir(os.path.join(loc, f)):
            # each results will contain data for one row
            iter_path_url = loc + "/" + f + '/' + itr_path

            results = featurize_results(iter_path_url)

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
        if "warmup" in f:
            continue

        # data = json.load(open(f))
        data = convfiletojson(f)
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

def convfiletojson(loc) -> dict:
        df = pd.read_csv(loc, sep=';', names=['timestamp', 'value'])
        df['value'] = df['value'].apply(lambda x: float(x.rstrip('",')))
        data = {}
        data['timestamp'] = df['timestamp'].tolist()
        data['value'] = df['value'].tolist()
        data[loc.split('/')[-1].split('-')[0]] = os.path.basename(loc)
        head, tail = os.path.split(loc)
        data['Iteration'] = os.path.basename(head)
        head1, tail1 = os.path.split(head)
        head2, tail2 = os.path.split(head1)
        data['Exp_names'] = os.path.basename(head2)
        return data

    # out_file=open("tests.json","w")
    # json.dump(dict1, out_file, indent = 4, sort_keys = False)


def createcsv(loc):
    df = pd.read_csv(loc, skip_blank_lines=False)
    str = ""
    file1 = open(loc)
    Lines = file1.readlines()
    for line in Lines:
        line.strip()
        line.replace("\"", "")
        print(line)
        str = str + line
    str.transpose()
    df.columns = ['Exp_names', ' Iteration', 'Metric-name', 'timestamp', 'value']
    df.to_csv('ppj.csv', index=None)
loc = "/Users/prakalp/Documents/GitHub/autotune-results/Renaissance/exp_results"

overall_loop(loc)