from bs4.builder import LXMLTreeBuilder
from bs4.element import NavigableString, Tag
from cac.io.html.html_tag import HtmlTag
from cac.io.text.text_writer import TextWriter

BUILDER: LXMLTreeBuilder = LXMLTreeBuilder()


class HtmlWriter:

    def __init__(self, file_name: str) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, tag: HtmlTag) -> None:
        self._file.write_line(str(self._convert_element(tag)))

    def _convert_element(self, wrapper_element: HtmlTag, parent: Tag = None) -> Tag:
        native_element: Tag = Tag(name=wrapper_element.name, attrs=wrapper_element.attributes, parent=parent,
            previous=NavigableString('\n'), builder=BUILDER)
        for child in wrapper_element.children:
            native_element.contents.append(self._convert_element(child, native_element))
        if len(wrapper_element.text) > 0:
            native_element.contents = [NavigableString(wrapper_element.text)]
        return native_element

    def close(self) -> None:
        self._file.close()
