from custom.consumer import Consumer
from custom.io.text.read_file import ReadFile
from custom.json._array import Array
from custom.json._object import Object

class Document:

    def __init__(self, file_name):
        self._file = ReadFile(file_name)
        self._root = None

    @property
    def root(self):
        assert self._root != None, 'Document has not been parsed yet'
        return self._root

    def parse(self):
        assert self._root == None, 'Document has already been parsed'
        self._file.read_lines()
        parse_line = self._file.get_parse_line()
        consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        if consumer.peek() == '{':
            self._root = Object()
            self._root.parse(consumer)
        elif consumer.peek() == '[':
            self._root = Array()
            self._root.parse(consumer)
        else:
            raise ValueError('\"' + consumer.peek() + '\" is not a valid starting character')
