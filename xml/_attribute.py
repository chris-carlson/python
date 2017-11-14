class Attribute:

    def __init__(self):
        self._name = None
        self._value = None

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def parse(self, consumer):
        self._name = consumer.consume_to('=')
        consumer.consume_char('=')
        consumer.consume_one_of(['\'', '\"'])
        self._value = consumer.consume_to_one_of(['\'', '\"'])
        consumer.consume_one_of(['\'', '\"'])
