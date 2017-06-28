from list_.list_ import List
from json_._value import Value

class Array:

    def __init__(self, consumer):
        self._elements = List()
        consumer.consume_char('[')
        consumer.consume_whitespace()
        while consumer.peek() != ']':
            value = Value(consumer)
            self._elements.append(value)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
        consumer.consume_char(']')

    def __str__(self):
        return '[' + self._elements.to_string() + ']'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        for element in self._elements:
            yield element.value

    def __getitem__(self, index):
        if not type(index) == int:
            raise TypeError('Index \'' + index + '\' must be of integer type')
        if index < 0:
            raise IndexError('Index \'' + index + '\' must be positive')
        if index >= len(self._elements):
            raise IndexError('Index \'' + index + '\' must be less than the length of the array')
        return self._elements[index].value

    @property
    def value(self):
        return self._elements
