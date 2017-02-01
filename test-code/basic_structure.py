import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM
from sklearn.cross_validation import train_test_split
from collections import Counter

keystroke_data = pd.read_csv(r'../data/genuine_user.csv', header= 0)
#print(keystroke_data)
#print(keystroke_data.size)
#print(keystroke_data.columns)
#X = keystroke_data[['ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
#y = keystroke_data['genuine']
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
#print(X)
#print(y)

# k-NN
#knn = KNeighborsClassifier(n_neighbors=3)
#knn.fit(X,y)
#print(knn.predict([[0,0,0,0,0]]))
#print(knn.get_params(deep=True))
results = []
for user in keystroke_data.id.unique():
	user_keystroke_data= keystroke_data[keystroke_data['id'] == user]
	X = user_keystroke_data[['ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
	y = user_keystroke_data['genuine']
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
	# SVM
	svm_clf = OneClassSVM(kernel='poly')
	svm_clf.fit(X_train,y_train)
	#print(svm_clf.get_params())
	#print("Score")
	prediction_results= svm_clf.predict(X_test)
	#print(prediction_results)
	counter= Counter(prediction_results)
	correct_preditions = counter.get(1.0, 0)
	wrong_preditions = counter.get(-1.0, 0)
	results.append({'user':user, 'classifier':'ocsvm', 
		'data':{'correct_preditions':correct_preditions, 'wrong_preditions':wrong_preditions}
	})
	#print("Correct Preditions = {}".format(correct_preditions))
	#print("Wrong Predictions = {}".format(wrong_preditions))

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