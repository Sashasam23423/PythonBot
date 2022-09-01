
import discord
from discord.ext import commands

from Interfaces.InterfacesMessage.IMessage import IMessage


class MessageLimit(IMessage):
    def __init__(self):
        pass

    async def send_message(self, ctx: commands.Context, limit: int):
        await ctx.message.delete()
        emb = discord.Embed(title="Ой!!!", colour=0x1abc9c)
        emb.set_footer(text=f"У вас ограничение до {limit} сообщений".format(), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        return
