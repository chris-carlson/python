from custom.json._value import Value

class Array:

    def __init__(self):
        self._elements = []

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
    def elements(self):
        return self._elements

    def parse(self, consumer):
        consumer.consume_char('[')
        consumer.consume_whitespace()
        while consumer.peek() != ']':
            value = Value()
            value.parse(consumer)
            self._elements.append(value.value)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
        consumer.consume_char(']')
