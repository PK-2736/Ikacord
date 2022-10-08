import discord
from discord.ext import commands
from discord import SlashCommand, Option, SlashCommandGroup, option, OptionChoice, AllowedMentions
import config
from datetime import datetime, timedelta, timezone
from discord import Button, ButtonStyle, SelectMenu, SelectOption
from cogs import guild_ids

bot = commands.Bot(command_prefix='p.', intents=discord.Intents.all())
#管理者用 = bot.create_group("管理者用", "管理者用コマンド", guild_ids = guild_ids)

@bot.event
async def on_shard_ready(shard_id):
    print(f"shard: {shard_id} has loaded")

@bot.event
async def on_ready():
    print("起動成功!")
    print("Pycord バージョン: " + str(discord.__version__))
    print("    ________")
    print("Spla-server!")
    print("管理者PheyK")

@bot.event
async def on_member_join(member) :
    print(f"{member} has joined the server")

@bot.event
async def on_member_remove(member) :
    print(f"{member} has left the server")

# @commands.is_owner()
# @管理者用.command(guild_ids = guild_ids, description="cogsファイルをリロード")
# async def reload(ctx, module_name: Option(str, "例：cog.commands.spla")):
#         await ctx.respond(f"モジュール{module_name}の再読み込みを開始します。")
#         try:
#             bot.reload_extension(module_name)
#             await ctx.send(f"モジュール{module_name}の再読み込みを終了しました。")
#         except (commands.errors.ExtensionNotLoaded, commands.errors.ExtensionNotFound,
#                 commands.errors.NoEntryPointError, commands.errors.ExtensionFailed) as e:
#             await ctx.respond(f"モジュール{module_name}の再読み込みに失敗しました。理由：{e}")
#             return

# @commands.is_owner()
# @管理者用.command(guild_ids = guild_ids, description="cogsファイルをロード")
# async def load(ctx, extension) :
#     bot.load_extension(f'cogs.{extension}')

# @commands.is_owner()
# @管理者用.command(guild_ids = guild_ids, description="cogsファイルをアンロード")
# async def unload(ctx, extension) :
#     bot.unload_extension(f'cogs.{extension}')

  
#cogs reload

#bot.load_extension("cogs.test")
#bot.load_extension("cogs.test2")

bot.load_extension("cogs.help.help")
bot.load_extension("cogs.help.botuse")
bot.load_extension("cogs.help.description")
bot.load_extension("cogs.help.rule")

bot.load_extension("cogs.stage.regularstage")
bot.load_extension("cogs.stage.bankarachallengestage")
bot.load_extension("cogs.stage.bankaraopenstage")
bot.load_extension("cogs.stage.coopstage")

bot.load_extension("cogs.rect.private")
bot.load_extension("cogs.rect.bankara-open")
bot.load_extension("cogs.rect.coop")
bot.load_extension("cogs.rect.regular")
bot.load_extension("cogs.rect.rectspla3")
bot.load_extension("cogs.rect.festival")

bot.load_extension("cogs.spla.spla3")
bot.load_extension("cogs.spla.gear")
bot.load_extension("cogs.spla.fc")

#bot.load_extension("cogs.Twitter")
#bot.load_extension("cogs.client")
bot.load_extension("cogs.event")

bot.run(config.token)