import os

directory = r'/mnt/4650AF4250AF3817/Work/BE Project/keystroke/data/user_input/'

def extractFeatures(userId, sessionId):
	global directory
	dataDirectory = directory + '{}/{}/'.format(userId, sessionId)
	tempData = None
	with open(dataDirectory + r'raw_press.txt') as f:
		tempData = f.readlines()
	rawPress = []
	for line in tempData:
		temp = line.split()
		rawPress.append(int(temp[1]))

	with open(dataDirectory + r'raw_release.txt') as f:
		tempData = f.readlines()
	rawRelease = []
	for line in tempData:
		temp = line.split()
		rawRelease.append(int(temp[1]))

	# print("RawPress=> {}".format(rawPress))
	# print("RawRelease=> {}".format(rawRelease))

	pp = []
	pr = []
	rp = []
	rr = []
	for i in range(0, len(rawPress)-1):
		pp.append(rawPress[i+1] - rawPress[i])
		pr.append(rawRelease[i] - rawPress[i])
		rp.append(rawPress[i+1] - rawRelease[i])
		rr.append(rawRelease[i+1] - rawRelease[i])
	pr.append(rawRelease[-1] - rawPress[-1])
	total = rawRelease[-1] - rawPress[0]

	# print("PP=> {}".format('\n'.join(map(str, pp))))
	# print("PR=> {}".format('\n'.join(map(str, pr))))
	# print("RP=> {}".format('\n'.join(map(str, rp))))
	# print("RR=> {}".format('\n'.join(map(str, rr))))
	# print("Total=> {}".format(total))

	ppFile = open(dataDirectory + 'pp.txt', 'w')
	prFile = open(dataDirectory + 'pr.txt', 'w')
	rpFile = open(dataDirectory + 'rp.txt', 'w')
	rrFile = open(dataDirectory + 'rr.txt', 'w')
	totalFile = open(dataDirectory + 'total.txt', 'w')

	ppFile.write('\n'.join(map(str, pp)))
	prFile.write('\n'.join(map(str, pr)))
	rpFile.write('\n'.join(map(str, rp)))
	rrFile.write('\n'.join(map(str, rr)))
	totalFile.write(str(total))

	ppFile.close()
	prFile.close()
	rpFile.close()
	rrFile.close()
	totalFile.close()

# extract(str(36), '2017-03-18T17:55:23')

def addToCSV(userId, sessionId):
	global directory
	dataDirectory = directory + '{}/'.format(userId)
	csvFile = open(dataDirectory + 'userData.csv', 'a')
	if os.path.getsize(dataDirectory + 'userData.csv') == 0:
		csvFile.write('id,date,genuine,password,release_codes,pp,pr,rp,rr,ppavg,pravg,rpavg,rravg,total\n')
	dataDirectory = dataDirectory + '{}/'.format(sessionId)

	ppavg = 0
	pravg = 0
	rpavg = 0
	rravg = 0

	csvFile.write(str(userId) + ',')
	with open(dataDirectory + 'date.txt') as f:
		csvFile.write(f.readline() + ',')
	with open(dataDirectory + 'genuine.txt') as f:
		csvFile.write(f.readline() + ',')
	with open(dataDirectory + 'password.txt') as f:
		csvFile.write(f.readline() + ',')
	with open(dataDirectory + 'release_codes.txt') as f:
		csvFile.write(f.readline() + ',')
	with open(dataDirectory + 'pp.txt') as f:
		lines = [line.strip('\n') for line in f.readlines()]
		csvFile.write(' '.join(lines) + ',')
		lines = list(map(int, lines))
		ppavg = sum(lines)/len(lines)
	with open(dataDirectory + 'pr.txt') as f:
		lines = [line.strip('\n') for line in f.readlines()]
		csvFile.write(' '.join(lines) + ',')
		lines = list(map(int, lines))
		pravg = sum(lines)/len(lines)
	with open(dataDirectory + 'rp.txt') as f:
		lines = [line.strip('\n') for line in f.readlines()]
		csvFile.write(' '.join(lines) + ',')
		lines = list(map(int, lines))
		rpavg = sum(lines)/len(lines)
	with open(dataDirectory + 'rr.txt') as f:
		lines = [line.strip('\n') for line in f.readlines()]
		csvFile.write(' '.join(lines) + ',')
		lines = list(map(int, lines))
		rravg = sum(lines)/len(lines)
	csvFile.write(str(ppavg) + ',')
	csvFile.write(str(pravg) + ',')
	csvFile.write(str(rpavg) + ',')
	csvFile.write(str(rravg) + ',')
	with open(dataDirectory + 'total.txt') as f:
		csvFile.write(f.readline() + '\n')
	csvFile.close()