from discord.ext import tasks, commands
import discord as discord

from discord.commands import slash_command, Option
import random
from datetime import datetime
import requests
import json
from cogs import guild_ids

print("spla3の読み込み完了")
dt = datetime.now()

class Splatoon3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    spla3 = discord.SlashCommandGroup("ステージ", "フレンドコード関連", guild_ids = guild_ids)

    @spla3.command(guild_ids = guild_ids, description='レギュラーのステージ情報を取得します。')
    async def レギュラー(self, ctx):

        url = "https://spla3.yuu26.com/api/regular/now"
        url_2 = "https://spla3.yuu26.com/api/regular/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        regular_map0 = jsonData["results"][0]["stages"][0]["name"]
        regular_map1 = jsonData["results"][0]["stages"][1]["name"]

        response = requests.get(url_2)
        jsonData = response.json()

        regular_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
        regular_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

        regular_embed = discord.Embed(
                                    title = "レギュラーマッチ（ナワバリバトル）",
                                    color=0x00ff00,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のステージ情報")
        regular_embed.add_field(name=f"いま: **{regular_map0}** / **{regular_map1}**",
                                value=f"つぎ: **{regular_nextmap0}** / **{regular_nextmap1}**",
                                inline=False)
        regular_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
        regular_embed.set_footer(text="API: https://spla3.yuu26.com")

        await ctx.respond(embed=regular_embed,ephemeral = True)

    @spla3.command(guild_ids = guild_ids, description='バンカラチャレンジのステージ情報を取得します。')
    async def バンカラチャレンジ(self, ctx):

        url = "https://spla3.yuu26.com/api/bankara-challenge/now"
        url_2 = "https://spla3.yuu26.com/api/bankara-challenge/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        ranked_mode = jsonData["results"][0]["rule"]["name"]
        ranked_map0 = jsonData["results"][0]["stages"][0]["name"]
        ranked_map1 = jsonData["results"][0]["stages"][1]["name"]

        response = requests.get(url_2)
        jsonData = response.json()

        ranked_nextmode = jsonData["results"][0]["rule"]["name"]
        ranked_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
        ranked_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

        ranked_embed = discord.Embed(
                                    title = "バンカラチャレンジ",
                                    color=0xff0000,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
        ranked_embed.add_field(name=f"いま: **{ranked_mode}**", value=f"つぎ: **{ranked_nextmode}**", inline=False)
        ranked_embed.add_field(name=f"いま: **{ranked_map0}** / **{ranked_map1}**",
                              value=f"つぎ: **{ranked_nextmap0}** / **{ranked_nextmap1}**",
                              inline=False)
        ranked_embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
        ranked_embed.set_footer(text="API: https://spla3.yuu26.com")

        await ctx.respond(embed=ranked_embed,ephemeral = True)

    @spla3.command(guild_ids = guild_ids, description='バンカラオープンのステージ情報を取得します。')
    async def バンカラオープン(self, ctx):

        url = "https://spla3.yuu26.com/api/bankara-open/now"
        url_2 = "https://spla3.yuu26.com/api/bankara-open/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        league_mode = jsonData["results"][0]["rule"]["name"]
        league_map0 = jsonData["results"][0]["stages"][0]["name"]
        league_map1 = jsonData["results"][0]["stages"][1]["name"]

        response = requests.get(url_2)
        jsonData = response.json()

        league_nextmode = jsonData["results"][0]["rule"]["name"]
        league_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
        league_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

        league_embed = discord.Embed(
                                    title = "バンカラオープン",
                                    color=0xffc0cb,
                                    description=f"{dt.strftime('%Y年%m月%d日 %H:%M:%S')}時点と次のモードとステージ情報")
        league_embed.add_field(name=f"いま: **{league_mode}**", value=f"つぎ: **{league_nextmode}**", inline=False)
        league_embed.add_field(name=f"いま: **{league_map0}** / **{league_map1}**",
                               value=f"つぎ: **{league_nextmap0}** / **{league_nextmap1}**",
                               inline=False)
        league_embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
        league_embed.set_footer(text="API: https://spla3.yuu26.com")

        await ctx.respond(embed=league_embed,ephemeral = True)

    @spla3.command(guild_ids = guild_ids, description='サーモンランのステージ情報を取得します。')
    async def サーモンラン(self, ctx):

        url = "https://spla3.yuu26.com/api/coop-grouping-regular/now"
        url2 = "https://spla3.yuu26.com/api/coop-grouping-regular/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        # 現在のサーモンランのデータを取得

        salmon_map   = jsonData["results"][0]["stage"]["name"]
        salmon_wpn_1 = jsonData["results"][0]["weapons"][0]["name"]
        salmon_wpn_2 = jsonData["results"][0]["weapons"][1]["name"]
        salmon_wpn_3 = jsonData["results"][0]["weapons"][2]["name"]
        salmon_wpn_4 = jsonData["results"][0]["weapons"][3]["name"]


        response = requests.get(url2)
        jsonData = response.json()

        salmon_map2   = jsonData["results"][0]["stage"]["name"]
        salmon_wpn_5 = jsonData["results"][0]["weapons"][0]["name"]
        salmon_wpn_6 = jsonData["results"][0]["weapons"][1]["name"]
        salmon_wpn_7 = jsonData["results"][0]["weapons"][2]["name"]
        salmon_wpn_8 = jsonData["results"][0]["weapons"][3]["name"]

        salmon_embed = discord.Embed(
                                    title = "サーモンラン",
                                    color = 0xff7f50)
        salmon_embed.add_field(name=f"ブキ: {salmon_wpn_1}, {salmon_wpn_2}, {salmon_wpn_3}, {salmon_wpn_4}",
                               value=f"ステージ: **{salmon_map}**",
                               inline=False)
        salmon_embed.add_field(name=f"ブキ: {salmon_wpn_5}, {salmon_wpn_6}, {salmon_wpn_7}, {salmon_wpn_8}",
                               value=f"ステージ: **{salmon_map2}**",
                               inline=False)
        salmon_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
        salmon_embed.set_footer(text="API: https://spla3.yuu26.com")

        await ctx.respond(embed=salmon_embed,ephemeral = True)

    @slash_command(guild_ids = guild_ids, description='Splatoon3の武器をランダムに抽選')
    async def 武器(self, message):
            json_open = open('data/spla3.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            buki = random.choice(json_data)
            ja_name = buki["name"]["ja_JP"]
            en_name = buki["name"]["en_US"]
            path = "images/main/" + buki["name"]["ja_JP"] + ".jpg"
            user = message.author.display_name
            await message.respond(f"{user}さんにおすすめのブキは\n{ja_name}({en_name})！", file=discord.File(path))
            

def setup(bot):
    bot.add_cog(Splatoon3(bot))