from main import *

def search(df):
    a,b,c = input('Enter draft years').split(' ')
    player_name1 = df['player_name'][df['draft_year'] == a].values[0]
    player_name2 = df['player_name'][df['draft_year'] == b].values[0]
    player_name3 = df['player_name'][df['draft_year'] == c].values[0]
    return player_name1, player_name2, player_name3


df2 = df.sort_values('draft_number')

def display_columns(player_name):
    pts = df['pts'][df['player_name'] == str(player_name)]
    season = df['season'][df['player_name'] == str(player_name)]
    return pts, season

def display_plot(season, pts, player_name):
    plt.plot(season, pts, color = 'red', marker = 'o', label = player_name)
    title = 'Average Pts for 1st Draft Pick ' + str(player_name.upper())
    plt.title(title)
    plt.xlabel('Season')
    plt.ylabel('Points')
    plt.legend()
    plt.show()

x ,y, z = search(df2)

pts_x, season_x = display_columns(x)
pts_y, season_y = display_columns(y)
pts_z, season_z = display_columns(z)

display_plot(season_x, pts_x, x )
display_plot(season_y, pts_y, y )
display_plot(season_z, pts_z, z )
