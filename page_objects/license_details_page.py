from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class LicenseDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __license_header = (By.XPATH, "//h1[contains(text(), 'License Details')]")
    __delete_button = (By.XPATH, "//*[@type='danger-alt']")
    __cancel_delete_button = (By.XPATH, "//*[contains(text(),'Cancel')]")
    __remove_license_key_button = (By.XPATH, "//*[contains(text(),'Remove license key')]")
    __basic_mode_label = (By.XPATH, "//*[contains(text(),'basic mode')]")
    __type_value = (By.XPATH, "//label[contains(text(),'Type')]//following-sibling::*/div/label")
    __buy_license_button = (By.XPATH, "//div[contains(text(), 'BUY LICENSE')]")
    __go_to_directory_button = (By.XPATH, "//div[contains(text(), 'GO TO')]")
    __subscribe_dialog_header = (By.XPATH, "//h2[contains(text(),'Subscribe')]")

    def is_license_header_shown(self):
        return self.is_displayed(self.__license_header)

    def invoke_delete_license(self):
        self.click(self.__delete_button)
        return self

    def confirm_delete(self):
        self.click(self.__remove_license_key_button)
        return self

    def cancel_delete(self):
        self.click(self.__cancel_delete_button)
        return self

    def is_basic_mode_label_shown(self):
        return self.is_displayed(self.__basic_mode_label)

    def get_license_type(self):
        return self.get_text(self.__type_value)

    def is_buy_license_shown(self):
        return self.is_displayed(self.__buy_license_button)

    def is_go_to_directory_shown(self):
        return self.is_displayed(self.__go_to_directory_button)

    def is_buy_license_triggered(self):
        self.click(self.__buy_license_button)
        return self.is_displayed(self.__subscribe_dialog_header)
