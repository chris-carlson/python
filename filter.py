from typing import List, TypeVar

E = TypeVar('E')


class Filter:

    @staticmethod
    def filter_duplicates(item_list: List[E]) -> List[E]:
        filtered_list: List[E] = []
        for item in item_list:
            if item not in filtered_list:
                filtered_list.append(item)
        return filtered_list
