import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):

  def __intit__(self, client):

    self.client = client

  @commands.Cog.listener()

  async def onready(self):

    print('ReactionRoles Cog updated.')
  
#This part is changed and to be tabed so it is lined up with @commands.Cog.listener

#---------------------------------

#Commands

  
#--------------------------------- 

#Errors

#--------------------------------- 

def setup(client):
  client.add_cog(ReactionRoles(client))