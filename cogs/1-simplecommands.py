import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!AB ')

class Bot_Commands(commands.Cog):
  def __intit__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def onready(self):
        print('BotCommands Cog updated.')

  #online      
  @commands.command()
  async def online(self, ctx):
    embed=discord.Embed(title="Task Complete!", color=0x003366)
    embed.set_footer(text = "Good morning!" )
    await ctx.send(embed = embed)
  
  #Sire is bipolar
  @commands.command(name='SiB', aliases=['sib','SIB'], description="As a joke for a friend")
  async def SiB(self, ctx):
    embed=discord.Embed(title="Task Complete!", color=0x003366)
    embed.set_footer(text = "Sire is bipolar!" )
    await ctx.send(embed = embed)

  #Credits
  @commands.command(name='credits', aliases=['cr', 'CREDITS', 'CR'])
  async def credits(self, ctx):
    embed=discord.Embed(title="Credits", color=0x003366)
    embed.add_field(name= "Recaff", value = "Helping with some of the programming and keeping me sane when needed.", inline = False)
    embed.add_field(name= "SpookyBoi", value = "Helped with some of the error codes and made the bot's website.", inline = False)
    embed.add_field(name= "IFrostvsDread", value = "Owner of the bot and maintaining code as time goes on.", inline = False)
    embed.set_footer(text = "Thank you for your contributions to Alloy Bot!" )
    await ctx.send(embed = embed)
 
  #Richard
  @commands.command(name = 'richard')
  async def richard(self, ctx):
    embed=discord.Embed(title="Task Complete!", color=0x003366)
    embed.set_footer(text = '"His name should be Richard for the funny nickname" -Flippyr')
    await ctx.send(embed = embed)

  #Support Sever
  @commands.command(name = 'ss', aliases =['SS'])
  async def ss(self, ctx):
    await ctx.send("https://discord.gg/padZEPyz4Z")
        
def setup(client):
  client.add_cog(Bot_Commands(client))