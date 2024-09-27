# bot.py
import os
import datetime
from discord import *
from discord.ext import commands
import botDatabase
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="s!", intents=intents)

@bot.event
async def on_ready():
    botDatabase.loadData()
    print(f'{bot.user} has connected to Discord!')

@bot.event   
async def on_member_join(member):
    channel = bot.get_channel(1289291483479937066)
    rulesChannel = bot.get_channel("ID")
    announcementsChannel = bot.get_channel("ID")
    print(member)
    embed = Embed(
        description=f'Welcome {member.mention} to **STEM-E**! Please complete the following steps:\n' +
        '* Change your nickname to your real name\n' +
        f'* Read and accept {rulesChannel}\n' +
        f'* Review {announcementsChannel}\n',
        color=0xfcec03,
        timestamp=datetime.datetime.now(),
    )
    role = utils.get(member.guild.roles, name='Members')
    await member.add_roles(role)
    await channel.send(embed=embed)

bot.run(TOKEN)
