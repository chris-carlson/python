from typing import Dict, Sequence, TypeVar

E = TypeVar('E')


class MultiSet(Dict[E, int]):

    @staticmethod
    def count_from(sequence: Sequence[E]) -> 'MultiSet[E]':
        multi_set: MultiSet[E] = MultiSet[E]()
        for item in sequence:
            multi_set.add(item)
        return multi_set

    def add(self, element: E) -> None:
        if element in self:
            count: int = self[element]
            count += 1
            self[element] = count
        else:
            self[element] = 1
