import os
import linuxGetTimelog
import sys

from dbConnection import DBConnection
from extraction import extractFeatures, addToCSV
from termios import tcflush, TCIOFLUSH

userId = None

def enroll():
    db = DBConnection()
    success, dbId = db.addUserCredentials()
    if success != True:
        return False, None
    dbUsername, dbPassword = db.getUserCredentials(dbId)
    print('Starting the Enrollment process')
    counter = 0
    while counter < 20:
        print('Sample => {}'.format(counter + 1))
        username = input('Enter username:\n').strip()
        if username != dbUsername:
            print('Removed the sample as username did not match')
            continue
        print('Enter password:')
        user = linuxGetTimelog.User(dbId, dbUsername, dbPassword)
        success, date = user.startLogging()
        if success == True:
            extractFeatures(dbId, date)
            addToCSV(dbId, date)
            counter += 1
        sys.stdout.flush();
        tcflush(sys.stdin, TCIOFLUSH)
    db.closeConnection()
    global userId
    userId = dbId
    print("Enrollment Process over")
    return True, userId