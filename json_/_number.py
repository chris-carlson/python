class Number:

    def __init__(self, consumer):
        value = consumer.consume_to(',', '}', ']').strip()
        if '.' in value or 'e' in value or 'E' in value:
            self._value = float(value)
        else:
            self._value = int(value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        return self._value
