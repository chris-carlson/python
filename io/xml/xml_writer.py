import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from cac.io.text.text_writer import TextWriter
from cac.io.xml.xml_element import XmlElement


class XmlWriter:

    def __init__(self, file_name: str) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, element: XmlElement) -> None:
        self._file.write_line(ET.tostring(self._convert_element(element), 'unicode'))

    def _convert_element(self, wrapper_element: XmlElement) -> Element:
        native_element: Element = Element(wrapper_element.name, wrapper_element.attributes)
        native_element.text = wrapper_element.text
        for child in wrapper_element.children:
            native_element.append(self._convert_element(child))
        return native_element

    def close(self) -> None:
        self._file.close()
