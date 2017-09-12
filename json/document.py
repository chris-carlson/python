from custom.consumer.consumer import Consumer
from custom.file_.read_file import ReadFile
from custom.json_._array import Array
from custom.json_._object import Object

class Document:

    def __init__(self, file_name):
        self._file = ReadFile(file_name)

    def __str__(self):
        return str(self._root)

    def __repr__(self):
        return self.__str__()

    @property
    def root(self):
        return self._root

    def parse_file(self):
        self._file.read_lines()
        parse_line = json_file.get_parse_line()
        consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        if consumer.peek() == '{':
            self._root = Object(consumer)
        elif consumer.peek() == '[':
            self._root = Array(consumer)
        else:
            raise ValueError('\"' + consumer.peek() + '\" is not a valid starting character')
