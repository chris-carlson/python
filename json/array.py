from typing import TypeVar, Generic, List

from cac.json.value import Value
from consumer import Consumer

E = TypeVar('E')


class Array(Generic[E]):

    def __init__(self) -> None:
        self._elements: List[E] = []

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self) -> E:
        for element in self._elements:
            yield element

    def __getitem__(self, index: int) -> E:
        if not type(index) == int:
            raise TypeError('Index \'' + str(index) + '\' must be of integer type')
        if index < 0:
            raise IndexError('Index \'' + str(index) + '\' must be positive')
        if index >= len(self._elements):
            raise IndexError('Index \'' + str(index) + '\' must be less than the length of the array')
        return self._elements[index].value

    @property
    def elements(self) -> List[E]:
        return self._elements

    def parse(self, consumer: Consumer) -> None:
        consumer.consume_char('[')
        consumer.consume_whitespace()
        while consumer.peek() != ']':
            value: Value = Value()
            value.parse(consumer)
            self._elements.append(value.value)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
        consumer.consume_char(']')
