import sys
from typing import List, Dict

from cac.color import Color

class Args:

    @staticmethod
    def print_help(flag: str, arg: str, description: str) -> None:
        print(Color.highlight_text('-' + flag, Color.FORE['Magenta'], Color.STYLE['Bright']) + ' ' + Color.highlight_text(arg, Color.FORE['Green'], Color.STYLE['Bright']) + ': ' + description)

    def __init__(self, num_args: int = -1, arg_flags: List[str] = None) -> None:
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
        if num_args != -1:
            assert len(self._args) == num_args

    def __len__(self) -> int:
        return len(self._args)

    def __str__(self) -> str:
        return '(' + str(self._args) + ', ' + str(self._flags) + ')'

    def __repr__(self) -> str:
        return self.__str__()

    def get_args(self) -> List[str]:
        return self._args

    def get_arg(self, num) -> str:
        assert num >= 1
        return self._args[num - 1]

    def has_flag(self, flag) -> bool:
        return flag in self._flags

    def get_flag(self, flag) -> str:
        return self._flags[flag]
