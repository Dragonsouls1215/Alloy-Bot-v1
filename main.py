import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle
my_secret = os.environ['TOKEN']

class CustomHelpCommand(commands.HelpCommand):
  def __init__(self):
    super().__init__()


  async def send_bot_help(self,mapping):
    for cog in mapping:
      await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')

    return await super().send_bot_help(mapping)

  async def send_cog_help(self, cog):
    await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')
    return await super().send_cog_help(cog)
  
  async def send_group_help(self, group):
    await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')
    return await super().send_group_help(group)
  
  async def send_command_help(self, command):
    await self.get_destination().send(command.name)
    return await super().send_command_help(command)


client = commands.Bot(command_prefix='!AB ', help_command=commands.MinimalHelpCommand())
status = cycle([
    '!AB help', 'A truely adorable robot!', '!AB help',
    'FLIPPYR, MY NAME IS NOT RICHARD!'
])

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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
client.run(os.getenv('TOKEN'))