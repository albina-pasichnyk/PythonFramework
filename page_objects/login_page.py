from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from page_objects.sidebar import SideBar
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_page_header = (By.XPATH, "//h1")
    __how_to_link = (By.XPATH, "//*[contains(text(), 'how to generate a personal access token.')]")
    __security_tooltip_icon = (By.XPATH, "//*[@data-icon='exclamation-circle']")
    __security_tooltip = (By.XPATH, "//div/span/a/parent::node()")
    __security_tooltip_link = (By.XPATH, "//*[contains(text(), 'Read more about security.')]")
    __token_input = (By.XPATH, "//input")
    __login_button = (By.XPATH, "//*[@class='sc-kpOJdX eHicQo']")
    __invalid_token_pop_up = (By.XPATH, "//*[@class='sc-htpNat jfFyHc']")
    __invalid_pop_up_title = (By.XPATH, "//div/h3/span")
    __invalid_pop_up_content = (By.XPATH, "//*[@class='sc-bxivhb gVoBLL']/span")
    __token_missing_pop_up = (By.XPATH, "//*[@class='sc-hwwEjo dNeRxR']")
    __token_missing_pop_up_title = (By.XPATH, "//*[@class='sc-htpNat jfFyHc']/span")
    __token_missing_pop_up_content = (By.XPATH, "//*[@class='sc-bxivhb gVoBLL']")

    def get_login_page_header(self):
        return self.get_text(self.__login_page_header)

    @allure.step
    def get_how_to_link(self):
        return self.get_link_value(self.__how_to_link)

    @allure.step
    def get_tooltip_content(self):
        self.hover_the_element(self.__security_tooltip_icon)
        return self.get_text(self.__security_tooltip)

    @allure.step
    def get_security_tooltip_link(self):
        return self.get_link_value(self.__security_tooltip_link)

    @allure.step
    def set_token(self, token_value):
        self.send_keys(self.__token_input, token_value)
        return self

    @allure.step
    def click_login(self):
        self.click(self.__login_button)
        return SideBar(self._driver)

    @allure.step
    def login(self, token_value):
        self.set_token(token_value).click_login()
        return SideBar(self._driver)

    @allure.step
    def get_missing_pop_up_info(self):
        return (self.is_displayed(self.__token_missing_pop_up), self.get_text(self.__token_missing_pop_up_title),
                self.get_text(self.__token_missing_pop_up_content))

    @allure.step
    def get_invalid_pop_up_info(self):
        return (self.is_displayed(self.__invalid_token_pop_up), self.get_text(self.__invalid_pop_up_title),
                self.get_text(self.__invalid_pop_up_content))
