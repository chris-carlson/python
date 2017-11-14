from custom.json._string import String
from custom.json._value import Value

class Pair:

    def __init__(self):
        self._key = None
        self._value = None

    @property
    def key(self):
        return self._key.value

    @property
    def value(self):
        return self._value.value

    def parse(self, consumer):
        self._key = String()
        self._key.parse(consumer)
        consumer.consume_whitespace()
        consumer.consume_char(':')
        consumer.consume_whitespace()
        self._value = Value()
        self._value.parse(consumer)
