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

print("bankaraopenstageの読み込み完了")

class bankaraopen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name='バンカラオープン', guild_ids = guild_ids, description='バンカラオープンのステージ情報を取得します。')
    async def bankaraopen(self, ctx, time : Option(str, '時間', choices=["今", "次", "次の次"])):

        if time == "今":
            url = "https://spla3.yuu26.com/api/bankara-open/schedule"
            ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
            headers = {"User-Agent": ua}
            response = requests.get(url)
            jsonData = response.json()
            rule = jsonData["results"][0]["rule"]["name"]
            map = jsonData["results"][0]["stages"][0]["name"]
            map2 = jsonData["results"][0]["stages"][1]["name"]
            time = jsonData["results"][0]["start_time"]
            time2 = jsonData["results"][0]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t.strftime('%H:%M')
            image = jsonData["results"][0]["stages"][0]["image"]
            image2 = jsonData["results"][0]["stages"][1]["image"]

            img = Image.new('RGB', (800,200), (0, 0, 0))
            im1 = Image.open(io.BytesIO(requests.get(image).content))
            im2 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary = io.BytesIO()
            img.paste(im1, (405,0))
            img.paste(im2, (0,0))
            img.save(img_binary, format='PNG')
            img_binary.seek(0)

            embed = discord.Embed(
                                        title = "バンカラオープン",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file = discord.File(img_binary, filename='image.png')
            embed.set_image(url="attachment://image.png")
            embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

            await ctx.respond(embed=embed,file=file)

        if time == "次":
            url1 = "https://spla3.yuu26.com/api/bankara-open/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][1]["rule"]["name"]
            map = jsonData["results"][1]["stages"][0]["name"]
            map2 = jsonData["results"][1]["stages"][1]["name"]
            time = jsonData["results"][1]["start_time"]
            time2 = jsonData["results"][1]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t.strftime('%H:%M')
            image = jsonData["results"][1]["stages"][0]["image"]
            image2 = jsonData["results"][1]["stages"][1]["image"]

            img1 = Image.new('RGB', (800,200), (0, 0, 0))
            im3 = Image.open(io.BytesIO(requests.get(image).content))
            im4 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary1 = io.BytesIO()
            img1.paste(im3, (405,0))
            img1.paste(im4, (0,0))
            img1.save(img_binary1, format='PNG')
            img_binary1.seek(0)
            embed2 = discord.Embed(
                                        title = "バンカラオープン",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file1 = discord.File(img_binary1, filename='image1.png')
            embed2.set_image(url="attachment://image1.png")
            embed2.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed2.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
    
            await ctx.respond(embed=embed2,file=file1)

        if time == "次の次":
            url1 = "https://spla3.yuu26.com/api/bankara-open/schedule"
            response = requests.get(url1)
            jsonData = response.json()
            rule = jsonData["results"][2]["rule"]["name"]
            map = jsonData["results"][2]["stages"][0]["name"]
            map2 = jsonData["results"][2]["stages"][1]["name"]
            time = jsonData["results"][2]["start_time"]
            time2 = jsonData["results"][2]["end_time"]
            t = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
            n = t.strftime('%H:%M')
            t2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S%z')
            n2 = t2.strftime('%H:%M')
            image = jsonData["results"][2]["stages"][0]["image"]
            image2 = jsonData["results"][2]["stages"][1]["image"]

            img2 = Image.new('RGB', (800,200), (0, 0, 0))
            im5 = Image.open(io.BytesIO(requests.get(image).content))
            im6 = Image.open(io.BytesIO(requests.get(image2).content))
            img_binary2 = io.BytesIO()
            img2.paste(im5, (405,0))
            img2.paste(im6, (0,0))
            img2.save(img_binary2, format='PNG')
            img_binary2.seek(0)
            embed3 = discord.Embed(
                                        title = "バンカラオープン",
                                        color=0xdb4a13,

                                        description=f"**{n}から{n2}まで**\n\n**{rule}**\n\n**{map}**\n**{map2}**")
            file2 = discord.File(img_binary2, filename='image2.png')
            embed3.set_image(url="attachment://image2.png")
            embed3.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
            embed3.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
    
            await ctx.respond(embed=embed3,file=file2)


def setup(bot):
    bot.add_cog(bankaraopen(bot))
