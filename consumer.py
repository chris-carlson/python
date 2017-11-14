from custom.regex import Regex

class Consumer:

    WHITESPACE_REGEX = Regex('\s')

    def __init__(self, rep):
        self._rep = rep

    def has_input(self):
        return len(self._rep) > 0

    def starts_with(self, sequence):
        return self._rep.startswith(sequence)

    def contains(self, sequence):
        return self._rep.find(sequence) != -1

    def peek(self):
        assert len(self._rep) > 0, 'Consumer does not have any input left'
        return self._rep[0]

    def consume_char(self, check_char=None):
        if check_char != None:
            assert self.peek() == check_char, 'Expected ' + check_char + ', got \'' + self.peek() + '\''
        return self.consume_chars(1)

    def consume_one_of(self, check_chars):
        if len(check_chars) > 0:
            assert self.peek() in check_chars, 'Expected one of ' + str(check_chars) + ', got \'' + self.peek() + '\''
        return self.consume_chars(1)

    def consume_chars(self, num):
        assert num <= len(self._rep), 'Expected to consume ' + str(num) + ' chars, only found ' + str(len(self._rep)) + ' chars'
        consumed = ''
        for i in range(0, num):
            consumed += self._rep[i]
        self._rep = self._rep[num:]
        return consumed

    def consume_to(self, char):
        assert self.contains(char), 'Could not find \'' + char + '\''
        return self.consume_to_one_of([char])

    def consume_to_one_of(self, chars):
        assert self._contains_one_of(chars), 'Could not find one of \'' + str(chars) + '\''
        consumed = ''
        while self._rep[0] not in chars:
            consumed += self._rep[0]
            self._remove_char()
        return consumed

    def consume_to_sequence(self, sequence):
        assert self.contains(sequence), 'Could not find \'' + sequence + '\''
        consumed = ''
        while not self.starts_with(sequence):
            consumed += self._rep[0]
            self._remove_char()
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
        consumed += self.consume_chars(len(sequence))
        return consumed

    def consume_whitespace(self):
        consumed = ''
        while self.has_input() and self.WHITESPACE_REGEX.matches(self.peek()):
            consumed += self.consume_char()
        return consumed

    def consume_to_whitespace(self):
        consumed = ''
        while self.has_input() and not self.WHITESPACE_REGEX.matches(self.peek()):
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
        self._rep = self._rep[1:]
