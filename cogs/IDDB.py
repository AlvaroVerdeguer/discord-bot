from discord.ext import commands

class IDDB(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
      
    @commands.Cog.listener()
    async def on_ready(self):
        print('IDDB cog successfully loaded.')


    @commands.command()
    async def iddb(self,ctx):
      f=open('IDs.txt','r+')
      contenido = f.readlines()
      ID=(ctx.author.id)
      if ID in contenido:
          print('camarera')
      else:
          f.write(ID)
      f.close()
    
    
    #list.count(elem)
    #@commands.command(pass_context=True)
    #async def dm(self,ctx):
    #    user=await self.get_user_info("User's ID here")
    #    await ctx.send(user, "Your message goes here")

def setup(bot):
  bot.add_cog(IDDB(bot))