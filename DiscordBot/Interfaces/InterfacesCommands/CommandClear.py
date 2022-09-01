from discord.ext import commands

from Builder.Builder import Builder
from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.MessageLimit import MessageLimit


class CommandClear(ICommand):
    def __init__(self):
        self.name = "clear"

    async def run(self, ctx: commands.Context, limit: int):
        user = await Builder.CreateUser(ctx.author)
        if await user.Check_limit(limit):
            await MessageLimit().send_message(ctx, user.limit)
            return
        await ctx.channel.purge(limit=limit)
        return
