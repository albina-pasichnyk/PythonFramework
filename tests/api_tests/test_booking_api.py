from http import HTTPStatus

from api_collections.data_classes.booking_data import Booking


def test_get_booking_ids(booking_api):
    response = booking_api.get_booking_ids()
    assert response.status_code == HTTPStatus.OK, 'Incorrect status code'
    assert len(response.json()) > 0, 'Empty is is returned'
    assert 'bookingid' in response.json()[0], 'bookingis key is missing'


def test_get_booking_by_id_200(mock_booking, booking_api):
    booking_id = mock_booking.get_booking_id()
    response = booking_api.get_booking_by_id(booking_id)
    actual_booking = Booking(**response.json())
    assert response.status_code == HTTPStatus.OK, 'Incorrect status code'
    assert mock_booking.get_body_dict() == actual_booking.get_body_dict(), 'Incorrect response content'


def test_get_booking_by_id_404(booking_api):
    invalid_booking_id = 'qwerty'
    response = booking_api.get_booking_by_id(invalid_booking_id)
    assert response.status_code == HTTPStatus.NOT_FOUND, 'Incorrect status code'


def test_create_booking(mock_booking, booking_api):
    response = booking_api.create_booking(mock_booking)
    assert response.status_code == HTTPStatus.OK, 'Incorrect status code'
    created_booking = Booking(response.json()['bookingid'], **response.json()['booking'])
    assert mock_booking.get_body_dict() == created_booking.get_body_dict(), 'Incorrect body/content of created booking'


def test_update_booking(mock_booking, booking_auth_api):
    booking_to_update = mock_booking
    id_to_update = booking_to_update.get_booking_id()
    booking_to_update.firstname = 'Albina'
    response = booking_auth_api.update_booking(id_to_update, booking_to_update)
    assert response.status_code == HTTPStatus.OK, 'Incorrect status code'
    updated_booking = Booking(**response.json())
    assert updated_booking.firstname == booking_to_update.firstname, 'Incorrect update of booking'


def test_partial_update_booking(mock_booking, booking_auth_api):
    id_to_patch = mock_booking.get_booking_id()
    param_to_update = {"firstname": "James", "lastname": "Brown"}
    response = booking_auth_api.partial_update_booking(id_to_patch, param_to_update)
    assert response.status_code == HTTPStatus.OK, 'Incorrect status code'
    patched_booking = Booking(**response.json())
    assert patched_booking.firstname == param_to_update['firstname'], 'Incorrect partial update of booking'


def test_delete_booking(mock_booking, booking_auth_api):
    id_to_delete = mock_booking.get_booking_id()
    delete_response = booking_auth_api.delete_booking(id_to_delete)
    assert delete_response.status_code == HTTPStatus.CREATED, 'Incorrect status code'
    result_after_delete = booking_auth_api.get_booking_by_id(id_to_delete)
    assert result_after_delete.status_code == HTTPStatus.NOT_FOUND, 'Incorrect status code'
