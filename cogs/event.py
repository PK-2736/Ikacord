import discord
import asyncio
from discord.ext import commands

print("eventの読み込み完了")

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            client = self.bot
            await client.change_presence(activity = discord.Activity(name="Help:/help", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="splatoon3", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            joinserver=len(client.guilds)
            servers=str(joinserver)
            await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="botについての連絡はPheyK#1280", type=discord.ActivityType.playing))
            await asyncio.sleep(15)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        CustomEmoji = "<:emoji_3:1000747740294291517>"
        guild = self.bot.get_guild("channel_id")
        channel = guild.get_channel("channel_id")
        embed = discord.Embed( # Embedを定義する
                        title=f"{member.name}が入室しました！",# タイトル
                        description="まずは <#982580263936749578>を呼んで <#982600148259602442>を書きましょう！",
                        color=0x00ff00,) # フレーム色指定(今回は緑)
        meg = await channel.send(embed=embed)
        await meg.add_reaction(CustomEmoji)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = self.bot.get_guild("channel_id")
        channel = guild.get_channel("channel_id")
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild("channel_id")
        channel = guild.get_channel("channel_id")
        embed = discord.Embed( # Embedを定義する
                        title="＜ルール＞",# タイトル
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
                                    "（通知用ロールは #ロール-通知許可ﾛｰﾙ で取得できます）\n",
                        color=0x4298c2,) 
        file = discord.File(fp="./Ikacord3_splatoonlogo.png",filename="image.png",spoiler=False)
        embed.set_image(url=f"attachment://image.png")               
        embed.set_footer(text="Splatoon3 Discord Server\n"
                              "made by PheyK")
        await channel.send(embed=embed, file=file)

    #@commands.Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError
            ):
        if isinstance(error, discord.ApplicationCommandInvokeError):
                embed = discord.Embed( # Embedを定義する
                    color=0xe64b47, # フレーム色指定(今回は緑)
                    description="コマンドエラー" # Embedの説明文 必要に応じて
                    )
                await ctx.send(embed=embed, reference=ctx.message)
        else:
                raise error  # Here we raise other errors to ensure they aren't ignored


def setup(bot):
    bot.add_cog(event(bot))