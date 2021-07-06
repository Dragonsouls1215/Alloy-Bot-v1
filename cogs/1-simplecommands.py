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
    await ctx.send('Good morning!')
  
  #Sire is bipolar
  @commands.command(name='SiB', aliases=['sib','SIB'], description="As a joke for a friend")
  async def SiB(self, ctx):
    await ctx.channel.send('Sire is bipolar.')

  #credits
  @commands.command(name='credits', aliases=['cr', 'CREDITS', 'CR'])
  async def credits(self, ctx):
    await ctx.send("The developers of this bot are the following: IFrostvsDread, SpookyBoi and Recaffenated.")

  #credits2
  @commands.command(name='credits2', aliases=['cr2', 'CREDITS2', 'CR2'])
  async def credits2(self, ctx):
    await ctx.send("This is a test command for reloading cogs 5x.")
  #richard
  @commands.command(name = 'richard')
  async def richard(self, ctx):
    await ctx.send("MY NAME IS NOT RICHARD")

  #Support Sever
  @commands.command(name = 'ss', aliases =['SS'])
  async def ss(self, ctx):
    await ctx.send("https://discord.gg/YQ2vvVXKcj")
    
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send('Command not found')
      
def setup(client):
    client.add_cog(Bot_Commands(client))
