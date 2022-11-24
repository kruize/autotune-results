import os
import glob
import pandas as pd
import numpy as np


def overall_loop(loc):

    data = []
    exp_names = []
    iter=[]
    for f in os.listdir(loc):

        if not os.path.isdir(loc + "/" + f):
            continue

        for itr_path in os.listdir(os.path.join(loc, f)):
            if itr_path.split('.')[-1] == 'log':
                continue
            iter_path_url = loc + "/" + f + '/' + itr_path
            results_list = featurize_results(iter_path_url)
            data1=pd.DataFrame(results_list)
            data1['Iteration'] ='_'.join(itr_path.split(os.path.sep)[-2:])
            data1['exp_name']=os.path.basename(loc)
            data.append(data1)

            #iter.append('_'.join(itr_path.split(os.path.sep)[-2:]))
            #exp_names.append(os.path.basename(loc))


    #data = pd.DataFrame(data)
    #data['Iteration']=iter
    #data['exp_name']=exp_names
    data=pd.concat(data,axis=0)
    data.to_csv('try.csv', index=None)

    return data


def featurize_results(loc):
    '''
    loc: location of json files for a certain iteration
    e.g. loc = results/renaissance-202207201850/scale_1/ITR-0
    '''

    results_list = []
    for f in glob.glob(os.path.join(loc, "*.json")):
        print(f)
        if "warmup" in f:
            continue

        # data = json.load(open(f))
        data = convfiletojson(f)
        results = featurize_metrics(data, f.split('/')[-1].split('-')[0])
        results_list.append(results)
    return results_list


def featurize_metrics(data, metric_name):
    '''
    All particular calculations for the metrics should go here
    '''
    results={}
    results['metric-name'] = metric_name

    # import ipdb
   # ipdb.set_trace()
    results[f'max'] = np.max(data['value'])
    results[f'min'] = np.min(data['value'])

    for p in [10, 25, 50, 75, 90]:
        results[f'{p}th-percentile'] = np.percentile(data['value'], p)

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
        data['Iteration'] = os.path.basename(head2)
        return data

    # out_file=open("tests.json","w")
    # json.dump(dict1, out_file, indent = 4, sort_keys = False)


"""def createcsv(loc):
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
    df.columns = ['exp_name', ' Iteration', 'Metric-name', 'timestamp', 'value']
    df.to_csv('try1.csv', index=None)"""


loc = "/home/kchalasa/IdeaProjects/benchmarks/renaissance/results/page-rank"

results_list=overall_loop(loc)
