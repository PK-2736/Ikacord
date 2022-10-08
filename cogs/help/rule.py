import discord
import asyncio
from discord.ext import commands

print("ruleの読み込み完了")

class rule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return 
        if message.content.startswith("ルール"):
            global embedrule
            embedrule = discord.Embed( 
                            title="＜ルール＞",
                            description="①暴言、下ネタは 御遠慮願います\n"
                                        "あまりにも酷い場合はサーバーから退室して頂きます\n"
                                        "\n"
                                        "②スプラに関する募集等は\n"
                                        "#スプラ募集 でお願いします\n"
                                        "(宣伝等はご遠慮ください)\n"
                                        "\n"
                                        "③味方への不満を言うのは大丈夫ですが\n"
                                        "過度な煽りや暴言はダメです\n"
                                        "\n"
                                        "④他人への迷惑行為。 過度な連投やスパムはご法度です\n"
                                        "\n"
                                        "ボイスチャット等の強要は致しません！(聞き専ok!)\n"
                                        "\n"
                                        "以上のルールを守って楽しくスプラトゥーンをしましょう！\n"
                                        "（通知用ロールは <#982580781589331998> で取得できます）\n",
                                        color=0x4298c2) 
            file = discord.File("images/Ikacord3_splatoonlogo.png", filename="spla3.png")
            embedrule.set_image(url=f"attachment://spla3.png")               
            embedrule.set_footer(text="Ikacord3 Discord Server\n"
                                "made by PheyK")
            
            channel = self.bot.get_channel(982580263936749578)

            await channel.send(file=file,embed=embedrule)

def setup(bot):
    bot.add_cog(rule(bot))