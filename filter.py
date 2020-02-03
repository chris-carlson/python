from typing import List, TypeVar

E = TypeVar('E')


class Filter:

    @staticmethod
    def filter_duplicates(item_list: List[E]) -> List[E]:
        return list(set(item_list))
