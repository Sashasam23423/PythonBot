from DiscordBot.Users.IUser import IUser


class Builder:
    def __init__(self):
        pass

    async def CreateUser(author):
        return IUser(author)
