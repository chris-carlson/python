from typing import Dict, List, TypeVar

E = TypeVar('E')

class MultiSet(Dict[E, int]):

    def __init__(self, collection: List[E] = None) -> None:
        super().__init__()
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

    def extend(self, multi_set: 'MultiSet[E]') -> None:
        for key, count in multi_set.items():
            for _ in range(0, count):
                self.add(key)
