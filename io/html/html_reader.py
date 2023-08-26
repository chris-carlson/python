from typing import TextIO

from bs4 import BeautifulSoup
from bs4.element import Tag
from cac.io.html.html_tag import HtmlTag

def read_root(soup: BeautifulSoup) -> HtmlTag:
    # noinspection PyTypeChecker
    root: Tag = soup.html
    return HtmlTag(root)

class HtmlReader:

    @staticmethod
    def read_text(text: str) -> HtmlTag:
        soup: BeautifulSoup = BeautifulSoup(text, features='html.parser')
        return read_root(soup)

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_root(self) -> HtmlTag:
        file: TextIO = open(self._file_name)
        soup: BeautifulSoup = BeautifulSoup(file, features='html.parser')
        return read_root(soup)
