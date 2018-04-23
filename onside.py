import csv, collections
import matplotlib.pyplot as plt
onsides = []
successful_onsides = []

all_onsides = csv.reader(open('onside.csv'), quotechar='"')
for onside in all_onsides:
	onsides.append(onside)
	if 'RECOVERED' in onside[18]:
		#successfull
		successful_onsides.append(onside)
# for so in successful_onsides:
	# print(*so, sep='|')
	
total_onsides = len(onsides)
total_successes = len(successful_onsides)
rate = total_successes / total_onsides
# print(rate)
labels = 'Recoveries', 'Failures'
sizes = [total_successes, total_onsides-total_successes]
colors = ['yellowgreen', 'lightcoral']
explode=[0.05,0]
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%',shadow=True, explode=explode, startangle=120)
plt.axis('equal')
plt.title('Onside Kick Recovery Rates in the NFL From 2011 - 2015')

# teams = [x[17] for x in onsides][1:]
# team_count = collections.Counter(teams)
# # print(team_count)
# x = list(team_count.keys())
# height = list(team_count.values())
# plt.bar(x, height)
# plt.title('Onside Kick Attempts by Team')
# plt.xlabel('Team')
# plt.ylabel('Attempts')
plt.show()