from Config.emojis import error_emoji
from Config.colors import red_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onSlashError(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        if isinstance(error, commands.BadInviteArgument): 
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O link de convite ``{error.argument}`` é inválido ou expirado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if isinstance(error, commands.NotOwner): 
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas o dono do bot pode utilizar esse comando!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if isinstance(error, commands.CommandOnCooldown): 
            tempo = str(datetime.timedelta(seconds= int(error.retry_after)))
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você já utilizou esse comando recentemente! Por favor espere ``{tempo}`` para utilizar o comando novamente.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return  
            
def setup(bot):
    bot.add_cog(onSlashError(bot))