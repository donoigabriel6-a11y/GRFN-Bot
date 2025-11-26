import discord
from discord.ext import commands, tasks

import os
TOKEN = os.environ["MTQ0MzEwNjQ3MTk2MDEyMTM2NA.G04Dvb.wVGnEmukGdWEykRIqK8-rmTMZL7JRRrsG-dFzc"]
GUILD_ID = 1428919783574999204
CHANNEL_ID = 1443109090560708680  # ID of "Members: Loading"

# --- Discord Intents ---
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")
    update_member_count.start()


@tasks.loop(minutes=1)
async def update_member_count():
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Guild not found!")
        return

    channel = guild.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found!")
        return

    new_name = f"Members: {guild.member_count}"
    await channel.edit(name=new_name)
    print(f"Updated channel name → {new_name}")


bot.run(TOKEN)

