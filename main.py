import discord.ext.commands as commands
import os

bot = commands.Bot('!')

# Cogs

# End cogs


bot.run(os.environ['token'])