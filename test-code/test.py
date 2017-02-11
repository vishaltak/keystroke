import pandas as pd
import numpy
from scipy.sparse import csr_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import FeatureHasher
from sklearn.svm import OneClassSVM
from collections import Counter

keystroke_data = pd.read_csv(r'data/genuine_user.csv', header= 0)
results = []
for user in keystroke_data.id.unique():
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	no_of_samples = user_keystroke_data.id.count()
	#prepare X->perform queries on it
	hash_length= len(user_keystroke_data.password.iloc[0])
	#TODO: refine the value of hash_length
	hash_length= hash_length + hash_length//2
	print("Hash Length: {}".format(hash_length))

	X = user_keystroke_data[['release_codes', 'pp', 'pr', 'rp', 'rr', 'total']]
	y = user_keystroke_data['genuine']

	print("==== X before transformation =====")
	print("====X type: {}".format(type(X)))
	print("====y type: {}".format(type(y)))
	print(X.shape)

	# TODO: sort this shit out
	hasher= FeatureHasher(n_features=10, input_type='string', non_negative=True)

	X_transformed= []
	for i in range(no_of_samples):
		#print("==========i value: {}".format(i))
		#print(X.iloc[i])
		temp_X = X.iloc[i]
		temp_X = temp_X[['pp', 'pr', 'rp', 'rr']]
		#print(temp_X)
		#temp_dict = {}
		#temp_dict['release_codes'] = temp_X.release_codes
		#temp_dict['pp'] = temp_X.pp
		#temp_dict['pr'] = temp_X.pr
		#temp_dict['rp'] = temp_X.rp
		#temp_dict['rr'] = temp_X.rr
		#temp_dict['total'] = temp_X.total
		#print("====temp dict : {}".format(temp_dict))
		X_transformed.append(hasher.fit_transform(temp_X))

	with open(r'output.csv', 'w') as file:
		file.write(pd.DataFrame(X_transformed).to_csv())


# 	X_train, X_test, y_train, y_test = train_test_split(pd.DataFrame(X_transformed), y, test_size=0.4, random_state=0)
# 	print("====X_train type: {}".format(type(X_train)))
# 	# SVM
# 	svm_clf = OneClassSVM(kernel='poly')
# 	svm_clf.fit(X_train,y_train)
# 	prediction_results= svm_clf.predict(X_test)
# 	counter= Counter(prediction_results)
# 	correct_preditions = counter.get(1.0, 0)
# 	wrong_preditions = counter.get(-1.0, 0)
# 	results.append({'user':user, 'classifier':'ocsvm', 
# 		'data':{'correct_preditions':correct_preditions, 'wrong_preditions':wrong_preditions}
# 	})

# #results are only for positive samples. negactive samples have not yet been tested
# for result in results:
# 	user= result.get('user')
# 	classifier= result.get('classifier')
# 	correct_preditions= result.get('data').get('correct_preditions')
# 	wrong_preditions= result.get('data').get('wrong_preditions')
# 	accuracy= correct_preditions/(correct_preditions + wrong_preditions)*100
# 	print("User: {} => Classifier: {} => Correct: {}, Wrong: {}, Accuracy: {}%"
# 		.format(user, classifier, correct_preditions, wrong_preditions, accuracy)
# 	)