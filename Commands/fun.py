from Config.emojis import error_emoji, text_channel_emoji, arrow_left, arrow_right, coincrown_emoji, coinface_emoji
from Config.colors import red_color, green_color, white_color, yellow_color, purple_color
from Commands.utils import generate_puzzle_embed, random_puzzle_id
from Config.links import openweather_link
from disnake import Option, OptionType
from disnake.ext import commands
from Config.bot import footer
from typing import List
import datetime
import requests
import asyncio
import disnake
import random
import time


lista_cancela = ["ser lindo(a) demais", "ser ruim", "ser gado(a) demais", "ser feio(a) demais", "ser gostoso(a) de mais", "ser bom(a)"]
crystall_list = ["Vai incomodar outra pessoa, obrigado.", "Não.", "Sim.", "Claro que não!", "Claro que sim!", "Talvez...", "Será?", "Provavelmente.", "Claro que é po.", "Claro que não po."]
url = openweather_link


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

class Feedback(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @disnake.ui.button(label="🟢 Bom",custom_id="feedback_green_button", style=disnake.ButtonStyle.green)
    async def bom(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

    @disnake.ui.button(label="🟡 Mais ou menos", custom_id="feedback_grey_button", style=disnake.ButtonStyle.grey)
    async def mais_ou_menos(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()
    
    @disnake.ui.button(label="🔴 Ruim", custom_id="feedback_red_button", style=disnake.ButtonStyle.red)
    async def ruim(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()
    
class Pegar(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        self.value = None

    @disnake.ui.button(label="Pegar café",custom_id="take_coffe_green_button", style=disnake.ButtonStyle.green)
    async def pegar(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.value = True
        self.stop()

#class Apagar(disnake.ui.View):
    #def __init__(self):
        #super().__init__(timeout=300)
        #self.value = None

    #@disnake.ui.button(label="Apagar mensagem", emoji="<:lixo:924690705539006514>", custom_id="delete_how_to_play_button", style=disnake.ButtonStyle.grey)
    #async def delete2(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        #await interaction.response.defer()
        #self.value = True
        #self.stop()


class Diversão(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="「😂 Diversão」Jogue Termo, só que no Discord 😈")
    async def termo(self, interaction: disnake.AppCommandInteraction):
        embed = disnake.Embed(title="Termo, só que no Discord", description="Antes de jogar, você só precisa seguir uma regrinha: A palavra que você colocar **NÃO** pode possuir nenhuma letra em **__caixa alta__** **(Caps Lock)**, caso contrário, o bot irá falar que ela é uma palavra inválida.", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.set_thumbnail(url=interaction.author.avatar.url)
        embed.set_footer(text=footer)
        await interaction.response.send_message(embed=embed, components=[disnake.ui.Button(label="Ok, iniciar!", custom_id="initiate_game_green", style=disnake.ButtonStyle.green), disnake.ui.Button(label="Como jogar", custom_id="how_to_play_blurple", style=disnake.ButtonStyle.blurple), disnake.ui.Button(label="Link do jogo original", url=f"https://term.ooo/")])

    @commands.slash_command(description="「😂 Diversão」Hora do café!")
    async def cafe(self, ctx):
        view = Feedback()
        view1 = Pegar()

        CaféEmbed = disnake.Embed(title="Hora do café! ☕", description=f"Aguarde {ctx.author.mention}! O seu café está sendo preparado.", timestamp=datetime.datetime.now(), color=yellow_color)
        CaféEmbed.set_footer(text=footer)
        await ctx.send(embed=CaféEmbed)
        msg = await ctx.original_message()

        await asyncio.sleep(5)

        CaféEmbed2 = disnake.Embed(title=" ☕ | Café pronto!", description=f"O seu café está pronto {ctx.author.mention}, aqui está! ☕", timestamp=datetime.datetime.now(), color=green_color)
        CaféEmbed2.set_footer(text=footer)
        view1.message = await msg.edit(embed=CaféEmbed2, view=view1)
        await view1.wait()

        if view1.value is None:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"O seu café esfriou! Peça outro caso queria beber um quente.", timestamp=datetime.datetime.utcnow(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            await asyncio.sleep(3)
            await view1.message.delete()

        elif view1.value:
            embed = disnake.Embed(title=f"Como estava o café Sr{ctx.author.name}?", description="🟢 | Bom\n🟡 | Mais ou menos\n 🔴 | Ruim", timestamp=datetime.datetime.utcnow(), color=yellow_color)
            embed.set_footer(text=footer)
            view.message = await ctx.author.send(embed=embed, view=view) 
            await view1.message.delete() 
            await view.wait()

            if view.value:
                embed = disnake.Embed(title="Obrigado pelo feedback!", description=f"Muito obrigado pelo seu feedback {ctx.author.mention}! A cafeteria LabyCoffe agradece muito.", timestamp=datetime.datetime.utcnow(), color=green_color)
                embed.set_footer(text=footer)
                await view.message.edit(embed=embed, view=None)

        
    @commands.slash_command(description="「😂 Diversão」Tudo que você escrever, eu deixo oa oirártnoc!", options=[Option('texto', 'Texto para eu deixar ao contrário', required=True)])
    @commands.guild_only()
    async def reverso(self, ctx, *, texto):
        t_rev = texto[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        embed = disnake.Embed(title="Reverso!", description=f"{text_channel_emoji} | Texto que você escreveu: **{texto}**\n🔁 | Texto que você escreveu, só que ao contrário: **{t_rev}**", timestamp=datetime.datetime.utcnow(), color=white_color)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

    @commands.slash_command(description="「😂 Diversão」Shipe uma pessoa com outra pessoa, pera, quê?", options=[Option('pessoa1', 'Selecione um membro que você quer shipar', OptionType.user, required=True), Option('pessoa2', 'Selecione um membro que você quer shipar com a pessoa1', OptionType.user, required=True)])
    @commands.guild_only()
    async def ship(self, ctx, pessoa1, pessoa2):
            shipnumber = int(random.randint(0, 100))
        
            if not pessoa1:
                name1 = ctx.author.name
                name2 = random.choice(ctx.guild.members)
                name2 == name2.name
            if not pessoa2:
                name2 = ctx.author.name
                name1 = name1
            if 0 <= shipnumber <= 30:
                comment = "Muito baixo!\n\n {}".format(random.choice(
                ["Friendzone ;(", 
                'Apenas "amigos"', 
                "Quase não há amor ;(",
                "Eu sinto um pouco de amor!",
                "Ainda estão na friendzone ;(",
                "Não, apenas não!",
                "Há um pequeno senso de romance de uma pessoa!"]))
            elif 31 <= shipnumber <= 70:
                comment = "Moderado!\n\n {}".format(random.choice(
                ["Justo!",
                "Um pouco de amor está no ar...",
                "Eu sinto que há algum romance progredindo!",
                "Estou começando a sentir um pouco de amor!",
                "Pelo menos isso é aceitável",
                "...",
                "Eu sinto um pouco de potencial!",
                "Hm... Talvez."]))
            elif 71 <= shipnumber <= 90:
                comment = "Quase perfeito!\n\n {}".format(random.choice(
                ["Eu definitivamente posso ver que o amor está no ar",
                "Eu sinto o amor! Há um sinal de um romance!",
                "Hm... Será que vai? 👀",
                "Eu definitivamente posso sentir o amor!",
                "Isso tem um grande potencial!",
                "Eu posso ver que o amor está lá! Em algum lugar..."]))
            elif 90 <= shipnumber <= 100:
                comment = "Amor verdadeiro!\n\n {}".format(random.choice(
                ["É uma combinação!", 
                "Namorados? KKKKKKKKK, Eles já são casados!", 
                "Definitivamente é uma combinação!", 
                "O amor está realmente no ar!", 
                "O amor está definitivamente no ar!"]))
            if shipnumber <= 40:
                shipColor = red_color
            elif 41 < shipnumber < 80:
                shipColor = yellow_color
            else:
                shipColor = green_color

            emb = (disnake.Embed(color=shipColor, \
                                title=comment, \
                                description="**{0}** e **{1}** {2}".format(pessoa1.mention, pessoa2.mention, random.choice(
                                [
                                    ":sparkling_heart:", 
                                    ":heart_decoration:", 
                                    ":heart_exclamation:", 
                                    ":heartbeat:"]
                                                                                                        ), timestamp=datetime.datetime.utcnow()
                                                                            )
                                )
                )
            emb.add_field(name="Resultados:", value=f"**{shipnumber}%**, {comment}", inline=True)
            emb.set_footer(text=footer)
            await ctx.send(embed=emb)
    
    @commands.slash_command(description="「😂 Diversão」Cara ou coroa?")
    @commands.guild_only()
    async def coinflip(self, ctx):
        choices = [f"{coinface_emoji} | **Deu cara!** ", f"{coincrown_emoji} | **Deu coroa!**"]
        rancoin = random.choice(choices)
        embed = disnake.Embed(title="Cara ou Coroa?", description=f"{rancoin}", timestamp=datetime.datetime.now(), color=white_color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

   #@slash_command(description="「😂 Diversão」Crie um sorteio!", options=[Option('tempo', 'Qual será o tempo do sorteio?', required=True), Option('prêmio', 'Qual será o prêmio do sorteio?', required=True), Option('canal', 'Qual canal em que o sorteio irá acontecer?', OptionType.CHANNEL, required=True), Option('reação', 'Qual vai ser a reação que será usada no sorteio?', required=True)])
    #async def giveaway(self, ctx, tempo, *, prêmio, canal: discord.TextChannel, reação):
        #if (not ctx.author.guild_permissions.manage_channels):
            #ErrorEmbed = discord.Embed(title=f"{error_emoji} | Erro!", description=f"{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Canais``!", timestamp=datetime.datetime.now(), color=0xFF0000)
            #ErrorEmbed.set_footer(text=footer)
            #await ctx.send(embed=ErrorEmbed)
            #return
        #await ctx.send(f'O sorteio foi criado com sucesso no canal {canal.mention}!')
        #gvembed = discord.Embed(title=f'Novo sorteio começando!', description=f'🎁 | **Prêmio: {prêmio};\n<:892799472478871613:916835300213403699> | Tempo: {tempo};\n{owner_emoji} | Criado por: {ctx.author.mention}.', color=0xfafafa)
        #time_convert = {"s": 1, "m":60, "h":3600, "d":86400}
        #gawtime = int(tempo[0]) * time_convert[tempo[-1]]
        #gvembed.set_footer(text=f"Sorteio acaba em {tempo}.")
        #gaw_msg = await canal.send(embed=gvembed)

        #await gaw_msg.add_reaction(f'{reação}')
        #await asyncio.sleep(gawtime)
        
        #new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)
        #users = await new_gaw_msg.reactions[0].users().flatten()
        #users.pop(users.index(self.bot.user))

        #vencedor = random.choices(users)
        
        #await ctx.send(f"🎉 | O membro {vencedor.mention} ganhou o sorteio de **{prêmio}**! Parabéns!")
        #await gaw_msg.delete()
                
    @commands.slash_command(description="「😂 Diversão」Veja a previsão do tempo de uma cidade por comando!", options=[Option('cidade', 'Cidade que você quer ver o clima', required=True)])
    @commands.guild_only()
    async def clima(self, ctx, *, cidade: str):
        city_name = cidade
        complete_url= url + '&q=' + city_name + "&"
        r = requests.get(complete_url)
        x = r.json()
        channel = ctx.channel
        if x["cod"] == "404":
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"**{cidade}** é uma cidade inválida! Por favor digite uma cidade válida.", timestamp=datetime.datetime.now(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            return await ctx.send(embed=ErrorEmbed, ephemeral=True)
        await channel.trigger_typing()
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature_celsiuis = str(round(current_temperature - 273.15))
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        feels_like = y["feels_like"]
        feels_like_celsiuis = str(round(feels_like - 273.15))
        wind = x["wind"]["speed"]
        weather = x["weather"][0]["icon"]
        z = x["weather"]
        weather_description = z[0]["description"]
        embed = disnake.Embed(title=f"Previsão do tempo - {city_name}", timestamp=datetime.datetime.now(), color=white_color)
        embed.add_field(name="Descrição:", value=f"**{weather_description}**", inline=False)
        embed.add_field(name="Temperatura(C):", value=f"**{current_temperature_celsiuis}°C**", inline=False)
        embed.add_field(name="Umidade(%):", value=f"**{current_humidity}%**", inline=False)
        embed.add_field(name="Pressão Atmosférica(hPa):", value=f"**{current_pressure}hPa**", inline=False)
        embed.add_field(name="Sensação térmica de:", value=f'**{feels_like_celsiuis}°C**')
        embed.set_thumbnail(url=f'https://openweathermap.org/img/w/{weather}.png')
        embed.set_footer(text=footer)

        embed1 = disnake.Embed(title=f"Previsão do tempo - {city_name}", timestamp=datetime.datetime.now(), color=white_color)
        embed1.add_field(name="Velocidade do vento:", value=f'**{wind}km/h**')        
        embed1.set_thumbnail(url=f'https://openweathermap.org/img/w/{weather}.png')
        embed1.set_footer(text=footer)

        valid_embeds = [embed, embed1]

        await ctx.send(embed=valid_embeds[0], view=Menu(valid_embeds, ctx))

                    
    @commands.slash_command(description="「😂 Diversão」Jogue pedra, papel e tesoura comigo!", options=[Option('escolha', 'Item que você quer utilizar', required=True)])
    @commands.guild_only()
    async def jokenpo(self, ctx, escolha):
        answer = escolha.lower()
        choices = ["pedra", "papel", "tesoura"]
        computers_answer = random.choice(choices)
        if answer not in choices:
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description="Isso não é uma opção válida! Por favor use ``pedra``, ``papel`` ou ``tesoura``!", timestamp=datetime.datetime.now(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
        else:
            if computers_answer == answer:
                EmpateEmbed = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                EmpateEmbed.add_field(name="Você escolheu:", value=f'``{answer}``')
                EmpateEmbed.add_field(name="Eu escolhi:", value=f'``{answer}``', inline=False)
                EmpateEmbed.add_field(name="Resultado do jogo:", value="``Empate!``", inline=False)
                EmpateEmbed.set_footer(text=footer)
                await ctx.send(embed=EmpateEmbed)
            if computers_answer == "pedra":
                if answer == "papel":
                    MemberWinEmbed1 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    MemberWinEmbed1.add_field(name="Você escolheu:", value=f'``{answer}``')
                    MemberWinEmbed1.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    MemberWinEmbed1.add_field(name="Resultado do jogo:", value="``Você ganhou!``", inline=False)
                    MemberWinEmbed1.set_footer(text=footer)
                    await ctx.send(embed=MemberWinEmbed1)
            if computers_answer == "papel":
                if answer == "pedra":
                    BotWinEmbed1 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    BotWinEmbed1.add_field(name="Você escolheu:", value=f'``{answer}``')
                    BotWinEmbed1.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    BotWinEmbed1.add_field(name="Resultado do jogo:", value="``Eu ganhei!``", inline=False)
                    BotWinEmbed1.set_footer(text=footer)
                    await ctx.send(embed=BotWinEmbed1)
            if computers_answer == "tesoura":
                if answer == "pedra":
                    MemberWinEmbed2 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    MemberWinEmbed2.add_field(name="Você escolheu:", value=f'``{answer}``')
                    MemberWinEmbed2.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    MemberWinEmbed2.add_field(name="Resultado do jogo:", value="``Você ganhou!``", inline=False)
                    MemberWinEmbed2.set_footer(text=footer)
                    await ctx.send(embed=MemberWinEmbed2) 
            if computers_answer == "pedra":
                if answer == "tesoura":
                    BotWinEmbed2 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    BotWinEmbed2.add_field(name="Você escolheu:", value=f'``{answer}``')
                    BotWinEmbed2.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    BotWinEmbed2.add_field(name="Resultado do jogo:", value="``Eu ganhei!``", inline=False)
                    BotWinEmbed2.set_footer(text=footer)
                    await ctx.send(embed=BotWinEmbed2)
            if computers_answer == "papel":
                if answer == "tesoura":
                    MemberWinEmbed3 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    MemberWinEmbed3.add_field(name="Você escolheu:", value=f'``{answer}``')
                    MemberWinEmbed3.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    MemberWinEmbed3.add_field(name="Resultado do jogo:", value="``Você ganhou!``", inline=False)
                    MemberWinEmbed3.set_footer(text=footer)
                    await ctx.send(embed=MemberWinEmbed3)
            if computers_answer == "tesoura":
                if answer == "papel":
                    BotWinEmbed3 = disnake.Embed(title="Pedra, Papel ou Tesoura?", timestamp=datetime.datetime.now(), color=white_color)
                    BotWinEmbed3.add_field(name="Você escolheu:", value=f'``{answer}``')
                    BotWinEmbed3.add_field(name="Eu escolhi:", value=f'``{computers_answer}``', inline=False)
                    BotWinEmbed3.add_field(name="Resultado do jogo:", value="``Eu ganhei!``", inline=False)
                    BotWinEmbed3.set_footer(text=footer)
                    await ctx.send(embed=BotWinEmbed3)
                              
    @commands.slash_command(description="「😂 Diversão」Faça eu falar algo!", options=[Option('mensagem', 'Mensagem que você quer que eu fale' , required=True)])
    @commands.guild_only()
    async def say(self, ctx, *, mensagem):
        if (not ctx.author.guild_permissions.manage_messages):
            ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Mensagens``!", timestamp=datetime.datetime.now(), color=red_color)
            ErrorEmbed.set_footer(text=footer)
            await ctx.send(embed=ErrorEmbed, ephemeral=True)
            return            
        else: 
            palavras = ["troxa", "sexo", "trouxa", "fdp", "filho da puta", "cuzao", "otario", "arrombado", "seu lixo humano", "seu lixo", "lixo", "seu trouxa", "seu resto de aborto", "macaco", "puta", "babaca", "boiola", "boquete", "anal", "buceta", "busseta", "caralho", "chupado", "da uma chupada", "escrota", "escroto fedido", "macaca", "fudendo", "fodida", "fudido", "punhetao", "cu", "vagabunda", "vagabundo", "vadia", "transar", "sex", "porra", "puta que pariu", "chupa meu pau", "seu negro", "seu macaco", "seu preto", "preto de merda", "preto horrivel", "seu pobre", "seu pirata", "vai se fuder", "comi sua mae", "peguei sua mae", "xvideos", "pornhub", "come muita gorda", "come gorda", "seu gorila", "nem golira", "prostituta", "putinha", "comi uma piriquita", "tomanocu", "pobre imundo", "tmnc", "filho da put@ CARALKHO", "FUDID0 VAI TOMA NOCU", "seu mamaco", "macamaco", "seu mamaquinho", "m4m4c0", "macaquinho", "ma🌵", "neandertal", "neandretal", "semata", "pobre", "fudid0", "fudid0", "FILHODAPUTA", "meu pau", "seu pau", "merd", "Fodase", "F0d1s3", "caralhoi", "penis", "M4c4c0", "seexo", "sexxo", "sexoo", "seexxoo", "ssexo", "sseexxoo", "s3x0", "s3xo", "sex0", "put4", "p0br3", "fodendo", "merda", "foda-se", "p@rra"]
            if mensagem.lower() in palavras:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Você não pode enviar essa palavra!", timestamp=datetime.datetime.now(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            menções = ["@everyone", "@here"]
            if mensagem.lower() in menções:
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Meu dono não deixa eu fazer isso 😔", timestamp=datetime.datetime.now(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            else:
                await ctx.send(mensagem)
                
    @commands.slash_command(description='「😂 Diversão」Role um dado!')
    @commands.guild_only()
    async def dado(self, ctx):
        message = await ctx.send("Escolha um número:\n**4**, **6**, **8**, **10**, **12**, **20** ")
        
        def check(m):
            return m.author == ctx.author

        try:
            message = await self.bot.wait_for("message", check = check, timeout = 30.0)
            m = message.content

            if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
                ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description="Desculpe, escolha inválida, lembrando que tem que ser um desses números que eu falei!", timestamp=datetime.datetime.now(), color=red_color)
                ErrorEmbed.set_footer(text=footer)
                await ctx.send(embed=ErrorEmbed, ephemeral=True)
                return
            
            coming = await ctx.channel.send("Rolando o dado!")
            time.sleep(2)
            await coming.delete()
            embed = disnake.Embed(title="Lá vem o dado :game_die:", description=f"O número que saiu do dado foi: **{random.randint(1, int(m))}**!", timestamp=datetime.datetime.now(), color=green_color)
            embed.set_footer(text=footer)
            await ctx.channel.send(embed=embed)
        except asyncio.TimeoutError:
            await message.delete()
            embed = disnake.Embed(title=f"{error_emoji} | Erro!", description="O processo foi cancelado pois você não deu resposta dentro desses 30 segundos.", timestamp=datetime.datetime.now(), color=red_color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, ephemeral=True)
     
    @commands.slash_command(description="「😂 Diversão」Faça uma pergunta para a bola de cristal!", options=[Option('pergunta', 'Sua pergunta', required=True)])
    @commands.guild_only()
    async def bola_de_cristal(self, ctx, *, pergunta):
        crystallEmbed = disnake.Embed(title="A bola de cristal diz: :crystal_ball:", description=f'**Sua pergunta: {pergunta}**\nResposta: {random.choice(crystall_list)}', timestamp=datetime.datetime.now(), color=purple_color)
        crystallEmbed.set_footer(text=footer)
        await ctx.send(embed=crystallEmbed)
        
    @commands.slash_command(description="「😂 Diversão」Cancele um meliante por menção!", options=[Option('usuário', 'Usuário para ser cancelado', OptionType.user, required=True)])
    @commands.guild_only()
    async def cancelar(self, ctx, usuário: disnake.Member):
        CancelEmbed = disnake.Embed(title="Eita! 👀", description=f"{usuário.mention} foi cancelado por {random.choice(lista_cancela)}.", timestamp=datetime.datetime.now(), color=usuário.color)
        CancelEmbed.set_footer(text=footer)
        await ctx.send(embed=CancelEmbed)
    
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        if inter.data.custom_id == "how_to_play_blurple":
            await inter.response.send_message("As instruções foram enviados para sua DM.", ephemeral=True)
            embed = disnake.Embed(title="Como jogar", description="Descubra a palavra correta em ``6`` tentativas. A cada tentativa, as peças mostram o quão perto você está da palavra certa. Exemplo:\n\n<:1000176813236043877:1000177693574299759><:1000176813236043877:1000179029648887958><:1000176813236043877:1000179559880196197><:1000176813236043877:1000179138008711251><:1000176813236043877:1000179255319212106>\n\nA letra <:1000176813236043877:1000177693574299759> faz parte da palavra e está na posição correta.\n\n<:1000176813236043877:1000179075815591957><:1000176813236043877:1000179029648887958><:1000181470096269403:1000182084935106692><:1000176813236043877:1000179053690626138><:1000176813236043877:1000179465189601320>\n\nA letra <:1000181470096269403:1000182084935106692> faz parte da palavra mas em outra posição.\n\n<:1000176813236043877:1000178124862005258><:1000176813236043877:1000177645947998348><:1000176813236043877:1000178101407457370><:1000176813236043877:1000178124862005258><:1000176813236043877:1000179465189601320>\n\n A letra <:1000176813236043877:1000179465189601320> não faz parte da palavra.\n\nAo contrário do jogo original, os acentos não são preenchidos automaticamente, pois não há **nenhuma** palavra com acentos e você pode jogar quando quiser! Em vez de poder jogar uma vez por dia.\n\nAs palavras podem possuir letras repetidas e para responder, basta dar reply na mensagem.", timestamp=datetime.datetime.utcnow(), color=0xfafafa)
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(text=footer)
            await inter.author.send(embed=embed, delete_after=120)
        if inter.data.custom_id == "initiate_game_green":
            puzzle_id = random_puzzle_id()
            embed = generate_puzzle_embed(inter.author, puzzle_id)
            await inter.response.edit_message(view=None)
            await inter.followup.send("O jogo foi iniciado!", delete_after=5)
            await inter.followup.send("Para dar uma resposta, basta dar reply na mensagem.",embed=embed)
            return
         
def setup(bot):
    bot.add_cog(Diversão(bot))