from typing import Dict

from bs4 import BeautifulSoup
from bs4.element import Tag
from cac.io.html.html_tag import HtmlTag


# noinspection PyTypeChecker
def _convert_attributes(native_attributes: Dict[str, object]) -> Dict[str, str]:
    wrapper_attributes: Dict[str, str] = {}
    for name, value in native_attributes.items():
        if type(value) == str:
            wrapper_attributes[name] = value
        elif type(value) == list:
            wrapper_attributes[name] = ' '.join(value)
        else:
            raise ValueError('Unexpected attribute type \'' + str(type(value)) + '\'')
    return wrapper_attributes


class HtmlReader:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_root(self) -> HtmlTag:
        soup: BeautifulSoup = BeautifulSoup(open(self._file_name), features='lxml')
        return self._convert_element(soup.find('html'))

    def _convert_element(self, native_element: Tag) -> HtmlTag:
        wrapper_attributes: Dict[str, str] = _convert_attributes(native_element.attrs)
        wrapper_element: HtmlTag = HtmlTag(native_element.name, wrapper_attributes)
        for child in native_element.contents:
            if type(child) == Tag:
                wrapper_element.children.append(self._convert_element(child))
        if len(wrapper_element.children) == 0:
            wrapper_element.text = native_element.text
        return wrapper_element
