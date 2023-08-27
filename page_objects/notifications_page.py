# import allure

from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class NotificationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __page_header = (By.XPATH, "//*[@class='sc-bdVaJa ljnUkc']")
    __tooltip_icon = (By.XPATH, "//*[@data-icon='exclamation-circle']")
    __tooltip_content = (By.XPATH, "//*[@role='tooltip']/div")
    __no_user_label = (By.XPATH, "//div/h2")
    __invoke_create_button = (By.XPATH, "//*[contains(text(),'Create')]")
    __cancel_button = (By.XPATH, "//*[contains(text(),'Cancel')]")
    __name_input = (By.XPATH, "//*[@name='name']")
    __email_input = (By.XPATH, "//*[@name='email']")
    __create_user_button = (By.XPATH, "//div[contains(text(),'Create')]")
    __created_user_name = (By.XPATH, "//*[@class='sc-ifAKCX fmUSpj break-all']")
    __created_user_email = (By.XPATH, "//*[@class='break-all']")
    __dots_menu = (By.XPATH, "//div/i")
    __delete_menu_item = (By.XPATH, "//*[contains(text(),'Delete')]")

    def is_page_header_present(self):
        return self.is_displayed(self.__page_header)

    # @allure.step
    def get_tooltip_content(self):
        self.hover_the_element(self.__tooltip_icon)
        return self.get_text(self.__tooltip_content)

    def is_default_label_displayed(self):
        return self.is_displayed(self.__no_user_label)

    def get_default_label(self):
        return self.get_text(self.__no_user_label)

    # @allure.step
    def trigger_create_user(self):
        self.click(self.__invoke_create_button)
        return self

    # @allure.step
    def cancel_creating_user(self):
        self.click(self.__cancel_button)
        return self

    # @allure.step
    def set_user_name(self, user_name_value):
        self.send_keys(self.__name_input, user_name_value)
        return self

    # @allure.step
    def set_user_email(self, user_email_value):
        self.send_keys(self.__email_input, user_email_value)
        return self

    # @allure.step
    def create_user(self):
        self.click(self.__create_user_button)
        return self

    def is_user_added(self):
        return self.is_displayed(self.__created_user_name) and self.is_displayed(self.__created_user_email)

    # @allure.step
    def delete_user(self):
        self.click(self.__dots_menu)
        self.click(self.__delete_menu_item)
        return self
