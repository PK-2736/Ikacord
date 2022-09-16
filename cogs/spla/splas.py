# import asyncio
# import os
# import random
# import json
# import requests
# import discord
# from discord.ext import commands
# from discord import Embed, AllowedMentions
# from discord.commands import slash_command, Option
# from cogs import guild_ids

# print("splaの読み込み完了")

# class Game(commands.Cog):
#     """トレーニングといったお遊び系のコマンドがあるカテゴリーです"""
#     def __init__(self, bot):
#         self.bot = bot
#         self.stage_info = None
#         self.s_endpoint = 'https://stat.ink/api/v2'
#         self.spla_api_key = os.getenv('SPLATOON2_KEY')

#     spla = discord.SlashCommandGroup("spla", "フレンドコード関連", guild_ids = guild_ids)

#     @spla.command(guild_ids = guild_ids, description='Splatoon2のステージ情報を取得します',
#                       usage='[対戦ルールタイプ] <n(次の時間帯)>')
#     async def ステージ2(self, ctx, ステージ: Option(str, "r(レギュラー) l(リーマッチ) s(サーモンラン) g(ガチマッチ)"), 次のステージを表示: Option(str, "r次のステージ表示（n)")=None):
#         def get_stage(game, time_next: bool):
#             if game == 'regular':
#                 if time_next:
#                     res = requests.get('https://spla2.yuu26.com/regular/next')
#                     return res.json()['result'][0]
#                 else:
#                     res = requests.get('https://spla2.yuu26.com/regular/now')
#                     return res.json()['result'][0]
#             elif game == 'gachi':
#                 if time_next:
#                     res = requests.get('https://spla2.yuu26.com/gachi/next')
#                     return res.json()['result'][0]
#                 else:
#                     res = requests.get('https://spla2.yuu26.com/gachi/now')
#                     return res.json()['result'][0]
#             elif game == 'league':
#                 if time_next:
#                     res = requests.get('https://spla2.yuu26.com/league/next')
#                     return res.json()['result'][0]
#                 else:
#                     res = requests.get('https://spla2.yuu26.com/league/now')
#                     return res.json()['result'][0]
#             elif game == 'coop':
#                 if time_next:
#                     res = requests.get('https://spla2.yuu26.com/coop/schedule')
#                     return res.json()['result'][1]
#                 else:
#                     res = requests.get('https://spla2.yuu26.com/coop/schedule')
#                     return res.json()['result'][0]

#         if ステージ is None:
#             no_type_msg = Embed(description='ステージ情報のタイプ(r, g, l, s)を指定してください\n'
#                                             'r: レギュラーマッチ\ng: ガチマッチ\nl: リーグマッチ\ns: サーモンラン')
#             await ctx.respond(embed=no_type_msg, allowed_mentions=AllowedMentions.none())
#         elif ステージ == 'r':
#             if 次のステージを表示 is None:
#                 self.stager_info = get_stage('regular', False)
#             elif 次のステージを表示 == 'n':
#                 self.stager_info = get_stage('regular', True)

#             stage_info = self.stager_info
#             rule_name = stage_info["rule"]
#             stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
#             s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
#             e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
#             image_url = random.choice([stage_info['maps_ex'][0]['image']])
#             image_url2 = random.choice([stage_info['maps_ex'][1]['image']])

#             de_msg = f'**ルール**\n\n{rule_name}\n**ステージ**\n\n{stage}\n\n' \
#                      f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
#             embed = Embed(title='Splatoon2 ステージ情報 | レギュラーマッチ',
#                           description=de_msg,
#                           color=261888)  # カラー:ライトグリーン)
#             embed.set_image(url=image_url)
#             embed.set_thumbnail(url=image_url2)
#             await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

#         elif ステージ == 'g':
#             if 次のステージを表示 is None:
#                 self.stage_info = get_stage('gachi', False)
#             elif 次のステージを表示 == 'n':
#                 self.stage_info = get_stage('gachi', True)

#             stage_info = self.stage_info
#             rule_name = stage_info["rule"]
#             stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
#             s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
#             e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
#             image_url = random.choice([stage_info['maps_ex'][0]['image']])
#             image_url2 = random.choice([stage_info['maps_ex'][1]['image']])

#             de_msg = f'**ルール**\n\n{rule_name}\n\n**ステージ**\n\n{stage}\n\n' \
#                      f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
#             embed = Embed(title='Splatoon2 ステージ情報 | ガチマッチ',
#                           description=de_msg,
#                           color=14840346)  # カラー:オレンジ
#             embed.set_image(url=image_url)
#             embed.set_thumbnail(url=image_url2)
#             await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

#         elif ステージ == 'l':
#             if 次のステージを表示 is None:
#                 self.stage_info = get_stage('league', False)
#             elif 次のステージを表示 == 'n':
#                 self.stage_info = get_stage('league', True)

#             stage_info = self.stage_info
#             rule_name = stage_info["rule"]
#             stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
#             s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
#             e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
#             image_url = random.choice([stage_info['maps_ex'][0]['image']])
#             image_url2 = random.choice([stage_info['maps_ex'][1]['image']])


#             de_msg = f'**ルール**\n\n{rule_name}\n\n**ステージ**\n\n{stage}\n\n' \
#                      f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
#             embed = Embed(title='Splatoon2 ステージ情報 | リーグマッチ',
#                           description=de_msg,
#                           color=15409787)  # カラー:ピンク
#             embed.set_image(url=image_url)
#             embed.set_thumbnail(url=image_url2)
#             await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

#         elif ステージ == 's':
#             if 次のステージを表示 is None:
#                 self.stage_info = get_stage('coop', False)
#             elif 次のステージを表示 == 'n':
#                 self.stage_info = get_stage('coop', True)

#             stage_info = self.stage_info
#             stage = stage_info["stage"]["name"]
#             image_url = stage_info['stage']['image']
#             s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
#             e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
#             weapons = ''
#             for we in stage_info['weapons']:
#                 weapons += f'・{we["name"]}\n'

#             de_msg = f'**ステージ**\n\n{stage}\n\n**支給ブキ**\n\n{weapons}\n' \
#                      f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
#             embed = Embed(title='Splatoon2 ステージ情報 | サーモンラン',
#                           description=de_msg,
#                           color=15442812)  # カラー:薄橙
#             embed.set_image(url=image_url)
#             await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())


#     @spla.command(guild_ids = guild_ids, description='Splatoon2の武器をランダムに抽選')
#     async def 武器2(self, message):
#             json_open = open('data/weapon.json', 'r',encoding='utf-8')
#             json_data = json.load(json_open)
#             buki = random.choice(json_data)
#             ja_name = buki["name"]["ja_JP"]
#             en_name = buki["name"]["en_US"]
#             path = "images/main/" + buki["name"]["ja_JP"] + ".png"
#             user = message.author.display_name
#             await message.respond(f"{user}さんにおすすめのブキは{ja_name}({en_name})！" , file=discord.File(path))

# def setup(bot):
#     bot.add_cog(Game(bot))