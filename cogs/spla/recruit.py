from dataclasses import field
import re

import discord
from discord.ext import commands
from discord.ui import Button, View, Item
from datetime import datetime
from discord.commands import slash_command, Option

from cogs import guild_ids

print("rectの読み込み完了")

class CustomView(View):
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
                return embed.add_field(name=f"参加者", value=f"{interaction.user.mention} {datetime.now().strftime('%m/%d %H:%M')}", inline=True)

            for idlist in embed.fields[4].value.split("\n"):
                # フィールドの中にあるidと一致するか比較
                match = re.search(f"{interaction.user.id}",idlist)
                print(f"{interaction.user.id}",idlist)
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
                time = datetime.now().strftime("%m/%d %H:%M")
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

    def remove_embed(self, button: Button, interaction: discord.Interaction):  
        embed = interaction.message.embeds[0]     
        flag = True
        # mebedが存在する場合
        if embed:
            # embedの数が0個の時、
            if len(embed.fields) == 5:
                return embed.add_field(name="不参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%m/%d %H:%M')}", inline=False)

        for idlist in embed.fields[5].value.split("\n"):
                # フィールドの中にあるidと一致するか比較
                    match = re.search(f"{interaction.user.id}",idlist)
                    print(f"{interaction.user.id}",idlist)
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
                time = datetime.now().strftime("%m/%d %H:%M")
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
    # async def callback_sime(self, button: Button, interaction: discord.Interaction):
    #     embed = discord.Embed()
    #     embed.set_author(name=f"本当に募集をしめますか？", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))

    #     view = View()

    #     button_1 = Button(label="はい", style=discord.ButtonStyle.green, custom_id="ok")
    #     async def callback_ok(self):  
    #             embed = discord.Embed()
    #             embed.set_author(name=f"{interaction.user.name}の募集〆", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
    #             await interaction.message.reply(embed=embed)
    #     button_1.callback  = callback_ok
    #     view.add_item(button_1)
                    

    #     button_2 = Button(label="いいえ", style=discord.ButtonStyle.red, custom_id="no")
    #     async def callback_no(interaction: discord.Interaction): 
    #         await interaction.response.send_message(content="募集〆をキャンセルしました", delete_after=15.0)
    #     button_2.callback  = callback_no
    #     view.add_item(button_2)
                         
    #     await interaction.response.send_message(embed=embed, view=view, delete_after=15.0)

class MyModals(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xc2df52
        )
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=self.children[1].value, inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=self.children[3].value, inline=False)
        embed.add_field(name="参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%m/%d %H:%M')}", inline=True)
        embed.set_thumbnail(url="https://www.nintendo.co.jp/switch/av5ja/images/sp/kv/logo.png?imbypass=true")
        embed.set_author(name='募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message(f"<@&983297498271580170>: {CustomView.is_persistent(CustomView())}", embed=embed, view=CustomView())


class MyModalr(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0x13dbaf
        )
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=self.children[1].value, inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=self.children[3].value, inline=False)
        embed.add_field(name=datetime.now().strftime('%m/%d %H:%M'), value=interaction.user.mention, inline=True)
        embed.set_thumbnail(url="https://img.game8.jp/1624580/4a48b2bf985a9b5e79b78bdc7753f8b3.png/show")
        embed.set_author(name='レギュラーマッチ募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message("<@&983297498271580170>", embed=embed, view=CustomView())

class MyModalc(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdb8013
        )
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=self.children[1].value, inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=self.children[3].value, inline=False)
        embed.add_field(name=f"参加者\n{datetime.now().strftime('%m/%d %H:%M')}", value=interaction.user.mention, inline=True)
        embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/13/S2_Band_Grizzco_Industries.jpg/251px-S2_Band_Grizzco_Industries.jpg")
        embed.set_author(name='サーモンラン募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message("<@&983297498271580170>", embed=embed, view=CustomView())

class MyModalb(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdb4a13
        )
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=self.children[1].value, inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=self.children[3].value, inline=False)
        embed.add_field(name=f"参加者\n{datetime.now().strftime('%m/%d %H:%M')}", value=interaction.user.mention, inline=True)
        embed.set_thumbnail(url="http://cocohp.com/students/free2019/010/images/bt04.png")
        embed.set_author(name='バンカラマッチ募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message("<@&983297498271580170>", embed=embed, view=CustomView())
    
class MyModalp(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="時間"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xdb13cc
        )
        embed.add_field(name="募集人数", value=self.children[0].value, inline=True)
        embed.add_field(name="時間", value=self.children[1].value, inline=True)
        embed.add_field(name="通話の有無", value=self.children[2].value, inline=True)
        embed.add_field(name="募集内容", value=self.children[3].value, inline=False)
        embed.add_field(name=f"参加者\n{datetime.now().strftime('%m/%d %H:%M')}", value=interaction.user.mention, inline=True)
        embed.set_thumbnail(url="https://freepngimg.com/thumb/octopus/83095-splatoon-smile-squid-nose-download-free-image.png")
        embed.set_author(name='プライベートマッチ募集 by %s' % interaction.user.name, icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.response.send_message("<@&983297498271580170>", embed=embed, view=CustomView())

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    募集 = discord.SlashCommandGroup("rect", "募集関連", guild_ids=guild_ids)

    @募集.command(guild_ids=guild_ids, description="スプラ関連なんでも募集(フェス）")
    async def スプラ(self, interaction: discord.Interaction):
        if interaction.channel.id not in [982602254278357022, 981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339, 982602254278357022]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = MyModals(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @募集.command(guild_ids=guild_ids, description="バンカラマッチメンバーの募集")
    async def バンカラ(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = MyModalb(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @募集.command(guild_ids=guild_ids, description="レギュラーマッチメンバーの募集")
    async def レギュラー(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = MyModalr(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @募集.command(guild_ids=guild_ids, description="プライベートマッチメンバーの募集")
    async def プラベ(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = MyModalp(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

    @募集.command(guild_ids=guild_ids, description="サーモンランメンバーの募集")
    async def バイト(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。")
        modal = MyModalc(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot=bot))