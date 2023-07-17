from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator: tuple, value, is_clear=True):
        element = self.__wait_until_element_visible(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator: tuple):
        self.__wait_until_element_clickable(locator).click()

    def is_displayed(self, locator: tuple):
        return self.__wait.until(EC.presence_of_element_located(locator)).is_displayed

    def get_link_value(self, locator: tuple):
        if self.is_displayed(locator):
            link_text = self._driver.find_element(locator[0], locator[1])
            return link_text.get_attribute('href')
        else:
            return ''

    def hover_the_element(self, locator: tuple):
        actions = ActionChains(self._driver)
        self.__wait_until_element_visible(locator)
        element_to_hover = self.__wait_until_element_visible(locator)
        actions.move_to_element(element_to_hover).perform()

    def get_text(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element.text
