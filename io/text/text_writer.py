from typing import TextIO

from unidecode import unidecode


class TextWriter:

    def __init__(self, file_name: str, tab_size: int = 0, append: bool = False) -> None:
        mode: str = 'a' if append else 'w'
        self._file: TextIO = open(file_name, mode=mode, encoding='utf-8', newline='\n')
        self._tab_size: int = tab_size

    def write(self, string: str, num_tabs: int = 0) -> None:
        self._file.write(self._get_tab_spaces(num_tabs) + unidecode(string))

    def write_line(self, string: str = '', num_tabs: int = 0) -> None:
        self._file.write(self._get_tab_spaces(num_tabs) + unidecode(string) + '\n')

    def write_char_line(self, char: str, num: int) -> None:
        for _ in range(0, num):
            self._file.write(char)
        self._file.write('\n')

    def close(self) -> None:
        self._file.close()

    def _get_tab_spaces(self, num_tabs: int) -> str:
        return ''.join([' ' * self._tab_size for _ in range(0, num_tabs)])
