from custom.consumer.consumer import Consumer
from custom.file_.read_file import ReadFile
from custom.str_ import Str
from custom.xml_._element import Element

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
        parse_line = Str(xml_file.get_parse_line())
        parse_line = parse_line.remove_whitespace()
        consumer = Consumer(parse_line)
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        self._root = Element(consumer)
