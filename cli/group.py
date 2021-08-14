import sys
from typing import List

from cac.cli.command import Command
from cac.finder import Finder


class Group:

    def __init__(self, name: str, commands: List[Command]) -> None:
        self._name: str = name
        self._commands: List[Command] = commands

    def get_user_command(self) -> Command:
        command_names: List[str] = [command.name for command in self._commands]
        user_input: str = sys.argv[1]
        if user_input not in command_names:
            raise ValueError('Invalid command \'{0}\' given'.format(user_input))
        command: Command = Finder.find_only([command for command in self._commands if command.name == user_input])
        return Command(command.name, command.arguments, command.flags, sys.argv[2:])
