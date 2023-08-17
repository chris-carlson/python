from functools import reduce
from typing import Any, Callable, List, TypeVar

from finder import Finder

E = TypeVar('E')

class Stream(List[E]):

    def __init__(self, item_list: List[E] = None) -> None:
        super().__init__()
        if item_list is not None:
            self.extend(item_list)

    def execute(self, lambda_function: Callable[[E], Any]) -> None:
        for item in self:
            lambda_function(item)

    def find(self, lambda_function: Callable[[E], Any]) -> E:
        filtered_items: List[E] = self.filter(lambda_function)
        return Finder.find_only(filtered_items)

    def find_optional(self, lambda_function: Callable[[E], Any]) -> E:
        filtered_items: List[E] = self.filter(lambda_function)
        return Finder.find_optional(filtered_items)

    def filter(self, lambda_function: Callable[[E], Any]) -> 'Stream[E]':
        return Stream(list(filter(lambda_function, self)))

    def map(self, lambda_function: Callable[[E], Any]) -> 'Stream[E]':
        return Stream(list(map(lambda_function, self)))

    def reduce(self, initial_value: E) -> E:
        return reduce(lambda accumulator, current: accumulator + current, self, initial_value)
