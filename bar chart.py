from main import *


x_indexes = np.arange(len(ages))

width = 0.25

plt.bar(x_indexes - width, pts_lebron,color = 'orange', width = width, label = 'Lebron James')
plt.bar(x_indexes, pts_wade, color ='yellow', width = width, label = 'Dwyane Wade')
plt.bar(x_indexes + width, pts_carmelo, color= 'purple',width = width, label = 'Carmelo Anthony')
plt.xlabel('Season')
plt.ylabel('Average Points')
plt.xticks(ticks = x_indexes, labels = ages)
plt.legend()
plt.show()