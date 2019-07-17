from cac.consumer import Consumer
from cac.io.text.text_reader import TextReader
from cac.xml.element import Element


class XmlDocument:

    def __init__(self, file_name: str) -> None:
        self._text_reader: TextReader = TextReader(file_name)
        self._root: Element = None

    @property
    def root(self) -> Element:
        assert self._root is not None, 'Document has not been parsed yet'
        return self._root

    def parse(self) -> Element:
        assert self._root is None, 'Document has already been parsed'
        self._text_reader.read_lines()
        consumer: Consumer = Consumer(self._text_reader.get_parse_line())
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        consumer.consume_whitespace()
        self._root = Element()
        self._root.parse(consumer)
        return self._root
