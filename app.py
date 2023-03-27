
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
OWNER = os.getenv('DISCORD_OWNER')
PREFIX = os.getenv('DISCORD_PREFIX')

client = discord.Client(guild_subscriptions=True, intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for member in client.get_all_members():
        print(member)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    one = ['Hello.',
           'Hi',
           'Hey!',
           'Hi there!',
           'Hey there!',
           'Hey man!',
           'Hey bro!',
           'Hey dude!',
           'Hey buddy!',
           'Yo!',
           'Howdy!']

    two = ['How are you?',
           'How are ya?',
           'How are things?',
           'How are things going?',
           'How’s it going?',
           'What’s going on?',
           'How have you been?',
           'How’s everyone?',
           'How’s everyone doing?  ',
           'Whazzup?',
           'Sup?  ',
           'What’s happening?',
           'What are you up to these days?',
           'What’s new?',
           'What’s shaking?',
           'What’s shakin’?',
           'How are you holding up?',
           'Doing OK?',
           'Everything OK?']

    if message.content == '!Hi':
        response = random.choice(one) + ' ' + random.choice(two)
        await message.channel.send(response)

    if message.content == '!m':
        response = 'm!help' # https://open.spotify.com/artist/6159IBm5gLPwG4BcJXseXc?si=2Hc9KEl2Q82l3bXp3Coo_A'
        await message.channel.send(response)


client.run(TOKEN)
