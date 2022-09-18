from Config.colors import red_color, yellow_color, green_color
from Config.emojis import error_emoji, confirm_emoji
from disnake import Option, OptionType
from disnake.ext import commands
from Config.bot import footer
import datetime
import asyncio
import disnake


class Confirm(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=30)
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

    @disnake.ui.button(label="Confirmar", emoji=confirm_emoji, custom_id="confirm_button_one", style=disnake.ButtonStyle.green)
    async def confirm4(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.response.send_message("Confirmando...")
        await asyncio.sleep(4)
        self.value = True
        self.stop()

    @disnake.ui.button(label="Cancelar", emoji=error_emoji, custom_id="cancel_button_one", style=disnake.ButtonStyle.red)
    async def cancel4(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await asyncio.sleep(4)
        await interaction.response.send_message("Cancelando...")
        self.value = False
        self.stop()
        
class Moderação(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 
    @commands.slash_command(description="「🔧 Moderação」Bane uma pessoa do servidor", options=[Option('membro', 'Membro para ser banido' , OptionType.user, required=True) , Option('motivo', 'Motivo do banimento')])
    @commands.guild_only()
    async def ban(self, ctx, membro, *, motivo=None):
        if (not ctx.author.guild_permissions.ban_members):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Banir Membros``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        if membro.id == self.bot.user.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você está tentando me banir? Impossível...", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.guild.owner_id == membro.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Eu não posso banir o dono do servidor!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.user.id == membro.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Sério? Você realmente está tentando se banir?", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return


        ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja banir o membro {membro.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        ConfirmEmbed.set_footer(text=footer)
        view = Confirm(ctx)
        view.message = await ctx.send(embed=ConfirmEmbed, view=view)
        await view.wait()
        msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()
            
        elif view.value:
            BanEmbed = disnake.Embed(title=f'{confirm_emoji} | Membro banido!', description=f"O membro {membro.mention} foi banido com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            BanEmbed.add_field(name="Membro banido:", value=f"{membro.mention}")
            BanEmbed.add_field(name="Quem baniu?", value=f"{ctx.author.mention}", inline=False)
            if motivo == None:
                BanEmbed.add_field(name="Motivo:", value=f"Não foi colocado nenhum motivo!", inline=False)
            else:
                BanEmbed.add_field(name="Motivo:", value=f"**{motivo}**", inline=False)
            BanEmbed.set_footer(text=footer)
            await membro.ban(reason=motivo)
            await ctx.channel.send(embed=BanEmbed)
            await asyncio.sleep(4)
            await msg.delete()
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Banimento cancelado!", description=f"O banimento do membro {membro.mention} foi cancelado com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete()

    @commands.slash_command(description="「🔧 Moderação」Desbane uma pessoa que estava no servidor", options=[Option('usuário', 'ID do usuário para ser desbanido', OptionType.user, required=True)])
    @commands.guild_only()
    async def unban(self, ctx, *, usuário):
        if (not ctx.author.guild_permissions.ban_members):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Banir Membros``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        if usuário.id == self.bot.user.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Hã? Como você está tentando me desbanir desse servidor, sendo que eu estou bem aqui mandando essa mensagem de erro? 🧐", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.guild.owner_id == usuário.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji}| Erro!", description=f"Eu não posso desbanir o dono do servidor sendo que ele já está no servidor!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.user.id == usuário.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Sério? Você realmente está tentando se desbanir, sendo que você já está nesse servidor?", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        guild = ctx.guild
        banned_users = await guild.bans() 

        ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja desbanir o usuário {usuário.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        ConfirmEmbed.set_footer(text=footer)
        view = Confirm(ctx)
        view.message = await ctx.send(embed=ConfirmEmbed, view=view)
        await view.wait()
        msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()

        elif view.value:
            for ban in banned_users:
                if usuário.id == ban.user.id:
                    await guild.unban(user=usuário)
                    UnbanEmbed = disnake.Embed(title=f"{confirm_emoji} | Usuário desbanido!", description=f"O usuário {usuário.mention} foi desbanido com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
                    UnbanEmbed.add_field(name="Membro desbanido:", value=f"{usuário.mention}")
                    UnbanEmbed.add_field(name="Quem desbaniu?", value=f"{ctx.author.mention}", inline=False)
                    UnbanEmbed.set_footer(text=footer)
                    await ctx.send(embed=UnbanEmbed)
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Unban cancelado!", description=f"O unban do usuário {usuário.mention} foi cancelado com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete()

    
    @commands.slash_command(description="「🔧 Moderação」Expulsa um membro do servidor",  options=[Option('membro', 'Membro para ser expulso', OptionType.user, required=True) , Option('motivo', 'Motivo da expulsão', required=True)])
    @commands.guild_only()
    async def kick(self, ctx, membro, *, motivo=None):
        if (not ctx.author.guild_permissions.kick_members):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Expulsar Membros``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed)
            return
        
        if membro.id == self.bot.user.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você está tentando me expulsar? Impossível...", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.guild.owner_id == membro.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Eu não posso banir o dono do servidor!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        elif ctx.user.id == membro.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Sério? Você realmente está tentando se expulsar?", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return

        ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja expulsar o membro {membro.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        ConfirmEmbed.set_footer(text=footer)
        view = Confirm(ctx)
        view.message = await ctx.send(embed=ConfirmEmbed, view=view)
        await view.wait()
        msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()
        elif view.value:
            KickEmbed = disnake.Embed(title=f"{confirm_emoji} | Membro expulso!", description=f"O membro {membro.mention} foi expulso com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            KickEmbed.add_field(name="Membro expulso:", value=f"{membro.mention}")
            KickEmbed.add_field(name="Quem expulsou?", value=f"{ctx.author.mention}", inline=False)
            if motivo == None:
                KickEmbed.add_field(name="Motivo:", value=f"Não foi colocado nenhum motivo!", inline=False)
            else:
                KickEmbed.add_field(name="Motivo:", value=f"**{motivo}**", inline=False)
            KickEmbed.set_footer(text=footer)
            await ctx.send(embed=KickEmbed)
            await membro.kick(reason=motivo)
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Expulsão cancelada!", description=f"A expulsão do membro {membro.mention} foi cancelado com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete()    
    
    @commands.slash_command(description="「🔧 Moderação」Adicione um cargo em um membro por comando!", options=[Option('membro', 'Membro para ter o cargo adicionado', OptionType.user, required=True), Option('cargo', 'Cargo para ser adicionado no membro', OptionType.role, required=True)])
    @commands.guild_only()
    async def add_cargo(self, ctx, membro, cargo):
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
        
        ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja adicionar o cargo {cargo.mention} no membro {membro.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        ConfirmEmbed.set_footer(text=footer)
        view = Confirm(ctx)
        view.message = await ctx.send(embed=ConfirmEmbed, view=view)
        await view.wait()
        msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()
        elif view.value:
            await membro.add_roles(cargo)
            AddCargoEmbed = disnake.Embed(title=f"{confirm_emoji} | Cargo adicionado com sucesso!", description=f"O cargo {cargo.mention} foi adicionado com sucesso no membro {membro.mention}.", timestamp=datetime.datetime.utcnow(), color=membro.color)
            AddCargoEmbed.set_footer(text=footer)
            await ctx.send(embed=AddCargoEmbed) 
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Adição cancelada!", description=f"A adição do cargo {cargo.mention} no membro {membro.mention} foi cancelada com sucesso!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete()    
    
    @commands.slash_command(description="「🔧 Moderação」Remova um cargo de um membro por comando!", options=[Option('membro', 'Membro para ter o cargo removido', OptionType.user, required=True), Option('cargo', 'Cargo para ser removido do membro', OptionType.role, required=True)])
    @commands.guild_only()
    async def remover_cargo(self, ctx, membro, cargo: disnake.Role):
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

        ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja remover o cargo {cargo.mention} no membro {membro.mention}?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
        ConfirmEmbed.set_footer(text=footer)
        view = Confirm(ctx)
        view.message = await ctx.send(embed=ConfirmEmbed, view=view)
        await view.wait()
        msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()
        elif view.value:
            await membro.remove_roles(cargo)
            RemoveCargoEmbed = disnake.Embed(title=f"{confirm_emoji} | Cargo removido com sucesso!", description=f"O cargo {cargo.mention} foi removido com sucesso do membro {membro.mention}.", timestamp=datetime.datetime.utcnow(), color=membro.color)
            RemoveCargoEmbed.set_footer(text=footer)
            await ctx.send(embed=RemoveCargoEmbed)
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Remoção cancelada!", description=f"A remoção do cargo {cargo.mention} no membro {membro.mention} foi cancelada com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete() 
    
    #@commands.slash_command(description="「🔧 Moderação」Bloqueia um chat", options=[Option('canal', 'Canal para ser bloqueado', OptionType.channel, required=True)])
    #async def lock(self, ctx, canal):
        #if (not ctx.author.guild_permissions.manage_channels):
            #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Canais``!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            #ErrorEmbed.set_footer(text=footer)
            #await ctx.send(embed=ErrorEmbed)
            #return
        #channel = canal or ctx.channel
        #await channel.set_permissions(channel, create_topics=False, attach_files=False, use_slash_commands=False, send_messages=False)
        #LockEmbed = disnake.Embed(title="Canal bloqueado! 🔓", description=f"O canal {canal.mention} foi bloqueado por: {ctx.author.mention}", timestamp=datetime.datetime.utcnow(), color=0x00FF00)
        #LockEmbed.set_footer(text=footer)
        #await ctx.send(embed=LockEmbed)
        
    #@commands.slash_command(description="「🔧 Moderação」Desbloqueia um chat", options=[Option('canal', 'Canal para ser bloqueado', OptionType.channel, required=True)])
    #async def unlock(self, ctx, canal):
        #if (not ctx.author.guild_permissions.manage_channels):
            #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Canais``!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            #ErrorEmbed.set_footer(text=footer)
            #await ctx.send(embed=ErrorEmbed)
            #return
        #channel = canal or ctx.channel
        #await channel.set_permissions()
        #UnlockEmbed = disnake.Embed(title="Canal desbloqueado! 🔒", description=f"O canal {canal.mention} foi desbloqueado por: {ctx.author.mention}", timestamp=datetime.datetime.utcnow(), color=0x00FF00)
        #UnlockEmbed.set_footer(text=footer)
        #await ctx.send(embed=UnlockEmbed)

    @commands.slash_command(description="「🔧 Moderação」Limpe uma quantidade de mensagens", options=[Option('quantia', 'Quantidade de mensagens para serem deletadas', OptionType.number, required=True)])
    @commands.guild_only()
    async def clear(self, ctx, quantia):
        counter = [0]

        def check_purge(m):
            if m.pinned:
                counter[0] += 1
                return

            return True        
        
        if (not ctx.author.guild_permissions.manage_messages):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Mensagens``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)

            await asyncio.sleep(10)
            return
        if quantia >= 1001:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Eu só posso limpar entre **2** até **1000** mensagens!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)

            await asyncio.sleep(10)
            return
        else:
            quantia = int(quantia)+1
            apagadas = await ctx.channel.purge(limit=int(quantia))   
            clearEmbed = disnake.Embed(title='Chat limpo! :wastebasket:', description=f'Você apagou ``{len(apagadas)-1}`` mensagens com sucesso no chat.', timestamp=datetime.datetime.utcnow(), color=green_color)
            clearEmbed.set_footer(text=f'Já podem conversar novamente! | {footer}')
            await ctx.send(embed=clearEmbed)

            await asyncio.sleep(10)
            return
        apagadas = await ctx.channel.purge(limit=int(quantia)) 
        if not apagadas:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Eu não posso apagar mensagens de um canal que não tem mensagens!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)

            await asyncio.sleep(10)
            return

    
    #@commands.slash_command(description="「🔧 Moderação」Adiciona slowmode no chat", options=[Option('tempo', 'Tempo do slowmode', OptionType.number, required=True), Option('canal', 'Canal para ter o slowmode setado', OptionType.channel, required=True)])
    #async def slowmode(self, ctx, tempo:int, canal):
        #if (not ctx.author.guild_permissions.manage_channels):
            #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Canais``!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
            #ErrorEmbed.set_footer(text=footer)
            #await ctx.send(embed=ErrorEmbed)
            #return
        #else:
            #if tempo == 0:
                #NoSlowModeEmbed = disnake.Embed(title=f"{error_emoji} | SlowMode OFF!", description=f"O canal {canal.mention} agora está com o slowmode desligado.", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
                #NoSlowModeEmbed.set_footer(text=footer)
                #await ctx.send(embed=NoSlowModeEmbed)
                #await canal.edit(slowmode_delay = 0)
            #elif tempo > 21600:
                #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode setar um SlowMode acima de 6 horas. O tempo máximo é de 21600 segundos. (**6 Horas**) ", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
                #ErrorEmbed.set_footer(text=footer)
                #await ctx.send(embed=ErrorEmbed)
                #return
            #else:
                #SlowModeEmbed = disnake.Embed(title=f"{confirm_emoji} | SlowMode ON!", description=f"O canal {canal.mention} agora está com um slowmode de **{tempo}** segundos!", timestamp=datetime.datetime.utcnow(), color=0x00FF00)
                #SlowModeEmbed.set_footer(text=footer)
                #await canal.edit(slowmode_delay = tempo)
                #await ctx.send(embed=SlowModeEmbed)
        
    @commands.slash_command(description="「🔧 Moderação」Troca o nickname de um membro do seu servidor", options=[Option('membro', 'Membro para ter o nick trocado', OptionType.user, required=True), Option('nick', 'Novo nick do membro.', required=True)])
    @commands.guild_only()
    async def changenick(self, ctx, membro, nick):
        if (not ctx.author.guild_permissions.manage_channels):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Apelidos``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
    
        elif ctx.guild.owner_id == membro.id:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Eu não posso alterar o nick do dono do servidor!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if membro.nick is None:
            ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja atualizar o nickname do membro {membro.mention} para ``{nick}``?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            ConfirmEmbed.set_footer(text=footer)
            view = Confirm(ctx)
            view.message = await ctx.send(embed=ConfirmEmbed, view=view)
            await view.wait()
        else:
            ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Você tem certeza que deseja atualizar o nickname do membro {membro.name} de ``{membro.nick}`` para ``{nick}``?", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            ConfirmEmbed.set_footer(text=footer)
            view = Confirm(ctx)
            view.message = await ctx.send(embed=ConfirmEmbed, view=view)
            await view.wait()
            msg = await ctx.original_message()

        if view.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await msg.delete()
            
        elif view.value:       
            if membro.nick is None:
                nickEmbed = disnake.Embed(title=f'{confirm_emoji} | Nickname alterado! :wrench:', description=f"O nickname de **{membro.name}** foi alterado para ``{nick}``.", timestamp=datetime.datetime.utcnow(), color=green_color)
                nickEmbed.set_footer(text=footer)
                await ctx.send(embed=nickEmbed)
                await membro.edit(nick=nick)
            else:
                nickEmbed = disnake.Embed(title=f"{confirm_emoji} | Nickname alterado! :wrench:", description=f"O nickname de {membro.mention} foi alterado de ``{membro.nick}`` para ``{nick}``", timestamp=datetime.datetime.utcnow(), color=green_color)
                nickEmbed.set_footer(text=footer)
                await ctx.send(embed=nickEmbed)
                await membro.edit(nick=nick)
        else:
            ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Atualização cancelada!", description=f"A atualização de nickname do membro {membro.mention} foi cancelada com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            ErrorEmbed.set_footer(text=footer)
            msg2 = await ctx.channel.send(embed=ErrorEmbed)
            await asyncio.sleep(10)
            await msg2.delete()
            await asyncio.sleep(4)
            await msg.delete()

def setup(bot):
    bot.add_cog(Moderação(bot))