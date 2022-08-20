from Config.bot import token, token_testes, prefix, intents
from disnake.ext import commands
import os


bot = commands.Bot(command_prefix=prefix, test_guilds=None, owner_id=901498839981236235, intents=intents)
bot.remove_command("help")
bot.sniped_messages = {}


def load_cogs(bot):
    bot.load_extension("events")

    for file in os.listdir("Events"): 
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Events.{cog}")

    for file in os.listdir("Logs"): 
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Logs.{cog}")

    
    for file in os.listdir("Commands"): 
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Commands.{cog}")
               
    for file in os.listdir("./Commands/LabyTeam"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"Commands.LabyTeam.{cog}")
    
load_cogs(bot)

bot.run(token)

#bot.run(token_testes)
