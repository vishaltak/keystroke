import platform

if platform.system() == 'Windows':
	exec(open(<filename>).read())
	#exec(open(r'/home/tak/Desktop/keystroke/windowsGetTimelog.py').read())
	#exec(open(r'D:\keystroke\windowsGetTimelog.py').read())
elif platform.system() == 'Linux':
	exec(open(<filename>).read())
	#exec(open(r'/home/tak/Desktop/keystroke/linuxGetTimelog.py').read())
	#exec(open(r'D:\keystroke\linuxGetTimelog.py').read())
else:
	print('OS not yet supported. Please be patient.')