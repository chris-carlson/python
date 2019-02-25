from cac.consumer import Consumer
from cac.xml.element import Element


class Document:

    def __init__(self, text: str) -> None:
        self._text: str = text
        self._root: Element = None

    @property
    def root(self) -> Element:
        assert self._root is not None, 'Document has not been parsed yet'
        return self._root

    def parse(self) -> None:
        assert self._root is None, 'Document has already been parsed'
        consumer: Consumer = Consumer(self._text)
        if consumer.starts_with('<?'):
            consumer.consume_through('>')
        consumer.consume_whitespace()
        self._root = Element()
        self._root.parse(consumer)
