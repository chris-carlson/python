from csv import writer as Writer
from io import TextIOWrapper
from typing import List


class CsvWriter:

    def __init__(self, file_name: str, append: bool = False) -> None:
        mode: str = 'a' if append else 'w'
        self._file: TextIOWrapper = open(file_name, mode, newline='')

    def write_row(self, values: List[str]) -> None:
        writer: Writer = Writer(self._file, delimiter=',')
        writer.writerow(values)

    def close(self) -> None:
        self._file.close()
