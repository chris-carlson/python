from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from cac.consumer import Consumer
from cac.io.text.read_file import ReadFile

E = TypeVar('E')


class Document(ABC, Generic[E]):

    def __init__(self, file_name: str) -> None:
        self._file: ReadFile = ReadFile(file_name)
        self._root: E = None

    @property
    def root(self) -> E:
        assert self._root is not None, 'Document has not been parsed yet'
        return self._root

    def parse(self) -> None:
        assert self._root is None, 'Document has already been parsed'
        self._file.read_lines()
        parse_line: str = self._file.get_parse_line()
        consumer: Consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        self._root = self._parse_value(consumer)

    @abstractmethod
    def _parse_value(self, consumer: Consumer) -> E:
        pass
