import random
from enum import IntEnum
from typing import List, TypeVar

E = TypeVar('E')

class Random:

    @staticmethod
    def get_random_number(start: int, end: int) -> int:
        random.seed()
        return random.randint(start, end)

    @staticmethod
    def get_random_index(elements: List[E]) -> int:
        random.seed()
        return random.randrange(0, len(elements))

    @staticmethod
    def get_random_element(elements: List[E], should_remove: bool = False) -> E:
        if len(elements) == 0:
            raise ValueError('List does not have any elements')
        random.seed()
        index: int = random.randrange(0, len(elements))
        element: E = elements[index]
        if should_remove:
            elements.pop(index)
        return element

    @staticmethod
    def get_random_percent() -> float:
        random.seed()
        return random.random() * 100

    @staticmethod
    def flip_coin(weight: float = 50.0) -> int:
        percent: float = Random.get_random_percent()
        return CoinSide.HEADS if percent < weight else CoinSide.TAILS

class CoinSide(IntEnum):
    HEADS: int = 0
    TAILS: int = 1
