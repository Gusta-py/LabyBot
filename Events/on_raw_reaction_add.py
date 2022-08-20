from disnake.ext import commands
import disnake


class onRawReactionAdd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ourMessageID = 927705586722807899
        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild
            
            emoji = payload.emoji.name
            if emoji == '👨':
                role = disnake.utils.get(guild.roles, name="👨・Ele")
            elif emoji == '🌈':
                role = disnake.utils.get(guild.roles, name="🌈・Não-Binário")
            elif emoji == '👩':
                role = disnake.utils.get(guild.roles, name="👩・Ela")
            
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(onRawReactionAdd(bot))