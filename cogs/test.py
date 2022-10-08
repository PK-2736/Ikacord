from email import message
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import io
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ui import Button, View, Item
from datetime import datetime
import textwrap
import requests

from cogs import guild_ids

print("testの読み込み完了")

class spla3(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        style=discord.ButtonStyle.green,
        label="参加",
        custom_id="join"
    )
    async def callback_join(self, button: Button, interaction: discord.Interaction):
        for child in self.children: 
            child.disabled = True 
        embed = interaction.message.embeds[0]
        flag = True
        if embed:
            if len(embed.fields) == 0:
                return embed.add_field(name=f"参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=True)

            for idlist in embed.fields[0].value.split("\n"):
                match = re.search(f"{interaction.user.id}",idlist)

            if match:
                flag = False
                embed2 = discord.Embed(description=f"{interaction.user.name}は既に参加しています")
                await interaction.response.send_message(embed=embed2,ephemeral = True)
                return embed

            if flag:
                users = [interaction.user.mention]
                cm = embed.fields[0].value
                tmp = "\n".join([str(user) for user in users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(0,name="参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
                await interaction.response.edit_message(embed=embed)
                embed = discord.Embed()
                embed.set_author(name=f"{interaction.user.name}が参加しました", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
                await interaction.message.reply(f"{interaction.message.interaction.user.mention}{interaction.user.mention}", embed=embed, delete_after=120.0)                

    @discord.ui.button(
        style=discord.ButtonStyle.blurple,
        label="取り消し",
        custom_id="remove"
    )
    async def callback_remove(self, button: Button, interaction: discord.Interaction):
        for child in self.children: 
            child.disabled = True
        embed = interaction.message.embeds[0]     
        flag = True
        if embed:
            if len(embed.fields) == 1:
                return embed.add_field(name="不参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)

            for idlist in embed.fields[1].value.split("\n"):
                match = re.search(f"{interaction.user.id}",idlist)

            if match:
                flag = False
                embed2 = discord.Embed(description=f"{interaction.user.name}は既に取り消しています")
                await interaction.response.send_message(embed=embed2,ephemeral = True)
                return embed

            if flag:
                summon_users = [interaction.user.mention]
                cm = embed.fields[1].value
                tmp = "\n".join([str(user) for user in summon_users])
                summon = tmp if tmp else "なし"
                time = datetime.now().strftime("%H:%M")
                embed.set_field_at(1,name="不参加者リスト", value=f"{cm}\n{summon} {time}", inline=False)
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
        for child in self.children: 
            child.disabled = True 
        embed = discord.Embed()
        embed.set_author(name=f"{interaction.user.name}の募集〆", icon_url=interaction.user.display_avatar.replace(format="png", static_format="png"))
        await interaction.message.reply(embed=embed)
        await interaction.response.edit_message(view=self)

class recttest(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="時間", required=False))
        self.add_item(discord.ui.InputText(label="募集人数"))
        self.add_item(discord.ui.InputText(label="通話の有無"))
        self.add_item(discord.ui.InputText(label="募集内容", style=discord.InputTextStyle.long, required=False))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        img = Image.open("images/rect/regular.png")
        draw = ImageDraw.Draw(img) 
        font_path = "data/LightNovelPOPv2.otf"
        font = ImageFont.truetype(font_path, 80)
        font2 = ImageFont.truetype(font_path, 80)
        time = '' if self.children[0].value else "集まり次第"
        draw.text((1150,380), f"{self.children[0].value}{time}" ,(0,0,0),font=font)
        draw.text((1150,700), self.children[1].value ,(0,0,0),font=font)
        draw.text((1150,1000), self.children[2].value ,(0,0,0),font=font)

        content = '' if self.children[3].value else "記載なし"
        wrap_list = textwrap.wrap(f"{self.children[3].value}{content}", 8)  
        font2 = ImageFont.truetype(font_path, 70)  
        line_counter = 0 
        for line in wrap_list:
            y = line_counter*80+600
            draw.multiline_text((300, y),line, fill=(0,0,0), font=font2)
            line_counter = line_counter +1 
        img_binary = io.BytesIO()
        img.save(img_binary, format='PNG')
        img_binary.seek(0)
        f = discord.File(img_binary, filename='image.png')

        embed = discord.Embed(
            timestamp=datetime.now(),
            color=0xe9dede
        )
        embed.add_field(name="参加者リスト", value=f"{interaction.user.mention} {datetime.now().strftime('%H:%M')}", inline=False)
        embed.set_footer(text='イカコード3|スプラ募集')
        await interaction.followup.send(f"<@&983297498271580170>: {spla3.is_persistent(spla3())}", embed=embed, file=f, view=spla3())

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=guild_ids)
    async def test(self, interaction: discord.Interaction):
        if interaction.channel.id not in [981474117020712973, 1007288564247179347, 1011555949837824001, 1011556210719338537, 1011556131786735677, 802345513495822339]:
            return await interaction.respond("エラー：募集コマンドを実行出来るのは <#981474117020712973> だけです。",ephemeral = True)
        modal = recttest(title="募集の詳細を説明")
        await interaction.response.send_modal(modal)

def setup(bot: commands.Bot):
    bot.add_cog(test(bot=bot))