import csv
import os

save_path = r"/home/riddhi/keystroke/output_numpy/dataset/"
csv_file = save_path + r"genuine_user.csv"
inputfileloc = save_path + r"genuine.txt"
inputfile = open(inputfileloc, 'r')
with open(csv_file, 'w') as csvfile:
	fieldnames = ['user', 'pr', 'pp', 'rp', 'rr', 'total', 'output']
	csvwriter = csv.DictWriter(csvfile, fieldnames= fieldnames)
	csvwriter.writeheader()
	#csvwriter.writerow({'user':'1', 'pp':'2', 'pr':'3', 'rp':'4', 'rr':'5', 'total':'10', 'output':'1'})
	#csvwriter.writerow({'user':'2', 'pp':'2', 'pr':'3', 'rp':'4', 'rr':'5', 'total':'10', 'output':'1'})
	lines = [line[:-1] for line in inputfile]
	print(lines)
	for line in lines:
		line = line.split()
		print(line)
		csvwriter.writerow({'user':line[0], 'pp':line[1], 'pr':line[2], 'rp':line[3], 'rr':line[4], 'total':line[5], 'output':line[6]})

inputfile.close()