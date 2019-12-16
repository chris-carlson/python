from typing import Dict, Set, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class MultiDict(Dict[K, Set[V]]):

    def add(self, key: K) -> None:
        if key in self:
            raise ValueError('Key \'' + key + '\' is already in the MultiDict')
        self[key] = set()

    def add(self, key: K, value: V) -> None:
        if key in self:
            values: Set[V] = self.get(key)
            values.add(value)
        else:
            values: Set[V] = set()
            values.add(value)
            self[key] = values
