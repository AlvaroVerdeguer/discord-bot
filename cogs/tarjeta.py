import discord
from discord.ext import commands
import datetime

class tarjeta(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('tarjeta cog successfully loaded.')

    @commands.command(aliases=['tarjeta','informacion'])
    async def info(self,ctx):
      embed = discord.Embed(title=f"{ctx.guild.name}", description="servidor dedicado a estar de tranquis con los panacotas", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.add_field(name="Server creado el", value=f"{ctx.guild.created_at}")
      embed.add_field(name="dueño del server", value=f"{ctx.guild.owner}")
      embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
      embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
      # embed.set_thumbnail(url=f"{ctx.guild.icon}")
      embed.set_thumbnail(url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289")

      await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(tarjeta(bot))