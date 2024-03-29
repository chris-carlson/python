from typing import List, Tuple

from cac.regex import Regex

WHITESPACE_REGEX: Regex = Regex(r'\s')

class Consumer:

    def __init__(self, rep: str) -> None:
        self._rep: str = rep

    def __str__(self) -> str:
        return self._rep

    def __repr__(self) -> str:
        return self._rep

    def __len__(self) -> int:
        return len(self._rep)

    def has_input(self) -> bool:
        return len(self._rep) > 0

    def starts_with(self, sequence: str) -> bool:
        return self._rep.startswith(sequence)

    def contains(self, sequence: str) -> bool:
        return sequence in self._rep

    def matches(self, regex: Regex) -> bool:
        return regex.matches(self._rep)

    def peek(self) -> str:
        assert self.has_input(), 'Consumer does not have any input left'
        return self._rep[0]

    def consume_char(self, char: str = None) -> str:
        assert self.has_input(), 'Consumer does not have any input left'
        if char is not None:
            assert self.peek() == char, 'Expected \'' + char + '\', got \'' + self.peek() + '\''
        return self._remove_char()

    def consume_one_of(self, chars: List[str]) -> str:
        if len(chars) > 0:
            assert self.peek() in chars, 'Expected one of ' + str(chars) + ', got \'' + self.peek() + '\''
        return self.consume_char()

    def consume_chars(self, chars: List[str]) -> str:
        consumed: str = ''
        for char in chars:
            consumed += self.consume_char(char)
        return consumed

    def consume_num_chars(self, num_chars: int) -> str:
        consumed: str = ''
        for _ in range(0, num_chars):
            consumed += self.consume_char()
        return consumed

    def consume_to(self, char: str, allow_escaped: bool = False) -> str:
        assert self.contains(char), 'Could not find \'' + char + '\''
        return self.consume_to_one_of([char], allow_escaped)

    def consume_to_one_of(self, chars: List[str], allow_escaped: bool = False) -> str:
        assert self._contains_one_of(chars), 'Could not find one of \'' + str(chars) + '\''
        consumed: str = ''
        is_escaped: bool = False
        while self.peek() not in chars or (is_escaped and not allow_escaped):
            is_escaped = self.peek() == '\\'
            consumed += self._remove_char()
        return consumed

    def consume_to_sequence(self, sequence: str) -> str:
        assert self.contains(sequence), 'Could not find \'' + sequence + '\''
        consumed: str = ''
        while not self.starts_with(sequence):
            consumed += self._remove_char()
        return consumed

    def consume_through(self, char: str) -> str:
        assert self.contains(char), 'Could not find \'' + char + '\''
        return self.consume_through_one_of([char])

    def consume_through_one_of(self, chars: List[str]) -> str:
        consumed: str = self.consume_to_one_of(chars)
        consumed += self.consume_char()
        return consumed

    def consume_through_sequence(self, sequence: str) -> str:
        consumed: str = self.consume_to_sequence(sequence)
        consumed += self._remove_chars(len(sequence))
        return consumed

    def consume_through_match(self, open_char: str, close_char: str = None) -> str:
        if close_char is None:
            close_char = open_char
        consumed: str = self.consume_char(open_char)
        balance: int = 1
        while balance != 0:
            char: str = self.consume_char()
            if char == open_char:
                balance += 1
            elif char == close_char:
                balance -= 1
            consumed += char
        return consumed

    def consume_whitespace(self) -> str:
        consumed: str = ''
        while self.has_input() and WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def consume_to_whitespace(self) -> str:
        consumed: str = ''
        while self.has_input() and not WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def consume_regex(self, regex: Regex) -> str:
        match_index: Tuple[str, int] = regex.find_match_index(self._rep)
        if match_index[1] != 0:
            raise ValueError('Consumer does not start with regex \'' + str(regex) + '\'')
        return self.consume_through_sequence(match_index[0])

    def consume_to_regex(self, regex: Regex) -> str:
        match_index: Tuple[str, int] = regex.find_match_index(self._rep)
        return self._remove_chars(match_index[1])

    def consume_through_regex(self, regex: Regex) -> str:
        match_index: Tuple[str, int] = regex.find_match_index(self._rep)
        return self._remove_chars(match_index[1] + len(match_index[0]))

    def consume_to_end(self) -> str:
        consumed: str = ''
        while self.has_input():
            consumed += self.consume_char()
        return consumed

    def _contains_one_of(self, chars: List[str]) -> bool:
        contains: bool = False
        for char in chars:
            if self.contains(char):
                contains = True
        return contains

    def _remove_char(self) -> str:
        return self._remove_chars(1)

    def _remove_chars(self, num_chars: int) -> str:
        consumed: str = self._rep[:num_chars]
        self._rep = self._rep[num_chars:]
        return consumed
