from typing import Generic, List, Tuple, TypeVar

from cac.collections.pair_list import PairList

E = TypeVar('E')


class MultiSet(Generic[E]):

    def __init__(self) -> None:
        self._rep: PairList = PairList()

    def __str__(self) -> str:
        return self._rep.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rep)

    def __contains__(self, key: E) -> bool:
        return key in self.keys()

    def __iter__(self) -> Tuple[E, int]:
        for item in self._rep:
            yield item

    def __getitem__(self, key: E) -> int:
        return self.get(key)

    def get(self, key: E) -> int:
        return self._rep.get(key)

    def keys(self) -> List[E]:
        return self._rep.keys()

    def values(self) -> List[int]:
        return self._rep.values()

    def add(self, key: E) -> None:
        if key in self:
            for item in self._rep:
                if item[0] == key:
                    count: int = item[1]
                    self._rep.remove(item[0])
                    self._rep.add(key, count + 1)
                    break
        else:
            self._rep.add(key, 1)

    def remove(self, key: E) -> None:
        self._rep.remove(key)

    def sort_keys(self) -> None:
        self._rep.sort_keys()

    def sort_values(self) -> None:
        self._rep.sort_values()

    def reverse(self) -> None:
        self._rep.reverse()
