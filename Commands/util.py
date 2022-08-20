from Config.colors import red_color, green_color, white_color
from Config.emojis import error_emoji
from disnake.ext import commands
from Config.bot import footer
from disnake import Option
import datetime
import disnake
import asyncio


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="「💡 Útil」Crie um lembrete!", options=[Option('tempo', 'Tempo do lembrete', required=True), Option('lembrete', 'O seu lembrete', required=True)])
    @commands.guild_only()
    async def lembrete(self, ctx, tempo, *, lembrete):
        def convert(tempo):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = tempo[-1]

            if unit not in pos:
                return -1
            try:
                val = int(tempo[:-1])
            except:
                return -2
            
            return val * time_dict[unit]
        converted_time = convert(tempo)
        
        if converted_time == -1:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Parece que você cometeu um erro, veja abaixo o porque dessa mensagem.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.add_field(name="Erro:", value="``Você não digitou o tempo corretamente!``")
            ErrorEmbed.add_field(name="Explicação:", value="``s`` = ``Segundos`` | ``m`` = ``Minutos`` | ``h`` = ``Horas`` | ``d`` = ``Dias``", inline=False)
            ErrorEmbed.add_field(name="Exemplo:", value="``/lembrete 8m Beber água``", inline=False)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
              
        embed = disnake.Embed(title="Lembrete ativado!", description=f"Irei te lembrar em **{tempo}**", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.add_field(name="Lembrete:", value=f"**{lembrete}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/916835300213403699.png?size=80")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
        
        embed = disnake.Embed(title="Lembrete ativado!", description=f"Passando pra te relembrar que irei te lembrar em **{tempo}**", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.add_field(name="Lembrete:", value=f"**{lembrete}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/916835300213403699.png?size=80")
        embed.set_footer(text=footer)
        await ctx.author.send(embed=embed)
        
        await asyncio.sleep(converted_time)
        embed = disnake.Embed(title="Lembrete completo!", description=f"{ctx.author.mention} Você tem um lembrete!", timestamp=datetime.datetime.utcnow(), color=green_color)
        embed.add_field(name="Estou te lembrando que:", value=f"**{lembrete}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/918687075463753728.png?size=80")
        embed.set_footer(text=footer)
        await ctx.channel.send(content=f'{ctx.author.mention}', embed=embed)
        
        embed = disnake.Embed(title="Lembrete completo!", description=f"{ctx.author.mention} Você tem um lembrete! Lembra do lembrete que você criou no **({ctx.guild.name})**?", timestamp=datetime.datetime.utcnow(), color=green_color)
        embed.add_field(name="Lembrete:", value=f"**{lembrete}**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/918687075463753728.png?size=80")
        embed.set_footer(text=footer)
        await ctx.author.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Util(bot))