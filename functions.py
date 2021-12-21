from asyncio.windows_events import NULL
import requests
import nest_asyncio
from bs4 import BeautifulSoup



nest_asyncio.apply()
import pandas as pd


def get_name(player):
        
        info = requests.get(" https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()
        
        for player in info['data']:

            player_name = '\n' + str(player['first_name']) + " " + (player['last_name'])

            return(player_name)

def get_player_info(player):

        info = requests.get(" https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()
        
        for player in info['data']:
            postion ="**POS**: " + player['position']
            height = "**Height**: " + str(player['height_feet']) + "," + str(player['height_inches'])
            weight = "**Weight**: " + str(player['weight_pounds']) + " lbs"
            # age = "**Age**": + 
            team = "**Team**: " + str(player['team']['full_name'])
        
            player_info = team + '\n' + postion + "\n" + height + '\n' + weight + '\n' 
            return(player_info)

def get_player_stats(player, year):
        display_stats = ''
        id = ''
        info = requests.get("https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()

        for i in info['data']:
            id = i['id']

        player_stat = requests.get("https://www.balldontlie.io/api/v1/season_averages?season={}&player_ids[]={}".format(year,id)).json()

        for j in player_stat['data']:
            year1 =(str(year) + "-" + str(int(year)+1))
            ppg = '**PPG**: ' + str(j['pts'])
            reb = '**REB**: ' + str(j['reb'])
            ast = '**AST**: ' + str(j['ast'])
            blk = '**BLK**: ' + str(j['blk'])
            stl = '**STL**: ' + str(j['stl'])
            to = '**TO**: ' + str(j['turnover'])
            fg = '**FG%**: ' + str(j['fg_pct'])
            fg3 = '**3FG%**: ' + str(j['fg3_pct'])

            display_stats = str(get_name(player)) + " " + year1 + " stats per game:" + '\n' + ppg + '\n' + reb + '\n' + ast + '\n' + blk + '\n' + stl + '\n' + to + '\n' + fg + '\n' + fg3
            
            return(display_stats)

def get_adv_stats(player, year):
        display_stats = ''
        id = ''
        info = requests.get("https://www.balldontlie.io/api/v1/players?search={}".format(player)).json()

        for i in info['data']:
            id = i['id']

        player_stat = requests.get("https://www.balldontlie.io/api/v1/season_averages?season={}&player_ids[]={}".format(year,id)).json()

        for j in player_stat['data']:
            year1 =(str(year) + "-" + str(int(year)+1))
            min = '**Min**: ' + str(j['min'])
            fgm = '**Fgm**: ' + str(j['fgm'])
            fga = '**Fga**: ' + str(j['fga'])
            fg3m = '**Fg3m**: ' + str(j['fg3m'])
            fg3a = '**Fg3a**: ' + str(j['fg3a'])
            ftm = '**Ftm**: ' + str(j['ftm'])
            fta = '**Fta**: ' + str(j['fta'])
            oreb = '**Oreb**: ' + str(j['oreb'])
            dreb = '**Dreb**: ' + str(j['dreb'])
            ft_pct = '**FT%**: ' + str(j['ft_pct']) + '%'

            display_stats = str(get_name(player)) + " " + year1 + " advanced stats per game:" + '\n' + min + '\n' + fgm + '\n' + fga + '\n' + fg3m + '\n' + fg3a + '\n' + ftm + '\n' + fta + '\n' + oreb + '\n' + dreb + '\n' + ft_pct
        
            return display_stats





