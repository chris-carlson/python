from typing import List, TextIO

from unidecode import unidecode

class TextReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIO = open(file_name, mode='r')

    def read_string(self) -> str:
        return '\n'.join([line for line in self._file])

    def read_raw_lines(self) -> List[str]:
        return [unidecode(line) for line in self._file]

    def read_lines(self) -> List[str]:
        return [line.rstrip() for line in self.read_raw_lines()]

    def read_stripped_lines(self) -> List[str]:
        return [line.strip() for line in self.read_raw_lines()]

    def close(self) -> None:
        self._file.close()
