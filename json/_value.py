from custom.regex import Regex

class Value:

    def __init__(self, consumer):
        number_regex = Regex(r'(-|[0-9])')
        boolean_regex = Regex(r'(t|f)')
        if consumer.peek() == '{':
            from json_._object import Object
            self._value = Object(consumer)
        elif consumer.peek() == '[':
            from json_._array import Array
            self._value = Array(consumer)
        elif consumer.peek() == '\"':
            from json_._string import String
            self._value = String(consumer)
        elif number_regex.matches(consumer.peek()):
            from json_._number import Number
            self._value = Number(consumer)
        elif boolean_regex.matches(consumer.peek()):
            from json_._boolean import Boolean
            self._value = Boolean(consumer)
        else:
            self._value = None

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        from json_._object import Object
        from json_._array import Array
        if type(self._value) == Object or type(self._value) == Array:
            return self._value
        else:
            return self._value.value
