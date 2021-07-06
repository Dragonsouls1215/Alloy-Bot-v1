import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!AB ')

class Moderation(commands.Cog):
  def __intit__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def onready(self):
        print('BotCommands Cog updated.')

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
                
  #clear error (number not specified)
  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please specify the amount of messages to delete')
  #ban error (member not specified)
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please specify the person you are trying to ban')
  #unban error (member not specified)
  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please specify the person you are trying to unban')
  #kick error (member not specified)
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please specify the person you are trying to kick')

def setup(client):
  client.add_cog(Moderation(client))