import discord
from discord.ext import commands


class melon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Melon'])
    async def melon(self,ctx):
        await ctx.send("https://tenor.com/es/view/cat-pet-cute-eating-watermelon-me-lon-gif-17316751")


def setup(bot):
    bot.add_cog(melon(bot))
