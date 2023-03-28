import discord
from discord.ext.commands import Bot

from dotenv import dotenv_values

config = dotenv_values('.env')

TOKEN = config['DISCORD_TOKEN']
GUILD = config['DISCORD_GUILD']
OWNER = config['DISCORD_OWNER']
PREFIX = config['DISCORD_PREFIX']

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
        await ctx.channel.send(f'Aye \'der {ctx.author.mention}.. nice tuh see ya.')

bot.run(TOKEN)
