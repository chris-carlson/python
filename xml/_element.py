from custom.xml_._attribute import Attribute

class Element:

    def __init__(self, consumer):
        consumer.consume_char('<')
        self._name = consumer.consume_to('>', ' ')
        self._attributes = []
        while consumer.peek() == ' ':
            consumer.consume_whitespace()
            attribute = Attribute(consumer)
            self._attributes.append(attribute)
        consumer.consume_char('>')
        consumer.consume_whitespace()
        self._children = []
        while consumer.peek() == '<' and not consumer.starts_with('</'):
            child = Element(consumer)
            self._children.append(child)
            consumer.consume_whitespace()
        self._body = consumer.consume_to('<')
        consumer.consume_char('<')
        consumer.consume_char('/')
        closing_tag_name = consumer.consume_to('>')
        assert closing_tag_name == self._name, 'Closing tag name ' + closing_tag_name + ' does not match opening tag name ' + self._name
        consumer.consume_char('>')
        consumer.consume_whitespace()

    def __str__(self):
        str_ = '<' + self._name
        for attribute in self._attributes:
            str_ += ' ' + str(attribute)
        str_ += '>'
        for child in self._children:
            str_ += str(child)
        str_ += self._body
        str_ += '</' + self._name + '>'
        return str_

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._name

    @property
    def body(self):
        return self._body

    def get_attribute(self, attribute_name):
        for attribute in self._attributes:
            if attribute.name == attribute_name:
                return attribute.value
        raise ValueError('Attribute ' + attribute_name + ' does not exist on this element')

    def get_child(self, child_name):
        for child in self._children:
            if child.name == child_name:
                return child
        raise ValueError('Child ' + child_name + ' does not exist on this element')

    def get_children(self, child_name):
        children = []
        for child in self._children:
            if child.name == child_name:
                children.append(child)
        return children
