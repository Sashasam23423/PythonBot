import discord
from discord.ext import commands

from Interfaces.InterfacesCommands.CommandBanID import CommandBanID
from Interfaces.InterfacesCommands.CommandClear import CommandClear
from Interfaces.InterfacesCommands.CommandHello import CommandHello
from Interfaces.InterfacesCommands.CommandKick import CommandKick
from Interfaces.InterfacesCommands.CommandKickID import CommandKickID
from Interfaces.InterfacesCommands.CommandMute import CommandMute
from Interfaces.InterfacesCommands.CommandUnmute import CommandUnmute
from Interfaces.InterfacesCommands.CommandBan import CommandBan
from roles import roles
from Interfaces.InterfacesExtantion.IMyCheck import IMyCheck
from Interfaces.InterfacesMessage.MyMessage import MyMessage


class Bot(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.check = IMyCheck()
        self.my_message = MyMessage()

    @commands.command()
    async def hello(self):
        CommandHello().run()
        return

    @commands.command()
    async def upd(self, ctx: commands.Context):
        await ctx.message.delete()
        embed = discord.Embed(color=0x1abc9c, title='Список команд:', description="""
                27/07/2022
                **1** banid - теперь доступен бан по id 
                **2** kickid - теперь доступен кик по id 
                **3* не большая доработка собщений от бота
              """)
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx: commands.Context):
        await ctx.message.delete()
        embed = discord.Embed(color=0x1abc9c, title='Список команд:', description="""
           1.Команда "ban" - банит пользователя.
           1.1  Команда "banid" - банит пользователя по id.
           2.Команда "kick" - кикает пользователя.
           2.2 Команда "kick" - кикает пользователя по id.
           3.Команда "mute" - мутит пользователя на время в минутах.
           4.Комманад "unmute" - снимает мут с пользователя.
           """)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"])
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        await CommandBan().run(ctx, member, reason)
        return


    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"])
    async def banid(self, ctx: commands.Context, id: int, *, reason=None):
        await CommandBanID().run(ctx, id, reason)
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"])
    async def create_role_muted(self):
        guild = self.guild
        await guild.create_role(name="Muted")
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"], roles["Администратор"])
    async def mute(self, ctx: commands.Context, member: discord.Member, time: int):
        await CommandMute().run(ctx, member, time)
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"], roles["Администратор"])
    async def unmute(self, ctx: commands.Context, member: discord.Member):
        await CommandUnmute().run(ctx, member)
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"], roles["Администратор"])
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        await CommandKick().run(ctx, member, reason)
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"], roles["Администратор"])
    async def kickid(self, ctx: commands.Context, id: int, *, reason=None):
        await CommandKickID().run(ctx, id, reason)
        return

    @commands.command()
    @commands.has_any_role(roles["Зам. Владельца"], roles["Владелец"], roles["Куратор"])
    async def clear(self, ctx: commands.Context, limit: int):
        await CommandClear().run(ctx, limit)
        return


def setup(bot):
    bot.add_cog(Bot(bot))
