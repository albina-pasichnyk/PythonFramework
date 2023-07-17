import pytest

from page_objects.connections_page import ConnectionsPage
from page_objects.login_page import LoginPage
from utilities.config_reader import ReadConfig
from utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_app_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def login_to_app(open_login_page):
    return open_login_page.login(ReadConfig.get_user_creds())


@pytest.fixture()
def go_to_connections_page(open_login_page, create_driver):
    open_login_page.login(ReadConfig.get_user_creds())
    return ConnectionsPage(create_driver)


@pytest.fixture()
def go_to_notifications_page(login_to_app):
    return login_to_app.go_to_notifications_page()


@pytest.fixture()
def trigger_user_creation(go_to_notifications_page):
    return go_to_notifications_page.trigger_create_user()


@pytest.fixture()
def go_to_license_page(login_to_app):
    return login_to_app.go_to_license_details_page()
