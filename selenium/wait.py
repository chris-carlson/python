from cac.selenium.by import By
from cac.selenium.element import Element
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By as SeleniumBy
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Wait:

    def __init__(self, driver: WebDriver, time: int) -> None:
        self._rep: WebDriverWait = WebDriverWait(driver, time)

    def wait_for_element(self, package_by: By, search: str) -> Element:
        selenium_by: SeleniumBy = By.convert(package_by)
        selenium_element: WebElement = self._rep.until(
                expected_conditions.visibility_of_element_located((selenium_by, search)))
        return Element(selenium_element)
