from Config.emojis import loading_emoji, error_emoji, confirm_emoji, wallet_emoji, bank_emoji, coin_emoji, warning_emoji, work_emoji, clock_emoji, manwithmoney_emoji, deposit_emoji, withdraw_emoji
from Config.colors import red_color, green_color, yellow_color, blurple_color
from disnake import Option, OptionType
from disnake.ext import commands
from Config.bot import footer
import datetime
import sys, os
import asyncio
import disnake
import sqlite3
import random


class Dropdown(disnake.ui.Select):
    def __init__(self):

        options = [
            disnake.SelectOption(label="Bombeiro", emoji="<:1010304681005809684:1017958221840916540>"),
            disnake.SelectOption(label="Chefe de cozinha", emoji="<:1010304681005809684:1017958377554448465>"),
            disnake.SelectOption(label="Garçom", emoji="<:1010304681005809684:1017958636288475157>"),
            disnake.SelectOption(label="Jardineiro", emoji="<:1010304681005809684:1017958768547463259>"),
            disnake.SelectOption(label="Lixeiro", emoji="<:1010304681005809684:1017959078498156544>"),
            disnake.SelectOption(label="Manobrista", emoji="<:1010304681005809684:1017959187290017802>"),
            disnake.SelectOption(label="Médico", emoji="<:1010304681005809684:1017959368106455040>"),
            disnake.SelectOption(label="Motorista de ônibus", emoji="<:1010304681005809684:1017959735422631956>"),
            disnake.SelectOption(label="Piloto de avião", emoji="<:1010304681005809684:1017959870772826232>"),
            disnake.SelectOption(label="Policial", emoji="<:1010304681005809684:1017960243768078406>"),
            disnake.SelectOption(label="Programador", emoji="<:1010304681005809684:1017960439725953044>"),
            disnake.SelectOption(label="Uber", emoji="<:1010304681005809684:1017960606676033556>"),
            disnake.SelectOption(label="Vigia", emoji="<:1010304681005809684:1017961120792858624>")

        ]

        super().__init__(
            placeholder="Escolha um emprego",
            min_values=1,
            max_values=1,
            custom_id="work_select",
            options=options,
        )
    async def callback(self, interaction: disnake.MessageInteraction):
        try:
            await interaction.response.defer()
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT banco FROM eco WHERE user_id = ?", (interaction.author.id, ))
            wallet = cursor.fetchone()

            horas = random.randint(4, 16)
            if horas < 12:
                earnings = random.randint(400, 9000)
            if horas > 12:
                earnings = random.randint(500, 14000)
            if horas == 16:
                earnings = random.randint(8000, 16000)

            try:
                wallet = wallet[0]
            except:
                wallet = 0

            sql = ("UPDATE eco SET banco = ? WHERE user_id = ?")
            val = (wallet + int(earnings), interaction.author.id)
            cursor.execute(sql, val)

            embed = disnake.Embed(timestamp=datetime.datetime.utcnow(), color=interaction.author.color)
            embed.set_author(icon_url=interaction.author.avatar.url, name=interaction.author.name)
            embed.add_field(name=f"{work_emoji} | Você trabalhou como:", value=f"``{self.values[0]}``")
            embed.add_field(name=f"{clock_emoji} | Por:", value=f"``{horas}`` Horas", inline=False)
            embed.add_field(name=f"{manwithmoney_emoji} | E recebeu:", value=f"``{earnings}`` LabyCoins!", inline=False)
            embed.set_thumbnail(url=interaction.author.avatar.url)
            embed.set_footer(text=footer)
            await interaction.edit_original_message(embed=embed, view=None)
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)
        
class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

    async def interaction_check(self, interaction: disnake.Interaction):
        if interaction.author.mention not in interaction.message.embeds[0].description:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode utilizar esse painel! Caso queira trabalhar, use o comando ``/trabalhar``!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
        else:
            return True

