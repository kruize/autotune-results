'''import pandas as pd
from sklearn.model_selection import StratifiedKFold
#from featurizer.py import *
df=pd.DataFrame
#df=for_other_file(df)
df= pd.read_csv('/Users/prakalp/Downloads/yy.csv')
x = df.iloc[:, 2:-1].values
y = df. iloc [:, 0].values
print("Matrix of features", x, sep='\n')
print("--------------------------------------------------")
print("Target Variable", y, sep='\n')
from sklearn.model_selection import cross_validate
def cross_validation(model, _x, _y, _cv=5):
    _scoring = ['accuracy', 'precision', 'recall', 'f1']
    results = cross_validate(estimator=model,
                             x=_x,
                             y=_y,
                             cv=_cv,
                             scoring=_scoring,
                             return_train_score=True)
    return {"Training Accuracy scores": results['train_accuracy'],
            "Mean Training Accuracy": results['train_accuracy'].mean() * 100,
            "Training Precision scores": results['train_precision'],
            "Mean Training Precision": results['train_precision'].mean(),
            "Training Recall scores": results['train_recall'],
            "Mean Training Recall": results['train_recall'].mean(),
            "Training F1 scores": results['train_f1'],
            "Mean Training F1 Score": results['train_f1'].mean(),
            "Validation Accuracy scores": results['test_accuracy'],
            "Mean Validation Accuracy": results['test_accuracy'].mean() * 100,
            "Validation Precision scores": results['test_precision'],
            "Mean Validation Precision": results['test_precision'].mean(),
            "Validation Recall scores": results['test_recall'],
            "Mean Validation Recall": results['test_recall'].mean(),
            "Validation F1 scores": results['test_f1'],
            "Mean Validation F1 Score": results['test_f1'].mean()}'''