from lxml import etree
from lxml.etree import Element
from lxml.etree import ElementTree

from cac.io.text.text_reader import TextReader
from cac.io.xml.xml_element import XmlElement
from cac.string import String

class XmlReader:

    @staticmethod
    def read_text(text: str) -> XmlElement:
        element: Element = etree.XML(text)
        return self._convert_element(element)

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def is_empty(self) -> bool:
        reader: TextReader = TextReader(self._file_name)
        lines: List[str] = [line for line in reader.read_stripped_lines() if len(line) > 0 and not line.startswith('<?xml')]
        return len(lines) == 0

    def read_root(self) -> XmlElement:
        tree: ElementTree = etree.parse(self._file_name)
        return self._convert_element(tree.getroot())

    def _convert_element(self, native_element: Element) -> XmlElement:
        tag_name: str = self._get_tag_name(native_element)
        wrapper_element: XmlElement = XmlElement(tag_name, native_element.attrib)
        if len(list(native_element)) == 0:
            wrapper_element.text = native_element.text
        for child in list(native_element):
            wrapper_element.children.append(self._convert_element(child))
        return wrapper_element

    def _get_tag_name(self, native_element: Element) -> str:
        tag: String = String(native_element.tag)
        if tag.startswith('{'):
            for abbreviation, expansion in native_element.nsmap.items():
                if tag.startswith('{' + expansion + '}'):
                    if abbreviation is None:
                        return tag.substring_after('}')
                    else:
                        return abbreviation + ':' + tag.substring_after('}')
        return tag
