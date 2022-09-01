import discord
from discord.ext import commands

from Interfaces.InterfacesMessage.IMessage import IMessage


class MessageErrorCommandAdmin(IMessage):
    def __init__(self):
        pass

    async def send_message(self, ctx: commands.Context, command: str):
        await ctx.message.delete()
        emb = discord.Embed(title="Ой!!!", colour=discord.Color.red())
        emb.set_footer(text=f"Вы не можете применить +{command} на себя или админов выше вас".format(), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        return
