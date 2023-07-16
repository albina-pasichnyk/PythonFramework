import pytest

from page_objects.login_page import LoginPage
from page_objects.license_details_page import LicenseDetailsPage
from utilities.config_reader import ReadConfig


@pytest.mark.regression
def test_cancel_deleting_license(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    license_page = sidebar.go_to_license_details_page()
    current_license = license_page.get_license_type()
    license_page.invoke_delete_license().cancel_delete()
    updated_license = license_page.get_license_type()
    assert updated_license == current_license, 'Delete not canceled. License is deleted'


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_license(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    license_page = sidebar.go_to_license_details_page()
    current_license = license_page.get_license_type()
    license_page.invoke_delete_license().confirm_delete()
    assert license_page.is_basic_mode_label_shown(), 'No basic mode label'
    updated_license = license_page.get_license_type()
    assert updated_license != current_license, 'License is not deleted'


@pytest.mark.regression
def test_buy_license_button(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    license_page = sidebar.go_to_license_details_page()
    assert license_page.is_buy_license_shown(), 'No Buy License section'
    assert license_page.is_basic_mode_label_shown(), 'Buy License section must be available only for Free plan'


@pytest.mark.regression
def test_find_expert_section(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    license_page = sidebar.go_to_license_details_page()
    assert license_page.is_go_to_directory_shown(), 'No Find Expert section'
    assert license_page.is_basic_mode_label_shown(), 'Find Export section must be available only for Free plan'


@pytest.mark.smoke
@pytest.mark.regression
def test_trigger_buy_license(create_driver):
    # login to be moved out
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()

    license_page = sidebar.go_to_license_details_page()
    assert license_page.trigger_buy_license(), 'Subsribe to Exalate dialog is not opened'
