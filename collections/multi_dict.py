from typing import Dict, List, Set, Tuple, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class MultiDict(Dict[K, Set[V]]):

    def add(self, key: K, value: V) -> None:
        if key in self:
            values: Set[V] = self.get(key)
            values.add(value)
        else:
            values: Set[V] = set()
            values.add(value)
            self[key] = values

    def to_sorted_list(self) -> List[Tuple[K, Set[V]]]:
        pair_list: List[Tuple[K, Set[V]]] = []
        for key, values in self.items():
            pair_list.append((key, values))
        pair_list.sort(key=lambda pair: pair[0])
        return pair_list
