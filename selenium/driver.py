from typing import List

from cac.selenium.by import By
from cac.selenium.element import Element
from cac.selenium.wait import Wait
from selenium import webdriver
from selenium.webdriver.common.by import By as SeleniumBy

class Driver:

    def __init__(self, headless: bool = False, wait_time: int = 10) -> None:
        chrome_options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('headless')
            chrome_options.add_argument('disable-gpu')
        self._rep: webdriver.Chrome = webdriver.Chrome(chrome_options=chrome_options)
        self._wait: Wait = Wait(self._rep, wait_time)

    @property
    def source(self) -> str:
        return self._rep.page_source

    def navigate(self, url: str) -> None:
        self._rep.get(url)

    def has_element(self, by: By, search: str) -> bool:
        return self._get_root().has_element(by, search)

    def wait_for_element(self, by: By, search: str) -> Element:
        return self._wait.wait_for_element(by, search)

    def find_element(self, by: By, search: str) -> Element:
        return self._get_root().find_element(by, search)

    def find_elements(self, by: By, search: str) -> List[Element]:
        return self._get_root().find_elements(by, search)

    def quit(self) -> None:
        self._rep.quit()

    def _get_root(self) -> Element:
        return Element(self._rep.find_element(SeleniumBy.TAG_NAME, 'html'))
