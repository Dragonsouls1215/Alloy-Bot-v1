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

#status loop
@tasks.loop(seconds=45)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#Cogs (Make sure to specify what cog you want to reload)
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command(name= "help", aliases=["h", "H", "HELP"]) 
async def help(ctx):
  embed=discord.Embed(title="Bot Commands", url = "https://Alloy-Bot-V1.ifrostvsdread.repl.co", color=0x003366)

  embed.add_field(name = "help", value = "prints this message | Aliases: Help, h , H", inline = False)
  embed.add_field(name = "online", value = "prints 'Good morning', test command | Aliases: none", inline = False)
  embed.add_field(name = "SiB", value = "prints 'Sire is bipolar', test command | Aliases: sib, SIB", inline = False)
  embed.add_field(name = "credits", value = "prints the credits for the bot | Aliases: CREDITS, cr, CR", inline = False)
  embed.add_field(name = "credits2", value = "prints test command | Aliases: CREDITS2, cr2, CR2", inline = False)
  embed.add_field(name = "richard", value = "prints 'MY NAME IS NOT RICHARD' (Joke command because Flippyr keeps calling him Richard Bot) | Aliases: none", inline = False)
  await ctx.send(embed=embed)

  embed=discord.Embed(title="Staff Commands", url = "https://Alloy-Bot-V1.ifrostvsdread.repl.co", color=0x003366)

  embed.add_field(name = "clear", value = "Allows the user to clear a number of messages | Aliases: c, C , CL", inline = False)
  embed.add_field(name = "kick", value = "Allow's the user to kick other users, requires 'kick members' permission | Aliases: k, K , KICK", inline = False)
  embed.add_field(name = "ban", value = "Allows the user to ban users, requires 'ban members' permission | Aliases: b, B, BAN", inline = False)
  embed.add_field(name = "unban", value = "Allows the user to unban users, requires 'ban members' permission | Aliases: ub, UB, UNBAN", inline = False)
  
  await ctx.send(embed=embed)

  embed=discord.Embed(title="Developer Commands", url = "https://Alloy-Bot-V1.ifrostvsdread.repl.co", color=0x003366)

  embed.add_field(name = "loadcog", value = "Loads the cogfile inputted", inline = False)
  embed.add_field(name = "unloadcog", value = "Unloads the cogfile inputted", inline = False)
  embed.add_field(name = "reload", value = "Reloads the cogfile inputted", inline = False)
  embed.set_footer(text="**DO NOT USE DEVELOPER COMMANDS IF YOU DON'T WORK ON THE BOT!**")
  em = discord.Embed(description='requested by:\n{0}'.format(ctx.author))
  em.set_thumbnail(url=ctx.author.avatar_url)
  
  await ctx.send(embed=embed)
  await ctx.send("Attached to all the embeds is a link to the bot's hosting website which has all the commands available")



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
client.run(os.getenv('TOKEN'))