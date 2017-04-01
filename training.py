import sys
# sys.path.append(r'/home/riddhi/keystroke/processing_utils')
sys.path.append(r'/mnt/4650AF4250AF3817/Work/BE Project/keystroke/processing_utils')

import pandas as pd
import numpy as np

from data import get_hashed_matrix
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib

# number of new samples required to create/update the model
sampleSize = 20
windowSize = 100

def trainModel(userId):
	print('Training of model has started')
	userData = pd.read_csv('data/user_input/{}/userData.csv'.format(userId), header= 0)
	global sampleSize
	global windowSize
	if userData.shape[0] % sampleSize == 0:
		# you now have enough samples to create a new/updated model
		if userData.shape[0] > windowSize:
			# move the window i.e use the last 'windowSize' samples
			userData = userData.tail(windowSize)
		X = userData[['release_codes', 'pp','pr', 'rp', 'rr', 'ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
		y = userData['genuine']
		X = get_hashed_matrix(X)

		names = [
			"Isolation Forest Ensemble", 
		]

		classifiers = [
			IsolationForest(random_state=np.random.RandomState(42)),
		]
		for name, clf in zip(names, classifiers):
			clf.fit(X, y)
			joblib.dump(clf, 'data/user_input/{}/userModel-{}.pkl'.format(userId, name))
			# print("\nDumped model for classifier : {}".format(name))
		print('Model has been trained')
	else:
		pass

# trainModel(122)