from discord.ext.commands import Bot

class TavernBot(Bot):
    def __init__(self, template):
        super().__init__(**template)

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