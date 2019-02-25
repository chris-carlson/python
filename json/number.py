class Number:

    @staticmethod
    def _is_float(value):
        return '.' in value or 'e' in value or 'E' in value

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def parse(self, consumer):
        value = consumer.consume_to_one_of([',', '}', ']']).strip()
        if self._is_float(value):
            self._value = float(value)
        else:
            self._value = int(value)
