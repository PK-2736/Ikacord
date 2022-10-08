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


print("spla3の読み込み完了")
dt = datetime.now()

class Splatoon3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    spla3 = discord.SlashCommandGroup("ステージ", "フレンドコード関連", guild_ids = guild_ids)

    # @spla3.command(guild_ids = guild_ids, description='レギュラーのステージ情報を取得します。')
    # async def regulartest(self, ctx, time: Option(str, 'test', choices=["test", "test2", "test3"])):

    #     if time == "test":
    #         url = "https://spla3.yuu26.com/api/regular/schedule"
    #         ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
    #         headers = {"User-Agent": ua}
    #         response = requests.get(url)
    #         jsonData = response.json()
    #         regular_maptest0 = jsonData["results"][0]["stages"][0]["name"]
    #         regular_maptest1 = jsonData["results"][0]["stages"][1]["name"]
    #         regular_image0 = jsonData["results"][0]["stages"][0]["image"]
    #         regular_image1 = jsonData["results"][0]["stages"][1]["image"]

    #         img = Image.new('RGB', (800,200), (0, 0, 0))
    #         im1 = Image.open(io.BytesIO(requests.get(regular_image0).content))
    #         im2 = Image.open(io.BytesIO(requests.get(regular_image1).content))
    #         # im1.resize((im1.width // 2, im1.height // 2))
    #         # im2.resize((im2.width // 2, im2.height // 2))
    #         img_binary = io.BytesIO()
    #         img.paste(im1, (405,0))
    #         img.paste(im2, (0,0))
    #         img.save(img_binary, format='PNG')
    #         img_binary.seek(0)

    #         embedtest = discord.Embed(
    #                                     title = "レギュラーマッチ",
    #                                     color=0x00ff00,

    #                                     description=f"**{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点のステージ**\n\n**{regular_maptest0}**\n**{regular_maptest1}**")
    #         file = discord.File(img_binary, filename='image.png')
    #         embedtest.set_image(url="attachment://image.png")
    #         embedtest.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
    #         embedtest.set_footer(text="API: https://spla3.yuu26.com| イカコード3")

    #         await ctx.respond(embed=embedtest,file=file,ephemeral = True)

    #     if time == "test2":
    #         url1 = "https://spla3.yuu26.com/api/regular/schedule"
    #         response = requests.get(url1)
    #         jsonData = response.json()
    #         regular_maptest2 = jsonData["results"][1]["stages"][0]["name"]
    #         regular_maptest3 = jsonData["results"][1]["stages"][1]["name"]
    #         regular_image2 = jsonData["results"][1]["stages"][0]["image"]
    #         regular_image3 = jsonData["results"][1]["stages"][1]["image"]

    #         img1 = Image.new('RGB', (800,200), (0, 0, 0))
    #         im3 = Image.open(io.BytesIO(requests.get(regular_image2).content))
    #         im4 = Image.open(io.BytesIO(requests.get(regular_image3).content))
    #         # im1.resize((im1.width // 2, im1.height // 2))
    #         # im2.resize((im2.width // 2, im2.height // 2))
    #         img_binary1 = io.BytesIO()
    #         img1.paste(im3, (405,0))
    #         img1.paste(im4, (0,0))
    #         img1.save(img_binary1, format='PNG')
    #         img_binary1.seek(0)
    #         embedtest2 = discord.Embed(
    #                                     title = "レギュラーマッチ",
    #                                     color=0x00ff00,

    #                                     description=f"**{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点のステージ**\n\n**{regular_maptest2}**\n**{regular_maptest3}**")
    #         file1 = discord.File(img_binary1, filename='image1.png')
    #         embedtest2.set_image(url="attachment://image1.png")
    #         embedtest2.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
    #         embedtest2.set_footer(text="API: https://spla3.yuu26.com| イカコード3")
    
    #         await ctx.respond(embed=embedtest2,file=file1,ephemeral = True)

    # @spla3.command(name='バンカラチャレンジ', guild_ids = guild_ids, description='バンカラチャレンジのステージ情報を取得します。')
    # async def bankarachallenge(self, ctx):

    #     url = "https://spla3.yuu26.com/api/bankara-challenge/now"
    #     url_2 = "https://spla3.yuu26.com/api/bankara-challenge/next"
    #     ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
    #     headers = {"User-Agent": ua}

    #     response = requests.get(url)
    #     jsonData = response.json()

    #     ranked_mode = jsonData["results"][0]["rule"]["name"]
    #     ranked_map0 = jsonData["results"][0]["stages"][0]["name"]
    #     ranked_map1 = jsonData["results"][0]["stages"][1]["name"]

    #     response = requests.get(url_2)
    #     jsonData = response.json()

    #     ranked_nextmode = jsonData["results"][0]["rule"]["name"]
    #     ranked_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
    #     ranked_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

    #     ranked_embed = discord.Embed(
    #                                 title = "バンカラチャレンジ",
    #                                 color=0xff0000,
    #                                 description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
    #     ranked_embed.add_field(name=f"いま: **{ranked_mode}**", value=f"つぎ: **{ranked_nextmode}**", inline=False)
    #     ranked_embed.add_field(name=f"いま: **{ranked_map0}** / **{ranked_map1}**",
    #                           value=f"つぎ: **{ranked_nextmap0}** / **{ranked_nextmap1}**",
    #                           inline=False)
    #     ranked_embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
    #     ranked_embed.set_footer(text="API: https://spla3.yuu26.com")

    #     await ctx.respond(embed=ranked_embed,ephemeral = True)

    # @spla3.command(name='バンカラオープン', guild_ids = guild_ids, description='バンカラオープンのステージ情報を取得します。')
    # async def bankaraopen(self, ctx):

    #     url = "https://spla3.yuu26.com/api/bankara-open/now"
    #     url_2 = "https://spla3.yuu26.com/api/bankara-open/next"
    #     ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
    #     headers = {"User-Agent": ua}

    #     response = requests.get(url)
    #     jsonData = response.json()

    #     league_mode = jsonData["results"][0]["rule"]["name"]
    #     league_map0 = jsonData["results"][0]["stages"][0]["name"]
    #     league_map1 = jsonData["results"][0]["stages"][1]["name"]

    #     response = requests.get(url_2)
    #     jsonData = response.json()

    #     league_nextmode = jsonData["results"][0]["rule"]["name"]
    #     league_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
    #     league_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

    #     league_embed = discord.Embed(
    #                                 title = "バンカラオープン",
    #                                 color=0xffc0cb,
    #                                 description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
    #     league_embed.add_field(name=f"いま: **{league_mode}**", value=f"つぎ: **{league_nextmode}**", inline=False)
    #     league_embed.add_field(name=f"いま: **{league_map0}** / **{league_map1}**",
    #                            value=f"つぎ: **{league_nextmap0}** / **{league_nextmap1}**",
    #                            inline=False)
    #     league_embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
    #     league_embed.set_footer(text="API: https://spla3.yuu26.com")

    #     await ctx.respond(embed=league_embed,ephemeral = True)

    # @spla3.command(name='サーモンラン', guild_ids = guild_ids, description='サーモンランのステージ情報を取得します。')
    # async def coopa(self, ctx):

    #     url = "https://spla3.yuu26.com/api/coop-grouping-regular/now"
    #     url2 = "https://spla3.yuu26.com/api/coop-grouping-regular/next"
    #     ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
    #     headers = {"User-Agent": ua}

    #     response = requests.get(url)
    #     jsonData = response.json()

    #     # 現在のサーモンランのデータを取得

    #     salmon_map   = jsonData["results"][0]["stage"]["name"]
    #     salmon_wpn_1 = jsonData["results"][0]["weapons"][0]["name"]
    #     salmon_wpn_2 = jsonData["results"][0]["weapons"][1]["name"]
    #     salmon_wpn_3 = jsonData["results"][0]["weapons"][2]["name"]
    #     salmon_wpn_4 = jsonData["results"][0]["weapons"][3]["name"]


    #     response = requests.get(url2)
    #     jsonData = response.json()

    #     salmon_map2   = jsonData["results"][0]["stage"]["name"]
    #     salmon_wpn_5 = jsonData["results"][0]["weapons"][0]["name"]
    #     salmon_wpn_6 = jsonData["results"][0]["weapons"][1]["name"]
    #     salmon_wpn_7 = jsonData["results"][0]["weapons"][2]["name"]
    #     salmon_wpn_8 = jsonData["results"][0]["weapons"][3]["name"]

    #     salmon_embed = discord.Embed(
    #                                 title = "サーモンラン",
    #                                 color = 0xff7f50)
    #     salmon_embed.add_field(name=f"いま\nブキ: {salmon_wpn_1}, {salmon_wpn_2}, {salmon_wpn_3}, {salmon_wpn_4}",
    #                            value=f"ステージ: **{salmon_map}**",
    #                            inline=False)
    #     salmon_embed.add_field(name=f"つぎ\nブキ: {salmon_wpn_5}, {salmon_wpn_6}, {salmon_wpn_7}, {salmon_wpn_8}",
    #                            value=f"ステージ: **{salmon_map2}**",
    #                            inline=False)
    #     salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
    #     salmon_embed.set_footer(text="API: https://spla3.yuu26.com")

    #     await ctx.respond(embed=salmon_embed,ephemeral = True)


    # @tasks.loop(seconds=1)
    # async def loop(self):
    #     # 現在の時刻
    #     await self.bot.wait_until_ready()
    #     now = datetime.now().strftime('%H:%M')
    #     if now == '22:28':
    #         channel = self.bot.get_channel(803029346088517683)
    #         if channel is not None:
    #             await channel.send('おはよう')  
    #     else:
    #         print("error")

    @slash_command(name='ランダム武器', guild_ids = guild_ids, description='Splatoon3の武器をランダムに抽選')
    async def rw(self, message):
            json_open = open('data/spla3.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            buki = random.choice(json_data)
            ja_name = buki["name"]["ja_JP"]
            path = "images/main/" + buki["name"]["ja_JP"] + ".jpg"
            file = discord.File(path, filename="image.png")
            user = message.author.display_name
            rw = discord.Embed(title = f"{user}さんにおすすめのブキは\n{ja_name}！",)
            #rw.add_field(name=f"{user}さんにおすすめのブキは",value=f"{ja_name}！")
            rw.set_image(url="attachment://image.png")
            await message.respond(file=file,embed=rw)

    @slash_command(name='ギア表', guild_ids = guild_ids, description='Splatoon3のブランド別ギア表を表示')
    async def gear(self, message):
            gear = discord.File("images/gear.jpg", filename="gear.png")
            brands = discord.Embed()
            brands.set_image(url="attachment://gear.png")
            await message.respond(file=gear,embed=brands)

    @slash_command(name='ダメージ表', guild_ids = guild_ids, description='Splatoon3の武器別ダメージ表を表示')
    async def damage(self, message):
            damage = discord.File("images/damage.jpg", filename="damage.png")
            brands = discord.Embed()
            brands.set_image(url="attachment://damage.png")
            await message.respond(file=damage,embed=brands)
       
def setup(bot):
    bot.add_cog(Splatoon3(bot))