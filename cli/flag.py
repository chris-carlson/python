from typing import List, Tuple

from cac.regex import Regex


class Flag:

    def __init__(self, names: Tuple[str, str], description: str, parameter: str = None, values: List[str] = None,
                 regex: Regex = None) -> None:
        self._names: Tuple[str, str] = names
        self._description: str = description
        self._parameter: str = parameter
        self._values: List[str] = values
        self._regex: Regex = regex

    @property
    def names(self) -> Tuple[str, str]:
        return self._names

    @property
    def description(self) -> str:
        return self._description

    @property
    def parameter(self) -> str:
        return self._parameter

    @property
    def values(self) -> List[str]:
        return self._values

    @property
    def regex(self) -> Regex:
        return self._regex
