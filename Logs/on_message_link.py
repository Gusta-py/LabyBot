from Config.emojis import id_emoji, users_emoji, link_emoji, text_channel_emoji, userinfo_emoji, warning_emoji
from Config.colors import yellow_color
from disnake.ext import commands
import datetime
import disnake

class onMessageLink(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, mensagem):
        if not mensagem.guild:
            return
        if mensagem.guild.id != 892799472478871613: 
            return
        if mensagem.author.id == self.bot.user.id:
            return
        whitelist = [892802037186711553, 916716814627667979, 937052487427440760, 937052490237607996, 937052508017295430, 937052521699106847]
        tem = disnake.utils.find(lambda r: r.id in whitelist, mensagem.author.roles)   
        if tem: return
        whitelist2 = [937083319819051088, 937128041191178260]
        
        if mensagem.channel.id not in whitelist2:
            conteudo = mensagem.content.lower()

            links = ["https://", "discord.gg"]

            if any(word in conteudo for word in links):
                await mensagem.delete()

                channel2 = self.bot.get_channel(988916851172048907)
                embed = disnake.Embed(description=f"{warning_emoji} | Um domínio registrado recentemente foi detectado!", timestamp=datetime.datetime.utcnow(), color=yellow_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.add_field(name=f"{link_emoji} | Mensagem com o link detectado:", value=f"||{mensagem.content}||")
                embed.add_field(name=f"{text_channel_emoji} | Canal:", value=mensagem.channel.mention, inline=False)
                embed.add_field(name=f"{userinfo_emoji} | Membro:", value=mensagem.author.mention)
                embed.add_field(name=f"{users_emoji} | Tag do usuário:", value=f"``{mensagem.author}``")
                embed.add_field(name=f"{id_emoji} | ID:", value=f"``{mensagem.author.id}``")
                embed.set_footer(text="LabyBot Logs, todos os direitos reservados.")
                await channel2.send(embed=embed)

def setup(bot):
    bot.add_cog(onMessageLink(bot))