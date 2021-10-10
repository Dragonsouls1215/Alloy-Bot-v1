import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import MissingPermissions
client = commands.Bot(command_prefix='!Ab ')

class Moderation(commands.Cog):
  def __intit__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def onready(self):
        print('BotCommands Cog updated.')

  #Clear
  @commands.command(name='clear', aliases=['c','cl','CL','C'], description="Clears a number of messages, must provide a value")
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount: int):
    if (amount == 0):
      embed=discord.Embed(title="Task Failed!", color=0x003366)
      embed.set_footer(text = "You aren't going to be deleting anything if you put 0, I automatically add 1 to the amount and that will only delete the command request, so please use a larger number.")
      await ctx.send(embed = embed, delete_after = 5)
    elif (amount < 0):
      embed=discord.Embed(title="Task Failed!", color=0x003366)
      embed.set_footer(text = "How do you expect me to delete negative messages? That's not even possible!")
      await ctx.send(embed = embed, delete_after = 5)
    elif (amount > 0 ):
      await ctx.channel.purge(limit = amount + 1)
      embed=discord.Embed(title="Task Completed!", color=0x003366)
      embed.set_footer(text = f"I have deleted {amount} messages!")
      await ctx.send(embed = embed, delete_after = 5)

#Kick
  @commands.command(name='kick', aliases=['k','K', 'KICK'])
  @commands.has_permissions(kick_members=True)
  
  async def kick(self, ctx, member: discord.Member, *, reason=None):
      await ctx.message.delete()
      await member.kick(reason=reason)
      embed=discord.Embed(title="Task completed!", color=0x003366)
      embed.set_footer(text = f'I have kicked {member.mention}!')
      await ctx.send(embed = embed, delete_after = 3)
    
  #Ban
  @commands.command(name='ban', aliases=['b', 'B', 'BAN'])
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

    embed=discord.Embed(title="Task completed!", color=0x003366)
    embed.set_footer(text = f'I have banned {member.mention}!')
    await ctx.send(embed = embed, delete_after = 3)


  #Unban
  @commands.command(name='unban', aliases=['ub', 'UB', 'UNBAN'])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_disciminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_disciminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(title="Task completed!", color=0x003366)
                embed.set_footer(text = f'I have unbanned {member.mention}!')
                await ctx.send(embed = embed, delete_after = 3)
                return


  #Clear Errors
  #Amount to clear not specified
  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "Please specify the amount of messages you are trying to clear!" )
      await ctx.send(embed = embed, delete_after = 3)
  #Missing permission to run command
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed(title="Error", color=0x003366)
      embed.set_footer(text = "You are missing the 'manage messages' permission!" )
      await ctx.send(embed = embed, delete_after = 3)
  
    #Ban Errors
  #Member not specified
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "Please specify who you are trying to ban!" )
      await ctx.send(embed = embed, delete_after = 3)
  #Missing permission to run command
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "You are missing the 'ban members' permission!" )
      await ctx.send(embed = embed, delete_after = 3)

  #Unban error
  #Member not specified
  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "Please specify who you are trying to unban!" )
      await ctx.send(embed = embed, delete_after = 3)
  #Missing Permissions to run command
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "You are missing the 'ban members' permission!" )
      await ctx.send(embed = embed, delete_after = 3)
    
      

  #Kick Errors
  #Member not specified
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "Please specify who you are trying to kick!" )
      await ctx.send(embed = embed, delete_after = 3)
  #Missing Permissions to run command
    if isinstance(error, commands.MissingPermissions):
      embed=discord.Embed(title="Error!", color=0x003366)
      embed.set_footer(text = "You are missing the 'kick members' permission!" )
      await ctx.send(embed = embed, delete_after = 3)

def setup(client):
  client.add_cog(Moderation(client))