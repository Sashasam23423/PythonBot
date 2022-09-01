import asyncio

import discord
from discord.ext import commands

from Builder.Builder import Builder
from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.MessageCommandAdmin import MessageCommandAdmin
from Interfaces.InterfacesMessage.MessageErrorCommandAdmin import MessageErrorCommandAdmin


class CommandMute(ICommand):
    def __init__(self):
        self.name ="mute"

    async def run(self, ctx: commands.Context, member: discord.Member, time: int):
        user = await Builder.CreateUser(ctx.author)
        if await user.Check(member):
            await MessageErrorCommandAdmin().send_message(ctx, self.name)
            return

        title = "Участник Был замучен! На : *" + str(time) + '* минуты'
        msg = "Его замутил: {}"
        await MessageCommandAdmin().send_message(ctx, member, title, msg)
        muted_role = discord.utils.get(ctx.message.guild.roles, name="Muted")
        await member.add_roles(muted_role)

        # Спим X минут, перед тем как снять роль.
        await asyncio.sleep(time * 60)
        # Снимаем роль замученного.
        await member.remove_roles(muted_role)
        return
