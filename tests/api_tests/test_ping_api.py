from http import HTTPStatus

import allure

from api_collections.ping_api import PingAPI


@allure.feature('API Tests')
def test_health_check(environment):
    ping_api = PingAPI(environment)
    response = ping_api.health_check()
    assert response.status_code == HTTPStatus.CREATED, 'Incorrect status code'
