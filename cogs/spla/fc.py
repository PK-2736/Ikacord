import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import asyncio

from cogs import guild_ids

print("fcの読み込み完了")

class fc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    fc = discord.SlashCommandGroup("フレコ", "フレンドコード関連", guild_ids = guild_ids)

    # @commands.Cog.listener()
    # async def on_message(self, message): 
    #     if message.author.bot:
    #         return
    #     discordname = message.author.mention
    #     def check(msg):
    #         return msg.author == message.author
    #     global embed
    #     if message.content.startswith("fcset"):
    #         embed = discord.Embed(
    #             color=0xc5c3bf, 
    #                 description="フレンドコードを入力してください",
    #             )
    #         await message.channel.send(embed=embed)

    #     try:
    #         msg = await self.bot.wait_for("message", check=check, timeout=40)
    #     except asyncio.TimeoutError:
    #             embed = discord.Embed( # Embedを定義する
    #                       color=0xe91010, # フレーム色指定(今回は緑)
    #                       description="タイムアウトしました\nもう一度実行して下さい" # Embedの説明文 必要に応じて
    #         )
    #             await message.channel.send(embed=embed)
    #             return
    #     embed = discord.Embed( # Embedを定義する
    #                       color=0xf09214, # フレーム色指定(今回は緑)
    #                       description=f'{discordname} フレンドコードを設定しました\n**/fc find @メンションで確認出来ます！**\n設定が終わったのでチャンネルを非表示にします\n' # Embedの説明文 必要に応じて
    #         )        
    #     await message.channel.send(embed=embed)
    #     print(msg.content)
    #     file = open("data/friendcodes.txt", "a")
    #     file.write(f'{discordname} ')
    #     file.write(f'{msg.content}\n')
    #     file.close()


    @fc.command(name="登録", guild_ids=guild_ids, description="自分のフレンドコードをセットします")
    async def register(self, ctx, *, friendcode: Option(str, "例：1111-1111-1111")):
        discordname = ctx.author.id
        file = open("data/friendcodes.txt", "a")
        file.write(f'<@{discordname}> ')
        file.write(f'{friendcode}\n')
        file.close()
        embed = discord.Embed( # Embedを定義する
                          color=0xf09214, # フレーム色指定(今回は緑)
                          description=f"<@{discordname}> フレンドコードを設定しました {friendcode}" # Embedの説明文 必要に応じて
                          )
        await ctx.respond(embed=embed)

    @fc.command(name="検索", guild_ids=guild_ids, description="特定の人のフレンドコードを表示します")
    async def search(self, ctx, member: Option(str, "例：@PheyK")):
        searchfile = open("data/friendcodes.txt", "r")
        member = member.replace('!', '')
        print(member)
        for line in searchfile:
            if f'{member}' in line:
                print(member)
                print(line)
            if f'{member}' in line:
                embed = discord.Embed( # Embedを定義する
                          color=0x4cc2e2, # フレーム色指定(今回は緑)
                          description=f"フレンドコード-> {line}" # Embedの説明文 必要に応じて
                          )
        await ctx.respond(embed=embed)
        searchfile.close()

    @fc.command(name="削除", guild_ids=guild_ids, description="登録しているフレンドコードを削除します")
    async def delete(self, ctx, member: Option(str, "例：@PheyK"), fc: Option(str, "例：1111-1111-1111")):
        with open("data/friendcodes.txt", "r") as f:
            lines = f.readlines()
            print(lines)
            print(member)
            print(fc)
        with open("data/friendcodes.txt", "w") as f:
            for line in lines:
                if line.strip(" \n") != f'{member} {fc}':
                    f.write(line)
            embed = discord.Embed( # Embedを定義する
                          color=0xe64b47, # フレーム色指定(今回は緑)
                          description="フレンドコードを削除しました" # Embedの説明文 必要に応じて
                          )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(fc(bot))