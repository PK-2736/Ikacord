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

print("gear3の読み込み完了")

class gear3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(guild_ids=guild_ids, description='ゲソタウン情報を取得します。')
    async def testgear(self, ctx: discord.ApplicationContext):
            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            #%Y-%m-%dT%H:%M:%S%z
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][0]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][0]["gear"]["primaryGearPower"]
            # bgearpoweradd = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd2 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd3 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            bprice = jsonData["pickupBrand"]["brandGears"][0]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][0]["gear"]["image"]["url"]

            # bgear1 = jsonData["results"][0]["stages"][0]["name"]
            # bgear2 = jsonData["results"][0]["stages"][1]["name"]
            # bgear3 = jsonData["results"][0]["stages"][0]["image"]
            # regular_image1 = jsonData["results"][0]["stages"][1]["image"]

            embed = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed.set_footer(text="API: https://api.koukun.jp/| イカコード3")
            embed.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            #%Y-%m-%dT%H:%M:%S%z
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][1]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][1]["gear"]["primaryGearPower"]
            # bgearpoweradd = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd2 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd3 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            bprice = jsonData["pickupBrand"]["brandGears"][1]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][1]["gear"]["image"]["url"]

            # bgear1 = jsonData["results"][0]["stages"][0]["name"]
            # bgear2 = jsonData["results"][0]["stages"][1]["name"]
            # bgear3 = jsonData["results"][0]["stages"][0]["image"]
            # regular_image1 = jsonData["results"][0]["stages"][1]["image"]

            embed2 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}￥**")
            embed2.set_footer(text="API: https://api.koukun.jp/| イカコード3")
            embed2.set_thumbnail(url=bimage)

            url = "https://api.koukun.jp/splatoon/3/geso/"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            btime = jsonData["pickupBrand"]["saleEndTime"]
            t = datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
            #%Y-%m-%dT%H:%M:%S%z
            n = t.strftime('%m/%d %H:%M')
            bgearname = jsonData["pickupBrand"]["brandGears"][2]["gear"]["name"]
            bgearpower = jsonData["pickupBrand"]["brandGears"][2]["gear"]["primaryGearPower"]
            # bgearpoweradd = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd2 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            # bgearpoweradd3 = jsonData["pickupBrand"]["brandGears"]["gear"]["additionalGearPowers"]["name"]
            bprice = jsonData["pickupBrand"]["brandGears"][2]["price"]
            url2 = "https://splatoon3.ink/data/gear.json"
            response = requests.get(url2)
            jsonData = response.json()
            bimage = jsonData["data"]["gesotown"]["pickupBrand"]["brandGears"][2]["gear"]["image"]["url"]

            # bgear1 = jsonData["results"][0]["stages"][0]["name"]
            # bgear2 = jsonData["results"][0]["stages"][1]["name"]
            # bgear3 = jsonData["results"][0]["stages"][0]["image"]
            # regular_image1 = jsonData["results"][0]["stages"][1]["image"]

            embed3 = discord.Embed(
                                        title = "ブランドピックギア",
                                        color=0x457fce,

                                        description=f"**{n}まで**\n\n**{bgearname}**\n\n**{bgearpower}**\n\n**{bprice}**￥")
            embed3.set_footer(text="API: https://api.koukun.jp/| イカコード3")
            embed3.set_thumbnail(url=bimage)

            page = [embed,embed2,embed3]
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
    bot.add_cog(gear3(bot))