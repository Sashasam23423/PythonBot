from discord.ext import commands


class IMessage:
    async def send_message(self, ctx: commands.Context, text: str):
        await ctx.send(text)