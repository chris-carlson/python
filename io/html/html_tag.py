from typing import Dict, List

from cac.finder import Finder


class HtmlTag:

    def __init__(self, name: str, attributes: Dict[str, str] = None, children: List['HtmlTag'] = None, text: str = '') -> None:
        self._name: str = name
        self._attributes: Dict[str, str] = attributes if attributes is not None else {}
        self._children: List[HtmlTag] = children if children is not None else []
        self._text: str = text

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self._name

    @property
    def text(self) -> str:
        return self._text

    @property
    def attributes(self) -> Dict[str, str]:
        return self._attributes

    @property
    def children(self) -> List['HtmlTag']:
        return self._children

    @text.setter
    def text(self, text) -> None:
        self._text = text

    def can_get_child(self, name: str) -> bool:
        return len(self.get_all_by_name(name)) > 0

    def can_find_child(self, name: str) -> bool:
        return len(self.find_all_by_name(name)) > 0

    def get_classes(self) -> List[str]:
        if 'class' in self._attributes:
            return self._attributes['class'].split(' ')
        return []

    def get_by_id(self, id_name: str) -> 'HtmlTag':
        return Finder.find_only(
                [child for child in self._children if 'id' in child.attributes and child.attributes['id'] == id_name])

    def get_one_by_name(self, name: str) -> 'HtmlTag':
        return Finder.find_only(self.get_all_by_name(name))

    def get_one_by_text(self, text: str) -> 'HtmlTag':
        return Finder.find_only(self.get_all_by_text(text))

    def get_one_by_class(self, class_name: str) -> 'HtmlTag':
        return Finder.find_only(self.get_all_by_class(class_name))

    def get_all_by_name(self, name: str) -> List['HtmlTag']:
        return [child for child in self._children if child.name == name]

    def get_all_by_text(self, text: str) -> List['HtmlTag']:
        return [child for child in self._children if child.text == text]

    def get_all_by_class(self, class_name: str) -> List['HtmlTag']:
        return [child for child in self._children if class_name in child.get_classes()]

    def find_by_id(self, id_name: str) -> 'HtmlTag':
        return Finder.find_only(self._find_all_by_id(id_name))

    def _find_all_by_id(self, id_name: str) -> List['HtmlTag']:
        matching_children: List[HtmlTag] = [child for child in self._children if
                'id' in child.attributes and child.attributes['id'] == id_name]
        for child in self._children:
            matching_children.extend(child._find_all_by_id(id_name))
        return matching_children

    def find_one_by_name(self, name: str) -> 'HtmlTag':
        return Finder.find_only(self.find_all_by_name(name))

    def find_one_by_text(self, text: str) -> 'HtmlTag':
        return Finder.find_only(self.find_all_by_text(text))

    def find_one_by_class(self, class_name: str) -> 'HtmlTag':
        return Finder.find_only(self.find_all_by_class(class_name))

    def find_all_by_name(self, name: str) -> List['HtmlTag']:
        matching_children: List[HtmlTag] = self.get_all_by_name(name)
        for child in self._children:
            matching_children.extend(child.find_all_by_name(name))
        return matching_children

    def find_all_by_text(self, text: str) -> List['HtmlTag']:
        matching_children: List[HtmlTag] = self.get_all_by_text(text)
        for child in self._children:
            matching_children.extend(child.find_all_by_text(text))
        return matching_children

    def find_all_by_class(self, class_name: str) -> List['HtmlTag']:
        matching_children: List[HtmlTag] = self.get_all_by_class(class_name)
        for child in self._children:
            matching_children.extend(child.find_all_by_class(class_name))
        return matching_children
