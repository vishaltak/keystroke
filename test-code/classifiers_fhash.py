import pandas as pd
import numpy as np
import pprint

from collections import Counter

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction import FeatureHasher
from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM
from sklearn.tree import DecisionTreeClassifier

hasher= FeatureHasher(n_features=10, input_type='dict', non_negative=True, dtype='int64')

def get_hashed_matrix(X, y):
	X_transformed= []
	y_transformed= []
	temp_list = []
	for i in range(X.shape[0]):
		tempX = X.iloc[i]
		rc = list(tempX.release_codes.split())
		pp = list(map(int, tempX.pp.split()))
		pr = list(map(int, tempX.pr.split()))
		rp = list(map(int, tempX.rp.split()))
		rr = list(map(int, tempX.rr.split()))
		temp_dict = {}
		for j in range(0, len(rc)-1):
			index_str = 'pp.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = pp[j]

			index_str = 'rp.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = rp[j]

			index_str = 'rr.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = rr[j]

			index_str = 'pr.'+ rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = pr[j]

		index_str = 'pr.'+ rc[-1]
		while temp_dict.get(index_str, -1) != -1:
			index_str = '_' + index_str
		temp_dict[index_str] = pr[-1]
		temp_dict['ppavg'] = tempX.ppavg
		temp_dict['pravg'] = tempX.pravg
		temp_dict['rpavg'] = tempX.rpavg
		temp_dict['rravg'] = tempX.rravg
		temp_dict['total'] = tempX.total
		temp_list.append(temp_dict)
		y_transformed.append(1)
	X_transformed = pd.DataFrame(hasher.fit_transform(temp_list).todense())
	y_transformed = pd.DataFrame(y_transformed)
	return X_transformed, y_transformed


keystroke_data = pd.read_csv(r'../data/genuine_user.csv', header= 0)
results = []
overall_correct_total = 0
overall_wrong_total = 0
rng = np.random.RandomState(42)

names = [
	# "OC-SVM", 
	"Isolation Forest Ensemble"
	# "Decision Tree"
	# "Gradient Boosting Classifier"
	# "AdaBoost Classifier"
]

classifiers = [
	# OneClassSVM(kernel='linear'), 
	IsolationForest(random_state=rng)
	# DecisionTreeClassifier()
	# GradientBoostingClassifier()
	# AdaBoostClassifier()
]

for user in keystroke_data.id.unique():
	#print("User {}".format(user))
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	X = user_keystroke_data[['release_codes', 'pp','pr', 'rp', 'rr', 'ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
	y = user_keystroke_data['genuine']
	X, y = get_hashed_matrix(X, y)
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

				clf.fit(X_train, X_test)
				prediction_results= clf.predict(X_test)
				counter= Counter(prediction_results)
				correct_preditions = counter.get(1.0, 0)
				wrong_preditions = counter.get(-1.0, 0)
				# results.append({'user':user, 'classifier':name, 
				# 	'data':{'correct_preditions':correct_preditions, 'wrong_preditions':wrong_preditions}
				# })
				accuracy = correct_preditions/(correct_preditions + wrong_preditions)*100
				correct_total += correct_preditions
				wrong_total +=wrong_preditions
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