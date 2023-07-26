from http import HTTPStatus

import allure

from api_collections.auth_api import AuthAPI
from utilities.data_randomizer import generate_randon_login, generate_randon_password


@allure.feature('API Tests')
def test_create_token(environment):
    auth_api = AuthAPI(environment)
    response = auth_api.create_token()
    assert response.status_code == HTTPStatus.OK
    assert 'token' in response.json()


@allure.feature('API Tests')
def test_failed_create_token(environment):
    invalid_credentials = {"username": f"{generate_randon_login}", "password": f"{generate_randon_password}"}
    auth_api = AuthAPI(environment)
    response = auth_api.create_token(invalid_credentials)
    assert response.status_code == HTTPStatus.OK
    assert 'reason' in response.json()
    assert response.json()['reason'] == "Bad credentials"
