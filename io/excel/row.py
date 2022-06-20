from typing import List

from cac.io.excel.cell import Cell
from cac.io.excel.letter_converter import LetterConverter


class Row(List[Cell]):

    @staticmethod
    def raw_data(data: List[object]) -> 'Row':
        return Row([Cell(value) for value in data])

    def __init__(self, rep: List[Cell]) -> None:
        super().__init__()
        self._rep: List[Cell] = rep

    def __str__(self) -> str:
        return str(self._rep)

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rep)

    def __iter__(self) -> Cell:
        for cell in self._rep:
            yield cell

    def __getitem__(self, index: int) -> Cell:
        return self._rep[index]

    def get_cells(self, starting_letter: str, ending_letter: str) -> List[Cell]:
        starting_index: int = LetterConverter.convert_letter(starting_letter)
        ending_index: int = LetterConverter.convert_letter(ending_letter)
        return [self._rep[index] for index in range(starting_index, ending_index + 1)]

    def get_cell(self, letter: str) -> Cell:
        index: int = LetterConverter.convert_letter(letter)
        return self._rep[index]

    def set_cell(self, letter: str, value: object) -> None:
        index: int = LetterConverter.convert_letter(letter)
        self._rep[index] = Cell(value)

    def get_values(self, starting_letter: str, ending_letter: str) -> List[object]:
        return [cell.value for cell in self.get_cells(starting_letter, ending_letter)]

    def get_value(self, letter: str) -> object:
        cell: Cell = self.get_cell(letter)
        return cell.value
