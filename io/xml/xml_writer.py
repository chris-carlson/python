from typing import Tuple

from cac.io.text.text_writer import TextWriter
from cac.io.xml.xml_element import XmlElement
from lxml.etree import Element, QName, tostring

class XmlWriter:

    @staticmethod
    def to_string(element: XmlElement, pretty_print: bool = None, namespace: Tuple[str, str] = None) -> str:
        return tostring(XmlWriter._convert_element(element, namespace), encoding='unicode', pretty_print=pretty_print)

    @staticmethod
    def _convert_element(wrapper_element: XmlElement, namespace: Tuple[str, str] = None) -> Element:
        native_element: Element = Element(wrapper_element.name, wrapper_element.attributes)
        if namespace is not None:
            native_element = Element(QName(namespace[1], wrapper_element.name), wrapper_element.attributes,
                {namespace[0]: namespace[1]})
        native_element.text = wrapper_element.text
        for child in wrapper_element.children:
            native_element.append(XmlWriter._convert_element(child, namespace))
        return native_element

    def __init__(self, file_name: str) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, element: XmlElement, pretty_print: bool = None, namespace: Tuple[str, str] = None) -> None:
        self._file.write(XmlWriter.to_string(element, pretty_print, namespace))

    def close(self) -> None:
        self._file.close()
