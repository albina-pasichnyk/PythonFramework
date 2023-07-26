import allure

from utilities.api_utilities.base_api import BaseAPI


class AuthAPI(BaseAPI):
    def __init__(self, environment):
        super().__init__(environment)
        self.__auth_url = '/auth'
        self.__credentials = environment.credentials

    @allure.step
    def create_token(self, credentials=None):
        if credentials is None:
            credentials = self.__credentials
        response = self.post(self.__auth_url, credentials)
        return response
