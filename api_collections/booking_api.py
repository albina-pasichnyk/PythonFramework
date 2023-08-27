# import allure

from utilities.api_utilities.base_api import BaseAPI
from api_collections.auth_api import AuthAPI


class BookingAPI(BaseAPI):

    def __init__(self, environment):
        super().__init__(environment)
        self.__booking_url = '/booking'

    # @allure.step
    def setup_token(self, environment):
        auth_api = AuthAPI(environment)
        response = auth_api.create_token()
        token = response.json()['token']
        self.token = token

    # @allure.step
    def get_booking_ids(self):
        return self.get(self.__booking_url)

    # @allure.step
    def get_booking_by_id(self, booking_id, headers=None):
        return self.get(f'{self.__booking_url}/{booking_id}', headers=headers)

    # @allure.step
    def create_booking(self, booking, headers=None):
        return self.post(self.__booking_url, booking.get_body_dict(), headers=headers)

    # @allure.step
    def update_booking(self, booking_id, booking, headers=None):
        return self.put(f'{self.__booking_url}/{booking_id}', booking.get_body_dict(), headers=headers)

    # @allure.step
    def partial_update_booking(self, booking_id, parameters: dict, headers=None):
        return self.patch(f'{self.__booking_url}/{booking_id}', parameters, headers=headers)

    # @allure.step
    def delete_booking(self, booking_id, headers=None):
        return self.delete(f'{self.__booking_url}/{booking_id}', headers=headers)
