from io import TextIOWrapper
from typing import List, Set


class TextReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIOWrapper = open(file_name, mode='r')

    def read_raw_lines(self) -> List[str]:
        lines: List[str] = []
        try:
            lines = [line for line in self._file]
        except UnicodeDecodeError:
            pass
        return lines

    def read_lines(self) -> List[str]:
        return [line.rstrip() for line in self.read_raw_lines()]

    def read_stripped_lines(self) -> List[str]:
        return [line.strip() for line in self.read_raw_lines()]

    def close(self) -> None:
        self._file.close()
