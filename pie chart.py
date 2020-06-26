from main import *
i = input( 'enter player name')
ids = df['team_abbreviation'][df['player_name'] == i]

team_counter = Counter()

for response in ids:
    team_counter.update(response.split(';'))

team_name = []
years_played = []

for item in team_counter.most_common():
    team_name.append(item[0])
    years_played.append(item[1])

slices = years_played
labels = team_name
plt.pie(slices, labels = labels, wedgeprops = {'edgecolor' : 'black'})
plt.title('Years Played for each team')
plt.show()
