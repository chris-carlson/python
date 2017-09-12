import os

from selenium import webdriver
from custom.selenium.element import Element

class Driver:

    def __init__(self):
        chromedriver_path = os.environ['CHROMEDRIVER']
        self._rep = webdriver.Chrome(chromedriver_path)

    def navigate(self, url):
        self._rep.get(url)

    def has_element(self, by, search):
        root = Element(self._rep.find_element_by_tag_name('html'))
        return root.has_element(by, search)

    def find_element(self, by, search):
        root = Element(self._rep.find_element_by_tag_name('html'))
        return root.find_element(by, search)

    def find_elements(self, by, search):
        root = Element(self._rep.find_element_by_tag_name('html'))
        return root.find_elements(by, search)

    def quit(self):
        self._rep.quit()
