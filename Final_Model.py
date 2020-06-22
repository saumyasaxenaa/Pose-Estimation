import pandas as pd
from sklearn.model_selection import train_test_split


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score


data = pd.read_csv('/Users/saumyasaxena/Desktop/untitled folder/New/Master.csv')
data_new = data.fillna(data.mean())
y = data_new.Label
x = data_new.drop('Label', axis = 1)
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=0)

clf = SVC(kernel = 'linear', C = 1)
clf.fit(x_train, y_train)
scores = cross_val_score(clf, x, y, cv=5)
print('Cross Validation Scores: ', scores)
svm_predictions = clf.predict(x_test)
print("Cross Validation Accuracy: %0.2f" % (scores.mean()))
accuracy1 = clf.score(x_test, y_test)
cm1 = confusion_matrix(y_test, svm_predictions)
print('SVM Accuracy:',accuracy1)
print('Confusion Matrix:\n',cm1)