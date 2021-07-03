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

  #clear
  @commands.command(name='clear', aliases=['c','cl','CL','C'], description="Clears a number of messages, must provide a value")
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Cleared' + amount + ' messages')

  #kick
  @commands.command(name='kick', aliases=['k','K', 'KICK'])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)

  #ban
  @commands.command(name='ban', aliases=['b', 'B', 'BAN'])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

  #unban
  @commands.command(name='unban', aliases=['ub', 'UB', 'UNBAN'])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disciminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_disciminator):
                await ctx.guild.unban(user)
                (f'Unbanned {member.mention}')
                await ctx.send('User has been unbanned')
                return
  #credits
  @commands.command(name='credits', aliases=['cr', 'CREDITS', 'CR'])
  async def credits(self, ctx):
    await ctx.send("The developers of this bot are the following: IFrostvsDread, SpookyBoi and Recaffenated.")

  @commands.command(name='credits2', aliases=['cr2', 'CREDITS2', 'CR2'])
  async def credits2(self, ctx):
    await ctx.send("This is a test command for reloading cogs 5x.")

  @commands.command(name = 'richard')
  async def richard(self, ctx):
    await ctx.send("MY NAME IS NOT RICHARD")
    
  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please specify the amount of messages to delete')

  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send('Command not found')
def setup(client):
    client.add_cog(Bot_Commands(client))
