import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.utils import shuffle
import sys
import os
import time

stime=time.time()
if len(sys.argv)<2 or len(sys.argv)>2:
    print("Arguments are wrong.\n" \
          "Correct usage: cod.py data.txt")
    exit(0)
else:
    data_file = sys.argv[1]

# #############################################################################
data = open(data_file, 'r').readlines()
feature_names = []
for f in range(len(data[0].split())-1):
	feature_names.append(data[0].split()[f])
num_of_feature = len(data[0].split())-1
data=data[1:]
x =[]
num_of_data=len(data)-1
for i in range(num_of_data):
    x.append([])
    for j in range(1,len(data[0].split())):
        x[i].append(data[i].split()[j])
# feature
X = np.zeros((num_of_data,num_of_feature))
for i in range(num_of_data):
    for j in range(0,num_of_feature):
        X[i][j] = x[i][j]
#print(X)

#Target
y = np.zeros((num_of_data))
for i in range(num_of_data):
	for j in range(num_of_feature-1,num_of_feature):
		y[i] = x[i][j+1]
X,y=shuffle(X,y)
#print(y)

# ###############################################
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.8)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

# ###############################################
#gridsearch
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

GBR=GradientBoostingRegressor()
#work4 parameter combinations
search_grid={'n_estimators':[100,200,300,400,500],'learning_rate':[0.01,0.1,1],'max_depth':[2,3,4,5,6,7,8],'subsample':[0.08,0.8,1],'min_samples_split':[2,3,4,5],
'min_samples_leaf':[2,3,4,5],'loss':['ls','lad','huber']}
search=GridSearchCV(estimator=GBR,param_grid=search_grid,n_jobs=20,cv=10)
search.fit(X,y)
#print(search.cv_results_)
print("\nbest score=", search.best_score_)
print("\nbest parameters:",search.best_params_)
etime=time.time()
print("time=",etime-stime,"s")
