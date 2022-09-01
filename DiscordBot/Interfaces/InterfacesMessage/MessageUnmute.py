import discord
from discord.ext import commands

from Interfaces.InterfacesMessage.IMessage import IMessage


class MessageUnmute(IMessage):
    def __init__(self):
        pass

    async def send_message(self, ctx: commands.Context, member: discord.Member):
        await ctx.message.delete()
        emb = discord.Embed(title="Участник был размучен!", colour=0x1abc9c)
        emb.set_author(name=member.name, icon_url=member.avatar_url)
        emb.set_footer(text="Его разамутил: {}".format(ctx.author.id), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)