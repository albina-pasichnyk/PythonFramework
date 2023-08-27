# import allure

from utilities.api_utilities.base_api import BaseAPI


class PingAPI(BaseAPI):
    def __init__(self, environment):
        super().__init__(environment)
        self.__ping_url = '/ping'

    # @allure.step
    def health_check(self):
        response = self.get(self.__ping_url)
        return response
