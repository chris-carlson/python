from custom.json._pair import Pair

class Object:

    def __init__(self):
        self._pairs = {}

    def __contains__(self, key):
        for pair in self._pairs:
            if pair.key == key:
                return True
        return False

    def __iter__(self):
        for pair in self._pairs:
            yield pair

    def __getitem__(self, key):
        if not type(key) == str:
            raise TypeError('Key \'' + key + '\' must be of string type')
        for pair in self._pairs:
            if pair.key == key:
                return pair.value
        raise KeyError('Key \'' + key + '\' does not exist in the object')

    @property
    def pairs(self):
        return self._pairs

    def parse(self, consumer):
        consumer.consume_char('{')
        consumer.consume_whitespace()
        while consumer.peek() != '}':
            pair = Pair()
            pair.parse(consumer)
            self._pairs[pair.key] = pair.value
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
        consumer.consume_char('}')
