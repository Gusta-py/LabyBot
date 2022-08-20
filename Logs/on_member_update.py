from Config.colors import pink_color
from disnake.ext import commands
import disnake


class onMessageUpdate(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, after, before):
        cargo = before.guild.premium_subscriber_role
        if before.guild is None:
            return
        if before.guild.id != 892799472478871613: 
            return
            
        if cargo not in before.roles and cargo in after.roles:
            channel = self.bot.get_channel(950218542421258240)
            guild = self.bot.get_guild(892799472478871613)
            embed = disnake.Embed(title="Muito obrigado por impulsionar o servidor! ❤", description="Muito obrigado por impulsionar o meu servidor! Com isso você ganhou o cargo Laby Booster que em breve terá benefícios. 👀", color=pink_color)
            embed.set_thumbnail(before.author.avatar.url)
            await before.author.send(embed=embed)
            print("Embed enviada.")
            msg = await channel.send(f'{before.mention} impulsionou o servidor e agora estamos com **{guild.premium_subscription_count}** boosts! Obrigado! ❤')
            await msg.add_reaction("🎉")
            return
    
    
def setup(bot):
    bot.add_cog(onMessageUpdate(bot))