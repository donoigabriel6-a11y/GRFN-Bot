import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()  # loads DISCORD_TOKEN from .env file

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

