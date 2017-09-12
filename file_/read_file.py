from custom.list_.list_ import List
from custom.set_.multi_set import MultiSet
from custom.set_.ordered_set import OrderedSet
from custom.str_ import Str

class ReadFile:

    def __init__(self, file_name):
        self._file = open(file_name, 'r')
        self._lines = List()

    @property
    def lines(self):
        return self._lines

    def read_lines(self):
        for line in self._file:
            self._lines.append(Str(line))

    def get_parse_line(self):
        parse_line = ''
        for line in self._lines:
            parse_line += line
        return parse_line

    def get_stripped_lines(self):
        stripped_lines = List()
        for line in self._lines:
            stripped_lines.append(line.strip())
        return stripped_lines

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

    def get_filtered_lines(self, regex):
        return self.get_stripped_lines().filter_text(regex)
