import os
import discord
from discord import message
from functions import get_name,get_player_info,get_player_stats,get_adv_stats
client = discord.Client()



@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    list = []
    name = ''
    help = "\n**Help Menu**:\n**Basic Info**: .'player_name'\n**Basic Stats**: .'player_name', 'year'\n**Advanced Stats**: .'player_name', 'year', adv\n**Team Stats**: .'team_name'\n**Help Menu**: .help\n**Support**: .support\n-----------" 
    if message.author == client.user:
        return

    if message.content.startswith('.'):
        x = message.content.split(",")
        name = x[0].replace('.','')

        if message.content == '.help':
            await message.channel.send(help)
        else:
            if len(x)==1:
                try:
                    await message.channel.send(get_name(name))
                    await message.channel.send(get_player_info(name))
                    await message.channel.send("-----------")
                         
                except Exception as e1:
                    await message.channel.send('**THERE IS AN ERROR IN THE REQUEST YOU SENT**')
                    await message.channel.send("\nCheck the the formatting from the '**.help**' menu")
                    await message.channel.send("-----------")
                    
            else:
                try:
                    year = x[1]
                    if len(x)>2 and x[-1]=='adv':
                        await message.channel.send(get_adv_stats(name,year))
                        await message.channel.send("-----------")
                    elif len(x)==2:
                        await message.channel.send(get_player_stats(name,year))
                        await message.channel.send("-----------")
                    else:
                        raise ValueError
                except Exception as e2:
                    await message.channel.send('**THERE IS AN ERROR IN THE REQUEST YOU SENT**')
                    await message.channel.send("\nCheck the the formatting from the '**.help**' menu")
                    await message.channel.send("-----------")
    
client.run(os.environ.get('TOKEN'))


