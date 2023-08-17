import sys
from typing import Dict, List

from cac.cli.argument import Argument
from cac.cli.command import Command
from cac.color import Color
from cac.finder import Finder

HELP_ARGS: List[str] = ['help', '--help', '-h']
NO_DESCRIPTION: str = '[No description provided]'

def should_print_group_help() -> bool:
    return len(sys.argv) > 1 and sys.argv[1] in HELP_ARGS

class Group:

    def __init__(self, name: str, commands: List[Command]) -> None:
        self._name: str = name
        self._commands: List[Command] = [
                Command(command.name, command.arguments, command.flags, command.description, user_inputs=sys.argv[2:])
                for command in commands]
        self._commands.append(Command('help', [Argument('command', 'Command name to print help for', required=False)],
            user_inputs=sys.argv[2:]))

    def get_user_command(self) -> Command:
        if should_print_group_help():
            self.print_help()
            sys.exit()
        if sys.argv[1] == 'help':
            command: Command = self._find_command(2)
            command.print_help()
            sys.exit()
        return self._find_command(1)

    def _find_command(self, index: int) -> Command:
        command_names: List[str] = [command.name for command in self._commands]
        user_input: str = sys.argv[index]
        if user_input not in command_names:
            raise ValueError('Invalid command \'{0}\' given'.format(user_input))
        return Finder.find_only([command for command in self._commands if command.name == user_input])

    def print_help(self) -> None:
        help_command: Command = Finder.find_only([command for command in self._commands if command.name == 'help'])
        arguments: Dict[str, str] = help_command.parse_arguments()
        if 'command' in arguments:
            command_name: str = arguments['command']
            user_command: Command = Finder.find_only(
                [command for command in self._commands if command.name == command_name])
            user_command.print_help()
        else:
            self._print_group_help()

    def _print_group_help(self) -> None:
        group_name: str = Color.highlight_text(self._name, Color.FORE['Magenta'])
        generic_command: str = Color.highlight_text('<command>', Color.FORE['Green'])
        generic_args: str = Color.highlight_text('[<args>]', Color.FORE['Green'])
        print(group_name + ' ' + generic_command + ' ' + generic_args)
        print()
        user_commands: List[Command] = [command for command in self._commands if command.name != 'help']
        for command in user_commands:
            command_name: str = Color.highlight_text(command.name, Color.FORE['Cyan'])
            command_description: str = command.description if command.description is not None else NO_DESCRIPTION
            print(command_name + ': ' + command_description)
