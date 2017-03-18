import bcrypt
import pymysql.cursors
import os
import linuxGetTimelog
import sys
from termios import tcflush, TCIOFLUSH

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='keystroke',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
        username = input('Enter username:\n').strip()
        password = input('Enter password:\n').strip().encode('utf-8')
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        cursor.execute(sql, (username, password))

    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT `id`, `username`, `password` FROM `users` WHERE `username`=%s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        dbId = result['id']
        dbUsername = result['username']
        dbPassword = result['password']
finally:
    connection.close()

counter = 0
print("Starting the Enrollment process")
while counter < 2:
    print("Sample => {}".format(counter + 1))
    username = input('Enter username:\n').strip()
    print('Enter password:')
    user = linuxGetTimelog.User(dbId, dbUsername, dbPassword)
    if user.startLogging() == True:
        counter += 1
    sys.stdout.flush();
    tcflush(sys.stdin, TCIOFLUSH)