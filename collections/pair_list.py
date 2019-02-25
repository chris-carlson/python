from typing import TypeVar, Generic, List, Tuple

K = TypeVar('K')
V = TypeVar('V')


class PairList(Generic[K, V]):

    def __init__(self) -> None:
        self._rep: List[Tuple[K, V]] = []

    def __str__(self) -> str:
        string: str = '{'
        for i in range(0, len(self._rep)):
            item: Tuple[K, V] = self._rep[i]
            string += str(item[0]) + ': ' + str(item[1])
            if i < len(self._rep) - 1:
                string += ', '
        string += '}'
        return string

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rep)

    def __contains__(self, key: K) -> bool:
        return key in self.keys()

    def __iter__(self) -> Tuple[K, V]:
        for item in self._rep:
            yield item

    def __getitem__(self, key: K) -> V:
        return self.get(key)

    def __setitem__(self, key: K, value: V) -> None:
        self.add(key, value)

    def get(self, key: K) -> V:
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in the list')
        for item in self._rep:
            if item[0] == key:
                return item[1]

    def keys(self) -> List[K]:
        return [item[0] for item in self._rep]

    def values(self) -> List[V]:
        return [item[1] for item in self._rep]

    def add(self, key: K, value: V) -> None:
        self._rep.append((key, value))

    def remove(self, key: K) -> V:
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in the list')
        item_to_remove: V = None
        for item in self._rep:
            if item[0] == key:
                item_to_remove = item
                break
        self._rep.remove(item_to_remove)
        return item_to_remove

    def sort_keys(self) -> None:
        if len(self._rep) > 0:
            if type(self._rep[0][0]) == str:
                self._rep.sort(key=lambda pair: pair[0].lower())
            else:
                self._rep.sort(key=lambda pair: pair[0])

    def sort_values(self) -> None:
        if len(self._rep) > 0:
            if type(self._rep[0][1]) == str:
                self._rep.sort(key=lambda pair: pair[1].lower())
            else:
                self._rep.sort(key=lambda pair: pair[1])

    def reverse(self) -> None:
        self._rep.reverse()
