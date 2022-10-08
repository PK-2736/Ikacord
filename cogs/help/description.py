import discord
import asyncio
from discord.ext import commands

print("descriptionの読み込み完了")

class description(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content.startswith("サーバー説明"):
            global embeddescription
            embeddescription = discord.Embed(title="サーバー説明",
                                    description="```ロール```\n"
                                                "<@&983297498271580170>"
                                                "<#981474117020712973>にて誰かが募集した際に通知します。\n"
                                                "<@&999913414732296302>"
                                                "掲示板でのこのサーバーの表示順をupするためのコマンドが使用出来るようになったら、通知します。\n"
                                                "<@&1013421495218872410>"
                                                "過去のフェスでの各チームのチャットを閲覧可能になります。\n"
                                                "```募集```\n"
                                                "スプラ募集チャンネルで<#982600408704892998>の募集コマンドを使用して募集できます\n"
                                                "誰かの募集に参加する際は、「参加」ボタンを押すことで参加できます。\n"
                                                "募集したメンバー同士の会話はスプラチャット1又は2、VCはスプラボイス1、又は2で行えます。\n"
                                                "```雑談関連```\n"
                                                "<#982595425867558982>、<#982595463498850374>は、雑談用のチャンネルです。主な会話はここで行ってください。\n"
                                                "<#982601748243951646> では、クリップやスクリーンショットを投稿できます。\n"
                                                "<#982602254278357022> では、/levelなどを使用してサーバー上でのレベルを確認できます。\n"
                                                "<#1020816298449575967> では、投稿を作成してサーバーメンバーに質問をすることができます。知恵袋を開き、「＋新しい投稿」を押すことで投稿を作成できます。"
                                    ,color=0xf07930)

            channel = self.bot.get_channel(1022072333978058802)

            await channel.send(embed=embeddescription)

def setup(bot):
    bot.add_cog(description(bot))