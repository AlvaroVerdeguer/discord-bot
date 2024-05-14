import discord
from discord.ext import commands

class usuario(commands.Cog):

    def __init__(self,bot):
      self.bot = bot

 
    @commands.Cog.listener()
    async def on_ready(self):
        print('usuario cog successfully loaded.')



    @commands.command(aliases=['yo','usuario','autor'])
    async def me(self,ctx):
      await ctx.send(f"usuario: {ctx.author}"+'\ncon ID: '+str(ctx.author.id))

    @commands.command()
    async def soy_yo(self,ctx):
      if ctx.author.id == 375201148166209536:
        await ctx.send('este mensaje solo lo puede sacar mi creador Verduxo ')
    


def setup(bot):
  bot.add_cog(usuario(bot))