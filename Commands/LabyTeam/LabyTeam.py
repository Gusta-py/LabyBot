from Config.colors import blurple_color, red_color
from Config.emojis import error_emoji
from disnake.ext import commands
from Config.bot import footer
from disnake import Option
import datetime
import disnake


class LabyTeam(commands.Cog):
   
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam」Use esse comando para trocar o seu apelido no meu servidor de suporte", options=[Option('nick', 'Digite aqui o seu novo nickname', required=True)])
    @commands.guild_only()
    async def mudar_apelido(self, ctx, nick):
        if disnake.utils.find(lambda r: r.id in [939301321687838790], ctx.author.roles):
            try:
                novonick = nick + ' ✦'
                channel = self.bot.get_channel(939591739939881021)
                await ctx.send(f'Seu apelido foi trocado com sucesso para {nick}!', ephemeral=True)
                embed = disnake.Embed(title="Nickname alterado!", description=f"Olá {ctx.author.mention}, só vim aqui dizer que seu nickname foi alterado para **{nick}** com sucesso.", color=blurple_color)
                await ctx.author.send(embed=embed)
                Embed = disnake.Embed(description=f"O membro {ctx.author.mention} trocou o nick para **{nick}**.", timestamp=datetime.datetime.utcnow(), color=blurple_color)
                Embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await ctx.author.edit(nick=novonick)
                await channel.send(embed=Embed)
            except:
                pass
        else:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem o cargo necessário para utilizar esse comando!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
    
def setup(bot):
    bot.add_cog(LabyTeam(bot))