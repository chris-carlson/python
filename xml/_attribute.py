class Attribute:

    def __init__(self, consumer):
        self._name = consumer.consume_to('=')
        consumer.consume_char('=')
        consumer.consume_char('\'', '\"')
        self._value = consumer.consume_to('\'', '\"')
        consumer.consume_char('\'', '\"')

    def __str__(self):
        return self._name + '=\"' + self._value + '\"'

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value
