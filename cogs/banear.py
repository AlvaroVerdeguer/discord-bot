import discord
from discord.ext import commands


class banear(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('banear cog successfully loaded.')

    @commands.command(aliases=['tirar','expulsar','desterrar'])
    async def kick(self,ctx,member : discord.Member,*,reason=None):
      if ctx.author.id == 375201148166209536:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} **fue expulsado**')


    @commands.command(aliases=['banear'])
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member : discord.Member,*,reason=None):
      if ctx.author.id == 375201148166209536:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} **fue baneado**')


    @commands.command(aliases=['desbanear'])
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
      if ctx.author.id == 375201148166209536:
        banned_user = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')
        for ban in banned_user:
          user = ban.user
          if (user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} **fue desbaneado**')
            return

def setup(bot):
  bot.add_cog(banear(bot))

