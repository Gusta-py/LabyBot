from Config.emojis import vscode_emoji, python_emoji, paper_emoji, config1_emoji, config_emoji, memory_emoji
from Config.links import botadd_link, labyserver_link, labysite_link
from Config.discloud import api_token
from Config.colors import white_color
from disnake.ext import commands
from Config.bot import footer
import discloud
import datetime
import disnake


client = discloud.Client(api_token)

class onMessagePing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.content in ["<@908870304909115432>", "<@!908870304909115432>"]:
                any(mentioned.bot for mentioned in message.mentions)
                members = 0
                for guild in self.bot.guilds:
                    members += guild.member_count - 1

                serverCount = len(self.bot.guilds)
                bot = await client.app_info(target=908870304909115432)

                view1 = disnake.ui.View()
                item = disnake.ui.Button(label="Me adicione!", style=disnake.ButtonStyle.blurple, url=botadd_link)
                view1.add_item(item=item)


                item2 = disnake.ui.Button(label="Meu servidor", style=disnake.ButtonStyle.green, url=labyserver_link)
                view1.add_item(item=item2)


                item3 = disnake.ui.Button(label="Meu website", style=disnake.ButtonStyle.grey, url=labysite_link)
                view1.add_item(item=item3)

                if message.guild.id == 892799472478871613:
                    view1 = disnake.ui.View()
                    item = disnake.ui.Button(label="Me adicione!", style=disnake.ButtonStyle.blurple, url=botadd_link)
                    view1.add_item(item=item)

                item3 = disnake.ui.Button(label="Meu website", style=disnake.ButtonStyle.blurple, url=labyserver_link)
                view1.add_item(item=item3)

        
                mentionEmbed = disnake.Embed(title="👋 | Olá!", description=f"Olá {message.author.mention}! Me chamo LabyBot, mas pode me chamar de Laby,prazer em conhecê-lo! Sou um bot em versão para os servidores do Discord, veja algumas de minhas informações logo abaixo!", timestamp=datetime.datetime.utcnow(), color=white_color)
                mentionEmbed.add_field(name=f'{config1_emoji} | Prefixo:', value="``/``")
                mentionEmbed.add_field(name=f'{vscode_emoji} | Programado em:', value='``Visual Studio Code (Python)``', inline=False)
                mentionEmbed.add_field(name=f'{python_emoji} | Python:', value=f'``3.10.6``', inline=False )
                mentionEmbed.add_field(name=f"{memory_emoji} | Memória", value=f"``{bot.memory.using}``", inline=False)
                mentionEmbed.add_field(name=f'{paper_emoji} | Comandos:', value=f'``{len(self.bot.global_slash_commands)}`` Comandos!', inline=False)
                mentionEmbed.add_field(name=f"{config_emoji} | Estou em...", value=f"``{serverCount}`` Servidores com um total de ``{members}`` amigos!")
                mentionEmbed.set_thumbnail(url=self.bot.user.avatar.url)
                mentionEmbed.set_footer(text=footer)
                await message.channel.send(embed=mentionEmbed, view=view1, delete_after=100)
        except Exception as e:
            print(e)
                        
def setup(bot):
    bot.add_cog(onMessagePing(bot))