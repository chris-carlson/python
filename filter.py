from typing import List, TypeVar

E = TypeVar('E')


class Filter:

    @staticmethod
    def filter_duplicates(item_list: List[E]) -> List[E]:
        return list(set(item_list))

    @staticmethod
    def find_shared_items(list_1: List[E], list_2: List[E]) -> List[E]:
        return [item for item in list_1 if item in list_2]
