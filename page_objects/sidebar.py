from page_objects.license_details_page import LicenseDetailsPage
from page_objects.notifications_page import NotificationsPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class SideBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.XPATH, "//*[@class='sc-ifAKCX sc-sdtwF lGUCz']")
    __logout_button = (By.XPATH, "//span[@aria-label='Logout']")
    __notifications_sidebar_item = (By.XPATH, "//div/b[contains(text(), 'Notifications')]")
    __license_details_sidebar_item = (By.XPATH, "//div/b[contains(text(), 'License Details')]")
    __github_link = (By.XPATH, "//*[@class='sc-dyGzUR cbOCWZ']")
    __sidebar_area = (By.XPATH, "//nav")
    __collapse_button = (By.XPATH, "//*[@data-icon='arrow-circle-left']")
    __expand_button = (By.XPATH, "//*[@data-icon='arrow-circle-right']")

    def is_logout_present(self):
        return self.is_displayed(self.__logout_button)

    def click_logout(self):
        self.click(self.__logout_button)
        return self

    def is_login_present(self):
        return self.is_displayed(self.__login_button)

    def go_to_notifications_page(self):
        self.click(self.__notifications_sidebar_item)
        return NotificationsPage(self._driver)

    def get_github_link(self):
        self.is_displayed(self.__github_link)
        return self.get_link_value(self.__github_link)

    def hover_sidebar(self):
        self.hover_the_element(self.__sidebar_area)
        return self

    def is_collapse_button_shown(self):
        self.hover_the_element(self.__sidebar_area)
        self.is_displayed(self.__collapse_button)
        return self

    def collapse_sidebar(self):
        self.is_displayed(self.__collapse_button)
        self.click(self.__collapse_button)
        return self

    def is_expand_button_shown(self):
        self.hover_the_element(self.__sidebar_area)
        self.is_displayed(self.__expand_button)
        return self

    def expand_sidebar(self):
        self.is_displayed(self.__expand_button)
        self.click(self.__expand_button)
        return self

    def go_to_license_details_page(self):
        self.click(self.__license_details_sidebar_item)
        return LicenseDetailsPage(self._driver)
