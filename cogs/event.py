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
        channel = self.bot.get_channel(982580316894015530)
        embed = discord.Embed( 
                        title=f"{member.name}が入室しました！",
                        description="まずは <#982580263936749578>を呼んで <#982600148259602442>を書きましょう！"
                                            "<#1022072333978058802> に簡単なサーバー説明が書いてあります。",
                        color=0x00ff00,) 
        meg = await channel.send(embed=embed)
        await meg.add_reaction(CustomEmoji)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(982596256868225054)
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")

    @commands.Cog.listener()
    async def on_ready(self):
        embed = discord.Embed( 
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
        file = discord.File("images/Ikacord3_splatoonlogo.png", filename="spla.png")
        embed.set_image(url=f"attachment://spla.png")               
        embed.set_footer(text="Splatoon3 Discord Server\n"
                              "made by PheyK")
        
        channel = self.bot.get_channel(982580263936749578)

        await channel.send(embed=embed, file=file)

    @commands.Cog.listener()
    async def on_ready(self):
        embed = discord.Embed(title="サーバー説明",
                                description="```ーーロールーー```\n"
                                            "<@&983297498271580170>"
                                            "<#981474117020712973>にて誰かが募集した際に通知します。\n"
                                            "<@&999913414732296302>"
                                            "掲示板でのこのサーバーの表示順をupするためのコマンドが使用出来るようになったら、通知します。\n"
                                            "<@&1013421495218872410>"
                                            "過去のフェスでの各チームのチャットを閲覧可能になります。\n"
                                            "```ーー募集ーー```\n"
                                            "スプラ募集チャンネルで<#982600408704892998>の募集コマンドを使用して募集できます\n"
                                            "誰かの募集に参加する際は、「参加」ボタンを押すことで参加できます。\n"
                                            "募集したメンバー同士の会話はスプラチャット1又は2、VCはスプラボイス1、又は2で行えます。\n"
                                            "```ーー雑談関連ーー```\n"
                                            "<#982595425867558982>、<#982595463498850374>は、雑談用のチャンネルです。主な会話はここで行ってください。\n"
                                            "<#982601748243951646> では、クリップやスクリーンショットを投稿できます。\n"
                                            "<#982602254278357022> では、/levelなどを使用してサーバー上でのレベルを確認できます。\n"
                                            "<#1020816298449575967> では、投稿を作成してサーバーメンバーに質問をすることができます。知恵袋を開き、「＋新しい投稿」を押すことで投稿を作成できます。"
                                ,color=0xf07930)

        channel = self.bot.get_channel(1022072333978058802)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self): 
        embed = discord.Embed( 
                          title="IkacordBOTの使い方",
                           description="```ーースプラ3コマンドーー```\n"
                                        "バンカラ(オープン)"
                                        "/ステージ バンカラオープン\n"
                                        "バンカラ(チャレンジ)"
                                        "/ステージ バンカラオープン\n"
                                        "レギュラー"
                                        "/ステージ レギュラー\n"
                                        "サーモンラン"
                                        "/ステージ サーモンラン\n"
                                        "ランダムに武器を表示"
                                        "/ランダム武器\n"
                                        "ブランド別ギア表を表示"
                                        "/ギア表\n"
                                        "```ーーフレンドコードコマンドーー```\n"
                                        "フレンドコードを保存する"
                                        "/フレコ 登録 (自分のフレンドコード)\n"
                                        "フレンドコードを検索する"
                                        "/フレコ 検索 (対象の人をメンション)\n"
                                        "自分のフレンドコードを削除する"
                                        "/フレコ 削除 (自分をメンション) (自分のフレンドコード)\n"
                                        "```ーー募集コマンドーー```\n"
                                        "バンカラ募集"
                                        "/募集バンカラ\n"
                                        "レギュラー募集"
                                        "/募集レギュラー\n"
                                        "バイト募集"
                                        "/募集バイト\n"
                                        "なんでも募集"
                                        "/募集スプラ\n"
                                        "```ーー読み上げコマンドーー```\n"
                                        "読み上げを開始"
                                        "!talk,?talk\n"
                                        "読み上げ終了"
                                        "!stop,?stop\n"
                                        "```ーーその他コマンドーー```\n"
                                        "コマンド別help表示"
                                        "/ヘルプ\n"
                          ,color=0x30f05d, )

        channel = self.bot.get_channel(982600408704892998)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_application_command_error(
        self, ctx: discord.ApplicationContext, error: discord.ApplicationCommandError
            ):
        if isinstance(error, discord.ApplicationCommandInvokeError):
                embed = discord.Embed(
                    color=0xe64b47,
                    description="コマンドエラー"
                    )
                await ctx.send(embed=embed, reference=ctx.message)
        else:
                raise error

def setup(bot):
    bot.add_cog(event(bot))