from typing import Dict, List

from cac.io.text.text_reader import TextReader
from cac.io.xml.xml_element import XmlElement
from cac.string import String
from lxml import etree
from lxml.etree import Element, ElementTree


class XmlReader:

    @staticmethod
    def read_text(text: str) -> XmlElement:
        element: Element = etree.XML(text)
        return XmlReader._convert_element(element)

    @staticmethod
    def _convert_element(native_element: Element, parent: XmlElement = None) -> XmlElement:
        tag_name: str = XmlReader._get_tag_name(native_element)
        attributes: Dict[str, str] = XmlReader._get_attributes(native_element)
        wrapper_element: XmlElement = XmlElement(tag_name, attributes, parent=parent)
        if len(list(native_element)) == 0:
            wrapper_element.text = native_element.text
        for child in list(native_element):
            wrapper_element.children.append(XmlReader._convert_element(child, wrapper_element))
        return wrapper_element

    @staticmethod
    def _get_tag_name(native_element: Element) -> str:
        tag: String = String(native_element.tag)
        if tag.startswith('{'):
            for abbreviation, expansion in native_element.nsmap.items():
                if tag.startswith('{' + expansion + '}'):
                    return tag.substring_after('}')
        return tag

    @staticmethod
    def _get_attributes(native_element: Element) -> Dict[str, str]:
        return {name: value for name, value in native_element.attrib.items()}

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def is_empty(self) -> bool:
        reader: TextReader = TextReader(self._file_name)
        lines: List[str] = [line for line in reader.read_stripped_lines() if
                len(line) > 0 and not line.startswith('<?xml')]
        reader.close()
        return len(lines) == 0

    def read_root(self) -> XmlElement:
        tree: ElementTree = etree.parse(self._file_name)
        return XmlReader._convert_element(tree.getroot())
