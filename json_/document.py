from consumer.consumer import Consumer
from file_.read_file import ReadFile
from json_._array import Array
from json_._object import Object

class Document:

    def __init__(self, file_name):
        json_file = ReadFile(file_name)
        parse_line = json_file.get_parse_line()
        consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        if consumer.peek() == '{':
            self._root = Object(consumer)
        elif consumer.peek() == '[':
            self._root = Array(consumer)
        else:
            raise ValueError('\"' + consumer.peek() + '\" is not a valid starting character')

    def __str__(self):
        return str(self._root)

    def __repr__(self):
        return self.__str__()

    @property
    def root(self):
        return self._root
