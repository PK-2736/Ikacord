from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
from datetime import datetime
import requests
import json
from discord.ext import pages
from cogs import guild_ids


class Splatoon3event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=1)
    async def loop(self):
        # 現在の時刻
        await self.bot.wait_until_ready()
        now = datetime.now().strftime('%H:%M')
        if now == '22:28':
            channel = self.bot.get_channel(803029346088517683)
            if channel is not None:
                await channel.send('おはよう')  
        else:
            print("error")

def setup(bot):
    bot.add_cog(Splatoon3event(bot))