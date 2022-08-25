from Config.emojis import link_emoji, userinfo_emoji, owner_emoji, bot_emoji, info_emoji, maping_emoji, vscode_emoji, paper_emoji, python_emoji, clock_emoji, monitor_emoji, netlify_emoji, rules_emoji, discloud_emoji, partner_emoji
from Config.colors import white_color, green_color, blurple_color, red_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class Dono(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    async def notifications_embed(self, ctx):
        channel = self.bot.get_channel(917417508955390052)

        comp = [
            disnake.ui.Button(label="Atualizações", emoji="📰", custom_id="updates_button"),
            disnake.ui.Button(label="Parcerias", emoji=partner_emoji, custom_id="partners_button"),
            disnake.ui.Button(label="Status", emoji="🚧", custom_id="status_button")
        ]

        embed4 = disnake.Embed(title="Pegue abaixo os cargos que deseja receber notificações.", description="📰 Atualizações • <@&917419484388659201>.\n\n<:892799472478871613:939137623526617129> Parcerias • <@&917419484388659201>.\n\n🚧 Status • <@&917419485831507989>.", color=white_color)  
        await channel.send(embed=embed4, components=comp)
    
    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    async def roles_embed(self, ctx):
        channel = self.bot.get_channel(927669655907237930)

        embed = disnake.Embed(title="Pegue cargos extras nesse canal!", description="Clique no botão abaixo para ver a lista de cargos que você pode obter.", color=white_color)
        await channel.send(embed=embed, components=[disnake.ui.Button(label="Clique aqui", custom_id="click_here_button", style=disnake.ButtonStyle.green)])
        
    @commands.slash_command(guild_ids=[892799472478871613], description="「👑 Dono」Veja a lista dos servidores que eu estou")
    @commands.guild_only()
    @commands.is_owner()
    async def serverlist(self, ctx):
        x = '\n'.join([str(server) for server in self.bot.guilds])
        y = len(self.bot.guilds)
        if y < 30:
            embed = disnake.Embed(title="Estou atualmente em " + str(y) + " servidores! Servidores que eu estou:", description="```json\n" + x  + "```", color=white_color)
            return await ctx.send(embed=embed) 

    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    @commands.is_owner()
    async def infos(self, ctx):
        epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
        tempo = (ctx.me.created_at.replace(tzinfo=None).astimezone(datetime.timezone.utc)-epoch).total_seconds()
        channel = self.bot.get_channel(1010331602330603540)

        embed4 = disnake.Embed(title="💼・INFO - CARGOS", color=white_color)
        embed4.add_field(name="ㅤㅤㅤㅤㅤㅤㅤINFO DE TODOS OS CARGOSㅤㅤㅤㅤㅤㅤㅤㅤㅤ", value="<@&939141878689984566>・Cargo dado a um membro que é parceiro do nosso servidor.\n<@&904874120011993118>・Cargo padrão do servidor, dado depois de se verificar.\n<@&939301321687838790>・Membro verificado no servidor, dado depois de se verificar.\n<@&938805433701896212>・Membro que está no servidor, mas não está verificado.\n<@&928678002827599892>・Cargo dedicado aos bots que estão no servidor.")
        embed4.set_footer(text=f"Informações atualizadas do dia 13/04/2022 às 20:07. • Parte 2/2 ")
        embed4.set_thumbnail(url=ctx.guild.icon.url)

        embed3 = disnake.Embed(title="💼・INFO - CARGOS", color=white_color)
        embed3.add_field(name="ㅤㅤㅤㅤㅤㅤㅤINFO DE TODOS OS CARGOSㅤㅤㅤㅤㅤㅤㅤㅤㅤ", value="<@&892802037186711553>・É o dono do servidor, **NINGUÉM** pode obter esse cargo, ao menos que o próprio dono coloque esse cargo em alguém.\n<@&937052487427440760>・Membro da staff que gerencia o servidor, os membros, o bot e etc.\n<@&937052490237607996>・Tag dada ao membro da staff que já progrediu bem e está apenas ajudando, observando e dando experiência a todos os membros e staffs.\n<@&937052508017295430>・Membro que está apenas observando, organizando e dando experiência aos novos membros.\n<@&937052521699106847>・Membro da staff que vai responder tickets, tirar dúvidas, ajudar os membros e etc.\n<@&936738889744416798>・Cargo dado a uma pessoa que ajuda e testa o LabyBot, com sugestões boas, testando comandos e códigos.\n<@&949792715548287087>・Cargo dado a uma pessoa que impulsionou o servidor.\n<@&916716666879098901>・Cargo dado a um membro que manda ótimas sugestões, reporta bastante bugs e ajuda em questão de códigos e ideias.")
        embed3.set_footer(text=f"Informações atualizadas do dia 05/04/2022 às 16:10. • Parte 1/2 ")
        embed3.set_thumbnail(url=ctx.guild.icon.url)
                
        embed1 = disnake.Embed(title='Olá eu sou o LabyBot!', color=white_color, description=f'Olá! me chamo LabyBot, mas pode me chamar de Laby! Sou um bot simples e em beta para o discord! Veja abaixo minhas informações atualizadas!')
        embed1.set_thumbnail(url=self.bot.user.avatar.url)
        embed1.add_field(name=f'{vscode_emoji} | Programado em: ', value='``Visual Studio Code (Python)``')
        embed1.add_field(name=f'{python_emoji} | Python:', value=f'``3.10.6``', inline=False)
        embed1.add_field(name=f'{paper_emoji} | Comandos:', value=f'``50+``', inline=False)
        embed1.add_field(name=f"{maping_emoji} | Minha data de nascimento:", value=f"<t:{int(tempo)}:F> | <t:{int(tempo)}:R>")
        embed1.add_field(name=f'{owner_emoji} | Criado por: ', value='<@901498839981236235>', inline=False)

        embed2 = disnake.Embed(title=f"{userinfo_emoji} __Informações principais__", description="Aqui estão algumas informações e links dos quais você pode estar procurando. Fique à vontade para usar e enviar para aqueles amigos!", color=white_color)
        embed2.add_field(name=f"{bot_emoji} | Bot:\n\n{discloud_emoji} | Hospedado em:", value="``Discloud``")
        embed2.add_field(name=f"{info_emoji} | Versão:", value="``v2``", inline=False)
        embed2.add_field(name=f"{clock_emoji} | Desde:", value="<t:1640325060:F> | <t:1640325060:R>\n\n", inline=False)
        embed2.add_field(name=f"\n{monitor_emoji} | Website:\n\n{netlify_emoji} | Hospedado em:", value="``Netlify``")
        embed2.add_field(name=f"{link_emoji} | Link:", value="**[Website](https://labybot.netlify.app/)**.", inline=False)
        embed2.set_thumbnail(url=self.bot.user.avatar.url)
        embed2.add_field(name=f"{clock_emoji} | Desde:", value="<t:1647899040:F> | <t:1647899040:R>", inline=False)
                
        embed5 = disnake.Embed(title="💻・INFO - CANAIS", color=white_color)
        embed5.set_thumbnail(url="")
        embed5.add_field(name="Algumas informações úteis:", value=' ・Fique por dentro de todas as <#917098963474198538>.\n・Veja o status do LabyBot em <#917101161310478366>.\n・Para ficar atento as novidades e outros assuntos acesse o <#917100196578598943>.\n・Converse a vontade no <#926991761522458624>, assim como nos canais de voz.\n・Veja as atualizações do LabyBot e do servidor em <#917099856613486642>.\n・Ganhe cargos de notificações em <#917417508955390052> e cargos extras no <#927669655907237930>.\n\n Para qualquer dúvida, a equipe de colaboradores e superiores estará ao seu dispor!')
        await channel.send(embed=embed1)
        await channel.send(embeds=[embed2, embed3, embed4, embed5])

    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    @commands.is_owner()
    async def up(self, ctx):
        
        channel = self.bot.get_channel(1010331602330603540)
        view = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.green, label="Clique aqui para subir ao topo do canal!", url=f"https://discord.com/channels/892799472478871613/1010331602330603540/1010682254655246446")
        view.add_item(item=item)

        await channel.send("Veja algumas informações nesse canal!", view=view) 

    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    @commands.is_owner()
    async def welcome_embed(self, ctx):
        channel = self.bot.get_channel(917096016501694504)
        embed = disnake.Embed(title="Embed enviada!", description=f"A embed foi enviada com sucesso para o canal <#917096016501694504>!", timestamp=datetime.datetime.utcnow(), color=green_color)
        await ctx.send(embed=embed)
        embed1 = disnake.Embed(title="👋 Bem-vindo(a) ao servidor de suporte do LabyBot.", description="Olá! Seja muito bem-vindo(a) <:892799472478871613:916778384959365140>\nNós da equipe de suporte do LabyBot estamos muito felizes em o(a) ter aqui com a gente.", color=white_color)
        embed1.add_field(name="Algumas informações úteis:", value=' ・Fique por dentro de todas as <#917098963474198538>.\n・Veja o status do LabyBot em <#917101161310478366>.\n・Para ficar atento as novidades e outros assuntos acesse o <#917100196578598943>.\n・Converse a vontade no <#926991761522458624>, assim como nos canais de voz.\n・Veja as atualizações do LabyBot e do servidor em <#917099856613486642>.\n・Ganhe cargos de notificações em <#917417508955390052> e cargos extras no <#927669655907237930>.\n\n Para qualquer dúvida, a equipe de colaboradores e superiores estará ao seu dispor!')
        await channel.send(embed=embed1)
        
            
    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    @commands.is_owner()
    async def rules_embed(self, ctx):
        channel = self.bot.get_channel(917098963474198538)
        embed = disnake.Embed(title="Embed enviada!", description=f"A embed foi enviada com sucesso para o canal <#917098963474198538>!", timestamp=datetime.datetime.utcnow(), color=green_color)
        await ctx.send(embed=embed)
        embed2 = disnake.Embed(title=f"{rules_emoji} REGRAS", description="‧ 1 - **REGRAS DE CHAT**\n\n‧ 1.1 - Não será tolerado membros xingando um ao outro, e inclusive membros tóxicos;\n\n‧ 1.2 - Não será tolerada nenhuma forma de preconceito;\n\n‧ 1.3 - Não marque excessivamente os membros;\n\n‧ 1.4 - Não polua nenhum chat com Flood, Spam ou qualquer tipo de mensagem desnecessária ou longa demais;\n\n‧ 1.5 - Sem discussões no chat geral, seja qual for o motivo;\n\n‧ 1.6 - Esta terminantemente proibido qualquer forma de ofensa e descriminação;\n\n‧ 1.7 - Proibido divulgar fotos ou conteúdos privados de outros membros sem autorização prévia do mesmo\n\n‧ 2 - **CONTEÚDOS INADEQUADOS:**\n\n‧ 2.1 - Está proibido conteúdo **NSFW** - **Not Safe To Work** (inclui qualquer tipo de conteúdo inapropriado, como gore, pornografia, apologias, etc); [BAN IMEDIATO E PERMANENTE]\n\n‧ 2.2 - Sem discussões sobre política, gênero, e qualquer outro assunto polêmico ou que possa gerar conflitos;\n\n‧ 2.3 - Não faça nenhum pedido ou peça ajuda para algo ilegal [BAN IMEDIATO E PERMANENTE];\n\n‧ 2.4 - Proibido a divulgação de sites com conteúdo +18. [BAN IMEDIATO E PERMANENTE].", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed2.set_footer(text="LabyTeam Terms.")
        await channel.send(embed=embed2)
    
    @commands.slash_command(guild_ids=[892799472478871613], description="「🧪 LabyTeam/👑 Dono」???")
    @commands.guild_only()
    @commands.is_owner()
    async def rules2_embed(self, ctx):
        channel = self.bot.get_channel(917098963474198538)
        embed = disnake.Embed(title="Embed enviada!", description=f"A embed foi enviada com sucesso para o canal <#917098963474198538>!", timestamp=datetime.datetime.utcnow(), color=green_color)
        await ctx.send(embed=embed)
        embed2 = disnake.Embed(description="‧ 3 - **DIVULGAÇÕES E DISCUSSÕES PARALELAS:**\n\n‧ 3.1 - Proibido divulgações terceirizadas e sites que possam prejudicar outros usuários;\n\n‧ 3.4 - Não divulgue nenhum tipo de conteúdo ofensivo, comunidades, servidores e bots do discord na DM dos membros. [BAN IMEDIATO E PERMANENTE].\n\n‧ 4 - **SUPORTE E DENUNCIAS:**\n\n‧ 4.1 - Você pode denunciar outros usuários que não estão de concordância com as regras mencionando alguém da **staff** que esteja disponível ou indo no canal <#937041811812270180> e abrindo um ticket;\n\n‧ 4.2 - Caso queira denunciar algum membro, garanta que você possua provas o suficiente;\n\n‧ 4.3 - A equipe de moderação tem o poder de expulsar/banir os usuários que infligiram as regras;\n\n‧ 4.4 - Qualquer forma de ofensa aos integrantes da **staff** está estritamente proibida;\n\nSe alguém da equipe de moderação fez algo injusto ou abusou, encaminhe imediatamente para o dono do servidor <@901498839981236235>.", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed2.set_footer(text="LabyTeam Terms.")
        await channel.send(embed=embed2)
    
    @commands.Cog.listener()
    async def on_button_click(self, interaction: disnake.MessageInteraction):
        logs = self.bot.get_channel(1012005047330148433)

        cargo1 = disnake.utils.get(interaction.guild.roles, id=917419484388659201)
        cargo2 = disnake.utils.get(interaction.guild.roles, id=939136447175340092)
        cargo3 = disnake.utils.get(interaction.guild.roles, id=917419485831507989)

        cargo4 = disnake.utils.get(interaction.guild.roles, id=919773864437895238)
        cargo5 = disnake.utils.get(interaction.guild.roles, id=919773866509893732)
        cargo6 = disnake.utils.get(interaction.guild.roles, id=919773865847193680)

        cargo7 = disnake.utils.get(interaction.guild.roles, id=927652414532759602)
        cargo8 = disnake.utils.get(interaction.guild.roles, id=927652416114032690)
        cargo9 = disnake.utils.get(interaction.guild.roles, id=927652421612732417)

        comp = [
                disnake.ui.Button(label="Ver mais", custom_id="see_more_button", style=disnake.ButtonStyle.green),
                disnake.ui.Button(label="👨 Ele", custom_id="he_button"),
                disnake.ui.Button(label="🌈 Não-Binário", custom_id="not_binary_button"),
                disnake.ui.Button(label="👩 Ela", custom_id="she_button")
            ]

        comp2 = [
                disnake.ui.Button(label="Voltar", custom_id="see_minus_button", style=disnake.ButtonStyle.red),
                disnake.ui.Button(label="🎒 13-16 Anos", custom_id="13_16_button"),
                disnake.ui.Button(label="🍺 17-21 Anos", custom_id="17_21_button"),
                disnake.ui.Button(label="💼 22+", custom_id="22+_button"),
            ]

        if interaction.data.custom_id == "click_here_button":
            embed = disnake.Embed(title="Qual é o seu gênero?", description="👨 - Ele • <@&919773864437895238>.\n\n🌈 - Não-Binário • <@&919773866509893732>.\n\n👩 - Ela • <@&919773865847193680>.", color=blurple_color)  
            await interaction.response.send_message(embed=embed, components=comp, ephemeral=True)

        if interaction.data.custom_id == "see_more_button":    
            await interaction.response.defer()
            embed1 = disnake.Embed(title="Qual é a sua idade?", description="🎒 - 13-16 Anos • <@&927652414532759602>.\n\n🍺 - 17-21 Anos • <@&927652416114032690>.\n\n💼 - 22+ • <@&927652421612732417>.", color=blurple_color)  
            await interaction.edit_original_message(embed=embed1, components=comp2) 
                        
        if interaction.data.custom_id == "see_minus_button":
            await interaction.response.defer()
            embed = disnake.Embed(title="Qual é o seu gênero?", description="👨 - Ele • <@&919773864437895238>.\n\n🌈 - Não-Binário • <@&919773866509893732>.\n\n👩 - Ela • <@&919773865847193680>.", color=blurple_color)  
            await interaction.edit_original_message(embed=embed, components=comp)

        #Cargos de notificações
        
        if interaction.data.custom_id == "updates_button":
            if cargo1 not in interaction.author.roles:
                await interaction.author.add_roles(cargo1)

                await interaction.response.send_message(f"O cargo {cargo1.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Atualizações``\nID customizável: ``updates_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo1.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo1)

                await interaction.response.send_message(f"O cargo {cargo1.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Atualizações``\nID customizável: ``updates_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo1.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)


        if interaction.data.custom_id == "partners_button":
            if cargo2 not in interaction.author.roles:
                await interaction.author.add_roles(cargo2)

                await interaction.response.send_message(f"O cargo {cargo2.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Parcerias``\nID customizável: ``partners_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo2.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo2)

                await interaction.response.send_message(f"O cargo {cargo2.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Parcerias``\nID customizável: ``partners_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo2.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "status_button":
            if cargo3 not in interaction.author.roles:
                await interaction.author.add_roles(cargo3)

                await interaction.response.send_message(f"O cargo {cargo3.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Status``\nID customizável: ``status_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo3.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo3)

                await interaction.response.send_message(f"O cargo {cargo3.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#917417508955390052>\nBotão: ``Status``\nID customizável: ``status_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo3.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)
        
        #Cargos de gênero

        if interaction.data.custom_id == "he_button":
            if cargo4 not in interaction.author.roles:
                await interaction.author.add_roles(cargo4)

                await interaction.response.send_message(f"O cargo {cargo4.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Ele``\nID customizável: ``he_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo4.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo4)

                await interaction.response.send_message(f"O cargo {cargo4.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Ele``\nID customizável: ``he_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo4.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "not_binary_button":
            if cargo5 not in interaction.author.roles:
                await interaction.author.add_roles(cargo5)

                await interaction.response.send_message(f"O cargo {cargo5.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Não binário``\nID customizável: ``not_binary_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo5.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo5)

                await interaction.response.send_message(f"O cargo {cargo5.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Não binário``\nID customizável: ``not_binary_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo5.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "she_button":
            if cargo6 not in interaction.author.roles:
                await interaction.author.add_roles(cargo6)

                await interaction.response.send_message(f"O cargo {cargo6.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Ela``\nID customizável: ``she_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo6.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo6)

                await interaction.response.send_message(f"O cargo {cargo6.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``Ela``\nID customizável: ``she_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo6.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        #Cargos de idade

        if interaction.data.custom_id == "13_16_button":
            if cargo7 not in interaction.author.roles:
                await interaction.author.add_roles(cargo7)

                await interaction.response.send_message(f"O cargo {cargo7.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``13-16 Anos``\nID customizável: ``13_16_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo7.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo7)

                await interaction.response.send_message(f"O cargo {cargo7.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``13-16 Anos``\nID customizável: ``13_16_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo7.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "17_21_button":
            if cargo8 not in interaction.author.roles:
                await interaction.author.add_roles(cargo8)

                await interaction.response.send_message(f"O cargo {cargo8.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``17-21 Anos``\nID customizável: ``17_21_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo8.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo8)

                await interaction.response.send_message(f"O cargo {cargo8.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``17-21 Anos``\nID customizável: ``17_21_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo8.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "22+_button":
            if cargo9 not in interaction.author.roles:
                await interaction.author.add_roles(cargo9)

                await interaction.response.send_message(f"O cargo {cargo9.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``22+``\nID customizável: ``22+_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo9.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo9)

                await interaction.response.send_message(f"O cargo {cargo9.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: <#927669655907237930>\nBotão: ``22+``\nID customizável: ``22+_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo9.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

def setup(bot):
    bot.add_cog(Dono(bot))