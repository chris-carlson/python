from typing import TypeVar

K = TypeVar('K')
V = TypeVar('V')


class Pair:

    def __init__(self, key: K, value: V) -> None:
        self._key: K = key
        self._value: V = value

    @property
    def key(self) -> K:
        return self._key

    @property
    def value(self) -> V:
        return self._value
