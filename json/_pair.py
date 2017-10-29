from custom.json_._string import String
from custom.json_._value import Value

class Pair:

    def __init__(self, consumer):
        self._key = String(consumer)
        consumer.consume_whitespace()
        consumer.consume_char(':')
        consumer.consume_whitespace()
        self._value = Value(consumer)

    def __str__(self):
        return str(self._key) + ':' + str(self._value)

    def __repr__(self):
        return self.__str__()

    @property
    def key(self):
        return self._key.value
    
    @property
    def value(self):
        return self._value.value
