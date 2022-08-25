from disnake.ext import commands


class onMessageVerification(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild: 
            return
        if message.channel.id == 938813191255887872: 
            if message.author.id == 908870304909115432:
                return  
            else:
                await message.delete()
            try: 
                await message.author.send('Você não pode enviar mensagens no canal <#938813191255887872>! Utilize o comando /verificar para se verificar e ter os canais liberados.')
            except:
                pass
  
def setup(bot):
    bot.add_cog(onMessageVerification(bot))