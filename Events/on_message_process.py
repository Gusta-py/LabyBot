from Commands.utils import process_message_as_guess
from disnake.ext import commands
import disnake


class onMessage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        processed_as_guess = await process_message_as_guess(self.bot, message)
        if not processed_as_guess:
            await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(onMessage(bot))