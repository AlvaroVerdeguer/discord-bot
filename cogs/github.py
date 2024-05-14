#
from discord.ext import commands

class github(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
      
    @commands.Cog.listener()
    async def on_ready(self):
        print('github cog successfully loaded.')

    @commands.command(aliases=['gh','git','dios'])
    async def github(self,ctx):
      await ctx.channel.send('El mejor programador del universo, mi creador:\nhttps://github.com/Verduxo/')
      await ctx.send('su último proyecto: \nhttps://github.com/Verduxo/Mega.nz-Link-Checker')



def setup(bot):
  bot.add_cog(github(bot))