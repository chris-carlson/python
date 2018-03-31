from custom.consumer import Consumer
from custom.io.text.read_file import ReadFile
from custom.xml.element import Element


class Document:

    def __init__(self, file_name):
        self._file = ReadFile(file_name)
        self._root = None

    @property
    def root(self):
        assert self._root is not None, 'Document has not been parsed yet'
        return self._root

    def parse(self):
        assert self._root is None, 'Document has already been parsed'
        self._file.read_lines()
        parse_line = self._file.get_parse_line()
        consumer = Consumer(parse_line)
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        consumer.consume_whitespace()
        self._root = Element()
        self._root.parse(consumer)
