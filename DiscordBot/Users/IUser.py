import discord
from discord.ext import commands

from Interfaces.InterfacesMessage.MyMessage import MyMessage
from roles_limit import roles_limit


class IUser:
    def __init__(self, author):
        self.user = author
        self.limit = roles_limit[author.top_role.id]

    async def Check_limit(self, limit: int) -> bool:
        return self.limit < limit

    async def Check(self,  member: discord.Member) -> bool:
        if self.user.top_role.id == member.id:
            return True
        if member.top_role >= self.user.top_role:
            return True
        return False
