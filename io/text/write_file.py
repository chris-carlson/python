from collections import Iterable
from io import TextIOWrapper


class WriteFile:

    def __init__(self, file_name: str, append: bool = False) -> None:
        mode: str = 'a' if append else 'w'
        self._file: TextIOWrapper = open(file_name, mode=mode, encoding='utf-8', newline='\n')

    def write(self, string: str) -> None:
        self._file.write(str(string))

    def write_line(self, string: str = '') -> None:
        self._file.write(str(string) + '\n')

    def write_char_line(self, char: str, num: int) -> None:
        for _ in range(0, num):
            self._file.write(char)
        self._file.write('\n')

    def write_iterable(self, iterable: Iterable) -> None:
        for item in iterable:
            self._file.write(str(item) + '\n')

    def close(self) -> None:
        self._file.close()
