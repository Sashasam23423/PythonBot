

import discord
from discord.ext import commands

from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesExtantion.MyAdminCheck import MyAdminCheck
from Interfaces.InterfacesExtantion.MyYourselfCheck import MyYourselfCheck
from Interfaces.InterfacesMessage.MessageUnmute import MessageUnmute


class CommandUnmute(ICommand):
    def __init__(self):
        self.name ="unmute"

    async def run(self, ctx: commands.Context, member: discord.Member):

        if await MyYourselfCheck(self.name).check(ctx, member):
            return
        if await MyAdminCheck(self.name).check(ctx, member):
            return

        await MessageUnmute().send_message(ctx, member)
        muted_role = discord.utils.get(ctx.message.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await member.remove_roles(muted_role)
        return
