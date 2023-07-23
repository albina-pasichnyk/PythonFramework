from http import HTTPStatus

from api_collections.auth_api import AuthAPI


def test_create_token(environment):
    auth_api = AuthAPI(environment)
    response = auth_api.create_token()
    assert response.status_code == HTTPStatus.OK
    assert 'token' in response.json()


def test_failed_create_token(environment):
    invalid_credentials = {"username": "test", "password": "test_value"}
    auth_api = AuthAPI(environment)
    response = auth_api.create_token(invalid_credentials)
    assert response.status_code == HTTPStatus.OK
    assert 'reason' in response.json()
    assert response.json()['reason'] == "Bad credentials"
