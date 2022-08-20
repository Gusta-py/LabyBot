from Config.emojis import confirm_emoji, error_emoji, trash_emoji, lamp_emoji
from Config.colors import yellow_color, red_color, green_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class Confirmar2(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="Aprovar", emoji=confirm_emoji, custom_id="confirm_button", style=disnake.ButtonStyle.green)
    async def confirm1(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

    @disnake.ui.button(label="Negar", emoji=error_emoji, custom_id="cancel_button", style=disnake.ButtonStyle.red)
    async def cancel1(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = False
        self.stop()

class ApagarAprovado(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value = None

    @disnake.ui.button(label="Apagar mensagem", emoji=trash_emoji, custom_id="delete_aproved_button", style=disnake.ButtonStyle.green)
    async def delete1(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

class ApagarAnalise(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value = None

    @disnake.ui.button(label="Apagar mensagem", emoji=trash_emoji, custom_id="delete_analised_button", style=disnake.ButtonStyle.grey)
    async def delete2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.delete_original_message()
        self.stop()

class ApagarNegado(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value = None

    @disnake.ui.button(label="Apagar mensagem", emoji=trash_emoji, custom_id="delete_recused_button", style=disnake.ButtonStyle.red)
    async def delete3(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

class Sugestões(commands.Cog):
   
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild: 
            return
        if message.channel.id == 993913747485761566: 
            canal = self.bot.get_channel(994666954243723324)
            canal2 = self.bot.get_channel(993913747485761566)
            if message.author.id == 908870304909115432:
                return
            else:
                await message.delete()
            try: 
                
                view = Confirmar2()
                view1 = ApagarAnalise()
                view2 = ApagarAprovado()
                view3 = ApagarNegado()

                AnaliseEmbed = disnake.Embed(title=f"{confirm_emoji} | Sugestão enviada para análise!", description=f"Olá {message.author.mention}! Só vim aqui dizer que sua sugestão foi enviada para análise! Caso ela não apareça no canal novamente, ela foi recusada.\n\nSugestão:\n```{message.content}```", timestamp=datetime.datetime.utcnow(), color=yellow_color)
                AnaliseEmbed.set_thumbnail(url=message.author.avatar.url)
                AnaliseEmbed.set_footer(text=footer)
                view1.message = await message.author.send(embed=AnaliseEmbed, view=view1)
            
                if view1.value:
                    await view1.message.delete()
                    
            except:
                return

            embed1 = disnake.Embed(title=f"{lamp_emoji} | Nova sugestão!", description=f"O membro {message.author.mention} enviou uma sugestão!\n\n```{message.content}```\n\n・Para votar aprovar a sugestão, clique em ``Aprovar``.\n・Para recusar a sugestão, clique em ``Recusar``.", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            embed1.set_thumbnail(url=message.author.avatar.url)
            embed1.set_footer(text=footer)

            view.message = await canal.send(embed=embed1, view=view)
            await view.wait()
           
            if view.value:
                embed = disnake.Embed(title=f"{confirm_emoji} | Sugestão aprovada!", description=f"A sugestão de {message.author.mention} foi aprovada!\n\nSugestão:\n```{message.content}```", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.set_thumbnail(url=message.author.avatar.url)
                embed.set_footer(text=footer)
                await view.message.edit(embed=embed, view=None)

                channelEmbed = disnake.Embed(title=f"{confirm_emoji} | Nova sugestão!", description=f"O membro {message.author.mention} enviou uma sugestão!\n\n```{message.content}```\n\n・Para votar a favor da sugestão, clique na reação <:892799472478871613:916835300100153365>.\n・Para votar contra a sugestão, clique na reação <:892799472478871613:916835300318253097>.", timestamp=datetime.datetime.utcnow(), color=green_color)
                channelEmbed.set_thumbnail(url=message.author.avatar.url)
                channelEmbed.set_footer(text=footer)
                msg = await canal2.send(embed=channelEmbed)

                
                await msg.add_reaction("<:892799472478871613:916835300100153365>")
                await msg.add_reaction("<:892799472478871613:916835300318253097>")


                AprovedEmbed = disnake.Embed(title=f"{confirm_emoji} | Sugestão aprovada!", description=f"Olá {message.author.mention}! Só vim aqui dizer que sua sugestão foi aprovada com sucesso!\n\nSugestão:\n```{message.content}```", timestamp=datetime.datetime.utcnow(), color=green_color)
                AprovedEmbed.set_thumbnail(url=message.author.avatar.url)
                AprovedEmbed.set_footer(text=footer)
                view2.message = await message.author.send(embed=AprovedEmbed, view=view2)
                await view2.wait()

                if view2.value:
                    await view2.message.delete()

            else:
                embed = disnake.Embed(title=f"{confirm_emoji} | Sugestão negada!", description=f"A sugestão de {message.author.mention} foi recusada!\n\nSugestão:\n```{message.content}```", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_thumbnail(url=message.author.avatar.url)
                embed.set_footer(text=footer)
                await view.message.edit(embed=embed, view=None)

                RecusedEmbed = disnake.Embed(title=f"{confirm_emoji} | Sugestão negada!", description=f"Olá {message.author.mention}! Só vim aqui dizer que sua sugestão infelizmente foi negada. Mas não se preocupe! Você pode mandar outra sugestão a qualquer momento!\n\nSugestão:\n```{message.content}```", timestamp=datetime.datetime.utcnow(), color=red_color)
                RecusedEmbed.set_thumbnail(url=message.author.avatar.url)
                RecusedEmbed.set_footer(text=footer)
                view3.message = await message.author.send(embed=RecusedEmbed, view=view3)
                await view3.wait()

                if view3.value:
                    await view3.message.delete()
       
def setup(bot):
    bot.add_cog(Sugestões(bot))