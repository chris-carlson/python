from custom.selenium.by import By

from selenium.webdriver.common.keys import Keys


class Element:

    def __init__(self, element):
        self._rep = element

    @property
    def name(self):
        return self._rep.tag_name

    @property
    def text(self):
        return self._rep.text

    def has_element(self, by, search):
        return len(self.find_elements(by, search)) > 0

    def find_element(self, by, search):
        results = self.find_elements(by, search)
        if len(results) > 1:
            raise ValueError('Found ' + str(len(results)) + ' elements for search \'' + search + '\'')
        elif len(results) == 0:
            raise ValueError('Found no elements for search \'' + search + '\'')
        return results[0]

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

    def has_class(self, klass):
        return klass in self.get_classes()

    def get_classes(self):
        return [klass for klass in self._rep.get_attribute('class').split(' ') if len(klass) > 0]

    @staticmethod
    def _get_elements(results):
        return [Element(result) for result in results]
