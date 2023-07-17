import pytest
from utilities.data_randomizer import generate_invalid_invitation_code


@pytest.mark.smoke
@pytest.mark.regression
def test_update_connection_status(go_to_connections_page):
    connections_page = go_to_connections_page
    # activate > deactivated
    initial_active_status = 'Active'
    initial_deactivated_status = 'Deactivated'
    current_status = connections_page.get_connection_status()
    if current_status == initial_active_status:
        deactivated_status = connections_page.deactivate_connection().get_connection_status()
        assert deactivated_status != current_status, 'Status is not updated'
    # deactivated > active
    elif current_status == initial_deactivated_status:
        reactivated_status = connections_page.activate_connection().get_connection_status()
        assert reactivated_status != current_status, 'Status is not updated'
    else:
        raise ValueError('Incorrect connection status')


def test_default_invitation_dialog(go_to_connections_page):
    connections_page = go_to_connections_page
    invitation_code_dialog = connections_page.invoke_accept_code_dialog_shown()
    # check content
    expected_description = 'Please paste the invitation code, received from your partner'
    expected_textarea_label = 'Enter the invitation code'
    actual_description = invitation_code_dialog.get_description()
    actual_textarea_label = invitation_code_dialog.get_textarea_label()
    assert actual_description == expected_description, 'Incorrect modal dialog description'
    assert actual_textarea_label == expected_textarea_label, 'Incorrect text area label'


@pytest.mark.regression
def test_invalid_invitation_code(go_to_connections_page):
    connections_page = go_to_connections_page
    invalid_invitation_code = generate_invalid_invitation_code()  # create random invalid invitation code
    invitation_code_dialog = connections_page.invoke_accept_code_dialog_shown()
    invitation_code_dialog.set_invitation_code(invalid_invitation_code).click_next_button()
    expected_pop_up_title = 'Invitation code is invalid'
    expected_pop_up_content = 'Please contact your partner to get the new invitation code'
    pop_up_info = connections_page.get_invalid_code_pop_up_info()
    # check shown pop up
    assert pop_up_info[0], 'Pop up is not shown'
    # pop up title
    assert pop_up_info[1] == expected_pop_up_title, 'Incorrect pop up title'
    # pop up content
    assert pop_up_info[2] == expected_pop_up_content, 'Incorrect pop up message'


@pytest.mark.regression
def test_footer_links(go_to_connections_page):
    connections_page = go_to_connections_page
    # check documentation link
    expected_documentation_link = 'https://docs.exalate.com/docs?utm_medium=product&utm_source=exalate_github'
    actual_documentation_link = connections_page.get_documentation_link()
    assert actual_documentation_link == expected_documentation_link, 'Incorrect Documentation link'
    # check eula link
    expected_eula_link = 'https://static.idalko.com/legal/eula-addons.pdf?utm_medium=product&utm_source=exalate_github'
    actual_eula_link = connections_page.get_eula_link()
    assert actual_eula_link == expected_eula_link, 'Incorrect EULA link'
    # check report a bug link
    expected_report_a_bug_link = 'https://support.idalko.com/servicedesk/customer/portal/8?utm_medium=product&utm_source=exalate_github'
    actual_report_a_bug_link = connections_page.get_report_a_bug_link()
    assert actual_report_a_bug_link == expected_report_a_bug_link, 'Incorrect Report a bug link'


def test_navigation_to_support(go_to_connections_page):
    connections_page = go_to_connections_page
    assert connections_page.is_support_opened(), 'Support header is not present'
