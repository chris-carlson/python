import sys
from typing import Dict, List

from cac.color import Color
from cac.regex import Regex


class Args:

    @staticmethod
    def print_command_help(command: str, arguments: List[str] = None) -> None:
        colored_command: str = Color.highlight_text(command, Color.FORE['Magenta'])
        colored_arguments: List[str] = []
        if arguments is not None:
            colored_arguments = [Color.highlight_text(argument, Color.FORE['Green']) for argument in arguments]
        argument_string: str = ' ' + ', '.join(colored_arguments) if len(colored_arguments) > 0 else ''
        print(colored_command + argument_string)

    @staticmethod
    def print_argument_help(argument: str, values: List[str] = None, description: str = '') -> None:
        colored_argument: str = Color.highlight_text(argument, Color.FORE['Magenta'])
        colored_values: List[str] = []
        if values is not None:
            colored_values = [Color.highlight_text(value, Color.FORE['Green']) for value in values]
        value_string: str = ' [' + ', '.join(colored_values) + ']' if len(colored_values) > 0 else ''
        description_suffix: str = ': ' + description if len(description) > 0 else ''
        print(colored_argument + value_string + description_suffix)

    @staticmethod
    def print_flag_help(flag: str, arg: str = '', values: List[str] = None, description: str = '') -> None:
        colored_flag: str = Color.highlight_text('-' + flag, Color.FORE['Magenta'])
        colored_arg: str = ' ' + Color.highlight_text(arg, Color.FORE['Green']) if len(arg) > 0 else ''
        colored_values: List[str] = []
        if values is not None:
            colored_values = [Color.highlight_text(value, Color.FORE['Green']) for value in values]
        value_string: str = ' [' + ', '.join(colored_values) + ']' if len(colored_values) > 0 else ''
        description_suffix: str = ': ' + description if len(description) > 0 else ''
        print(colored_flag + colored_arg + value_string + description_suffix)

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
                if flag not in valid_flags and flag != 'help':
                    raise ValueError('Invalid flag entered: \'' + flag + '\'')

    def __len__(self) -> int:
        return len(self._args)

    def __str__(self) -> str:
        return '(' + str(self._args) + ', ' + str(self._flags) + ')'

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def args(self) -> List[str]:
        return self._args

    @property
    def flags(self) -> Dict[str, str]:
        return self._flags

    def get_arg(self, num: int, values: List[str] = None, regex: Regex = None) -> str:
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

    def get_flag(self, flag: str, values: List[str] = None) -> str:
        flag: str = self._flags[flag]
        if values is not None:
            if flag not in values:
                raise ValueError('Value for flag \'' + flag + '\' must be one of ' + str(values))
        return flag
