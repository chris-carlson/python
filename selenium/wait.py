from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from custom.selenium.by import By
from custom.selenium._element import Element

class Wait:

    def __init__(self, driver, time):
        self._rep = WebDriverWait(driver._rep, time)

    def until_visible(self, package_by, search):
        selenium_by = By.convert(package_by)
        return Element(self._rep.until(expected_conditions.visibility_of_element_located((selenium_by, search))))

    def until_clickable(self, package_by, search):
        selenium_by = By.convert(package_by)
        return Element(self._rep.until(expected_conditions.element_to_be_clickable((selenium_by, search))))
