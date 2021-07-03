import discord
from discord.ext import commands

class chatresponse(discord.Client):
  def __intit__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def onready(self):
    print('Chatresponse Cog updated.')

  async def on_message(self, message):
    print('Message from {0.author}: {content}'.format(message))
  


def setup(client):
  client.add_cog(chatresponse(client))