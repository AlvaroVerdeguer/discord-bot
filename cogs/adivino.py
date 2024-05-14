from discord.ext import commands
import random

class adivino(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
 
    @commands.Cog.listener()
    async def on_ready(self):
        print('adivino cog successfully loaded.')
    @commands.command(aliases=['ad','adivina','FortuneTeller','AD','a','A'])
    async def adivino(self,ctx,*,question):
      response = [
        'Tio,me das miedo',
        '¿pero que te crees?, ¿que soy adivino? ',
        'noruma lelelelele',
        'no se, soy de letras',
        'he verda',
        'sin duda',
        'obvio',
        'deberías rendirte',
        'podría ser',
        'no creo',
        'pregunta de nuevo más tarde',
        'mmm, lo veo complicado',
        'absolutamente no',
        'impredecible',
        'seguramente',
      ]
      await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(response)}')



def setup(bot):
  bot.add_cog(adivino(bot))