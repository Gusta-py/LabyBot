from Config.emojis import warning_emoji, interrogation_emoji, chat_emoji, partner_emoji, added_emoji, removed_emoji
from Config.colors import green_color
from disnake.ext import commands
import disnake


class DD(disnake.ui.Select):
    def __init__(self):
        options = [
        disnake.SelectOption(label="Fazer uma denúncia", emoji="🚨"),
        disnake.SelectOption(label="Fazer parceria", emoji=partner_emoji),
        disnake.SelectOption(label="Tirar dúvidas", emoji=chat_emoji),
        disnake.SelectOption(label="Outro", emoji=interrogation_emoji),
        ]

        super().__init__(
            placeholder="Escolha uma categoria",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="dropdown_help"
        )

    async def callback(self, interaction: disnake.Interaction):
        if self.values[0] == "Fazer uma denúncia":
            await interaction.response.send_message(f"{warning_emoji}> **|** Para fazer uma denúncia, vamos precisar do **motivo da denúncia, autores do ocorrido e provas.** Não crie um ticket de denúncia apenas para testar a ferramenta ou para tirar dúvidas (existem outros espaços para isso!).\n\nSe quiser prosseguir com sua denúncia, crie um ticket abaixo.", ephemeral=True, view=Ticket(bot="bot"))
        if self.values[0] == "Fazer parceria":
            await interaction.response.send_message(f"{warning_emoji} **|** Para divulgar seu servidor, ele precisa seguir todos os requisitos que estão no <#942525315782168636> e depois basta você clicar no botão abaixo para abrir um ticket!", ephemeral=True, view=Ticket(bot="bot"))
        if self.values[0] == "Tirar dúvidas":
            await interaction.response.send_message(f"{warning_emoji} **|** Tem dúvidas sobre o servidor ou o bot? Não se preoucupe! Basta criar um ticket logo baixo!", ephemeral=True, view=Ticket(bot="bot"))
        if self.values[0] == "Outro":
            await interaction.response.send_message(f"{warning_emoji} **|** Se seu problema ou dúvida não pode ser resolvido no chat <#926991761522458624>, fale com um atendente sobre sua questão criando um ticket abaixo.", ephemeral=True, view=Ticket(bot="bot"))


class DDV(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(DD())


class Ticket0(disnake.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        self.value = None

    @disnake.ui.button(label="Fechar ticket", style=disnake.ButtonStyle.red, emoji=removed_emoji)
    async def close(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        membro = interaction.author
        guild = interaction.author.guild
        category = disnake.utils.get(guild.categories, id=942515479547895858)

        
        overwrite = {
                guild.default_role: disnake.PermissionOverwrite(read_messages=False),
                guild.me: disnake.PermissionOverwrite(read_messages=False, create_public_threads=False, create_private_threads=False),
                membro: disnake.PermissionOverwrite(read_messages=False, send_messages=True, attach_files=True, use_slash_commands=False, create_public_threads=False),
                ** {guild.get_role(r_id): disnake.PermissionOverwrite(read_messages=False, send_messages=True, attach_files=True, create_public_threads=False)
                for r_id in [937052521699106847, 937052508017295430, 937052490237607996]}
                
            }

        await interaction.channel.edit(name=f'🚨・arquivado-{interaction.author}', category=category, overwrites=overwrite)
        embed = disnake.Embed(description=f"📩 | Atendimento encerrado! O ticket foi arquivado por {interaction.author.mention}.", color=green_color)
        await interaction.response.send_message(embed=embed)
        

class Ticket(disnake.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=300)
        self.bot = bot
        self.value = None
    

    @disnake.ui.button(label="Abrir ticket", style=disnake.ButtonStyle.green, emoji=added_emoji)
    async def open(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.stop()
        
        guild = interaction.author.guild
        membro = interaction.author
        category = disnake.utils.get(guild.categories, id=920120762730422394)

        view1 = Ticket0(self.bot)
    
        overwrite = {
                guild.default_role: disnake.PermissionOverwrite(read_messages=False),
                guild.me: disnake.PermissionOverwrite(read_messages=True, create_public_threads=False, create_private_threads=False),
                membro: disnake.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True, use_slash_commands=False, create_public_threads=False),
                ** {guild.get_role(r_id): disnake.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True, create_public_threads=False)
                for r_id in [937052521699106847, 937052508017295430, 937052490237607996]}
                
            }
        
        channel = await guild.create_text_channel(name=f'🚨・suporte-{interaction.author}', topic=interaction.author.mention, category=category, overwrites=overwrite)
        
        view = disnake.ui.View()
        item = disnake.ui.Button(label="Atalho para o canal", style=disnake.ButtonStyle.blurple, url=channel.jump_url)
        view.add_item(item=item)

        embed = disnake.Embed(description=f"📩 | {interaction.author.mention} ticket criado! Envie todas as informações possíveis sobre o seu caso e aguarde até que um membro da equipe de suporte responda.\n\nApós sua questão ser sanada, você pode clicar no cadeado abaixo para finalizar o atendimento.", color=green_color)
        await interaction.response.send_message(content=f"Criei um ticket para você!", view=view, ephemeral=True)
        await channel.send(content=f"{interaction.author.mention} | <@&937052521699106847>", embed=embed, view=view1)


class TicketsLBT(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.prepare_view())

    async def prepare_view(self):
        await self.bot.wait_until_ready()
        self.bot.add_view(DDV())

def setup(bot):
    bot.add_cog(TicketsLBT(bot))