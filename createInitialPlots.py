import pandas as pd
from matplotlib import pyplot as plt

keystroke_data = pd.read_csv(r'data/genuine_user.csv', header= 0)

fig_size = []
fig_size.append(30)
fig_size.append(20)
plt.rcParams["figure.figsize"] = fig_size
fig = plt.figure()

for user in keystroke_data.id.unique():
	user_keystroke_data = keystroke_data[keystroke_data.id == user]
	titles = ['Avg PP', 'Avg PR', 'Avg RP', 'Avg RR', 'Total']
	data = ['ppavg', 'pravg', 'rpavg', 'rravg', 'total']
	for i in range(1,6):
	    ax = fig.add_subplot(3,2,i)
	    ax.tick_params(axis='both', which='major', labelsize=30)
	    ax.text(.5,.9,titles[i-1],
	        horizontalalignment='center',
	        transform=ax.transAxes,
	        size=50)

	    ax.plot(user_keystroke_data[data[i-1]])
	fig.suptitle('User ' + str(user), fontsize=50)
	fig.savefig(r'/mnt/4650AF4250AF3817/Work/BE Project/keystroke/data/graphs/initial-plots/user_' + str(user))
	fig.clear()