from bot import TavernBot, BotConfig

config = BotConfig()
tavernbot = TavernBot(config.template)

tavernbot.run(config.token)