from typing import Tuple

from cac.io.text.text_writer import TextWriter
from cac.io.xml.xml_element import XmlElement
from lxml.etree import Element, QName, tostring


class XmlWriter:

    def __init__(self, file_name: str, pretty_print: bool = None) -> None:
        self._file: TextWriter = TextWriter(file_name)
        self._pretty_print: bool = pretty_print

    def write(self, element: XmlElement, namespace: Tuple[str, str] = None) -> None:
        self._file.write(
                tostring(self._convert_element(element, namespace), encoding='unicode', pretty_print=self._pretty_print))

    def _convert_element(self, wrapper_element: XmlElement, namespace: Tuple[str, str] = None) -> Element:
        native_element: Element = Element(wrapper_element.name, wrapper_element.attributes)
        if namespace is not None:
            native_element = Element(QName(namespace[1], wrapper_element.name), wrapper_element.attributes,
                    {namespace[0]: namespace[1]})
        native_element.text = wrapper_element.text
        for child in wrapper_element.children:
            native_element.append(self._convert_element(child, namespace))
        return native_element

    def close(self) -> None:
        self._file.close()
