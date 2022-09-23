from dataclasses import field
import re

import discord
from discord.ext import commands
from discord.ui import Button, View, Item
from datetime import datetime
from discord.commands import slash_command, Option
import requests

from cogs import guild_ids

print("rectregularの読み込み完了")

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
            if len(embed.fields) == 4:
                # 自分を追加して返す
                return embed.add_field(name=f"参加者", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=True)

            for idlist in embed.fields[4].value.split("\n"):
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
                cm = embed.fields[4].value
                tmp = "\n".join([str(user) for user in summon_users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(4,name="参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                    
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
                time = datetime.now().strftime("%H:%M")
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
        url = "https://spla3.yuu26.com/api/regular/now"
        url_2 = "https://spla3.yuu26.com/api/regular/next"
        ua = "Splatoon3/ikacord bot (twitter @Mt_PheyK, Discord PheyK#1280"
        headers = {"User-Agent": ua}

        response = requests.get(url)
        jsonData = response.json()

        regular_map0 = jsonData["results"][0]["stages"][0]["name"]
        regular_map1 = jsonData["results"][0]["stages"][1]["name"]

        response = requests.get(url_2)
        jsonData = response.json()

        regular_nextmap0 = jsonData["results"][0]["stages"][0]["name"]
        regular_nextmap1 = jsonData["results"][0]["stages"][1]["name"]

        regular_embed = discord.Embed(
                                    title = "レギュラーマッチ（ナワバリバトル）",
                                    color=0x00ff00)
        regular_embed.add_field(name=f"いま: **{regular_map0}** / **{regular_map1}**",
                                value=f"つぎ: **{regular_nextmap0}** / **{regular_nextmap1}**",
                                inline=False)
        regular_embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
        regular_embed.set_footer(text="API: https://spla3.yuu26.com")

        await interaction.response.send_message(embed=regular_embed,ephemeral = True)

class rectregular(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間", required=False))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0x1ae05f
        )
        time = '' if self.children[1].value else "集まり次第"
        i = '' if self.children[3].value else "記載なし"
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=f"{self.children[1].value}{time}", inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=f"{self.children[3].value}{i}", inline=False)
        embed.add_field(name="参加者", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)
        embed.set_thumbnail(url="https://img.game8.jp/1624580/4a48b2bf985a9b5e79b78bdc7753f8b3.png/show")
        embed.set_author(name='レギュラーマッチ募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message(f"<@&983297498271580170>: {spla3.is_persistent(spla3())}", embed=embed, view=spla3())

class regular(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="募集レギュラー",guild_ids=guild_ids, description="レギュラーマッチメンバーの募集")
    async def rectregular(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = rectregular(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

def setup(bot: commands.Bot):
    bot.add_cog(regular(bot=bot))
