class String:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def parse(self, consumer):
        consumer.consume_char('\"')
        self._value = consumer.consume_to('\"')
        consumer.consume_char('\"')
