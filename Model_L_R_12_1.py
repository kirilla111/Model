import numpy
import xgboost
import sklearn
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
# load data
dataset = numpy.loadtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]
# split data into train and test sets
seed = 40 #было 7
ts = 0.15 #было 0.33
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size = ts, random_state=seed)
# fit model no training data
model = xgboost.XGBClassifier()
model.fit(X_train, y_train)
print(model)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
