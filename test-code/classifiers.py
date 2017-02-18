import sys
# sys.path.append(r'/home/riddhi/keystroke/processing_utils')
sys.path.append(r'/mnt/4650AF4250AF3817/Work/BE Project/keystroke/processing_utils')

import pandas as pd
import numpy as np
import pprint

from collections import Counter
from data import split_data

from sklearn.svm import OneClassSVM
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

keystroke_data = pd.read_csv(r'../data/genuine_user_cleaned.csv', header= 0)
overall_correct_total = 0
overall_wrong_total = 0
rng = np.random.RandomState(42)

names = [
	# "OC-SVM", 
	"Isolation Forest Ensemble",
	# "Decision Tree", 
	# "Gradient Boosting Classifier", 
	# "AdaBoost Classifier", 
]

classifiers = [
	# OneClassSVM(kernel='linear'), 
	IsolationForest(random_state=rng), 
	# DecisionTreeClassifier(), 
	# GradientBoostingClassifier(), 
	# AdaBoostClassifier()

]

for user in keystroke_data.id.unique():
	#print("User {}".format(user))
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	X = user_keystroke_data[['release_codes', 'pp','pr', 'rp', 'rr', 'ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
	y = user_keystroke_data['genuine']
	X = split_data(X)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

	print("\n{0:*^80}".format("User " + str(user)))

	for name, clf in zip(names, classifiers):
		print("\nClassifier : {}".format(name))

		correct_total = 0
		wrong_total = 0
		start_index = 0
		step = 20
		end_index = start_index + step
		X_train = pd.DataFrame()
		y_train = pd.DataFrame()
		X_test = pd.DataFrame()
		y_test = pd.DataFrame()

		iteration_number = 0
		while end_index < X.shape[0]:
			try:
				iteration_number += 1
				temp_data_X = X[start_index:end_index]
				temp_data_y = y[start_index:end_index]
				if X_train.shape[0] >= 100:
					X_train = X_train[step:]
					y_train = y_train[step:]
				X_train = X_train.append(temp_data_X)
				y_train = X_train.append(temp_data_y)
				X_test = X[end_index:]
				y_test = y[end_index:]

				clf.fit(X_train, y_train)
				prediction_results= clf.predict(X_test)
				counter= Counter(prediction_results)
				correct_preditions = counter.get(1.0, 0)
				wrong_preditions = counter.get(-1.0, 0)
				accuracy = correct_preditions/(correct_preditions + wrong_preditions)*100
				correct_total += correct_preditions
				wrong_total += wrong_preditions
				print("Iteration {} => Accuracy {:.2f}"
					.format(
						str(iteration_number).rjust(2), 
						accuracy
					)
				)

				start_index = end_index
				end_index = start_index + step
			except IndexError:
				break

		print("Average Accuracy {:.2f}"
			.format(
				correct_total/(correct_total + wrong_total) * 100
			)
		)

		overall_correct_total += correct_total
		overall_wrong_total += wrong_total
	print("\n{0:*^80}".format(""))


print("Overall accuracy of system {:.2f}"
	.format(
		overall_correct_total/(overall_correct_total + overall_wrong_total) * 100
	)
)