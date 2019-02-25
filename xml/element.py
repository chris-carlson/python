from typing import Dict, List

from cac.xml.element_list import ElementList
from consumer import Consumer


class Element:

    def __init__(self) -> None:
        self._name: str = ''
        self._attributes: Dict[str, str] = {}
        self._children: ElementList = ElementList()
        self._data: str = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def children(self) -> List['Element']:
        assert self._data is None, 'Element \'' + self._name + '\' has no children'
        return self._children

    @property
    def data(self) -> str:
        assert self._data is not None, 'Element \'' + self._name + '\' has no data'
        return self._data

    def parse(self, consumer: Consumer) -> None:
        consumer.consume_char('<')
        self._name = consumer.consume_to_one_of(['>', ' ', '/'])
        while consumer.peek() == ' ':
            consumer.consume_whitespace()
            attribute_name: str = consumer.consume_to('=')
            consumer.consume_char('=')
            consumer.consume_one_of(['\'', '\"'])
            attribute_value: str = consumer.consume_to_one_of(['\'', '\"'])
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
                    child: Element = Element()
                    child.parse(consumer)
                    self._children.append(child)
            else:
                self._data = consumer.consume_to('<')
            consumer.consume_char('<')
            consumer.consume_char('/')
            closing_tag_name: str = consumer.consume_to('>')
            assert closing_tag_name == self._name, 'Closing tag name \'' + closing_tag_name + '\' does not match ' \
                                                                                              'opening tag name \'' + \
                                                   self._name + '\''
            consumer.consume_char('>')
            consumer.consume_whitespace()
