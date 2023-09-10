from typing import Any, Callable, Dict, List, TypeVar

from cac.collections.pair import Pair

E = TypeVar('E')
K = TypeVar('K')
V = TypeVar('V')

class ListSorter:

    @staticmethod
    def sort(collection: List[E], lambda_function: Callable[[E], Any] = lambda item: item, reverse: bool = False) -> \
            List[E]:
        sorted_list: List[E] = list(collection)
        sorted_list.sort(key=lambda_function)
        if reverse:
            sorted_list.reverse()
        return sorted_list

class DictSorter:

    @staticmethod
    def sort(collection: Dict[K, V], lambda_function: Callable[[Pair[K, V]], Any] = lambda item: item,
            reverse: bool = False) -> List[Pair[K, V]]:
        sorted_list: List[Pair[K, V]] = [Pair((key, value)) for key, value in collection.items()]
        sorted_list.sort(key=lambda_function)
        if reverse:
            sorted_list.reverse()
        return sorted_list
