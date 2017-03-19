import sys
# sys.path.append(r'/home/riddhi/keystroke/processing_utils')
sys.path.append(r'/mnt/4650AF4250AF3817/Work/BE Project/keystroke/processing_utils')

import pandas as pd
import numpy as np
import linuxGetTimelog

from data import get_hashed_matrix
from dbConnection import DBConnection
from extraction import extractFeatures, addToCSV
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib
from termios import tcflush, TCIOFLUSH

def testModel(userId):
    print('Let us test the created model')
    db = DBConnection()
    dbUsername, dbPassword = db.getUserCredentials(userId)
    username = input('Enter username:\n').strip()
    if username != dbUsername:
        print('Removed the sample as username did not match')
        return
    print('Enter password:')
    user = linuxGetTimelog.User(userId, dbUsername, dbPassword)
    success, date = user.startLogging()
    if success == True:
        extractFeatures(userId, date)
        addToCSV(userId, date)
    sys.stdout.flush();
    tcflush(sys.stdin, TCIOFLUSH)

    userData = pd.read_csv('data/user_input/{}/userData.csv'.format(userId), header= 0).tail(1)
    X = userData[['release_codes', 'pp','pr', 'rp', 'rr', 'ppavg', 'pravg', 'rpavg', 'rravg', 'total']]
    X = get_hashed_matrix(X)

    names = [
        "Isolation Forest Ensemble", 
    ]

    classifiers = [
        IsolationForest(random_state=np.random.RandomState(42)),
    ]
    for name, clf in zip(names, classifiers):
        # print("\nLoading classifier : {}".format(name))
        clf = joblib.load('data/user_input/{}/userModel-{}.pkl'.format(userId, name))
        result = clf.predict(X)
        if result[0] == 1:
            print('Welcome')
        else:
            print('Stay away impostor!')

# testModel(114)