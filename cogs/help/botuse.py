import discord
import asyncio
from discord.ext import commands

print("botuseの読み込み完了")

class botuse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content.startswith("IkacordBOTの使い方"):
            global embedbotuse
            embedbotuse = discord.Embed( 
                            title="IkacordBOTの使い方",
                            description="バンカラ(オープン)"
                                            "```/ステージ バンカラオープン```\n"
                                            "バンカラ(チャレンジ)"
                                            "```/ステージ バンカラオープン```\n"
                                            "レギュラー"
                                            "```/ステージ レギュラー```\n"
                                            "サーモンラン"
                                            "```/ステージ サーモンラン```\n"
                                            "ランダムに武器を表示"
                                            "```/ランダム武器```\n"
                                            "ブランド別ギア表を表示"
                                            "```/ギア表```\n"
                                            "フレンドコードを保存する"
                                            "```/フレコ 登録 (自分のフレンドコード)```\n"
                                            "フレンドコードを検索する"
                                            "```/フレコ 検索 (対象の人をメンション)```\n"
                                            "自分のフレンドコードを削除する"
                                            "```/フレコ 削除 (自分をメンション) (自分のフレンドコード)```\n"
                                            "バンカラ募集"
                                            "```/募集バンカラ```\n"
                                            "レギュラー募集"
                                            "```/募集レギュラー```\n"
                                            "バイト募集"
                                            "```/募集バイト```\n"
                                            "なんでも募集"
                                            "```/募集スプラ```\n"
                                            "読み上げを開始"
                                            "```!stop,?stop```\n"
                                            "コマンド別help表示"
                                            "```/ヘルプ```"
                            ,color=0x30f05d, )

            channel = self.bot.get_channel(982600408704892998)

            await channel.send(embed=embedbotuse)

def setup(bot):
    bot.add_cog(botuse(bot))

