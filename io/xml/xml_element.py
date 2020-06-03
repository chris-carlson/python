from typing import Dict, List

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from cac.finder import Finder

class XmlElement:

    def __init__(self, name: str, attributes: Dict[str, str] = {}, parent: 'XmlElement' = None, text: str = '') -> None:
        self._name: str = name
        self._attributes: Dict[str, str] = attributes
        self._parent: type = parent
        self._text: str = text
        self._children: List[XmlElement] = []

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
        return [child for child in self._children if name in child.attributes and (value == None or child.attributes[name] == value)]

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
