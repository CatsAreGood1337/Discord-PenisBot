import requests
import discord
import random
from asyncio import sleep
from discord.ext import commands
from config import settings
from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command( 'help' )
text_filter = ['@everyone']

@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.idle, activity=discord.Game("| $penis"))
          await sleep(10)

@bot.command()
async def penis(ctx):
    penis = "8" + ("=" * random.randint(4, 15)) + "D"
    await ctx.send(penis)

bot.run(settings['token'])