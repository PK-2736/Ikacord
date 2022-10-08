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
                        description="まずは <#982580263936749578>を呼んで <#982600148259602442>を書きましょう！\n"
                                            "<#1022072333978058802> に簡単なサーバー説明が書いてあります。",
                        color=0x00ff00,) 
        meg = await channel.send(embed=embed)
        await meg.add_reaction(CustomEmoji)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(982596256868225054)
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")


    #@commands.Cog.listener()
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