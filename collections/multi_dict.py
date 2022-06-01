from typing import Dict, List, Tuple, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class MultiDict(Dict[K, List[V]]):

    def __init__(self, collection: List[Tuple[K, V]] = None) -> None:
        super().__init__()
        if collection is not None:
            for key, value in collection:
                self.add(key, value)

    def add(self, key: K, value: V = None) -> None:
        if key in self:
            if value is None:
                raise ValueError('Key \'' + str(key) + '\' is already in the MultiDict')
            values: List[V] = self.get(key)
            if value not in values:
                values.append(value)
        else:
            if value is None:
                values: List[V] = []
            else:
                values: List[V] = [value]
            self[key] = values
