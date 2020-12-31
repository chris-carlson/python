from typing import List

from cac.color import Color
from cac.cli.command import Command
from cac.cli.flag import Flag


class Printer:

    def __init__(self, command: Command) -> None:
        self._command: Command = command

    def print_help(self) -> None:
        command: str = Color.highlight_text(self._command.name, Color.FORE['Magenta'])
        if len(self._command.flags) > 0:
            command += self._create_flag_help()
        if len(self._command.arguments) > 0:
            command += self._create_argument_help()
        print(command)
        if len(self._command.flags) > 0:
            print()
            self._print_flag_details()

    def _create_flag_help(self) -> str:
        standalone_flag_names: List[str] = [flag.names[1] for flag in self._command.flags if
                len(flag.names[1]) > 0 and flag.parameter is None]
        command = ' [' + Color.highlight_text('-' + ''.join(standalone_flag_names), Color.FORE['Cyan']) + ']'
        parameter_flags: List[Flag] = [flag for flag in self._command.flags if
                len(flag.names[1]) > 0 and flag.parameter is not None]
        command += ''.join([
                '[' + Color.highlight_text('-' + flag.names[1], Color.FORE['Cyan']) + ' ' + self._create_flag_parameter(
                        flag) + ']' for flag in parameter_flags])
        return command

    def _create_flag_parameter(self, flag: Flag) -> str:
        parameter: str = Color.highlight_text('<' + flag.parameter + '>', Color.FORE['Green'])
        if flag.values is not None and len(flag.values) > 0:
            parameter += '=' + Color.highlight_text('{' + '|'.join(flag.values) + '}', Color.FORE['Yellow'])
        return parameter

    def _create_argument_help(self) -> str:
        command: str = ''
        for argument in self._command.arguments:
            argument_name: str = Color.highlight_text('<' + argument.name + '>', Color.FORE['Green'])
            if argument.values is not None and len(argument.values) > 0:
                argument_name += '=' + Color.highlight_text('{' + '|'.join(argument.values) + '}', Color.FORE['Yellow'])
            if argument.repeated:
                argument_name += '...'
            if argument.required:
                command += ' ' + argument_name
            else:
                command += ' [' + argument_name + ']'
        return command

    def _print_flag_details(self) -> None:
        for flag in self._command.flags:
            long_name: str = Color.highlight_text('--' + flag.names[0], Color.FORE['Cyan'])
            if flag.parameter is not None:
                long_name += ' ' + Color.highlight_text('<' + flag.parameter + '>', Color.FORE['Green'])
                if flag.values is not None and len(flag.values) > 0:
                    long_name += '=' + Color.highlight_text('{' + '|'.join(flag.values) + '}', Color.FORE['Yellow'])
            short_name: str = Color.highlight_text('-' + flag.names[1], Color.FORE['Cyan']) + ', ' if len(
                    flag.names[1]) > 0 else ''
            print(short_name + long_name + ': ' + flag.description)
