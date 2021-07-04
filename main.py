import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle
import colorama
from colorama import Fore, Style
my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix='!AB ', help_command=commands.MinimalHelpCommand())

client.remove_command(name="help")
status = cycle([
    '!AB h', 'A truely adorable robot!', '!AB h',
    'FLIPPYR, MY NAME IS NOT RICHARD!'
])

#startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!AB help"))
    change_status.start()
    print(Fore.BLUE + '{0.user} is online. '.format(client))


#status loop
@tasks.loop(seconds=45)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#custom help command
@client.command(name="help", aliases=["Help", "h", "H"]) 
async def help(ctx):
  embed=discord.Embed(
      color=ctx.author.color, timestamp=ctx.message.created_at)
  embed.set_author(name= "Bot Commands", icon_url=ctx.author.avatar_url)
  embed.add_field(name="help", value="Shows this message. | Aliases: Help, h, H.", inline=False)
  embed.add_field(name="online", value= "Prints: 'Good morning'. Test command | Aliases: None.", inline = False)
  embed.add_field(name="SiB", value= "Prints: 'Sire is bipolar'. Test command | Aliases: sib, SIB.")
  embed.add_field(name="credits", value= "Prints the credits for bot. | Aliases: CREDITS, cr, CR.", inline = False)
  embed.add_field(name="credits2", value= "Test command. | Aliases: CREDITS2, cr2, CR2.", inline = False)
  embed.add_field(name="richard", value= "Prints: MY NAME IS NOT RICHARD. Joke command | Aliases: None.", inline = False)
  embed.add_field(name="---------------------------------------------------------", value= "Staff Commands.", inline = False)
  embed.add_field(name="clear", value= "Allows the user to clear a number of messages | Aliases: c, C, cl, CL | User Requires 'Manage Messages' Permission.", inline = False)
  embed.add_field(name="kick", value= "Allows the user to kick other users. | Aliases: k, K, KICK | User Requires 'Kick Member' Permission.", inline = False)
  embed.add_field(name="ban", value= "Allows the user to ban other users. | Aliases: b, B, BAN | User Requires 'Ban Member' Permission.", inline = False)
  embed.add_field(name="unban", value= "Allows the user to unban other users. | Aliases: ub, UB, UNBAN | User Requires 'Ban Member' Permission.", inline = False)
  embed.add_field(name="---------------------------------------------------------", value= "Bot Developer Commands, DON'T USE IF YOU DON'T WORK ON THE BOT!", inline = False)
  embed.add_field(name="load", value= "Loads the cog file inputted (enables bot files for everyone), otherwise it will do nothing and print errors on bot's end | Requires administrator permissions", inline= False)
  embed.add_field(name="unload", value= "Unloads the cog file inputted (disables bot files for everyone), otherwise it will do nothing and print errors on bot's end | Requires administrator permissions", inline= False)
  await ctx.send(embed = embed)


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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
client.run(os.getenv('TOKEN'))
