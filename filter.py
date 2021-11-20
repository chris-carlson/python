from typing import List, TypeVar

from regex import Regex

E = TypeVar('E')


class Filter:

    @staticmethod
    def filter_duplicates(item_list: List[E]) -> List[E]:
        return list(set(item_list))

    @staticmethod
    def find_shared_items(list_1: List[E], list_2: List[E]) -> List[E]:
        return [item for item in list_1 if item in list_2]

    @staticmethod
    def find_matching_lines(string_list: List[str], regex: Regex) -> List[str]:
        return [string for string in string_list if regex.matches(string)]
