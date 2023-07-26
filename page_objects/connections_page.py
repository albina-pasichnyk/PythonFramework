import allure

from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ConnectionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __invoke_dropdown_button = (By.XPATH, "//*[@role='dropDown']")
    __deactivate_action_item = (By.XPATH, "//*[contains(text(), 'Deactivate')]")
    __activate_action_item = (By.XPATH, "//*[contains(text(), 'Activate')]")
    __connection_status = (By.XPATH, "//div[@class='sc-fyjhYU UaqNw']")
    __accept_invitation_button = (By.XPATH, "//*[contains(text(), 'Accept invitation')]")
    __accept_invitation_modal_dialog = (By.XPATH, "//*[@class='sc-bwzfXH jjqluN']")
    __description_of_modal_dialog = (By.XPATH, "//*[@class='sc-htpNat jfFyHc']")
    __textarea_label = (By.XPATH, "//*[@class='sc-bZQynM zymJo']")
    __invitation_code_field = (By.XPATH, "//textarea")
    __next_button = (By.XPATH, "//*[contains(text(), 'Next')]")
    __invalid_code_pop_up = (By.XPATH, "//*[@class='sc-hwwEjo dNeRxR']")
    __invalid_code_pop_up_title = (By.XPATH, "//*[contains(text(), 'Invitation code is invalid')]")
    __invalid_code_pop_up_content = (By.XPATH, "//*[contains(text(), 'Invitation code is invalid')]/parent::node()/div")
    __documentation_link = (By.XPATH, "//*[contains(text(), 'Documentation')]")
    __eula_link = (By.XPATH, "//*[contains(text(), 'EULA')]")
    __report_a_bug_link = (By.XPATH, "//*[contains(text(), 'Report a bug')]")
    __support_link = (By.XPATH, "//div/a[contains(text(), 'Support')]")
    __support_page_header = (By.XPATH, "//div/h1")

    @allure.step
    def deactivate_connection(self):
        self.click(self.__invoke_dropdown_button)
        self.click(self.__deactivate_action_item)
        return self

    @allure.step
    def activate_connection(self):
        self.click(self.__invoke_dropdown_button)
        self.click(self.__activate_action_item)
        return self

    @allure.step
    def get_connection_status(self):
        return self.get_text(self.__connection_status)

    @allure.step
    def invoke_accept_code_dialog_shown(self):
        self.click(self.__accept_invitation_button)
        return self
        # self.is_displayed(self.__accept_invitation_modal_dialog)

    @allure.step
    def set_invitation_code(self, invitation_code):
        self.send_keys(self.__invitation_code_field, invitation_code)
        return self

    @allure.step
    def click_next_button(self):
        self.click(self.__next_button)
        return self

    @allure.step
    def get_invalid_code_pop_up_info(self):
        return (self.is_displayed(self.__invalid_code_pop_up), self.get_text(self.__invalid_code_pop_up_title),
                self.get_text(self.__invalid_code_pop_up_content))

    @allure.step
    def get_description(self):
        return self.get_text(self.__description_of_modal_dialog)

    @allure.step
    def get_textarea_label(self):
        return self.get_text(self.__textarea_label)

    @allure.step
    def get_documentation_link(self):
        return self.get_link_value(self.__documentation_link)

    @allure.step
    def get_eula_link(self):
        return self.get_link_value(self.__eula_link)

    @allure.step
    def get_report_a_bug_link(self):
        return self.get_link_value(self.__report_a_bug_link)

    @allure.step
    def is_support_opened(self):
        self.click(self.__support_link)
        return self.is_displayed(self.__support_page_header)
