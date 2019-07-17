from typing import Dict, List

from cac.consumer import Consumer


class XmlElement:

    def __init__(self) -> None:
        self._name: str = ''
        self._attributes: Dict[str, str] = {}
        self._children: List[Element] = []
        self._data: str = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def children(self) -> List['Element']:
        return self._children

    @property
    def data(self) -> str:
        assert self._data is not None
        return self._data

    def find_child_by_name(self, name: str) -> 'Element':
        filtered_items: List[Element] = self.filter_children_by_name(name)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with name \'' + name + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with name \'' + name + '\'')
        return filtered_items[0]

    def find_children_by_name(self, name: str) -> List['Element']:
        return [item for item in self._children if item.name == name]

    def find_child_by_attribute(self, name: str, value: str) -> 'Element':
        filtered_items: List[Element] = self.filter_children_by_attribute(name, value)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with attribute \'' + name + '\' and value \'' + value + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with attribute \'' + name + '\' and value \'' + value + '\'')
        return filtered_items[0]

    def find_children_by_attribute(self, name: str, value: str) -> List['Element']:
        return [item for item in self._children if name in item.attributes and item.attributes[name] == value]

    def find_child_by_data(self, data: str) -> 'Element':
        filtered_items: List[Element] = self.filter_children_by_data(data)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with data \'' + data + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with data \'' + data + '\'')
        return filtered_items[0]

    def find_children_by_data(self, data: str) -> List['Element']:
        return [item for item in self._children if item.data == data]

    def parse(self, consumer: Consumer) -> None:
        consumer.consume_char('<')
        self._name = consumer.consume_to_one_of(['>', ' ', '/'])
        while consumer.peek() != '/' and consumer.peek() != '>':
            consumer.consume_whitespace()
            attribute_name: str = consumer.consume_to('=')
            consumer.consume_char('=')
            consumer.consume_one_of(['\'', '\"'])
            attribute_value: str = consumer.consume_to_one_of(['\'', '\"'])
            attribute_value = attribute_value.replace('&amp;', '&')
            consumer.consume_one_of(['\'', '\"'])
            self._attributes[attribute_name] = attribute_value
            consumer.consume_whitespace()
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
                    consumer.consume_whitespace()
            else:
                self._data = consumer.consume_to('<')
            consumer.consume_char('<')
            consumer.consume_char('/')
            closing_tag_name: str = consumer.consume_to('>')
            assert closing_tag_name == self._name
            consumer.consume_char('>')
            consumer.consume_whitespace()
