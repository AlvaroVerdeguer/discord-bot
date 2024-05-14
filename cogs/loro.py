import discord
from discord.ext import commands

class loro(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('loro cog successfully loaded.')

    @commands.command(aliases=['repeat','repetir','Repetir','Loro','L'])
    async def loro(self,ctx, *args):
      await ctx.send('{}'.format( ' '.join(args)))
def setup(bot):
  bot.add_cog(loro(bot))