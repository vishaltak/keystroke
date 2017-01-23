
import csv
import os
import shutil

database_folder = r"/home/riddhi/keystroke/output_numpy/custom_dataset/"
save_path = r"/home/riddhi/keystroke/output_numpy/dataset/"
csv_file = save_path + r"data.csv"
data = []
counter = 1
with open(save_path + "genuine.txt", "w") as av:
	for user in os.listdir(database_folder):
		s_type = ["/genuine/"]
		if not os.path.exists(save_path):
			os.makedirs(save_path)
		try:
			for session_type in s_type:
				for session in os.listdir(database_folder + user + session_type):
					if os.path.isdir(database_folder + user + session_type + session):
						with open(database_folder + user + session_type + session + r'/pr.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgpr = sum(data)/len(data)
							print(data)
							print(avgpr)
						av.write("%d, " %avgpr)

						with open(database_folder + user + session_type + session + r'/pp.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgpp = sum(data)/len(data)
						av.write("%d, " %avgpp)

						with open(database_folder + user + session_type + session + r'/rp.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgrp = sum(data)/len(data)
						av.write("%d, " %avgrp)

						with open(database_folder + user + session_type + session + r'/rr.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgrr = sum(data)/len(data)
						av.write("%d, " %avgrr)
						with open(database_folder + user + session_type + session + r'/total.txt') as f:
							total = f.readlines() 
							av.write(total[0]+ ', ')

						av.write(str(int(user[-3:len(user)])) +'\n')
						print(user)

		except NotADirectoryError:
			pass