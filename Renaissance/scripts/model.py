import numpy as np
import pandas as pd
from time import time
from sklearn import metrics
from sklearn import datasets, neighbors, linear_model, tree
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
#from sklearn.decomposition import RandomizedPCA
from sklearn.metrics import classification_report, confusion_matrix

#1-KNN
from sklearn.neighbors import KNeighborsClassifier
#2-RandomForest
from sklearn.ensemble import RandomForestClassifier
#3-SVM
from sklearn import datasets, svm
#4-DecisionTree
from sklearn import tree
#5-LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#6-GaussianNB
from sklearn.naive_bayes import GaussianNB
#7-MLP
from sklearn.neural_network import MLPClassifier

#comments from Sanjay: SRA

#Step 1: read data and split into features (X) and target variable (y)
df = pd.read_csv("/home/kchalasa/PycharmProjects/autotune-results/scripts/data.csv")
target_col_name = '...' #the column that contains the application name

X = df.drop(target_col_name, axis=1)
y = df[target_col_name]

#Step 2: split into train and test sets
#WARNING: this will be nonsensical if you have two few iterations per experiment
#Example: if there is only one iteration per application, there'll be applications
#in the test set that never show up in the train set i.e. the model will never even
#"know" these labels exist
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#Step 3: function to train and evaluate a model
#WARNING: Random forests are a good starting point. Other methods depend on preprocessing the data
#Example: KNearestNeighbors uses a distance metrics between every pair of points
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
#By default, the metric is the Euclidean metric (distance^2 = (x1_y1)^2 + (x2_y2)^2 + ...)
#Here the coordinates of each point (x1, x2, ...) are the columns in your dataframe
#If two metrics are measured on very different scales (CPU between 0-1 and memory between 0 and 64GB),
#then the distance metric will add quantities with different units which is not meaningful
#This requires normalizing the data. E.g. each column is divided by its standard deviation
def train_eval_model(X_train, y_train, X_test, y_test, model, score_func):
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    train_score = score_func(y_train, train_pred)

    test_pred = model.predict(X_test)
    test_score = score_func(y_test, test_pred)

    return model, train_score, test_score

score_func = metrics.accuracy_score #For classification, AUC is a more meaningful score
#If you want to know why, please ping me

#Note the results for KNN might not be meaningful given the comments about distance above
#Similarly, for SVCs data should be normalized. Just stick to random forests for now
model_list = [
                #model = neighbors.KNeighborsClassifier(n_neighbors = 5),
                model = RandomForestClassifier(n_estimators=100, n_jobs=4),
                #model = svm.SVC(kernel='rbf'),
                #model = svm.SVC(kernel='poly')
                ]
#Step 4: Train each model and print out scores
for model in model_list:
    print(model)
    model, train_score, test_score = train_eval_model(X_train, y_train,
                                                      X_test, y_test,
                                                      model, score_func)
    print(f'train_score = {train_score} test_score = {test_score}\n\n')
