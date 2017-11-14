from custom.json._array import Array
from custom.json._boolean import Boolean
from custom.json._number import Number
from custom.json._object import Object
from custom.json._string import String
from custom.regex import Regex

class Value:

    NUMBER_REGEX = Regex('(-|[0-9])')
    BOOLEAN_REGEX = Regex('(t|f)')

    def __init__(self):
        self._value = None

    @property
    def value(self):
        if type(self._value) == Object or type(self._value) == Array:
            return self._value
        else:
            return self._value.value

    def parse(self, consumer):
        if consumer.peek() == '{':
            self._value = Object(consumer)
        elif consumer.peek() == '[':
            self._value = Array(consumer)
        elif consumer.peek() == '\"':
            self._value = String(consumer)
        elif self.NUMBER_REGEX.matches(consumer.peek()):
            self._value = Number(consumer)
        elif self.BOOLEAN_REGEX.matches(consumer.peek()):
            self._value = Boolean(consumer)
        else:
            self._value = None
