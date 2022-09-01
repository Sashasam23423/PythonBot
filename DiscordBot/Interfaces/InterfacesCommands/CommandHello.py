from Interfaces.InterfacesCommands.ICommand import ICommand
from Interfaces.InterfacesMessage.IMessage import IMessage


class CommandHello(ICommand):
    def __init__(self):
        self.name = "hello"

    async def run(self):
        IMessage.send_message("Hello")