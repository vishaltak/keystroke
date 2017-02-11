import pandas as pd
import pprint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM
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
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

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

# results are only for positive samples. negactive samples have not yet been tested
for result in results:
	user= result.get('user')
	classifier= result.get('classifier')
	correct_preditions= result.get('data').get('correct_preditions')
	wrong_preditions= result.get('data').get('wrong_preditions')
	accuracy= correct_preditions/(correct_preditions + wrong_preditions)*100

	print("User: {} => Classifier: {} => Correct: {}, Wrong: {}, Accuracy: {:.2f}%"
		.format(
			str(user).rjust(3), 
			str(classifier).rjust(6), 
			str(correct_preditions).rjust(3), 
			str(wrong_preditions).rjust(3), 
			accuracy
		)
	)