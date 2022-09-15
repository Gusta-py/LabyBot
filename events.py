from disnake.ext import commands, tasks
import sqlite3
import disnake
import random


class Eventos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        
    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect('eco.sqlite')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS eco (
            user_id INTERGER, carteira INTERGER, banco INTERGER
        )''')

        @tasks.loop(seconds=10)
        async def status():
            
            #servers = len(self.bot.guilds)
            members = 0
            for guild in self.bot.guilds:
                members += guild.member_count - 1

            poss = 1, 2, 3, 4, 5, 6

            esch = random.choice(poss)
            #before = time.monotonic()

            #ping = (time.monotonic() - before) * 1000
                
            if esch == 1:
                await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"{(members)} Amigos!"))
            elif esch == 2:
                await self.bot.change_presence(activity=disnake.Game(name=f"🛠️ | Conversando no suporte!"))
            elif esch == 3:
                await self.bot.change_presence(activity=disnake.Game(name="⚙ | Prefixo: /"))
            elif esch == 4:
                await self.bot.change_presence(activity=disnake.Game(name="❓ | /help "))
            elif esch == 5:
                await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"💻 | {len(self.bot.guilds)} Servidores!"))
            elif esch == 6:
                await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"💳 | Novo sistema de economia!"))
        status.start()
        print(f" - [APLICAÇÃO] Online com uma latência de {int(self.bot.latency * 1000)}ms.")

   
    #@commands.Cog.listener()
    #async def on_command_error(self, error, ctx, inter: disnake.ApplicationCommandInteraction):
        #if isinstance(error, commands.NoPrivateMessage):
            #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} Você só pode utilizar o comando ``{inter.data.name}`` em um servidor!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            #ErrorEmbed.set_footer(text=footer)
            #await ctx.author.send(embed=ErrorEmbed)
            #return

    #LabyTeam.py  

    #   @commands.Cog.listener()
    #async def on_member_join(self, member):
        #channel = self.bot.get_channel(892820686828081153)
        
        #if member.guild.id != 892799472478871613: return
        #if not member.bot:


            #WelcomeEmbed = discord.Embed(title=f'{member.name} | Bem vindo(a)!', color=0xfafafa)
            #WelcomeEmbed.set_thumbnail(url=member.avatar.url)
            #WelcomeEmbed.description = f'Olá, seja bem vindo(a) ao servidor de suporte do LabyBot!'
            #WelcomeEmbed.add_field(name="<:892799472478871613:916405308220399627> Leia as nossas diretrizes.", value="<#917098963474198538>")
            #WelcomeEmbed.add_field(name="<:892799472478871613:916842078024114186> Veja a introdução do servidor.", value="<#917096016501694504>", inline=False)
            #WelcomeEmbed.add_field(name=f"<:892799472478871613:916713061627351090> Atualmente estamos com", value=f'{len(member.guild.members)} membros!')
            #WelcomeEmbed.add_field(name="<:892799472478871613:916423317156671489> Precisando de ajuda?", value='Caso você tenha alguma dúvida ou problema com o bot, marque ou chame no privado o <@901498839981236235> ', inline=False)
            #WelcomeEmbed.set_footer(text=f"ID do usuário: {member.id} | ©️ Discord configurado por Flipz")
            
            #await channel.send(embed=WelcomeEmbed)

    #ILT:

    #@commands.Cog.listener()
    #async def on_message_delete(self, message):
        #if not message.guild: 
            #return
        #if message.guild.id!= 841374958365835325: 
           #return
        #cargo1 = discord.utils.get(message.guild.roles, name='・Comunidade')
        #cargo2 = discord.utils.get(message.guild.roles, name="🌐・PSG Member        ")
        #whitelist = ["・Ajudante", "・Moderador", "・Administrador", "・Gerente", "・Diretor", "・Fundador"]
        #tem = discord.utils.find(lambda r: r.name in whitelist, message.author.roles)   
        #if tem: return
        #if cargo1 in message.author.roles or cargo2 in message.author.roles: 
            #channel = self.bot.get_channel(918649586128666645)
            #embed = discord.Embed(title="Mensagem apagada!", description=f'Mensagem apagada por: {message.author.mention}. \n\nChat da mensagem: {message.channel.mention}', timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            #embed.set_thumbnail(url=message.author.avatar.url)
            #embed.add_field(name='Mensagem:', value=f'{message.content}')

            #await channel.send(embed=embed) 

    #@commands.Cog.listener()
    #async def on_message_edit(self, message_before, message_after):
        #if not message_before.guild: 
            #return
        #if message_before.guild.id != 841374958365835325: 
            #return
        #cargo1 = discord.utils.get(message_before.guild.roles, name='・Comunidade')
        #cargo2 = discord.utils.get(message_before.guild.roles, name="🌐・PSG Member")
        #whitelist = ["・Ajudante", "・Moderador", "・Administrador", "・Gerente", "・Diretor", "・Fundador"]
        #tem = discord.utils.find(lambda r: r.name in whitelist, message_before.author.roles)
        #if tem: return
        #if cargo1 in message_before.author.roles or cargo2 in message_before.author.roles: 
            #channel = self.bot.get_channel(918649586128666645)
            #embed = discord.Embed(title='Mensagem editada!', description=f'Mensagem editada por: {message_before.author.mention}.\n\nChat da mensagem: {message_before.channel.mention}.\n\nClique **[aqui](https://discord.com/channels/{message_before.guild.id}/{message_before.channel.id}/{message_before.id})** para ir para a mensagem.', timestamp=datetime.datetime.utcnow(), color=0xFFE800)
            #embed.set_thumbnail(url=message_before.author.avatar.url)
            #embed.add_field(name='Antes:', value=f'{message_before.content}', inline=False)
            #embed.add_field(name='Depois:', value=f'{message_after.content}', inline=False)
            
            #await channel.send(embed=embed)

    #@commands.Cog.listener()
    #async def on_message(self, mensagem):
        #if mensagem.guild is None:
            #return
        #if mensagem.guild.id != 841374958365835325: return

        #if mensagem.author.id == self.bot.user.id:
            #return
        #whitelist = ["・Ajudante", "・Moderador", "・Administrador","・Gerente", "・Diretor", "・Fundador"]
        #tem = discord.utils.find(lambda r: r.name in whitelist, mensagem.author.roles)   
        #if tem: return
        #whitelist2 = [884939347776897074, 878687372114554955, 929200890789892156, 879724094420025374, 841382393697009695, 894710555980464170]
        
        ##if mensagem.channel.id not in whitelist2:
            #conteudo = mensagem.content.lower()

            #links = ['www.youtube.com', 'https://youtu.be', 'www.instagram.com', 'www.twitch.tv']

            #if any(word in conteudo for word in links):
                #await mensagem.delete()
                #await mensagem.channel.send(f"{mensagem.author.mention}, Utilize o <#884939347776897074> para divulgar suas lives, vídeos ou redes sociais!")
                    
def setup(bot):
    bot.add_cog(Eventos(bot))