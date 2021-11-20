from typing import Dict, List, Optional

from cac.finder import Finder


class XmlElement:

    def __init__(self, name: str, attributes: Dict[str, str] = None, children: List['XmlElement'] = None,
            parent: 'XmlElement' = None, text: str = '') -> None:
        self._name: str = name
        self._attributes: Dict[str, str] = attributes if attributes is not None else {}
        self._children: List[XmlElement] = children if children is not None else []
        self._parent: XmlElement = parent
        self._text: str = text

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self._name

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def parent(self) -> 'XmlElement':
        return self._parent

    @property
    def text(self) -> str:
        return self._text

    @property
    def path(self) -> List[str]:
        if self._parent is None:
            return [self._name]
        return self._parent.path + [self._name]

    @property
    def children(self) -> List['XmlElement']:
        return self._children

    @text.setter
    def text(self, text) -> None:
        self._text = text

    def can_get_child(self, name: str) -> bool:
        return len(self.get_all_by_name(name)) > 0

    def can_find_child(self, name: str) -> bool:
        return len(self.find_all_by_name(name)) > 0

    def get_one_by_name(self, name: str) -> 'XmlElement':
        return Finder.find_only(self.get_all_by_name(name))

    def get_one_by_text(self, text: str) -> 'XmlElement':
        return Finder.find_only(self.get_all_by_text(text))

    def get_one_by_attribute(self, name: str, value: str = None) -> 'XmlElement':
        return Finder.find_only(self.get_all_by_attribute(name, value))

    def get_all_by_name(self, name: str) -> List['XmlElement']:
        return [child for child in self._children if child.name == name]

    def get_all_by_text(self, text: str) -> List['XmlElement']:
        return [child for child in self._children if child.text == text]

    def get_all_by_attribute(self, name: str, value: str = None) -> List['XmlElement']:
        return [child for child in self._children if
                name in child.attributes and (value is None or child.attributes[name] == value)]

    def find_one_by_name(self, name: str) -> 'XmlElement':
        return Finder.find_only(self.find_all_by_name(name))

    def find_one_by_text(self, text: str) -> 'XmlElement':
        return Finder.find_only(self.find_all_by_text(text))

    def find_one_by_attribute(self, name: str, value: str = None) -> 'XmlElement':
        return Finder.find_only(self.find_all_by_attribute(name, value))

    def find_all_by_name(self, name: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_name(name)
        for child in self._children:
            matching_children.extend(child.find_all_by_name(name))
        return matching_children

    def find_all_by_text(self, text: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_text(text)
        for child in self._children:
            matching_children.extend(child.find_all_by_text(text))
        return matching_children

    def find_all_by_attribute(self, name: str, value: str = None) -> List['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_attribute(name, value)
        for child in self._children:
            matching_children.extend(child.find_all_by_attribute(name, value))
        return matching_children

    def get_optional_child(self, name: str) -> Optional['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_name(name)
        if len(matching_children) == 0:
            return None
        if len(matching_children) > 1:
            raise ValueError('Found multiple matching children')
        return matching_children[0]
