from custom.regex import Regex

class Value:

    NUMBER_REGEX = Regex('(-|[0-9])')
    BOOLEAN_REGEX = Regex('(t|f)')

    def __init__(self):
        self._value = None

    @property
    def value(self):
        from custom.json._object import Object
        from custom.json._array import Array
        if type(self._value) == Object or type(self._value) == Array:
            return self._value
        else:
            return self._value.value

    def parse(self, consumer):
        if consumer.peek() == '{':
            from custom.json._object import Object
            self._value = Object()
            self._value.parse(consumer)
        elif consumer.peek() == '[':
            from custom.json._array import Array
            self._value = Array()
            self._value.parse(consumer)
        elif consumer.peek() == '\"':
            from custom.json._string import String
            self._value = String()
            self._value.parse(consumer)
        elif self.NUMBER_REGEX.matches(consumer.peek()):
            from custom.json._number import Number
            self._value = Number()
            self._value.parse(consumer)
        elif self.BOOLEAN_REGEX.matches(consumer.peek()):
            from custom.json._boolean import Boolean
            self._value = Boolean()
            self._value.parse(consumer)
        else:
            self._value = None
