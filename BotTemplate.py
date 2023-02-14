import discord
from CONFIG import token, CMDS_DIR
import datetime
import pytz
import os
import pathlib
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import Bot

time = datetime.datetime.now()
mst_now = time.astimezone(pytz.timezone('America/Denver'))
mst_format= mst_now.strftime("%Y/%m/%d %H:%M:%S")

intents = discord.Intents.all()
bot = Bot(command_prefix='!', intents = intents)
TOKEN = token

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game('Vibin'))
  print(f'Bot connected as {bot.user}')
  print(mst_format)
  for cmd_file in CMDS_DIR.glob('*.py'):
    if cmd_file.name != '__BotTemplate__.py':
      await bot.load_extension(f'cmds.{cmd_file.name[:-3]}')
  await bot.tree.sync()

@bot.tree.command(name="ping", description="Checking latency")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message('Pong! Took {0} ms'.format(round(bot.latency, 1)))

bot.run(TOKEN)