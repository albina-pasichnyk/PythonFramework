from utilities.api_utilities.base_api import BaseAPI


class BookingAPI(BaseAPI):

    def __init__(self, environment):
        super().__init__(environment)
        self.__booking_url = '/booking'

    def setup_token(self, environment):
        from api_collections.auth_api import AuthAPI
        auth_api = AuthAPI(environment)
        response = auth_api.create_token()
        token = response.json()['token']
        self.token = token

    def get_booking_ids(self):
        return self.get(self.__booking_url)

    def get_booking_by_id(self, booking_id, headers=None):
        return self.get(f'{self.__booking_url}/{booking_id}', headers=headers)

    def create_booking(self, booking, headers=None):
        return self.post(self.__booking_url, booking.get_body_dict(), headers=headers)

    def update_booking(self, booking_id, booking, headers=None):
        return self.put(f'{self.__booking_url}/{booking_id}', booking.get_body_dict(), headers=headers)

    def partial_update_booking(self, booking_id, parameters: dict, headers=None):
        return self.patch(f'{self.__booking_url}/{booking_id}', parameters, headers=headers)

    def delete_booking(self, booking_id, headers=None):
        return self.delete(f'{self.__booking_url}/{booking_id}', headers=headers)
