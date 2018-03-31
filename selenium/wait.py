from custom.selenium.element import Element
from custom.selenium.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Wait:

    def __init__(self, driver, time):
        self._rep = WebDriverWait(driver, time)

    def wait_for_element(self, package_by, search):
        selenium_by = By.convert(package_by)
        selenium_element = self._rep.until(expected_conditions.visibility_of_element_located((selenium_by, search)))
        return Element(selenium_element)
