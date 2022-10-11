from Config.emojis import error_emoji, confirm_emoji, monitor_emoji, color_emoji, user_joined, role_emoji, id_emoji, users_emoji, calendar_emoji, text_channel_emoji, userinfo_emoji, owner_emoji, notification_emoji, computer_emoji, bot_emoji, online_emoji, idle_emoji, dnd_emoji, offline_emoji, vscode_emoji, python_emoji, memory_emoji, paper_emoji, ping_emoji, maping_emoji, discord_emoji, thumbsup_emoji, loading_emoji, spotify_emoji, info_emoji, arrow_left, arrow_right
from Config.colors import red_color, green_color, white_color, yellow_color
from Config.database import levelling_cluster, rep_cluster
from Config.images import image_failed
from disnake import Option, OptionType
from Config.discloud import api_token
from disnake import User, Member
from disnake.ext import commands
from typing import Union, List
from Config.bot import footer
from disnake import Spotify
import calendar
import discloud
import datetime
import requests
import disnake
import asyncio
import pymongo
import pytz


cluster = pymongo.MongoClient(levelling_cluster)
levelling = cluster["Discord"]["Níveis"]

cluster1 = pymongo.MongoClient(rep_cluster)
verificados = cluster1["Discord"]["Reputações"]

client = discloud.Client(api_token)


class Menu(disnake.ui.View):
    def __init__(self, embeds: List[disnake.Embed], ctx):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.ctx = ctx
        self.embed_count = 0

        self.prev_page.disabled = True

        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"LabyBot, todos direitos reservados. • Página {i + 1} de {len(self.embeds)}")
    
    async def interaction_check(self, interaction: disnake.Interaction):
        if interaction.user != self.ctx.author:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas {self.ctx.author.mention} pode clicar nesse botão!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
            return False
        else:
            return True

    @disnake.ui.button(emoji=arrow_left, style=disnake.ButtonStyle.secondary)
    async def prev_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False
        if self.embed_count == 0:
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @disnake.ui.button(label="Apagar", style=disnake.ButtonStyle.red)
    async def remove(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.delete_original_message()
        self.stop()

    @disnake.ui.button(emoji=arrow_right, style=disnake.ButtonStyle.secondary)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)


