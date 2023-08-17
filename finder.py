from typing import List, Set, TypeVar

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

    @staticmethod
    def find_optional(filtered_list: List[E]) -> E:
        if len(filtered_list) == 0:
            return None
        if len(filtered_list) > 1:
            raise ValueError('Found multiple matches in the list')
        return filtered_list[0]

    @staticmethod
    def find_duplicates(item_list: List[E]) -> Set[E]:
        search_list: List[E] = item_list[:]
        encountered_items: Set[E] = set()
        duplicated_items: Set[E] = set()
        while len(search_list) > 0:
            item: E = search_list.pop(0)
            if item in encountered_items:
                duplicated_items.add(item)
            encountered_items.add(item)
        return duplicated_items
