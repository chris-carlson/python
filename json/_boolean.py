class Boolean:

    TRUE = 'true'
    FALSE = 'false'

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def parse(self, consumer):
        value = consumer.consume_to_one_of([',', '}', ']']).strip()
        if value == self.TRUE:
            self._value = True
        elif value == self.FALSE:
            self._value = False
        else:
            raise ValueError('\'' + value + '\' is an invalid boolean value')
