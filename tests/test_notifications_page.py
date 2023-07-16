import pytest

from page_objects.login_page import LoginPage
from page_objects.notifications_page import NotificationsPage
from utilities.config_reader import ReadConfig
from utilities.data_randomizer import generate_random_user_name, generate_random_user_email


def test_notification_tooltip(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    sidebar.go_to_notifications_page()
    expected_tooltip_content = 'Add users to receive email notifications about Exalate errors that block synchronization.'
    tooltip = NotificationsPage(driver).hover_tooltip()
    actual_tooltip_content = tooltip.get_tooltip_content()
    assert actual_tooltip_content == expected_tooltip_content, 'Incorrect tooltip'


def test_default_page_state(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    sidebar.go_to_notifications_page()
    expected_default_label = 'There are no users defined to receive Exalate error notifications.'
    actual_default_label = NotificationsPage(driver).get_default_label()
    assert actual_default_label == expected_default_label, 'Incorrect default label'


@pytest.mark.regression
def test_cancel_creating_user(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    sidebar.go_to_notifications_page()
    notifications_page = NotificationsPage(driver).trigger_create_user().cancel_creating_user()
    assert notifications_page.is_default_label_displayed(), 'No default label'


@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    sidebar.go_to_notifications_page()
    notifications_page = NotificationsPage(driver).trigger_create_user().set_user_name(
        generate_random_user_name()).set_user_email(generate_random_user_email()).create_user()
    assert notifications_page.check_user_added(), 'User is not created'


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    sidebar.go_to_notifications_page()
    notifications_page = NotificationsPage(driver).delete_user()
    assert notifications_page.is_default_label_displayed(), 'User is not deleted'
