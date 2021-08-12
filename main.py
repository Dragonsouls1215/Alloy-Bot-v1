import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle
my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix='!AB ', help_command=commands.MinimalHelpCommand())
status = cycle([
    '!AB help', 'A truely adorable robot!', '!AB help', 
    'FLIPPYR, MY NAME IS NOT RICHARD!'
])

client.remove_command('help')

#startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!AB help"))
    change_status.start()
    print('{0.user} is online. '.format(client))

#Variables
bclient = discord.client

#Status loop
@tasks.loop(seconds=45)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#Cogs (Make sure to specify what cog you want to reload)
@client.command()
@commands.has_permissions(administrator=True)
async def loadcog(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Success!", value = f"{extension} cog has been loaded!")
    await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(administrator=True)
async def reloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Success!", value = f"Cog {extension} has been reloaded!")
    await ctx.send(embed = embed)


@client.command()
@commands.has_role(860304775592935457)
async def unloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    ctx.send(f'{extension} cog unloaded')
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Success!", value = f"{extension} cog has been unloaded!")
    await ctx.send(embed = embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Server List
@client.command() 
@commands.has_role(860304775592935457)
async def slist(ctx):

  serverlist = client.guilds
  
  
  op = str(serverlist)
  

  slWrite = open("serverlist.md", 'w')
  slWrite.write(f"""
  
  Server List: {op}, 
  """)
  slWrite.close()

  embed = discord.Embed(title = "Task Complete!", color = 0x003366)
  embed.add_field(name = f"{ctx.author}, Refer to the following file:", value = "serverlist.md", inline = False)
  embed.add_field(name = "Or", value = "Below this embed is the list (if it doesn't print, it means that the list is too long)", inline = False)
  embed.set_footer(text = "You can also check serverlist.md by using the following link as well: https://replit.com/@IFrostvsDread/Alloy-Bot-V1")
  await ctx.send(embed = embed)
  await ctx.send(f"```List of servers with ID's, Names, Shards, and Member Counts: {op}```")

#Help Command
@client.command(name= "help", aliases=["h", "H", "HELP"]) 
async def help(ctx):
  embed=discord.Embed(title="Bot Commands", color=0x003366)

  embed.add_field(name = "help", value = "prints this message | Aliases: Help, h , H", inline = True)
  embed.add_field(name = "online", value = "prints 'Good morning', test command | Aliases: none", inline = True)
  embed.add_field(name = "SiB", value = "prints 'Sire is bipolar', test command | Aliases: sib, SIB", inline = True)
  embed.add_field(name = "credits", value = "prints the credits for the bot | Aliases: CREDITS, cr, CR", inline = True)
  embed.add_field(name = "credits2", value = "prints test command | Aliases: CREDITS2, cr2, CR2", inline = True)
  embed.add_field(name = "richard", value = "prints 'MY NAME IS NOT RICHARD' (Joke command because Flippyr keeps calling him Richard Bot) | Aliases: none", inline = True)
  await ctx.send(embed=embed)

  embed=discord.Embed(title="Staff Commands",color=0x003366)

  embed.add_field(name = "clear", value = "Allows the user to clear a number of messages | Aliases: c, C , CL", inline = True)
  embed.add_field(name = "kick", value = "Allow's the user to kick other users, requires 'kick members' permission | Aliases: k, K , KICK", inline = True)
  embed.add_field(name = "ban", value = "Allows the user to ban users, requires 'ban members' permission | Aliases: b, B, BAN", inline = True)
  embed.add_field(name = "unban", value = "Allows the user to unban users, requires 'ban members' permission | Aliases: ub, UB, UNBAN", inline = True)
  embed.set_footer(text= 'These commands will only work if you have "Administrator" or the matching permissions for each command!')
  await ctx.send(embed=embed)

  embed=discord.Embed(title="Developer Commands", color=0x003366)

  embed.add_field(name = "loadcog", value = "Loads the cogfile inputted", inline = True)
  embed.add_field(name = "unloadcog", value = "Unloads the cogfile inputted", inline = True)
  embed.add_field(name = "reloadcog", value = "Reloads the cogfile inputted", inline = True)
  embed.set_footer(text="Developer commands only work in my test server and are reserved for 'Alloy Bot Developers'!")
  em = discord.Embed(description='requested by:\n{0}'.format(ctx.author))
  em.set_thumbnail(url=ctx.author.avatar_url)
  
  await ctx.send(embed=embed)

#Error's

@slist.error
async def serverlisterror(ctx, error):
  if isinstance(error, commands.MissingRole):
    embed = discord.Embed(title= "Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = 'Reason: You need to have the "Alloy Bot Developer" role in my test server!', inline = True)
    await ctx.send(embed = embed)

@reloadcog.error
async def reloadcogerror(ctx, error):
  if isinstance(error, commands.MissingRole):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name="Error!",value = "Reason: Only users with 'Alloy Bot Developer' in my test server can run this command", inline = True)
    await ctx.send(embed = embed)

  if isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = "Reason: Please input the name of the file you are trying to load!")
    await ctx.send(embed = embed)

@loadcog.error
async def loadcogerror(ctx, error):
  if isinstance(error, commands.MissingRole):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = "Reason: You do not have permission to use this command!")
    embed.add_field(name = "Requirements", value = 'You need to have the "Alloy Bot Developer" role in my test server!', inline = True) 
    await ctx.send(embed = embed)

  if isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = "Reason: Please input the name of the file you are trying to load!")
    await ctx.send(embed = embed)

@unloadcog.error
async def unloadcogerror(ctx, error):
  if isinstance(error, commands.MissingRole):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = "Reason: You do not have permission to use this command!")
    embed.add_field(name = "Requirements", value = 'You need to have the "Alloy Bot Developer" role in my test server!', inline = True)
    await ctx.send(embed = embed)

  if isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title="Task Result", color=0x003366)
    embed.add_field(name = "Error!", value = "Reason: Please input the correct name of the file you are trying to unload!")
    await ctx.send(embed = embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed=discord.Embed(title="Task Result", color=0x003366)
      embed.add_field(name = "Error!", value = "Reason: Invalid command detected! Please refer to !AB help for commands I can complete!")
      await ctx.send(embed = embed)

keep_alive()
client.run(os.getenv('TOKEN'))