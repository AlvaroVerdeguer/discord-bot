
from discord.ext import commands
from googleapiclient.discovery import build
from bs4 import BeautifulSoup


def google_search(search_term, api_key, cse_id, **kwargs):
  service = build("customsearch", "v1", developerKey=api_key)
  res = service.cse().list(
  q=search_term, cx=cse_id, **kwargs).execute()
  return res['items']

class google(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('google cog successfully loaded.')

    @commands.command(aliases=['codigo','código','Html','HTML'])
    async def html(self,ctx,arg):
      my_api_key = "AIzaSyBd4IjSx00LmB4aYCXZGFOkZcgFuqpcnY8"
      my_cse_id = "d42751372989ad788"
      results = google_search(
      arg, my_api_key, my_cse_id, num=1)
      for result in results:
        await ctx.send('\n'+result+'\n')


def setup(bot):
  bot.add_cog(google(bot))

