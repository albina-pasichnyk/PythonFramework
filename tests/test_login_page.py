from time import sleep

import allure
import pytest
from utilities.data_randomizer import generate_random_token


@allure.description('Test link "How to generate a personal token"')
@allure.feature('Login Page')
def test_how_to_link(open_login_page):
    login_page = open_login_page
    how_to_link_expected = 'https://docs.exalate.com/docs/how-to-generate-a-personal-access-token-in-github'
    how_to_link_actual = login_page.get_how_to_link()
    assert how_to_link_expected == how_to_link_actual, 'Incorrect "how to generate a personal access token" link'


@allure.description('Test tooltip and link "Read more about security"')
@allure.feature('Login Page')
@pytest.mark.regression
def test_security_tooltip(open_login_page):
    login_page = open_login_page
    # tooltip content
    # tooltip_content_expected = 'Exalate is not storing any credential information - Read more about security.'
    # tooltip_content_actual = login_page.get_tooltip_content()
    # assert tooltip_content_actual == tooltip_content_expected, 'Incorrect tooltip content'
    # tooltip link
    tooltip_security_link_expected = 'https://docs.exalate.com/docs/data-security-and-privacy-statement'
    tooltip_security_link_actual = login_page.get_security_tooltip_link()
    assert tooltip_security_link_actual == tooltip_security_link_expected, 'Incorrect "Read more about security" link'


@allure.feature('Login Page')
@pytest.mark.smoke
@pytest.mark.regression
def test_login(open_login_page, environment):
    token = environment.token
    login_page = open_login_page
    sidebar = login_page.login(token)
    assert sidebar.is_logout_present(), 'Logout button is not present'


@allure.feature('Login Page')
@allure.issue('https://link_to_jira_project.com', 'XLT-1 Incorrect pop up content on failed login')
@allure.severity('TRIVIAL')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('token,pop_up_title,pop_up_content', [
    (generate_random_token(), 'Invalid token', 'Please check if the token is correct.'),
    ('', 'Token is missing', 'Token field cannot be empty.')]
                         )
def test_invalid_login(open_login_page, token, pop_up_title, pop_up_content):
    login_page = open_login_page
    # error token pop up
    token_pop_up = open_login_page.set_token(token)
    token_pop_up.click_login()
    sleep(1)
    # if token == '':
    #     popup_info = token_pop_up.get_missing_pop_up_info()
    # else:
    #     popup_info = token_pop_up.get_invalid_pop_up_info()
    # # check shown pop up
    # assert popup_info[0], 'Pop up is not shown'
    # # pop up title
    # assert popup_info[1] == pop_up_title, 'Incorrect pop up title'
    # # pop up content
    # assert popup_info[2] == pop_up_content, 'Incorrect pop up content'
