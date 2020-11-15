import random
from typing import List


class Random:

    @staticmethod
    def get_random_number(start: int, end: int) -> int:
        random.seed()
        return random.randint(start, end)

    @staticmethod
    def get_random_index(elements: List[object]) -> int:
        random.seed()
        return random.randrange(0, len(elements))

    @staticmethod
    def get_random_element(elements: List[object], should_remove: bool = False) -> object:
        if len(elements) == 0:
            raise ValueError('List does not have any elements')
        random.seed()
        index: int = random.randrange(0, len(elements))
        element: object = elements[index]
        if should_remove:
            elements.pop(index)
        return element

    @staticmethod
    def get_random_percent() -> float:
        random.seed()
        return random.random() * 100
