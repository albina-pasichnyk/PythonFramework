import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_logout(login_to_app):
    sidebar = login_to_app
    sidebar.click_logout()
    assert sidebar.is_login_present(), 'Login sidebar item is not present'


def test_go_to_notifications(login_to_app):
    sidebar = login_to_app
    notifications_page = sidebar.go_to_notifications_page()
    assert notifications_page.is_page_header_present(), 'Page Header is not present'


def test_github_link(login_to_app):
    sidebar = login_to_app
    github_link = 'https://github.com/'
    actual_github_link = sidebar.get_github_link()
    assert actual_github_link == github_link


@pytest.mark.regression
def test_collapse_expand_sidebar(login_to_app):
    sidebar = login_to_app
    sidebar.hover_sidebar().collapse_sidebar()
    assert sidebar.is_expand_button_shown(), 'No expand button for sidebar'
    sidebar.hover_sidebar().expand_sidebar()
    assert sidebar.is_collapse_button_shown(), 'No collapse button for sidebar'


def test_go_to_license_details(login_to_app):
    sidebar = login_to_app
    license_details = sidebar.go_to_license_details_page()
    assert license_details.is_license_header_shown(), 'No license header is shown'
