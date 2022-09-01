import discord
from discord.ext import commands

from Interfaces.InterfacesExtantion.IMyCheck import IMyCheck
from Interfaces.InterfacesMessage.MyMessage import MyMessage


class MyAdminCheck(IMyCheck):
    def __init__(self, command) -> None:
        self.message = MyMessage()
        self.msg = "Внимание!!!"
        self.title = f"Вы не можете {command} своего ранга и выше!!!"

    async def check(self, ctx: commands.Context, member: discord.Member) -> bool:
        if member.top_role >= ctx.author.top_role:
            await self.message.create_message(ctx, member, self.title, self.msg)
            return True
        return False