import pandas as pd
import numpy
from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import FeatureHasher
from collections import OrderedDict
from sklearn.svm import OneClassSVM

keystroke_data = pd.read_csv(r'data/genuine_user.csv', header= 0)
results = []
for user in keystroke_data.id.unique():
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	no_of_samples = user_keystroke_data.id.count()
	hash_length= len(user_keystroke_data.password.iloc[0])
	#TODO: refine the value of hash_length
	hash_length= pow(hash_length, 2)

	X = user_keystroke_data[['release_codes', 'pp', 'pr', 'rp', 'rr', 'total']]
	y = user_keystroke_data['genuine']

	print("==== X before transformation =====")
	print("====X type: {}".format(type(X)))
	print("====y type: {}".format(type(y)))
	print(X.shape)

	# TODO: sort this shit out
	hasher= FeatureHasher(n_features=10, input_type='pair', non_negative=True)

	X_transformed= []
	for i in range(no_of_samples):
		temp_X = X.iloc[i]
		temp_list = []
		#rc contains the list of release code. ignore the last code as it refer to "enter" value
		rc = list(map(int, temp_X.release_codes.split()))
		pp = list(map(int, temp_X.pp.split()))
		pr = list(map(int, temp_X.pr.split()))
		rp = list(map(int, temp_X.rp.split()))
		rr = list(map(int, temp_X.rr.split()))
		for j in range(0, len(rc)-1):
			temp_list.append({'rc':rc[j], 'pp':pp[j], 'pr':pr[j], 'rp':rp[j], 'rr':rr[j]})
		X_transformed.append(hasher.transform(temp_list))

	X_transformed = pd.DataFrame(X_transformed)
	# X_transformed = X_transformed.fillna(method='pad', axis=1)
	with open(r'output.csv', 'w') as file:
		file.write(X_transformed.to_dense().to_csv())

	print("==== X before transformation =====")
	print(X_transformed.shape)

	X_train, X_test, y_train, y_test = train_test_split(pd.DataFrame(X_transformed), y, test_size=0.4, random_state=0)
	print("====X_train type: {}".format(type(X_train)))
	# SVM
	svm_clf = OneClassSVM(kernel='poly')
	svm_clf.fit(X_train,y_train)
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