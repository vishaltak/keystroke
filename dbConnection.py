import bcrypt
import pymysql.cursors

class DBConnection:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='keystroke',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    def addUserCredentials(self):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                username = input('Enter username:\n').strip()
                sql = "SELECT COUNT(`id`) FROM `users` WHERE `username`=%s"
                cursor.execute(sql, (username,))
                if cursor.fetchone()['COUNT(`id`)'] != 0:
                    print('Sorry! this username already exists. Please try again')
                    return False, None
                password = input('Enter password:\n').strip().encode('utf-8')
                sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
                password = bcrypt.hashpw(password, bcrypt.gensalt())
                cursor.execute(sql, (username, password))
            self.connection.commit()
            print('Added the user to the database')
            return True, cursor.lastrowid
        except:
            self.connection.rollback()

    def getUserCredentials(self, userId):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `username`, `password` FROM `users` WHERE `id`=%s"
                cursor.execute(sql, (userId,))
                result = cursor.fetchone()
                dbUsername = result['username']
                dbPassword = result['password']
            return dbUsername, dbPassword
        except:
            self.connection.rollback()

    def closeConnection(self):
        self.connection.close()