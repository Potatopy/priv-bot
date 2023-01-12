import nextcord
import os

from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
vc1 = os.getenv("CHANNEL_NAME")

class JTC(commands.Cog):
    
    temporary_channels = []

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Join 2 Create system is ready!")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: nextcord.Member, before: nextcord.VoiceState, after: nextcord.VoiceState):
        possible_channel_name = f"{member.name}'s area"
        if after.channel:
            if after.channel.name == vc1:
                temp_channel = await after.channel.clone(name=possible_channel_name)
                await member.move_to(temp_channel)
                self.temporary_channels.append(temp_channel.id)


        if before.channel:
            if before.channel.id in self.temporary_channels:
                if len(before.channel.members) == 0:
                    await before.channel.delete()

def setup(bot):
    bot.add_cog(JTC(bot))