from custom.regex import Regex

class Value:

    NUMBER_REGEX = Regex('(-|[0-9])')
    BOOLEAN_REGEX = Regex('(t|f)')

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def parse(self, consumer):
        if consumer.peek() == '{':
            from custom.json._object import Object
            object_ = Object()
            object_.parse(consumer)
            self._value = object_.pairs
        elif consumer.peek() == '[':
            from custom.json._array import Array
            array = Array()
            array.parse(consumer)
            self._value = array.elements
        elif consumer.peek() == '\"':
            from custom.json._string import String
            string = String()
            string.parse(consumer)
            self._value = string.value
        elif self.NUMBER_REGEX.matches(consumer.peek()):
            from custom.json._number import Number
            number = Number()
            number.parse(consumer)
            self._value = number.value
        elif self.BOOLEAN_REGEX.matches(consumer.peek()):
            from custom.json._boolean import Boolean
            boolean = Boolean()
            boolean.parse(consumer)
            self._value = boolean.value
        else:
            self._value = None
