
import csv
import os
import shutil

database_folder = r"/mnt/4650AF4250AF3817/Work/BE Project/Database/GREYC-Web based KeyStroke dynamics Dataset/database/passwords/"
save_path = r"/mnt/4650AF4250AF3817/Work/BE Project/keystroke/data/"
data = []
counter = 1
symbols = r'~!@#$%^&*()_+{}|:"<>?'
with open(save_path + "genuine_user_cleaned.csv", "w") as av:
	with open(save_path + r'/feilds.txt') as f:
		fd = f.read().splitlines()
	feildnames = fd[0]
	names = feildnames.split()
	fields = ','.join(names)
	av.write(fields + '\n')
	for user in os.listdir(database_folder):
		s_type = ["/genuine/"]
		if not os.path.exists(save_path):
			os.makedirs(save_path)
		
		try:
			for session_type in s_type:
				for session in os.listdir(database_folder + user + session_type):
					if os.path.isdir(database_folder + user + session_type + session):

						with open(database_folder + user + session_type + session + r'/p_release_codes.txt') as f:
							release = f.read().splitlines()
						r = release[0]
						rcode = r.split()
						rc = ' '.join(rcode)
						rc_length = len(rcode)

						with open(database_folder + user + session_type + session + r'/password.txt') as f:
							password = f.readline() 
							password_length = len(password)
							password_length += sum(1 for c in password if c.isupper())
							password_length += sum(1 for c in password if c in symbols)

						print("====rc_length = {}, password_length = {}".format(rc_length, len(password)))
						if(password_length != rc_length):
							print("Skipping the entry becasue it is corrupt!")
							continue


						av.write(str(int(user[-3:len(user)])) + ",")

						with open(database_folder + user + session_type + session + r'/date.txt') as f:
							date = f.readlines() 
							av.write(date[0]+ ",")
						
						with open(database_folder + user + session_type + session + r'/genuine.txt') as f:
							genuine = f.readlines() 
							av.write(genuine[0] + ",")
						
						# with open(database_folder + user + session_type + session + r'/password.txt') as f:
						# 	password = f.readline() 
						# 	av.write(password + ",")
						av.write(password + ",")
						# with open(database_folder + user + session_type + session + r'/p_release_codes.txt') as f:
						# 	release = f.read().splitlines()
						# r = release[0]
						# rcode = r.split()
						# rc = ' '.join(rcode)
						av.write(rc + ",")
						with open(database_folder + user + session_type + session + r'/p_pp.txt') as f:
							temp = []
							for line in f:
								temp.append(line.strip('\n'))
						pp = ' '.join(temp)
						av.write(pp + ",")
						with open(database_folder + user + session_type + session + r'/p_pr.txt') as f:
							temp = []
							for line in f:
								temp.append(line.strip('\n'))
							pr = ' '.join(temp)
						av.write(pr+ ",")
						with open(database_folder + user + session_type + session + r'/p_rp.txt') as f:
							temp = []
							for line in f:
								temp.append(line.strip('\n'))
							rp = ' '.join(temp)
						av.write(rp+ ",")
						with open(database_folder + user + session_type + session + r'/p_rr.txt') as f:
							temp = []
							for line in f:
								temp.append(line.strip('\n'))
							rr = ' '.join(temp)
						av.write(rr+ ",")
						with open(database_folder + user + session_type + session + r'/p_pp.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgpp = sum(data)/len(data)

						av.write("%d," %avgpp)
						with open(database_folder + user + session_type + session + r'/p_pr.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgpr = sum(data)/len(data)
							#print(data)
							#print(avgpr)

						av.write("%d," %avgpr)
						with open(database_folder + user + session_type + session + r'/p_rp.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgrp = sum(data)/len(data)

						av.write("%d," %avgrp)

						with open(database_folder + user + session_type + session + r'/p_rr.txt') as f:
							data = []
							for line in f:
								fields = line.split()
								rowdata = map(float, fields)
								data.extend(rowdata)
							avgrr = sum(data)/len(data)

						av.write("%d," %avgrr)						
						with open(database_folder + user + session_type + session + r'/p_total.txt') as f:
							total = f.readlines()
							av.write(total[0] + "\n")
						#av.write('\n')
						
						print(user)

		except NotADirectoryError:
			pass