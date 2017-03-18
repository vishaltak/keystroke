import bcrypt
import os
import pyxhook
import shutil
import time

class User:
    def __init__(self, id, dbUsername, dbPassword):
        date = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
        self.directory = '/mnt/4650AF4250AF3817/Work/BE Project/keystroke/data/user_input/{}/{}/'.format(id, date)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.count = 0
        self.dbPassword = dbPassword
        self.password = None
        self.running = False
        self.passwordFile = open(self.directory + 'password.txt', 'w')
        self.rawPressFile = open(self.directory + 'raw_press.txt', 'w')
        self.rawReleaseFile = open(self.directory + 'raw_release.txt', 'w')
        
        userNameFile = open(self.directory + 'login.txt', 'w')
        userNameFile.write(dbUsername)
        userNameFile.close()

        dateFile = open(self.directory + 'date.txt', 'w')
        dateFile.write(date.replace('T', ' '))
        dateFile.close()


    def kbpressevent(self, event):
        # print(event)
        values = str(event).split()
        self.rawPressFile.write(values[1] + ' ' + values[2] + '\n')

    def kbreleaseevent(self, event):
        # print(event)
        values = str(event).split()
        self.rawReleaseFile.write(values[1] + ' ' + values[2] + '\n')

        #If the ascii value matches enter, terminate the while loop
        if event.Ascii == 13:
            if self.count == 1:
                self.running = False
            self.count += 1
        else:
            self.password += values[0]

    def startLogging(self):

        self.password = ""
        #Create hookmanager
        hookman = pyxhook.HookManager()
        #Define our callback to fire when a key is pressed down
        hookman.KeyDown = self.kbpressevent
        #Define our callback to fire when a key is released
        hookman.KeyUp = self.kbreleaseevent
        #Hook the keyboard
        hookman.HookKeyboard()
        #Start our listener
        hookman.start()

        #Create a loop to keep the application running
        self.running = True
        while self.running:
            time.sleep(0.1)

        #Close the listener when we are done
        hookman.cancel()

        self.passwordFile.write(self.password)

        #Closed the files
        self.passwordFile.close()
        self.rawPressFile.close()
        self.rawReleaseFile.close()

        if not bcrypt.checkpw(self.password.encode('utf-8'), self.dbPassword.encode('utf-8')):
            shutil.rmtree(self.directory)
            print("Removed the sample as password did not match")
            return False
        else:
            return True