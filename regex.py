import re

from re import Match
from typing import List, Tuple


class Regex:

    def __init__(self, regex: str, case_sensitive=True) -> None:
        flags: int = 0 if case_sensitive else re.I
        self._rep = re.compile(regex, flags)

    def __str__(self) -> str:
        return self._rep.pattern

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def pattern(self) -> str:
        return self._rep.pattern

    def matches(self, string: str) -> bool:
        matches: List[str] = self.find_matches(string)
        return len(matches) > 0

    def find_match(self, string: str) -> str:
        matches: List[str] = self.find_matches(string)
        if len(matches) == 0:
            raise ValueError('Found no matches for string \'' + string + '\'')
        return matches[0]

    def find_match_index(self, string: str) -> Tuple[str, int]:
        match_indexes: List[Tuple[str, int]] = self.find_match_indexes(string)
        if len(match_indexes) == 0:
            raise ValueError('Found no matches for string \'' + string + '\'')
        return match_indexes[0]

    def find_matches(self, string: str) -> List[str]:
        return [match.group() for match in self._rep.finditer(string)]

    def find_match_indexes(self, string: str) -> List[Tuple[str, int]]:
        return [(match.group(), match.start()) for match in self._rep.finditer(string)]

    def count_groups(self, string: str) -> int:
        match: Match = self._rep.search(string)
        return len(match.groups())

    def find_groups(self, string: str) -> List[str]:
        match: Match = self._rep.search(string)
        return match.groups()

    def find_group(self, string: str, index: int = 1) -> str:
        match: Match = self._rep.search(string)
        return match.group(index)
