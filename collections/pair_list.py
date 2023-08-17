from typing import List, TypeVar

from cac.collections.pair import Pair

K = TypeVar('K')
V = TypeVar('V')

class PairList(List[Pair[K, V]]):

    def __init__(self, elements: List[Pair[K, V]] = None) -> None:
        super().__init__()
        if elements is not None:
            for element in elements:
                self.append(element)

    def add(self, key: K, value: V) -> None:
        self.append(Pair((key, value)))
