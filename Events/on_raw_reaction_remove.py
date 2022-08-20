from disnake.ext import commands
import disnake


class onRawReactionRemove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ourMessageID = 927705586722807899

        if ourMessageID == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == '👨':
                role = disnake.utils.get(guild.roles, name="👨・Ele")
            elif emoji == '🌈':
                role = disnake.utils.get(guild.roles, name="🌈・Não-Binário")
            elif emoji == '👩':
                role = disnake.utils.get(guild.roles, name="👩・Ela")  
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
    
def setup(bot):
    bot.add_cog(onRawReactionRemove(bot))