class Acessar(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=20)
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

    @disnake.ui.button(label="Acessar", custom_id="acess_button", style=disnake.ButtonStyle.green)
    async def acess(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()

class Confirm(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=20)
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

    @disnake.ui.button(label="Sim, deletar!", emoji=confirm_emoji, custom_id="confirm_button_four", style=disnake.ButtonStyle.green)
    async def confirm5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()

    @disnake.ui.button(label="Melhor não...", emoji=error_emoji, custom_id="cancel_button_four", style=disnake.ButtonStyle.red)
    async def cancel5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = False
        self.stop()

class Accept(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=20)
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

    @disnake.ui.button(label="Transferir!", emoji=manwithmoney_emoji, custom_id="accept_transition", style=disnake.ButtonStyle.green)
    async def confirm6(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()

class Accept2(disnake.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
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

    @disnake.ui.button(label="Aceitar!", emoji=manwithmoney_emoji, custom_id="accept_apost", style=disnake.ButtonStyle.green)
    async def confirm6(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()
    
    @disnake.ui.button(label="Cancelar!", emoji=error_emoji, custom_id="cancel_apost", style=disnake.ButtonStyle.red)
    async def cancel5(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = False
        self.stop()

class Accept3(disnake.ui.View):
    def __init__(self, usuário):
        super().__init__(timeout=10)
        self.value = None
        self.ctx = usuário

    async def interaction_check(self, interaction: disnake.Interaction):
        if self.ctx != interaction.user:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas {self.ctx.mention} pode clicar nesse botão!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
            return False
        else:
            return True

    @disnake.ui.button(label="Aceitar!", emoji=manwithmoney_emoji, custom_id="accept_apost_two", style=disnake.ButtonStyle.green)
    async def confirm8(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = True
        self.stop()
    
    @disnake.ui.button(label="Não!", emoji=error_emoji, custom_id="cancel_apost_two", style=disnake.ButtonStyle.red)
    async def cancel7(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        self.value = False
        self.stop()


class Economia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.prepare_view())

    async def prepare_view(self):
        await self.bot.wait_until_ready()
        self.bot.add_view(DropdownView())
    
    # @commands.slash_command(description="「💳 Economia」Compre alguma coisa na minha loja!")
    # async def loja(self, ctx):
    #     try:
    #         embed = disnake.Embed(description="Seja bem-vindo(a) a minha loja! Escolha uma categoria de itens.", color=blurple_color, timestamp=datetime.datetime.utcnow())
    #         embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
    #         embed.set_footer(text=footer)
    #         await ctx.send(embed=embed, components=[disnake.ui.Button(label="Geral", custom_id="geral_item_button", style=disnake.ButtonStyle.blurple, row=1), disnake.ui.Button(label="Armas", custom_id="guns_item_button", style=disnake.ButtonStyle.blurple, row=1)],ephemeral=True)
    #     except Exception as e:
    #         print(e)
            
    # @commands.slash_command()
    # async def vender(self, ctx):
    #     return
    
    @commands.slash_command(description="「💳 Economia」Abra sua conta bancária e inicie sua jornada no mundo econômico!")
    async def abrir_conta(self, ctx):
        try:
            db = sqlite3.connect('eco.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (ctx.author.id, ))
            bal = cursor.fetchone()
            if bal is not None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você já possui uma conta bancária!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return

            view = Acessar(ctx=ctx)

            view1 = disnake.ui.View()
            item = disnake.ui.Button(label="Abrir avatar no navegador", style=disnake.ButtonStyle.blurple, url=ctx.author.avatar.url)
            view1.add_item(item=item)

            embed = disnake.Embed(description=f"{loading_emoji} | Criando conta...", color=yellow_color, timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=8)
            await asyncio.sleep(8)

            sql = ("INSERT INTO eco(user_id, carteira, banco) VALUES (?, ?, ?)")
            val = (ctx.author.id, 100, 0)
            cursor.execute(sql, val)
            db.commit()

            embed = disnake.Embed(description=f"{confirm_emoji} | Sua conta bancária foi criada com sucesso! Clique no botão abaixo para acessar sua conta.", color=green_color, timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
            embed.set_footer(text=footer)
            view.message = await ctx.send(embed=embed, view=view, delete_after=10)
            await view.wait()
            
            if view.value:
                db = sqlite3.connect('eco.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (ctx.author.id, ))
                bal = cursor.fetchone()

                embed = disnake.Embed(color=ctx.author.color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=ctx.author.avatar.url, name=f"Conta bancária de {ctx.author.name}")
                embed.add_field(name=f"{wallet_emoji} | Carteira:", value=f"``{bal[0]}`` LabyCoins")
                embed.add_field(name=f"{bank_emoji} | Banco:", value=f"``{bal[1]}`` LabyCoins", inline=False)
                embed.add_field(name=f"{coin_emoji} | Total:", value=f"``{bal[0] + bal[1]}`` LabyCoins", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar.url)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, view=view1)
                cursor.close()
                db.close()
                return
            else:
                await ctx.send("Para ver sua conta bancária utilize o comando ``/saldo``.", ephemeral=True)
        except Exception as e:
            print(e)
        
    @commands.slash_command(description="「💳 Economia」Delete sua conta bancária!")
    async def deletar_conta(self, ctx):
        try:
            db = sqlite3.connect('eco.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (ctx.author.id, ))
            bal = cursor.fetchone()
            view = Confirm(ctx=ctx)
            if bal is  None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            else:
                embed = disnake.Embed(title=f"{warning_emoji} | Espera aí!", description="Você realmente deseja deletar sua conta bancária? Você irá perder tudo! Tudo mesmo!", timestamp=datetime.datetime.utcnow(), color=yellow_color)
                embed.set_footer(text=footer)
                view.message = await ctx.send(embed=embed, view=view, delete_after=20)
                await view.wait()
                msg = await ctx.original_message()

                if view.value:
                    embed = disnake.Embed(description=f"{confirm_emoji} | Sua conta bancária foi deletada com sucesso! Você pode abrir uma nova conta a qualquer momento usando o comando ``/abrir_conta``.", timestamp=datetime.datetime.utcnow(), color=green_color)
                    embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
                    embed.set_footer(text=footer)
                    await msg.edit(embed=embed, view=None)
                    db = sqlite3.connect('eco.sqlite')
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM eco WHERE user_id = ?", (ctx.author.id, ))

                    db.commit()
                    cursor.close()
                    db.close()
                    return
                else:
                    await ctx.send("Que bom que você decidiu não apagar sua conta bancária! Mas caso realmente queira apagá-la, basta usar esse comando novamente. (``/deletar_conta``)", ephemeral=True)
                    await msg.delete()
        except Exception as e:
            print(e)
            # await ctx.send(e)
            # exc_type, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # await ctx.send(f"Classe: ``{exc_type}``\nArquivo: ``{fname}``\nLinha: ``{exc_tb.tb_lineno}``\nErro: {e}")

    @commands.slash_command(description="「💳 Economia」Mostra a sua conta bancária ou a de outro usuário", options=[Option("usuário", "Menção ou ID do usuário.", OptionType.user)])
    async def saldo(self, ctx, usuário: disnake.User = None):
        try:
            member = usuário if usuário else ctx.author  

            db = sqlite3.connect('eco.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (member.id, ))
            bal = cursor.fetchone()

            view2 = disnake.ui.View()
            item = disnake.ui.Button(label="Abrir avatar no navegador", style=disnake.ButtonStyle.blurple, url=member.avatar.url)
            view2.add_item(item=item)

            if member.bot:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"No meu banco, BOTs não possuem ter uma conta bancária.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            if member.id != ctx.author.id:
                if bal is None:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Este usuário não possui uma conta bancária.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    return
            if bal is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            embed = disnake.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=member.avatar.url, name=f"Conta bancária de {member.name}")
            embed.add_field(name=f"{wallet_emoji} | Carteira:", value=f"``{bal[0]}`` LabyCoins")
            embed.add_field(name=f"{bank_emoji} | Banco:", value=f"``{bal[1]}`` LabyCoins", inline=False)
            embed.add_field(name=f"{coin_emoji} | Total:", value=f"``{bal[0] + bal[1]}`` LabyCoins", inline=False)
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, view=view2)

            cursor.close()
            db.close()
        except Exception as e:
            exc_type, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Classe: ``{exc_type}``\nArquivo: ``{fname}``\nLinha: ``{exc_tb.tb_lineno}``\nErro: {e}")

    @commands.slash_command(description="「💳 Economia」Deposite uma quantia de dinheiro na sua conta bancária")
    async def depositar(self, ctx, quantia:int):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM eco WHERE user_id = ?", (ctx.author.id, ))
        data = cursor.fetchone()
        if data is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        try:
            carteira = data[1]
            banco = data[2]
        except:
            return
        if quantia == 0:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Não é possível depositar ``0`` LabyCoins!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if carteira == 0:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui dinheiro na sua carteira para ser depositado no seu banco.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if carteira < quantia:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui tudo isso de dinheiro na sua carteira!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        else:
            cursor.execute("UPDATE eco SET banco = ? WHERE user_id = ?", (banco + quantia, ctx.author.id))            
            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (carteira - quantia, ctx.author.id))
            embed = disnake.Embed(description=f"{deposit_emoji} | Você depositou ``{quantia}`` LabyCoins no seu banco com sucesso!", timestamp=datetime.datetime.utcnow(), color=0x00FF00)
            embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)

        db.commit()
        cursor.close()
        db.close()

    @commands.slash_command(description="「💳 Economia」Saque uma quantia de dinheiro da sua conta bancária")
    async def sacar(self, ctx, quantia:int):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM eco WHERE user_id = ?", (ctx.author.id, ))
        data = cursor.fetchone()
        if data is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        try:
            carteira = data[1]
            banco = data[2]
        except:
            return
        if quantia == 0:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode sacar ``0`` LabyCoins", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if banco == 0:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui dinheiro depositado no seu banco.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        if banco < quantia:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Sua conta bancária não possui tudo isso de dinheiro!", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return
        else:
            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (carteira + quantia, ctx.author.id))
            cursor.execute("UPDATE eco SET banco = ? WHERE user_id = ?", (banco - quantia, ctx.author.id))            
            embed = disnake.Embed(description=f"{withdraw_emoji} | Você sacou ``{quantia}`` LabyCoins do seu banco com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
            embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)
        
        db.commit()
        cursor.close()
        db.close()
    
    @commands.slash_command(description="「💳 Economia」Trabalhe para ganhar dinheiro!")
    @commands.cooldown(1, 28800, commands.BucketType.user)
    async def trabalhar(self, interaction: disnake.AppCommandInteraction):
        try:
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT banco FROM eco WHERE user_id = ?", (interaction.author.id, ))
            wallet = cursor.fetchone()
            if wallet is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
                interaction.application_command.reset_cooldown(interaction)
                return
            view = DropdownView()

            embed = disnake.Embed(description=f"||{interaction.user.mention}|| Escolha um emprego:", color=yellow_color, timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=interaction.author.avatar.url, name=interaction.author.name)
            embed.set_footer(text=footer)
            await interaction.response.send_message(embed=embed, view=view)


            cursor.close()
            db.close()
        except Exception as e:
            print(e)

    @commands.slash_command(description="「💳 Economia」Colete seu prêmio diário e ganhe LabyCoins!")
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, interaction: disnake.AppCommandInteraction):
        try:
            daily = random.randint(1500, 3500)

            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT banco FROM eco WHERE user_id = ?", (interaction.author.id, ))
            wallet = cursor.fetchone()
            if wallet is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await interaction.response.send_message(embed=ErrorEmbed, ephemeral=True)
                interaction.application_command.reset_cooldown(interaction)
                return
            try:
                wallet = wallet[0]
            except:
                wallet = 0                
            if interaction.guild.id == 892799472478871613:
                sql = ("UPDATE eco SET banco = ? WHERE user_id = ?")
                val = (wallet + int(daily*2), interaction.author.id)
                cursor.execute(sql, val)

                embed = disnake.Embed(timestamp=datetime.datetime.utcnow(), color=interaction.author.color)
                embed.set_author(icon_url=interaction.author.avatar.url, name=f"Prêmio diário de {interaction.author.name}")
                embed.add_field(name=f"{manwithmoney_emoji} | Prêmio de hoje:", value=f"``{daily*2}`` LabyCoins")
                embed.add_field(name=f"{bank_emoji} | Dinheiro no banco:", value=f"``{wallet + daily*2}`` LabyCoins", inline=False)
                embed.set_footer(text=footer)
                await interaction.response.send_message(f"Parabéns, hoje você ganhou ``{daily*2}`` LabyCoins! Você iria ganhar ``{daily}`` LabyCoins, mas meu servidor possui LabyCoins em dobro no daily! O dinheiro foi depositado em seu banco.", embed=embed)
                return

            sql = ("UPDATE eco SET banco = ? WHERE user_id = ?")
            val = (wallet + int(daily), interaction.author.id)
            cursor.execute(sql, val)

            embed = disnake.Embed(timestamp=datetime.datetime.utcnow(), color=interaction.author.color)
            embed.set_author(icon_url=interaction.author.avatar.url, name=f"Prêmio diário de {interaction.author.name}")
            embed.add_field(name=f"{manwithmoney_emoji} | Prêmio de hoje:", value=f"``{daily}`` LabyCoins")
            embed.add_field(name=f"{bank_emoji} | Dinheiro no banco:", value=f"``{wallet + daily}`` LabyCoins", inline=False)
            embed.set_thumbnail(url=interaction.user.avatar.url)
            embed.set_footer(text=footer)
            await interaction.response.send_message(f"Parabéns, hoje você ganhou ``{daily}`` LabyCoins! O dinheiro foi depositado em seu banco. Caso queira LabyCoins em dobro, entre no meu servidor utilizando o comando ``/servidor``!", embed=embed)

            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)
    
    @commands.slash_command(description="「💳 Economia」Faça uma aposta com outro usuário!", options=[Option("usuário", "Menção ou ID do usuário", OptionType.user, required=True), Option("quantia", "Quantia que o usuário irá receber", required=True)])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def apostar(self, ctx, usuário: disnake.Member, quantia:int):
        try:
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (usuário.id, ))
            data1 = cursor.fetchone()

            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (ctx.author.id, ))
            data2 = cursor.fetchone()
                
            try:
                money2 = data1[0]
                money = data2[0]
                if money == 0:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui dinheiro na sua carteira.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
                if money < int(quantia):
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui ``{quantia}`` LabyCoins na sua carteira!", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
                if money2 == 0:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{usuário.mention} não possui dinheiro na carteira.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
                if usuário.id != ctx.author.id:
                    if money2 < int(quantia):
                        ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{usuário.mention} não possui ``{quantia}`` LabyCoins na carteira.", timestamp=datetime.datetime.utcnow(), color=red_color)
                        ErrorEmbed.set_footer(text=footer)
                        await ctx.send(embed=ErrorEmbed, ephemeral=True)
                        ctx.application_command.reset_cooldown(ctx)
                        return
            except Exception as e:
                print(e)

            cursor.execute(f"SELECT user_id FROM eco WHERE user_id = ?", (ctx.author.id, ))
            data3 = cursor.fetchone()
            
            cursor.execute(f"SELECT user_id FROM eco WHERE user_id = ?", (usuário.id, ))
            data4 = cursor.fetchone()
            
            if data3 is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if usuário.id != ctx.author.id:
                if data4 is None:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Este usuário não possui uma conta bancária.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
            if usuário.id == ctx.author.id:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode apostar com você mesmo!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if int(quantia) < 5:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode apostar menos de ``5`` LabyCoins!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            else:
                view = Accept2(ctx=ctx)
                embed = disnake.Embed(title="Confirmação", description=f"Você realmente deseja apostar ``{quantia}`` LabyCoins com {usuário.mention}?", color=yellow_color, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text=footer)
                view.message = await ctx.send(content=ctx.author.mention, embed=embed, view=view, delete_after=10)
                await view.wait()
                msg = await ctx.original_message()
                if view.value is None:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
                if view.value:
                    await msg.delete()
                    view2 = Accept3(usuário=usuário)
                    embed = disnake.Embed(title="Confirmação", description=f"Você realmente deseja apostar ``{quantia}`` LabyCoins com {ctx.author.mention}?", color=yellow_color, timestamp=datetime.datetime.utcnow())
                    embed.set_footer(text=footer)
                    view2.message = await ctx.send(content=usuário.mention, embed=embed, view=view2, delete_after=10)
                    await view2.wait()
                    if view2.value is None:
                        ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
                        ErrorEmbed.set_footer(text=footer)
                        await ctx.send(content=usuário.mention, embed=ErrorEmbed, delete_after=8)
                        ctx.application_command.reset_cooldown(ctx)
                        return
                    if view2.value:
                        user = ctx.author, usuário	
                        winner = random.choice(user)
                        if winner == ctx.author:
                            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (money2 - int(quantia), usuário.id, ))
                            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (money + int(quantia), ctx.author.id, )) 
                        if winner == usuário:
                            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (money2 + int(quantia), usuário.id, ))
                            cursor.execute("UPDATE eco SET carteira = ? WHERE user_id = ?", (money - int(quantia), ctx.author.id, )) 
                        
                        embed = disnake.Embed(color=green_color, timestamp=datetime.datetime.utcnow())
                        embed.set_author(icon_url=winner.avatar.url, name=winner.name)
                        embed.add_field(name="Vencedor:", value=winner.mention)
                        embed.add_field(name="Prêmio:", value=f"``{quantia}`` LabyCoins, parabéns!", inline=False)
                        embed.set_thumbnail(url=winner.avatar.url)
                        embed.set_footer(text=footer)
                        await ctx.send(embed=embed)

                        #await ctx.send(f"{var.mention} ganhou ``{quantia}`` LabyCoins")
                    else:
                        ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Aposta cancelada!", description=f"Você cancelou a aposta com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
                        ErrorEmbed.set_footer(text=footer)
                        await ctx.send(embed=ErrorEmbed, ephemeral=True)
                        await ctx.send(f"{ctx.author.mention}, o usuário em que você quis apostar arregou e saiu correndo!")
                        ctx.application_command.reset_cooldown(ctx)
                        return
                else:
                    ErrorEmbed = disnake.Embed(title=f"{confirm_emoji} | Aposta cancelada!", description=f"Você cancelou a aposta com sucesso!", timestamp=datetime.datetime.utcnow(), color=green_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    await msg.delete()
                    ctx.application_command.reset_cooldown(ctx)
                    return

                db.commit()
                cursor.close()
                db.close()
                return
        except Exception as e:
            print(e)


    @commands.slash_command(description="「💳 Economia」Faça um pix para um usuário!", options=[Option("usuário", "Menção ou ID do usuário.", OptionType.user, required=True), Option("quantia", "Quantia que o usuário irá receber", required=True)])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def pix(self, ctx, usuário: disnake.Member, quantia:int):
        try:
            #member = usuário if usuário else ctx.author  

            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (usuário.id, ))
            data1 = cursor.fetchone()

            cursor.execute(f"SELECT carteira, banco FROM eco WHERE user_id = ?", (ctx.author.id, ))
            data2 = cursor.fetchone()
            
            try:
                money2 = data1[1]
                money = data2[1]
            except Exception as e:
                print

            cursor.execute(f"SELECT user_id FROM eco WHERE user_id = ?", (ctx.author.id, ))
            data3 = cursor.fetchone()
            
            cursor.execute(f"SELECT user_id FROM eco WHERE user_id = ?", (usuário.id, ))
            data4 = cursor.fetchone()
            
            if data3 is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui um conta bancária! Por favor, utilize o comando ``/abrir_conta`` caso queira criar uma.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if usuário.id != ctx.author.id:
                if data4 is None:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Este usuário não possui uma conta bancária.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
            if usuário.id == ctx.author.id:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode fazer um pix para você mesmo!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if int(quantia) < 5:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode fazer um pix de menos de ``5`` LabyCoins!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if money == 0:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui dinheiro depositado no seu banco.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            if money < int(quantia):
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não possui ``{quantia}`` LabyCoins depositados no seu banco!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                ctx.application_command.reset_cooldown(ctx)
                return
            else:
                view = Accept(ctx=ctx)
                embed = disnake.Embed(title="Confirmação", description=f"Você realmente deseja transferir ``{quantia}`` LabyCoins para {usuário.mention}?", color=yellow_color, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text=footer)
                view.message = await ctx.send(embed=embed, view=view)
                await view.wait()
                msg = await ctx.original_message()

                if view.value is None:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
                    ctx.application_command.reset_cooldown(ctx)
                    return
                if view.value:
                    view1 = disnake.ui.View()
                    item = disnake.ui.Button(label="Clique aqui para ir a mensagem!", style=disnake.ButtonStyle.blurple, url=msg.jump_url)
                    view1.add_item(item=item)

                    cursor.execute("UPDATE eco SET banco = ? WHERE user_id = ?", (money2 + int(quantia), usuário.id, ))
                    cursor.execute("UPDATE eco SET banco = ? WHERE user_id = ?", (money - int(quantia), ctx.author.id, ))     
                    # data2 = cursor.fetchone()       
                    # print(data2)
                    embed = disnake.Embed(description=f"{coin_emoji} | Você fez um pix de ``{quantia}`` LabyCoins para {usuário.mention}!", timestamp=datetime.datetime.utcnow(), color=green_color)
                    embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.author.name)
                    embed.set_footer(text=footer)
                    if int(quantia) < 90:
                        embed2 = disnake.Embed(description=f"O usuário {ctx.author.mention} fez um pix de ``{quantia}`` LabyCoins para você, não é muito, mas lembre-se, uma quantia pequena de dinheiro pode mudar a vida de qualquer um!", color=green_color, timestamp=datetime.datetime.utcnow())
                        embed2.set_author(icon_url=usuário.avatar.url, name=usuário.name)
                        embed2.set_footer(text=footer)
                        await msg.edit(embed=embed, view=None)
                        await usuário.send(embed=embed2, view=view1)
                    else:
                        embed3 = disnake.Embed(description=f"O usuário {ctx.author.mention} fez um pix de ``{quantia}`` LabyCoins para você, tá rico hein!", color=green_color, timestamp=datetime.datetime.utcnow())
                        embed3.set_author(icon_url=usuário.avatar.url, name=usuário.name)
                        embed3.set_footer(text=footer)
                        await msg.edit(embed=embed, view=None)
                        await usuário.send(embed=embed3, view=view1)                        

                db.commit()
                cursor.close()
                db.close()
                return
        except Exception as e:
            print(e)

    # @commands.slash_command()
    # async def caçar(self, ctx):
    #     horas = [2, 3, 4, 5]
    #     lista_de_animais = [None, "🦊 Raposas", "🐺 Lobos", "🦝 Guaxinims", "🐯 Tigres", "🦁 Leãos", "🐆 Leopardos", "🦓 Zebras", "🦌 Cervos", "🐍 Cobras", "🐸 Sapos", "🦛 Hipopótamos"]

    #     db = sqlite3.connect("eco.sqlite")
    #     cursor = db.cursor()

    #     cursor.execute(f"SELECT * FROM animais WHERE user_id = {ctx.author.id}")
    #     animais = cursor.fetchone()
        
    #     cursor.execute(f"SELECT pistola FROM ferramentas WHERE user_id = {ctx.author.id}")
    #     pistola = cursor.fetchone()

    #     quantia = random.randrange(11)
    #     caçada = random.choice(lista_de_animais)

    #     if pistola[0] > 0:
    #         if caçada == lista_de_animais[1]:
    #             cursor.execute(f"UPDATE animais SET raposa = ? WHERE user_id = ?", (animais[1] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[2]:
    #             cursor.execute(f"UPDATE animais SET lobo = ? WHERE user_id = ?", (animais[2] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[3]:
    #             cursor.execute(f"UPDATE animais SET guaxinim = ? WHERE user_id = ?", (animais[3] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[4]:
    #             cursor.execute(f"UPDATE animais SET tigre = ? WHERE user_id = ?", (animais[4] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[5]:
    #             cursor.execute(f"UPDATE animais SET leão = ? WHERE user_id = ?", (animais[5] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[6]:
    #             cursor.execute(f"UPDATE animais SET leopardo = ? WHERE user_id = ?", (animais[6] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[7]:
    #             cursor.execute(f"UPDATE animais SET zebra = ? WHERE user_id = ?", (animais[7] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[8]:
    #             cursor.execute(f"UPDATE animais SET cervo = ? WHERE user_id = ?", (animais[8] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[9]:
    #             cursor.execute(f"UPDATE animais SET sapo = ? WHERE user_id = ?", (animais[9] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[10]:
    #             cursor.execute(f"UPDATE animais SET hipopótamo = ? WHERE user_id = ?", (animais[10] + quantia, ctx.author.id))
    #         if caçada == lista_de_animais[0]:
    #             cursor.execute(f"UPDATE ferramentas SET pistola = ? WHERE user_id = ?", (pistola[0] - 1, ctx.author.id))
    #             await ctx.send(f"Você saiu para caçar por {random.choice(horas)} horas e infelizmente não conseguiu nada! Mais sorte na próxima vez.")
    #             return
    #         cursor.execute(f"UPDATE ferramentas SET pistola = ? WHERE user_id = ?", (pistola[0] -1, ctx.author.id))
    #         await ctx.send(f"Você saiu para caçar por {random.choice(horas)} horas e caçou ``{quantia}`` **{caçada}**!")
    #     else:
    #         await ctx.send("Você precisa de uma pistola para realizar uma caçada!")
        
    #     db.commit()
    #     cursor.close()
    #     db.close()
    
    # @commands.slash_command()
    # async def inventário(self, ctx):
    #     lista_de_animais = [None, "🦊 Raposa", "🐺 Lobo", "🦝 Guaxinim", "🐯 Tigre", "🦁 Leão", "🐆 Leopardo", "🦓 Zebra", "🦌 Cervo", "🐍 Cobra", "🐸 Sapo", "🦛 Hipopótamo", "🐊 Jacaré", "🐑 Ovelha", "🦨 Gambá"]
    #     lista_de_ferramentas = [None, "🔫 Pistola", "🏹 Arco", "🗡 Lança"]
        
    #     db = sqlite3.connect("eco.sqlite")
    #     cursor = db.cursor()

    #     cursor.execute(f"SELECT * FROM animais WHERE user_id = {ctx.author.id}")
    #     animais = cursor.fetchone()

    #     cursor.execute(f"SELECT * FROM ferramentas WHERE user_id = {ctx.author.id}")
    #     ferramentas = cursor.fetchone()
        
    #     animais_ = [f"{i} x{j}" for i, j in itertools.zip_longest(lista_de_animais, animais) if j > 0 and j < 10000000000000]
    #     ferramentas_ = [f"{i} x{j}" for i, j in itertools.zip_longest(lista_de_ferramentas, ferramentas) if j > 0 and j < 1000000000000]

    #     animais_ = "\n".join(animais_) if len(animais_) > 0 else "Nenhum animal no inventário."
    #     ferramentas_ = "\n".join(ferramentas_) if len(ferramentas_) > 0 else "Nenhuma ferramenta no inventário."

    #     embed = disnake.Embed(title="Seu inventário", description="Tudo que você coletou na sua jornada", color=ctx.author.color)
    #     embed.add_field(name="Animais:", value=animais_)
    #     embed.add_field(name="Ferramentas:", value=ferramentas_)
    #     await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Economia(bot))