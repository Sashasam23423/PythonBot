import discord
from discord.ext import commands

from Interfaces.InterfacesMessage.IMessage import IMessage


class MessageCommandAdmin(IMessage):
    def __init__(self):
        pass

    async def send_message(self, ctx: commands.Context, member: discord.Member, title: str, message: str):
        await ctx.message.delete()
        ctx.emb = discord.Embed(title=title, colour=0x1abc9c)
        ctx.emb.set_author(name=member.name, icon_url=member.avatar_url)
        ctx.emb.set_footer(text=message.format(ctx.author.id), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=ctx.emb)
        return
