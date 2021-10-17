import discord
import random
from discord.ext import commands
import math

class DnD_Dice(commands.Cog):

  def __intit__(self, client):

    self.client = client

  @commands.Cog.listener()

  async def onready(self):

    print('DnD Dice Cog updated.')
  
  rollvalue = 0
  rollvalue2 = 0
  roll = 0



#Commands

  @commands.command(name = "rolls")
  async def rolls(self, ctx):
    embed = discord.Embed(title="Choose your roll!", color=0x003366)
    embed.add_field(name = "1", value = "Rolls a 1d2/d2", inline = True)
    embed.add_field(name = "2", value = "Rolls a 1d3/d3", inline = True)
    embed.add_field(name = "3", value = "Rolls a 1d4/d4", inline = True)
    embed.add_field(name = "4", value = "Rolls a 1d6/d6", inline = True)
    embed.add_field(name = "5", value = "Rolls a 1d8/d8", inline = True)
    embed.add_field(name = "6", value = "Rolls a 1d10/d10", inline = True)
    embed.add_field(name = "7", value = "Rolls a 1d12/d12", inline = True)
    embed.add_field(name = "8", value = "Rolls a 1d20/d20", inline = True)
    embed.add_field(name = "9", value = "Rolls a 1d100/d100", inline = True)
    embed.set_footer(text = "Use !Ab roll to select the one you want, adjust numbers as needed.")
    await ctx.send(embed = embed, delete_after = 15)
    
  @commands.command(name = "roll")
  async def roll(self, ctx, *, roll: int):
    if roll == 1:
          rollvalue = random.randint(1,2)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 2:
          rollvalue = ((random.randint(1,6) / 2))
          rollvalue = math.ceil(rollvalue)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 3:
          rollvalue = random.randint(1,4)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 4:
          rollvalue = random.randint(1,6)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 5:
          rollvalue = random.randint(1,8)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 6:
          rollvalue = random.randint(1,10)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 7:
          rollvalue = random.randint(1,12)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 8:
          rollvalue = random.randint(1,20)
          embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
          await ctx.send(embed = embed, delete_after = 15)
    elif roll == 9:
          rollvalue = random.randint(1,10)
          
          if rollvalue == 10:
            rollvalue = rollvalue * 10
            embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
            await ctx.send(embed = embed, delete_after = 15)

          elif rollvalue <= 10:
            rollvalue2 = random.randint(1,9)
            rollvalue = rollvalue * 10
            rollvalue = rollvalue + rollvalue2
            embed = discord.Embed(title = f"Your roll is {rollvalue}", color=0x003366)
            await ctx.send(embed = embed, delete_after = 15)
          

    else:
          await ctx.send("Your input is invalid, please try again.")

    
#--------------------------------- 

#Errors

#--------------------------------- 

def setup(client):
  client.add_cog(DnD_Dice(client))
  