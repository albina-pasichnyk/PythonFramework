from http import HTTPStatus

from api_collections.ping_api import PingAPI


def test_health_check(environment):
    ping_api = PingAPI(environment)
    response = ping_api.health_check()
    assert response.status_code == HTTPStatus.CREATED, 'Incorrect status code'
