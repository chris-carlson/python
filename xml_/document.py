from consumer.consumer import Consumer
from file_.read_file import ReadFile
from str_ import Str
from xml_._element import Element

class Document:

    def __init__(self, file_name):
        xml_file = ReadFile(file_name)
        parse_line = Str(xml_file.get_parse_line())
        parse_line = parse_line.remove_whitespace()
        consumer = Consumer(parse_line)
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        self._root = Element(consumer)

    def __str__(self):
        return str(self._root)

    def __repr__(self):
        return self.__str__()

    @property
    def root(self):
        return self._root
