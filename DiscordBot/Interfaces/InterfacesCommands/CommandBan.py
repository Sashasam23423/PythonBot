import discord
from discord.ext import commands

from Builder.Builder import Builder
from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.MessageCommandAdmin import MessageCommandAdmin
from Interfaces.InterfacesMessage.MessageErrorCommandAdmin import MessageErrorCommandAdmin


class CommandBan(ICommand):
    def __init__(self):
        self.name ="ban"

    async def run(self, ctx: commands.Context, member: discord.Member, reason: str):
        user = await Builder.CreateUser(ctx.author)
        if await user.Check(member):
            await MessageErrorCommandAdmin().send_message(ctx, self.name)
            return

        await member.ban(reason=reason)
        title = "Участник был забанен! По причине: *" + reason + '*'
        msg = "Его забанил: {}"
        await MessageCommandAdmin().send_message(ctx, member, title, msg)
        return
