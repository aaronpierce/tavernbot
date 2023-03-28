
import discord
from discord.ext.commands import Bot

from dotenv import dotenv_values

load_dotenv('.env')
TOKEN = dotenv_values('DISCORD_TOKEN')
GUILD = dotenv_values('DISCORD_GUILD')
OWNER = dotenv_values('DISCORD_OWNER')
PREFIX = dotenv_values('DISCORD_PREFIX')

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
