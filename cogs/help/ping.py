import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from cogs import guild_ids

print("pingの読み込み完了")

class AppCmdCubotPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=guild_ids, description="Ping値を表示します。")
    async def ping(self, ctx):
        embed = discord.Embed(title="PING", description=f"`PING`：{round(self.bot.latency * 1000)}ms",
                              color=0x3498DB)
        await ctx.respond(embed=embed)

def setup(bot):
    return bot.add_cog(AppCmdCubotPing(bot))