import os

from selenium import webdriver
from custom.selenium._element import Element

class Driver:

    def __init__(self, headless=False):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('headless')
            chrome_options.add_argument('disable-gpu')
        self._rep = webdriver.Chrome(os.environ['CHROMEDRIVER'], chrome_options=chrome_options)

    def navigate(self, url):
        self._rep.get(url)

    def has_element(self, by, search):
        return self._get_root().has_element(by, search)

    def find_element(self, by, search):
        return self._get_root().find_element(by, search)

    def find_elements(self, by, search):
        return self._get_root().find_elements(by, search)

    def quit(self):
        self._rep.quit()

    def _get_root(self):
        return Element(self._rep.find_element_by_tag_name('html'))
