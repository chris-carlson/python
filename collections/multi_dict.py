from typing import Dict, List, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class MultiDict(Dict[K, List[V]]):

    def add(self, key: K) -> None:
        if key in self:
            raise ValueError('Key \'' + key + '\' is already in the MultiDict')
        self[key] = []

    def add(self, key: K, value: V) -> None:
        if key in self:
            values: List[V] = self.get(key)
            values.append(value)
        else:
            values: List[V] = []
            values.append(value)
            self[key] = values
