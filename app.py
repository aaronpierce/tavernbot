from bot import TavernBot, BotConfig
from TavernRPG.server import RPG
from TavernRPG.client import Client

config = BotConfig()
template = config.template
template['rpg'] = RPG
template['client'] = Client

tavernbot = TavernBot(template)
tavernbot.run(config.token)