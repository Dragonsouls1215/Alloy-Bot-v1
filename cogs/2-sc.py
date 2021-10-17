import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!Ab ')

class Simple_Commands(commands.Cog):
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
    await ctx.send(embed = embed, delete_after = 3)
  
  #User is bipolar
  @commands.command(name='UiB', aliases=['uib','UIB'])
  async def SiB(self, ctx, *, msg):
    await ctx.message.delete()
    embed=discord.Embed(title="Task Complete!", color=0x003366)
    embed.set_footer(text = f"{msg} is bipolar!" )
    await ctx.send(embed = embed, delete_after = 5)

  #Credits
  @commands.command(name='credits', aliases=['cr', 'CREDITS', 'CR'])
  async def credits(self, ctx):
    
    embed=discord.Embed(title="Credits", color=0x003366)
    embed.add_field(name= "Recaff", value = "Helping with some of the programming and keeping me (IFvD) sane when needed.", inline = False)
    embed.add_field(name= "SpookyBoi", value = "Helped with some of the error codes and made the bot's original website.", inline = False)
    embed.add_field(name= "IFrostvsDread", value = "Owner of the bot and maintaining code as time goes on.", inline = False)
    embed.set_footer(text = "Thank you for your contributions to Alloy Bot!" )
    await ctx.send(embed = embed, delete_after = 5)
 
  #Richard
  @commands.command(name = 'richard', aliases= ["Richard"])
  async def richard(self, ctx):
    
    embed=discord.Embed(title="Task Complete!", color=0x003366)
    await ctx.send(embed = embed, delete_after = 8)
    await ctx.send("https://media.discordapp.net/attachments/873584600167878736/885681573914087425/richardbot.png", delete_after = 8)
        
def setup(client):
  client.add_cog(Simple_Commands(client))