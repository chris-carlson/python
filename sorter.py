from typing import Any, Callable, Dict, List, Tuple, TypeVar

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
    def sort(collection: Dict[K, V], lambda_function: Callable[[Tuple[K, V]], Any] = lambda item: item,
             reverse: bool = False) -> List[Tuple[K, V]]:
        sorted_list: List[Tuple[K, V]] = list(collection.items())
        sorted_list.sort(key=lambda_function)
        if reverse:
            sorted_list.reverse()
        return sorted_list
