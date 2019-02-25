class String:

    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> None:
        return self._value

    def parse(self, consumer) -> None:
        consumer.consume_char('\"')
        self._value = consumer.consume_to('\"')
        consumer.consume_char('\"')
