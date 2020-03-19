import sys

from typing import List, Dict

from cac.color import Color
from cac.regex import Regex

class Args:

    @staticmethod
    def print_command_help(command: str, arguments: List[str] = []) -> None:
        command = Color.highlight_text(command, Color.FORE['Magenta'], Color.STYLE['Bright'])
        arguments = [Color.highlight_text(argument, Color.FORE['Green'], Color.STYLE['Bright']) for argument in arguments]
        argument_string: str = ' [' + ', '.join(arguments) + ']' if len(arguments) > 0 else ''
        print(command + argument_string)

    @staticmethod
    def print_argument_help(argument: str, values: List[str] = [], description: str = '') -> None:
        argument = Color.highlight_text(argument, Color.FORE['Magenta'], Color.STYLE['Bright'])
        values = [Color.highlight_text(value, Color.FORE['Green'], Color.STYLE['Bright']) for value in values]
        value_string: str = ' [' + ', '.join(values) + ']' if len(values) > 0 else ''
        description = ': ' + description if len(description) > 0 else ''
        print(argument + value_string + description)

    @staticmethod
    def print_flag_help(flag: str, arg: str = '', values: List[str] = [], description: str = '') -> None:
        flag = Color.highlight_text('-' + flag, Color.FORE['Magenta'], Color.STYLE['Bright'])
        arg = ' ' + Color.highlight_text(arg, Color.FORE['Green'], Color.STYLE['Bright']) if len(arg) > 0 else ''
        values = [Color.highlight_text(value, Color.FORE['Green'], Color.STYLE['Bright']) for value in values]
        value_string: str = ' [' + ', '.join(values) + ']' if len(values) > 0 else ''
        description = ': ' + description if len(description) > 0 else ''
        print(flag + arg + value_string + description)

    @staticmethod
    def exit() -> None:
        sys.exit()

    def __init__(self, valid_flags: List[str] = None, arg_flags: List[str] = None) -> None:
        self._args: List[str] = []
        self._flags: Dict[str, str] = {}
        args: List[str] = sys.argv[1:][:]
        while len(args) > 0:
            arg: str = args.pop(0)
            if arg.startswith('-'):
                if arg.startswith('--'):
                    flag: str = arg[2:]
                else:
                    flag: str = arg[1:]
                value: str = ''
                if arg_flags is not None and flag in arg_flags:
                    value = args.pop(0)
                self._flags[flag] = value
            else:
                self._args.append(arg)
        if valid_flags is not None:
            for flag in self._flags:
                if flag not in valid_flags:
                    raise ValueError('Invalid flag entered: \'' + flag + '\'')

    def __len__(self) -> int:
        return len(self._args)

    def __str__(self) -> str:
        return '(' + str(self._args) + ', ' + str(self._flags) + ')'

    def __repr__(self) -> str:
        return self.__str__()

    def get_args(self) -> List[str]:
        return self._args

    def get_arg(self, num: str, values: List[str] = None, regex: Regex = None) -> str:
        assert num >= 1
        arg: str = self._args[num - 1]
        if values is not None:
            if arg not in values:
                raise ValueError('Argument \'' + arg + '\' must be one of ' + str(values))
        if regex is not None:
            if not regex.matches(arg):
                raise ValueError('Argument \'' + arg + '\' must match regex ' + str(regex))
        return arg

    def has_flag(self, flag: str) -> bool:
        return flag in self._flags

    def get_flags(self) -> Dict[str, str]:
        return self._flags

    def get_flag(self, flag: str, values: List[str] = None) -> str:
        flag: str = self._flags[flag]
        if values is not None:
            if flag not in values:
                raise ValueError('Value for flag \'' + flag + '\' must be one of ' + str(values))
        return flag

    def should_print_help(self, expected_arguments: int) -> bool:
        return 'help' in self._flags or len(self._args) != expected_arguments
