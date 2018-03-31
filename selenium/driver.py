import os
from custom.selenium.element import Element
from custom.selenium.wait import Wait

from selenium import webdriver


class Driver:

    def __init__(self, headless=False, wait_time=10):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('headless')
            chrome_options.add_argument('disable-gpu')
        self._rep = webdriver.Chrome(os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
        self._wait = Wait(self._rep, wait_time)

    def navigate(self, url):
        self._rep.get(url)

    def has_element(self, by, search):
        return self._get_root().has_element(by, search)

    def wait_for_element(self, by, search):
        return self._wait.wait_for_element(by, search)

    def find_element(self, by, search):
        return self._get_root().find_element(by, search)

    def find_elements(self, by, search):
        return self._get_root().find_elements(by, search)

    def quit(self):
        self._rep.quit()

    def _get_root(self):
        return Element(self._rep.find_element_by_tag_name('html'))
