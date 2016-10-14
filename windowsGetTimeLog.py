import time
import pyHook
import pythoncom

def kbpressevent( event ):
    
    #print key info
    global raw_press
    #When the key is Backspace, it is represented by a prefix "-" in the file. So that line and the preevious line is not to be considered
    if event.Ascii == 8:
        raw_press.write("-"+ str(event)+"\n")
    else:
        raw_press.write(str(event)+"\n")
    print("ese")
    print(event)
    return 0

def kbreleaseevent( event ):
	
    #print key info
    global raw_release
    #When the key is Backspace, it is represented by a prefix "-" in the file. So that line and the preevious line is not to be considered
    if event.Ascii == 8:
        raw_release.write("-"+ str(event)+"\n")
    else:
        raw_release.write(str(event)+"\n")

    #If the ascii value matches enter, terminate the while loop
    if event.Ascii == 13:
        global running
        running = False
    return 0

#Open the files to enter the data
raw_press = open(<filename> , 'w')
raw_release = open(<filename> , 'w')
#raw_press = open(r'D:\keystroke\data\raw_press.txt' , 'w')
#raw_release = open(r'D:\keystroke\data\raw_release.txt' , 'w')

#Create hookmanager
hookman = pyHook.HookManager()
#Define our callback to fire when a key is pressed down
hookman.KeyDown = kbpressevent
#Define our callback to fire when a key is released
hookman.KeyUp = kbreleaseevent
#Hook the keyboard
hookman.HookKeyboard()

#Create a loop to keep the application running
running = True
while running:
    #Start our listener 
    pythoncom.PumpWaitingMessages()
    time.sleep(0.1)

#Close the listener when we are done        
hookman.UnhookKeyboard()
#Close the files
raw_press.close()
raw_release.close()

