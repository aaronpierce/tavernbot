
import os
import random
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OWNER = os.getenv('DISCORD_OWNER')
PREFIX = os.getenv('DISCORD_PREFIX')

intents = discord.Intents.all()
intents.members = True
intents.presences = True
intents.messages = True
intents.typing = True
intents.guilds = True


bot = Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print('Tavern Bot Connected.')

@bot.command()
async def hello(ctx):
        await ctx.channel.send(f'hello there {ctx.author.mention}')

bot.run(TOKEN)
