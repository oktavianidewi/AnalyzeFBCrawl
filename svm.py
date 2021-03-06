from sklearn import svm, cross_validation
from sklearn.metrics import precision_recall_fscore_support, classification_report, confusion_matrix
from sklearn.decomposition import PCA
from sklearn.learning_curve import learning_curve
import numpy as np
import csv

clf = svm.SVC()

# load dataset
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
            Xdataset.append( row[12:len(row)] )
            yConstitutionalpatriot.append(row[5])
            yFoodgroup.append(row[6])
            yHikingWithDogs.append(row[7])
            yJJ.append(row[8])
            yLikeForLikePromoteYourBusiness.append(row[9])
            yTEDtranslate.append(row[10])
            yTraveladdition.append(row[11])
        i += 1

# print X
X = np.array(Xdataset, dtype=np.int_)
y = np.array(yTraveladdition)

# kernel linear better than rbf when there number of features is larger than number of observation

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)
pca = PCA(n_components=2) # adjust by ourself

pca.fit(X_train)
X_t_train = pca.transform(X_train)
X_t_test = pca.transform(X_test)

print(X.dtype)


print len(X)
print len(y)
print len(X_train)
print len(y_train)

clf.set_params(kernel='linear').fit(X_train, y_train)
prediction_result = list(clf.predict(X_test))

"""
clf.set_params(kernel='linear').fit(X_t_train, y_train)
prediction_result = list(clf.predict(X_t_test))
"""

# print clf.predict(X_test)
# goldstandard = y[:1]
# prediction = list(clf.predict(X[:1]))

# print X
# print y

# print 'score', clf.score(X_test, y_test)

print confusion_matrix(y_test, prediction_result)
print classification_report(y_test, prediction_result)

