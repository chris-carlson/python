import xml.etree.ElementTree as ET

from typing import Dict, List
from xml.etree.ElementTree import Element

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

    def find_by_tag(self, tag: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = []
        for child in self._children:
            if child.tag == tag:
                matching_children.append(child)
            matching_children.extend(child.find_by_tag(tag))
        return matching_children

    def find_by_text(self, text: str) -> List['XmlElement']:
        matching_children: List[XmlElement] = []
        for child in self._children:
            if child.text == text:
                matching_children.append(child)
            matching_children.extend(child.find_by_text(text))
        return matching_children
