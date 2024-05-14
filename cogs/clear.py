from discord.ext import commands

class clear(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
      
    @commands.Cog.listener()
    async def on_ready(self):
        print('clear cog successfully loaded.')

    @commands.command(aliases=['limpiar','limpieza'])
    @commands.has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=5):
      await ctx.channel.purge(limit=amount)



def setup(bot):
  bot.add_cog(clear(bot))