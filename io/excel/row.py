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

    def get_cells(self, starting_letter: str, ending_letter: str) -> List[Cell]:
        cells: List[Cell] = []
        starting_index: int = LetterConverter.convert_letter(starting_letter)
        ending_index: int = LetterConverter.convert_letter(ending_letter)
        for index in range(starting_index, ending_index + 1):
            cells.append(self._rep[index])
        return cells

    def get_cell(self, letter: str) -> Cell:
        index: int = LetterConverter.convert_letter(letter)
        return self._rep[index]

    def set_cell(self, letter: str, value: object) -> None:
        index: int = LetterConverter.convert_letter(letter)
        self._rep[index] = Cell(value)
