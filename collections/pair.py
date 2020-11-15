from typing import Tuple, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class Pair(Tuple[K, V]):

    @property
    def key(self) -> K:
        return self[0]

    @property
    def value(self) -> V:
        return self[1]
