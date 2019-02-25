class Number:

    @staticmethod
    def _is_float(value):
        return '.' in value or 'e' in value or 'E' in value

    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> None:
        return self._value

    def parse(self, consumer) -> None:
        value = consumer.consume_to_one_of([',', '}', ']']).strip()
        if self._is_float(value):
            self._value = float(value)
        else:
            self._value = int(value)
