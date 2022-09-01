from discord.ext import commands
from Interfaces.InterfacesExtantion.IMyCheck import IMyCheck
from Interfaces.InterfacesMessage.MyMessage import MyMessage
import discord


class MyYourselfCheck(IMyCheck):
    def __init__(self, command) -> None:
        self.message = MyMessage()
        self.msg = "Внимание!!!"
        self.title = f"Вы не можете {command} себя!!!"

    async def check(self, ctx: commands.Context, member: discord.Member) -> bool:
        if member.id == ctx.author.id:
            await self.message.create_message(ctx, member, self.title, self.msg)
            return True
        return False
