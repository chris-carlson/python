from typing import Dict, TypeVar

E = TypeVar('E')


class MultiSet(Dict[E, int]):

    def add(self, element: E) -> None:
        if element in self:
            count: int = self[element]
            count += 1
            self[element] = count
        else:
            self[element] = 1
