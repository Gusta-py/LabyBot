from disnake.ext import commands
import disnake


class onMessageJoin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id != 892799472478871613: return
        channel = self.bot.get_channel(938813191255887872)
        autorole = disnake.utils.get(member.guild.roles, name = '・Não verificado')
        await member.add_roles(autorole)
        await channel.send(f'{member.mention}', delete_after=1)
  
def setup(bot):
    bot.add_cog(onMessageJoin(bot))