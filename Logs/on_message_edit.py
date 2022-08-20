from Config.colors import yellow_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onMessageEdit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        if not message_before.guild: 
            return
        if message_before.guild.id != 892799472478871613: 
            return
        if message_before.author.id == 908870304909115432:
            return 
        cargo1 = disnake.utils.get(message_before.guild.roles, name='・Visitante')
        whitelist = [892802037186711553, 916716814627667979, 937052487427440760, 937052490237607996, 937052508017295430, 937052521699106847]
        tem = disnake.utils.find(lambda r: r.id in whitelist, message_before.author.roles)
        if tem: return
        if cargo1 in message_before.author.roles: 
            channel = self.bot.get_channel(939652081294409798)
            embed = disnake.Embed(title='Mensagem editada!', description=f'Mensagem editada por: {message_before.author.mention}.\n\nChat da mensagem: {message_before.channel.mention}.\n\nClique **[aqui](https://discord.com/channels/{message_before.guild.id}/{message_before.channel.id}/{message_before.id})** para ir para a mensagem.', timestamp=datetime.datetime.utcnow(), color=yellow_color)
            embed.set_thumbnail(url=message_before.author.avatar.url)
            embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
            embed.add_field(name='Antes:', value=f"```{message_before.content}```", inline=False)
            embed.add_field(name='Depois:', value=f"```{message_after.content}```", inline=False)
            embed.set_footer(text=footer)

            await channel.send(embed=embed)
    
def setup(bot):
    bot.add_cog(onMessageEdit(bot))