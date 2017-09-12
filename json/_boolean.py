TRUE = 'true'
FALSE = 'false'

class Boolean:

    def __init__(self, consumer):
        value = consumer.consume_to(',', '}', ']').strip()
        if value == TRUE:
            self._value = True
        elif value == FALSE:
            self._value = False
        else:
            raise ValueError('\'' + value + '\' is an invalid boolean value')

    def __str__(self):
        return str(self._value).lower()

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        return self._value
