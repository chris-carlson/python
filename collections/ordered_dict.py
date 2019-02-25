from typing import TypeVar

from cac.collections.pair_list import PairList

K = TypeVar('K')
V = TypeVar('V')


class OrderedDict(PairList[K, V]):

    def __setitem__(self, key: K, value: V) -> None:
        if key in self:
            for item_index in range(0, len(self._rep)):
                if self._rep[item_index][0] == key:
                    self._rep[item_index] = (key, value)
        else:
            self.add(key, value)

    def add(self, key: K, value: V) -> None:
        if key not in self:
            self._rep.append((key, value))
