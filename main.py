from matplotlib import pyplot as plt
import pandas as pd
import csv
import numpy as np
from collections import Counter
import re

df = pd.read_csv('all_seasons.csv')
df['eff'] = df['pts'] + df['reb'] + df['ast']






'''ages = df['season'][df['player_name'] == 'LeBron James'].head(16)

pts_lebron = df['pts'][df['player_name'] == 'LeBron James'].head(16)
pts_carmelo =  df['pts'][df['player_name'] == 'Carmelo Anthony'].head(16)
pts_wade = df['pts'][df['player_name'] == 'Dwyane Wade'].head(16)
plt.plot(ages, pts_lebron, label = 'Lebron James', marker ='*')
plt.plot(ages,pts_wade, label = 'Dwyane Wade', marker = 'o' )
plt.plot(ages, pts_carmelo, label = 'Carmelo Anthony', marker = '>')
plt.xlabel('Season')
plt.ylabel('Average Points')
plt.grid()
plt.legend()
plt.show()
'''





