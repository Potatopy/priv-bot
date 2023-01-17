import nextcord
import os

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
p = os.getenv("PREFIX")

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Util Cog is ready!")

    @commands.group()
    async def util(self, ctx):
        pass
    
    @commands.command()
    async def echo(self, ctx, *, arg = ""):
        if arg == "":
            await ctx.send("Please enter a message to echo")
        else:
            await ctx.message.delete()
            await ctx.send(arg)
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! 🏓: {str(round(self.bot.latency * 1000))}ms")
    
    @util.command()
    async def help(self, ctx):
        em = nextcord.Embed(title="Util Help", description="Commands:")
        em.add_field(name=f"**{p}ping**", value="Shows the bot's latency", inline=False)
        em.set_footer(text="More commands will be added soon!")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Util(bot))