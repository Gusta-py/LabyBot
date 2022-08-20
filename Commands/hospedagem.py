from Config.emojis import error_emoji, confirm_emoji, userinfo_emoji, owner_emoji, terminal_emoji, host_emoji, memory_emoji, restart_emoji
from Config.discloud import api_token, discloud_link, discloudsite_link, discloudapp_link, discloudlogs_link, discloudrestart_link
from Config.colors import red_color, blurple_color, white_color, black_color, yellow_color, green_color
from Config.images import discloudbanner_image, discloudlogo_image
from translate import Translator
from disnake.ext import commands
from Config.bot import footer
import datetime
import requests
import asyncio
import disnake


token = api_token


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

    @disnake.ui.button(label="Tudo ok, reiniciar!", emoji=confirm_emoji, custom_id="confirm_button_two", style=disnake.ButtonStyle.green)
    async def confirm3(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()


class Host(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        #self.bot.restart = self.bot.loop.create_task(self.restart())


    @commands.slash_command(description="「🛠 Hospedagem」Seu bot 24h online agora!")
    @commands.guild_only()
    async def discloud(self, ctx):
        view1 = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Discord", url=discloud_link)
        view1.add_item(item=item)

        item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Website", url=discloudsite_link)
        view1.add_item(item=item)

        DiscloudEmbed = disnake.Embed(title="Discloud", description="Seu bot **24h** online agora!", timestamp=datetime.datetime.utcnow(), color=blurple_color)
        DiscloudEmbed.add_field(name="O que é a Discloud?", value="A Discloud é uma host feita para bots que nasceu com a vontade de oferecer hospedagem fácil, gratuita e de qualidade para bots do Discord, beneficiando centenas de pessoas através dos seus serviços gratuitos à mais de 3 anos, hoje a plataforma mantém mais de ``1000`` Bots online e tudo isso é graças à sua ótima equipe de moderação, colaboração e carinho dos doadores.")
        DiscloudEmbed.add_field(name="<:905914689442160700:929848185575329833> Recursos:", value="─ Integração › DisCloud-API & GITHUB/GITLAB\n─ Time › 24/7\n─ Backup › Rápido & Fácil\n─ Flexibilidade › Rapidez & Controle\n─ Suporte › Português / Inglês", inline=False)
        DiscloudEmbed.set_image(url=discloudbanner_image)
        DiscloudEmbed.set_thumbnail(url=discloudlogo_image)
        DiscloudEmbed.set_footer(text=footer)

        await ctx.send(embed=DiscloudEmbed, view=view1)

    @commands.slash_command(description="「🛠 Hospedagem」Veja os status e algumas informações do bot")
    @commands.guild_only()
    async def status(self, interaction: disnake.AppCommandInteraction, escolhas: str = commands.Param(choices=[disnake.OptionChoice(name="Aplicação", value="app"), disnake.OptionChoice(name="Logs (Apenas moderadores do LabyBot)", value="logs"), disnake.OptionChoice(name="Usuário (Apenas dono)", value="user")])):
        if (escolhas == 'app'):
            await interaction.response.defer()

            bot = requests.get(discloudapp_link, headers={"api-token": token}).json()
            cpu = bot["cpu"]
            ram = bot["memory"]
            restart = bot["last_restart"]
            translator= Translator(to_lang="pt")
            translation = translator.translate(restart)

            StatusEmbed = disnake.Embed(title=f"Opa {interaction.author.name}! Veja aqui as minhas informações.", description=f'{userinfo_emoji} | Nome/ID: **LabyBot#3926/908870304909115432**\n{host_emoji} | CPU: **{cpu}**\n{memory_emoji} | RAM: **{ram}**\n{restart_emoji} | Última reinicialização: **Há {translation}**', timestamp=datetime.datetime.utcnow(), color=white_color)
            StatusEmbed.set_thumbnail(url=self.bot.user.avatar.url)
            StatusEmbed.set_footer(text=footer)
            await interaction.followup.send(embed=StatusEmbed)

        if (escolhas == 'logs'):
            await interaction.response.defer(ephemeral=True)

            logs = requests.get(discloudlogs_link, headers={"api-token": token}).json()
            complete = logs["link"]
            texto = logs["logs"]
            whitelist = [892802037186711553, 937052487427440760, 916716814627667979, 936738889744416798]
            tem = disnake.utils.find(lambda r: r.id in whitelist, interaction.author.roles)

            if tem: 
                v = disnake.ui.View()
                item = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label="Terminal completo", emoji=terminal_emoji, url=complete)
                v.add_item(item=item)

                LogsEmbed = disnake.Embed(title=f"{terminal_emoji} | Últimos 1800 caracteres do terminal:", description=f"```json\n{texto}```", timestamp=datetime.datetime.utcnow(), color=black_color)
                LogsEmbed.set_footer(text=footer)
                await interaction.followup.send(embed=LogsEmbed, view=v, ephemeral=True)
            else:
                if interaction.guild.id == 892799472478871613:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem o cargo necessário para utilizar esse comando!", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await interaction.followup.send(embed=ErrorEmbed, ephemeral=True)
                else:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas certas pessoas do meu servidor que podem utilizar esse comando!", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await interaction.followup.send(embed=ErrorEmbed, ephemeral=True)
            
        if (escolhas == 'user'):
            await interaction.response.defer(ephemeral=True)
            if interaction.author.id == 901498839981236235:
                embed = disnake.Embed(title=f"{userinfo_emoji} | Informações do seu plano", description=f"{owner_emoji} | Plano: ``Free``\n<:892799472478871613:916835300213403699> | Tempo restante: ``∞``.", timestamp=datetime.datetime.utcnow(), color=white_color)
                embed.set_footer(text=footer)
                await interaction.followup.send(embed=embed, ephemeral=True)
            else:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas o dono do bot pode ver essa categoria!", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await interaction.followup.send(embed=ErrorEmbed, ephemeral=True)
                return
            #userinfo = requests.get(disclouduser_link, headers={"api-token": token}).json()
            #plano = userinfo["plan"]
            #tempo_dias = userinfo['lastDataLeft']['days']
            #tempo_horas = userinfo['lastDataLeft']['hours']

            #if interaction.author.id == 901498839981236235:
                #embed = disnake.Embed(title=f"{userinfo_emoji} | Informações do seu plano", description=f"{owner_emoji} | Plano: ``{plano}``\n<:892799472478871613:916835300213403699> | Tempo restante: ``{tempo_dias}`` dias e ``{tempo_horas}`` horas.", timestamp=datetime.datetime.utcnow(), color=white_color)
                #embed.set_footer(text=footer)
                #await interaction.followup.send(embed=embed, ephemeral=True)
            #else:
                #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Apenas o dono do bot pode ver essa categoria!", timestamp=datetime.datetime.utcnow(), color=0xFF0000)
                #ErrorEmbed.set_footer(text=footer)
                #await interaction.followup.send(embed=ErrorEmbed, ephemeral=True)
                #return

    @commands.slash_command(guild_ids=[892799472478871613], description="「🛠 Host/Dono」Reinicia o bot")
    @commands.guild_only()
    async def restart(self, ctx):
        whitelist = [892802037186711553, 937052487427440760, 916716814627667979, 936738889744416798]
        tem = disnake.utils.find(lambda r: r.id in whitelist, ctx.author.roles)
        if tem: 
            channel = self.bot.get_channel(994313419509481472)

            ConfirmEmbed = disnake.Embed(title="Confirmação", description=f"Antes de reiniciar o bot, verifique se há alguma sugestão para ser aprovada ou negada no canal <#994666954243723324>. Caso tenha, por favor aprove ou negue o mesmo.", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            ConfirmEmbed.set_footer(text=footer)
            view = Confirm(ctx)
            view.message = await ctx.send(embed=ConfirmEmbed, view=view)
            await view.wait()
            msg = await ctx.original_message()

            if view.value is None:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O tempo foi esgotado.", timestamp=datetime.datetime.utcnow(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(ctx.author.mention, embed=ErrorEmbed, ephemeral=True)
                await msg.delete()

            elif view.value:
                await msg.delete()
                await asyncio.sleep(2)
                await ctx.send("O bot foi reiniciado com sucesso!")

                embed = disnake.Embed(title="Sistema reiniciado!", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.add_field(name="Quem reiniciou o bot?", value=f"{ctx.author.mention} | ``{ctx.author.id}``", inline=False)
                embed.add_field(name="Reiniciado com sucesso?", value="``Sim``", inline=False)
                embed.set_thumbnail(url=self.bot.user.avatar.url)
                embed.set_footer(text=footer)

                msg2 = await channel.send(embed=embed)

            try:
                result = requests.post(discloudrestart_link, headers={"api-token": token}).json()
            except Exception as e:
                print(e)

            if result:
                await msg.edit("Ocorreu um erro ao reiniciar o bot.")

                embed = disnake.Embed(title="Falha ao reiniciar o sistema!", timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.add_field(name="Quem tentou reiniciar o bot?", value=f"{ctx.author.mention} | ``{ctx.author.id}``", inline=False)
                embed.add_field(name="Reiniciado com sucesso?", value="``Não``", inline=False)
                embed.set_thumbnail(url=self.bot.user.avatar.url)
                embed.set_footer(text=footer)

                await msg2.edit(embed=embed)
       

    #@commands.slash_command(description="「🛠 Host/dono」Sincroniza o timer do bot com a discloud")
    #async def resync(self, ctx):
        #if ctx.author.id == 901498839981236235:
            #self.bot.restart.cancel()
            #self.bot.restart = self.bot.loop.create_task(self.restart())
            #embed = disnake.Embed(title="Sincronizado com sucesso!", description="O tempo de desligamento do bot foi sincronizado com a ``discloud`` com sucesso!", timestamp=datetime.datetime.utcnow(), color=0x5865F2)
            #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/905914689442160703/929484641847640157/discloud.png")
            #embed.set_footer(text=footer)
        #else:
            #ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} apenas o dono do bot pode utilizar esse comando!", color=0xFF0000)
            #await ctx.send(embed=ErrorEmbed)
        #return

def setup(bot):
    bot.add_cog(Host(bot))