from csv import writer
from typing import List, TextIO

class CsvWriter:

    def __init__(self, file_name: str, append: bool = False) -> None:
        mode: str = 'a' if append else 'w'
        self._file: TextIO = open(file_name, mode, newline='')

    def write_row(self, values: List[str]) -> None:
        csv_writer: writer = writer(self._file, delimiter=',')
        csv_writer.writerow(values)

    def close(self) -> None:
        self._file.close()
