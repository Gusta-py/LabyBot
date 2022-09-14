from Config.emojis import error_emoji, folder_emoji, confirm_emoji, rules_emoji, interrogation_emoji
from Config.colors import blurple_color, white_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class Verificação(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.slash_command(description="a")
    #async def embed(self, ctx):
        #channel = self.bot.get_channel(938813191255887872)
        #embed = disnake.Embed(title="__LabyBot Support | Sistema de Verificação__", description="<:892799472478871613:916846701292187730> Bem-vindo ao meu servidor de suporte! Não se esqueça de ler as regras em <#917098963474198538> para evitar ser punido!\n\n<:892799472478871613:916846701292187730> Caso tenha alguma dúvida, estamos aqui para ajudar você! Entre em contato com a staff no canal <#981578389305565234>.\n\n<:892799472478871613:916846701292187730> Após a verificação, você irá receber o cargo <@&904874120011993118>.\n\n```Para se verificar, basta usar o comando /verificar.```", timestamp=datetime.datetime.utcnow(), color=0xfafafa)
        #embed.set_footer(icon_url=self.bot.user.avatar.url,text=f"LabyBot Support • {footer})
        #await channel.send(embed=embed)

    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam」Use esse comando para se verificar no meu servidor de suporte")
    @commands.guild_only()
    async def verificar(self, interaction: disnake.AppCommandInteraction):
        if disnake.utils.find(lambda r: r.id in [938805433701896212], interaction.author.roles):
            try:
                channel = self.bot.get_channel(938804946441228298)  
                channel2 = self.bot.get_channel(892820686828081153)
                member_role = disnake.utils.get(interaction.guild.roles, id=904874120011993118)
                member_role2 = disnake.utils.get(interaction.guild.roles, id=938805433701896212)
                member_role3 = disnake.utils.get(interaction.guild.roles, id=939301321687838790)
                membro = interaction.author.name
                novonick = membro + " ✦"
            
                await interaction.author.add_roles(member_role)
                await interaction.author.add_roles(member_role3)
                await interaction.author.remove_roles(member_role2)

                await interaction.response.send_message(f"Você foi verificado(a) com sucesso.", ephemeral=True) 
                await channel.send(f'O membro {interaction.author.mention} foi verificado(a) com sucesso!')
   
                WelcomeEmbed = disnake.Embed(title=f'{interaction.author.name} | Bem-vindo(a)!', description="Olá, seja bem-vindo(a) ao servidor de suporte do LabyBot!", color=white_color)
                WelcomeEmbed.set_thumbnail(url=interaction.author.avatar.url)
                WelcomeEmbed.add_field(name=f"{rules_emoji} | Leia as nossas diretrizes.", value="<#917098963474198538>")
                WelcomeEmbed.add_field(name=f"{folder_emoji} | Veja algumas informações do servidor.", value="<#1010331602330603540>", inline=False)
                WelcomeEmbed.add_field(name=f"{confirm_emoji} | Atualmente estamos com:", value=f'``{len(interaction.guild.members)}`` membros!')
                WelcomeEmbed.add_field(name=f"{interrogation_emoji} | Precisando de ajuda?", value='Caso você tenha alguma dúvida ou problema com o bot, marque ou chame no privado o <@901498839981236235>!', inline=False)
                WelcomeEmbed.set_footer(text=f"ID do usuário: {interaction.author.id} | ©️ Discord configurado por Flipz")
                
                await channel2.send(embed=WelcomeEmbed)
                await channel2.send(interaction.author.mention, delete_after=1)
                await interaction.author.edit(nick=novonick)

                Embed = disnake.Embed(title="Verificado(a) com sucesso!", description=f"Olá {interaction.author.mention}, você acaba de se verificar no meu servidor, caso queira mudar seu nick, use o comando ``/mudar_apelido`` no canal <#937083319819051088>. Espero que faça amigos e se divirta!\n\nAtenciosamente,\nLabyBot.", color=blurple_color)
                await interaction.author.send(embed=Embed)
            except:
                Embed = disnake.Embed(title="Verificado(a) com sucesso!", description=f"Olá {interaction.author.mention}, você acaba de se verificar no meu servidor, caso queira mudar seu nick, use o comando ``/mudar_apelido`` no canal <#937083319819051088>. Espero que faça amigos e se divirta!\n``Estou enviando essa mensagem aqui pois o seu privado está fechado.``\n\nAtenciosamente,\nLabyBot.", color=blurple_color)
                await interaction.response.send_message(embed=Embed, ephemeral=True)
        else:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas pessoas que **__NÃO__** são verificadas podem utilizar esse comando!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
            return
    
def setup(bot):
    bot.add_cog(Verificação(bot))