from discord.ext import commands
from config import settings
import os
bot = commands.Bot(command_prefix=settings['prefix'])
bot.load_extension('DiscordBot.bot')
bot.run(os.environ["Token"])