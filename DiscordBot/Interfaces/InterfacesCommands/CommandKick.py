import discord
from discord.ext import commands

from Builder.Builder import Builder
from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.MessageCommandAdmin import MessageCommandAdmin
from Interfaces.InterfacesMessage.MessageErrorCommandAdmin import MessageErrorCommandAdmin


class CommandKick(ICommand):
    def __init__(self):
        self.name ="kick"

    async def run(self, ctx: commands.Context, member: discord.Member, reason: str):
        user = await Builder.CreateUser(ctx.author)
        if await user.Check(member):
            await MessageErrorCommandAdmin().send_message(ctx, self.name)
            return

        await member.kick(reason=reason)
        title = "Участник был кикнут! По причине: *" + reason + '*'
        msg = "Его кикнул: {}"
        await MessageCommandAdmin().send_message(ctx, member, title, msg)
        return
