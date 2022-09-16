from discord.ext import commands
import discord
import psutil
import datetime
from discord.ui import View, Button
from discord.ext import commands
from cogs import guild_ids

print("clientの読み込み完了")

class client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = discord.SlashCommandGroup("ボット", "bot関連", guild_ids=guild_ids)

    @commands.is_owner()
    @bot.command(guild_ids=guild_ids, description="BOTをシャットダウン")
    async def client_close(self, ctx):
        client = self.bot
        await ctx.respond("Botアカウントからログアウトします。")
        await client.close()
        
    @bot.command(guild_ids=guild_ids, description="BOTの情報表示2")
    async def client_info(self, ctx):
        client = self.bot
        await ctx.respond(
            f"Botユーザー名: {client.user.name}\n"
            f"BotユーザーID: {client.user.id}\n"
            f"Guild数: {len(client.guilds)}\n"
            f"ボイス接続数: {len(client.voice_clients)}\n"
            f"ユニークユーザー数: {len(client.users)}\n"
            f"延べユーザー数: {sum([g.member_count for g in client.guilds])}\n"
        )

    @bot.command(guild_ids=guild_ids, description="BOTの情報表示")
    async def client_application_info(self, ctx):
        client = self.bot
        app_info = await client.application_info()
        await ctx.respond(
            f"アプリケーションID: {app_info.id}\n"
            f"Botオーナー: {app_info.owner.name}\n"
            f"Public Bot?: {app_info.bot_public}\n"
        )

    @bot.command(guild_ids=guild_ids, description="BOT稼働状況確認")
    async def systeminfo(self, ctx):
        embed = discord.Embed(title="Systeminfo", timestamp=datetime.datetime.now())
        embed.add_field(name="CPU Cores", value=psutil.cpu_count(), inline=False)
        embed.add_field(name="CPU", value=psutil.cpu_percent(1), inline=False)
        embed.add_field(name="RAM", value=psutil.virtual_memory()[2], inline=False)
        await ctx.respond(embed=embed, delete_after=60)
        
def setup(bot):
    bot.add_cog(client(bot))