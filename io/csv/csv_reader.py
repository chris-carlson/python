from csv import reader as Reader
from io import TextIOWrapper
from typing import List


class CsvReader:

    def __init__(self, file_name: str) -> None:
        self._file: TextIOWrapper = open(file_name, newline='')

    def read_rows(self) -> List[List[str]]:
        rows: List[List[str]] = []
        reader: Reader = Reader(self._file, delimiter=',')
        for row in reader:
            rows.append(row)
        return rows

    def close(self) -> None:
        self._file.close()
