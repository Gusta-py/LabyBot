from disnake.ext import commands
import disnake


class onReactionAdd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ourMessageID = 927705730537115679
        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild
            
            emoji = payload.emoji.name
            if emoji == '🎒':
                role = disnake.utils.get(guild.roles, name="13-16 Anos")
            elif emoji == '🍺':
                role = disnake.utils.get(guild.roles, name="17-21 Anos")
            elif emoji == '💼':
                role = disnake.utils.get(guild.roles, name="22+ Anos")
            
            await member.add_roles(role)
    
def setup(bot):
    bot.add_cog(onReactionAdd(bot))