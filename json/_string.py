class String:

    def __init__(self, consumer):
        consumer.consume_char('\"')
        self._value = consumer.consume_to('\"')
        consumer.consume_char('\"')

    def __str__(self):
        return '\"' + str(self._value) + '\"'

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        return self._value
