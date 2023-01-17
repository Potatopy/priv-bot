import aiosqlite
import asyncio
import nextcord
import random

from nextcord.ext import commands

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self, message):
        print("Level cog is ready")
        db = await aiosqlite.connect("db/level.db")
        async with db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS levels (level INT, xp, INT, user INT, guild INT)")

    @commands.Cog.listener()
    async def on_message(self, message): 
        db = await aiosqlite.connect("db/level.db")
        if message.author.bot:
            return
        author = message.author
        guild = message.guild
        async with db.cursor() as cursor:
            await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id))
            xp = await cursor.fetchone()
            await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id))
            level = await cursor.fetchone()

            if not xp or not level:
                await cursor.execute("INSERT INTO levels VALUES (?, ?, ?, ?)", (0, 0, author.id, guild.id))
                await db.commit()
            
            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0

            if level < 5:
                xp += random.randint(5, 10) # chaneable xp gain
                await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
            else:
                rand = random.randint(1, (level // 4)) # changeable xp gain
                if rand == 1:
                    xp += random.randint(5, 10)
                    await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
            if xp >= 100:
                level += 1
                await cursor.execute("UPDATE levels SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id))
                await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id))
                await message.channel.send(f"{author.mention} has leveled up to level **{level}**!")

    @commands.command(aliases=['lvl', 'rank', 'r'])
    async def level(self, ctx, member: nextcord.Member = None):
        db = await aiosqlite.connect("db/level.db")
        if member is None:
            member = ctx.author
        async with db.cursor() as cursor:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
                xp = await cursor.fetchone()
                await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
                level = await cursor.fetchone()

                if not xp or not level:
                    await cursor.execute("INSERT INTO levels VALUES (?, ?, ?, ?)", (0, 0, author.id, guild.id))
                    await db.commit()
                
                try:
                    xp = xp[0]
                    level = level[0]
                except TypeError:
                    xp = 0
                    level = 0

                em = nextcord.Embed(title=f"{member.name}'s Level", description=f"Level: **{level}**\nXP: **{xp}**")
                await ctx.send()
    
    @commands.group()
    async def level(self, ctx):
        pass

    @level.command()
    async def help(self, ctx):
        await ctx.send("Coming Soon!")

def setup(bot):
    bot.add_cog(Level(bot))