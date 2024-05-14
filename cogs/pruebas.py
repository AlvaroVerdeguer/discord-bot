import discord
from discord.ext import commands
import asyncio

class pruebas(commands.Cog):
    def __init__(self,bot):
      self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('pruebas cog successfully loaded.')

    
    @commands.command(pass_context=True)
    async def pruebas(self,ctx):
        await ctx.send("seguro? [y(es)/n(o)]")

        def check(m):
            return m.author == ctx.author

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=10)
            # OR `check=lambda m: m.author == ctx.author`

            if msg.content.lower() in ['y', 'yes']:
                await ctx.send("en proceso..")
            elif  msg.content.lower() in ['n', 'no']:
                await ctx.send("abortando")
            else:
                await ctx.send("beep,no entendi,boop, esa respuesta,beep")
        except asyncio.TimeoutError as e:
            await ctx.send("esperaste demasiado para responder")




def setup(bot):
  bot.add_cog(pruebas(bot))

