import pytest
from utilities.data_randomizer import generate_random_user_name, generate_random_user_email


def test_notification_tooltip(go_to_notifications_page):
    notifications_page = go_to_notifications_page
    expected_tooltip_content = 'Add users to receive email notifications about Exalate errors that block synchronization.'
    actual_tooltip_content = notifications_page.get_tooltip_content()
    assert actual_tooltip_content == expected_tooltip_content, 'Incorrect tooltip'


def test_default_page_state(go_to_notifications_page):
    notifications_page = go_to_notifications_page
    expected_default_label = 'There are no users defined to receive Exalate error notifications.'
    actual_default_label = notifications_page.get_default_label()
    assert actual_default_label == expected_default_label, 'Incorrect default label'


@pytest.mark.regression
def test_cancel_creating_user(trigger_user_creation):
    user_creation = trigger_user_creation
    user_creation.cancel_creating_user()
    assert user_creation.is_default_label_displayed(), 'No default label'


@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(trigger_user_creation):
    user_creation = trigger_user_creation
    user_creation.set_user_name(
        generate_random_user_name()).set_user_email(generate_random_user_email()).create_user()
    assert user_creation.is_user_added(), 'User is not created'


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user(go_to_notifications_page):
    notifications_page = go_to_notifications_page
    notifications_page.delete_user()
    assert notifications_page.is_default_label_displayed(), 'User is not deleted'
