from typing import TypeVar

from cac.collections.ordered_set import OrderedSet
from cac.collections.pair_list import PairList

K = TypeVar('K')
V = TypeVar('V')


class MultiDict(PairList[K, OrderedSet[V]]):

    def add(self, key: K, value: V) -> None:
        if key in self:
            value_set: OrderedSet[V] = self.get(key)
            value_set.add(value)
        else:
            value_set: OrderedSet[V] = OrderedSet[V]()
            value_set.add(value)
            self._rep.append((key, value_set))
