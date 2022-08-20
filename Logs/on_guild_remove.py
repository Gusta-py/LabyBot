from Config.emojis import role_emoji, id_emoji, users_emoji, owner_emoji
from Config.images import image_failed
from Config.colors import red_color
from disnake.ext import commands
from Config.bot import footer
import disnake


class onRemove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(937060001984417853)

        await channel.send('<@901498839981236235>', delete_after=1)

        class DetailButton(disnake.ui.Button):
            def __init__(self):
                super().__init__(style=disnake.ButtonStyle.red, label="Detalhes", emoji=role_emoji)

            async def callback(self, inter):
                self.view.remove_item(self)
                self.view.add_item(BackButton())
                await inter.response.edit_message(embed=JoinEmbed1, view=self.view)
                
        class BackButton(disnake.ui.Button):
            def __init__(self):
                super().__init__(style=disnake.ButtonStyle.red, label="Voltar")
            
            async def callback(self, inter):
                self.view.remove_item(self)
                self.view.add_item(DetailButton())
                await inter.response.edit_message(embed=JoinEmbed, view=self.view)

        v = disnake.ui.View(timeout=None)
        v.add_item(DetailButton())

        JoinEmbed = disnake.Embed(title="📤 | Saída", description="**Acabei de sair de um servidor! Clique no botão abaixo para ver os detalhes do servidor.**", color=red_color)
        await channel.send(embed=JoinEmbed, view=v)

        JoinEmbed1 = disnake.Embed(description=f"**Detalhes do servidor:**", color=red_color)
        if guild.icon is None:
                JoinEmbed1.set_thumbnail(url=image_failed)
        else:
            JoinEmbed1.set_thumbnail(url=guild.icon.url)
        JoinEmbed1.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
        JoinEmbed1.add_field(name=f"{role_emoji} | Nome do servidor:", value=f"``{guild.name}``")
        JoinEmbed1.add_field(name=f"{id_emoji} | ID do servidor:", value=f"``{guild.id}``", inline=False)
        JoinEmbed1.add_field(name=f"{users_emoji} | Membros:", value=f"`{len([m for m in guild.members if not m.bot])}` usuários e `{len(list(filter(lambda m: m.bot, guild.members)))}` bots", inline=False)
        JoinEmbed1.add_field(name=f"{owner_emoji} | Dono do servidor:", value=f"{guild.owner.mention}", inline=False)
        JoinEmbed1.set_footer(text=footer)
    
def setup(bot):
    bot.add_cog(onRemove(bot))