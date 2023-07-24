import json

import pytest

from api_collections.auth_api import AuthAPI
from api_collections.booking_api import BookingAPI
from api_collections.data_classes.booking_data import Booking
from constants import ROOT_DIR
from page_objects.connections_page import ConnectionsPage
from page_objects.login_page import LoginPage
from utilities.config_object import ConfigObject
from utilities.driver_factory import create_driver_factory


@pytest.fixture(scope='session', autouse=True)
def environment():
    # update absolute path to relative
    with open(f'{ROOT_DIR}/configurations/configuration.json') as file:
        file_data = file.read()
        json_data = json.loads(file_data)
        return ConfigObject(**json_data)


@pytest.fixture()
def create_driver(environment):
    driver = create_driver_factory(environment.browser_id)
    driver.maximize_window()
    driver.get(environment.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def login_to_app(open_login_page, environment):
    return open_login_page.login(environment.token)


@pytest.fixture()
def go_to_connections_page(open_login_page, create_driver, environment):
    open_login_page.login(environment.token)
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


@pytest.fixture()
def mock_booking(environment):
    mock_data = BookingAPI(environment).create_booking(Booking())
    booking_body = mock_data.json()['booking']
    booking_id = mock_data.json()['bookingid']
    booking = Booking(booking_id, **booking_body)
    return booking


@pytest.fixture()
def booking_api(environment):
    booking_api = BookingAPI(environment)
    return booking_api


@pytest.fixture()
def booking_auth_api(environment):
    booking_auth_api = BookingAPI(environment)
    booking_auth_api.setup_token(environment)
    return booking_auth_api
