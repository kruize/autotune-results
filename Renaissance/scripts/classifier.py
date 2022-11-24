import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
from sklearn.metrics import accuracy_score, roc_auc_score,\
    precision_recall_curve, roc_curve, classification_report
from sklearn.model_selection import cross_validate, \
    StratifiedKFold, train_test_split

from sklearn.preprocessing import label_binarize
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
#read data
df = pd.read_csv('yy1.csv')
#can drop specific columns from dataframe
df_features = df.drop(['exp_name', 'iteration'], axis=1)
#can select specific columns
df_target = df['exp_name']
#choosing columns by indices can be dangerous
#because they can change
#x = df.iloc[:, 2:-1].values
#y = df. iloc [:, 0].values
print("Matrix of features", df_features, sep='\n')
print("--------------------------------------------------")
print("Target Variable", df_target, sep='\n')
print(f'Unique metrics: {np.unique([f.split("_")[0] for f in df_features.columns])}')
#simplest model validation scheme
#rename features and target for simplicity
X = df_features
y = df_target
#every model in sklearn has the fit, predict interface
#so we can initialize the model and pass it to the fitting function simple_validation
model = RandomForestClassifier(n_estimators=100, max_depth=5)
random_state = 0
#def simple_validation(model, random_state=0):
    #fix random state for reproducibility
    #split into train and test sets
    #warning: we have very low statistics i.e. very few points per label/workload
    #this will give nonsensical results but we are just testing out the process for now
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=random_state)
print(f'Train sizes: {X_train.shape} {y_train.shape}')
print(f'Test  sizes: {X_test.shape} {y_test.shape}')
print(f'\nUnique classes in train set: {np.unique(y_train)}')
print(f'Unique classes in test  set: {np.unique(y_test)}')
model = model.fit(X_train, y_train) #fit on training set - need features and labels
#predict which label/class/workload each row belongs to
train_pred = model.predict(X_train) #make predictions on train set - need only features
test_pred = model.predict(X_test) #make predictions on test set
#predict the probability of each class for each row - this returns a matrix of size
#num_rows x num_workloads where each row in the matrix adds up to 1 i.e. these are probabilities
#(and the entries are between 0 and 1)
train_pred_probs = model.predict_proba(X_train)
test_pred_probs = model.predict_proba(X_test)
#can compute metrics to evalute the model
#accuracy is the simplest one but can be misleading
#e.g. suppose most of our data (90%) is from page-rank
#we can just "predict" that each row is page-rank i.e. there is no model
#then we'll get all page-rank rows correct and all other rows (10%) incorrect
#accuracy = 90% even though our model is not making useful predictions
#this is not the case for us since the classes are evenly distributed but good to keep in mind
train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, test_pred)
print(f'\nTrain accuracy = {train_acc}')
print(f'Test  accuracy = {test_acc}')
#exercise: are the train and test accuracies similar? are we overfitting or underfitting?
#print reports including precision and recall
#exercise: definition of precision, definition of recall
#exercise: how are precision and recall computed and how they depend on a threshold
#exercise: what does the precision-recall curve tell you
print(classification_report(y_train, train_pred))
print(classification_report(y_test, test_pred))
print(df.corr())
hyperparameter_space = {'max_depth':[1,2,3,4,5,6,7,8,9,10],
                        'n_estimators':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
],
                        }
gs = GridSearchCV(model, param_grid=hyperparameter_space,
                  scoring="accuracy",
                  n_jobs=-1, return_train_score=True)
gs.fit(X_train, y_train)
print("Optimal hyperparameter combination:", gs.best_params_)
print()
print("Mean cross-validated testing accuracy score:",
      gs.best_score_)
gs.best_estimator_.fit(X_train, y_train)
y_pred = gs.best_estimator_.predict(X_test) # Predictions
y_true = y_test # True values

