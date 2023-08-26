from bs4 import Tag
from cac.io.html.html_tag import HtmlTag, convert_tag
from cac.io.text.text_writer import TextWriter

class HtmlWriter:

    def __init__(self, file_name: str) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, wrapper_tag: HtmlTag) -> None:
        native_tag: Tag = convert_tag(wrapper_tag)
        html: str = str(native_tag)
        self._file.write_line(html)

    def close(self) -> None:
        self._file.close()
