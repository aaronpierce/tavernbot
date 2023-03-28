from dotenv import dotenv_values
from discord import Intents

class BotConfig():
	def __init__(self):
		self.root = dotenv_values('.env')

		self.token = self.root['DISCORD_TOKEN']
		self.guild = self.root['DISCORD_GUILD']
		self.owner = self.root['DISCORD_OWNER']
		self.prefix = self.root['DISCORD_PREFIX']

		self.case_insensitive = True

		self.intents = None
		self.setup_intents()

		self.template = None
		self.setup_template()

	def setup_intents(self):
		intents = Intents.all()

		intents.members = True
		intents.presences = True
		intents.messages = True
		intents.typing = True
		intents.guilds = True

		self.intents = intents

	def setup_template(self):
		self.template = {'command_prefix':self.prefix,
								'intents':self.intents,
								'case_insensitive':self.case_insensitive}