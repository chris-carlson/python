import xml.etree.ElementTree as ET

from typing import Dict, List
from xml.etree.ElementTree import Element

from cac.finder import Finder

class XmlElement:

    def __init__(self, tag: str, attributes: Dict[str, str] = {}) -> None:
        self._tag: str = tag
        self._attributes: Dict[str, str] = attributes
        self._text: str = ''
        self._children: List[XmlElement] = []

    def __str__(self) -> str:
        return self._tag

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def text(self) -> str:
        return self._text

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def children(self) -> List['XmlElement']:
        return self._children

    @text.setter
    def text(self, text) -> None:
        self._text = text

    def has_tag(self, tag: str) -> bool:
        matching_children: List[XmlElement] = self.get_all_by_tag(tag)
        return len(matching_children) > 0

    def get_one_by_tag(self, tag: str) -> 'XmlElement':
        matching_children: List[XmlElement] = self.get_all_by_tag(tag)
        return Finder.find_only(matching_children)

    def get_one_by_text(self, text: str) -> 'XmlElement':
        matching_children: List[XmlElement] = self.get_all_by_text(text)
        return Finder.find_only(matching_children)

    def get_all_by_tag(self, tag: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = []
        for child in self._children:
            if child.tag == tag:
                matching_children.append(child)
        return matching_children

    def get_all_by_text(self, text: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = []
        for child in self._children:
            if child.text == text:
                matching_children.append(child)
        return matching_children

    def find_one_by_tag(self, tag: str) -> 'XmlElement':
        matching_children: List[XmlElement] = self.find_all_by_tag(tag)
        return Finder.find_only(matching_children)

    def find_one_by_text(self, text: str) -> 'XmlElement':
        matching_children: List[XmlElement] = self.find_all_by_text(text)
        return Finder.find_only(matching_children)

    def find_all_by_tag(self, tag: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_tag(tag)
        for child in self._children:
            matching_children.extend(child.find_all_by_tag(tag))
        return matching_children

    def find_all_by_text(self, text: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = self.get_all_by_text(text)
        for child in self._children:
            matching_children.extend(child.find_all_by_text(text))
        return matching_children
