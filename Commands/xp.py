from Config.colors import red_color, green_color, white_color
from Config.database import levelling_cluster
from Config.images import image_failed
from disnake import Option, OptionType
from Config.emojis import error_emoji
from disnake.ext import commands
from Config.bot import footer
import datetime
import pymongo
import disnake


cluster = pymongo.MongoClient(levelling_cluster)
levelling = cluster["Discord"]["Níveis"]


class Levels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="「⚡ XP」Mostra seu xp e progresso", options=[Option('membro', 'Selecione o membro que você quer ver os status', OptionType.user)])
    @commands.guild_only()
    async def xp(self, ctx, membro: disnake.Member = None):
            member = membro if membro else ctx.author
            stats = levelling.find_one({"id" : member.id})
            if stats is None:
                embed = disnake.Embed(title=f'{error_emoji} | Erro!', description=f'Você possui não possui XP.', timestamp=datetime.datetime.utcnow(), color=red_color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, ephemeral=True)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*lvl)):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort("xp", -1)
                for x in rankings:
                    rank +=1
                    if stats["id"] == x["id"]:
                        break
                if member.id == ctx.author.id:
                    embed = disnake.Embed(title=f"Seu status", timestamp=datetime.datetime.utcnow(), color=member.color)
                else:
                    embed = disnake.Embed(title=f"{member.name} Status", timestamp=datetime.datetime.utcnow(), color=member.color)
                embed.add_field(name="XP do nível:", value=f"{xp}", inline=True)
                embed.add_field(name="Nível:", value=f'{lvl}', inline=True)
                embed.add_field(name="Rank:", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="XP Total:", value=f'{stats["xp"]}')
                embed.add_field(name=f"Progress Bar: [{xp}/{int(200*((1/2)*lvl))}]", value=boxes * ":green_square:" + (20-boxes) * ":white_large_square:",  inline=False)
                embed.set_thumbnail(url=member.avatar.url)
                embed.set_footer(text=footer)
                try:
                    await ctx.send(embed=embed)
                except disnake.NotFound:
                    ErrorEmbed = disnake.Embed(title=f"{error_emoji} | Erro!", description=f"Não consegui achar esse usuário...", timestamp=datetime.datetime.utcnow(), color=red_color)
                    ErrorEmbed.set_footer(text=footer)
                    await ctx.send(embed=ErrorEmbed, ephemeral=True)
    
    @commands.slash_command(description="「⚡ XP」Mostra o placar de xp do servidor")
    @commands.guild_only()
    async def rank(self, ctx):
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = disnake.Embed(title = f"{ctx.guild.name} leaderboard:", timestamp=datetime.datetime.utcnow(), color=white_color)
            embed.set_footer(text=footer)
            if ctx.guild.icon is None:
                embed.set_thumbnail(url=image_failed)
            else:
                embed.set_thumbnail(url=ctx.guild.icon.url)

            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x['id'])
                    tempxp = x["xp"]
                    if i == 1:
                        posicao = f'🏆 {i}'
                    elif i == 2:
                        posicao = f'🥈 {i}' 
                    elif i == 3:
                        posicao = f'🥉 {i}' 
                    else:
                        posicao = f'{i}'
                    lvl = 0
                    while True:
                        if tempxp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl +=1

                    embed.add_field(name=f'{posicao}º {temp.name}#{temp.discriminator} | Lvl {lvl}', value=f"XP: {tempxp}", inline=False)
                    i +=1
                except:
                    pass
                if i == 11:
                    break
            await ctx.send(embed=embed) 

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
                stats = levelling.find_one({"id" : message.author.id})
                if not message.author.bot:
                    if stats is None:
                        newuser = {"id" : message.author.id, "xp" : 0}
                        levelling.insert_one(newuser)
                    else:
                        xp = stats["xp"] + 1 #Inserir XP
                        levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                        lvl = 0
                        while True:
                            if xp < ((50*(lvl**2))+(50*lvl)):
                                break
                            lvl +=1
                        xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                        {"user_id": {"xp": 10}}
                        {"guild_id": {"user_id": {"xp": 10}}}
                        if xp == 0:
                            channel = self.bot.get_channel(999734768180670474)
                            embed = disnake.Embed(title="Level Up!", description=f"🎉 | Parabéns {message.author.mention}! Você subiu para o nível **{lvl}**!", timestamp=datetime.datetime.utcnow() ,color=green_color)
                            embed.set_footer(text=footer)
                            await message.channel.send(embed=embed)

                            embedlogs = disnake.Embed(description=f"O usuário {message.author.mention} subiu para o nível ``{lvl}`` em ``{message.guild.name}``!", timestamp=datetime.datetime.utcnow(), color=green_color)
                            embedlogs.set_author(icon_url=self.bot.user.avatar.url, name="LabyBot Logs")
                            embedlogs.set_footer(text=footer)
                            await channel.send(embed=embedlogs)

    
def setup(bot):
    bot.add_cog(Levels(bot))