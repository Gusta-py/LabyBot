from Config.colors import red_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onMessageDelete(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.guild: 
            return
        if message.guild.id != 892799472478871613: 
            return
        if message.author.id == 908870304909115432:
            return 
        cargo1 = disnake.utils.get(message.guild.roles, name='・Visitante')
        whitelist = [892802037186711553, 916716814627667979, 937052487427440760, 937052490237607996, 937052508017295430, 937052521699106847]
        tem = disnake.utils.find(lambda r: r.id in whitelist, message.author.roles)   
        if tem: return
        if cargo1 in message.author.roles: 
            channel = self.bot.get_channel(939652081294409798)
            embed = disnake.Embed(title="Mensagem apagada!", description=f'Mensagem apagada por: {message.author.mention}.\n\nChat da mensagem: {message.channel.mention}', timestamp=datetime.datetime.utcnow(), color=red_color)
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
            embed.add_field(name='Mensagem:', value=f"```{message.content}```")
            embed.set_footer(text=footer)

            await channel.send(embed=embed) 
    
def setup(bot):
    bot.add_cog(onMessageDelete(bot))