from typing import List, Set

from cac.cli.argument import Argument
from cac.cli.flag import Flag
from cac.finder import Finder


class Command:

    def __init__(self, name: str, arguments: List[Argument], flags: List[Flag] = None) -> None:
        self._name: str = name
        self._arguments: List[Argument] = arguments
        self._flags: List[Flag] = flags if flags is not None else []
        self._validate_input()

    @property
    def name(self) -> str:
        return self._name

    @property
    def arguments(self) -> List[Argument]:
        return self._arguments

    @property
    def flags(self) -> List[Flag]:
        return self._flags

    def _validate_input(self) -> None:
        flag_names: List[str] = [flag.names[0] for flag in self._flags] + [flag.names[1] for flag in self._flags]
        duplicate_flag_names: Set[str] = Finder.find_duplicates(flag_names)
        if len(duplicate_flag_names) > 0:
            raise ValueError('Duplicate flag definitions found: ' + str(duplicate_flag_names))
        argument_names: List[str] = [argument.name for argument in self._arguments]
        duplicate_argument_names: Set[str] = Finder.find_duplicates(argument_names)
        if len(duplicate_argument_names) > 0:
            raise ValueError('Duplicate argument definitions found: ' + str(duplicate_argument_names))
