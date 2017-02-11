import pandas as pd
import numpy as np
import pprint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import OneClassSVM

from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import IsolationForest

from sklearn.model_selection import train_test_split
from collections import Counter

def split_data(X):
	data = []
	for i in range(0, X.shape[0]):
		tempX = X.iloc[i]
		pp = [int(value) for value in tempX.pp.split()]
		pr = [int(value) for value in tempX.pr.split()]
		rp = [int(value) for value in tempX.rp.split()]
		rr = [int(value) for value in tempX.rr.split()]
		misc = [int(tempX.ppavg), int(tempX.rpavg), int(tempX.rravg), int(tempX.pravg), int(tempX.total)]
		temp_data = tuple(pp) + tuple(rp) + tuple(rr) + tuple(pr)  + tuple(misc)
		data.append(temp_data)
	data = pd.DataFrame.from_records(data)
	return data

keystroke_data = pd.read_csv(r'../data/genuine_user_cleaned.csv', header= 0)
results = []
for user in keystroke_data.id.unique():
	#print("User {}".format(user))
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	X = user_keystroke_data[['release_codes', 'pp','pr', 'rp', 'rr', 'ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
	X = split_data(X)
	y = user_keystroke_data['genuine']

	start_index = 0
	step = 20
	end_index = start_index + step
	X_train = pd.DataFrame()
	y_train = pd.DataFrame()
	X_test = pd.DataFrame()
	y_test = pd.DataFrame()

	while end_index < X.shape[0]:
		try:
			temp_data_X = X[start_index:end_index]
			temp_data_y = y[start_index:end_index]
			if X_train.shape[0] >= 100:
				X_train = X_train[step:]
				y_train = y_train[step:]
			X_train = X_train.append(temp_data_X)
			y_train = X_train.append(temp_data_y)
			X_test = X[end_index:]
			y_test = y[end_index:]
			# print("Start:{}, End:{}".format(start_index, end_index))
			# print("X_train ={}, X_test ={}".format(X_train.shape[0], X_test.shape[0]))
			
			# # SVM
			# svm_clf = OneClassSVM(kernel='linear')
			# svm_clf.fit(X_train,y_train)
			# prediction_results= svm_clf.predict(X_test)
			# counter= Counter(prediction_results)
			# correct_preditions = counter.get(1.0, 0)
			# wrong_preditions = counter.get(-1.0, 0)

			# results.append({'user':user, 'classifier':'ocsvm', 
			# 	'data':{'correct_preditions':correct_preditions, 'wrong_preditions':wrong_preditions}
			# })
			
			# Classifier
			rng = np.random.RandomState(42)
			clf = IsolationForest(random_state=rng)
			clf.fit(X_train, y_train)
			prediction_results= clf.predict(X_test)
			counter= Counter(prediction_results)
			correct_preditions = counter.get(1.0, 0)
			wrong_preditions = counter.get(-1.0, 0)
			accuracy= correct_preditions/(correct_preditions + wrong_preditions)*100
			print("User {}, Accuracy {:.2f}"
				.format(
					str(user).rjust(3), 
					accuracy
				)
			)

			start_index = end_index
			end_index = start_index + step
		except IndexError:
			break


# # results are only for positive samples. negactive samples have not yet been tested
# for result in results:
# 	user= result.get('user')
# 	classifier= result.get('classifier')
# 	correct_preditions= result.get('data').get('correct_preditions')
# 	wrong_preditions= result.get('data').get('wrong_preditions')
# 	accuracy= correct_preditions/(correct_preditions + wrong_preditions)*100
# 	print("User: {} => Classifier: {}, Accuracy: {:.2f}%"
# 		.format(
# 			str(user).rjust(3), 
# 			str(classifier).rjust(6), 
# 			accuracy
# 		)
# 	)