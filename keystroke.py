from enrollment import enroll
from testing import testModel
from training import trainModel

success, userId = enroll()
if success == True:
	trainModel(userId)
	testModel(userId)
else:
	print('DUH')