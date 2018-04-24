import csv, collections
import matplotlib.pyplot as plt
import numpy as np
onsides = []
successful_onsides = []
unsuccessful = []
first_half = []
all_onsides = csv.reader(open('onside.csv'), quotechar='"')
for onside in all_onsides:
	onsides.append(onside)
	if 'RECOVERED' in onside[18]:
		#successfull
		successful_onsides.append(onside)
	else: 
		unsuccessful.append(onside)
	if 'TimeSecs' not in onside[7] and int(onside[7]) >= 1800:
		first_half.append(onside)
# for so in successful_onsides:
	# print(*so, sep='|')
print(len(first_half))	
total_onsides = len(onsides)
total_successes = len(successful_onsides)
rate = total_successes / total_onsides
# print(rate)

recovery_epa = [float(x[-12]) for x in successful_onsides]
recovery_wpa = [float(x[-4]) for x in successful_onsides] # if x[62] != '1' else 0
wpa = [-float(x[-4]) for x in onsides[1:]]
# print(recovery_epa)
# print(sum(recovery_epa) / len(recovery_epa)) #mean EPA for successful onside kicks
# print(sum(recovery_wpa) / len(recovery_wpa)) #mean WPA for successful onside kicks


timesecs = [float(x[7]) for x in onsides[1:]]
recovered = [1 if 'RECOVERED' in x[18] else 0 for x in onsides[1:]]
winprob_pre = [float(x[-9]) if x[17] == x[71] else float(x[-8]) for x in onsides[1:]]
home = [x[71] for x in onsides[1:]]
away = [x[72] for x in onsides[1:]]
kickingteam = [x[17] for x in onsides[1:]]

scorediff = [-int(x[69]) for x in onsides[1:]]
x, y = zip(*sorted(zip(scorediff, wpa)))
plt.scatter(x, y)
plt.title('Score Differential vs. WPA For Kicking Team')
plt.xlabel('Kicking Team\'s Score Margin')
plt.ylabel('Kicking Teams\'s Win Probability Added')
#State of game score pie chart
# scorediff = [x[69] for x in onsides[1:]]
# abs_scorediff = [x[70] for x in onsides[1:]]
# tied, down, up = 0, 0, 0
# for diff in scorediff:
	# if diff == '0':
		# tied += 1
	# elif int(diff) > 0:
		# down += 1
	# else:
		# up += 1
# labels = 'Tied', 'Losing', 'Winning'
# sizes = [tied, down, up]
# plt.axis('equal')
# plt.title('Game Score State During Onside Kicks')
# plt.pie(sizes, labels=labels, startangle=130, autopct='%1.1f%%', shadow=True)


# print(winprob_pre)
# bins = np.array([0.0, 0.01, 0.02, 0.070, 0.35, 1])
# x = np.array(winprob_pre)
# inds = np.digitize(x, bins)
# binned = {}
# for i in range(len(winprob_pre)):
	# if inds[i] in binned:
		# binned[inds[i]].append(recovered[i])
	# else:
		# binned[inds[i]] = []
		# binned[inds[i]].append(recovered[i])
# binned_rates = dict(zip(binned.keys(), [sum(x)/len(x) for x in binned.values()]))		
# print(binned_rates)
# rates = []
# for i in range(1,6):
	# rates.append(binned_rates[i])
# plt.xticks(np.arange(5), ('0.0-0.01', '0.01-0.02', '0.02-0.07', '0.07-0.35', '0.35-1'))
# plt.title('Onside Kick Percentage By WinProb of Kicking Team Pre-kick')
# plt.xlabel('WinProb')
# plt.ylabel('Percentage')
# plt.plot([0,1,2,3,4], rates)

# pie chart for recovery rate
# labels = 'Recoveries', 'Failures'
# sizes = [total_successes, total_onsides-total_successes]
# colors = ['yellowgreen', 'lightcoral']
# explode=[0.05,0]
# plt.pie(sizes, labels=labels, startangle=100, colors=colors,autopct='%1.1f%%', explode=explode)
# plt.axis('equal')
# plt.title('Onside Kick Recovery Rates in the NFL From 2011 - 2015')

# pie chart for which quarter onsides are attempted
# quarter = [x[3] for x in onsides][1:]
# qtrcount = collections.Counter(quarter)
# labels = ["qtr " + x for x in qtrcount.keys()]
# sizes = qtrcount.values()
# # explode = [0, 0.05, 0, 0, 0]
# colors = ['lightskyblue', 'purple', 'yellowgreen', 'gold', 'lightcoral']
# patches, texts, something = plt.pie(sizes, colors=colors, shadow=True,autopct='%1.1f%%')
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.title("When Are Onside Kicks Taken?")
# plt.tight_layout()

# bar chart for kick frequencies per team
# teams = [x[17] for x in onsides][1:]
# team_count = collections.Counter(teams)
# # print(team_count)
# x = list(team_count.keys())
# height = list(team_count.values())
# plt.bar(x, height)
# plt.title('Onside Kick Attempts Per Team')
# plt.xlabel('Team')
# plt.ylabel('Attempts')

# bar chart for kick frequencies against each team
# teams = [x[16] for x in onsides][1:]
# team_count = collections.Counter(teams)
# # print(team_count)
# x = list(team_count.keys())
# height = list(team_count.values())
# plt.bar(x, height)
# plt.title('Onside Kick Attempts Against Each Team')
# plt.xlabel('Team')
# plt.ylabel('Attempts Against')

plt.show()