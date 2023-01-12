import discord_ios
import nextcord
import os

from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

intents = nextcord.Intents.all()
activity = nextcord.Activity(type=nextcord.ActivityType.competing, name=f"{prefix}help")
bot = commands.Bot(command_prefix=prefix, intents=intents, activity=activity)

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

@bot.event
async def on_ready():
    print("\n" * 100)
    print("""

██████╗░░█████╗░████████╗░█████╗░████████╗░█████╗░  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██║░░██║░░░██║░░░███████║░░░██║░░░██║░░██║  ██████╦╝██║░░██║░░░██║░░░
██╔═══╝░██║░░██║░░░██║░░░██╔══██║░░░██║░░░██║░░██║  ██╔══██╗██║░░██║░░░██║░░░
██║░░░░░╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░╚█████╔╝  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░

© 2023 by h3lped
""")
    print(f"Bot is ready || Logged in as {bot.user} ID: {bot.user.id}")
    print("-----------------")

bot.run(TOKEN)