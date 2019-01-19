from cac.xml.element_list import ElementList


class Element:

    def __init__(self):
        self._name = ''
        self._attributes = {}
        self._children = ElementList()
        self._data = None

    @property
    def name(self):
        return self._name

    @property
    def attributes(self):
        return self._attributes

    @property
    def children(self):
        assert self._data is None, 'Element \'' + self._name + '\' has no children'
        return self._children

    @property
    def data(self):
        assert self._data is not None, 'Element \'' + self._name + '\' has no data'
        return self._data

    def parse(self, consumer):
        consumer.consume_char('<')
        self._name = consumer.consume_to_one_of(['>', ' ', '/'])
        while consumer.peek() == ' ':
            consumer.consume_whitespace()
            attribute_name = consumer.consume_to('=')
            consumer.consume_char('=')
            consumer.consume_one_of(['\'', '\"'])
            attribute_value = consumer.consume_to_one_of(['\'', '\"'])
            consumer.consume_one_of(['\'', '\"'])
            self._attributes[attribute_name] = attribute_value
        if consumer.peek() == '/':
            consumer.consume_char('/')
            consumer.consume_char('>')
            self._data = ''
        else:
            consumer.consume_char('>')
            consumer.consume_whitespace()
            if consumer.peek() == '<':
                while consumer.peek() == '<' and not consumer.starts_with('</'):
                    child = Element()
                    child.parse(consumer)
                    self._children.append(child)
            else:
                self._data = consumer.consume_to('<')
            consumer.consume_char('<')
            consumer.consume_char('/')
            closing_tag_name = consumer.consume_to('>')
            assert closing_tag_name == self._name, 'Closing tag name \'' + closing_tag_name + '\' does not match ' \
                                                                                              'opening tag name \'' + \
                                                   self._name + '\''
            consumer.consume_char('>')
            consumer.consume_whitespace()
