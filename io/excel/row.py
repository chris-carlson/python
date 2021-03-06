from typing import Dict, List, TypeVar

from cac.io.excel.letter_converter import LetterConverter

E = TypeVar('E')


class Row(List[E]):

    def __init__(self, rep: List[object], bold: bool = False, number_formats: Dict[str, str] = None) -> None:
        super().__init__()
        self._rep: List[object] = rep
        self._bold: bool = bold
        self._number_formats: Dict[str, str] = number_formats if number_formats is not None else {}

    def __eq__(self, other: 'Row') -> bool:
        return self._rep == other._rep

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

    @property
    def bold(self) -> bool:
        return self._bold

    @property
    def number_formats(self) -> Dict[str, str]:
        return self._number_formats

    def get_cells(self, starting_letter: str, ending_letter: str) -> List[object]:
        cells: List[object] = []
        starting_index: int = LetterConverter.convert_letter(starting_letter)
        ending_index: int = LetterConverter.convert_letter(ending_letter)
        for index in range(starting_index, ending_index + 1):
            cells.append(self._retrieve_cell(index))
        return cells

    def get_cell(self, letter: str) -> object:
        index: int = LetterConverter.convert_letter(letter)
        return self._retrieve_cell(index)

    def set_cell(self, letter: str, value: object) -> None:
        index: int = LetterConverter.convert_letter(letter)
        self._rep[index] = value

    # noinspection PyUnresolvedReferences
    def _retrieve_cell(self, index: int) -> object:
        cell: object = self._rep[index]
        if type(cell) == str:
            cell = cell.strip()
        return cell

    def extend(self, rep: List[object]) -> None:
        self._rep.extend(rep)
