from Config.emojis import role_emoji, confirm_emoji, error_emoji, info_emoji, bug_emoji, key_emoji, warning_emoji, config_emoji
from Config.links import botadd_link, labysite_link, labyserver_link
from Config.colors import green_color, white_color, red_color
from disnake.ext import commands
from Config.bot import footer
from disnake import Option
import datetime
import disnake


class AN(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @disnake.ui.button(label="Aprovar", emoji=confirm_emoji, custom_id="confirm_button_three", style=disnake.ButtonStyle.green)
    async def confirm5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Bug aprovado!", ephemeral=True)
        self.value = True
        self.stop()

    @disnake.ui.button(label="Negar", emoji=error_emoji, custom_id="cancel_button_three", style=disnake.ButtonStyle.red)
    async def cancel5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = False
        self.stop()

class Resolved(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @disnake.ui.button(label="Resolvido", emoji=key_emoji, custom_id="resolved_button", style=disnake.ButtonStyle.blurple)
    async def confirm6(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

    @disnake.ui.button(label="Cancelar", emoji=error_emoji, custom_id="cancel_button_two", style=disnake.ButtonStyle.red)
    async def cancel6(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = False
        self.stop()

class Suporte(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="「⚙ Suporte」Mostra as novidades do bot")
    @commands.guild_only()
    async def novidades(self, ctx):

        view1 = disnake.ui.View()
        item = disnake.ui.Button(label="Me adicione!", style=disnake.ButtonStyle.blurple, url=botadd_link)
        view1.add_item(item=item)


        item2 = disnake.ui.Button(label="Meu servidor", style=disnake.ButtonStyle.green, url=labyserver_link)
        view1.add_item(item=item2)


        item3 = disnake.ui.Button(label="Meu website", style=disnake.ButtonStyle.grey, url=labysite_link)
        view1.add_item(item=item3)

        if ctx.guild.id == 892799472478871613:
            view1 = disnake.ui.View()
            item = disnake.ui.Button(label="Me adicione!", style=disnake.ButtonStyle.blurple, url=botadd_link)
            view1.add_item(item=item)

            item3 = disnake.ui.Button(label="Meu website", style=disnake.ButtonStyle.blurple, url=labysite_link)
            view1.add_item(item=item3)

        embed = disnake.Embed(title="Novidades do dia 14/09/2022",description=f'``Novidades do dia 14/09/2022``\n\n{config_emoji} | Um novo sistema de economia foi lançado em versão ``BETA``!\n\n**Caso encontre algum bug, por favor reportar usando o comando ``/bug``.**', timestamp=datetime.datetime.utcnow(), color=green_color)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, view=view1)

    @commands.slash_command(description="「⚙ Suporte」Dê uma sugestão para a nossa equipe de suporte", options=[Option('sugestão', 'Sua sugestão', required=True)])
    @commands.guild_only()
    async def sugestão(self, ctx, *, sugestão):
        channel = self.bot.get_channel(937060377185890334)

        embed1 = disnake.Embed(title="Nova sugestão!", description=f"Sugestão de **{ctx.author.mention}** do servidor **{ctx.guild.name}**", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed1.set_thumbnail(url=ctx.author.avatar.url)
        embed1.add_field(name="Sugestão:", value=f"{sugestão}", inline=False)
        embed1.set_footer(text=footer)
        await channel.send(embed=embed1)

        embed=disnake.Embed(title="Obrigado pela sugestão!", description=f"Agradecemos por enviar a sua sugestão **{ctx.author.mention}**.", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.set_thumbnail(url=f"{self.bot.user.avatar.url}")
        embed.add_field(name="Sugestão:", value=f"{sugestão}", inline=False)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, ephemeral=True)
        
    @commands.slash_command(description="「⚙ Suporte」Reporte um bug para a equipe de suporte", options=[Option('comando', 'Comando no qual ocorre o bug (sem espaços)', required=True), Option('bug', "Descreva como o bug ocorre:", required=True)])
    @commands.guild_only()
    async def bug(self, ctx, comando, *, bug):
        channel = self.bot.get_channel(916771430451015731)
        logchannel = self.bot.get_channel(999846918526095461)
        await ctx.send("Bug reportado com sucesso! Agradecemos por entrar em contato.", ephemeral=True)

        view = AN()
        view1 = Resolved()

        embed = disnake.Embed(title="Novo bug reportado!", description=f"Bug reportado por {ctx.author.mention} | ``{ctx.author.id}`` do servidor **{ctx.guild.name}**.", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.add_field(name=f"{info_emoji} | Informações do bug:\n{role_emoji} | Comando no qual o bug ocorre:", value=f"```{comando}```")
        embed.add_field(name=f"{bug_emoji} | Descrição do bug:", value=f"```{bug}```", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=footer)
        view.message = await channel.send(embed=embed, view=view)
        await view.wait()

        if view.value:
            embed = disnake.Embed(title="Report aprovado!", description=f"O bug reportado por {ctx.author.mention} | ``{ctx.author.id}`` do servidor **{ctx.guild.name}** foi aprovado com sucesso!", timestamp=datetime.datetime.utcnow(), color=white_color)
            embed.add_field(name=f"{info_emoji} | Informações do bug:\n{role_emoji} | Comando no qual o bug ocorre:", value=f"```{comando}```")
            embed.add_field(name=f"{bug_emoji} | Descrição do bug:", value=f"```{bug}```", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=footer)
            view1.message = await view.message.edit(embed=embed, view=view1)
            await view1.wait()
            if view1.value:
                await view.message.delete()
                embed = disnake.Embed(title="Report resolvido!", description=f"O bug reportado por {ctx.author.mention} | ``{ctx.author.id}`` do servidor **{ctx.guild.name}** foi resolvido com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.add_field(name=f"{info_emoji} | Informações do bug:\n{role_emoji} | Comando no qual ocorria o bug:", value=f"```{comando}```")
                embed.add_field(name=f"{bug_emoji} | Descrição do bug:", value=f"```{bug}```", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar.url)
                embed.set_footer(text=footer)
                await logchannel.send(embed=embed)
            else:
                await view1.message.delete()
        else:
            embed = disnake.Embed(title="Report negado!", description=f"O bug reportado por {ctx.author.mention} | ``{ctx.author.id}`` do servidor **{ctx.guild.name}** foi negado com sucesso!", timestamp=datetime.datetime.utcnow(), color=red_color)
            embed.add_field(name=f"{info_emoji} | Informações do bug:\n{role_emoji} | Comando no qual o bug ocorre:", value=f"```{comando}```")
            embed.add_field(name=f"{bug_emoji}> | Descrição do bug:", value=f"```{bug}```", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=footer)
            view1.message = await view.message.edit(embed=embed, view=None)
            await view1.wait()

    @commands.slash_command(description="「⚙ Suporte」Escreva o seu feedback para a equipe de suporte", options=[Option('feedback', 'Digite seu feedback', required=True)])
    @commands.guild_only()
    async def feedback(self, ctx, *, feedback):
        channel = self.bot.get_channel(937059682684657755)
        embed1 = disnake.Embed(title="Novo feedback!", description=f"Feedback por **{ctx.author.mention}** do servidor **{ctx.guild.name}**", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed1.set_thumbnail(url=f"{ctx.author.avatar.url}")
        embed1.add_field(name="Feedback:", value=f"{feedback}", inline=False)
        embed1.set_footer(text=footer)       
        await channel.send(embed=embed1)

        embed=disnake.Embed(title="Obrigado pelo feedback!", description=f"Agradecemos muito pelo feedback {ctx.author.mention}!", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.set_thumbnail(url=f"{self.bot.user.avatar.url}")
        embed.add_field(name="Feedback:", value=f"{feedback}", inline=False)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, ephemeral=True)
    
    @commands.slash_command(description="「⚙ Suporte」Me adicione ou atualize minhas permissões no seu servidor!")
    @commands.guild_only()
    async def add(self, ctx):

        view1 = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Me adicione!", url=botadd_link)
        view1.add_item(item=item)

        addEmbed = disnake.Embed(title="LabyBot", description="Clique no botão abaixo para me adicionar ou atualizar minhas permissões!", timestamp=datetime.datetime.utcnow(), color=white_color)
        addEmbed.set_footer(text=footer)
        await ctx.send(embed=addEmbed, view=view1)

    @commands.slash_command(description="「⚙ Suporte」Entre no meu servidor de suporte!")
    @commands.guild_only()
    async def servidor(self, ctx):

        view1 = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Servidor", url=labyserver_link)
        view1.add_item(item=item)

        ServerEmbed = disnake.Embed(title="LabyBot", description="Clique no botão abaixo para entrar no meu servidor de suporte!", timestamp=datetime.datetime.utcnow(), color=white_color)
        ServerEmbed.set_footer(text=footer)
        await ctx.send(embed=ServerEmbed, view=view1)
    
    #@commands.slash_command(guild_ids=[892799472478871613],description="「⚙ Suporte/LabyTeam」Reporte um membro do meu servidor de suporte", options=[Option('membro', 'Membro para ser reportado', OptionType.user, required=True), Option('motivo', 'Motivo para o membro ser reportado', required=True)])
    #@commands.guild_only()
    #async def reportar(self, ctx, motivo, membro):

        #view1 = disnake.ui.View()
        #item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Servidor", url=f"https://discord.gg/2GFXwgXT2e")
        #view1.add_item(item=item)

        #if disnake.utils.find(lambda r: r.id in [939301321687838790], ctx.author.roles):
            #channel = self.bot.get_channel(945754932487786497)
            #embed1 = disnake.Embed(title="Novo report!", description=f"O membro {membro.mention} foi reportado pelo {ctx.author.mention}!", timestamp=datetime.datetime.utcnow(), color=0xfafafa)
            #embed1.set_thumbnail(url=f"{ctx.author.avatar.url}")
            #embed1.add_field(name="Motivo:", value=f"**{motivo}**", inline=False)
            #embed1.set_footer(text=footer)       
            #await channel.send(embed=embed1)

            #embed = disnake.Embed(title="Obrigado pelo report!", description=f"Agradecemos muito pelo seu report do membro {membro.mention}, espero que ele seja punido!", timestamp=datetime.datetime.utcnow(), color=0xfafafa)
            #embed.set_thumbnail(url=f"{self.bot.user.avatar.url}")
            #embed.add_field(name="Motivo:", value=f"**{motivo}**", inline=False)
            #embed.set_footer(text=footer)
            #await ctx.send(embed=embed, ephemeral=True)
        
def setup(bot):
    bot.add_cog(Suporte(bot))