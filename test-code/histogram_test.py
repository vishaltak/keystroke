import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import FeatureHasher
from sklearn.svm import OneClassSVM
from collections import Counter


def hist_from_string(intervals, bins=np.linspace(0, 1000, 11)):
	lst = [int(value) for value in intervals.split()]
	print(bins)
	h, _ = np.histogram(lst, bins=bins, density=True)
	#print(" _ = {}".format( _))
	return h

def hists_from_data(arr):
	feats = []
	for row in arr:
		for intervals in row:
			feats.append(hist_from_string(intervals))
	return np.asarray(feats).reshape(arr.shape[0], -1)

keystroke_data = pd.read_csv(r'/home/riddhi/Desktop/test/genuine2.csv', header=0)
keystroke_data = keystroke_data.values
user_list = keystroke_data[:, 0]
user_list = np.unique(user_list)
results = []

for user in user_list:
	print("User {}".format(user))
	X = hists_from_data(keystroke_data[:, 5:9])
	#print(X)
	y = np.asarray(keystroke_data[:, 2], dtype='int')
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
	# SVM
	svm_clf = OneClassSVM(kernel='poly')
	svm_clf.fit(X_train, y_train)
	prediction_results= svm_clf.predict(X_test)
	counter= Counter(prediction_results)
	correct_preditions = counter.get(1.0, 0)
	wrong_preditions = counter.get(-1.0, 0)
	results.append({'user':user, 'classifier':'ocsvm', 
		'data':{'correct_preditions':correct_preditions, 'wrong_preditions':wrong_preditions}
	})

#results are only for positive samples. negactive samples have not yet been tested
for result in results:
	user= result.get('user')
	classifier= result.get('classifier')
	correct_preditions= result.get('data').get('correct_preditions')
	wrong_preditions= result.get('data').get('wrong_preditions')
	accuracy= correct_preditions/(correct_preditions + wrong_preditions)*100
	print("User: {} => Classifier: {} => Correct: {}, Wrong: {}, Accuracy: {}%"
		.format(user, classifier, correct_preditions, wrong_preditions, accuracy)
	)