from typing import List, Tuple, TypeVar

E = TypeVar('E')

class Comparer:

    def __init__(self, list1: List[E], list2: List[E]) -> None:
        self._list1: List[E] = list1
        self._list2: List[E] = list2

    def find_common_items(self) -> List[E]:
        return [item for item in self._list1 if item in self._list2]

    def find_unique_items(self) -> Tuple[List[E], List[E]]:
        unique_list1: List[E] = [item for item in self._list1 if item not in self._list2]
        unique_list2: List[E] = [item for item in self._list2 if item not in self._list1]
        return unique_list1, unique_list2
