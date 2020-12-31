from typing import List, Set

from cac.color import Color
from cac.finder import Finder
from cac.help.argument import Argument
from cac.help.flag import Flag


class Command:

    def __init__(self, name: str, flags: List[Flag], arguments: List[Argument]) -> None:
        self._name: str = name
        self._flags: List[Flag] = flags
        self._arguments: List[Argument] = arguments
        self._validate_input()

    @property
    def flags(self) -> List[Flag]:
        return self._flags

    @property
    def arguments(self) -> List[Argument]:
        return self._arguments

    def _validate_input(self) -> None:
        flag_names: List[str] = [flag.names[0] for flag in self._flags] + [flag.names[1] for flag in self._flags]
        duplicate_flag_names: Set[str] = Finder.find_duplicates(flag_names)
        if len(duplicate_flag_names) > 0:
            raise ValueError('Duplicate flag definitions found: ' + str(duplicate_flag_names))
        argument_names: List[str] = [argument.name for argument in self._arguments]
        duplicate_argument_names: Set[str] = Finder.find_duplicates(argument_names)
        if len(duplicate_argument_names) > 0:
            raise ValueError('Duplicate argument definitions found: ' + str(duplicate_argument_names))

    def print_help(self) -> None:
        command: str = Color.highlight_text(self._name, Color.FORE['Magenta'])
        if len(self._flags) > 0:
            command += self._create_flag_help()
        if len(self._arguments) > 0:
            command += self._create_argument_help()
        print(command)
        print()
        self._print_flag_details()

    def _create_flag_help(self) -> str:
        standalone_flag_names: List[str] = [flag.names[1] for flag in self._flags if
                len(flag.names[1]) > 0 and flag.parameter is None]
        command = ' [' + Color.highlight_text('-' + ''.join(standalone_flag_names), Color.FORE['Cyan']) + ']'
        parameter_flags: List[Flag] = [flag for flag in self._flags if
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
        for argument in self._arguments:
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
        for flag in self._flags:
            long_name: str = Color.highlight_text('--' + flag.names[0], Color.FORE['Cyan'])
            if flag.parameter is not None:
                long_name += ' ' + Color.highlight_text('<' + flag.parameter + '>', Color.FORE['Green'])
                if flag.values is not None and len(flag.values) > 0:
                    long_name += '=' + Color.highlight_text('{' + '|'.join(flag.values) + '}', Color.FORE['Yellow'])
            short_name: str = Color.highlight_text('-' + flag.names[1], Color.FORE['Cyan']) + ', ' if len(
                    flag.names[1]) > 0 else ''
            print(short_name + long_name + ': ' + flag.description)
