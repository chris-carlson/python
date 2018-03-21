from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from custom.selenium.by import By
from custom.selenium._element import Element

class Wait:

    def __init__(self, driver, time=10):
        self._rep = WebDriverWait(driver._rep, time)

    def find_element(self, package_by, search):
        selenium_by = By.convert(package_by)
        selenium_element = self._rep.until(expected_conditions.visibility_of_element_located((selenium_by, search)))
        return Element(selenium_element)

    def find_elements(self, package_by, search):
        selenium_by = By.convert(package_by)
        selenium_elements = self._rep.until(expected_conditions.visibility_of_all_elements_located((selenium_by, search)))
        return [Element(selenium_element) for selenium_element in selenium_elements]
