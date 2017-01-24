def convertVirtualKeyCode(charCode):	
	if (charCode == 8):	
		value = "backspace"	
		#  backspace
	elif (charCode == 9):	
		value = "tab"	
		#  tab
	elif (charCode == 13):	
		value = "enter"	
		#  enter
	elif (charCode == 16):	
		value = "shelift"	
		#  shelift
	elif (charCode == 17):	
		value = "ctrl"	
		#  ctrl
	elif (charCode == 18):	
		value = "alt"	
		#  alt
	elif (charCode == 19):	
		value = "pause/break"	
		#  pause/break
	elif (charCode == 20):	
		value = "caps lock"	
		#  caps lock
	elif (charCode == 27):	
		value = "escape"	
		#  escape
	elif (charCode == 32):	
		value = "spacebar"	
		#  spacebar
	elif (charCode == 33):	
		value = "page up"	
		# page up, to avoid displaying alternate character and confusing people	         
	elif (charCode == 34):	
		value = "page down"	
		# page down
	elif (charCode == 35):	
		value = "end"	
		# end
	elif (charCode == 36):	
		value = "home"	
		# home
	elif (charCode == 37):	
		value = "left arrow"	
		# left arrow
	elif (charCode == 38):	
		value = "up arrow"	
		# up arrow
	elif (charCode == 39):	
		value = "right arrow"	
		# right arrow
	elif (charCode == 40):	
		value = "down arrow"	
		# down arrow
	elif (charCode == 45):	
		value = "insert"	
		# insert
	elif (charCode == 46):	
		value = "delete"	
		# delete

	elif (charCode == 48):	
		value = "0"	
		# Number 0
	elif (charCode == 49):	
		value = "1"	
		# Number 1
	elif (charCode == 50):	
		value = "2"	
		# Number 2
	elif (charCode == 51):	
		value = "3"	
		# Number 3
	elif (charCode == 52):	
		value = "4"	
		# Number 4
	elif (charCode == 53):	
		value = "5"	
		# Number 5
	elif (charCode == 54):	
		value = "6"	
		# Number 6
	elif (charCode == 55):	
		value = "7"	
		# Number 7
	elif (charCode == 56):	
		value = "8"	
		# Number 8
	elif (charCode == 57):	
		value = "9"	
		# Number 9

	elif (charCode == 65):	
		value = "a"
	elif (charCode == 66):	
		value = "b"
	elif (charCode == 67):	
		value = "c"
	elif (charCode == 68):	
		value = "d"
	elif (charCode == 69):	
		value = "e"
	elif (charCode == 70):	
		value = "f"
	elif (charCode == 71):	
		value = "g"
	elif (charCode == 72):	
		value = "h"
	elif (charCode == 73):	
		value = "i"
	elif (charCode == 74):	
		value = "j"
	elif (charCode == 75):	
		value = "k"
	elif (charCode == 76):	
		value = "l"
	elif (charCode == 77):	
		value = "m"
	elif (charCode == 78):	
		value = "n"
	elif (charCode == 79):	
		value = "o"
	elif (charCode == 80):	
		value = "p"
	elif (charCode == 81):	
		value = "q"
	elif (charCode == 82):	
		value = "r"
	elif (charCode == 83):	
		value = "s"
	elif (charCode == 84):	
		value = "t"
	elif (charCode == 85):	
		value = "u"
	elif (charCode == 86):	
		value = "v"
	elif (charCode == 87):	
		value = "w"
	elif (charCode == 88):	
		value = "x"
	elif (charCode == 89):	
		value = "y"
	elif (charCode == 90):	
		value = "z"

	elif (charCode == 91):	
		value = "left window"	
		# left window
	elif (charCode == 92):	
		value = "right window"	
		# right window
	elif (charCode == 93):	
		value = "select key"	
		# select key
	elif (charCode == 96):	
		value = "numpad 0"	
		# numpad 0
	elif (charCode == 97):	
		value = "numpad 1"	
		# numpad 1
	elif (charCode == 98):	
		value = "numpad 2"	
		# numpad 2
	elif (charCode == 99):	
		value = "numpad 3"	
		# numpad 3
	elif (charCode == 100):	
		value = "numpad 4"	
		# numpad 4
	elif (charCode == 101):	
		value = "numpad 5"	
		# numpad 5
	elif (charCode == 102):	
		value = "numpad 6"	
		# numpad 6
	elif (charCode == 103):	
		value = "numpad 7"	
		# numpad 7
	elif (charCode == 104):	
		value = "numpad 8"	
		# numpad 8
	elif (charCode == 105):	
		value = "numpad 9"	
		# numpad 9
	elif (charCode == 106):	
		value = "multiply"	
		# multiply
	elif (charCode == 107):	
		value = "add"	
		# add
	elif (charCode == 109):	
		value = "subtract"	
		# subtract
	elif (charCode == 110):	
		value = "decimal point"	
		# decimal point
	elif (charCode == 111):	
		value = "divide"	
		# divide
	elif (charCode == 112):	
		value = "F1"	
		# F1
	elif (charCode == 113):	
		value = "F2"	
		# F2
	elif (charCode == 114):	
		value = "F3"	
		# F3
	elif (charCode == 115):	
		value = "F4"	
		# F4
	elif (charCode == 116):	
		value = "F5"	
		# F5
	elif (charCode == 117):	
		value = "F6"	
		# F6
	elif (charCode == 118):	
		value = "F7"	
		# F7
	elif (charCode == 119):	
		value = "F8"	
		# F8
	elif (charCode == 120):	
		value = "F9"	
		# F9
	elif (charCode == 121):	
		value = "F10"	
		# F10
	elif (charCode == 122):	
		value = "F11"	
		# F11
	elif (charCode == 123):	
		value = "F12"	
		# F12
	elif (charCode == 144):	
		value = "num lock"	
		# num lock
	elif (charCode == 145):	
		value = "scroll lock"	
		# scroll lock
	elif (charCode == 186):	
		value = ";"	
		# semi-colon
	elif (charCode == 187):	
		value = "="	
		# equal-sign
	elif (charCode == 188):	
		value = ","	
		# comma
	elif (charCode == 189):	
		value = "-"	
		# dash
	elif (charCode == 190):	
		value = "."	
		# period
	elif (charCode == 191):	
		value = "/"	
		# forward slash
	elif (charCode == 192):	
		value = "`"	
		# grave accent
	elif (charCode == 219):	
		value = "["	
		# open bracket
	elif (charCode == 220):	
		value = "\\"	
		# back slash
	elif (charCode == 221):	
		value = "]"	
		# close bracket
	elif (charCode == 222):	
		value = "'"	
		# single quote

	return:	
		value