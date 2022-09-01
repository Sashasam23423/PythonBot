import discord
from discord.ext import commands

from Builder.Builder import Builder
from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.MessageCommandAdmin import MessageCommandAdmin
from Interfaces.InterfacesMessage.MessageErrorCommandAdmin import MessageErrorCommandAdmin


class CommandBanID(ICommand):
    def __init__(self):
        self.name ="banid"

    async def run(self, ctx: commands.Context, id: int, reason: str):
        user = await Builder.CreateUser(ctx.author)
        member = ctx.guild.fetch_member(id)
        if await user.Check(member):
            await MessageErrorCommandAdmin().send_message(ctx, self.name)
            return

        await member.ban(reason=reason)
        title = "Участник был забанен! По причине: *" + reason + '*'
        msg = "Его забанил: {}"
        await MessageCommandAdmin().send_message(ctx, member, title, msg)
        return
