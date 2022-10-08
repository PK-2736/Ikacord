import discord
from discord.commands import slash_command, Option
from discord.ext import commands
import asyncio
import re

from cogs import guild_ids

print("fcの読み込み完了")

class fc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    fc = discord.SlashCommandGroup("フレコ", "フレンドコード関連", guild_ids = guild_ids)

    @commands.Cog.listener()
    async def on_message(self, message): 
        if message.channel.id not in []:
            if message.author.bot:
                return
            discordname = message.author.mention
            words=['/フレコ 登録']
            for word in words:
                if word in message.content:
                    before_words = message.content
                    after_words = re.search(r'(\d{4})-?(\d{4})-?(\d{4})', before_words)
                    global embed
                    embed = discord.Embed(
                    color=0xf09214, 
                    description=f'{discordname} フレンドコードを設定しました\n'
                                 '/フレコ 検索で確認出来ます'
                                         )   
                    embed.set_footer(text="Ikacord3 Discord Server")
    
                    await message.author.send(embed=embed)
                    print(after_words.group(0))
                    file = open("data/friendcodes.txt", "a")
                    file.write(f'{discordname} ')
                    file.write(f'{after_words.group(0)}\n')
                    file.close()

    @fc.command(name="登録", guild_ids=guild_ids, description="自分のフレンドコードをセットします")
    async def register(self, ctx, *, フレンドコード: Option(str, "例：1111-1111-1111")):
        discordname = ctx.author.id
        file = open("data/friendcodes.txt", "a")
        file.write(f'<@{discordname}> ')
        file.write(f'{フレンドコード}\n')
        file.close()
        embed = discord.Embed( # Embedを定義する
                          color=0xf09214, # フレーム色指定(今回は緑)
                          description=f"<@{discordname}> フレンドコードを設定しました {フレンドコード}" # Embedの説明文 必要に応じて
                          )
        await ctx.respond(embed=embed,ephemeral = True)

    @fc.command(name="検索", guild_ids=guild_ids, description="特定の人のフレンドコードを表示します")
    async def search(self, ctx, メンション: Option(str, "例：@PheyK")):
        searchfile = open("data/friendcodes.txt", "r")
        メンション = メンション.replace('!', '')
        print(メンション)
        for line in searchfile:
            if f'{メンション}' in line:
                print(メンション)
                print(line)
            if f'{メンション}' in line:
                embed = discord.Embed( # Embedを定義する
                          color=0x4cc2e2, # フレーム色指定(今回は緑)
                          description=f"フレンドコード-> {line}" # Embedの説明文 必要に応じて
                          )
        await ctx.respond(embed=embed)
        searchfile.close()

    @fc.command(name="削除", guild_ids=guild_ids, description="登録しているフレンドコードを削除します")
    async def delete(self, ctx, メンション: Option(str, "例：@PheyK"), フレンドコード: Option(str, "例：1111-1111-1111")):
        with open("data/friendcodes.txt", "r") as f:
            lines = f.readlines()
            print(lines)
            print(メンション)
            print(フレンドコード)
        with open("data/friendcodes.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != f'{メンション} {フレンドコード}':
                    f.write(line)
            embed = discord.Embed( # Embedを定義する
                          color=0xe64b47, # フレーム色指定(今回は緑)
                          description="フレンドコードを削除しました" # Embedの説明文 必要に応じて
                          )
            await ctx.respond(embed=embed,ephemeral = True)

def setup(bot):
    bot.add_cog(fc(bot))