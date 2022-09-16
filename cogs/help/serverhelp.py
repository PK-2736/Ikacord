import discord
from discord.ext import commands
from discord.commands import slash_command, Option

print("serverhelpの読み込み完了")

class serverhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
    async def on_ready(self): 
        embed = discord.Embed( # Embedを定義する
                          title="IkacordBOTの使い方",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          )
        #embed.add_field(name="スプラコマンド",value="スプラ2のステージ表示：スプラコマンド, s(サーモンラン))を指定\n"
                            #"ランダムに武器を表示：武器")
        #embed.add_field(name="フレンドコードコマンド",value="フレンドコードを保存する：/fc set (自分のフレンドコード）\n"
        #"フレンドコードを検索する：/fc find (対象の人をメンション)\n"
        #"/fc remove (自分をメンション) (自分のフレンドコード)：/fc remove (自分をメンション) (自分のフレンドコード)")
        #embed.add_field(name="募集コマンド",value="BOTのメンションの後に'時間' 'ルール' '募集人数' '募集内容'を記入\n"
        #"例：```例：@splabot 21時から@1リグマ募集```")
        #embed.add_field(name="読み上げコマンド",value="読み上げを開始：!talk,?talk"
        #"\n!talk,?talk：!stop,?stop\n※このコマンドは別のBOTが反応します")
        #embed.add_field(name="音楽コマンド",value="BOTを指定したボイスチャンネルに接続：/music connect (ボイスチャンネルID)\n"
        #"指定した曲を再生、またはキューに追加：music play (自分の流したい曲のURL)\n"
        #"現在流している曲名を表示：/music now_playing\n"
        #"キューに入っている曲を表示します：/music queue\n"
        #"曲を一時停止します：/music pause\n曲を再生します：/music resume\n"
        #"曲をスキップします：/music skip"
        #"\n音のボリュームを変更します：/music volume (ボリュームの数値)\n"
        #"ボイスチャンネルからBOTを退出させます：/music stop")
        #embed.add_field(name="その他コマンド",value="簡易HELPを表示：/help\n"
        #"BOTの情報を表示：/client_info\n"
        #"BOTの情報を表示2：/client_application_info")
        embed.add_field(name='ㅤ', value='```スプラ3ステージ情報```', inline=False)
        embed.add_field(name='バンカラ(オープン)', value='/ステージ バンカラオープン', inline=False)
        embed.add_field(name='バンカラ(チャレンジ)', value='/ステージ バンカラチャレンジ', inline=False)
        embed.add_field(name='レギュラー', value='/ステージ レギュラー', inline=False)
        embed.add_field(name='サーモンラン', value='/ステージ サーモンラン', inline=False)
        embed.add_field(name='ランダムに武器を表示', value='/武器', inline=False)
        embed.add_field(name='ㅤ', value='```フレンドコードコマンド```', inline=False)
        embed.add_field(name='フレンドコードを保存する', value='/フレコ 登録 (自分のフレンドコード）', inline=True)
        embed.add_field(name='フレンドコードを検索する', value='/フレコ 検索 (対象の人をメンション)', inline=True)
        embed.add_field(name='自分のフレンドコードを削除する', value='/フレコ 削除 (自分をメンション) (自分のフレンドコード)', inline=True)
        embed.add_field(name='ㅤ', value='```募集コマンド```', inline=False)
        embed.add_field(name='バンカラ募集', value='/募集バンカラ', inline=False)
        embed.add_field(name='レギュラー募集', value='/募集レギュラー', inline=False)
        embed.add_field(name='バイト募集', value='/募集バイト', inline=False)
        embed.add_field(name='プラベ募集', value='/募集プラベ', inline=False)
        embed.add_field(name='なんでも募集', value='/募集スプラ', inline=False)
        embed.add_field(name='ㅤ', value='```読み上げコマンド```', inline=False)
        embed.add_field(name='読み上げを開始', value='!talk,?talk', inline=True)
        embed.add_field(name='読み上げ終了', value='!stop,?stop', inline=True)
        embed.add_field(name='ㅤ', value='```その他コマンド```', inline=False)
        embed.add_field(name='コマンド別help表示', value='/ヘルプ', inline=True)

        guild = self.bot.get_guild("channel_id")
        channel = guild.get_channel("channel_id")

        await channel.send(embed=embed) # embedの送信には、embed={定義したembed名}

def setup(bot):
    bot.add_cog(serverhelp(bot))