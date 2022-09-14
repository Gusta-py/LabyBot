from Config.emojis import error_emoji, interrogation_emoji, home_emoji, host_emoji, config1_emoji, added_emoji, paper_emoji, ping_emoji, rules_emoji
from Config.colors import white_color, red_color, yellow_color, blurple_color, grey_color, green_color, black_color, orange_color
from Config.links import labyserver_link, botadd_link
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class Dropdown(disnake.ui.Select):
    def __init__(self):

        options = [
            disnake.SelectOption(label="Menu Principal", description="Mostra o menu principal do painel", emoji=home_emoji),
            disnake.SelectOption(label="Ajuda ∫02∫", description="Mostra os comandos da categoria Ajuda", emoji=interrogation_emoji),
            disnake.SelectOption(label="Discord ∫13∫", description="Mostra os comandos da categoria Discord", emoji="📌"),
            disnake.SelectOption(label="Economia ∫09∫", description="Mostra os comandos da categoria Economia", emoji="💳"),
            disnake.SelectOption(label="Diversão ∫11∫", description="Mostra os comandos da categoria Diversão", emoji="😂"),
            disnake.SelectOption(label="Hospedagem ∫02∫", description="Mostra os comandos da categoria Hospedagem", emoji=host_emoji),
            disnake.SelectOption(label="Suporte ∫06∫", description="Mostra os comandos da categoria Suporte", emoji="⚙️"),
            disnake.SelectOption(label="Moderação ∫06∫", description="Mostra os comandos da categoria Moderação", emoji="🔧"),
            disnake.SelectOption(label="Útil ∫01∫", description="Mostra os comandos da categoria Útil", emoji="💡"),
            disnake.SelectOption(label="XP ∫02∫", description="Mostra os comandos da categoria XP", emoji="⚡")]

        super().__init__(
            placeholder="Escolha uma categoria",
            min_values=1,
            max_values=1,
            custom_id="select_teste_2",
            options=options,
        )
        
    async def callback(self, interaction: disnake.MessageInteraction):
        members = 0
        for guild in interaction.bot.guilds:
            members += guild.member_count - 1

        comandos = len(interaction.bot.global_slash_commands)

        menu = disnake.Embed(title="👋 | Olá!", description=f"Olá {interaction.author.mention}! Bem-vindo ao menu de ajuda do LabyBot! Um bot em beta para os servidores do Discord! Veja meu menu de comandos logo abaixo!", timestamp=datetime.datetime.utcnow(), color=white_color)
        menu.add_field(name=f'{config1_emoji} | Prefixo:', value="``/``")
        menu.add_field(name=f'{paper_emoji} | Comandos:', value=f'``{comandos}`` Comandos!', inline=False)
        menu.add_field(name=f"{interrogation_emoji} | Precisa de ajuda?", value=f"Não se preocupe! Basta entrar no meu servidor de suporte utilizando o comando ``/servidor`` ou clicando **[aqui]({labyserver_link})**.", inline=False)
        menu.add_field(name=f"{added_emoji} | Quer me adicionar?", value=f"Não tem problema! Basta utilizar o comando ``/add`` ou clicando **[aqui]({botadd_link})**!", inline=False)
        menu.set_thumbnail(url=interaction.bot.user.avatar.url)
        menu.set_footer(text=footer)

        ajuda = disnake.Embed(title="Comandos da categoria Ajuda", description=f"||{interaction.author.mention}||\n\n``/comandos`` - Mostra todos os comandos disponíveis\n``/help`` - Recebe a mensagem de ajuda do LabyBot", timestamp=datetime.datetime.utcnow(), color=green_color)
        ajuda.set_thumbnail(url=interaction.bot.user.avatar.url)
        ajuda.set_footer(text=footer)

        discord = disnake.Embed(title="Comandos da categoria Discord", description=f"||{interaction.author.mention}||\n\n``/avatar`` - Mostra o avatar de um usuário\n``/botinfo`` - Mostra algumas informações sobre o bot\n``/criar_cargo`` - Permite que você crie um cargo por comando\n``/deletar_cargo`` - Permite que você delete um cargo por comando\n``/emoji_info`` - Mostra as informações de um emoji personalizado\n``/valeu`` - Agradeça algum usuário por ter te ajudado no servidor!\n``/reps`` - Mostra a quantidade de reps que um usuário tem\n``/servericon`` - Mostra a logo do servidor atual\n``/ping`` - Mostra a latência do LabyBot e da API\n``/role_info`` - Mostra as informações de um cargo\n``/serverinfo`` - Mostra as informações do servidor atual\n``/spotify`` - Veja o que um usuário está escutando no spotify!\n``/userinfo`` - Mostra as informações de um usuário", timestamp=datetime.datetime.utcnow(), color=blurple_color)
        discord.set_thumbnail(url=interaction.bot.user.avatar.url)
        discord.set_footer(text=footer)

        economia = disnake.Embed(title="Comandos da categoria Economia", description=f"||{interaction.author.mention}||\n\n``/abrir_conta`` - Abra sua conta bancária e inicie sua jornada no mundo econômico!\n``/apostar`` - Faça uma aposta com outro usuário!\n``/daily`` - Colete seu prêmio diário e ganhe LabyCoins!\n``/deletar_conta`` - Delete sua conta bancária!\n``/depositar`` - Deposite uma quantia de dinheiro na sua conta bancária\n``/sacar`` - Saque uma quantia de dinheiro da sua conta bancária!\n``/saldo`` - Mostra a sua conta bancária ou a de outro usuário \n``/pix`` - Faça um pix para um usuário!\n``/trabalhar`` - Trabalhe para ganhar dinheiro!", timestamp=datetime.datetime.utcnow(), color=orange_color)
        economia.set_thumbnail(url=interaction.bot.user.avatar.url)
        economia.set_footer(text=footer)

        diversão = disnake.Embed(title="Comandos da categoria Diversão", description=f"||{interaction.author.mention}||\n\n``/cancelar`` - Cancele um meliante por menção!\n``/coinflip`` - Cara ou coroa?\n``/bola_de_cristal`` - Faça uma pergunta para a bola de cristal\n``/clima`` - Veja a previsão do tempo de uma cidade por comando!\n``/dado`` - Role um dado!\n``/jokenpo`` - Jogue pedra, papel e tesoura comigo!\n``/reverso`` - Tudo que você escrever, eu deixo oa oirártnoc!\n``/say`` - Faça eu falar algo!\n``/ship`` - Shipe uma pessoa com outra pessoa, pera, quê?\n``/termo`` - Jogue Termo, só que no Discord 😈", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        diversão.set_thumbnail(url=interaction.bot.user.avatar.url)
        diversão.set_footer(text=footer)

        host = disnake.Embed(title="Comandos da categoria Hospedagem", description=f"||{interaction.author.mention}||\n\n``/discloud`` - Seu bot 24h online agora!\n``/status`` - Veja os status e algumas informações do bot", timestamp=datetime.datetime.utcnow(), color=blurple_color)
        host.set_thumbnail(url=interaction.bot.user.avatar.url)
        host.set_footer(text=footer)

        suporte = disnake.Embed(title="Comandos da categoria Suporte", description=f"||{interaction.author.mention}||\n\n``/add`` - Me adicione ou atualize minhas permissões no seu servidor!\n``/bug`` - Reporte um bug para a equipe de suporte\n``/feedback`` - Diga seu feedback para a equipe de suporte\n``/novidades`` - Mostra as novidades do bot\n``/servidor`` - Entre no meu servidor de suporte!\n``/sugestão`` - Dê uma sugestão para a nossa equipe de suporte", timestamp=datetime.datetime.utcnow(), color=grey_color)
        suporte.set_thumbnail(url=interaction.bot.user.avatar.url)
        suporte.set_footer(text=footer)

        moderação = disnake.Embed(title="Comandos da categoria Moderação", description=f"||{interaction.author.mention}||\n\n``/add_cargo`` - Adicione um cargo em um membro por comando!\n``/ban`` - Bane uma pessoa do servidor\n``/changenick`` - Troca o nick de um membro do seu servidor\n``/clear`` - Limpe uma certa quantia de mensagens\n``/kick`` - Expulsa um membro do servidor\n``/remover_cargo`` - Remova um cargo de um membro por comando!\n``/unban`` - Desbane um usuário que estava no seu servidor", timestamp=datetime.datetime.utcnow(), color=red_color)
        moderação.set_thumbnail(url=interaction.bot.user.avatar.url)
        suporte.set_footer(text=footer)

        útil = disnake.Embed(title="Comandos da categoria Útil", description=f"||{interaction.author.mention}||\n\n``/lembrete`` - Crie um lembrete!", timestamp=datetime.datetime.utcnow(), color=white_color)
        útil.set_thumbnail(url=interaction.bot.user.avatar.url)
        útil.set_footer(text=footer)

        xp = disnake.Embed(title="Comandos da categoria XP", description=f"||{interaction.author.mention}||\n\n``/rank`` - Mostra o placar de XP do servidor\n``/xp`` - Mostra o seu xp e progresso", timestamp=datetime.datetime.utcnow(), color=black_color)
        xp.set_thumbnail(url=interaction.bot.user.avatar.url)
        xp.set_footer(text=footer)

        if self.values[0] == "Menu Principal":
            await interaction.response.edit_message(embed=menu)
        if self.values[0] == "Ajuda ∫02∫":
            await interaction.response.edit_message(embed=ajuda)
        if self.values[0] == "Discord ∫13∫":
            await interaction.response.edit_message(embed=discord)
        if self.values[0] == "Economia ∫09∫":
            await interaction.response.edit_message(embed=economia)
        if self.values[0] == "Diversão ∫11∫":
            await interaction.response.edit_message(embed=diversão)
        if self.values[0] == "Hospedagem ∫02∫":
            await interaction.response.edit_message(embed=host)
        if self.values[0] == "Suporte ∫06∫":
            await interaction.response.edit_message(embed=suporte)
        if self.values[0] == "Moderação ∫06∫":
            await interaction.response.edit_message(embed=moderação)
        if self.values[0] == "Útil ∫01∫":
            await interaction.response.edit_message(embed=útil)
        if self.values[0] == "XP ∫02∫":
            await interaction.response.edit_message(embed=xp)

class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

    async def interaction_check(self, interaction: disnake.Interaction):
        if interaction.author.mention not in interaction.message.embeds[0].description:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode utilizar esse painel de comandos! Caso queira ver todos os meus comandos, use ``/comandos``.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
        else:
            return True

class Ajuda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.prepare_view())

    async def prepare_view(self):
        await self.bot.wait_until_ready()
        self.bot.add_view(DropdownView())

    @commands.slash_command(description='「🛠 Ajuda」Recebe a mensagem de ajuda do LabyBot')
    @commands.guild_only()
    async def help(self, ctx):
        
        view1 = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Servidor de suporte", url=labyserver_link)
        view1.add_item(item=item)

        if ctx.guild.id == 892799472478871613:
            helpEmbed = disnake.Embed(title='Ajuda do LabyBot', description=f'Olá {ctx.author.mention}! Bem-vindo ao menu de ajuda do LabyBot! Um bot em beta para os servidores do Discord! Veja logo abaixo como me usar!', timestamp=datetime.datetime.utcnow(), color=white_color)
            helpEmbed.set_thumbnail(url=self.bot.user.avatar.url)
            helpEmbed.add_field(name=f'{ping_emoji} | Minha latência:', value=f'``{round(self.bot.latency * 1000)}``')
            helpEmbed.add_field(name=f'{rules_emoji} | Use para ver meus comandos disponíveis:', value='``/comandos``', inline=False)
            helpEmbed.set_footer(text=footer)
            await ctx.send(embed=helpEmbed)
        else:
            helpEmbed = disnake.Embed(title='Ajuda do LabyBot', description='Bem-vindo ao menu de ajuda do LabyBot, um bot em beta para o discord! Veja logo abaixo como me usar:', timestamp=datetime.datetime.utcnow(), color=white_color)
            helpEmbed.set_thumbnail(url=self.bot.user.avatar.url)
            helpEmbed.add_field(name=f'{ping_emoji} | Minha latência:', value=f'``{round(self.bot.latency * 1000)}``')
            helpEmbed.add_field(name=f'{rules_emoji} | Use para ver meus comandos disponíveis:', value='``/comandos``', inline=False)
            helpEmbed.set_footer(text=footer)
            await ctx.send(embed=helpEmbed, view=view1)
            
    @commands.slash_command(description="「🛠 Ajuda」Mostra todos os comandos disponíveis")
    @commands.guild_only()
    async def comandos(self, ctx):    
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        comandos = len(self.bot.global_slash_commands)

        view = DropdownView()

        menu = disnake.Embed(title="👋 | Olá!", description=f"Olá {ctx.author.mention}! Bem-vindo ao menu de ajuda do LabyBot! Um bot em beta para os servidores do Discord! Veja meu menu de comandos logo abaixo!", timestamp=datetime.datetime.utcnow(), color=white_color)
        menu.add_field(name=f'{config1_emoji} | Prefixo:', value="``/``")
        menu.add_field(name=f'{paper_emoji} | Comandos:', value=f'``{comandos}`` Comandos!', inline=False)
        menu.add_field(name=f"{interrogation_emoji} | Precisa de ajuda?", value=f"Não se preocupe! Basta entrar no meu servidor de suporte utilizando o comando ``/servidor`` ou clicando **[aqui]({labyserver_link})**.", inline=False)
        menu.add_field(name=f"{added_emoji} | Quer me adicionar?", value=f"Não tem problema! Basta utilizar o comando ``/add`` ou clicando **[aqui]({botadd_link})**!", inline=False)
        #menu.set_thumbnail(url=self.bot.user.avatar.url)
        menu.set_footer(text=footer)

        await ctx.send(embed=menu, view=view)
        
def setup(bot):
    bot.add_cog(Ajuda(bot))