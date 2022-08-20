from disnake.ext import commands
import disnake


class onReactionRemove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ourMessageID = 927705730537115679

        if ourMessageID == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == '🎒':
                role = disnake.utils.get(guild.roles, name="13-16 Anos")
            elif emoji == '🍺':
                role = disnake.utils.get(guild.roles, name="17-21 Anos")
            elif emoji == '💼':
                role = disnake.utils.get(guild.roles, name="22+")  
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
    
def setup(bot):
    bot.add_cog(onReactionRemove(bot))