from logging import info
from os import name
from typing import ContextManager
import discord
from discord import player
from functions import get_name,get_player_info,get_player_stats
import urllib3

client = discord.Client()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    list = []
    name = ''
    if message.author == client.user:
        return

    if message.content.startswith('-'):

        x = message.content.split(",")
        name = x[0].replace('-','')

        await message.channel.send(get_name(name))
        await message.channel.send(get_player_info(name))
        await message.channel.send("-----")
    
        try:
            t = x[1]
        except IndexError:
            pass
        else:
            year = x[1]
            await message.channel.send(get_player_stats(name,year))
        

            
        #await message.channel.send(get_player_stats(message.content[1:]))

# @commands.command()
# async def year(message):
#     await ctx.send('Enter Year: ')
#     message_response = client.wait_for('message', check=lambda m: m.user == ctx.user)
#     year = int(message_response.content)
#     print(year)
        


    
client.run('ODk4ODA3MzExMDgxMDIxNTEy.YWpliQ.PR9rKXxXLTXL59ZqVSL143B3phs')


