import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
columns = ["Exp_names","Iteration", "avg", "min", "max", "median"]
'''import csv

results = []
with open("/Users/prakalp/Downloads/results.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # print(row)
        results.append(row)
print(results[0])

final_dict = {}
for (i, result) in enumerate(results):
    if result['Exp_names']:
        if result['Exp_names'] in final_dict:
            if result['Iteration'] in final_dict[result['Exp_names']]:
                final_dict[result['Exp_names']][result['Iteration']].append({
                    'Metric-name': result['Metric-name'],
                    'avg': result['avg'],
                    "min": result['min'],
                    "max": result['max'],
                    'median': result['median']
                })
            else:
                final_dict[result['Exp_names']][result['Iteration']] = [{
                    'Metric-name': result['Metric-name'],
                    'avg': result['avg'],
                    "min": result['min'],
                    "max": result['max'],
                    'median': result['median']
                }]
        else:
            final_dict[result['Exp_names']] = {
                result['Iteration']: [{
                    'Metric-name': result['Metric-name'],
                    'avg': result['avg'],
                    "min": result['min'],
                    "max": result['max'],
                    'median': result['median']
                }]
            }'''

#df = pd.DataFrame.from_dict(final_dict)
#df.to_csv('calc.csv')'''
df1 = pd.read_csv("/Users/prakalp/Downloads/results.csv",nrows=11,  usecols=columns)
#p = sns.relplot(data=df1, kind='line', height=4)
#p.savefig("output.png")
fp=df1.plot(y=["avg","min","max","median"],subplots=True,color='pink',label=['pg-itr-0','pg-itr-0','pg-itr-0','pg-itr-0'],fontsize=0.5)
df2 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 13) ],nrows=11,  usecols=columns)
df2.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='red',label=['pg-itr-1','pg-itr-1','pg-itr-1','pg-itr-1'],fontsize=0.5)

df3 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 25) ],nrows=11,  usecols=columns)
df3.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='blue',label=['pg-itr-2','pg-itr-2','pg-itr-2','pg-itr-2'],fontsize=0.5)

df4 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 37) ],nrows=11,  usecols=columns)
df4.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='green',label=['nb-itr-0','nb-itr-0','nb-itr-0','nb-itr-0'],fontsize=0.5)

df5 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 49) ],nrows=11,  usecols=columns)
df5.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='orange',label=['nb-itr-1','nb-itr-1','nb-itr-1','nb-itr-1'],fontsize=0.5)
df6 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 61) ],nrows=11,  usecols=columns)
df6.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='yellow',label=['nb-itr-2','nb-itr-2','nb-itr-2','nb-itr-2'],fontsize=0.5)
df7 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 73) ],nrows=11,  usecols=columns)
df7.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='magenta',label=['lr-itr-0','lr-itr-0','lr-itr-0','lr-itr-0'],fontsize=0.5)
df8 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 85) ],nrows=11,  usecols=columns)
df8.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='brown',label=['lr-itr-1','lr-itr-1','lr-itr-1','lr-itr-1'],fontsize=0.5)
df9 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 97) ],nrows=11,  usecols=columns)
df9.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='purple',label=['lr-itr-2','lr-itr-2','lr-itr-2','lr-itr-2'],fontsize=0.5)
df10 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 109) ],nrows=11,  usecols=columns)
df10.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='black',label=['rt-itr-0','rt-itr-0','rt-itr-0','rt-itr-0'],fontsize=0.5)
df11 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 121) ],nrows=11,  usecols=columns)
df11.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='lavender',label=['rt-itr-1','rt-itr-1','rt-itr-1','rt-itr-1'],fontsize=0.5)
df12 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 133) ],nrows=11,  usecols=columns)
df12.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='wheat',label=['rt-itr-2','rt-itr-2','rt-itr-2','rt-itr-2'],fontsize=0.5)
df13 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 145) ],nrows=11,  usecols=columns)
df13.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='darkslategrey',label=['db-itr-0','db-itr-0','db-itr-0','db-itr-0'],fontsize=0.5)
df14 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 157) ],nrows=11,  usecols=columns)
df14.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='crimson',label=['db-itr-1','db-itr-1','db-itr-1','db-itr-1'],fontsize=0.5)
df15 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 169) ],nrows=11,  usecols=columns)
df15.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='linen',label=['db-itr-2','db-itr-2','db-itr-2','db-itr-2'],fontsize=0.5)
df16 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 181) ],nrows=11,  usecols=columns)
df16.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='goldenrod',label=['sd-itr-0','sd-itr-0','sd-itr-0','sd-itr-0'],fontsize=0.5)
df17 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 193) ],nrows=11,  usecols=columns)
df17.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='lightcoral',label=['sd-itr-1','sd-itr-1','sd-itr-1','sd-itr-1'],fontsize=0.5)
df18 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 205) ],nrows=11,  usecols=columns)
df18.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='midnightblue',label=['sd-itr-2','sd-itr-2','sd-itr-2','sd-itr-2'],fontsize=0.5)
df19 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 217) ],nrows=11,  usecols=columns)
df19.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='indigo',label=['de-itr-0','de-itr-0','de-itr-0','de-itr-0'],fontsize=0.5)
df20 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 229) ],nrows=11,  usecols=columns)
df20.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='lightseagreen',label=['de-itr-1','de-itr-1','de-itr-1','de-itr-1'],fontsize=0.5)
df21 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 241) ],nrows=11,  usecols=columns)
df21.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='tan',label=['de-itr-2','de-itr-2','de-itr-2','de-itr-2'],fontsize=0.5)
df22 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 253) ],nrows=11,  usecols=columns)
df22.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='salmon',label=['fh-itr-0','fh-itr-0','fh-itr-0','fh-itr-0'],fontsize=0.5)
df23 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 265) ],nrows=11,  usecols=columns)
df23.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='aliceblue',label=['fh-itr-1','fh-itr-1','fh-itr-1','fh-itr-1'],fontsize=0.5)
df24 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 277) ],nrows=11,  usecols=columns)
df24.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='lightcyan',label=['fh-itr-2','fh-itr-2','fh-itr-2','fh-itr-2'],fontsize=0.5)
df25 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 289) ],nrows=11,  usecols=columns)
df25.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='gold',label=['pn-itr-0','pn-itr-0','pn-itr-0','pn-itr-0'],fontsize=0.5)
df26 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 301) ],nrows=11,  usecols=columns)
df26.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='forestgreen',label=['pn-itr-1','pn-itr-1','pn-itr-1','pn-itr-1'],fontsize=0.5)
df27 = pd.read_csv("/Users/prakalp/Downloads/results.csv",skiprows = [i for i in range(1, 313) ],nrows=11,  usecols=columns)
df27.plot(y=["avg","min","max","median"],ax=fp,subplots=True,color='rosybrown',label=['pn-itr-2','pn-itr-2','pn-itr-2','pn-itr-2'],fontsize=0.5)
frames=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27]
result = pd.concat(frames)
plt.show()



