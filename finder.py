from typing import List, TypeVar

E = TypeVar('E')


class Finder:

    @staticmethod
    def find(search_item: E, item_list: List[E]) -> E:
        filtered_list: List[E] = [item for item in item_list if item == search_item]
        return Finder.find_only(filtered_list)

    @staticmethod
    def find_first(item_list: List[E]) -> E:
        if len(item_list) == 0:
            raise ValueError('Found no items in the list')
        return item_list[0]

    @staticmethod
    def find_only(filtered_list: List[E]) -> E:
        if len(filtered_list) == 0:
            raise ValueError('Found no matches in the list')
        if len(filtered_list) > 1:
            raise ValueError('Found multiple matches in the list')
        return filtered_list[0]
