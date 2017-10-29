from custom.dict_.ordered_dict import OrderedDict
from custom.list_.list_ import List
from custom.json_._pair import Pair

class Object:

    def __init__(self, consumer):
        self._pairs = List()
        consumer.consume_char('{')
        consumer.consume_whitespace()
        while consumer.peek() != '}':
            pair = Pair(consumer)
            self._pairs.append(pair)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
        consumer.consume_char('}')

    def __str__(self):
        return '{' + self._pairs.to_string() + '}'

    def __repr__(self):
        return self.__str__()

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
    def value(self):
        return self._pairs
