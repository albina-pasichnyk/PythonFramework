import pytest
from page_objects.login_page import LoginPage
from utilities.config_reader import ReadConfig
from utilities.data_randomizer import generate_random_token


def test_how_to_link(create_driver):
    driver = create_driver
    how_to_link_expected = 'https://docs.exalate.com/docs/how-to-generate-a-personal-access-token-in-github'
    how_to_link_actual = LoginPage(driver).get_how_to_link()
    assert how_to_link_expected == how_to_link_actual, 'Incorrect "how to generate a personal access token" link'


@pytest.mark.regression
def test_security_tooltip(create_driver):
    driver = create_driver
    # tooltip content
    tooltip_content_expected = 'Exalate is not storing any credential information - Read more about security.'
    tooltip = LoginPage(driver).hover_security_tooltip()
    tooltip_content_actual = tooltip.get_tooltip_content()
    assert tooltip_content_actual == tooltip_content_expected, 'Incorrect tooltip content'
    # tooltip link
    tooltip_security_link_expected = 'https://docs.exalate.com/docs/data-security-and-privacy-statement'
    tooltip_security_link_actual = LoginPage(driver).get_security_tooltip_link()
    assert tooltip_security_link_actual == tooltip_security_link_expected, 'Incorrect "Read more about security" link'


@pytest.mark.smoke
@pytest.mark.regression
def test_login(create_driver):
    token = ReadConfig.get_user_creds()
    driver = create_driver
    sidebar = LoginPage(driver).set_token(token).click_login()
    assert sidebar.is_logout_present(), 'Logout button is not present'


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('token,pop_up_title,pop_up_content', [
    (generate_random_token(), 'Invalid token', 'Please check if the token is correct.'),
    ('', 'Token is missing', 'Token field cannot be empty.')]
                         )
def test_invalid_login(create_driver, token, pop_up_title, pop_up_content):
    driver = create_driver
    # error token pop up
    token_pop_up = LoginPage(driver).set_token(token)
    token_pop_up.click_login()
    if token == '':
        popup_info = token_pop_up.get_missing_pop_up_info()
    else:
        popup_info = token_pop_up.get_invalid_pop_up_info()
    # check shown pop up
    assert popup_info[0], 'Pop up is not shown'
    # pop up title
    assert popup_info[1] == pop_up_title, 'Incorrect pop up title'
    # pop up content
    assert popup_info[2] == pop_up_content, 'Incorrect pop up content'
