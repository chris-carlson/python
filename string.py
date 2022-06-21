import re
from typing import List, Tuple

from cac.consumer import Consumer
from cac.regex import Regex


class String(str):

    @staticmethod
    def pad_number(number: int, num_digits: int) -> str:
        string_number: str = str(number)
        while len(string_number) < num_digits:
            string_number = '0' + string_number
        return string_number

    def __init__(self, string: str = '') -> None:
        super().__init__()
        self._rep: str = string

    def __getitem__(self, key: int) -> 'String':
        return String(self._rep[key])

    def __add__(self, string: str) -> 'String':
        return String(self._rep + string)

    def find_indexes(self, char: str, invalid_preceding_char: str = '') -> List[int]:
        indexes: List[int] = []
        current_index: int = 0
        while current_index != -1:
            char_index: int = self._rep.find(char, current_index)
            if char_index != -1:
                if not self._preceded_by(invalid_preceding_char, char_index):
                    indexes.append(char_index)
                current_index = char_index + 1
            else:
                current_index = -1
        return indexes

    def substring_between(self, str1, str2, pair_num=1) -> 'String':
        indexes: Tuple = ()
        current_pair: int = 0
        start_index: int = 0
        while current_pair < pair_num:
            indexes = self._find_pair_indexes(str1, str2, start_index)
            current_pair += 1
            start_index = indexes[1] + 1
        return String(self._rep[indexes[0] + len(str1): indexes[1]].strip())

    def substring_to(self, substring: str) -> 'String':
        index: int = self._rep.find(substring)
        return String(self._rep[:index])

    def substring_to_last(self, substring: str) -> 'String':
        index: int = self._rep.rfind(substring)
        return String(self._rep[:index])

    def substring_through(self, substring: str) -> 'String':
        index: int = self._rep.find(substring)
        return String(self._rep[:index + len(substring)])

    def substring_from(self, substring: str) -> 'String':
        index: int = self._rep.find(substring)
        return String(self._rep[index:])

    def substring_after(self, substring: str) -> 'String':
        index: int = self._rep.find(substring)
        return String(self._rep[index + len(substring):])

    def substring_after_last(self, substring: str) -> 'String':
        index: int = self._rep.rfind(substring)
        return String(self._rep[index + len(substring):])

    def substring_after_occurrence(self, text: str, occurrence: int) -> 'String':
        indexes: List[int] = self.get_indexes(text)
        index: int = indexes[occurrence - 1] if occurrence >= 0 else indexes[occurrence]
        return String(self._rep[index + 1:])

    def get_indexes(self, char: str) -> List[int]:
        if len(char) != 1:
            raise ValueError('The string for indexes must be a character')
        indexes: List[int] = []
        for index in range(0, len(self._rep)):
            if self._rep[index] == char:
                indexes.append(index)
        return indexes

    def is_capitalized(self) -> bool:
        return self._rep[0] == self._rep[0].upper()

    def capitalize_first(self) -> 'String':
        return String(self._rep[0].upper() + self._rep[1:])

    def remove(self, sequence: str) -> 'String':
        string: str = self._rep
        while string.find(sequence) != -1:
            index: int = self._rep.find(sequence)
            string = string[:index] + string[index + len(sequence):]
        return String(string)

    def remove_whitespace(self) -> 'String':
        string: str = self._rep
        string = string.replace(' ', '')
        string = string.replace('\t', '')
        string = string.replace('\r', '')
        string = string.replace('\n', '')
        return String(string)

    def remove_excessive_whitespace(self) -> 'String':
        return String(re.sub(r'\s{2,}', ' ', self._rep))

    def insert_text(self, index: int, text: str) -> 'String':
        return String(self._rep[:index] + text + self._rep[index:])

    def insert_text_before(self, char: str, text: str) -> 'String':
        index: int = self._rep.find(char)
        return self.insert_text(index, text)

    def insert_text_after(self, char: str, text: str) -> 'String':
        index: int = self._rep.find(char) + 1
        return self.insert_text(index, text)

    def replace_completely(self, regex: Regex, text: str) -> 'String':
        string: str = self._rep
        while regex.matches(string):
            match_index: Tuple[str, int] = regex.find_match_index(string)
            match: str = match_index[0]
            index: int = match_index[1]
            string = string[:index] + text + string[index + len(match):]
        return String(string)

    def split_sections(self, regex: Regex, include_separator: bool = True) -> List[str]:
        match_indexes: List[int] = [match_index[1] for match_index in regex.find_match_indexes(self._rep)]
        section_indexes: List[Tuple[int, int]] = [
                (match_indexes[index], match_indexes[index + 1]) if index < len(match_indexes) - 1 else (
                        match_indexes[index], len(self._rep)) for index in range(0, len(match_indexes))]
        sections: List[str] = []
        for start_index, end_index in section_indexes:
            consumer: Consumer = Consumer(self._rep[start_index:end_index])
            if not include_separator:
                consumer.consume_through_regex(regex)
            sections.append(consumer.consume_to_end())
        return sections

    def _find_pair_indexes(self, str1: str, str2: str, index: int = 0) -> Tuple[int, int]:
        index1: int = self._rep.find(str1, index)
        index2: int = self._rep.find(str2, index1 + 1)
        if index1 == -1 or index2 == -1:
            raise ValueError(
                    'Could not find a pair of (\'' + str1 + '\', \'' + str2 + '\') in string starting at index ' + str(
                            index))
        return index1, index2

    def _preceded_by(self, char: str, index: int) -> bool:
        if index == -1 or index == 0:
            return False
        return self._rep[index - 1] == char
