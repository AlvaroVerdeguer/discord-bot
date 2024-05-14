from discord.ext import commands

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.error = error

    @commands.Cog.listener()
    async def on_ready(self):
        print('errorHandling cog successfully loaded.')

    @commands.Cog.listener()
    async def on_error(self,event, *args, **kwargs):
      with open('err.log', 'a') as f:
          if event == 'on_message':
              f.write(f'Unhandled message: {args[0]}\n')
          else:
              raise  

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
      if isinstance(error,commands.CommandNotFound):
        await ctx.send("""```ini
    creo que ese comando [no existe tio]
    vigila a ver si esta en la lista de comandos [$com]```""")

      if isinstance(error, commands.errors.NSFWChannelRequired):
        ctx.title = "NSFW Command"
        ctx.description = error.args[0]
        return await ctx.send(embed=ctx)


def setup(bot):
    bot.add_cog(error(bot))

