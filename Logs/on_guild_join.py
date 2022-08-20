from Config.emojis import role_emoji, id_emoji, users_emoji, owner_emoji
from Config.images import image_failed
from Config.colors import green_color
from disnake.ext import commands
from Config.bot import footer
import datetime
import disnake


class onJoin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(937060001984417853)

        view = disnake.ui.View(timeout=1)
        view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.green, label="Detalhes", emoji=role_emoji, custom_id=f"detalhes-{guild.id}"))

        await channel.send('<@901498839981236235>', delete_after=1)
        JoinEmbed0 = disnake.Embed(title="📥 | Entrada", description="**Acabei de entrar em um servidor! Clique no botão abaixo para ver os detalhes do servidor.**", color=green_color)
        await channel.send(embed=JoinEmbed0, view=view)
    
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        try:
            tipo, guild_id = inter.data.custom_id.split("-")
        except ValueError: 
            return
        guild = self.bot.get_guild(int(guild_id))
        view = disnake.ui.View(timeout=None)
        if tipo == "detalhes":
            view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.red, label="Voltar", custom_id=f"voltar-{guild.id}"))
            JoinEmbed2 = disnake.Embed(description=f"**Detalhes do servidor:**", timestamp=datetime.datetime.utcnow(), color=green_color)
            if guild.icon is None:
                JoinEmbed2.set_thumbnail(url=image_failed)
            else:
                JoinEmbed2.set_thumbnail(url=guild.icon.url)
            JoinEmbed2.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
            JoinEmbed2.add_field(name=f"{role_emoji} | Nome do servidor:", value=f"``{guild.name}``")
            JoinEmbed2.add_field(name=f"{id_emoji} | ID do servidor:", value=f"``{guild.id}``", inline=False)
            JoinEmbed2.add_field(name=f"{users_emoji} | Membros:", value=f"`{len([m for m in guild.members if not m.bot])}` usuários e `{len(list(filter(lambda m: m.bot, guild.members)))}` bots", inline=False)
            JoinEmbed2.add_field(name=f"{owner_emoji} | Dono do servidor:", value=f"{guild.owner.mention}", inline=False)
            JoinEmbed2.set_footer(text=footer)
            await inter.response.edit_message(embed=JoinEmbed2, view=view)
        if tipo == "voltar":
            view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.green, label="Detalhes", emoji=role_emoji, custom_id=f"detalhes-{guild.id}"))
            JoinEmbed0 = disnake.Embed(title="📥 | Entrada", description="**Acabei de entrar em um servidor! Clique no botão abaixo para ver os detalhes do servidor.**", color=green_color)
            await inter.response.edit_message(embed=JoinEmbed0, view=view)
    
def setup(bot):
    bot.add_cog(onJoin(bot))