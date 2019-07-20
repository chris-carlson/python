from io import TextIOWrapper
from typing import List, Set


class TextReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIOWrapper = open(file_name, mode='r')

    def read_lines(self) -> List[str]:
        lines: List[str] = []
        try:
            for line in self._file:
                lines.append(line.strip())
        except UnicodeDecodeError:
            pass
        return lines

    def close(self) -> None:
        self._file.close()
