import discord
from discord.ext import commands
import random
import aiohttp



class nsfw(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('nsfw cog successfully loaded.')

    @commands.command(aliases=['sfw','AlmaSucia'])
    async def nsfw(self,ctx,arg):
      if ctx.channel.is_nsfw():
        contador = 0
        while contador <= int(arg):
          embed = discord.Embed(title="test", description="test")
          async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
              res = await r.json()
              embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
              await ctx.send(embed=embed)
      else:
        await ctx.send('vete a hacer marranadas a un canal NSFW, puerc@')


def setup(bot):
  bot.add_cog(nsfw(bot))