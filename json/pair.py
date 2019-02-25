from cac.json.string import String
from cac.json.value import Value


class Pair:

    def __init__(self) -> None:
        self._key = None
        self._value = None

    @property
    def key(self) -> None:
        return self._key.value

    @property
    def value(self) -> None:
        return self._value.value

    def parse(self, consumer) -> None:
        self._key = String()
        self._key.parse(consumer)
        consumer.consume_whitespace()
        consumer.consume_char(':')
        consumer.consume_whitespace()
        self._value = Value()
        self._value.parse(consumer)
