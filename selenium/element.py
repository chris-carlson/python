from selenium.webdriver.common.keys import Keys

from custom.selenium.by import By

class Element:

    def __init__(self, element):
        self._rep = element

    @property
    def html(self):
        return self._rep.get_attribute('outerHTML')

    @property
    def tag_name(self):
        return self._rep.tag_name

    @property
    def text(self):
        return self._rep.text

    def has_element(self, by, search):
        return len(self.find_elements(by, search)) > 0

    def find_element(self, by, search):
        results = self.find_elements(by, search)
        if len(results) > 0:
            return results[0]
        else:
            return None

    def find_elements(self, by, search):
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

    @staticmethod
    def _get_elements(results):
        elements = []
        for result in results:
            elements.append(Element(result))
        return elements

    def click(self):
        if self._rep.tag_name == 'input':
            self._rep.send_keys(Keys.RETURN)
        else:
            self._rep.click()

    def clear_text(self):
        self._rep.clear()

    def enter_text(self, text):
        self._rep.send_keys(text)

    def get_attribute(self, attribute):
        return self._rep.get_attribute(attribute)
