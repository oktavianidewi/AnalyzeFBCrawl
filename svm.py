import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import precision_recall_fscore_support, \
    classification_report, confusion_matrix
import json, os, csv

clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

# load dataset
iris = datasets.load_iris()
X, y, z = iris.data, iris.target, iris.target_names[iris.target]


Xdataset = []
yConstitutionalpatriot = []
yFoodgroup = []
yHikingWithDogs = []
yJJ = []
yLikeForLikePromoteYourBusiness = []
yTEDtranslate = []
yTraveladdition = []

z = []
filename = 'like_english_all.csv'
with open(filename, 'rb') as csvfile:
    data = csv.reader(csvfile)
    i = 0
    for row in data:
        if i > 0:
            # print row
            Xdataset.append(row[12:len(row)])
            yConstitutionalpatriot.append(row[5])
            yFoodgroup.append(row[6])
            yHikingWithDogs.append(row[7])
            yJJ.append(row[8])
            yLikeForLikePromoteYourBusiness.append(row[9])
            yTEDtranslate.append(row[10])
            yTraveladdition.append(row[11])
        i += 1

# print X
"""
rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)
"""

X = Xdataset
y = yHikingWithDogs
# kernel linear better than rbf when there number of features is larger than number of observation
clf.set_params(kernel='linear').fit(X, y)
prediction_result = list(clf.predict(X))
# print clf.predict(X_test)
# goldstandard = y[:1]
# prediction = list(clf.predict(X[:1]))

print prediction_result
print y

print confusion_matrix(y, prediction_result)
print classification_report(y, prediction_result)

# score = list(precision_recall_fscore_support(goldstandard, prediction_result, average='macro'))
# print score

# print iris.data[:9]
# print iris