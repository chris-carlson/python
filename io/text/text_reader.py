from io import TextIOWrapper
from typing import List, Set

from cac.collections.multi_set import MultiSet


class TextReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIOWrapper = open(file_name, mode='r')
        self._lines: List[str] = []

    @property
    def lines(self) -> List[str]:
        return self._lines

    def read_lines(self) -> None:
        self._lines = []
        try:
            for line in self._file:
                self._lines.append(line)
        except UnicodeDecodeError:
            pass

    def get_parse_line(self) -> str:
        parse_line: str = ''.join(self._lines)
        parse_line = parse_line.replace('\t', '')
        parse_line = parse_line.replace('\r', '')
        parse_line = parse_line.replace('\n', '')
        return parse_line

    def get_stripped_lines(self) -> List[str]:
        return [line.strip() for line in self._lines]

    def get_unique_lines(self) -> Set[str]:
        ordered_set: Set[str] = set()
        for line in self.get_stripped_lines():
            ordered_set.add(line)
        return ordered_set

    def count_unique_lines(self) -> MultiSet[str]:
        multi_set: MultiSet[str] = MultiSet[str]()
        for line in self.get_stripped_lines():
            multi_set.add(line)
        return multi_set

    def close(self) -> None:
        self._file.close()