class Confirmar(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.value = None
        self.ctx = ctx

    
    async def interaction_check(self, interaction: disnake.Interaction):
        if interaction.user != self.ctx.author:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas {self.ctx.author.mention} pode clicar nesse botão!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
            return False
        else:
            return True

    @disnake.ui.button(label="Confirmar", emoji=confirm_emoji, style=disnake.ButtonStyle.green)
    async def confirm2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.response.send_message("Confirmando...")
        await asyncio.sleep(4)
        self.value = True
        self.stop()

    @disnake.ui.button(label="Cancelar", emoji=error_emoji, style=disnake.ButtonStyle.red)
    async def cancel2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.response.send_message("Cancelando...")
        await asyncio.sleep(4)
        self.value = False
        self.stop()

class MaisDetalhes(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx
        self.value = None

    
    async def interaction_check(self, interaction: disnake.Interaction):
        if interaction.user != self.ctx.author:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas {self.ctx.author.mention} pode clicar nesse botão!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
            return False
        else:
            return True

    @disnake.ui.button(label="Mais informações", emoji=info_emoji, custom_id="details_button" ,style=disnake.ButtonStyle.blurple)
    async def detalhes(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()


class Discord(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 
    @commands.slash_command(description="「📌 Discord」Veja as informações sobre um convite de um servidor", description_localizations="", options=[Option("link", "Link do convite que você quer ver as informações", OptionType.string, required=True)])
    async def inviteinfo(self, interaction: disnake.AppCommandInteraction, link: disnake.Invite):
        try:            
            if link.inviter is None:
                embed = disnake.Embed(title=f"{link.guild.name} - InviteInfo", timestamp=datetime.datetime.utcnow(), color=white_color)
                embed.set_thumbnail(url=link.guild.icon.url)
                embed.add_field(name=f"{id_emoji} | ID:", value=f"``{link.guild.id}``")
                embed.add_field(name=f'{users_emoji} | Membros', value=f'`{link.approximate_member_count}`', inline=False)
                embed.add_field(name=f"{notification_emoji} | Canal de convite:", value=f"`Indisponível`", inline=False)
                embed.add_field(name=f"{computer_emoji} | Quem convidou?", value=f"`{link.guild.name}` | ``{link.guild.id}``", inline=False)
                embed.set_footer(text=footer)
                await interaction.response.send_message(embed=embed, components=[disnake.ui.Button(label="Abrir ícone no navegador", url=link.guild.icon.url), disnake.ui.Button(label="Link do servidor", url=link.url)])
            else:
                embed = disnake.Embed(title=f"{link.guild.name} - InviteInfo", timestamp=datetime.datetime.utcnow(), color=white_color)
                embed.set_thumbnail(url=link.guild.icon.url)
                embed.add_field(name=f"{id_emoji} | ID:", value=f"``{link.guild.id}``")
                embed.add_field(name=f'{users_emoji} | Membros:', value=f"`{link.guild.member_count}`", inline=False)
                embed.add_field(name=f"{notification_emoji} | Canal de convite:", value=f"``{link.channel.name}`` | `{link.channel.id}`", inline=False)
                embed.add_field(name=f"{computer_emoji} | Quem convidou?", value=f"`{link.inviter.name}` | `{link.inviter.id}`", inline=False)
                embed.set_footer(text=footer)

                await interaction.response.send_message(embed=embed, components=[disnake.ui.Button(label="Abrir ícone no navegador", url=link.guild.icon.url), disnake.ui.Button(label="Link do servidor", url=link.url)])
        except Exception as e:
            print(e)
    
    
    @commands.slash_command(description="「📌 Discord」Mostra as informações de um usuário", options=[Option('usuário', 'Usúario para eu mostrar as informações', OptionType.user)])
    @commands.guild_only()
    async def userinfo(self, ctx, usuário: Union[Member, User] = None):
        try:
            membro = usuário if usuário else ctx.author     

            bot_ou_não = "Sim" if membro.bot else "Não"
            conta_criada = calendar.timegm(membro.created_at.utctimetuple())
            await ctx.channel.trigger_typing()

            view1 = disnake.ui.View()
            item = disnake.ui.Button(style=disnake.ButtonStyle.grey, label="Abrir avatar no navegador", url=(membro.avatar or membro.default_avatar).url)
            view1.add_item(item=item)

            busca = verificados.find_one({"id": membro.id})
            data = busca if busca else {}
            rep = data.get("reputações", 0)

            stats = levelling.find_one({"id" : membro.id})

            if isinstance(membro, Member):
                entrou_server = calendar.timegm(membro.joined_at.utctimetuple())

                view = MaisDetalhes(ctx=ctx)

                if membro.id == ctx.author.id:
                    embed = disnake.Embed(title=f'Suas informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                if membro.id == self.bot.user.id:
                    embed = disnake.Embed(title=f'Minhas informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                else:
                    embed = disnake.Embed(title=f'{membro} - Informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                embed.set_thumbnail(url=(membro.avatar or membro.default_avatar).url)
                embed.add_field(name=f'{id_emoji} | ID:', value=f'``{membro.id}``', inline=False)
                embed.add_field(name=f'{users_emoji} | Nick Completo:', value=f'``{membro}``', inline=False)
                if membro.id == self.bot.user.id:
                    embed.add_field(name=f"{bot_emoji} | Bot?", value=f"`Sim, eu sou um bot!`")
                else:
                    embed.add_field(name=f"{bot_emoji} | Bot?", value=f"`{bot_ou_não}`")
                if str(membro.status) == "online":
                    embed.add_field(name=f"{online_emoji} | Status", value=f"``Online``", inline=False)
                if str(membro.status) == "idle":
                    embed.add_field(name=f"{idle_emoji} | Status", value=f"``Ausente``", inline=False)
                if str(membro.status) == "dnd":
                    embed.add_field(name=f"{dnd_emoji} | Status", value=f"``Não Pertube``", inline=False)
                if str(membro.status) == "offline":
                    embed.add_field(name=f"{offline_emoji} | Status", value=f"``Offline``", inline=False)
                embed.add_field(name=f"{calendar_emoji} | No discord desde:", value=f'<t:{conta_criada}:f> | <t:{conta_criada}:R>', inline=False)
                embed.add_field(name=f'{user_joined} | Entrou em:', value=f'<t:{entrou_server}:f> | <t:{entrou_server}:R>', inline=False)
                embed.set_footer(text=footer)
                view.message = await ctx.send(embed=embed, view=view)
                await view.wait()
                msg = await ctx.original_message()

                if view.value:
                    if membro.id == ctx.author.id:
                        embed = disnake.Embed(title=f'Suas informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                    if membro.id == self.bot.user.id:
                        embed = disnake.Embed(title=f'Minhas informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                    else:
                        embed = disnake.Embed(title=f'{membro} - Informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                    embed.set_thumbnail(url=(membro.avatar or membro.default_avatar).url)
                    embed.add_field(name=f'{id_emoji} | ID:', value=f'``{membro.id}``')
                    embed.add_field(name=f'{users_emoji} | Nick Completo:', value=f'``{membro}``', inline=False)
                    if membro.id == self.bot.user.id:
                        embed.add_field(name=f"{bot_emoji} | Bot?", value=f"`Sim, eu sou um bot!`", inline=False)
                    else:
                        embed.add_field(name=f"{bot_emoji} | Bot?", value=f"`{bot_ou_não}`", inline=False)
                    if str(membro.status) == "online":
                        embed.add_field(name=f"{online_emoji} | Status", value=f"``Online``", inline=False)
                    if str(membro.status) == "idle":
                        embed.add_field(name=f"{idle_emoji} | Status", value=f"``Ausente``", inline=False)
                    if str(membro.status) == "dnd":
                        embed.add_field(name=f"{dnd_emoji} | Status", value=f"``Não Pertube``", inline=False)
                    if str(membro.status) == "offline":
                        embed.add_field(name=f"{offline_emoji} | Status", value=f"``Offline``", inline=False)
                    embed.add_field(name=f"{calendar_emoji} | No discord desde:", value=f'<t:{conta_criada}:f> | <t:{conta_criada}:R>', inline=False)
                    if membro.id == self.bot.user.id:
                        embed.add_field(name=f'{user_joined} | Entrei em:', value=f'<t:{entrou_server}:f> | <t:{entrou_server}:R>', inline=False)
                    else:
                        embed.add_field(name=f'{user_joined} | Entrou em:', value=f'<t:{entrou_server}:f> | <t:{entrou_server}:R>', inline=False)
                    if stats is None:
                        embed.remove_field(index=1)
                    else:
                        xp = stats["xp"]
                        lvl = 0
                        rank = 0
                        while True:
                            if xp < ((50*(lvl**2))+(50*lvl)):
                                break
                            lvl += 1
                        xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                        rankings = levelling.find().sort("xp", -1)
                        for x in rankings:
                            rank +=1
                            if stats["id"] == x["id"]:
                                break
                        embed.add_field(name="⭐ | XP:", value=f"Nível ``{lvl}`` ({stats['xp']} de XP)", inline=False)
                    if rep == 0:
                        embed.remove_field(index=1)
                    else:
                        embed.add_field(name=f"{thumbsup_emoji} | Reps:", value=f"``{rep}`` Reputações", inline=False)
                    if len(membro.roles) == 1:
                        embed.add_field(name=":tada: | Cargos:", value="``Sem cargos.``", inline=False)
                        embed.set_footer(text=footer)

                        if membro.avatar is None:
                            await ctx.send(embed=embed)
                            await msg.delete()
                        else:
                            await ctx.send(embed=embed, view=view1)
                            await msg.delete()
                    else:
                        sorted_roles = sorted([role for role in membro.roles[1:]], key=lambda x: x.position, reverse=True)
                        if len(membro.roles) > 2 :
                            embed.add_field(name=f':tada: | {len(membro.roles)-1} Cargos:', value=', '.join(role.mention for role in sorted_roles), inline=False)
                        else:
                            embed.add_field(name=f':tada: | {len(membro.roles)-1} Cargo:', value=', '.join(role.mention for role in sorted_roles), inline=False)
                        embed.set_footer(text=footer)

                        if membro.avatar is None:
                            await ctx.send(embed=embed)
                            await msg.delete()
                        else:
                            await ctx.send(embed=embed, view=view1)
                            await msg.delete()
                else:
                    return

            if isinstance(membro, User):
                embed = disnake.Embed(title=f'{membro} - Informações', timestamp=datetime.datetime.utcnow(), color=membro.color)
                if membro.avatar is None:
                    embed.set_thumbnail(url=membro.default_avatar.url)
                else:
                    embed.set_thumbnail(url=membro.avatar.url)
                embed.add_field(name=f'{id_emoji} | ID:', value=f'``{membro.id}``', inline=False)
                embed.add_field(name=f'{users_emoji} | Nick Completo:', value=f'``{membro}``', inline=False)
                embed.add_field(name=f"{bot_emoji} | Bot?", value=f"`{bot_ou_não}`")
                embed.add_field(name=f"{calendar_emoji} | No discord desde:", value=f'<t:{conta_criada}:f> | <t:{conta_criada}:R>', inline=False)
                if stats is None:
                    embed.remove_field(index=1)
                else:
                    xp = stats["xp"]
                    lvl = 0
                    rank = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    rankings = levelling.find().sort("xp", -1)
                    for x in rankings:
                        rank +=1
                        if stats["id"] == x["id"]:
                            break
                    embed.add_field(name="⭐ | XP:", value=f"Nível ``{lvl}`` ({stats['xp']} de XP)", inline=False)
                    if rep == 0:
                        embed.remove_field(index=1)
                    else:
                        embed.add_field(name=f"{thumbsup_emoji} | Reps:", value=f"``{rep}`` Reputações", inline=False)
                embed.set_footer(text=footer)
                if membro.avatar is None:
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(embed=embed, view=view1)
        except Exception as e:
            print(e)
    
    @commands.slash_command(description="「📌 Discord」Agradeça algum usuário por ter lhe ajudado no servidor!", options=[Option('usuário', 'Usuário para ser reputado', OptionType.user, required=True)])
    @commands.guild_only()
    async def valeu(self, ctx, usuário: disnake.User):
        if usuário.id == ctx.author.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode dar uma reputação para si mesmo!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if usuário.bot:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode dar uma reputação para um bot!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if usuário.id == self.bot.user.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Infelizmente você não pode dar uma reputação para mim, mas você pode mandar um feedback utilizando o comando </feedback:1011781821668806668>!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if not ctx.author.bot:
            ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja dar uma reputação ao membro {usuário.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            ConfirmEmbed.set_footer(text=footer)
            view = Confirmar(ctx)
            view.message = await ctx.send(embed=ConfirmEmbed, view=view)
            await view.wait()
            msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await msg.delete()
        elif view.value:
            stats = verificados.find_one({"id" : usuário.id})
            if stats is None:
                    newuser = {"usuário" : f"{usuário.name}#{usuário.discriminator}",
                                "id" : usuário.id,
                               "reputações" : 0 }
                    verificados.insert_one(newuser)
                    stats1 = verificados.find_one({"id" : usuário.id})

            rep = stats1["reputações"] + 1
            verificados.update_one({"usuário": f"{usuário.name}#{usuário.discriminator}", "id": usuário.id}, {"$set":{"reputações":rep}})
            rep1 = disnake.Embed(title=f'{confirm_emoji} | Membro reputado!', description=f"Você agradeceu {usuário.mention} e agora ele possui ``{rep}`` reputações!", timestamp=datetime.datetime.utcnow(), color=green_color)
            rep1.set_footer(text=footer)
            await ctx.send(embed=rep1, ephemeral=True)
            await msg.delete()
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Reputação cancelada!", description=f"A reputação do membro {usuário.mention} foi cancelada!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await msg.delete()
    
    @commands.slash_command(description="「📌 Discord」Mostra a quantidade de reps que um usuário tem", options=[Option('usuário', 'Usuário que você quer ver a quantidade de reputações', OptionType.user)])
    @commands.guild_only()
    async def reps(self, ctx, usuário: disnake.User = None):
        member = usuário if usuário else ctx.author        

        busca = verificados.find_one({"id": member.id})
        data = busca if busca else {}
        rep = data.get("reputações", 0)
        if member.bot:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Comigo, bots não possuem reputações! (Nem eu mesmo'-')", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if member.id == ctx.author.id:
            if rep == 0:
                await ctx.response.defer()
                embed = disnake.Embed(description=f"Infelizmente você não possui nenhuma reputação...", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Reps")
                embed.set_footer(text=footer)
                await ctx.send(embed=embed)
            else: 
                embed = disnake.Embed(description=f"Você possui ``{rep}`` reputações!", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Reps")
                embed.set_footer(text=footer)
                await ctx.send(embed=embed)
                return
        else:
            if rep == 0:
                embed = disnake.Embed(description=f"Infelizmente {usuário.mention} não possui nenhuma reputação...", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Reps")
                embed.set_footer(text=footer)
                await ctx.send(embed=embed)
                return
            else: 
                embed = disnake.Embed(description=f"{usuário.mention} possui ``{rep}`` reputações!", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Reps")
                embed.set_footer(text=footer)
                await ctx.send(embed=embed)
                return
    
    @commands.slash_command(description="「📌 Discord」Mostra o avatar de um usuário", options=[Option('usuário', 'Usuário para eu mostrar o avatar', OptionType.user)])
    @commands.guild_only()
    async def avatar(self, ctx, usuário: disnake.User = None):
        try:
            membro = usuário if usuário else ctx.author        

            avaEmbed = disnake.Embed(title=f"Avatar de {membro.name}", timestamp=datetime.datetime.utcnow(), color=white_color)
            if membro.id == ctx.author.id:
                avaEmbed = disnake.Embed(title=f'Seu avatar', timestamp=datetime.datetime.utcnow(), color=membro.color)
            if membro.id == self.bot.user.id:
                avaEmbed = disnake.Embed(title=f'Meu avatar', timestamp=datetime.datetime.utcnow(), color=membro.color)
            avaEmbed.set_footer(text=footer)
            avaEmbed.set_image(url=(membro.avatar or membro.default_avatar).url)
            if membro.avatar is None:
                await ctx.send(embed=avaEmbed)
            else:
                view1 = disnake.ui.View()
                item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Abrir avatar no navegador", url=membro.avatar.url)
                view1.add_item(item=item)
                await ctx.send(embed=avaEmbed, view=view1)
        except Exception as e:
            await ctx.send(e)
    
    @commands.slash_command(description="「📌 Discord」Mostra as informações de um emoji personalizado", options=[Option("emoji", "Emoji que você quer ver as informações", required=True)])
    @commands.guild_only()
    async def emoji_info(self, ctx, emoji: disnake.Emoji):    
         
        view5 = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Abrir emoji no navegador", url=f"{emoji.url}")
        view5.add_item(item=item)

        is_animated = "Sim" if emoji.animated else "Não"
        creation_time = calendar.timegm(emoji.created_at.utctimetuple())
        can_use_emoji = (
            "Todo mundo"
            if not emoji.roles
            else " ".join(role.name for role in emoji.roles)
        )

        description = f"""
        **Informações Gerais:**
        **- Nome:** ``{emoji.name}``
        **- ID:** ``{emoji.id}``
        **- Criado em:** <t:{creation_time}:F>
        **- Utilizável para:** ``{can_use_emoji}``
        
        **Outras Informações:**
        **- Animado?** ``{is_animated}``
        **- Quantidade de cargos com esse emoji:** ``{len(emoji.roles)}``
        **- Nome do servidor em que o emoji foi criado:** ``{emoji.guild.name}``
        **- ID do servidor em que o emoji foi criado:** ``{emoji.guild.id}``
        """

        embed = disnake.Embed(
            title=f"Informações do emoji: `{emoji.name}`",
            description=description,
            colour=white_color,
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url=emoji.url)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, view=view5)
        
    @commands.slash_command(description="「📌 Discord」Mostra as informações de um cargo", options=[Option("cargo", "Cargo que você quer ver as informações", OptionType.role, required=True)])
    @commands.guild_only()
    async def role_info(self, ctx, cargo: disnake.Role):
        try:
            creation_time2 = calendar.timegm(cargo.created_at.utctimetuple())
            mencionavel = "Sim" if cargo.mentionable else "Não"
            separadamente = "Sim" if cargo.hoist else "Não"
            perms_available = {
                "administrator": "``Administrador``",
                "send_messages": "``Enviar mensagens``",
                "manage_messages": "``Gerenciar mensagens``",
                "create_instant_invite": "``Criar um convite instantâneo``",
                "kick_members": "``Expulsar membros``",
                "ban_members": "``Banir membros``",
                "manage_channels": "``Gerenciar canais``",
                "manage_guild": "``Gerenciar servidor``",
                "add_reactions": "``Adicionar reações``",
                "view_audit_log": "``Ver o registro de auditoria``",
                "priority_speaker": "``Voz prioritária``",
                "view_channel": "``Ver canais``",
                "read_messages": "``Ler mensagens``",
                "send_tts_messages": "``Enviar mensagens em Texto-para-voz``",
                "embed_links": "``Inserir links``",
                "attach_files": "``Anexar arquivos``",
                "read_message_history": "``Ver histórico de mensagens``",
                "mention_everyone": "``Mencionar @everyone, @here e todos os cargos``",
                "external_emojis": "``Usar emojis externos``",
                "view_guild_insights": "``Ver análises do servidor``",
                "connect": "``Conectar em um canal de voz``",
                "speak": "``Falar em um canal de voz``",
                "mute_members": "``Silenciar membros em um canal de voz``",
                "deafen_members": "``Ensurdecer membros em um canal de voz``",
                "move_members": "``Mover membros de um canal de voz para outro``",
                "use_voice_activation": "``Usar detecção de voz``",
                "change_nickname": "``Mudar apelido``",
                "manage_nicknames": "``Gerenciar apelidos``",
                "manage_roles": "``Gerenciar cargos``",
                "manage_permissions": "``Gerenciar permissões``",
                "manage_webhooks": "``Gerenciar webhooks``",
                "manage_emojis": "``Gerenciar emojis``",
                "manage_emojis_and_stickers": "``Gerenciar emojis e figurinhas``",
                "use_slash_commands": "``Usar comandos de barra``",
                "request_to_speak": "``Pedir para falar``",
                "manage_events": "``Gerenciar eventos``",
                "manage_threads": "``Gerenciar tópicos``",
                "create_public_threads": "``Criar tópicos públicos``",           
                "create_private_threads": "``Criar tópicos privados``",
                "external_stickers": "``Usar figurinhas externas``",
                "send_messages_in_threads": "``Enviar mensagens em tópicos``",
                "moderate_members": "``Colocar membros de castigo``"
            }

            total = []

            for perm, traduzido in perms_available.items():
                if getattr(cargo.permissions, perm):
                    total.append(traduzido)        
            total = ', ' .join(total) if total else "``Sem permissões.``"

            embed = disnake.Embed(title=f"Informações do cargo: ``{cargo.name}``", timestamp=datetime.datetime.utcnow(), color=white_color)
            embed.add_field(name=f"{notification_emoji} | Menção:", value=f"`{cargo.mention}`")
            embed.add_field(name=f"{userinfo_emoji} | Data de criação:", value=f"<t:{creation_time2}:F>", inline=False)
            embed.add_field(name=f"{id_emoji} | ID:", value=f"`{cargo.id}`", inline=False)
            embed.add_field(name=f"{notification_emoji} | Mencionável por outros usuários?", value=f"`{mencionavel}`", inline=False)
            embed.add_field(name=f"{users_emoji} | Exibe separadamente na lista de membros?", value=f"`{separadamente}`", inline=False)
            embed.add_field(name=f"{users_emoji} | Quantidade de membros com esse cargo:", value=f"`{len(cargo.members)}`", inline=False)
            embed.add_field(name=f"{color_emoji} | Cor do cargo:", value=f"`{cargo.color}`", inline=False)
            embed.set_footer(text=footer)

            embed1 = disnake.Embed(title=f"Informações do cargo: ``{cargo.name}``", description=f"{computer_emoji} **| Permissões:**\n {total}", timestamp=datetime.datetime.utcnow(), color=white_color)
            #embed1.add_field(name=f"{computer_emoji} | Permissões:", value=total, inline=False)
            embed1.set_footer(text=footer)

            valid_embeds = [embed, embed1]

            await ctx.send(embed=valid_embeds[0], view=Menu(valid_embeds, ctx))

        except Exception as e:
            print(e)

    @commands.slash_command(description="「📌 Discord」Permite que você crie um cargo por comando", options=[Option('nome', 'Nome do cargo que irá ser criado', required=True)])
    @commands.guild_only()
    async def criar_cargo(self, ctx, *, nome):
        if (not ctx.author.guild_permissions.manage_roles):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Cargos``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        guild = ctx.guild
        await guild.create_role(name=nome)
        CargoEmbed = disnake.Embed(title=f"{confirm_emoji} | Cargo criado com sucesso!", description=f"O cargo **{nome}** foi criado com sucesso!", timestamp=datetime.datetime.utcnow(),color=white_color)
        CargoEmbed.set_footer(text=footer)
        await ctx.send(embed=CargoEmbed)

    @commands.slash_command(description="「📌 Discord」Permite que você delete um cargo por comando", options=[Option('cargo', 'Nome do cargo que irá ser deletado', OptionType.role, required=True)])
    @commands.guild_only()
    async def deletar_cargo(self, ctx, *, cargo: disnake.Role):
        if (not ctx.author.guild_permissions.manage_roles):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Cargos``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if cargo >= ctx.author.top_role:
            ErrorEmbed2 = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O cargo que você selecionou não pode ser mais alto do que o seu!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed2.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed2, ephemeral=True)
            return

        guild = ctx.guild
        if cargo in guild.roles:
            await cargo.delete()
            CargoEmbed = disnake.Embed(title=f"{confirm_emoji} | Cargo deletado com sucesso!", description=f"O cargo **{cargo}** foi deletado com sucesso!", timestamp=datetime.datetime.utcnow(), color=white_color)
            CargoEmbed.set_footer(text=footer)
            await ctx.send(embed=CargoEmbed)
        
    @commands.slash_command(description="「📌 Discord」Mostra as informações do servidor atual", options=[Option("servidor", "Servidor no qual você deseja ver as informações.")])
    @commands.guild_only()
    async def serverinfo(self, ctx, servidor: disnake.Guild=None):
        try:
            server = servidor if servidor else ctx.guild

            Criadoem = calendar.timegm(server.created_at.utctimetuple())
            total = len(server.text_channels) + len(server.voice_channels)

            view = disnake.ui.View()
            item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Abrir ícone no navegador", url=server.icon.url)
            view.add_item(item=item)

            if server.id == ctx.guild.id:
                serverinfoEmbed = disnake.Embed(title=f"Informações desse servidor", timestamp=datetime.datetime.utcnow(), color=white_color)
            else:
                serverinfoEmbed = disnake.Embed(title=f"{server.name} - Informações", timestamp=datetime.datetime.utcnow(), color=white_color)
            if server.icon is None:
                serverinfoEmbed.set_thumbnail(url=image_failed)
            else:
                serverinfoEmbed.set_thumbnail(url=server.icon.url) 
            serverinfoEmbed.add_field(name=f"{id_emoji} | ID:", value=f'``{server.id}``')
            serverinfoEmbed.add_field(name=f"{owner_emoji} | Dono:", value=f"``{server.owner}`` | ``{server.owner_id}``", inline=False)
            serverinfoEmbed.add_field(name=f'{role_emoji} | Cargos:', value=f'`{len(server.roles)}`', inline=False)
            serverinfoEmbed.add_field(name=f'{users_emoji} | Membros ({len(server.members)}):', value=f'`{len([m for m in server.members if not m.bot])}` usuários e `{len(list(filter(lambda m: m.bot, server.members)))}` bots', inline=False)
            serverinfoEmbed.add_field(name=f"{monitor_emoji} | **Canais: ({total})**", value=f'{text_channel_emoji} **Texto:** `{len(server.text_channels)}`\n<:892799472478871613:927236608611221565> **Voz:** `{len(server.voice_channels)}`')  
            serverinfoEmbed.add_field(name=f"{calendar_emoji} | Criado em:", value=f'<t:{Criadoem}:F> | <t:{Criadoem}:R>', inline=False)
            serverinfoEmbed.set_footer(text=footer)
            if server.icon is None:
                await ctx.send(embed=serverinfoEmbed)
            else:
                await ctx.send(embed=serverinfoEmbed, view=view)
        except Exception as e:
            print(e)
        
    @commands.slash_command(description="「📌 Discord」Mostra a logo do servidor atual")
    @commands.guild_only()
    async def servericon(self, ctx):
        if ctx.guild.icon is None:
            ErrorEmbed2 = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Esse servidor não possui um ícone.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed2.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed2, ephemeral=True)
            return
        else:
            embed = disnake.Embed(title=f'Ícone desse servidor', timestamp=datetime.datetime.utcnow(), color=white_color)
            embed.set_image(url=ctx.guild.icon.url)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)
            
    @commands.slash_command(description='「📌 Discord」Mostra algumas informações sobre o bot', timestamp=datetime.datetime.utcnow())
    @commands.guild_only()
    async def botinfo(self, ctx):   
        try:
            epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
            tempo = (ctx.me.created_at.replace(tzinfo=None).astimezone(datetime.timezone.utc)-epoch).total_seconds()


            members = 0
            for guild in ctx.bot.guilds:
                members += guild.member_count - 1
            servers = len(ctx.bot.guilds)

            bot = await client.app_info(target=908870304909115432)

            BotEmbed = disnake.Embed(title='Olá eu sou o LabyBot!', description=f'Olá {ctx.author.mention}! me chamo LabyBot, mas pode me chamar de Laby! sou um bot simples e em beta para o discord! Veja abaixo minhas informações atualizadas!', color=white_color, timestamp=datetime.datetime.utcnow())
            BotEmbed.set_thumbnail(url=self.bot.user.avatar.url)
            BotEmbed.add_field(name=f'{vscode_emoji} | Programado em:', value='``Visual Studio Code (Python)``')
            BotEmbed.add_field(name=f'{python_emoji} | Python:', value=f'``3.10.6``', inline=False)
            BotEmbed.add_field(name=f"{memory_emoji} | Memória", value=f"``{bot.memory.using}``", inline=False)
            BotEmbed.add_field(name=f'{paper_emoji} | Comandos:', value=f'``{len(self.bot.global_slash_commands)}``', inline=False)
            BotEmbed.add_field(name=f'{ping_emoji} | Ping:', value=f'``{round(self.bot.latency * 1000)}``', inline=False)
            BotEmbed.add_field(name=f"{maping_emoji} | Minha data de nascimento:", value=f"<t:{int(tempo)}:F> | <t:{int(tempo)}:R>")
            BotEmbed.add_field(name=f"{users_emoji} | Usuários:", value=f"``{members}``", inline=False)
            BotEmbed.add_field(name=f"{discord_emoji} | Servidores:", value=f"``{servers}``", inline=False)
            BotEmbed.add_field(name=f'{owner_emoji} | Criado por: ', value='<@901498839981236235>', inline=False)
            #BotEmbed.add_field(name='<:892799472478871613:916712894148788235> | Colaboradores: ', value='', inline=False)
            BotEmbed.set_footer(text=footer)
            await ctx.channel.trigger_typing()
            await ctx.send(embed=BotEmbed)
        except Exception as e:
                print(e)

    @commands.slash_command(description="「📌 Discord」Veja o que um usuário está escutando no spotify!", options=[Option('usuário', 'Usuário que você quer ver o que ela está escutando no spotify', OptionType.user)])
    @commands.guild_only()
    async def spotify(self, ctx, usuário: disnake.User = None):
        member = usuário if usuário else ctx.author        

        #user = ctx.guild.get_member(user.id)
        if not any([isinstance(presence, Spotify) for presence in member.activities]):
            if member.id == ctx.author.id:
                embed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não está escutando nada spotify, lembrando que você tem que ter o spotify conectado no discord!", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, ephemeral=True)
            else:
                embed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{member.mention} não está escutando nada spotify, lembrando que ele tem que ter o spotify conectado no discord!", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, ephemeral=True)
        else:
            for activity in member.activities:
                if isinstance(activity, Spotify):
                    view = disnake.ui.View()
                    item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Link da Música", url=f"https://open.spotify.com/track/{activity.track_id}")
                    view.add_item(item=item)
                    minutes = activity.duration.seconds // 60
                    seconds = activity.duration.seconds % 60
                    if member.id == ctx.author.id:
                        embed = disnake.Embed(title=f"{spotify_emoji} | Seu spotify", description="**Ouvindo:**\n``{}``".format(activity.title), timestamp=datetime.datetime.utcnow(), color=activity.color)
                    else:
                        embed = disnake.Embed(title=f"{spotify_emoji} | Spotify de {member.name}", description="**Ouvindo:**\n``{}``".format(activity.title), timestamp=datetime.datetime.utcnow(), color=activity.color)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Duração:", value=f"``{minutes}:{seconds}``", inline=False)
                    embed.add_field(name="Artista(s):", value=f'``{activity.artist}``')
                    embed.add_field(name="Álbum:", value=f'``{activity.album}``', inline=False)
                    data = activity.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M")
                    embed.set_footer(text=f"Musica iniciou às {data}. | {footer}")
                    
                    await ctx.send(embed=embed, view=view)

    @commands.slash_command(description='「📌 Discord」Mostra a latência do LabyBot e da API')
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f'{loading_emoji} | Calculando minha latência...')
        await asyncio.sleep(2)
        await ctx.edit_original_message(content=f"{loading_emoji} | Calculando minha latência......")
        await asyncio.sleep(2)
        await ctx.delete_original_message()
        msg = await ctx.channel.send("Latência calculada!")
        await asyncio.sleep(1)
        await msg.delete()
        pingEmbed = disnake.Embed(title="Pong!", description=f"{ping_emoji} | Minha latência: ``{int(self.bot.latency * 1000)}ms``", timestamp=datetime.datetime.utcnow(), color=white_color)
        pingEmbed.set_footer(text=footer)
        await ctx.send(embed=pingEmbed)
    
        #pingEmbed = discord.Embed(title=':ping_pong: | Pong!', color=0xfafafa, timestamp=datetime.datetime.utcnow())
        #pingEmbed.description = f'Estou com uma latência de ``{round(self.bot.latency * 1000)}ms``!'
        #pingEmbed.set_footer(text=footer)
        #await ctx.send(embed=pingEmbed)
    
    #@commands.slash_command()
    #async def fosforo(self, ctx):
        #channel = self.bot.get_channel(942525315782168636)
        #embed = disnake.Embed(title="Recompensas - Parceria", description="Sendo um parceiro nosso, você terá recompensas como:", color=0xfafafa)
        #embed.add_field(name="Rec.1", value="Um convite do seu servidor ficará no canal <#939137919363481690> até o fim da parceria com uma mensagem feita especialmente por você!")
        #embed.add_field(name="Rec.2", value="Você poderá ter um comando ou um evento **__básico__** personalizado no seu servidor, como mensagem de boas-vindas e etc.", inline=False)
        #embed.add_field(name="Rec.3", value="Embeds personalizadas para o seu servidor.\n\nCaso queira ter essas recompensas no seu servidor, basta abrir um ticket no <#981578389305565234> que um responsável por essa área irá lhe ajudar.", inline=False)
        #embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/942211409444491314.png')
        #await channel.send(embed=embed)

    #@commands.slash_command()
    #async def fosforo2(self, ctx):
        #channel = self.bot.get_channel(942525315782168636)
        #embed = disnake.Embed(title="Requisitos - Parceria", description="Olá pessoa! Está querendo ser nosso parceiro? Queriamos que você fosse nosso parceiro, mas calma lá! O seu servidor precisa cumprir alguns requisitos para ser aprovado e finalmente ser um parceiro nosso!", color=0xfafafa)
        #embed.add_field(name="Req.1", value="Ter o <@908870304909115432> (eu) no seu servidor.")
        #embed.add_field(name="Req.2", value="O seu servidor tem que ter no mínimo 30 membros.", inline=False)
        #embed.add_field(name="Req.3", value="O seu servidor tem que ser ativo.", inline=False)
        #embed.add_field(name="Req.4", value="O seu servidor não pode ter canais NSFW e muitas pessoas tóxicas.", inline=False)
        #embed.add_field(name="Req.5", value="O dono do servidor tem que está nesse servidor.", inline=False)
        #embed.add_field(name="Req.6", value="O seu servidor tem que ter um canal para parcerias e um cargo de parceiros.", inline=False)
        #embed.add_field(name="Req.7", value="O dono do servidor (você ou outra pessoa) tem que ter no mínimo 13 anos. (Segundo o Discord, menores de 13 não podem ter conta.)\n\nCaso o seu servidor cumpra os requisitos e quer ser um parceiro nosso, abra um ticket no <#981578389305565234> que um responsável por essa área irá lhe ajudar.", inline=False)
        #embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/937166069838266368/937166109931630653/c6447b128308cceb61aa795e61de7ee4.png')
        #await channel.send(embed=embed)
    
    #@commands.Cog.listener()
    #async def on_message(self, message):
        #if message.author.id in afks.keys():
            #afks.pop(message.author.id)
            #await message.channel.send(f'👋 | Bem vindo de volta {message.author.mention}, eu removi o seu AFK.')

        #for id, reason in afks.items():
            #member = get(message.guild.member, id=id)
            #if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                #await message.channel.send(f"{member.mention} está AFK no momento. | Motivo: **{reason}**")
    
    #@commands.slash_command(description="「📌 Discord」Ao utilizar esse comando, você fica AFK", options=[Option('motivo', 'Motivo do afk')])
    #async def afk(self, ctx, *, motivo="Nenhum motivo especificado."):
        #member = ctx.author 
        #embed = disnake.Embed(title=":zzz: Membro AFK", description=f"{member.mention} ativou o AFK.", timestamp=datetime.datetime.utcnow(), color=member.color)
        #embed.set_thumbnail(url=member.avatar.url)
        #embed.set_author(icon_url="https://cdn.discordapp.com/attachments/905914689442160703/916715968464564285/laby.png", name="LabyBot AFK System")
        #embed.set_footer(text=footer)
        #embed.add_field(name='Motivo do AFK:', value=motivo)
        #await ctx.send(embed=embed)
        #def check(x):
            #return x.guild == ctx.guild
        #msg = await self.bot.wait_for("message", check=check)
        #while True:
            #if msg.author == ctx.author:
                #break
            #if f"<@{ctx.author.id}>" in msg.content:
                    #await msg.channel.send(f"{member.mention} está AFK no momento. | Motivo: **{motivo}**.")
        #await msg.channel.send(f'👋 | Bem vindo de volta {msg.author.mention}, eu removi o seu AFK.')

def setup(bot):
    bot.add_cog(Discord(bot))