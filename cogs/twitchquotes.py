from bs4 import BeautifulSoup
import requests

from discord.ext import commands

class twitchquotes(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
      
    @commands.Cog.listener()
    async def on_ready(self):
        print('twitchquotes cog successfully loaded.')

    @commands.command(aliases=['tq','TwitchQuotes','TQ'])
    async def twitchquotes(self,ctx,arg):
      r = requests.get('https://www.twitchquotes.com/random/feed')
      html = r.text
      soup = BeautifulSoup(html, 'html.parser')
      lista = (soup.find_all("div", {"style":"display: none"}))
      contador = 1
      while contador <= int(arg):
        await ctx.send(lista[contador].text+'\n\n')
        contador+=1





def setup(bot):
  bot.add_cog(twitchquotes(bot))