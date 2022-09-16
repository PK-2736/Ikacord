from discord.ext import commands
import discord
from discord.commands import slash_command, Option
from cogs import guild_ids

print("helpの読み込み完了")

class uihelp(discord.ui.View):
    @discord.ui.select(
        placeholder="ココをタップ",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="スプラコマンド"),
            discord.SelectOption(label="フレンドコードコマンド"),
            discord.SelectOption(label="募集コマンド"),
            discord.SelectOption(label="読み上げコマンド"),
            discord.SelectOption(label="その他コマンド"),
        ],
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "スプラ3ステージコマンド":
            embed = discord.Embed( 
                          title="スプラコマンド",
                          color=0x76d8be, 
                          url="https://example.com"
                          )
            embed.add_field(name='バンカラ(オープン)', value='/ステージ バンカラオープン', inline=False)
            embed.add_field(name='バンカラ(チャレンジ)', value='/ステージ バンカラチャレンジ', inline=False)
            embed.add_field(name='レギュラー', value='/ステージ レギュラー', inline=False)
            embed.add_field(name='サーモンラン', value='/ステージ サーモンラン', inline=False)
            embed.add_field(name='ランダムに武器を表示', value='/武器', inline=False)
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "フレンドコードコマンド":
            embed = discord.Embed( 
                          title="フレンドコードコマンド",
                          color=0xe7ad5b, 
                          url="https://example.com"
                          )
            embed.add_field(name='フレンドコードを保存する', value='/フレコ 登録 (自分のフレンドコード）', inline=True)
            embed.add_field(name='フレンドコードを検索する', value='/フレコ 検索 (対象の人をメンション)', inline=True)
            embed.add_field(name='自分のフレンドコードを削除する', value='/フレコ 削除 (自分をメンション) (自分のフレンドコード)', inline=True)         
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "募集コマンド":
            embed = discord.Embed( 
                          title="募集コマンド",
                          color=0xc376d8, 
                          url="https://example.com" 
                          )
            embed.add_field(name='バンカラ募集', value='/募集バンカラ', inline=False)
            embed.add_field(name='レギュラー募集', value='/募集レギュラー', inline=False)
            embed.add_field(name='バイト募集', value='/募集バイト', inline=False)
            embed.add_field(name='プラベ募集', value='/募集プラベ', inline=False)
            embed.add_field(name='なんでも募集', value='/募集スプラ', inline=False)
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "読み上げコマンド":
            embed = discord.Embed( 
                          title="読み上げコマンド",
                          color=0x00ff00, 
                          url="https://example.com"
                          )
            embed.add_field(name='読み上げを開始', value='!talk,?talk', inline=False)
            embed.add_field(name='読み上げ終了', value='!stop,?stop', inline=False)              
            await interaction.response.edit_message(embed=embed)


        elif select.values[0] == "その他コマンド":
            embed = discord.Embed( 
                          title="その他コマンド",
                          color=0xdfdd1d, 
                          url="https://example.com"
                          )
            embed.add_field(name='コマンド別help表示', value='/ヘルプ', inline=False)
            await interaction.response.edit_message(embed=embed)

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @slash_command(guild_ids=guild_ids, description="コマンドのHELPを表示します")
    async def ヘルプ(self, ctx):
            await ctx.respond(f"{ctx.author.mention} コマンド一覧です", view=uihelp())

def setup(bot):
    bot.add_cog(help(bot))