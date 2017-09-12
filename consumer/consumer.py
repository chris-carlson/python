from custom.consumer import _matcher
from custom.regex import Regex

WHITESPACE_REGEX = Regex(r'\s')

class Consumer:

    def __init__(self, rep):
        self._rep = rep

    def __str__(self):
        return self._rep

    def __repr__(self):
        return self.__str__()

    def consume_chars(self, num):
        assert num <= len(self._rep)
        consumed = ''
        for i in range(0, num):
            consumed += self._rep[i]
        self._rep = self._rep[num:]
        return consumed

    def consume_char(self, *check_chars):
        if len(check_chars) > 0:
            assert self.peek() in check_chars, 'Expected one of ' + str(check_chars) + ', got \'' + self.peek() + '\''
        return self.consume_chars(1)

    def consume_to(self, *chars):
        consumed = ''
        while self._rep[0] not in chars:
            consumed += self._rep[0]
            self._rep = self._rep[1:]
        return consumed

    def consume_through(self, *chars):
        consumed = self.consume_to(*chars)
        consumed += self.consume_char()
        return consumed

    def consume_through_match(self):
        consumed = _matcher.find_match(self._rep)
        self._rep = self._rep[len(consumed):]
        return consumed

    def consume_whitespace(self):
        consumed = ''
        while self.has_input() and WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def has_input(self):
        return len(self._rep) > 0

    def peek(self):
        return self._rep[0]

    def starts_with(self, str_):
        return self._rep.startswith(str_)

    def contains(self, str_):
        return self._rep.find(str_) != -1
