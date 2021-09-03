from typing import List

from cac.selenium.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class Element:

    def __init__(self, element: WebElement) -> None:
        self._rep: WebElement = element

    @property
    def name(self) -> str:
        return self._rep.tag_name

    @property
    def text(self) -> str:
        return self._rep.text

    @property
    def html(self) -> str:
        return self._rep.get_attribute('outerHTML')

    def has_element(self, by: By, search: str) -> bool:
        return len(self.find_elements(by, search)) > 0

    def find_element(self, by: By, search: str) -> 'Element':
        results: List[Element] = self.find_elements(by, search)
        if len(results) > 1:
            raise ValueError('Found ' + str(len(results)) + ' elements for search \'' + search + '\'')
        elif len(results) == 0:
            raise ValueError('Found no elements for search \'' + search + '\'')
        return results[0]

    def find_elements(self, by: By, search: str) -> List['Element']:
        if by == By.ID:
            return Element._get_elements(self._rep.find_elements_by_id(search))
        elif by == By.NAME:
            return Element._get_elements(self._rep.find_elements_by_name(search))
        elif by == By.XPATH:
            return Element._get_elements(self._rep.find_elements_by_xpath(search))
        elif by == By.LINK:
            return Element._get_elements(self._rep.find_elements_by_link_text(search))
        elif by == By.TAG:
            return Element._get_elements(self._rep.find_elements_by_tag_name(search))
        elif by == By.CLASS:
            return Element._get_elements(self._rep.find_elements_by_class_name(search))
        elif by == By.CSS:
            return Element._get_elements(self._rep.find_elements_by_css_selector(search))
        raise ValueError('Invalid by value \'' + str(by) + '\'')

    def click(self) -> None:
        if self._rep.tag_name == 'input':
            self._rep.send_keys(Keys.RETURN)
        else:
            self._rep.click()

    def clear_text(self) -> None:
        self._rep.clear()

    def enter_text(self, text: str) -> None:
        self._rep.send_keys(text)

    def select(self, value: str, text=False) -> None:
        dropdown: Select = Select(self._rep)
        if text:
            dropdown.select_by_visible_text(value)
        else:
            dropdown.select_by_value(value)

    def get_attribute(self, attribute: str) -> str:
        return self._rep.get_attribute(attribute)

    def has_class(self, css_class: str) -> bool:
        return css_class in self.get_classes()

    def get_classes(self) -> List[str]:
        return [css_class for css_class in self._rep.get_attribute('class').split(' ') if len(css_class) > 0]

    def get_options(self) -> List[str]:
        dropdown: Select = Select(self._rep)
        options: List[Element] = [Element(option) for option in dropdown.options]
        return [option.get_attribute('value') for option in options]

    @staticmethod
    def _get_elements(results: List[WebElement]):
        return [Element(result) for result in results]
