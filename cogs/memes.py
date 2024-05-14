import discord
from discord.ext import commands
import praw
import random

reddit = praw.Reddit(
  client_id="d-elOPzKuIK64k9oVFB8LQ",
  client_secret="USspWqwP9NbIl2XUlbyV4ZClbkbu6Q",
  user_agent="ElPanaBot creado por Verduxo",
)
class meme(commands.Cog):
    def __init__(self,bot):
      self.bot = bot
 
    @commands.Cog.listener()
    async def on_ready(self):
        print('meme cog successfully loaded.')

    @commands.command(aliases=['memes'])
    async def meme(self,ctx,arg2):

      memes_submissions = reddit.subreddit('memes').new()
      post_to_pick = random.randint(1, 10)
      for i in range(0, post_to_pick):
          submission = next(x for x in memes_submissions if not x.stickied)

      await ctx.send(submission.url)

      topics = 'SpanishMeme\nhot\nAdviceAnimals\ndankmemes\nfunny\nteenagers\nokbuddyretard\ncringe\n'


def setup(bot):
  bot.add_cog(meme(bot))  