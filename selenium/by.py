from selenium.webdriver.common.by import By as SeleniumBy

class By:

    ID = 0
    NAME = 1
    XPATH = 2
    LINK = 3
    TAG = 4
    CLASS = 5
    CSS = 6

    @staticmethod
    def convert(package_by):
        if package_by == By.ID:
            return SeleniumBy.ID
        elif package_by == By.NAME:
            return SeleniumBy.NAME
        elif package_by == By.XPATH:
            return SeleniumBy.XPATH
        elif package_by == By.LINK:
            return SeleniumBy.LINK_TEXT
        elif package_by == By.TAG:
            return SeleniumBy.TAG_NAME
        elif package_by == By.CLASS:
            return SeleniumBy.CLASS_NAME
        elif package_by == By.CSS:
            return SeleniumBy.CSS_SELECTOR
        raise ValueError('Invalid by value \'' + str(package_by) + '\'')
