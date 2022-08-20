from Config.colors import white_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onSlash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
        channel = self.bot.get_channel(937059961169662042)
        LogEmbed = disnake.Embed(description=f'\n\nUsuário: **{inter.author.mention}**\nID: ``{inter.author.id}``\nComando: ``/{inter.data.name}``\nServidor: ``{inter.guild.name}`` | ``{inter.guild.id}``\nCanal: {inter.channel}', timestamp=datetime.datetime.now(), color=white_color)
        LogEmbed.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
        LogEmbed.set_footer(text=footer)
        await channel.send(embed=LogEmbed)

def setup(bot):
    bot.add_cog(onSlash(bot))