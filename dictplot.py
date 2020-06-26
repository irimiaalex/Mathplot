from main import *


#prima incercare de dictplot

df2 = df.sort_values(['draft_number', 'draft_round'])
df2['draft_number'] = pd.to_numeric(df2['draft_number'], errors='coerce')
df2['draft_round'] = pd.to_numeric(df2['draft_round'], errors='coerce')


def get_picks(df):
    yr = input('Select the year')
    num = int(input('enter number of top picks'))
    player_counter = Counter()
    ids = df['player_name'][df['draft_year'] == yr]
    for response in ids:
        player_counter.update(response.split(';'))
    player_name_lst = []
    for item in player_counter.most_common():
        player_name_lst.append(item[0])

    top = []
    for name in player_name_lst:
        if df['draft_round'][df['player_name'] == name].values[0] == 1:
            top.append(name)

    top_num_picks = []
    for pl_name in top:
        if df['draft_number'][df['player_name'] == pl_name].values[0] <=num :
            top_num_picks.append(pl_name)
    return top_num_picks

lst_players = get_picks(df2)

def get_csv_pts(lst_plr,df):
    lst_pts =[]
    for name in lst_plr:
        lst_pts.append(df['pts'][df['player_name'] == name].values[:])
    lst_seasons = []
    for name in lst_plr:
        lst_seasons.append(df['season'][df['player_name'] == name].values[:])

    return lst_pts, lst_seasons

lst_pts,lst_seasons = get_csv_pts(lst_players,df2)




def generate_plot(lst_plr, lst_pts,lst_season):
    dict = {}
    nr = 0
    for name in lst_plr:
        dict.update({name : (lst_pts[nr], lst_season[nr])})
        nr+=1
    plt.plot(list(dict.get(name)[0])), list(dict.get(name)[1])
    player_name = name
    plt.title(player_name)
    plt.xlabel('Season')
    plt.ylabel('Points(Units)')
    plt.show()



generate_plot(lst_players,lst_pts,lst_seasons)






