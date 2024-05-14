import requests
import json
from discord.ext import commands

def get_quote(self):
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return (quote)

class motivacion(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('motivacion cog successfully loaded.')

    @commands.command(aliases=['motivar','motivate'])
    async def motivacion(self,ctx):
      quote = get_quote()
      await ctx.send(quote)

def setup(bot):
  bot.add_cog(motivacion(bot))




