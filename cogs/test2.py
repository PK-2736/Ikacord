from discord.ext import tasks, commands
import discord
from discord.commands import slash_command, Option
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import requests
import json
from discord.ext import pages
from cogs import guild_ids
import io

print("test2の読み込み完了")


class AppCmdCubotHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=guild_ids, description="ヘルプを表示します。")
    async def testgear(self, ctx: discord.ApplicationContext):
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            bname = jsonData["pickupBrand"]["brand"]["name"]
            bpower = jsonData["pickupBrand"]["brand"]["usualGearPower"]["name"]
            bdesc = jsonData["pickupBrand"]["brand"]["usualGearPower"]["desc"]
            # bgear1 = jsonData["results"][0]["stages"][0]["name"]
            # bgear2 = jsonData["results"][0]["stages"][1]["name"]
            # bgear3 = jsonData["results"][0]["stages"][0]["image"]
            # regular_image1 = jsonData["results"][0]["stages"][1]["image"]

            embed = discord.Embed(
                                        title = "ピックギア",
                                        color=0x00ff00,

                                        description=f"**{bname}**\n\n{bpower}\n{bdesc}")
            embed.set_footer(text="API: https://api.koukun.jp/| イカコード3")
            embed.set_thumbnail(url="https://cdn.wikiwiki.jp/to/w/splatoon2ch/%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89/::ref/Skalop2.png?rev=b52ac6a666cc956be52585e7a045ffdd&t=20160113164100")
            await ctx.respond(embed=embed) 

            page = [embed, ]
            paginator = pages.Paginator(pages=page)
            paginator.add_button(pages.PaginatorButton(
                "first", label="<<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "prev", label="<", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "page_indicator", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "next", label=">", style=discord.ButtonStyle.primary))
            paginator.add_button(pages.PaginatorButton(
                "last", label=">>", style=discord.ButtonStyle.primary))
            await paginator.respond(ctx.interaction, ephemeral=False)


def setup(bot):
    return bot.add_cog(AppCmdCubotHelp(bot))