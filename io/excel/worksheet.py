from typing import List

from cac.io.excel.letter_converter import LetterConverter
from cac.io.excel.row import Row


class Worksheet:

    def __init__(self, title: str, rows: List[Row]) -> None:
        self._title: str = title
        self._rows: List[Row] = rows

    def __str__(self) -> str:
        return str(self._rows)

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> Row:
        for row in self._rows:
            yield row

    def __getitem__(self, index: int) -> Row:
        return self._rows[index]

    @property
    def title(self) -> str:
        return self._title

    @property
    def rows(self) -> List[Row]:
        return self._rows

    def get_columns(self) -> List[object]:
        longest_row: int = max([len(row) for row in self._rows])
        return [self.get_column_by_index(index) for index in range(0, longest_row)]

    def get_column_by_index(self, index: int) -> List[object]:
        return [row[index] for row in self._rows]

    def get_column_by_letters(self, letter: str) -> List[object]:
        index: int = LetterConverter.convert_letter(letter)
        return [row[index] for row in self._rows]
