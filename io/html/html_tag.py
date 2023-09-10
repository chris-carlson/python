from typing import Dict, List

from bs4 import BeautifulSoup, Tag
from cac.finder import Finder
from cac.text import Text

SOUP: BeautifulSoup = BeautifulSoup()

# noinspection PyTypeChecker
def convert_attributes(native_attributes: Dict[str, object]) -> Dict[str, str]:
    wrapper_attributes: Dict[str, str] = {}
    for name, value in native_attributes.items():
        if type(value) == str:
            wrapper_attributes[name] = value
        elif type(value) == list:
            wrapper_attributes[name] = ' '.join(value)
    return wrapper_attributes

def create_tag(name: str, attributes: Dict[str, str] = None, children: List['HtmlTag'] = None,
        text: str = '') -> 'HtmlTag':
    attributes = attributes if attributes is not None else {}
    native_element: Tag = SOUP.new_tag(name, attrs=attributes)
    children = children if children is not None else []
    for child in children:
        native_element.append(convert_tag(child))
    if len(text) > 0:
        native_element.string = text
    return HtmlTag(native_element)

def convert_tag(wrapper_element: 'HtmlTag') -> Tag:
    native_element: Tag = SOUP.new_tag(wrapper_element.name, attrs=wrapper_element.attributes)
    for child in wrapper_element.children:
        native_element.append(convert_tag(child))
    if len(wrapper_element.text) > 0:
        native_element.string = wrapper_element.text
    return native_element

class HtmlTag:

    def __init__(self, rep: Tag) -> None:
        self._rep = rep

    def __str__(self) -> str:
        return self._rep.name

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self._rep.name

    @property
    def text(self) -> str:
        return Text(self._rep.text).remove_excessive_whitespace() if self._rep.text is not None else ''

    @property
    def attributes(self) -> Dict[str, str]:
        return convert_attributes(self._rep.attrs)

    @property
    def children(self) -> List['HtmlTag']:
        # noinspection PyTypeChecker
        return [HtmlTag(child) for child in self._rep.contents if type(child) == Tag]

    def has_child(self, selector: str) -> bool:
        matching_children: List[Tag] = self._rep.select(selector)
        return len(matching_children) > 0

    def get_classes(self) -> List[str]:
        if 'class' in self._rep.attrs:
            return self._rep.attrs['class'].split(' ')
        return []

    def find_child(self, selector: str) -> 'HtmlTag':
        matching_children: List[HtmlTag] = self.find_children(selector)
        return Finder.find_only(matching_children)

    def find_children(self, selector: str) -> List['HtmlTag']:
        return [HtmlTag(child) for child in self._rep.select(selector)]

    def find_optional(self, selector: str) -> 'HtmlTag | None':
        matching_children: List[HtmlTag] = self.find_children(selector)
        if len(matching_children) == 0:
            return None
        return Finder.find_only(matching_children)
