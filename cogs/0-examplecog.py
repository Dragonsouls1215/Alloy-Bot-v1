import discord
from discord.ext import commands

class Example(commands.Cog):
  def __intit__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def onready(self):
    print('Example Cog updated.')
  
  @commands.command(name= 'ping', aliases = ['Ping'])
  async def ping(self, ctx):
    await ctx.send('Pong!', delete_after = 3)

def setup(client):
  client.add_cog(Example(client))

