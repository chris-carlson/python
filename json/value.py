from typing import TypeVar, Generic

from cac.regex import Regex
from consumer import Consumer

E = TypeVar('E')


class Value(Generic[E]):
    NUMBER_REGEX: Regex = Regex('(-|[0-9])')
    BOOLEAN_REGEX: Regex = Regex('(t|f)')

    def __init__(self) -> None:
        self._value: E = None

    @property
    def value(self) -> E:
        return self._value

    def parse(self, consumer: Consumer) -> None:
        if consumer.peek() == '{':
            from cac.json.object import Object
            json_object = Object()
            json_object.parse(consumer)
            self._value = json_object.pairs
        elif consumer.peek() == '[':
            from cac.json.array import Array
            array = Array()
            array.parse(consumer)
            self._value = array.elements
        elif consumer.peek() == '\"':
            from cac.json.string import String
            string = String()
            string.parse(consumer)
            self._value = string.value
        elif self.NUMBER_REGEX.matches(consumer.peek()):
            from cac.json.number import Number
            number = Number()
            number.parse(consumer)
            self._value = number.value
        elif self.BOOLEAN_REGEX.matches(consumer.peek()):
            from cac.json.boolean import Boolean
            boolean = Boolean()
            boolean.parse(consumer)
            self._value = boolean.value
        else:
            self._value = None
