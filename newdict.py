from main import *


df['draft_number'] = pd.to_numeric(df['draft_number'], errors='coerce')

def get_picks(df):
    yr = input('Enter draft year')
    num = int(input('enter number of picks'))
    new_df = df[(df['draft_year'] == yr) & (df['season'].str.contains(yr)) & (df['draft_round'] =='1')]
    dfdf = new_df.sort_values('draft_number')
    names = dfdf['player_name'].values[:num]
    return names


names = get_picks(df)

def get_points_seasons(names,df):
    pts_lst=[]
    seasons_lst =[]
    for name in names:
        pts_lst.append(df['pts'][df['player_name'] == name].values[:])
        seasons_lst.append(df['season'][df['player_name'] == name].values[:])
    return pts_lst, seasons_lst

pts_lst, seasons_lst = get_points_seasons(names,df)


def generate_plot(names,pts_lst,seasons_lst):
    dict={}
    nr = 0
    for name in names:
        dict.update({name: (pts_lst[nr], seasons_lst[nr])})
        nr +=1
    for key in dict:
        plt.title(key)
        pts = list(dict.get(key)[0])
        seasons = list(dict.get(key)[1])
        plt.plot(seasons, pts)
        plt.xlabel('Season')
        plt.ylabel('Points(UNITS)')
        plt.show()

generate_plot(names,pts_lst,seasons_lst)
