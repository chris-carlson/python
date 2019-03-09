from cac.consumer import Consumer
from cac.io.text.read_file import ReadFile
from cac.xml.element import Element


class Document:

    def __init__(self, file_name: str) -> None:
        self._read_file: ReadFile = ReadFile(file_name)
        self._root: Element = None

    @property
    def root(self) -> Element:
        assert self._root is not None, 'Document has not been parsed yet'
        return self._root

    def parse(self) -> Element:
        assert self._root is None, 'Document has already been parsed'
        self._read_file.read_lines()
        consumer: Consumer = Consumer(self._read_file.get_parse_line())
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        consumer.consume_whitespace()
        self._root = Element()
        self._root.parse(consumer)
        return self._root
