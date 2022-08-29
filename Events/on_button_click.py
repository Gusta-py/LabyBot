from Commands.utils import generate_puzzle_embed, random_puzzle_id
from Config.colors import red_color, green_color, blurple_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onButtonClick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Atualizações``\nID customizável: ``updates_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo1.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo1)

                await interaction.response.send_message(f"O cargo {cargo1.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Atualizações``\nID customizável: ``updates_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo1.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)


        if interaction.data.custom_id == "partners_button":
            if cargo2 not in interaction.author.roles:
                await interaction.author.add_roles(cargo2)

                await interaction.response.send_message(f"O cargo {cargo2.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Parcerias``\nID customizável: ``partners_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo2.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo2)

                await interaction.response.send_message(f"O cargo {cargo2.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Parcerias``\nID customizável: ``partners_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo2.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "status_button":
            if cargo3 not in interaction.author.roles:
                await interaction.author.add_roles(cargo3)

                await interaction.response.send_message(f"O cargo {cargo3.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Status``\nID customizável: ``status_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo3.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo3)

                await interaction.response.send_message(f"O cargo {cargo3.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Status``\nID customizável: ``status_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo3.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)
        
        #Cargos de gênero

        if interaction.data.custom_id == "he_button":
            if cargo4 not in interaction.author.roles:
                await interaction.author.add_roles(cargo4)

                await interaction.response.send_message(f"O cargo {cargo4.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Ele``\nID customizável: ``he_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo4.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo4)

                await interaction.response.send_message(f"O cargo {cargo4.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Ele``\nID customizável: ``he_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo4.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "not_binary_button":
            if cargo5 not in interaction.author.roles:
                await interaction.author.add_roles(cargo5)

                await interaction.response.send_message(f"O cargo {cargo5.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Não binário``\nID customizável: ``not_binary_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo5.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo5)

                await interaction.response.send_message(f"O cargo {cargo5.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Não binário``\nID customizável: ``not_binary_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo5.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "she_button":
            if cargo6 not in interaction.author.roles:
                await interaction.author.add_roles(cargo6)

                await interaction.response.send_message(f"O cargo {cargo6.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Ela``\nID customizável: ``she_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo6.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo6)

                await interaction.response.send_message(f"O cargo {cargo6.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``Ela``\nID customizável: ``she_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo6.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        #Cargos de idade

        if interaction.data.custom_id == "13_16_button":
            if cargo7 not in interaction.author.roles:
                await interaction.author.add_roles(cargo7)

                await interaction.response.send_message(f"O cargo {cargo7.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``13-16 Anos``\nID customizável: ``13_16_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo7.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo7)

                await interaction.response.send_message(f"O cargo {cargo7.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``13-16 Anos``\nID customizável: ``13_16_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo7.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "17_21_button":
            if cargo8 not in interaction.author.roles:
                await interaction.author.add_roles(cargo8)

                await interaction.response.send_message(f"O cargo {cargo8.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``17-21 Anos``\nID customizável: ``17_21_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo8.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo8)

                await interaction.response.send_message(f"O cargo {cargo8.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``17-21 Anos``\nID customizável: ``17_21_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo8.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        if interaction.data.custom_id == "22+_button":
            if cargo9 not in interaction.author.roles:
                await interaction.author.add_roles(cargo9)

                await interaction.response.send_message(f"O cargo {cargo9.mention} foi adicionado em você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``22+``\nID customizável: ``22+_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo9.mention} adicionado.", color=green_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                await logs.send(embed=embed)
            else:
                await interaction.author.remove_roles(cargo9)

                await interaction.response.send_message(f"O cargo {cargo9.mention} foi removido de você com sucesso!", ephemeral=True)

                embed = disnake.Embed(description=f"Usuário: {interaction.author.mention} (``{interaction.author.id}``)\nCanal: {interaction.channel.id}\nBotão: ``22+``\nID customizável: ``22+_button``\n\nDescrição:\nO membro {interaction.author.mention} e teve o cargo {cargo9.mention} removido.", color=red_color, timestamp=datetime.datetime.utcnow())
                embed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                embed.set_footer(text=footer)
                await logs.send(embed=embed)

        #Comando termo:

        if interaction.data.custom_id == "how_to_play_blurple":
            await interaction.response.send_message("As instruções foram enviados para sua DM.", ephemeral=True)
            embed = disnake.Embed(title="Como jogar", description="Descubra a palavra correta em ``6`` tentativas. A cada tentativa, as peças mostram o quão perto você está da palavra certa. Exemplo:\n\n<:1000176813236043877:1000177693574299759><:1000176813236043877:1000179029648887958><:1000176813236043877:1000179559880196197><:1000176813236043877:1000179138008711251><:1000176813236043877:1000179255319212106>\n\nA letra <:1000176813236043877:1000177693574299759> faz parte da palavra e está na posição correta.\n\n<:1000176813236043877:1000179075815591957><:1000176813236043877:1000179029648887958><:1000181470096269403:1000182084935106692><:1000176813236043877:1000179053690626138><:1000176813236043877:1000179465189601320>\n\nA letra <:1000181470096269403:1000182084935106692> faz parte da palavra mas em outra posição.\n\n<:1000176813236043877:1000178124862005258><:1000176813236043877:1000177645947998348><:1000176813236043877:1000178101407457370><:1000176813236043877:1000178124862005258><:1000176813236043877:1000179465189601320>\n\n A letra <:1000176813236043877:1000179465189601320> não faz parte da palavra.\n\nAo contrário do jogo original, os acentos não são preenchidos automaticamente, pois não há **nenhuma** palavra com acentos e você pode jogar quando quiser! Em vez de poder jogar uma vez por dia.\n\nAs palavras podem possuir letras repetidas e para responder, basta dar reply na mensagem.", timestamp=datetime.datetime.utcnow(), color=0xfafafa)
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(text=footer)
            await interaction.author.send(embed=embed, delete_after=120)
        if interaction.data.custom_id == "start_game_green":
            puzzle_id = random_puzzle_id()
            embed = generate_puzzle_embed(interaction.author, puzzle_id)
            await interaction.response.edit_message(view=None)
            await interaction.followup.send("O jogo foi iniciado!", delete_after=5)
            await interaction.followup.send("Para responder, basta dar reply na mensagem.",embed=embed)
            return
    
  
def setup(bot):
    bot.add_cog(onButtonClick(bot))