from main import *


ids = df['player_name']
player_counter = Counter()

for response in ids:
    player_counter.update(response.split(';'))

player_name = []
years_played = []

for item in player_counter.most_common(8):
    player_name.append(item[0])
    years_played.append(item[1])
player_name.reverse()
years_played.reverse()
plt.barh(player_name, years_played)
plt.title('NBA Longevity')
plt.tight_layout()
plt.show()
