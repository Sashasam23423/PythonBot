from discord.ext import commands
from Interfaces.InterfacesMessage.MyMessage import MyMessage
import discord


class IMyCheck:

    def __init__(self) -> None:
        self.message = MyMessage()
        self.msg = "Стратегия проверок"
        self.title = "Моя стратегия"

    async def check(self, ctx: commands.Context, member: discord.Member) -> bool:
        await self.message.create_message(ctx, member, self.title, self.msg)
        return True





