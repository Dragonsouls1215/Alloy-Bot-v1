import discord
from discord.ext import commands, tasks
class Updatelist(commands.Cog):
  def __intit__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def onready(self):
    print('Updates Cog updated.')
  

#---------------------------------
#Commands
  @commands.command()
  async def updates(self, ctx):
    embed=discord.Embed(title="Latest Updates to my coding:", color=0x003366)
    embed.add_field(name = "10/03/2021", value = "Messed around with ban command to make sure it works (which it stil does, must've been a role hierarchy issue. -IFvD", inline = False )

    embed.add_field(name = "10/03/2021", value = "Possibly going to be adding information for the mobile game 'Endless Arena' (Characters, abilities, and set bonuses to prioritize)", inline = False )
    await ctx.send(embed = embed)  
  
  @commands.command() 
  async def helpdev(stf, ctx):
    embed = discord.Embed(title = "How to turn on developer settings", color = 0x003366)
    embed.add_field(name = "Step 1", value = "Go to settings", inline = False)
    embed.add_field(name = "Step 2", value = "Go to appearance and turn developer mode on", inline = False)
    embed.add_field(name = "Success", value = "You can now copy user/channel/server IDs as needed.", inline = False)
    embed.set_footer(text= "This is important if you have lots of bots in your server since some require IDs to perform tasks like reaction roles!")
    await ctx.send(embed = embed)
  
    #Support Sever
  @commands.command(name = 'ss', aliases =['SS'])
  async def ss(self, ctx):
    await ctx.send("https://discord.gg/padZEPyz4Z")
    
def setup(client):
  client.add_cog(Updatelist(client))