import nextcord
from nextcord.ext import commands

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Util Cog is ready!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! 🏓: {str(round(self.bot.latency * 1000))}ms")

def setup(bot):
    bot.add_cog(Util(bot))