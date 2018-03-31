from custom.collections.multi_set import MultiSet
from custom.collections.ordered_set import OrderedSet


class ReadFile:

    def __init__(self, file_name):
        self._file = open(file_name, 'r')
        self._lines = []

    @property
    def lines(self):
        return self._lines

    def read_lines(self):
        self._lines = [line for line in self._file]

    def get_parse_line(self):
        parse_line = ''.join(self._lines)
        parse_line = parse_line.replace('\t', '')
        parse_line = parse_line.replace('\r', '')
        parse_line = parse_line.replace('\n', '')
        return parse_line

    def get_stripped_lines(self):
        return [line.strip() for line in self._lines]

    def get_unique_lines(self):
        ordered_set = OrderedSet()
        for line in self.get_stripped_lines():
            ordered_set.add(line)
        return ordered_set

    def count_unique_lines(self):
        multi_set = MultiSet()
        for line in self.get_stripped_lines():
            multi_set.add(line)
        return multi_set

    def close(self):
        self._file.close()
