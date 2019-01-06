from custom.regex import Regex

WHITESPACE_REGEX = Regex(r'\s')


class Consumer:

    def __init__(self, rep):
        self._rep = rep

    def __str__(self):
        return self._rep

    def __repr__(self):
        return self._rep

    def has_input(self):
        return len(self._rep) > 0

    def starts_with(self, sequence):
        return self._rep.startswith(sequence)

    def contains(self, sequence):
        return self._rep.find(sequence) != -1

    def peek(self):
        assert self.has_input(), 'Consumer does not have any input left'
        return self._rep[0]

    def matches(self, regex):
        return regex.matches(self._rep)

    def consume_char(self, char=None):
        assert self.has_input(), 'Consumer does not have any input left'
        if char is not None:
            assert self.peek() == char, 'Expected \'' + char + '\', got \'' + self.peek() + '\''
        return self._remove_char()

    def consume_one_of(self, chars):
        if len(chars) > 0:
            assert self.peek() in chars, 'Expected one of ' + str(chars) + ', got \'' + self.peek() + '\''
        return self.consume_char()

    def consume_chars(self, chars):
        consumed = ''
        for char in chars:
            consumed += self.consume_char(char)
        return consumed

    def consume_to(self, char):
        assert self.contains(char), 'Could not find \'' + char + '\''
        return self.consume_to_one_of([char])

    def consume_to_one_of(self, chars):
        assert self._contains_one_of(chars), 'Could not find one of \'' + str(chars) + '\''
        consumed = ''
        while self.peek() not in chars:
            consumed += self._remove_char()
        return consumed

    def consume_to_sequence(self, sequence):
        assert self.contains(sequence), 'Could not find \'' + sequence + '\''
        consumed = ''
        while not self.starts_with(sequence):
            consumed += self._remove_char()
        return consumed

    def consume_through(self, char):
        assert self.contains(char), 'Could not find \'' + char + '\''
        return self.consume_through_one_of([char])

    def consume_through_one_of(self, chars):
        consumed = self.consume_to_one_of(chars)
        consumed += self.consume_char()
        return consumed

    def consume_through_sequence(self, sequence):
        consumed = self.consume_to_sequence(sequence)
        consumed += self._remove_chars(len(sequence))
        return consumed

    def consume_whitespace(self):
        consumed = ''
        while self.has_input() and WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def consume_to_whitespace(self):
        consumed = ''
        while self.has_input() and not WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def consume_to_end(self):
        consumed = ''
        while self.has_input():
            consumed += self.consume_char()
        return consumed

    def _contains_one_of(self, chars):
        contains = False
        for char in chars:
            if self.contains(char):
                contains = True
        return contains

    def _remove_char(self):
        return self._remove_chars(1)

    def _remove_chars(self, num_chars):
        consumed = self._rep[:num_chars]
        self._rep = self._rep[num_chars:]
        return consumed
