from discord.ext import commands
import translators as ts


class traductor(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('traductor cog successfully loaded.')

    @commands.command()
    async def traducir(self,ctx,arg):
      await ctx.send(ts._deepl.language_map)

def setup(bot):
  bot.add_cog(traductor(bot))
