from typing import List

from cac.io.excel.cell import Cell
from cac.io.excel.letter_converter import LetterConverter


class Row(List[Cell]):

    @staticmethod
    def raw_data(data: List[object], bold: bool = False, color: str = None, number_format: str = None) -> 'Row':
        return Row([Cell(value, bold, color, number_format) for value in data])

    @staticmethod
    def create_header(data: List[object]) -> 'Row':
        return Row.raw_data(data, bold=True)

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

    def __add__(self, row: 'Row') -> 'Row':
        return Row(self._rep + row._rep)

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
