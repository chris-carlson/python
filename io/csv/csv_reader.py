from csv import reader
from typing import List, TextIO


class CsvReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIO = open(file_name, newline='')

    def read_rows(self) -> List[List[str]]:
        rows: List[List[str]] = []
        csv_reader: reader = reader(self._file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
        return rows

    def close(self) -> None:
        self._file.close()
