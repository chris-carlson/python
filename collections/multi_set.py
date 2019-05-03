from typing import Dict, List, Tuple, TypeVar

E = TypeVar('E')


class MultiSet(Dict[E, int]):

    def add(self, element: E) -> None:
        if element in self:
            count: int = self[element]
            count += 1
            self[element] = count
        else:
            self[element] = 1

    def to_sorted_list(self, sort_values=False) -> List[Tuple[E, int]]:
        pair_list: List[Tuple[E, int]] = []
        for element, count in self.items():
            pair_list.append((element, count))
        sort_index: int = 1 if sort_values else 0
        pair_list.sort(key=lambda pair: pair[sort_index])
        if sort_values:
            pair_list.reverse()
        return pair_list
