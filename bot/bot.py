from discord.ext.commands import Bot
import threading

class TavernBot(Bot):
    def __init__(self, template):
        super().__init__(**template)

        self.rpg = template['rpg']()
        self.client = template['client']
    
        self.server_thread = threading.Thread(target=self.rpg.start)
        self.server_thread.daemon = False
        self.server_thread.start()

        self.add_commands(self)


    async def on_ready(self):
        print('TavernBot hast cometh to the v\'rmilion minotaur.')

    async def on_presence_update(self, before, after):
        if after.status == 'online':
            print(f'{after.display_name} is now {after.status}.')

    def add_commands(self, bot):

        @bot.command()
        async def status(ctx):
            await ctx.channel.send('Ho {ctx.author.mention}! im still h\'re thee blinking idiot.')

        @bot.command()
        async def hello(ctx):
            await ctx.channel.send(f'Greetings to thee {ctx.author.mention}... nice tuh see ya.')

        @bot.command()
        async def play(ctx):
            await self.client('localhost', 9999)