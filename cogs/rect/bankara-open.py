from types import NoneType
import discord
from discord.ext import commands
from discord.ui import Button, View, Item
from datetime import datetime
from discord.commands import slash_command, Option
import requests
import re

from cogs import guild_ids

print("rectbankaraの読み込み完了")

class spla3(View):
    def __init__(self):
        super().__init__(timeout=None)

    def add_embed(self, interaction: discord.Interaction):
        # メッセージの先頭にあるembedを取得
        embed = interaction.message.embeds[0]
        # embedを追加する必要があるかの初期設定 (必要アリ。)
        flag = True
        # mebedが存在する場合
        if embed:
            # embedの数が0個の時、
            if len(embed.fields) == 5:
                # 自分を追加して返す
                return embed.add_field(name=f"参加者", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=True)

            for idlist in embed.fields[5].value.split("\n"):
                # フィールドの中にあるidと一致するか比較
                match = re.search(f"{interaction.user.id}",idlist)
                if match:
                        #一致したらflagをfalseに
                        flag = False
                        # 終了
                        return embed

            # もしflagがtrue (最初のflag)なら
            if flag:
                # メンションを追加
                summon_users = [interaction.user.mention]
                cm = embed.fields[5].value
                tmp = "\n".join([str(user) for user in summon_users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(5,name="参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                    
        # embedを返す
        return embed

    @discord.ui.button(
        style=discord.ButtonStyle.green,
        label="参加",
        custom_id="join"
    )
    async def callback_join(self, button: Button, interaction: discord.Interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        embed = self.add_embed(interaction=interaction)
        await interaction.response.edit_message(embed=embed)
        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}が参加しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)

    def remove_embed(self, interaction: discord.Interaction):  
        embed = interaction.message.embeds[0]     
        flag = True
        # mebedが存在する場合
        if embed:
            # embedの数が0個の時、
            if len(embed.fields) == 5:
                return embed.add_field(name="不参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)

        for idlist in embed.fields[5].value.split("\n"):
                # フィールドの中にあるidと一致するか比較
                    match = re.search(f"{interaction.user.id}",idlist)
        if match:
                        #一致したらflagをfalseに
                        flag = False
                        # 終了
                        return embed

            # もしflagがtrue (最初のflag)なら
        if flag:
                # メンションを追加
                summon_users = [interaction.user.mention]
                cm = embed.fields[5].value
                tmp = "\n".join([str(user) for user in summon_users])
                summon = tmp if tmp else "なし"
                time = f"**{datetime.now().strftime('%H:%M')}**"
                embed.set_field_at(5,name="不参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                    
        # embedを返す
        return embed
                 
    @discord.ui.button(
        style=discord.ButtonStyle.blurple,
        label="取り消し",
        custom_id="remove"
    )
    async def callback_remove(self, button: Button, interaction: discord.Interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        embed = self.remove_embed(interaction=interaction)
        await interaction.response.edit_message(embed=embed)
        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}が参加を取り消しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)

    @discord.ui.button(
        style=discord.ButtonStyle.red,
        label="しめ",
        custom_id="sime"
    )
    async def callback_sime(self, button: Button, interaction: discord.Interaction):
        interaction.permissions.use_application_commands = True
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}の募集〆", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(embed=embed)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(
        style=discord.ButtonStyle.grey,
        label="ステージ",
        custom_id="stage"
    )
    async def callback_stage(self, button: Button, interaction: discord.Interaction):
        url = "https://spla3.yuu26.com/api/bankara-open/now"
        url_2 = "https://spla3.yuu26.com/api/bankara-open/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        league_mode = jsonData["results"][0]["rule"]["name"]
        league_map0 = jsonData["results"][0]["stages"][0]["name"]
        league_map1 = jsonData["results"][0]["stages"][1]["name"]

        response = requests.get(url_2)
        jsonData = response.json()

        league_nextmode = jsonData["results"][0]["rule"]["name"]
        league_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
        league_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

        league_embed = discord.Embed(
                                    title = "バンカラオープン",
                                    color=0xffc0cb)
        league_embed.add_field(name=f"いま: **{league_mode}**", value=f"つぎ: **{league_nextmode}**", inline=False)
        league_embed.add_field(name=f"いま: **{league_map0}** / **{league_map1}**",
                               value=f"つぎ: **{league_nextmap0}** / **{league_nextmap1}**",
                               inline=False)
        league_embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
        league_embed.set_footer(text="API: https://spla3.yuu26.com")

        await interaction.response.send_message(embed=league_embed,ephemeral = True)

class rectbankara(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間", required=False))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集ウデマエ", required=False))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdb4a13
        )
        time = '' if self.children[1].value else "集まり次第"
        a = '' if self.children[3].value else "記載なし"
        i = '' if self.children[4].value else "記載なし"
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=f"{self.children[1].value}{time}", inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集ウデマエ", value=f"{self.children[3].value}{a}", inline=True)
        embed.add_field(name="募集内容", value=f"{self.children[4].value}{i}", inline=False)
        embed.add_field(name="参加者", value=f"{interaction.user.mention} **{datetime.now().strftime('%H:%M')}**", inline=False)
        embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
        embed.set_author(name='バンカラマッチ募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message(f"<@&983297498271580170>: {spla3.is_persistent(spla3())}", embed=embed, view=spla3())

class bankara(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="募集バンカラ",guild_ids=guild_ids, description="バンカラマッチメンバーの募集")
    async def rectbankara(self, interaction: discord.Interaction):
        if interaction.channel.id not in [1027901127099953152,981474117020712973]:
            return await interaction.respond("エラー：バンカラ募集コマンドは <#1027901127099953152> で実行して下さい。",ephemeral = True)
        modal = rectbankara(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

def setup(bot: commands.Bot):
    bot.add_cog(bankara(bot=bot))