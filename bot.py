import discord
from discord.ext import commands
from discord import app_commands
import os
import importlib
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

async def load_commands():
  commands_path = Path("commands")
  for file in commands_path.glob("*.py"):
    if file.name == "__init__.py":
      continue
    module_name = f"commands.{file.stem}"
    module = importlib.import_module(module_name)
    for attr in dir(module):
      cmd = getattr(module, attr)
      if isinstance(cmd, app_commands.Command):
        tree.add_command(cmd)

@bot.event
async def on_ready():
  print(f"Bot is online as {bot.user}")
  await load_commands()
  try:
    synced = await tree.sync()
    print(f"Synced {len(synced)} command(s) to guild.")
  except Exception as e:
    print(f"Failed to sync commands: {e}")

bot.run(DISCORD_BOT_TOKEN)