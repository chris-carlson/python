from typing import List

class Worksheet:

    def __init__(self, title: str, rows: List[List[object]]) -> None:
        self._title: str = title
        self._rows: List[List[object]] = rows

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> List[object]:
        for row in self._rows:
            yield row

    def __getitem__(self, index: int) -> List[object]:
        return self._rows[index]

    @property
    def title(self) -> str:
        return self._title
