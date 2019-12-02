from typing import List, TypeVar

from cac.io.excel.letter_converter import LetterConverter

E = TypeVar('E')

class Row(List[E]):

    def __init__(self, rep: List[object]) -> None:
        self._rep: List[object] = rep

    def __str__(self) -> str:
        return str(self._rep)

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rep)

    def __iter__(self) -> object:
        for cell in self._rep:
            yield cell

    def __getitem__(self, index: int) -> object:
        return self._rep[index]

    def get_cell(self, letter: str) -> object:
        index: int = LetterConverter.convert_letter(letter)
        return self._rep[index]

    def set_cell(self, letter: str, value: object) -> object:
        index: int = LetterConverter.convert_letter(letter)
        self._rep[index] = value
