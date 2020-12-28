from typing import Callable, List, Sequence


class Sorter:

    # noinspection PyUnresolvedReferences,PyTypeChecker
    @staticmethod
    def sort(collection: Sequence[object], lambda_function: Callable[[object], object] = lambda item: item, reverse: bool = False) -> List[object]:
        if issubclass(type(collection), dict):
            sorted_list: List[object] = list(collection.items())
        else:
            sorted_list: List[object] = list(collection)
        sorted_list.sort(key=lambda_function)
        if reverse:
            sorted_list.reverse()
        return sorted_list
