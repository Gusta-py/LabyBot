from disnake.ext import commands
import datetime
import disnake


class onMessageHelp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild: 
            return
        if message.guild.id != 892799472478871613: 
            return
        if message.author.id == self.bot.user.id:
            return
        whitelist = [892802037186711553, 916716814627667979, 937052487427440760, 937052490237607996, 937052508017295430, 937052521699106847]
        tem = disnake.utils.find(lambda r: r.id in whitelist, message.author.roles)
        if tem: return
        if "ajuda" in message.content.lower():
            await message.reply('Precisando de ajuda? Abra um ticket no canal <#981578389305565234> para um membro da equipe de suporte poder lhe ajudar!')
            return

def setup(bot):
    bot.add_cog(onMessageHelp(bot))