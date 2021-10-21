from asyncio.windows_events import NULL
from basketball_reference_scraper.players import get_stats
from basketball_reference_scraper.teams import get_roster
import requests
import json
import nest_asyncio


nest_asyncio.apply()
import pandas as pd


def get_name(player):
        
        info = requests.get(" https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()
        
        for player in info['data']:

            player_name = str(player['first_name']) + " " + (player['last_name'])
            id = player['id']

            return(player_name)




def get_player_info(player):

        info = requests.get(" https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()
        
        for player in info['data']:
            postion ="POS: " + player['position']
            height = "Height: " + str(player['height_feet']) + "," + str(player['height_inches'])
            weight = "Weight: " + str(player['weight_pounds']) + " lbs"

            player_info = postion + "\n" + height + '\n' + weight

            return(player_info)

def get_player_stats(player, year):
        display_stats = ''
        id = ''
        info = requests.get("https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()

        for i in info['data']:
            id = i['id']
 

        player_stat = requests.get("https://www.balldontlie.io/api/v1/season_averages?season={}&player_ids[]={}".format(year,id)).json()

        for j in player_stat['data']:
            year = str(year) + "-" + str(int(year[2:])+1)
            ppg = 'PPG: ' + str(j['pts'])
            reb = 'REB: ' + str(j['reb'])
            ast = 'AST: ' + str(j['ast'])
            blk = 'BLK: ' + str(j['blk'])
            stl = 'STL: ' + str(j['stl'])
            to = 'TO: ' + str(j['turnover'])
            fg = 'FG%: ' + str(j['fg_pct'])
            fg3 = '3FG%: ' + str(j['fg3_pct'])

            display_stats = str(get_name(player)) + " " + year + " stats per game:" + '\n'+ '\n' + ppg + '\n' + reb + '\n' + ast + '\n' + blk + '\n' + stl + '\n' + to + '\n' + fg + '\n' + fg3
            
            return(display_stats)


        
        




# def get_player_stats(player,season):
#     stats=''
#     stats= get_stats(get_name(player), stat_type ='PER_GAME', playoffs = False, career=False)

#     for i in stats.index:
#         if stats.iloc[i][0] == str(season):
#             print(stats.iloc[i])
#             return str(stats.iloc[i])

# get_player_stats('lebron','2019-20')



