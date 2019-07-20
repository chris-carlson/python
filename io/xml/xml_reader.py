import xml.etree.ElementTree as ET

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree

from cac.io.xml.xml_element import XmlElement

class XmlReader:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_root(self) -> XmlElement:
        tree: ElementTree = ET.parse(self._file_name)
        return self._convert_element(tree.getroot())

    def _convert_element(self, native_element: Element) -> XmlElement:
        wrapper_element: XmlElement = XmlElement(native_element.tag, native_element.attrib)
        wrapper_element.text = native_element.text
        for child in list(native_element):
            wrapper_element.children.append(self._convert_element(child))
        return wrapper_element
