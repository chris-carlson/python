from typing import List

from cac.io.excel.letter_converter import LetterConverter
from cac.io.excel.row import Row

class Worksheet:

    def __init__(self, title: str, rows: List[Row[object]]) -> None:
        self._title: str = title
        self._rows: List[Row[object]] = rows

    def __str__(self) -> str:
        return str(self._rows)

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> Row[object]:
        for row in self._rows:
            yield row

    def __getitem__(self, index: int) -> Row[object]:
        return self._rows[index]

    @property
    def title(self) -> str:
        return self._title

    @property
    def rows(self) -> List[Row[object]]:
        return self._rows

    def get_column_by_index(self, index: int) -> List[object]:
        return [row[index] for row in self._rows]

    def get_column_by_letters(self, letter: str) -> List[object]:
        index: int = LetterConverter.convert_letter(letter)
        return [row[index] for row in self._rows]
