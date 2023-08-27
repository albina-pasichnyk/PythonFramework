# import allure
import pytest


# @allure.feature('License Details Page')
@pytest.mark.regression
def test_cancel_deleting_license(go_to_license_page):
    license_page = go_to_license_page
    current_license = license_page.get_license_type()
    license_page.invoke_delete_license().cancel_delete()
    updated_license = license_page.get_license_type()
    assert updated_license == current_license, 'Delete not canceled. License is deleted'


# @allure.feature('License Details Page')
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_license(go_to_license_page):
    license_page = go_to_license_page
    current_license = license_page.get_license_type()
    license_page.invoke_delete_license().confirm_delete()
    assert license_page.is_basic_mode_label_shown(), 'No basic mode label'
    updated_license = license_page.get_license_type()
    assert updated_license != current_license, 'License is not deleted'


# @allure.feature('License Details Page')
@pytest.mark.regression
def test_buy_license_button(go_to_license_page):
    license_page = go_to_license_page
    expected_section_name = 'BUY LICENSE'
    actual_section_name = license_page.get_buy_license_content()
    assert license_page.is_buy_license_shown(), 'No Buy License section'
    assert license_page.is_basic_mode_label_shown(), 'Buy License section must be available only for Free plan'
    assert actual_section_name == expected_section_name, 'Incorrect section name'


# @allure.feature('License Details Page')
@pytest.mark.regression
def test_find_expert_section(go_to_license_page):
    license_page = go_to_license_page
    expected_section_name = 'GO TO DIRECTORY'
    actual_section_name = license_page.get_find_expert_content()
    assert license_page.is_go_to_directory_shown(), 'No Find Expert section'
    assert license_page.is_basic_mode_label_shown(), 'Find Export section must be available only for Free plan'
    assert actual_section_name == expected_section_name, 'Incorrect section name'


# @allure.feature('Exalate Subscription')
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_subscribe_dialog_default_state(go_to_license_page):
#     license_page = go_to_license_page
#     subscribe_dialog = license_page.invoke_subscribe_dialog()
#     # check dialog name
#     expected_dialog_name = 'Subscribe to Exalate'
#     actual_dialog_name = subscribe_dialog.get_subscribe_dialog_name()
#     assert actual_dialog_name == expected_dialog_name, 'Incorrect dialog name'
#     # check dialog description
#     expected_dialog_description = 'Please enter your organization information and then proceed to checkout. The ' \
#                                   'subscription will be activated once the payment is processed.'
#     actual_dialog_description = subscribe_dialog.get_subscribe_dialog_description()
#     assert actual_dialog_description == expected_dialog_description, 'Incorrect dialog description'
#     # check dialog input section label
#     expected_dialog_label = 'Organization Information'
#     actual_dialog_label = subscribe_dialog.get_subscribe_dialog_label()
#     assert actual_dialog_label == expected_dialog_label, 'Incorrect dialog label'
