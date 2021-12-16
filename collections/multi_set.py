from typing import Dict, List, TypeVar

E = TypeVar('E')


class MultiSet(Dict[E, int]):

    def __init__(self, collection: List[E] = None) -> None:
        if collection is not None:
            for item in collection:
                self.add(item)

    def add(self, element: E) -> None:
        if element in self:
            count: int = self[element]
            count += 1
            self[element] = count
        else:
            self[element] = 1
