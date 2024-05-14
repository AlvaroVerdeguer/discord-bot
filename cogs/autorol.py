import discord
from discord.ext import commands

class autorol(commands.Cog):
    def __init__(self,bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('autorol cog successfully loaded.')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
      message_id = payload.message_id
      if message_id == 800461740076040252:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

        if payload.emoji.name == 'perrowaton':
          role = discord.utils.get(guild.roles,name='perro waton')
          print('perro waton')
          #role = discord.utils.get(guild.roles, name ='Camping Fuck')
        elif payload.emoji.name == 'NullB':
          role = discord.utils.get(guild.roles,name='mainkra')
        else:
          role = discord.utils.get(guild.roles,name=payload.emoji.name)

        if role is not None:
          member = discord.utils.find(lambda m : m.id == payload.user_id,guild.members)
          if member is not None:
            await member.add_roles(role)
            print('hecho')
          else:
            print('persona no encontrada')
        else:
          print('rol no encontrado')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
      print('bye')
      message_id = payload.message_id
      if message_id == 800461740076040252:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

        if payload.emoji.name == 'perrowaton':
          role = discord.utils.get(guild.roles,name='perro waton')
          #role = discord.utils.get(guild.roles, name ='Camping Fuck')
        elif payload.emoji.name == 'NullB':
          role = discord.utils.get(guild.roles,name='mainkra')
        else:
          role = discord.utils.get(guild.roles,name=payload.emoji.name)

        if role is not None:
          member = discord.utils.find(lambda m : m.id == payload.user_id,guild.members)
          if member is not None:
            await member.remove_roles(role)
            print('hecho')
          else:
            print('persona no encontrada')
        else:
          print('rol no encontrado')
        
def setup(bot):
  bot.add_cog(autorol(bot))